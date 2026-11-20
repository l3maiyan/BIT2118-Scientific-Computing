import numpy as np

# Original case: estimate numbers of two server types from CPU and memory totals
# Type A: 4 CPU units and 8 GB; Type B: 2 CPU units and 12 GB
A = np.array([[4.0, 2.0], [8.0, 12.0]])
b = np.array([20.0, 72.0])
solution = np.linalg.solve(A, b)
print("ORIGINAL CASE: SERVER ALLOCATION")
print(f"Type A servers: {solution[0]:.0f}")
print(f"Type B servers: {solution[1]:.0f}")
print("Verification A @ x:", A @ solution)
print("Residual:", b - A @ solution)

# Parameter change: increase available CPU total from 20 to 24
b_changed = np.array([24.0, 72.0])
print("\nCHANGED INPUT: CPU TOTAL = 24")
print("New solution [Type A, Type B]:", np.linalg.solve(A, b_changed))

# Related case: blend two ingredients to meet nutrient targets
# Ingredient X: 3 protein units and 2 energy units; Y: 1 protein and 4 energy
nutrient_matrix = np.array([[3.0, 1.0], [2.0, 4.0]])
targets = np.array([11.0, 10.0])
print("\nRELATED CASE: INGREDIENT MIX")
print("Required quantities [X, Y]:", np.linalg.solve(nutrient_matrix, targets))
