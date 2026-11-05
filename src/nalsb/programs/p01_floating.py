#@@ CODE
# Floating-Point Errors & Loss of Significance
import numpy as np

# Floating-point representation (single precision cannot hold 1.0000001 exactly)
a = np.float32(1.0000001)
b = np.float32(1.0000000)

print("Difference:", a - b)


# Loss of significance (catastrophic cancellation)
def loss_significance(x):
    return np.sqrt(x**2 + 1) - x


# Stable rewrite: multiply and divide by the conjugate to avoid subtracting
# two nearly equal numbers.
def stable(x):
    return 1 / (np.sqrt(x**2 + 1) + x)


x = 1e8

print("Loss of significance:", loss_significance(x))
print("Stable formula      :", stable(x))
#@@ EXAMPLE
# (lab-manual example: the code above)

# Output:
# Difference: 1.1920929e-07
# Loss of significance: 0.0
# Stable formula      : 5e-09
#@@ EXAMPLE
# Single vs double precision using numpy.float32 and numpy.float64
import numpy as np

print("0.1 + 0.2 (float64):", np.float64(0.1) + np.float64(0.2))
print("0.1 + 0.2 == 0.3   :", np.float64(0.1) + np.float64(0.2) == np.float64(0.3))
print("0.1 + 0.2 (float32):", np.float32(0.1) + np.float32(0.2))
print("Machine epsilon float32:", np.finfo(np.float32).eps)
print("Machine epsilon float64:", np.finfo(np.float64).eps)

# Accumulated rounding error: add 0.1 one million times
s32 = np.float32(0.0)
s64 = np.float64(0.0)
for _ in range(1_000_000):
    s32 += np.float32(0.1)
    s64 += np.float64(0.1)
print("Sum of 0.1 x 1e6 (float32):", s32)
print("Sum of 0.1 x 1e6 (float64):", s64)

# Output:
# 0.1 + 0.2 (float64): 0.30000000000000004
# 0.1 + 0.2 == 0.3   : False
# 0.1 + 0.2 (float32): 0.3
# Machine epsilon float32: 1.1920929e-07
# Machine epsilon float64: 2.220446049250313e-16
# Sum of 0.1 x 1e6 (float32): 100958.34
# Sum of 0.1 x 1e6 (float64): 100000.00000133288
