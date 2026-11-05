#@@ CODE
# Numerical Integration - Composite Simpson's Rule
def simpsons_rule(f, a, b, n):

    if n % 2 != 0:
        raise ValueError("n must be even for Simpson's rule.")

    h = (b - a) / n

    result = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h

        if i % 2 != 0:
            weight = 4
        else:
            weight = 2

        result += weight * f(x)

    return (h / 3) * result
#@@ EXAMPLE
# Example function: f(x) = x^4  (exact integral from 0 to 2 is 6.4)
def f(x):
    return x**4


# Integrate f(x) from 0 to 2 using 6 intervals
a = 0
b = 2
n = 6

approx_integral = simpsons_rule(f, a, b, n)

print("Approximate integral:", approx_integral)

# Output:
# Approximate integral: 6.403292181069958
#@@ EXAMPLE
# Integrate sin(x) from 0 to pi (exact value = 2) and compare with scipy
import math
from scipy.integrate import quad

for n in (4, 10, 100):
    print(f"n = {n:3d}: {simpsons_rule(math.sin, 0, math.pi, n)}")

print("scipy.integrate.quad:", quad(math.sin, 0, math.pi)[0])

# Output:
# n =   4: 2.0045597549844207
# n =  10: 2.0001095173150043
# n = 100: 2.0000000108245044
# scipy.integrate.quad: 2.0
