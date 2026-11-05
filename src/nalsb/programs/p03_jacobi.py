#@@ CODE
# Jacobi Iterative Method
def jacobi_method(A, b, tolerance=1e-10, max_iterations=100):

    n = len(A)

    # Initial guess (zero vector)
    x = [0.0 for _ in range(n)]

    for iteration in range(max_iterations):

        x_new = x.copy()

        # Jacobi iteration
        for i in range(n):

            sum_ = sum(
                A[i][j] * x[j]
                for j in range(n)
                if j != i
            )

            x_new[i] = (b[i] - sum_) / A[i][i]

        # Check for convergence
        if all(
            abs(x_new[i] - x[i]) < tolerance
            for i in range(n)
        ):
            print(f"Converged in {iteration + 1} iterations.")
            return x_new

        x = x_new

    print("Did not converge within the maximum number of iterations.")
    return x
#@@ EXAMPLE
# Example system (diagonally dominant, so Jacobi converges):
A = [
    [10, -1, 2],
    [-1, 11, -1],
    [2, -1, 10]
]

b = [6, 25, -11]

solution = jacobi_method(A, b)

print("Solution:", solution)

# Output:
# Converged in 19 iterations.
# Solution: [1.0432692307598361, 2.269230769237108, -1.0817307692400526]
#@@ EXAMPLE
# A 3x3 tridiagonal, diagonally dominant system
A = [
    [4, -1, 0],
    [-1, 4, -1],
    [0, -1, 4]
]

b = [15, 10, 10]

solution = jacobi_method(A, b)

print("Solution:", solution)

import numpy as np
print("numpy   :", np.linalg.solve(A, b))

# Output:
# Converged in 25 iterations.
# Solution: [4.910714285697395, 4.64285714282596, 3.660714285697395]
# numpy   : [4.91071429 4.64285714 3.66071429]
