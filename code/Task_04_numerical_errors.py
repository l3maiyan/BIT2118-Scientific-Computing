import numpy as np

print("ORIGINAL CASE: FLOATING-POINT COMPARISON")
a = 0.1
b = 0.2
c = 0.3
total = a + b
print("0.1 + 0.2 =", repr(total))
print("Exact comparison with 0.3:", total == c)
print("Tolerance comparison:", np.isclose(total, c))
print("Absolute error:", abs(total - c))

# Parameter change: use a larger tolerance
print("\nCHANGED PARAMETER")
print("Comparison with atol=1e-8:", np.isclose(total, c, atol=1e-8))

# Related case: compare a rounded sensor measurement with a reference value
reference = 12.5
measured = 12.50000001
print("\nRELATED CASE: SENSOR CALIBRATION")
print("Within 1e-6 tolerance:", np.isclose(measured, reference, atol=1e-6))
print("Absolute measurement error:", abs(measured - reference))
