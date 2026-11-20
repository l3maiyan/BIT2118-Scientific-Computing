import numpy as np
from scipy.optimize import minimize

# Original case: minimize server operating cost subject to capacity >= 1000
def cost(z):
    x, y = z
    return 12*x + 18*y
def capacity_constraint(z):
    x, y = z
    return 100*x + 170*y - 1000
constraints = {"type": "ineq", "fun": capacity_constraint}
bounds = [(0, None), (0, None)]
solution = minimize(cost, x0=[5, 3], method="SLSQP", bounds=bounds, constraints=constraints)
x, y = solution.x
print("ORIGINAL CASE: SERVER RESOURCE OPTIMIZATION")
print("Optimization success:", solution.success)
print(f"Type A allocation: {x:.3f}")
print(f"Type B allocation: {y:.3f}")
print(f"Total capacity: {100*x+170*y:.2f}")
print(f"Minimum planning cost: {solution.fun:.2f}")

# Parameter change: raise required capacity from 1000 to 1200
def higher_capacity(z):
    return 100*z[0] + 170*z[1] - 1200
changed = minimize(cost, x0=[5, 4], method="SLSQP", bounds=bounds,
                   constraints={"type": "ineq", "fun": higher_capacity})
print("\nCHANGED PARAMETER: REQUIRED CAPACITY = 1200")
print("New allocation:", np.round(changed.x, 3))
print(f"New minimum cost: {changed.fun:.2f}")

# Related case: minimize delivery cost while meeting a daily carrying capacity
# Vehicle A costs 50 and carries 8 units; vehicle B costs 70 and carries 13 units.
def delivery_cost(z):
    a, b = z
    return 50*a + 70*b
def delivery_capacity(z):
    a, b = z
    return 8*a + 13*b - 60
delivery = minimize(delivery_cost, x0=[3, 3], method="SLSQP",
                    bounds=[(0, None), (0, None)],
                    constraints={"type": "ineq", "fun": delivery_capacity})
print("\nRELATED CASE: DELIVERY VEHICLE PLANNING")
print("Vehicle allocation:", np.round(delivery.x, 3))
print(f"Estimated minimum cost: {delivery.fun:.2f}")
