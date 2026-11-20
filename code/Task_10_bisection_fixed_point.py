import numpy as np
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt

def heat_balance(T):
    return T - 25 - 10*np.exp(-T/20)

# Original case
solution = root_scalar(heat_balance, bracket=[20, 40], method="bisect", xtol=1e-10)
def g(T):
    return 25 + 10*np.exp(-T/20)
T = 30.0
history = [T]
for _ in range(100):
    T_new = g(T); history.append(T_new)
    if abs(T_new-T) < 1e-10: break
    T = T_new
print("ORIGINAL CASE: HEAT BALANCE")
print(f"Bisection root: {solution.root:.6f} C")
print(f"Fixed-point estimate: {history[-1]:.6f} C")
print("Fixed-point iterations:", len(history)-1)
temps = np.linspace(20, 40, 300)
plt.plot(temps, heat_balance(temps)); plt.axhline(0, linewidth=.8)
plt.axvline(solution.root, linestyle="--")
plt.xlabel("Temperature (C)"); plt.ylabel("Heat-balance function")
plt.title("Equilibrium temperature"); plt.grid(True); plt.show()

# Parameter change: increase constant heat-loss offset from 25 to 27
def changed_balance(T):
    return T - 27 - 10*np.exp(-T/20)
changed = root_scalar(changed_balance, bracket=[20, 45], method="bisect")
print("\nCHANGED PARAMETER: OFFSET = 27")
print(f"New equilibrium: {changed.root:.6f} C")

# Related case: solve a simple equipment threshold model f(x)=x-40-5exp(-x/15)
def equipment_balance(x):
    return x - 40 - 5*np.exp(-x/15)
related = root_scalar(equipment_balance, bracket=[40, 50], method="bisect")
print("\nRELATED CASE: EQUIPMENT OPERATING THRESHOLD")
print(f"Estimated operating threshold: {related.root:.4f} units")
