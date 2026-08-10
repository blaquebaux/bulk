#!/usr/bin/python3
# =============================================================================
# bulk_2_tradeability.py — BLAQUE BAUX BULK #2 (the null: no systematic edge, no hedge).
#
# Three things a defense sleeve might offer, all rejected:
#   (a) EVENT FOLLOW-THROUGH — a conflict/budget/geopolitical shock might give next-day
#       drift. It does not: defense reacts SAME-DAY. After an ITA jump, next-day excess ~0;
#       after an oil spike (geopolitical proxy), defense next-day ~0; corr(oil_t, ITA_{t+1})
#       ~0. Priced instantly — the family law again (Blunt #3, the correlation study).
#   (b) TREND — trend+vol-target HURTS defense (it whipsaws), unlike QQQ (Broad). Buy&hold
#       the sector is actually the better Sharpe; there is no systematic trend edge.
#   (c) HEDGE — defense is NOT a risk-off hedge. corr 0.74 / beta 0.96 to SPY, and on the
#       market's worst days it falls just as much. It is high-beta industrials with a
#       geopolitical narrative, not a diversifier.
#
# RESULTS AS TESTED (2016-2026):
#   (a) ITA jump -> next-day excess +0.10% | oil>3% -> defense next-day +0.02% | corr +0.00
#   (b) ITA buy&hold +0.75/-51% vs trend+vt +0.44/-30% ; XAR +0.78/-46% vs +0.51/-17%
#   (c) corr(ITA,SPY) 0.74, beta 0.96, corr(ITA,XLI) 0.88 ; worst-5% SPY -2.70% vs ITA -2.71%
# Read-only.
# =============================================================================
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _bulk_common import panel, metrics, beta, trend_vt

u, ds, M = panel(["ITA", "XAR", "SPY", "XLI", "USO"]); R = M[1:] / M[:-1] - 1; i = {s: u.index(s) for s in u}
ita, spy, uso, xli = R[:, i["ITA"]], R[:, i["SPY"]], R[:, i["USO"]], R[:, i["XLI"]]
print("=" * 72, "\nBULK #2 — is defense tradeable / a hedge? (all rejected)\n" + "=" * 72)
print("(a) event follow-through — priced instantly:")
big = ita > 0.015; fwd = [ita[t + 1] - spy[t + 1] for t in range(len(ita) - 1) if big[t]]
oil = uso > 0.03; fo = [ita[t + 1] - spy[t + 1] for t in range(len(uso) - 1) if oil[t]]
print(f"    ITA up>1.5% -> next-day excess {np.mean(fwd)*100:+.2f}% (n={len(fwd)}) | oil>3% -> defense next-day {np.mean(fo)*100:+.2f}% | corr(oil_t,ITA_t+1) {np.corrcoef(uso[:-1],ita[1:])[0,1]:+.2f}")
print("\n(b) trend hurts (defense whipsaws):")
for s, r in [("ITA", ita), ("XAR", R[:, i["XAR"]])]:
    bh = metrics(r); tv = metrics(trend_vt(r))
    print(f"    {s}: buy&hold {bh['sh']:+.2f}/{bh['dd']*100:.0f}%DD  vs  trend+vt {tv['sh']:+.2f}/{tv['dd']*100:.0f}%DD")
print("\n(c) not a hedge — high-beta industrials:")
print(f"    corr(ITA,SPY) {np.corrcoef(ita,spy)[0,1]:.2f}  beta {beta(ita,spy):.2f}  corr(ITA,XLI) {np.corrcoef(ita,xli)[0,1]:.2f}")
w = spy < np.nanpercentile(spy, 5)
print(f"    worst-5% SPY days: SPY {np.mean(spy[w])*100:.2f}% vs ITA {np.mean(ita[w])*100:.2f}%  (falls just as much)")
print("\nVERDICT: null. No next-day shock drift (priced instantly), no trend edge (whipsaws),")
print("no hedge value (high-beta industrials). Defense is a fine buy&hold sector but offers")
print("no systematic alpha and no diversification — just equity beta with a narrative.")
