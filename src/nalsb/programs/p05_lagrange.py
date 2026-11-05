#@@ CODE
# Lagrange Polynomial Interpolation
def lagrange_interpolation(x_values, y_values, x):

    n = len(x_values)
    result = 0.0

    for i in range(n):

        term = y_values[i]

        for j in range(n):

            if i != j:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])

        result += term

    return result
#@@ EXAMPLE
# Example data points
x_points = [1, 2, 3, 4]
y_points = [1, 4, 9, 16]  # y = x^2

# Interpolate at x = 2.5
x_target = 2.5

interpolated_value = lagrange_interpolation(
    x_points, y_points, x_target
)

print(f"Interpolated value at x = {x_target} is {interpolated_value}")

# Output:
# Interpolated value at x = 2.5 is 6.25
#@@ EXAMPLE
# Interpolate y = x^3 from 4 points; a cubic is reproduced exactly
x_points = [0, 1, 2, 3]
y_points = [0, 1, 8, 27]

for x_target in (0.5, 1.5, 2.5):
    value = lagrange_interpolation(x_points, y_points, x_target)
    print(f"x = {x_target}: interpolated = {value}, exact = {x_target**3}")

# Output:
# x = 0.5: interpolated = 0.125, exact = 0.125
# x = 1.5: interpolated = 3.375, exact = 3.375
# x = 2.5: interpolated = 15.625, exact = 15.625
