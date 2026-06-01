"""Tests for thermion core — exact arithmetic throughout."""
from sympy import Rational, sqrt, Integer
from thermion.core.opcodes import (
    flip, flop, split, splat, twist, twist_eigenvalue, verify_pentagon
)
from thermion.core.fano import (
    are_collinear, fano_line_through, octonion_product_sign, FANO_LINES
)


class TestOpcodes:
    def test_flip_integer(self):
        assert flip(0) == 1
        assert flip(1) == 1
        assert flip(2) == 1

    def test_flip_half_integer(self):
        assert flip(Rational(1, 2)) == -1
        assert flip(Rational(7, 2)) == -1   # f-shell
        assert flip(Rational(9, 2)) == -1   # 1g9/2 shell

    def test_flop_x3872(self):
        # {0 1 1; 1 1 1} = -1/3 — X(3872)→J/ψγ amplitude (Paper 350 x354f)
        assert flop(0, 1, 1, 1, 1, 1) == Rational(-1, 3)

    def test_flop_111(self):
        assert flop(1, 1, 1, 1, 1, 1) == Rational(1, 6)

    def test_flip_flop_chain(self):
        # FLIP;FLOP = Pandya sign × 6j — same result for nuclear and QCD
        assert flip(1) * flop(0, 1, 1, 1, 1, 1) == Rational(-1, 3)

    def test_split_splat_frobenius(self):
        for j in [0, Rational(1, 2), 1, Rational(3, 2), 2]:
            assert split(j) * splat(j) == 1

    def test_split_quantum_dimension(self):
        assert split(0) == 1
        assert split(Rational(1, 2)) == sqrt(2)
        assert split(1) == sqrt(3)
        assert split(2) == sqrt(5)

    def test_twist_hyperfine(self):
        # Delta_TWIST = 1 (triplet - singlet) — universal for qq-bar (Paper 350)
        assert twist_eigenvalue(1) - twist_eigenvalue(0) == 1
        assert twist_eigenvalue(0) == Rational(-3, 4)
        assert twist_eigenvalue(1) == Rational(1, 4)

    def test_pentagon(self):
        passed, lhs, rhs = verify_pentagon(1, 1, 1, 1, 1)
        assert passed


class TestFano:
    def test_all_fano_lines_collinear(self):
        for a, b, c in FANO_LINES:
            assert are_collinear(a, b, c)

    def test_non_fano_triple_not_collinear(self):
        assert not are_collinear(1, 2, 3)
        assert not are_collinear(1, 3, 5)

    def test_line_through(self):
        # (1,2,4) is a Fano line — third point through 1 and 2 is 4
        assert fano_line_through(1, 2) == 4
        assert fano_line_through(2, 4) == 1
        assert fano_line_through(1, 4) == 2

    def test_octonion_product(self):
        # e1 * e2 = +e4 (first Fano line, cyclic order)
        sign, c = octonion_product_sign(1, 2)
        assert c == 4
        assert sign == 1
        # e2 * e1 = -e4 (anti-commutative)
        sign2, c2 = octonion_product_sign(2, 1)
        assert c2 == 4
        assert sign2 == -1

    def test_octonion_self_product(self):
        # e_a^2 = -1
        sign, c = octonion_product_sign(1, 1)
        assert sign == -1
        assert c == 0  # real part
