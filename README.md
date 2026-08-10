# Blaque Baux Bulk

**Defense and military — the primes, the suppliers, and the sector ETFs.**

Bulk is a member of the Blaque Baux family. The [core repo](https://github.com/Carter-Warrens/blaquebaux)
is the **engine and blueprint**. Bulk points that engine at defense, aerospace, and
military-adjacent names and ETFs — `ITA`, `XAR`, `PPA`, `DFEN`, and primes like `LMT`, `RTX`,
`NOC`, `GD`, `LHX`. It inherits the engine's governance wholesale.

> **Not investment advice.** Educational/research software. A single-sector book is
> concentrated by construction and exposed to policy/budget risk. Nothing here is validated.
> See [LICENSE](LICENSE).

```bash
git clone --recursive https://github.com/Carter-Warrens/blaquebaux-bulk.git
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

Nothing above is implemented or validated. This is the map, not the territory.

## Status
**Scaffold.** Engine wired as a submodule; strategy research not yet conducted.

## The Blaque Baux family
This repo is one sleeve of the **Blaque Baux** family — a single governed engine steered in
many directions. The [core repo](https://github.com/Carter-Warrens/blaquebaux) is the
base/blueprint and holds the [full family roster](https://github.com/Carter-Warrens/blaquebaux#the-blaque-baux-family).

## Layout
```
engine/     the Blaque Baux platform (git submodule → Carter-Warrens/blaquebaux)
research/   Path-A strategy sketches (to come)
live/       governed live drivers (once a sleeve graduates to paper A/B)
```

## License
[MIT](LICENSE). © 2026 Carter Warrens.
