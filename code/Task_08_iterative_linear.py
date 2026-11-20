import numpy as np
import matplotlib.pyplot as plt

A = np.array([[ 2., -1., 0., 0., 0.],
              [-1., 2., -1., 0., 0.],
              [0., -1., 2., -1., 0.],
              [0., 0., -1., 2., -1.],
              [0., 0., 0., -1., 2.]])
b = np.array([100., 0., 0., 0., 20.])

def jacobi(A, b, tol=1e-8, max_iter=500):
    D = np.diag(A)
    R = A - np.diagflat(D)
    x = np.zeros_like(b)
    errors = []
    for _ in range(max_iter):
        x_new = (b - R @ x) / D
        error = np.linalg.norm(x_new - x, ord=np.inf)
        errors.append(error)
        if error < tol:
            return x_new, errors
        x = x_new
    return x, errors

def gauss_seidel(A, b, tol=1e-8, max_iter=500):
    x = np.zeros_like(b)
    errors = []
    for _ in range(max_iter):
        old = x.copy()
        for i in range(len(b)):
            x[i] = (b[i] - A[i, :i] @ x[:i] - A[i, i+1:] @ old[i+1:]) / A[i, i]
        error = np.linalg.norm(x - old, ord=np.inf)
        errors.append(error)
        if error < tol:
            return x, errors
    return x, errors

x_j, err_j = jacobi(A, b)
x_gs, err_gs = gauss_seidel(A, b)
print("ORIGINAL CASE: STEADY-STATE TEMPERATURES")
print("Jacobi:", np.round(x_j, 5))
print("Gauss-Seidel:", np.round(x_gs, 5))
print("Direct solution:", np.round(np.linalg.solve(A, b), 5))
plt.semilogy(err_j, label="Jacobi")
plt.semilogy(err_gs, label="Gauss-Seidel")
plt.xlabel("Iteration")
plt.ylabel("Maximum change")
plt.title("Convergence of iterative temperature solution")
plt.legend(); plt.grid(True); plt.show()

# Parameter change: increase left boundary influence from 100 to 120
b_changed = np.array([120., 0., 0., 0., 20.])
print("\nCHANGED INPUT: LEFT BOUNDARY = 120 C")
print("New direct solution:", np.round(np.linalg.solve(A, b_changed), 5))

# Related case: five connected rooms with a 30 C and 18 C boundary
b_rooms = np.array([30., 0., 0., 0., 18.])
print("\nRELATED CASE: CONNECTED-ROOM TEMPERATURE MODEL")
print("Estimated room temperatures:", np.round(np.linalg.solve(A, b_rooms), 3))
