"""
thermion.forge
==============
β-parameterised, autodiff-compatible Origami ISA opcodes.

The Forge ISA (Paper 419) operates at finite inverse temperature β,
interpolating between the discrete Origami ISA (β→∞, thermion.core)
and the smooth Meld (β→0, thermion.meld).

Every opcode is a PyTorch nn.Module. β*(ρ) is computed from the
constraint graph topology in O(|V|+|E|) via union-find — no
hyperparameter search required.

Usage::

    from thermion.forge import SPLIT, SPLAT, FLOP, beta_star, BetaSchedule

    graph = ...  # networkx.Graph or (edge_list, n_vertices)
    beta  = beta_star(graph)

    split = SPLIT(B1=incidence_matrix, beta=beta)
    flop  = FLOP(B1=incidence_matrix, beta=beta)

    x = torch.zeros(n_vertices, requires_grad=True)
    out = flop(split(x))
    out.sum().backward()  # gradients flow through both opcodes

See API_SKETCH.md for full documentation.
Implemented in: Paper 424 (The Differentiable Origami ISA).
"""

# Imports will be added as modules are implemented (Paper 424)
# from .schedule import beta_star, BetaSchedule
# from .opcodes import SPLIT, SPLAT, FLOP, FLIP, TWIST
# from .programme import ForgeProgram
