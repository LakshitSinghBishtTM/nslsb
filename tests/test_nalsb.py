import contextlib
import io

import pytest

import nalsb as na


@pytest.mark.parametrize("n", range(1, 11))
def test_ques_and_ans_run(n):
    for source in (na.ques(n), na.ans(n)):
        compile(source, "<test>", "exec")
        with contextlib.redirect_stdout(io.StringIO()):
            exec(source, {"__name__": "__main__"})


@pytest.mark.parametrize("name,num", [
    ("floating", 1), ("gauss", 2), ("jacobi", 3), ("newton", 4), ("lagrange", 5),
    ("leastsquares", 6), ("simpson", 7), ("euler", 8), ("rk4", 9), ("power", 10),
    ("Gauss", 2), (" Runge-Kutta ", 9), ("Simpson's", 7), ("7", 7),
])
def test_names_match_numbers(name, num):
    assert na.ques(name) == na.ques(num)
    assert na.ans(name) == na.ans(num)


def test_ans_has_two_examples():
    assert na.ans(3).count("# ---------- Example") == 2


def test_bad_keys():
    for bad in (0, 11, "nonsense", True):
        with pytest.raises(ValueError):
            na.ques(bad)


def test_star_names():
    assert na.ques(na.gauss) == na.ques(2)
    assert na.ans(na.jacobi) == na.ans(3)


def test_gauss_does_not_mutate_inputs():
    ns = {}
    exec(na._core._load(2)[0], ns)
    A = [[2, 1], [1, 3]]
    b = [3, 5]
    first = ns["gauss_elimination"](A, b)
    second = ns["gauss_elimination"](A, b)
    assert first == second and A == [[2, 1], [1, 3]] and b == [3, 5]
