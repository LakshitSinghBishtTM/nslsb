#@@ CODE
# Least Squares Data Fitting (straight line y = m*x + c)
def least_squares_fit(x_values, y_values):

    n = len(x_values)

    if n != len(y_values):
        raise ValueError("x and y must be the same length")

    sum_x = sum(x_values)
    sum_y = sum(y_values)
    sum_xx = sum(x**2 for x in x_values)
    sum_xy = sum(x_values[i] * y_values[i] for i in range(n))

    denominator = n * sum_xx - sum_x**2
    if denominator == 0:
        raise ValueError("x values must not all be identical")

    # Calculate slope (m) and intercept (c)
    m = (n * sum_xy - sum_x * sum_y) / denominator

    c = (sum_y - m * sum_x) / n

    return m, c
#@@ EXAMPLE
# Example data
x_data = [1, 2, 3, 4, 5]
y_data = [2, 4, 5, 4, 5]

slope, intercept = least_squares_fit(x_data, y_data)

print(f"Best-fit line: y = {slope:.2f}x + {intercept:.2f}")

# Output:
# Best-fit line: y = 0.60x + 2.20
#@@ EXAMPLE
# Fit a line, compare with numpy.polyfit, and compute residuals and RMSE
import numpy as np

x_data = [0, 1, 2, 3, 4, 5]
y_data = [1, 3, 2, 5, 4, 7]

slope, intercept = least_squares_fit(x_data, y_data)
print(f"Best-fit line: y = {slope:.4f}x + {intercept:.4f}")
print("numpy.polyfit :", np.polyfit(x_data, y_data, 1))

residuals = [y - (slope * x + intercept) for x, y in zip(x_data, y_data)]
rmse = (sum(r**2 for r in residuals) / len(residuals)) ** 0.5
print("Residuals:", [round(r, 4) for r in residuals])
print(f"RMSE: {rmse:.4f}")

# Output:
# Best-fit line: y = 1.0286x + 1.0952
# numpy.polyfit : [1.02857143 1.0952381 ]
# Residuals: [-0.0952, 0.8762, -1.1524, 0.819, -1.2095, 0.7619]
# RMSE: 0.8962
