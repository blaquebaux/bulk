#!/usr/bin/python3
# =============================================================================
# bulk_1_structure.py — BLAQUE BAUX BULK #1 (the useful diagnostic).
#
# Where does defense sit on the family's correlation spectrum? The base's law: correlation
# is proportional to shared forced exposure. Banks (Basel) are homogenized into one factor;
# biotech (Bio) is idiosyncratic. Defense is IN BETWEEN — a "moderate factor": every prime
# rides the same demand driver (the defense budget / geopolitics), but each has a distinct
# program mix (aircraft vs ships vs missiles vs IT), so they do not collapse to one factor.
#
# RESULTS AS TESTED (8 primes, 2016-2026):
#   DEFENSE: avg corr 0.52 | eff-bets 2.7/8 | 1-factor 58% | dispersion 0.90%/d
#   spectrum: Bio 36% one-factor  <  DEFENSE 58%  <  Basel 81%
# Read-only.
# =============================================================================
import os, sys
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _bulk_common import PRIMES, panel, eff_bets

u, ds, M = panel(PRIMES); R = M[1:] / M[:-1] - 1
c, e, f = eff_bets(R); disp = np.nanmean(np.nanstd(R, 1))
print("=" * 72, "\nBULK #1 — defense on the Basel<->Bio correlation spectrum\n" + "=" * 72)
print(f"  DEFENSE primes ({len(PRIMES)}): avg corr {c:.2f}  eff-bets {e:.1f}/{len(PRIMES)}  1-factor {f:.0f}%  dispersion {disp*100:.2f}%/d")
print(f"  reference:  Bio biotech 0.32 / 6.3 bets / 36% one-factor  (idiosyncratic)")
print(f"              Basel banks 0.80 / 1.5 bets / 81% one-factor  (prudentially homogenized)")
print("\nVERDICT: defense is a MODERATE factor (58% one-factor, ~2.7 independent bets) — between")
print("biotech's idiosyncrasy and banks' homogeneity. A shared demand driver binds the primes,")
print("but distinct program mixes keep them from collapsing to one bet. Size to ~3 bets, not 8.")
