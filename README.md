# nalsb

The 10 programs from the *Numerical Methods for Scientific Computing* lab manual,
packaged as a Python library. Ask for a program's source code with one line.

```bash
pip install nalsb
```

```python
import nalsb as na

print(na.ques(4))        # program 4 (Newton-Raphson) + the lab-manual example
print(na.ans(4))         # program 4 + 2 worked examples with outputs

print(na.ques("gauss"))  # names work too: all lower case, no spaces
print(na.ans("jacobi"))

na.run("simpson")        # execute a program straight away
na.programs()            # list numbers and names
```

If you prefer no quotes, import the names:

```python
from nalsb import *
import nalsb as na
print(na.ques(gauss))
print(na.ans(jacobi))
```

## Programs

| # | name | program |
|---|------|---------|
| 1 | `floating` | Floating-point errors & loss of significance |
| 2 | `gauss` | Gaussian elimination with partial pivoting |
| 3 | `jacobi` | Jacobi iterative method |
| 4 | `newton` | Newton-Raphson method |
| 5 | `lagrange` | Lagrange polynomial interpolation |
| 6 | `leastsquares` | Least squares data fitting |
| 7 | `simpson` | Simpson's rule integration |
| 8 | `euler` | Euler's method for ODEs |
| 9 | `rk4` | Runge-Kutta (RK4) method for ODEs |
| 10 | `power` | Power method for the dominant eigenvalue |

Common alternative spellings (`"newtonraphson"`, `"rungekutta"`, `"simpsons"`, `"lsq"`, ...)
are accepted as well, and so are `"Gauss"` or `"Runge-Kutta"` (case, spaces and
punctuation are ignored).

## Development

```bash
pip install -e . pytest
pytest
```

## License

GPL-3.0-or-later. Copyright (C) 2026 Lakshit Singh Bisht <lakshitsinghbishttm@gmail.com>.
