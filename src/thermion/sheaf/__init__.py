"""
thermion.sheaf
==============
Sheaf-theoretic machinery for the Adelic Simplicial Architecture.

A sheaf assigns data to each open set of a topological space (or each
object of a category) and specifies how data on larger sets restricts
to smaller ones, subject to a gluing axiom.

In the ASA, sheaves appear in three contexts:

1. Financial contagion (Papers 332-337, econiac):
   The sheaf of solvency/liquidity states over the bank network.
   Each node carries a SystemState; restriction maps are the contagion
   operators; global sections are fixed points of the cascade.

2. Regge geometry (Paper 349):
   The sheaf of local simplicial geometries over a triangulation.
   Each tetrahedron carries a 6j amplitude; gluing conditions are
   the Pachner move identities; global sections are triangulation-
   invariant partition functions.

3. Admissibility geometry (Papers 294/313, TIR routing):
   The sheaf of Fano/G2/Abelian geometry types over a routing graph.
   Each node carries a geometry filter; restriction maps are the
   Gibbs lifting operators from thermion.core.geometry.

This module is a placeholder for v0.1.0.
Full sheaf machinery migrates from econiac in v0.2.0.

References
----------
Buckley (2026) Paper 294: Thermodynamic Information Routing.
  doi:10.5281/zenodo.20237288
Buckley (2026) Papers 332-337: Financial contagion sheaves.
"""
