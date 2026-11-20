import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Original case: RC circuit charging
Vs, R, C, V0 = 5.0, 1000.0, 0.001, 0.0
def rc_circuit(t, V):
    return [(Vs-V[0])/(R*C)]
t_eval = np.linspace(0, 5, 200)
solution = solve_ivp(rc_circuit, (0, 5), [V0], t_eval=t_eval, rtol=1e-9, atol=1e-11)
exact = Vs*(1-np.exp(-solution.t/(R*C)))
print("ORIGINAL CASE: RC CIRCUIT")
print("Solver success:", solution.success)
print(f"Voltage at 5 seconds: {solution.y[0,-1]:.4f} V")
print(f"Maximum error: {np.max(np.abs(solution.y[0]-exact)):.3e} V")
plt.plot(solution.t, solution.y[0], label="solve_ivp")
plt.plot(solution.t, exact, "--", label="Exact")
plt.xlabel("Time (s)"); plt.ylabel("Capacitor voltage (V)")
plt.title("RC circuit charging"); plt.legend(); plt.grid(True); plt.show()

# Parameter change: double the resistance
R_changed = 2000.0
def slower_rc(t, V):
    return [(Vs-V[0])/(R_changed*C)]
changed = solve_ivp(slower_rc, (0, 5), [V0], t_eval=[5])
print("\nCHANGED PARAMETER: RESISTANCE = 2000 OHMS")
print(f"Voltage after 5 seconds: {changed.y[0,-1]:.4f} V")

# Related case: medicine concentration decay (assumed first-order decay)
def concentration_decay(t, amount):
    return [-0.25*amount[0]]
related = solve_ivp(concentration_decay, (0, 8), [100.0], t_eval=[0, 2, 4, 6, 8])
print("\nRELATED CASE: FIRST-ORDER CONCENTRATION DECAY")
print("Amount at selected hours:", np.round(related.y[0], 2))
