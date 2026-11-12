from __future__ import annotations


def missing_frames(expected: list[int], found: list[int]) -> list[int]:
    """Return the sorted frames in expected that are not in found."""
    symm_diff = sorted(list(set(expected).symmetric_difference(set(found))))
    return [el for el in symm_diff if el in expected]


def extra_frames(expected: list[int], found: list[int]) -> list[int]:
    """Return the sorted frames in found that are not in expected."""
    symm_diff = sorted(list(set(expected).symmetric_difference(set(found))))
    return [el for el in symm_diff if el in found]

