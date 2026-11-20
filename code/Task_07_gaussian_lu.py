import numpy as np
from scipy.linalg import lu_factor, lu_solve

# Original case: same coefficient matrix, several measurement vectors
A = np.array([[4.0, -1.0, 0.0], [-1.0, 4.0, -1.0], [0.0, -1.0, 3.0]])
measurement_sets = [
    np.array([15.0, 10.0, 10.0]),
    np.array([16.0, 11.0, 9.0]),
    np.array([14.0, 12.0, 11.0])
]
lu, piv = lu_factor(A)
print("ORIGINAL CASE: LU DECOMPOSITION")
for i, b in enumerate(measurement_sets, start=1):
    x = lu_solve((lu, piv), b)
    print(f"Set {i}: solution={np.round(x, 4)}, residual norm={np.linalg.norm(b-A@x):.2e}")

# Parameter change: change the first measurement in set 1 from 15 to 18
changed_b = np.array([18.0, 10.0, 10.0])
print("\nCHANGED INPUT: FIRST MEASUREMENT = 18")
print("New solution:", lu_solve((lu, piv), changed_b))

# Related case: repeated water-flow balance calculations using the same pipe network matrix
flow_readings = [np.array([8.0, 5.0, 6.0]), np.array([9.0, 4.0, 7.0])]
print("\nRELATED CASE: PIPE-NETWORK FLOW ESTIMATES")
for b in flow_readings:
    print(np.round(lu_solve((lu, piv), b), 4))
