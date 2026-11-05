#@@ CODE
# Power Method for the dominant eigenvalue
import numpy as np


def power_method(A, max_iterations=1000, tolerance=1e-10, seed=0):

    A = np.asarray(A, dtype=float)
    n = A.shape[0]

    # Initial guess (random vector, seeded so results are reproducible)
    b_k = np.random.default_rng(seed).random(n)
    b_k = b_k / np.linalg.norm(b_k)

    eigenvalue = 0.0

    for i in range(max_iterations):

        # Multiply matrix by vector
        b_k1 = np.dot(A, b_k)

        # Calculate norm
        b_k1_norm = np.linalg.norm(b_k1)

        if b_k1_norm == 0:
            raise ValueError("A @ b is the zero vector; try another start.")

        # Normalize the vector
        b_k1 = b_k1 / b_k1_norm

        # Estimate the dominant eigenvalue (Rayleigh quotient)
        new_eigenvalue = np.dot(b_k1.T, np.dot(A, b_k1)) / np.dot(b_k1.T, b_k1)

        # Vector change (a negative dominant eigenvalue flips the sign
        # every step, so compare against both b_k and -b_k)
        change = min(np.linalg.norm(b_k1 - b_k), np.linalg.norm(b_k1 + b_k))

        b_k = b_k1

        # Check for convergence on both eigenvalue and eigenvector
        if abs(new_eigenvalue - eigenvalue) < tolerance and change < tolerance:
            eigenvalue = new_eigenvalue
            break

        eigenvalue = new_eigenvalue

    # Corresponding eigenvector
    eigenvector = b_k

    return eigenvalue, eigenvector
#@@ EXAMPLE
# Example matrix
A = np.array([
    [2, 1],
    [1, 3]
])


# Apply Power Method
eigenvalue, eigenvector = power_method(A)


print(f"Dominant Eigenvalue: {eigenvalue:.6f}")
print(f"Corresponding Eigenvector: {eigenvector}")

# Compare with numpy.linalg.eig
print("numpy eigenvalues:", np.sort(np.linalg.eigvals(A).real)[::-1])

# Output:
# Dominant Eigenvalue: 3.618034
# Corresponding Eigenvector: [0.52573111 0.85065081]
# numpy eigenvalues: [3.61803399 1.38196601]
#@@ EXAMPLE
# 3x3 symmetric matrix (eigenvalues 2 + sqrt(2), 2, 2 - sqrt(2))
A = np.array([
    [2, -1, 0],
    [-1, 2, -1],
    [0, -1, 2]
])

eigenvalue, eigenvector = power_method(A)

print(f"Dominant Eigenvalue: {eigenvalue:.6f}")
print(f"Corresponding Eigenvector: {eigenvector}")
print("numpy eigenvalues:", np.sort(np.linalg.eigvals(A).real)[::-1])

# Output:
# Dominant Eigenvalue: 3.414214
# Corresponding Eigenvector: [ 0.5        -0.70710678  0.5       ]
# numpy eigenvalues: [3.41421356 2.         0.58578644]
