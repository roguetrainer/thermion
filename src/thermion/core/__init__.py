"""
thermion.core
=============
The five Origami ISA opcodes (Rep(G) rewriting) and the Gibbs ensemble.

Opcodes — exact sympy arithmetic:
    flip, flop, split, splat, twist

Ensemble — thermodynamic routing:
    gibbs_weights, partition_function, free_energy

Geometry — admissibility structures:
    FanoGeometry, G2Geometry, AbelianGeometry
"""
from thermion.core.opcodes import (
    flip, flop, split, splat, twist,
    twist_eigenvalue, wigner3j, verify_pentagon,
)

__all__ = [
    "flip", "flop", "split", "splat", "twist",
    "twist_eigenvalue", "wigner3j", "verify_pentagon",
]
