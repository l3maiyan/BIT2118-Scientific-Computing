import numpy as np
import timeit

# Original case: convert one million network latency readings from ms to seconds
rng = np.random.default_rng(42)
latency_ms = rng.uniform(5, 250, 1_000_000)

def loop_version():
    result = []
    for value in latency_ms:
        seconds = value / 1000.0
        result.append(seconds ** 2)
    return result

def vectorized_version():
    seconds = latency_ms / 1000.0
    return seconds ** 2

loop_time = timeit.timeit(loop_version, number=1)
vector_time = timeit.timeit(vectorized_version, number=3) / 3
result = vectorized_version()
print("ORIGINAL CASE")
print("First five squared latency values:", result[:5])
print(f"Loop time: {loop_time:.4f} s")
print(f"Vectorized time: {vector_time:.4f} s")
print(f"Approximate speed-up: {loop_time / vector_time:.1f}x")

# Parameter change: use 100,000 readings instead of 1,000,000
smaller = latency_ms[:100_000]
print("\nCHANGED INPUT: 100,000 readings")
print("First five results:", (smaller / 1000)[:5] ** 2)

# Related case: convert a batch of sensor distances from centimetres to metres
distance_cm = np.array([125.0, 240.0, 315.0, 80.0])
distance_m = distance_cm / 100
print("\nRELATED CASE: SENSOR DISTANCES")
print("Distances in metres:", distance_m)
