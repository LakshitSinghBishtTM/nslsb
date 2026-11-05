# nalsb - Numerical Methods lab programs as a Python library
# Copyright (C) 2026  Lakshit Singh Bisht <lakshitsinghbishttm@gmail.com>
# Licensed under the GNU General Public License v3.0 or later (see LICENSE).
"""nalsb: the 10 Numerical Methods lab programs as a library.

    import nalsb as na
    print(na.ques(4))        # or na.ques("newton")
    print(na.ans("jacobi"))  # program + 2 examples
    na.run(2)                # execute a program
    na.programs()            # list numbers and names

Optionally ``from nalsb import *`` lets you write ``na.ques(gauss)`` without
quotes, because the names below are defined as plain strings.
"""

from ._core import ans, programs, ques, run

__version__ = "0.1.0"
__author__ = "Lakshit Singh Bisht"

# Name shortcuts so that, after ``from nalsb import *``, ques(gauss) works.
floating = "floating"
gauss = "gauss"
jacobi = "jacobi"
newton = "newton"
lagrange = "lagrange"
leastsquares = "leastsquares"
simpson = "simpson"
euler = "euler"
rk4 = "rk4"
power = "power"

__all__ = [
    "ques", "ans", "run", "programs",
    "floating", "gauss", "jacobi", "newton", "lagrange",
    "leastsquares", "simpson", "euler", "rk4", "power",
]
