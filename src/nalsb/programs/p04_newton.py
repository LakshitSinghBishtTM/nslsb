#@@ CODE
# Newton-Raphson Method
def newton_raphson(f, df, x0, tolerance=1e-10, max_iterations=100):

    x = x0

    for i in range(max_iterations):

        fx = f(x)
        dfx = df(x)

        # Check if derivative is zero
        if dfx == 0:
            raise ValueError("Derivative is zero. No solution found.")

        # Newton-Raphson formula
        x_new = x - fx / dfx

        # Check for convergence
        if abs(x_new - x) < tolerance:
            print(f"Converged in {i + 1} iterations.")
            return x_new

        x = x_new

    raise ValueError(
        "Did not converge within the maximum number of iterations."
    )
#@@ EXAMPLE
# Example: Solve f(x) = x^3 - x - 2
def f(x):
    return x**3 - x - 2


def df(x):
    return 3*x**2 - 1


# Initial guess
x0 = 1.5

# Apply Newton-Raphson Method
root = newton_raphson(f, df, x0)

print("Root:", root)

# Validate with scipy
from scipy.optimize import fsolve
print("fsolve:", fsolve(f, x0)[0])

# Output:
# Converged in 4 iterations.
# Root: 1.5213797068045676
# fsolve: 1.5213797068045751
#@@ EXAMPLE
# Example: Solve cos(x) - x = 0
import math


def g(x):
    return math.cos(x) - x


def dg(x):
    return -math.sin(x) - 1


root = newton_raphson(g, dg, 0.5)

print("Root:", root)
print("Check g(root):", g(root))

# Output:
# Converged in 5 iterations.
# Root: 0.7390851332151607
# Check g(root): 0.0
