# Blaque Baux Bulk

**Defense and military — the primes, the suppliers, and the sector ETFs.**

Bulk is a member of the Blaque Baux family. The [core repo](https://github.com/blaquebaux/base)
is the **engine and blueprint**. Bulk points that engine at defense, aerospace, and
military-adjacent names and ETFs — `ITA`, `XAR`, `PPA`, `DFEN`, and primes like `LMT`, `RTX`,
`NOC`, `GD`, `LHX`. It inherits the engine's governance wholesale.

> **Not investment advice.** Educational/research software. A single-sector book is
> concentrated by construction and exposed to policy/budget risk. Nothing here is validated.
> See [LICENSE](LICENSE).

```bash
git clone --recursive https://github.com/blaquebaux/bulk.git
julia --project=engine -e 'using Pkg; Pkg.instantiate()'   # one-time engine setup
```

## The thesis

Defense has two features the family already knows how to test. First, it is **event-driven**:
conflict and budget headlines move the whole sector at once — the tradeable question (as with
Blunt's crude→refiner) is whether there is next-day *follow-through* or whether it is priced
instantly. Second, it is a **concentrated, correlated basket** — Boom's crowding lesson applies:
the primes move largely as one factor, so "diversification" across five defense names is mostly
an illusion, and sizing must reflect that.

## Research plan (Path A — not yet built)

- **Sector trend / momentum** — ITA/XAR vol-targeted; the honest baseline for a defense tilt.
- **Event follow-through** — does a conflict/budget shock give next-day drift in the sector, or
  is it priced same-day (the Blunt/correlation test, applied to defense)?
- **Crowding check** — effective number of bets across the primes (Boom's participation-ratio
  method); size to the real factor count, not the name count.
- **Backlog / earnings** — order-backlog and earnings-reaction drift (needs a fundamentals feed).

## Research — first pass done

Full detail in [`research/README.md`](research/README.md). The scorecard:

| # | Question | Verdict |
|---|----------|---------|
| 1 | Where on the Basel↔Bio correlation spectrum? | ✅ **moderate factor** — corr 0.52, 58% one-factor, ~2.7 bets/8 |
| 2a | Do geopolitical shocks give next-day drift? | ❌ priced instantly (corr +0.00) |
| 2b | Does trend+vol-target help? | ❌ no — defense whipsaws (+0.75→+0.44) |
| 2c | Is defense a risk-off hedge? | ❌ no — high-beta industrials (β 0.96, falls as much on worst days) |

**The synthesis:** Bulk is a **null** for a systematic sleeve, with one useful diagnostic.
Defense fills the *middle* of the family's correlation spectrum — **Bio 36% → Bulk 58% →
Basel 81%** one-factor share — a moderate factor bound by a shared demand driver (defense
budget/geopolitics) but kept distinct by program mix (~3 real bets, not 8). But none of the
tradeable angles survive: geopolitical shocks are priced instantly (no drift, unlike
crude→refiner), trend-following whipsaws, and defense is high-beta industrials (corr 0.74 /
β 0.96 to SPY) that falls just as hard on the worst days — *not* a hedge. A fine buy&hold
sector, no systematic alpha, no diversification.

## Status
**Research: first pass complete — null (diagnostic only)** (`research/`). No systematic edge;
defense is equity beta with a narrative. No live driver. Nothing validated to the spine's bar.

## About Blaque Baux

**Blaque Baux** is a quantitative research initiative and a subsidiary of **[Carter Warrens](https://carterwarrens.com)**.
[**BlaqueBaux.com**](https://blaquebaux.com) is the home for the work; the code lives here on GitHub — open to
study, test, and build bespoke strategies on top of.

Anyone can point an AI at a market. The edge is **understanding what the data actually says — and turning it
into something you can act on.** We test relentlessly and put most of it *on the record as rejected, with the
reason*; what survives is built, governed, and validated before it is ever called real. That combination —
honest research, reproducible evidence, and execution you can trust — is why Carter Warrens leads on
**strategy and implementation**, not merely uses the tools everyone now has.

## The Blaque Baux family
This repo is one sleeve of the **Blaque Baux** family — a single governed engine steered in
many directions. The [core repo](https://github.com/blaquebaux/base) is the
base/blueprint and holds the [full family roster](https://github.com/blaquebaux/base#the-blaquebaux-family).

## Layout
```
engine/     the Blaque Baux platform (git submodule → blaquebaux/base)
research/   two Path-A sketches (correlation spectrum, tradeability null) + scorecard
live/       governed live drivers (once a sleeve graduates to paper A/B)
```

## License
[MIT](LICENSE). © 2026 Carter Warrens.
