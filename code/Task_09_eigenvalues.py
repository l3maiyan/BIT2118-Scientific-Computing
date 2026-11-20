import numpy as np

# Original case: small undirected computer network
A = np.array([[0., 1., 1., 0.],
              [1., 0., 1., 1.],
              [1., 1., 0., 1.],
              [0., 1., 1., 0.]])
eigenvalues, eigenvectors = np.linalg.eig(A)
idx = np.argmax(np.real(eigenvalues))
dominant_value = np.real(eigenvalues[idx])
v = np.abs(np.real(eigenvectors[:, idx]))
centrality = v / v.sum()
nodes = ["A", "B", "C", "D"]
print("ORIGINAL CASE: NETWORK IMPORTANCE")
print("Dominant eigenvalue:", round(dominant_value, 5))
for node, score in zip(nodes, centrality):
    print(f"{node}: {score:.4f}")
print("Verification error:", np.linalg.norm(A @ np.real(eigenvectors[:, idx]) -
                                             dominant_value * np.real(eigenvectors[:, idx])))

# Parameter change: add a connection between nodes A and D
A_changed = A.copy()
A_changed[0, 3] = A_changed[3, 0] = 1
vals, vecs = np.linalg.eig(A_changed)
i = np.argmax(np.real(vals))
scores = np.abs(np.real(vecs[:, i])); scores /= scores.sum()
print("\nCHANGED NETWORK: ADD LINK A-D")
print("New importance scores:", dict(zip(nodes, np.round(scores, 4))))

# Related case: connections between four departments in an organization
print("\nRELATED CASE: DEPARTMENT COLLABORATION")
departments = ["IT", "Finance", "HR", "Operations"]
print("Importance scores from original network:", dict(zip(departments, np.round(centrality, 4))))
