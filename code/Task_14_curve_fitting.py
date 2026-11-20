import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

users = np.array([50, 100, 150, 200, 250, 300, 350], dtype=float)
response_ms = np.array([82, 95, 115, 145, 185, 238, 305], dtype=float)
def model(x, a, b, c):
    return a*x**2 + b*x + c
params, covariance = curve_fit(model, users, response_ms)
a, b, c = params
predicted = model(users, a, b, c)
rmse = np.sqrt(np.mean((response_ms-predicted)**2))
print("ORIGINAL CASE: SERVER RESPONSE-TIME CURVE")
print(f"Fitted model: y = {a:.6f}x^2 + {b:.4f}x + {c:.2f}")
print(f"RMSE: {rmse:.2f} ms")
print(f"Predicted response at 400 users: {model(400,*params):.2f} ms")
x_plot = np.linspace(users.min(), 400, 300)
plt.scatter(users, response_ms, label="Measurements")
plt.plot(x_plot, model(x_plot,*params), label="Fitted curve")
plt.xlabel("Concurrent users"); plt.ylabel("Response time (ms)")
plt.title("Server response-time curve fitting"); plt.legend(); plt.grid(True); plt.show()

# Parameter change: add 20 ms to each measured response time
changed_response = response_ms + 20
changed_params, _ = curve_fit(model, users, changed_response)
print("\nCHANGED INPUT: ALL RESPONSE TIMES +20 MS")
print(f"New prediction at 400 users: {model(400,*changed_params):.2f} ms")

# Related case: fit a quadratic model to machine energy use at different production levels
units = np.array([10, 20, 30, 40, 50], dtype=float)
energy = np.array([15, 28, 45, 68, 96], dtype=float)
energy_params, _ = curve_fit(model, units, energy)
print("\nRELATED CASE: MACHINE ENERGY MODEL")
print(f"Predicted energy at 60 units: {model(60,*energy_params):.2f} units")
