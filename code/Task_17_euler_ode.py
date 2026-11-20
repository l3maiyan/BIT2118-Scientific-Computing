import numpy as np
import matplotlib.pyplot as plt

T_ambient = 25.0
T_initial = 90.0
k = 0.12
h = 1.0
end_time = 30.0
def cooling_rate(T):
    return -k*(T-T_ambient)
def run_euler(step):
    time = np.arange(0, end_time+step, step)
    temperature = np.zeros_like(time)
    temperature[0] = T_initial
    for i in range(len(time)-1):
        temperature[i+1] = temperature[i] + step*cooling_rate(temperature[i])
    return time, temperature
time, temperature = run_euler(h)
exact = T_ambient + (T_initial-T_ambient)*np.exp(-k*time)
print("ORIGINAL CASE: EULER COOLING MODEL")
print(f"Euler temperature after 30 min: {temperature[-1]:.2f} C")
print(f"Exact temperature after 30 min: {exact[-1]:.2f} C")
print(f"Absolute error: {abs(temperature[-1]-exact[-1]):.4f} C")
plt.plot(time, temperature, marker="o", label="Euler")
plt.plot(time, exact, label="Exact solution")
plt.xlabel("Time (minutes)"); plt.ylabel("Temperature (C)")
plt.title("Cooling of a hot object"); plt.legend(); plt.grid(True); plt.show()

# Parameter change: reduce step size from 1 minute to 0.5 minute
t_small, temp_small = run_euler(0.5)
print("\nCHANGED PARAMETER: STEP SIZE = 0.5 MIN")
print(f"New Euler temperature after 30 min: {temp_small[-1]:.2f} C")
print(f"New absolute error: {abs(temp_small[-1]-(T_ambient+(T_initial-T_ambient)*np.exp(-k*30))):.4f} C")

# Related case: simple population growth dP/dt = rP
population = 1000.0; growth_rate = 0.03; step = 1.0
for _ in range(10):
    population += step*growth_rate*population
print("\nRELATED CASE: POPULATION GROWTH")
print(f"Estimated population after 10 years: {population:.0f}")
