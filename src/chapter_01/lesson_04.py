from __future__ import annotations


def frame_number(name: str) -> int:
    """Return the frame of a filename as a number, e.g. "SH010_comp_v002.0007.exr" -> 7."""
    splits = name.split(".")
    frame_number = splits[-2]
    return int(frame_number)


def version_number(version: str) -> int:
    """Return the number of a version, e.g. "v002" -> 2."""
    return int(version[1:])


def next_version(version: str) -> str:
    """Return the next version with at least three digits, e.g. "v002" -> "v003"."""
    next_ver = str(version_number(version) + 1)
    while len(next_ver) < 3: 
        next_ver = "0" + next_ver
    return "v" + next_ver