# thermion

**Core engine for the Adelic Simplicial Architecture.**

*Every symmetry. Every scale. Exact.*

[![PyPI](https://img.shields.io/pypi/v/thermion)](https://pypi.org/project/thermion/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://python.org)

---

Thermion is the computational engine for the **Adelic Simplicial Architecture
(ASA)** — a unified framework in which representation theory, thermodynamics,
information geometry, and exceptional Lie algebra all reduce to the same five
rewriting operations on typed wires.

A thermion is a charged particle emitted by thermal energy. The name is apt:
thermion computes by emitting exact amplitudes from thermal distributions,
wherever symmetry acts.

---

## The five Origami ISA opcodes

The core of thermion is five operations — the **Pachner moves of the
3-simplex** — that generate all of representation theory:

| Opcode | Mathematical object | What it computes |
|--------|-------------------|-----------------|
| `flip(j)` | Evaluation map (cap) | Time-reversal; particle↔hole; C-parity |
| `flop(j1,j2,j12,j3,j,j23)` | Wigner 6j symbol | Recoupling cost; F-move; Pentagon |
| `split(j)` | Frobenius unit | Pair creation; quantum dimension √(2j+1) |
| `splat(j)` | Frobenius counit | Pair annihilation; bubble closure; Gibbs weight |
| `twist(j)` | Ribbon element | Spin-orbit phase; spin-statistics; holonomy |

Every result is an exact sympy expression — never a float.

```python
from thermion import flop, flip

flop(0, 1, 1, 1, 1, 1)          # → -1/3  (exact rational)
flip(1) * flop(0, 1, 1, 1, 1, 1)  # → -1/3  (FLIP;FLOP chain)
```

The **Pentagon identity** — five FLOPs compose to the identity — is
simultaneously Mac Lane's coherence theorem (1963), the Biedenhahn-Elliott
identity of nuclear spectroscopy (Racah 1942), and the Pachner 2→3 move of
triangulated topology (Pachner 1991). Three communities. One equation.

---

## The three computational frameworks

### MGE — Maslov-Gibbs Einsum

The **Maslov-Gibbs Einsum** is the thermodynamic bridge between continuous
optimisation and discrete logic. At inverse temperature β → ∞, it recovers
the tropical (max-plus) semiring — exact discrete logic. At β = 0, it gives
the uniform Gibbs distribution — maximum entropy. At finite β, it interpolates:
a differentiable, thermally-annealed tensor contraction.

```python
from thermion.core.ensemble import gibbs_weights, partition_function, free_energy

# Route probability mass across 7 channels at inverse temperature β
weights = gibbs_weights(utilities, beta=2.0)

# The FMO light-harvesting efficiency (Paper 325):
# η = 1 - SPLAT(β_cold) / SPLAT(β_hot) = 0.1825
```

MGE unifies eight independent rediscoveries of the same theorem: McFadden
(discrete choice), Jaynes (maximum entropy), Gibbs (statistical mechanics),
Maslov (tropical geometry), Sims (rational inattention), McKelvey-Palfrey
(quantal response), Friston (free energy principle), and Goel (information
equilibrium). They all derived the same routing primitive.

**Key paper:** [The Maslov-Gibbs Einsum](https://doi.org/10.5281/zenodo.17981393) (doi:10.5281/zenodo.17981393)

---

### TRS — Topological Resonance Synthesis

**Topological Resonance Synthesis** is the computational mode of the ASA in
which information geometry, holomorphic relaxation, and thermodynamic flow
are unified into a single engine. The TRS processor operates on the
statistical manifold (𝒫₊, g_Fisher) via Gibbs annealing — parallel transport
along the e-geodesic toward the Gibbs fixed point.

The TRS framework identifies three regimes of computation:
- **Regime 1** (associative): standard quantum mechanics, Pentagon trivial
- **Regime 2** (Origami): Rep(G) rewriting, Pentagon holds, 6j symbols exact
- **Regime 3** (Frog): octonion associator, Pentagon fails, PSL(2,7) symmetry

```python
from thermion.core.geometry import FanoGeometry, G2Geometry, AbelianGeometry

# Admissibility filter for Fano-structured routing
geom = FanoGeometry()
masked_utilities = geom.mask(utilities, source=0)
```

**Key paper:** [Topological Resonance Synthesis](https://doi.org/10.5281/zenodo.19858021) (doi:10.5281/zenodo.19858021)

---

### URN — Unitary Resonance Network

The **Unitary Resonance Network** is the hardware architecture that implements
the Origami ISA at the physical level. The 731-ISA (Paper 258) specifies the
machine code; the URN is the resonant substrate that executes it — a network
of coupled oscillators whose natural resonances implement the five opcodes.

The Fano plane PG(2,2) is the switching fabric of the 731-register:

```python
from thermion.core.fano import are_collinear, broken_fano_edges, FANO_LINES

# The 7 Fano lines — the connectivity of the 731-ISA register
FANO_LINES  # [(1,2,4), (2,3,5), (3,4,6), (4,5,7), (5,6,1), (6,7,2), (7,1,3)]

# Broken-line 6-731 topology (Paper 325, topological heat engine)
H = broken_fano_edges(source=0, r=0.18)  # J_weak/J_strong = 0.18
```

**Key paper:** [The 731 ISA](https://doi.org/10.5281/zenodo.19916429) (doi:10.5281/zenodo.19916429)

---

## The regime ladder

Thermion's regime taxonomy is parametrised by the normed division algebra
filling the tetrahedron interior (Hurwitz 1898 — the ladder terminates at
rung 3):

| Rung | Interior | Symmetry | Pentagon | Calculus | Physical instances |
|------|----------|----------|----------|----------|--------------------|
| 0 | ±1 scalar | ℤ/2ℤ | Trivial | ZX | Qubit circuits, Clifford gates |
| 1 | ℝ (6j) | S₄ (order 24) | **Holds** | **Origami** | All spectroscopy; spin networks |
| 1+ | ℂ (q-6j) | S₄ over ℂ | Holds | q-Origami | Turaev-Viro TQFT; topological QC |
| 3 | 𝕆 (associator) | PSL(2,7) (order 168) | **Fails** | Frog/731 | FeMo-cofactor; non-assoc. QEC |

ZX ⊂ Origami ⊂ Frog (strict inclusions).

---

## Where the same opcodes appear

The five opcodes compute the same objects across every physical scale:

| Domain | Computation | Scale | Paper |
|--------|------------|-------|-------|
| Atomic spectroscopy | f-shell coupling, G₂ wall | eV | [347](https://doi.org/10.5281/zenodo.20458996) |
| Nuclear spectroscopy | Pandya theorem, ⁹²Mo | MeV | [348](https://doi.org/10.5281/zenodo.20490046) |
| Quarkonium / QCD | X(3872) C-parity, FLIP;FLOP | GeV | [350](https://doi.org/10.5281/zenodo.20490294) |
| Molecular spectroscopy | CO₂ Fermi resonance | 10⁻³ eV | 353 |
| Biological (FMO) | Fano efficiency η = 0.1825 | 10⁻⁶ eV | [325](https://doi.org/10.5281/zenodo.20400638) |
| Topological heat engine | Carnot cycle, broken Fano line | — | [325](https://doi.org/10.5281/zenodo.20400638) |
| 3D quantum gravity | Ponzano-Regge partition function | Planck | [349](https://doi.org/10.5281/zenodo.20474914) |
| Financial routing | TIR Gibbs ensemble | — | [294](https://doi.org/10.5281/zenodo.20237288) |
| Topological QFT | Turaev-Viro 3-manifold invariants | — | — |
| Langlands program | Local L-function factors (planned) | — | 240 |

The `flop(0,1,1,1,1,1) = -1/3` identity appears in nuclear spectroscopy
**and** QCD charmonium decays at 3 GeV. Same exact rational. The universality
is only visible because the result is exact — floats return two slightly
different approximations and the identity is obscured.

---

## Installation

```bash
pip install thermion                 # core opcodes only (sympy)
pip install thermion[numerics]       # + numpy, scipy (Gibbs ensemble, geometry)
pip install thermion[jax]            # + jax (differentiable MGE routing)
```

---

## Applications built on thermion

| Package | Domain | Install |
|---------|--------|---------|
| [spectrafold](https://github.com/roguetrainer/spectrafold) | Angular momentum recoupling, spectroscopy | `pip install spectrafold` |
| [econiac](https://github.com/roguetrainer/econiac) | Financial gauge theory, TIR routing, MGE | `pip install econiac` |
| [racah](https://github.com/roguetrainer/racah) | Racah algebra (via spectrafold) | `pip install racah` |

---

## Selected papers

The ASA framework spans 50+ papers. Key foundational works:

**The engine:**
| Paper | DOI |
|-------|-----|
| The Maslov-Gibbs Einsum (MGE) | [10.5281/zenodo.17981393](https://doi.org/10.5281/zenodo.17981393) |
| Topological Resonance Synthesis (TRS) | [10.5281/zenodo.19858021](https://doi.org/10.5281/zenodo.19858021) |
| The 731 ISA (Origami ISA) | [10.5281/zenodo.19916429](https://doi.org/10.5281/zenodo.19916429) |
| The Origami Calculus (foundations) | [10.5281/zenodo.20474914](https://doi.org/10.5281/zenodo.20474914) |
| Thermodynamic Information Routing (TIR) | [10.5281/zenodo.20237288](https://doi.org/10.5281/zenodo.20237288) |

**Spectroscopy (spectrafold):**
| Paper | DOI |
|-------|-----|
| Spiders for Spectra (atomic) | [10.5281/zenodo.20458996](https://doi.org/10.5281/zenodo.20458996) |
| Spiders for Nuclei (nuclear) | [10.5281/zenodo.20490046](https://doi.org/10.5281/zenodo.20490046) |
| Spiders for Quarkonium (QCD) | [10.5281/zenodo.20490294](https://doi.org/10.5281/zenodo.20490294) |
| The Topological Heat Engine (FMO/ribosome) | [10.5281/zenodo.20400638](https://doi.org/10.5281/zenodo.20400638) |

**Thermodynamics & economics (econiac):**
| Paper | DOI |
|-------|-----|
| Thermal Economics | [10.5281/zenodo.20318505](https://doi.org/10.5281/zenodo.20318505) |
| Economic Gauge Theory | [10.5281/zenodo.20259495](https://doi.org/10.5281/zenodo.20259495) |
| Temperature of Rationality | [10.5281/zenodo.20234841](https://doi.org/10.5281/zenodo.20234841) |
| EconIAC: MONIAC for the 21st Century | [10.5281/zenodo.20315689](https://doi.org/10.5281/zenodo.20315689) |

**Non-associative geometry (rung 3):**
| Paper | DOI |
|-------|-----|
| The Frog Calculus, Part 1 | [10.5281/zenodo.19713350](https://doi.org/10.5281/zenodo.19713350) |
| The Frog Calculus, Part 2 | [10.5281/zenodo.20139448](https://doi.org/10.5281/zenodo.20139448) |
| Non-Associative Calculus | [10.5281/zenodo.20025384](https://doi.org/10.5281/zenodo.20025384) |
| Virtual Monopoles in FeMo-Cofactor | [10.5281/zenodo.20346650](https://doi.org/10.5281/zenodo.20346650) |

**Quantum computing (hardware):**
| Paper | DOI |
|-------|-----|
| The Resonance Processing Unit (RPU) | [10.5281/zenodo.19743800](https://doi.org/10.5281/zenodo.19743800) |
| Fibrational Tensor Codes (FTC) | [10.5281/zenodo.19821692](https://doi.org/10.5281/zenodo.19821692) |
| In Praise of Qudits | [10.5281/zenodo.20269991](https://doi.org/10.5281/zenodo.20269991) |

---

## License

MIT. Author: Ian R. C. Buckley — [ian.r.c.buckley@gmail.com](mailto:ian.r.c.buckley@gmail.com)

*"The same equation — the Pentagon identity — was independently discovered
and named three times: the Biedenhahn-Elliott identity (spectroscopy, 1952),
Mac Lane's coherence condition (category theory, 1963), and the Pachner 2→3
move (topology, 1991). Thermion names the calculus they all describe."*
