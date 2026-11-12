from __future__ import annotations
from chapter_01.lesson_03 import split_frame_name

def group_by_sequence(names: list[str]) -> dict[str, list[int]]:
    """Return each image sequence with its sorted frames, each listed once; skip non-images and non-digit frames."""
    out_dict = dict()
    for name in names:
        frame_name_dict = split_frame_name(name)

        if frame_name_dict is not None:
            sequence = frame_name_dict["sequence"]
            frame = frame_name_dict["frame"]
            extension = frame_name_dict["extension"]
            if frame.isdigit():
                image_sequence = sequence + extension
                if image_sequence not in out_dict.keys(): 
                    out_dict[image_sequence] = {int(frame)}
                else: 
                    out_dict[image_sequence].add(int(frame))
                    print(out_dict)

    for key, value in out_dict.items():
        out_dict[key] = sorted(list(value))

    return out_dict