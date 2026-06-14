# thermion.forge — API Sketch

**Status:** Design only. Implementation follows Paper 424.

thermion.forge is the β-parameterised, autodiff-compatible layer of the
Origami ISA. It sits between the discrete opcodes (thermion.core) and the
smooth operators (thermion.meld):

    thermion.core    — discrete (β→∞), exact, Rep(G), sympy
    thermion.forge   — finite β, differentiable, PyTorch/JAX
    thermion.meld    — smooth (β→0), scipy sparse, de Rham

---

## Core design principles

1. **Every opcode is a PyTorch nn.Module** — composable, differentiable,
   β is a parameter (either fixed or learnable).

2. **β*(ρ) is the default temperature** — computed from the constraint
   graph before running, not tuned by search.

3. **Drop-in for hard opcodes** — SPLIT(x) at large β ≈ hard B₁·x.
   Users can swap thermion.core opcodes for thermion.forge opcodes
   and get autodiff for free.

4. **TRS mandate respected** — β only appears in the Hamiltonian via
   the Gibbs weight. No ad-hoc schedules. Conformal, symplectic,
   adiabatic structure preserved.

---

## thermion.forge.schedule

```python
from thermion.forge.schedule import beta_star, BetaSchedule

# Compute β*(ρ) from a constraint graph
# graph: nx.Graph or (edge_list, n_vertices) tuple
beta = beta_star(graph)
# Returns: float, the critical inverse temperature

# Annealing schedule: linear ramp from 0 to β*, then exponential to β_max
schedule = BetaSchedule(
    graph=graph,
    n_steps=1000,
    mode='linear_to_critical',   # ramp to β*(ρ), then hold
    # mode='full_anneal'         # ramp to β*(ρ), then continue to β_max
    # mode='constant'            # fixed β=beta_star(graph) throughout
)
for step, beta in enumerate(schedule):
    loss = programme(x, beta=beta)
    loss.backward()
    optimizer.step()
```

**Implementation:**
```python
def beta_star(graph) -> float:
    """β*(ρ) = (3/8) * log(1 / (1 - rho))
    where rho = beta_1 / |E| = (|E| - |V| + components) / |E|
    Computable in O(|V| + |E|) via union-find.
    """
    n_v, n_e, n_comp = _graph_stats(graph)  # union-find
    beta_1 = n_e - n_v + n_comp
    rho = beta_1 / max(n_e, 1)
    if rho <= 0:
        return 0.0
    if rho >= 1:
        return float('inf')
    return (3/8) * math.log(1 / (1 - rho))
```

---

## thermion.forge.opcodes

### SPLIT_β

```python
import torch
import torch.nn as nn
from thermion.forge import SPLIT

# Construct from an incidence matrix B1 (m x n) and temperature β
split = SPLIT(B1=torch.tensor(B1, dtype=torch.float32), beta=beta)

# Forward: soft coboundary
# x: (batch, n_vertices)  →  out: (batch, n_edges)
out = split(x)

# Discrete limit (β→∞): out ≈ B1 @ x  (hard incidence)
# Smooth limit (β→0):   out ≈ 0.5 * ones_like(B1) @ x  (uniform)
```

**Implementation:**
```python
class SPLIT(nn.Module):
    def __init__(self, B1: torch.Tensor, beta: float):
        super().__init__()
        self.register_buffer('B1', B1)
        self.beta = beta

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # Soft incidence: sigmoid(β * B1) applied to x
        # At β→∞: sigmoid→step → hard B1
        # At β→0: sigmoid→0.5 → uniform weighting
        soft_B1 = torch.sigmoid(self.beta * self.B1)
        return soft_B1 @ x
```

### SPLAT_β

```python
splat = SPLAT(B1=B1, beta=beta)
# SPLAT_β = SPLIT_β.T (transpose)
# x: (batch, n_edges) → out: (batch, n_vertices)
out = splat(x)
```

**Implementation:** transpose of SPLIT_β. Gradient flows by transposing
the Jacobian automatically.

### FLOP_β

```python
flop = FLOP(B1=B1, beta=beta)
# Soft harmonic correction via β-regularised Laplacian solve
# x: (batch, n_edges) → out: (batch, n_edges)  [H¹ correction]
out = flop(x)
```

**Implementation:**
```python
class FLOP(nn.Module):
    def __init__(self, B1: torch.Tensor, beta: float):
        super().__init__()
        self.register_buffer('B1', B1)
        self.beta = beta

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        # Hodge Laplacian: L = B1.T @ B1 + B1 @ B1.T (up + down)
        # β-regularised solve: (L + (1/β)·I)⁻¹ x
        # As β→∞: ε=(1/β)→0, approaches exact Green's operator
        # As β→0: ε→∞, approaches identity (no correction)
        m = self.B1.shape[0]
        L = self.B1.T @ self.B1 + self.B1 @ self.B1.T
        eps = 1.0 / max(self.beta, 1e-6)
        L_reg = L + eps * torch.eye(L.shape[0], device=L.device)
        # torch.linalg.solve is autodiff-compatible
        return torch.linalg.solve(L_reg, x.T).T
```

### FLIP_β

```python
flip = FLIP(volumes=simplex_volumes, beta=beta)
# Soft Hodge star via β-weighted simplex volumes
# x: (batch, n_k_simplices) → out: (batch, n_{n-k}_simplices)
out = flip(x)
```

### TWIST_β

```python
twist = TWIST(phase=theta, beta=beta)
# Soft gauge transformation: x * exp(i * sigma_beta(theta))
# As β→∞: hard phase (0 or π)
# As β→0: identity (no twist)
out = twist(x)
```

---

## thermion.forge.programme

The high-level interface: compose opcodes into a ForgeProgram.

```python
from thermion.forge import ForgeProgram, SPLIT, SPLAT, FLOP, beta_star

# Build a Forge ISA programme for Max-Cut
graph = build_constraint_graph(edges, n_vertices)
beta  = beta_star(graph)

programme = ForgeProgram(beta=beta, schedule='linear_to_critical')
programme.add(SPLIT(B1, beta=beta))
programme.add(SPLAT(B1, beta=beta))
programme.add(FLOP(B1, beta=beta))

# Run with autodiff
x = torch.zeros(n_vertices, requires_grad=True)
optimizer = torch.optim.Adam([x], lr=0.01)

for step, current_beta in enumerate(programme.schedule(n_steps=1000)):
    programme.set_beta(current_beta)
    cut_value = programme.cut_value(x)
    loss = -cut_value  # maximise cut
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# Discrete solution at end of annealing
solution = (x > 0).int()
```

---

## thermion.meld — smooth limit operators

```python
from thermion.meld import d, delta, G, hodge_star, gauge

# Exterior derivative d: C^k(K) → C^{k+1}(K)
# Implemented as sparse matrix multiplication (exact, scipy.sparse)
df = d(f, complex=K, k=0)       # 0-forms → 1-forms

# Hodge codifferential δ = ★d★
delta_f = delta(f, complex=K, k=1)

# Green's operator G = (dδ+δd)⁻¹ on harmonic complement
# Implemented via scipy.sparse.linalg.spsolve
gf = G(f, complex=K, k=1)

# Hodge star ★: C^k → C^{n-k}
sf = hodge_star(f, complex=K, k=1)

# Gauge transform: parallel transport around a loop
gf = gauge(f, complex=K, loop=loop_edges, phase=theta)
```

**Key difference from thermion.forge:**
- thermion.forge: PyTorch, autodiff, finite β, approximate
- thermion.meld: scipy.sparse, exact, β=0, no autodiff needed
  (smooth operators are already differentiable analytically)

---

## Package structure

```
thermion/
  src/thermion/
    core/          ← existing: discrete opcodes, exact, sympy/Rep(G)
      opcodes.py   ← SPLIT, SPLAT, FLOP, FLIP, TWIST (exact)
      ensemble.py  ← Gibbs ensemble
      fano.py      ← Fano geometry
    forge/         ← NEW: β-parameterised, PyTorch, autodiff
      __init__.py
      opcodes.py   ← SPLIT_β, SPLAT_β, FLOP_β, FLIP_β, TWIST_β
      schedule.py  ← beta_star(), BetaSchedule
      programme.py ← ForgeProgram
      API_SKETCH.md
    meld/          ← NEW: smooth limit, scipy.sparse
      __init__.py
      operators.py ← d, delta, G, hodge_star, gauge
      complex.py   ← SimplicialComplex helper
```

---

## Dependencies

thermion.core (existing): sympy, numpy
thermion.forge (new):     torch >= 2.0, numpy, networkx
thermion.meld  (new):     scipy, numpy, networkx

Optional: jax (for JAX-compatible versions of forge opcodes)

---

## Connection to the trilogy

thermion.core  ↔  Origami ISA (Papers 258/349) — β→∞, discrete, exact
thermion.forge ↔  Forge ISA   (Paper 419)       — finite β, differentiable
thermion.meld  ↔  The Meld    (Paper 417)        — β→0, smooth, exact
