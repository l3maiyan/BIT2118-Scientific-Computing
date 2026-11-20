import numpy as np
import matplotlib.pyplot as plt

time = np.array([0, 1, 2, 3, 4, 5, 6], dtype=float)
position = np.array([0.0, 4.8, 10.2, 16.1, 22.7, 30.0, 38.0])
def estimate_speed(t, x):
    speed = np.zeros_like(x)
    speed[0] = (x[1]-x[0])/(t[1]-t[0])
    for i in range(1, len(t)-1):
        speed[i] = (x[i+1]-x[i-1])/(t[i+1]-t[i-1])
    speed[-1] = (x[-1]-x[-2])/(t[-1]-t[-2])
    return speed
speed = estimate_speed(time, position)
print("ORIGINAL CASE: GPS SPEED ESTIMATION")
for t, x, v in zip(time, position, speed):
    print(f"t={t:.0f}s, position={x:.1f}m, estimated speed={v:.2f}m/s")
plt.plot(time, speed, marker="o")
plt.xlabel("Time (s)"); plt.ylabel("Estimated speed (m/s)")
plt.title("Speed estimated from GPS position data"); plt.grid(True); plt.show()

# Parameter change: use a slightly higher position reading at 3 seconds
changed_position = position.copy(); changed_position[3] = 17.1
print("\nCHANGED INPUT: POSITION AT 3s = 17.1m")
print("New speed estimates:", np.round(estimate_speed(time, changed_position), 2))

# Related case: estimate flow rate from cumulative water volume readings
minutes = np.array([0, 1, 2, 3, 4], dtype=float)
volume_litres = np.array([0, 3, 7, 12, 18], dtype=float)
print("\nRELATED CASE: WATER FLOW RATE")
print("Estimated flow rates (L/min):", np.round(estimate_speed(minutes, volume_litres), 2))
