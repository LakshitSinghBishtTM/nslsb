#@@ CODE
# Euler's Method for ODEs
def euler_method(f, x0, y0, h, n):
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

        # Euler formula
        y = y + h * f(x, y)
        x = x + h

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

# Apply Euler's Method
solution = euler_method(f, x0, y0, h, n)

# Print results
for i, (x, y) in enumerate(solution):
    print(f"Step {i}: x = {x:.2f}, y = {y:.5f}")

# Output:
# Step 0: x = 0.00, y = 1.00000
# Step 1: x = 0.10, y = 1.10000
# Step 2: x = 0.20, y = 1.22000
# Step 3: x = 0.30, y = 1.36200
# Step 4: x = 0.40, y = 1.52820
# Step 5: x = 0.50, y = 1.72102
# Step 6: x = 0.60, y = 1.94312
# Step 7: x = 0.70, y = 2.19743
# Step 8: x = 0.80, y = 2.48718
# Step 9: x = 0.90, y = 2.81590
# Step 10: x = 1.00, y = 3.18748
#@@ EXAMPLE
# Example: dy/dx = y, y(0) = 1  (exact solution y = e^x)
import math


def g(x, y):
    return y


for h, n in ((0.1, 10), (0.01, 100)):
    x, y = euler_method(g, 0, 1, h, n)[-1]
    print(f"h = {h}: y(1) = {y:.5f}, exact = {math.e:.5f}, error = {abs(y - math.e):.5f}")

# Output:
# h = 0.1: y(1) = 2.59374, exact = 2.71828, error = 0.12454
# h = 0.01: y(1) = 2.70481, exact = 2.71828, error = 0.01347
