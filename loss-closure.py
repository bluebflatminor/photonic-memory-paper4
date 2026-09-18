#!/usr/bin/env python3
"""
Loss-closure computation for Paper 4 v10.12, §2.2a.

Residual absorption of graphene in the Pauli-blocked state, and the array size
it permits under a fixed per-optical-path insertion loss budget.

Key result: with omega*tau >> 1, Re(sigma_intra) = e^3 vF^2 / (pi hbar^2 w^2 mu).
The Fermi level cancels exactly (tau = mu*m*/e, m* = E_F/vF^2), so residual
transparent-state loss depends on mobility alone. Normalised to sigma_0 = e^2/4hbar
this gives the exchange rate between weight dynamic range and insertion loss,
which is independent of interaction length and of graphene layer count.

This is a FLOOR. Measured devices (arXiv:2506.03281) sit ~95x above it.
Not checked by any second instrument -- see banner item 36.
"""
import numpy as np

e    = 1.602176634e-19
hbar = 1.054571817e-34
c    = 2.99792458e8
vF   = 1.0e6
lam  = 1550e-9
w    = 2*np.pi*c/lam
sig0 = e**2/(4*hbar)

def fom(mu_cm2):
    """dB of weight dynamic range per dB of transparent-state insertion loss."""
    return np.pi*hbar*w**2*(mu_cm2*1e-4)/(4*e*vF**2)

def max_N(mu_cm2, R_dB, budget_dB=0.5):
    """Largest N x N tile closing the per-path budget at required range R."""
    return budget_dB*fom(mu_cm2)/R_dB

def mu_required(N, R_dB, budget_dB=0.5):
    """Mobility (cm^2/Vs) needed to close the budget at array size N."""
    need = R_dB*N/budget_dB
    return need*4*e*vF**2/(np.pi*hbar*w**2)*1e4

# Required weight dynamic range is a BRACKET, not a value (banner item 32):
#   7 dB  - low end, with retraining against hardware range   [51]
#  10 dB  - comfortable weighting range                        [51]
#  12 dB  - ~4 bits under a 3dB/bit slope rule                 [52] (T3, truncated)
#  18 dB  - ~6 bits, upper end of typical photonic precision   [50]
BRACKET = (7, 10, 12, 18)
CEILING = (8000, 10000)   # F2 theoretical ceiling, graphene on diamond [15]

if __name__ == "__main__":
    print(f"omega = {w:.4e} rad/s   sigma_0 = {sig0:.4e} S\n")

    print("Largest N closing a 0.5 dB per-path budget (Drude floor only)")
    print(f"{'mu (cm2/Vs)':>13}" + "".join(f"{str(r)+' dB':>10}" for r in BRACKET))
    for mu in (140, 1644, 2750, 3000, 5000, 8000, 10000):
        print(f"{mu:>13}" + "".join(f"{max_N(mu,r):>10.1f}" for r in BRACKET))

    print("\nMobility required (cm2/Vs), 0.5 dB budget")
    print(f"{'R (dB)':>8}{'N=16':>12}{'N=64':>12}")
    for r in BRACKET:
        m16, m64 = mu_required(16,r), mu_required(64,r)
        f16 = "" if m16 <= CEILING[1] else "  ABOVE CEILING"
        f64 = "" if m64 <= CEILING[1] else "  ABOVE CEILING"
        print(f"{r:>8}{m16:>12,.0f}{m64:>12,.0f}{f64}")

    print(f"\nF2 theoretical ceiling: {CEILING[0]:,}-{CEILING[1]:,} cm2/Vs")
    print("N=64 is unreachable across the entire bracket; N=16 is reachable across all of it.")
