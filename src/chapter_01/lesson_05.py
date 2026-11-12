from __future__ import annotations


def frame_list(first: int, last: int) -> list[int]:
    """Return every frame from first to last, including last; empty when last is before first."""
    out_list = []
    while (first <= last):
        out_list.append(first)
        first += 1
    return out_list


def expected_names(sequence: str, first: int, last: int, extension: str) -> list[str]:
    """Return every filename of the image sequence, in frame order, frames padded to 4 digits."""
    frame_order = frame_list(first, last)
    out_names = []
    for frame_number in frame_order:
        frame_number = str(frame_number)
        while len(frame_number) < 4: frame_number = "0" + frame_number
        name = sequence + "." + frame_number + extension
        out_names.append(name)
    return out_names