"""
thermion.core.fano
==================
The Fano plane — the incidence structure of the seven imaginary octonion
units, and the combinatorial backbone of the 731-ISA.

The Fano plane PG(2,2) has 7 points and 7 lines, each line containing
3 points, each point on 3 lines, every pair of points on exactly one line.
It is the smallest projective plane and the unique (7,3,1)-design.

Physical role
-------------
In the Origami ISA, the Fano incidence structure determines:
  - Which pairs of wire labels can be coupled (triangle inequality, Fano version)
  - The sign structure of octonion multiplication (the BIND opcode)
  - The 6-731 topology of the topological heat engine (Paper 325)
  - The PSL(2,7) symmetry of the associator-direction prediction (Paper 348, x353p)

The 7 Fano lines (1-based):
    (1,2,4), (2,3,5), (3,4,6), (4,5,7), (5,6,1), (6,7,2), (7,1,3)

References
----------
Baez (2002) The octonions. Bull. AMS 39, 145.
Buckley (2026) Paper 258: The 731 ISA. doi:10.5281/zenodo.19916429
Buckley (2026) Paper 325: The Topological Heat Engine. doi:10.5281/zenodo.20400638
"""

# The 7 Fano lines (1-based point labels)
FANO_LINES = [
    (1, 2, 4),
    (2, 3, 5),
    (3, 4, 6),
    (4, 5, 7),
    (5, 6, 1),
    (6, 7, 2),
    (7, 1, 3),
]

# Incidence matrix: FANO_INCIDENCE[i][j] = 1 if point i+1 is on line j+1
FANO_INCIDENCE = [
    [1, 0, 0, 0, 1, 0, 1],  # point 1: lines 1, 5, 7
    [1, 1, 0, 0, 0, 1, 0],  # point 2: lines 1, 2, 6
    [0, 1, 1, 0, 0, 0, 1],  # point 3: lines 2, 3, 7
    [1, 0, 1, 1, 0, 0, 0],  # point 4: lines 1, 3, 4
    [0, 1, 0, 1, 1, 0, 0],  # point 5: lines 2, 4, 5
    [0, 0, 1, 0, 1, 1, 0],  # point 6: lines 3, 5, 6
    [0, 0, 0, 1, 0, 1, 1],  # point 7: lines 4, 6, 7
]


def are_collinear(a, b, c):
    """
    Return True if points a, b, c (1-based) are collinear in the Fano plane.
    Collinear triples are exactly the Fano lines.
    """
    triple = frozenset([a, b, c])
    return any(frozenset(line) == triple for line in FANO_LINES)


def fano_line_through(a, b):
    """
    Return the third point on the unique Fano line through points a and b.
    Every pair of distinct points determines a unique line.

    Parameters
    ----------
    a, b : int (1-based, 1..7)

    Returns
    -------
    int : the third point on the line, or None if a == b.
    """
    if a == b:
        return None
    for line in FANO_LINES:
        if a in line and b in line:
            return next(p for p in line if p != a and p != b)
    return None


def octonion_product_sign(a, b):
    """
    Sign of e_a * e_b in the standard octonion multiplication table.
    Returns (sign, c) where e_a * e_b = sign * e_c.

    For a == b: returns (-1, 0) since e_a^2 = -1 (real part).
    For a != b: looks up the Fano line and determines cyclic order.

    Parameters
    ----------
    a, b : int (1-based, 1..7)

    Returns
    -------
    (sign, c) : (int, int)  sign ∈ {+1, -1}, c ∈ {0..7} (0 = real part)
    """
    if a == b:
        return (-1, 0)
    for line in FANO_LINES:
        if a in line and b in line:
            i_a = line.index(a)
            i_b = line.index(b)
            c = next(p for p in line if p != a and p != b)
            # Cyclic order: (i,j,k) → e_i e_j = +e_k
            sign = +1 if (i_b - i_a) % 3 == 1 else -1
            return (sign, c)
    raise ValueError(f"Points {a} and {b} not found on any Fano line")


def broken_fano_edges(source=0, r=0.18):
    """
    The 6-731 topology from Paper 325: the complete K_7 graph with one
    Fano line weakened (the 'broken line').

    Returns a 7x7 coupling matrix with the source-node Fano line
    weakened by factor r.

    Parameters
    ----------
    source : int (0-based node index, default 0 = BChl1 in FMO)
    r : float, weak coupling ratio J_weak / J_strong (default 0.18)

    Returns
    -------
    numpy.ndarray, shape (7, 7)
    """
    try:
        import numpy as np
    except ImportError:
        raise ImportError("numpy required: pip install thermion[numerics]")

    H = np.ones((7, 7)) - np.eye(7)
    # The broken line connects source (0-based) to its Fano partner
    # In the abstract 6-731 model: weaken edge (0, 2)
    broken_a, broken_b = source, (source + 2) % 7
    H[broken_a, broken_b] = r
    H[broken_b, broken_a] = r
    return H
