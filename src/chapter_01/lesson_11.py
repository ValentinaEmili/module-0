from __future__ import annotations

import os
import sys


def main(args: list[str]) -> int:
    """Print how many image files a folder holds; return 0, or 2 for bad input."""
    if len(args) != 1:
        print("usage: count-frames FOLDER")
        return 2
    
    folder = args[0]

    if not os.path.isdir(folder):
        print(f"error: {folder} is not a folder")
        return 2

    files = [
        file 
        for file in os.listdir(folder)
        if os.path.isfile(os.path.join(folder, file))
        and file.split(".")[-1].lower() in {'exr', 'dpx'}]
    print(f"{len(files)} image files")
    return 0


# TODO: the guard: when this file is run directly, unpack sys.argv and exit with main(args)
if __name__ == "__main__":
    script, *args = sys.argv
    sys.exit(main(args))