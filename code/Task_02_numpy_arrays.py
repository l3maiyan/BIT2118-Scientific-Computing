import numpy as np

# Original case: 24 hourly weather-station temperatures (degrees Celsius)
temperatures_c = np.array([
    18.5, 18.0, 17.8, 17.5, 17.9, 19.0, 21.5, 23.8,
    25.6, 27.1, 28.3, 29.0, 29.4, 29.1, 28.5, 27.6,
    26.2, 24.8, 23.4, 22.1, 21.0, 20.2, 19.6, 19.0
])
print("ORIGINAL CASE")
print(f"Mean: {np.mean(temperatures_c):.2f} C")
print(f"Minimum: {np.min(temperatures_c):.2f} C")
print(f"Maximum: {np.max(temperatures_c):.2f} C")
print("First six readings in Fahrenheit:", 1.8 * temperatures_c[:6] + 32)

# Parameter change: use a hotter set of readings (+2 C)
changed_temperatures = temperatures_c + 2
print("\nCHANGED INPUT (+2 C)")
print(f"New mean: {np.mean(changed_temperatures):.2f} C")

# Related real-world case: monitor water temperatures in an aquarium
water_c = np.array([24.0, 24.5, 25.0, 25.5, 26.0])
print("\nRELATED CASE: AQUARIUM WATER")
print(f"Average water temperature: {water_c.mean():.2f} C")
print(f"Safe-range check (assumed 24-26 C): {np.all((water_c >= 24) & (water_c <= 26))}")
