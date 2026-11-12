from __future__ import annotations


def sequence_name(shot: str, task: str, version: int) -> str:
    """Return the part every frame of an image sequence shares, e.g. SH010_comp_v002."""
    version = str(version)
    while len(version) < 3:
        version = '0' + version

    return f"{shot}_{task}_v{version}"


def frame_filename(shot: str, task: str, version: int, frame: int, extension: str) -> str:
    """Return the filename for one frame, e.g. SH010_comp_v002.1001.exr."""
    version = str(version)
    while len(version) < 3:
        version = '0' + version

    frame = str(frame)
    while len(frame) < 4:
        frame = '0' + frame

    return f"{shot}_{task}_v{version}.{frame}{extension}"
