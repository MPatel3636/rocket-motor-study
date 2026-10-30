"""
Nozzle expansion study: thrust coefficient (Cf) vs expansion ratio
at several ambient pressures (altitudes).

"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

# INPUTS 
gamma = 1.13      # ratio of specific heats of the exhaust gas
Pc = 3.4e6        # chamber pressure
cstar = 912.0     # characteristic velocity
altitudes = {"Sea level": 101325, "5 km": 54048, "10 km": 26436, "Vacuum": 0}

g = 9.8


def exit_pressure_ratio(eps, k):
    """Pe/Pc for a given expansion ratio eps = Ae/At (supersonic branch)."""
    def f(r):
        a = (2 / (k + 1)) ** (1 / (k - 1)) * (1 / r) ** (1 / k)
        b = np.sqrt((k + 1) / (k - 1) * (1 - r ** ((k - 1) / k)))
        return a / b - eps
    r_crit = (2 / (k + 1)) ** (k / (k - 1))
    return brentq(f, 1e-9, r_crit - 1e-9)


def thrust_coeff(eps, Pa, k, Pc):
    """Ideal thrust coefficient including the pressure-mismatch term."""
    r = exit_pressure_ratio(eps, k)
    momentum = np.sqrt(2 * k**2 / (k - 1)
                       * (2 / (k + 1)) ** ((k + 1) / (k - 1))
                       * (1 - r ** ((k - 1) / k)))
    return momentum + (r - Pa / Pc) * eps


eps_range = np.linspace(1.5, 30, 200)

print(f"{'Condition':<11}{'Best exp. ratio':>16}{'Best Cf':>9}{'Ideal Isp (s)':>15}{'Cf at ER 6':>12}")
plt.figure(figsize=(8, 5))
for name, Pa in altitudes.items():
    cf = np.array([thrust_coeff(e, Pa, gamma, Pc) for e in eps_range])
    i = cf.argmax()
    print(f"{name:<11}{eps_range[i]:>16.1f}{cf[i]:>9.3f}{cf[i] * cstar / g:>15.1f}"
          f"{thrust_coeff(6.0, Pa, gamma, Pc):>12.3f}")
    line, = plt.plot(eps_range, cf, label=name)
    plt.plot(eps_range[i], cf[i], "o", color=line.get_color())

plt.xlabel("Nozzle expansion ratio (Ae/At)")
plt.ylabel("Ideal thrust coefficient, Cf")
plt.title("Nozzle expansion study (dots = best expansion ratio in the range)")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("nozzle_study.png", dpi=150)
