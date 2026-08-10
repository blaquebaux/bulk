#!/usr/bin/python3
# =============================================================================
# _bulk_common.py — shared helpers for the Blaque Baux Bulk (defense) sketches.
# Alpaca SIP daily bars; reads ALPACA_KEY_ID / ALPACA_SECRET_KEY from env. Read-only.
# =============================================================================
import os, json, urllib.request, math
import numpy as np

H = {"APCA-API-KEY-ID": os.environ["ALPACA_KEY_ID"], "APCA-API-SECRET-KEY": os.environ["ALPACA_SECRET_KEY"]}
START, END = "2016-01-01", "2026-08-01"
_cache = {}

PRIMES = ["LMT", "RTX", "NOC", "GD", "LHX", "HII", "TXT", "LDOS"]   # pure defense primes

def bars(s):
    if s in _cache: return _cache[s]
    u = (f"https://data.alpaca.markets/v2/stocks/bars?symbols={s}&timeframe=1Day"
         f"&start={START}&end={END}&adjustment=all&feed=sip&limit=10000")
    b = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=H), timeout=40)).get("bars", {}).get(s, [])
    _cache[s] = {x["t"][:10]: x for x in b}
    return _cache[s]

def panel(syms, field="c"):
    D = {s: bars(s) for s in syms}; D = {s: v for s, v in D.items() if len(v) > 500}
    u = list(D); ds = sorted(set.intersection(*[set(v) for v in D.values()]))
    return u, ds, np.array([[D[s][d][field] for s in u] for d in ds], float)

def metrics(r, ppy=252):
    r = np.asarray(r, float); r = r[np.isfinite(r)]
    if len(r) < 30 or r.std() == 0: return dict(sh=float('nan'), cagr=float('nan'), dd=float('nan'))
    cum = np.cumprod(1 + r)
    return dict(sh=r.mean() / r.std() * math.sqrt(ppy), cagr=cum[-1] ** (ppy / len(r)) - 1,
                dd=(cum / np.maximum.accumulate(cum) - 1).min())

def eff_bets(Rm):
    C = np.corrcoef(Rm.T); lam = np.linalg.eigvalsh(C)
    return C[np.triu_indices(len(C), 1)].mean(), (lam.sum() ** 2) / (lam ** 2).sum(), 100 * lam.max() / lam.sum()

def beta(y, x):
    m = np.isfinite(y) & np.isfinite(x); y, x = y[m], x[m]
    return np.cov(y, x)[0, 1] / np.var(x) if len(y) > 30 and np.var(x) > 0 else float('nan')

def ewma_vol(r, hl=30):
    lam = 0.5 ** (1 / hl); v = r[0] ** 2; o = np.empty(len(r))
    for t in range(len(r)):
        v = r[t] ** 2 if t == 0 else lam * v + (1 - lam) * r[t] ** 2
        o[t] = math.sqrt(max(v, 1e-12)) * math.sqrt(252)
    return o

def trend_vt(r, tgt=0.15, cap=2.0):
    lvl = np.cumprod(1 + r); sig = np.full(len(r), np.nan)
    for t in range(120, len(r)):
        sig[t] = max(0.0, np.mean([np.sign(lvl[t] / lvl[t - h] - 1) for h in (30, 60, 120)]))
    sc = np.clip(tgt / np.maximum(ewma_vol(r), 1e-6), 0, cap)
    return (sig * sc)[:-1] * r[1:]
