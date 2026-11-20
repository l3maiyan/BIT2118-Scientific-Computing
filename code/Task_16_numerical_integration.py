import numpy as np
from scipy.integrate import simpson

time_hours = np.array([0, 2, 4, 6, 8, 10, 12], dtype=float)
power_kw = np.array([0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9])
trapezoid = np.trapezoid(power_kw, time_hours)
simpson_value = simpson(power_kw, x=time_hours)
print("ORIGINAL CASE: SMART-METER ENERGY")
print(f"Trapezoidal estimate: {trapezoid:.3f} kWh")
print(f"Simpson estimate: {simpson_value:.3f} kWh")
print(f"Difference: {abs(simpson_value-trapezoid):.3f} kWh")

# Parameter change: increase all power readings by 10 percent
changed_power = power_kw * 1.10
print("\nCHANGED INPUT: POWER READINGS +10%")
print(f"New Simpson energy: {simpson(changed_power, x=time_hours):.3f} kWh")

# Related case: estimate total water delivered from a changing flow rate
time_minutes = np.array([0, 5, 10, 15, 20, 25, 30], dtype=float)
flow_lpm = np.array([2, 3, 5, 6, 5, 4, 2], dtype=float)
volume = simpson(flow_lpm, x=time_minutes)
print("\nRELATED CASE: WATER DELIVERY")
print(f"Estimated water delivered: {volume:.2f} litres")
