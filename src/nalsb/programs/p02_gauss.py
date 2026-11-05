#@@ CODE
# Gaussian Elimination with Partial Pivoting
def gauss_elimination(matrix, rhs):
    n = len(rhs)

    # Work on a copy and augment it with the RHS vector
    # (so the caller's lists are not modified)
    matrix = [list(map(float, row)) + [float(rhs[i])] for i, row in enumerate(matrix)]

    # Forward Elimination
    for i in range(n):

        # Pivoting: find the maximum element in the current column
        max_row = max(range(i, n), key=lambda r: abs(matrix[r][i]))

        if abs(matrix[max_row][i]) < 1e-12:
            raise ValueError("Matrix is singular (no unique solution).")

        # Swap rows
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]

        # Make all rows below this one 0 in the current column
        for j in range(i + 1, n):
            factor = matrix[j][i] / matrix[i][i]

            for k in range(i, n + 1):
                matrix[j][k] -= factor * matrix[i][k]

    # Back Substitution
    x = [0] * n

    for i in range(n - 1, -1, -1):
        x[i] = (
            matrix[i][n]
            - sum(matrix[i][j] * x[j] for j in range(i + 1, n))
        ) / matrix[i][i]

    return x
#@@ EXAMPLE
# Example system:
#   2x -  y +  z =  2
#   3x + 3y + 9z = -1
#   3x + 3y + 5z =  4
A = [
    [2, -1, 1],
    [3, 3, 9],
    [3, 3, 5]
]

B = [2, -1, 4]

solution = gauss_elimination(A, B)

print("Solution:", solution)

# Compare with numpy
import numpy as np
print("numpy   :", np.linalg.solve(A, B))

# Output:
# Solution: [2.2222222222222223, 1.1944444444444444, -1.25]
# numpy   : [ 2.22222222  1.19444444 -1.25      ]
#@@ EXAMPLE
# A system whose first pivot is 0 (pivoting is essential here)
A = [
    [0, 2, 1],
    [1, -1, 2],
    [3, 1, -1]
]

B = [5, 6, 4]

solution = gauss_elimination(A, B)

print("Solution:", solution)

import numpy as np
print("numpy   :", np.linalg.solve(A, B))

# Output:
# Solution: [1.8333333333333333, 1.1666666666666667, 2.6666666666666665]
# numpy   : [1.83333333 1.16666667 2.66666667]
