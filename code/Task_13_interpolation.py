import numpy as np
from scipy.interpolate import interp1d, CubicSpline
import matplotlib.pyplot as plt

hours = np.array([8, 9, 10, 11, 12, 13, 14], dtype=float)
temperature = np.array([18.0, 20.0, 22.5, 24.0, 25.0, 25.5, 25.0])
linear = interp1d(hours, temperature, kind="linear")
cubic = CubicSpline(hours, temperature)
ten_minute_times = np.arange(8, 14 + 1/6, 1/6)
linear_estimates = linear(ten_minute_times)
cubic_estimates = cubic(ten_minute_times)
print("ORIGINAL CASE: HOURLY SENSOR INTERPOLATION")
print(f"Linear estimate at 10:30: {float(linear(10.5)):.2f} C")
print(f"Cubic estimate at 10:30: {float(cubic(10.5)):.2f} C")
plt.scatter(hours, temperature, label="Hourly measurements")
plt.plot(ten_minute_times, linear_estimates, label="Linear")
plt.plot(ten_minute_times, cubic_estimates, label="Cubic spline")
plt.xlabel("Hour of day"); plt.ylabel("Temperature (C)")
plt.title("Temperature interpolation"); plt.legend(); plt.grid(True); plt.show()

# Parameter change: alter the 11:00 reading from 24 to 26 C
changed_temp = temperature.copy(); changed_temp[3] = 26.0
changed_linear = interp1d(hours, changed_temp, kind="linear")
print("\nCHANGED INPUT: 11:00 READING = 26 C")
print(f"New 10:30 estimate: {float(changed_linear(10.5)):.2f} C")

# Related case: estimate water level between two measured times
water_hours = np.array([0, 2, 4, 6], dtype=float)
water_cm = np.array([40, 44, 51, 55], dtype=float)
water_interp = interp1d(water_hours, water_cm)
print("\nRELATED CASE: WATER-LEVEL SENSOR")
print(f"Estimated level at hour 3: {float(water_interp(3)):.1f} cm")
