from __future__ import annotations


def sort_by_frame(names: list[str]) -> list[str]:
    """Return a new list of frame filenames sorted by frame number."""
    frame_numbers = sorted([int(name.split(".")[-2]) for name in names])
    sorted_names = []
    for frame_number in frame_numbers:
        for name in names:
            curr_frame_number = int(name.split(".")[-2])
            if frame_number == curr_frame_number: sorted_names.append(name)
    return sorted_names


def format_run(start: int, end: int) -> str:
    """Return "1004" for a single frame, or "1001-1004" for a range."""
    if start == end: return str(start)
    return str(start) + "-" + str(end)
