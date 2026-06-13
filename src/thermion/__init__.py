"""
thermion
========
Core engine for the Adelic Simplicial Architecture.

Rep(G) rewriting, Gibbs ensemble, Pachner moves, Fano geometry, sheaves.
Every symmetry. Every scale. Exact.

The five Origami ISA opcodes
-----------------------------
    flip   — evaluation map (cap/cup); time-reversal of a wire
    flop   — Wigner 6j F-move; the cost of reassociation
    split  — Frobenius unit; pair creation, quantum dimension
    splat  — Frobenius counit; pair annihilation, bubble closure
    twist  — ribbon element; spin-orbit phase, spin-statistics

These are the Pachner moves of the 3-simplex. The Pentagon identity
(five FLOPs compose to the identity) is Mac Lane's coherence theorem.
Every computation in Rep(G) — spectroscopy, quantum gravity, financial
routing, automorphic forms — reduces to sequences of these five opcodes.

Quick start
-----------
>>> from thermion import flop, flip, split, splat, twist
>>> flop(0, 1, 1, 1, 1, 1)          # 6j {0 1 1; 1 1 1} — exact rational
-1/3
>>> flip(1) * flop(0, 1, 1, 1, 1, 1)  # FLIP;FLOP (Pandya / X(3872) E1)
-1/3

The Gibbs ensemble (requires thermion[numerics])
-------------------------------------------------
>>> from thermion.core.ensemble import gibbs_weights, free_energy

The Fano geometry
-----------------
>>> from thermion.core.fano import are_collinear, broken_fano_edges

Applications
------------
spectrafold — thermion for angular momentum recoupling (spectroscopy)
econiac     — thermion for financial gauge theory (TIR routing)
racah       — spectrafold for Racah algebra

Papers
------
Paper 258  731-ISA          doi:10.5281/zenodo.19916429
Paper 347  Spiders/Spectra  doi:10.5281/zenodo.20458996
Paper 348  Spiders/Nuclei   doi:10.5281/zenodo.20490046
Paper 349  Origami Calculus doi:10.5281/zenodo.20474914
Paper 325  Topological HE   doi:10.5281/zenodo.20400638
Paper 410  Spin Foams/LQG   doi:10.5281/zenodo.20680634
Paper 411  Pulse Sequences  doi:10.5281/zenodo.20680609
Paper 412  Typed DSL        doi:10.5281/zenodo.20681513
Paper 413  Molecular Mach.  doi:10.5281/zenodo.20682101
"""

from thermion.core.opcodes import (
    flip,
    flop,
    split,
    splat,
    twist,
    twist_eigenvalue,
    wigner3j,
    verify_pentagon,
)

# G₂ representation theory (Papers 410/411, x410a/b)
from thermion.core.g2 import (
    g2_dim,
    g2_casimir,
    g2_area_quantum,
    g2_irrep_table,
    fano_automorphisms,
    triality_automorphisms,
    canonical_triality,
    g2_weyl_group,
    weyl_element_order,
    barbero_immirzi_su2,
    barbero_immirzi_g2,
    FANO_LINES,
)

# Typed ISA DSL (Paper 412)
from thermion.core.typed import (
    Rep,
    Wire,
    AssocWire,
    FullWire,
    ISACircuit,
    frobenius_schur,
    is_assoc_wire,
    pcl_wire,
    pcl_flow,
)

__version__ = "0.2.0"
__author__ = "Ian R. C. Buckley"
__all__ = [
    # Origami ISA opcodes
    "flip", "flop", "split", "splat", "twist",
    "twist_eigenvalue", "wigner3j", "verify_pentagon",
    # G₂ representation theory
    "g2_dim", "g2_casimir", "g2_area_quantum", "g2_irrep_table",
    "fano_automorphisms", "triality_automorphisms", "canonical_triality",
    "g2_weyl_group", "weyl_element_order",
    "barbero_immirzi_su2", "barbero_immirzi_g2",
    "FANO_LINES",
    # Typed ISA DSL
    "Rep", "Wire", "AssocWire", "FullWire", "ISACircuit",
    "frobenius_schur", "is_assoc_wire",
    "pcl_wire", "pcl_flow",
]
