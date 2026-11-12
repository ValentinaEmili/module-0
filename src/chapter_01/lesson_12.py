from __future__ import annotations

import os
import sys
from typing import Any
import json

def inventory(folder: str) -> dict[str, Any]:
    """Return the image sequences (frames, missing, count) and other files directly inside folder."""
    out = dict({
        "sequences" : dict({}),
        "other" : []
    })
    
    for file in os.listdir(folder):
        if not os.path.isfile(os.path.join(folder, file)): 
            continue
        
        splits = file.split(".")
        if len(splits) != 3 or not splits[1].isdigit():
            out["other"].append(file)
            continue

        name, frame, extension = splits
        sequence_name = name + "." + extension
        
        if sequence_name not in out["sequences"]:
            out["sequences"][sequence_name] = dict({
                "frames": [],
                "missing": [],
                "count": 0
            })

        out["sequences"][sequence_name]["frames"].append(int(frame))

    for sequence in out["sequences"].values():
        frames = sorted(set(sequence["frames"]))

        sequence["missing"] = [
            frame
            for frame in range(frames[0], frames[-1] + 1)
            if frame not in frames
        ]

        if frames[0] == frames[-1]:
            sequence["frames"] = str(frames[0])
        else:
            sequence["frames"] = f"{frames[0]}-{frames[-1]}"

        sequence["count"] = len(frames)

    out["other"] = sorted(out["other"])
    return out

def report_lines(result: dict[str, Any]) -> list[str]:
    """Return the report: one line per sequence, sorted, then the other files."""
    lines = []
    for name, sequence in sorted(result["sequences"].items()):
        frames = sequence["frames"]
        missing = sequence["missing"]
        
        if missing:
            missing_str = ", ".join(str(frame) for frame in missing)
            status = f"(missing {missing_str})"
        else:
            status = "(complete)"
        
        lines.append(f"{name}: {frames} {status}")

    if result["other"]:
        other = ", ".join(result["other"])
    else:
        other = "none"
    lines.append(f"Other: {other}")
    
    return lines

def main(args: list[str]) -> int:
    """Print the report for FOLDER, save the inventory to OUTPUT; return 0, 1 (missing frames), or 2."""
    if len(args) != 2:
        print("usage: shot-inventory FOLDER OUTPUT")
        return 2
    
    folder, output = args
    
    if not os.path.isdir(folder):
        print(f"error: {folder} is not a folder")
        return 2
    
    result = inventory(folder) 

    for line in report_lines(result):
        print(line)

    with open(output, mode="w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    for sequence in result["sequences"].values():
        if sequence["missing"]:
            return 1
 
    return 0

# TODO: the guard: when this file is run directly, unpack sys.argv and exit with main(args)
if __name__ == "__main__":
    script, *args = sys.argv
    sys.exit(main(args))