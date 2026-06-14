"""
thermion.meld
=============
Smooth (β→0) limit operators: the Meld correspondence.

The Meld (Paper 417) identifies the β→0 limit of the Origami ISA:
the five discrete opcodes become the five operators of smooth
Hodge theory (d, δ, G, ★, gauge). At this limit, discrete and
continuous are revealed to be one.

    SPLIT  →  d       (exterior derivative)
    SPLAT  →  δ = ★d★ (Hodge codifferential)
    FLOP   →  G       (Green's operator, pseudo-inverse of Hodge Laplacian)
    FLIP   →  ★       (Hodge star)
    TWIST  →  gauge   (parallel transport / gauge transformation)

Implemented using scipy.sparse for exact linear algebra on
simplicial complexes. No autodiff needed — smooth operators are
analytically differentiable. Use thermion.forge for the
autodiff-compatible finite-β versions.

Usage::

    from thermion.meld import d, delta, G, hodge_star

    K = SimplicialComplex(vertices, edges, triangles)
    f = cochain(K, k=0)   # 0-cochain (function on vertices)

    df    = d(f, K)        # exterior derivative: 0-form → 1-form
    delta_f = delta(df, K) # codifferential: 1-form → 0-form
    harm  = G(df, K)       # harmonic part (H¹ residual)

See API_SKETCH.md for full documentation.
Implemented in: Paper 417 (The Meld) and Paper 424.
"""

# Imports will be added as modules are implemented (Paper 424)
# from .operators import d, delta, G, hodge_star, gauge
# from .complex import SimplicialComplex, cochain
