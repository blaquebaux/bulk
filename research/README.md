# Blaque Baux Bulk — research

First-pass Path-A research on the defense / military sleeve. All sketches read Alpaca SIP
daily bars, are read-only, print their own results. 2016–2026; 8 pure defense primes
(LMT, RTX, NOC, GD, LHX, HII, TXT, LDOS) + ETFs (ITA, XAR).

```bash
export $(grep -v '^#' ~/.config/blaquebaux/alpaca.env | xargs)   # or source it
python research/bulk_1_structure.py       # where defense sits on the correlation spectrum
python research/bulk_2_tradeability.py    # the null: no edge, no hedge
```

## Scorecard

| # | Question | Result | Verdict |
|---|----------|--------|---------|
| 1 | Where does defense sit on the Basel↔Bio spectrum? | corr 0.52, 2.7 bets/8, 58% one-factor | ✅ moderate factor (useful diagnostic) |
| 2a | Do geopolitical/conflict shocks give next-day drift? | ITA jump +0.10%, oil→defense +0.02%, corr +0.00 | ❌ priced instantly |
| 2b | Does trend+vol-target help? | ITA +0.75→+0.44 (whipsaws) | ❌ trend hurts |
| 2c | Is defense a risk-off hedge? | corr 0.74/β 0.96 to SPY; falls as much on worst days | ❌ high-beta industrials |

## The synthesis

**Bulk is a null for a systematic sleeve, but it contributes one genuinely useful diagnostic.**

- **#1 (the useful part):** defense fills the *middle* of the family's correlation spectrum.
  Avg pairwise correlation 0.52, ~2.7 independent bets from 8 primes, 58% one factor — more
  diversified than prudentially-homogenized banks (Basel, 81%), less than idiosyncratic
  biotech (Bio, 36%). A **moderate factor**: every prime rides the same demand driver (the
  defense budget / geopolitics), but distinct program mixes (aircraft vs ships vs missiles vs
  IT) keep them from collapsing to one bet. Practical takeaway: size a defense basket to ~3
  bets, not 8.

  > The correlation law now has three calibration points: **Bio 36% → Bulk 58% → Basel 81%**
  > one-factor share, ranked exactly by how forced/shared the common exposure is.

- **#2 (the null):** none of the tradeable angles survive.
  - **Event follow-through is priced instantly** — a defense jump or an oil spike (geopolitical
    proxy) gives ~0 next-day drift; corr(oil today, defense tomorrow) is +0.00. Unlike the
    crude→refiner lead-lag (+0.18), the geopolitics→defense channel is same-day. The family
    "priced instantly" law holds.
  - **Trend+vol-target *hurts*** — defense whipsaws, so the managed version underperforms
    buy&hold (ITA +0.75 → +0.44). No systematic trend edge.
  - **Not a hedge** — defense is high-beta industrials (corr 0.74, beta 0.96 to SPY, 0.88 to
    XLI) and falls just as hard on the market's worst days (−2.71% vs −2.70%). The "defense
    spikes on fear" intuition does not survive: it's equity beta with a narrative.

**Verdict:** defense is a fine buy-and-hold sector (~0.75 Sharpe) but offers no systematic
alpha, no shock drift, and no diversification. Not a sleeve. Its value to the family is the
diagnostic — a third anchor on the regulation/correlation spectrum.

## Files
- `_bulk_common.py` — shared helpers + the defense primes.
- `bulk_1_structure.py` — defense on the Basel↔Bio correlation spectrum.
- `bulk_2_tradeability.py` — event follow-through, trend, and hedge — all rejected.
