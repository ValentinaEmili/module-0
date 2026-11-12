from __future__ import annotations


def is_image(name: str) -> bool:
    """Return True for .exr and .dpx files in any letter case."""
    splits = name.split('.')
    extension = splits[-1].lower()
    accepted_extensions = ['exr', 'dpx']
    if extension in accepted_extensions:
        return True
    return False


def split_frame_name(name: str) -> dict[str, str] | None:
    """Return sequence, frame, and extension of an image named SEQUENCE.FRAME.ext, or None."""
    splits = name.split('.')
    accepted_extensions = ['exr', 'dpx']
    extension = splits[-1].lower()
    if extension not in accepted_extensions or len(splits) < 3: 
        return None
    
    sequence, frame, extension = splits[0], splits[-2], splits[-1]

    sequence = splits[0]
    for i in range(1, len(splits)-2):
        sequence = sequence + "." + splits[i]
    return dict({
        "sequence": sequence,
        "frame": frame,
        "extension": "." + extension
    })