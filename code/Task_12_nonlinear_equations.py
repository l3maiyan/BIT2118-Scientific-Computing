import numpy as np
from scipy.optimize import root

# Original case: intersection of circle x^2+y^2=4 and parabola y=x^2-1
def equations(z):
    x, y = z
    return [x**2 + y**2 - 4, y - (x**2 - 1)]

print("ORIGINAL CASE: CIRCLE AND PARABOLA INTERSECTIONS")
for guess in ([1.0, 1.0], [-1.0, 1.0]):
    sol = root(equations, guess)
    print("Initial guess:", guess)
    print("Intersection:", np.round(sol.x, 6))
    print("Residuals:", np.round(equations(sol.x), 10))
    print("Converged:", sol.success)

# Parameter change: increase circle radius from 2 to 2.5
def changed_equations(z):
    x, y = z
    return [x**2 + y**2 - 2.5**2, y - (x**2 - 1)]
changed = root(changed_equations, [1.0, 1.0])
print("\nCHANGED PARAMETER: CIRCLE RADIUS = 2.5")
print("One intersection estimate:", np.round(changed.x, 6))

# Related case: find operating point where two nonlinear production constraints meet
def production(z):
    x, y = z
    return [x**2 + y - 10, x + y**2 - 10]
related = root(production, [2.0, 2.0])
print("\nRELATED CASE: PRODUCTION MODEL")
print("Operating point [x, y]:", np.round(related.x, 6))
print("Residuals:", np.round(production(related.x), 10))
