#@@ CODE
# Runge-Kutta (RK4) Method for ODEs
def runge_kutta_4(f, x0, y0, h, n):
    """
    f  : function dy/dx = f(x, y)
    x0 : initial x value
    y0 : initial y value
    h  : step size
    n  : number of steps
    """

    x = x0
    y = y0

    # Store initial value
    results = [(x, y)]

    for i in range(n):

        # Calculate k1, k2, k3, k4
        k1 = h * f(x, y)
        k2 = h * f(x + h / 2, y + k1 / 2)
        k3 = h * f(x + h / 2, y + k2 / 2)
        k4 = h * f(x + h, y + k3)

        # RK4 formula
        y += (k1 + 2 * k2 + 2 * k3 + k4) / 6

        # Update x
        x += h

        results.append((x, y))

    return results
#@@ EXAMPLE
# Example: dy/dx = x + y
def f(x, y):
    return x + y


# Initial conditions
x0 = 0
y0 = 1

h = 0.1       # Step size
n = 10        # Number of steps

# Apply RK4 method
solution = runge_kutta_4(f, x0, y0, h, n)

# Print results
for i, (x, y) in enumerate(solution):
    print(f"Step {i}: x = {x:.2f}, y = {y:.5f}")

# Output:
# Step 0: x = 0.00, y = 1.00000
# Step 1: x = 0.10, y = 1.11034
# Step 2: x = 0.20, y = 1.24281
# Step 3: x = 0.30, y = 1.39972
# Step 4: x = 0.40, y = 1.58365
# Step 5: x = 0.50, y = 1.79744
# Step 6: x = 0.60, y = 2.04424
# Step 7: x = 0.70, y = 2.32750
# Step 8: x = 0.80, y = 2.65108
# Step 9: x = 0.90, y = 3.01920
# Step 10: x = 1.00, y = 3.43656
#@@ EXAMPLE
# Compare RK4 with scipy.integrate.solve_ivp for dy/dx = y, y(0) = 1
import math
from scipy.integrate import solve_ivp


def g(x, y):
    return y


x, y = runge_kutta_4(g, 0, 1, 0.1, 10)[-1]
print(f"RK4 y(1)  : {y:.8f}")

sol = solve_ivp(g, (0, 1), [1], rtol=1e-10, atol=1e-12)
print(f"solve_ivp : {sol.y[0][-1]:.8f}")
print(f"exact e   : {math.e:.8f}")

# Output:
# RK4 y(1)  : 2.71827974
# solve_ivp : 2.71828183
# exact e   : 2.71828183
