# thermion

**Core engine for the Adelic Simplicial Architecture.**

*Every symmetry. Every scale. Exact.*

[![PyPI](https://img.shields.io/pypi/v/thermion)](https://pypi.org/project/thermion/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://python.org)

---

Thermion is the Rep(G) rewriting engine at the heart of the Adelic Simplicial
Architecture (ASA). It provides five opcodes — **FLIP, FLOP, SPLIT, SPLAT,
TWIST** — that form a universal, exact, compositional language for any
computation in the representation theory of compact groups.

Every result is a sympy expression. No floats, no rounding, no guessing.

```python
from thermion import flop, flip

# The 6j symbol — the single most important object in Rep(G)
flop(0, 1, 1, 1, 1, 1)
# → -1/3  (exact rational)

# FLIP;FLOP: the Pandya theorem, X(3872)→J/ψγ, CO₂ Q-branch, FMO η
# — all the same two opcodes, across nuclear/QCD/molecular/biological scales
flip(1) * flop(0, 1, 1, 1, 1, 1)
# → -1/3
```

## The five opcodes

The five opcodes are the **Pachner moves of the 3-simplex** — the elementary
rewriting rules for triangulated 3-manifolds (Regge 1961, Ponzano-Regge 1968,
Mac Lane 1963, Turaev-Viro 1992):

| Opcode | Mathematical object | Physical meaning |
|--------|--------------------|--------------------|
| `flip(j)` | Evaluation map (cap) | Time-reversal; particle↔hole |
| `flop(j1,j2,j12,j3,j,j23)` | Wigner 6j symbol | Recoupling; F-move cost |
| `split(j)` | Frobenius unit | Pair creation; quantum dimension √(2j+1) |
| `splat(j)` | Frobenius counit | Pair annihilation; bubble closure |
| `twist(j)` | Ribbon element | Spin-orbit phase; spin-statistics |

The **Pentagon identity** — five FLOPs compose to the identity — is Mac Lane's
coherence theorem for monoidal categories. It is also the Pachner 2→3 move
identity and the Biedenhahn-Elliott identity of nuclear spectroscopy.

## Where the same opcodes appear

| Domain | What it computes | Paper |
|--------|-----------------|-------|
| Atomic spectroscopy | f-shell coupling, G₂ wall | 347 |
| Nuclear spectroscopy | Pandya theorem, 1g₉/₂ shell | 348 |
| Quarkonium / QCD | X(3872) C-parity selection rules | 350 |
| Molecular spectroscopy | CO₂ Fermi resonance, P/R branches | 353 |
| Biological (FMO) | Fano efficiency η = 0.1825 | 325 |
| 3D quantum gravity | Ponzano-Regge partition function | 349 |
| Financial routing | TIR Gibbs ensemble, contagion sheaves | 294 |
| Topological QFT | Turaev-Viro 3-manifold invariants | — |
| Langlands program | Local L-function factors (planned) | 240 |

Same opcodes. Every scale. The Origami ISA is the FFT of representation theory.

## The Gibbs ensemble

The thermodynamic core — the partition function, Gibbs weights, and free energy
— is in `thermion.core.ensemble` (requires `thermion[numerics]`):

```python
from thermion.core.ensemble import gibbs_weights, partition_function

# The FMO light-harvesting efficiency (Paper 325, x356b)
# η = 1 - SPLAT(β_cold) / SPLAT(β_hot) = 0.1825
```

## The Fano geometry

The Fano plane PG(2,2) — incidence structure of the seven imaginary octonion
units, backbone of the 731-ISA (Paper 258):

```python
from thermion.core.fano import are_collinear, broken_fano_edges

are_collinear(1, 2, 4)   # True — on the first Fano line
are_collinear(1, 2, 3)   # False — not a Fano line
```

## Installation

```bash
pip install thermion                 # core opcodes only (sympy)
pip install thermion[numerics]       # + numpy, scipy (Gibbs ensemble)
pip install thermion[jax]            # + jax (differentiable routing)
```

## Applications built on thermion

| Package | Domain |
|---------|--------|
| [spectrafold](https://github.com/roguetrainer/spectrafold) | Angular momentum recoupling, spectroscopy |
| [econiac](https://github.com/roguetrainer/econiac) | Financial gauge theory, TIR routing |
| [racah](https://github.com/roguetrainer/racah) | Racah algebra (via spectrafold) |

## Papers

All open access on Zenodo:

| Paper | Title | DOI |
|-------|-------|-----|
| 258 | The 731 Instruction Set Architecture | [10.5281/zenodo.19916429](https://doi.org/10.5281/zenodo.19916429) |
| 347 | Spiders for Spectra | [10.5281/zenodo.20458996](https://doi.org/10.5281/zenodo.20458996) |
| 348 | Spiders for Nuclei | [10.5281/zenodo.20490046](https://doi.org/10.5281/zenodo.20490046) |
| 349 | The Origami Calculus | [10.5281/zenodo.20474914](https://doi.org/10.5281/zenodo.20474914) |
| 325 | The Topological Heat Engine | [10.5281/zenodo.20400638](https://doi.org/10.5281/zenodo.20400638) |

## License

MIT. Author: Ian R. C. Buckley — [ian.r.c.buckley@gmail.com](mailto:ian.r.c.buckley@gmail.com)
