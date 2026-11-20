import numpy as np

# Original case: 2D transformation of points using a matrix
points = np.array([[1, 2], [3, 1], [2, 4]], dtype=float)
rotation_90 = np.array([[0, -1], [1, 0]], dtype=float)
transformed = points @ rotation_90.T
print("ORIGINAL CASE: 90-DEGREE ROTATION")
print("Input points:\n", points)
print("Transformation matrix:\n", rotation_90)
print("Transformed points:\n", transformed)

# Parameter change: use a 180-degree rotation matrix
rotation_180 = np.array([[-1, 0], [0, -1]], dtype=float)
print("\nCHANGED PARAMETER: 180-DEGREE ROTATION")
print(points @ rotation_180.T)

# Related case: scale image/diagram coordinates by 2
scale = np.array([[2, 0], [0, 2]], dtype=float)
print("\nRELATED CASE: DOUBLE-SIZE GRAPHICS")
print(points @ scale.T)
