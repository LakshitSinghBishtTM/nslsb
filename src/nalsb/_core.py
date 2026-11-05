# nalsb - Numerical Methods lab programs as a Python library
# Copyright (C) 2026  Lakshit Singh Bisht <lakshitsinghbishttm@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""Core lookup and loading logic for nalsb."""

import re
from importlib import resources

# number -> (canonical name, title, source file)
_PROGRAMS = {
    1: ("floating", "Floating-Point Errors & Loss of Significance", "p01_floating.py"),
    2: ("gauss", "Gaussian Elimination with Partial Pivoting", "p02_gauss.py"),
    3: ("jacobi", "Jacobi Iterative Method", "p03_jacobi.py"),
    4: ("newton", "Newton-Raphson Method", "p04_newton.py"),
    5: ("lagrange", "Lagrange Polynomial Interpolation", "p05_lagrange.py"),
    6: ("leastsquares", "Least Squares Data Fitting", "p06_leastsquares.py"),
    7: ("simpson", "Numerical Integration (Simpson's Rule)", "p07_simpson.py"),
    8: ("euler", "Euler's Method for ODEs", "p08_euler.py"),
    9: ("rk4", "Runge-Kutta (RK4) Method for ODEs", "p09_rk4.py"),
    10: ("power", "Power Method for Eigenvalues", "p10_power.py"),
}

# extra spellings that also work (all compared lower-case, letters/digits only)
_ALIASES = {
    "floating": ["float", "floats", "floatingpoint", "errors", "precision", "losssignificance"],
    "gauss": ["gaussian", "gausselimination", "gaussianelimination", "pivoting"],
    "jacobi": ["iterative", "jacobimethod"],
    "newton": ["newtonraphson", "raphson", "nr"],
    "lagrange": ["interpolation", "lagrangeinterpolation"],
    "leastsquares": ["lsq", "leastsquare", "fitting", "polyfit", "regression", "linearfit"],
    "simpson": ["simpsons", "simpsonsrule", "simpsonrule", "integration"],
    "euler": ["eulermethod", "eulers"],
    "rk4": ["rk", "rungekutta", "rungekutta4", "rk4method"],
    "power": ["powermethod", "eigen", "eigenvalue", "eigenvalues"],
}

_LOOKUP = {}
for _num, (_name, _title, _file) in _PROGRAMS.items():
    _LOOKUP[_name] = _num
    for _alias in _ALIASES[_name]:
        _LOOKUP[_alias] = _num

_SPLIT = re.compile(r"^#@@ (CODE|EXAMPLE)\n", re.M)


def _normalise(text):
    return re.sub(r"[^a-z0-9]", "", str(text).lower())


def _resolve(key):
    """Turn 1, "1", "gauss", "Gauss Elimination"... into a program number."""
    if isinstance(key, bool):
        raise ValueError("Use a number 1-10 or a name such as 'gauss'.")
    if isinstance(key, int):
        num = key
    else:
        norm = _normalise(key)
        if norm.isdigit():
            num = int(norm)
        elif norm in _LOOKUP:
            num = _LOOKUP[norm]
        else:
            raise ValueError(
                f"Unknown program {key!r}. Use a number 1-10 or a name: "
                + ", ".join(v[0] for v in _PROGRAMS.values())
            )
    if num not in _PROGRAMS:
        raise ValueError(f"Program number must be between 1 and {len(_PROGRAMS)}, got {key!r}.")
    return num


def _load(num):
    """Return (code, [example1, example2]) for program ``num``."""
    path = resources.files("nalsb").joinpath("programs", _PROGRAMS[num][2])
    text = path.read_text(encoding="utf-8")
    parts = _SPLIT.split(text)
    # ['', 'CODE', code, 'EXAMPLE', ex1, 'EXAMPLE', ex2]
    return parts[2].rstrip("\n"), [parts[4].rstrip("\n"), parts[6].rstrip("\n")]


def _header(num, kind):
    return f"# Program {num}: {_PROGRAMS[num][1]}  [{kind}]"


def ques(key):
    """Return the source code of a lab program as a string.

    ``key`` is a number 1-10 or a lower-case name (``'gauss'``, ``'jacobi'``...).
    The code is the program followed by the lab-manual example.
    """
    num = _resolve(key)
    code, (ex1, _) = _load(num)
    if num == 1:  # the program itself is the demo
        return f"{_header(num, 'ques')}\n{code}"
    return f"{_header(num, 'ques')}\n{code}\n\n\n{ex1}"


def ans(key):
    """Return the program code plus two worked examples (with outputs)."""
    num = _resolve(key)
    code, (ex1, ex2) = _load(num)
    if num == 1:
        ex1 = "# Output of the program above:\n" + ex1.split("# Output:\n", 1)[1]
    return (
        f"{_header(num, 'ans')}\n{code}\n\n\n"
        f"# ---------- Example 1 ----------\n{ex1}\n\n\n"
        f"# ---------- Example 2 ----------\n{ex2}"
    )


def run(key, example=None):
    """Execute a program. ``example`` = None runs ques(key); 1 or 2 runs that
    example only (with the program code loaded first)."""
    num = _resolve(key)
    if example is None:
        source = ques(num)
    else:
        code, exs = _load(num)
        if example not in (1, 2):
            raise ValueError("example must be 1 or 2")
        source = code + "\n\n" + exs[example - 1]
    exec(compile(source, f"<nalsb program {num}>", "exec"), {"__name__": "__main__"})


def programs():
    """Print the table of available programs and their names."""
    lines = [f"{n:>2}  {name:<13} {title}" for n, (name, title, _) in _PROGRAMS.items()]
    text = "\n".join(lines)
    print(text)
    return text
