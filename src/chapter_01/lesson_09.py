from __future__ import annotations

import os
from pathlib import Path
def list_files(folder: str) -> list[str]:
    """Return the sorted names of the files (not folders) directly inside folder."""
    return sorted(
        file 
        for file in os.listdir(folder) 
        if os.path.isfile(os.path.join(folder, file)))

def image_files(folder: str) -> list[str]:
    """Return the sorted names of the .exr and .dpx files directly inside folder, any case."""
    return sorted(
        file 
        for file in os.listdir(folder) 
        if os.path.isfile(os.path.join(folder, file))
        and file.split(".")[-1].lower() in {'exr', 'dpx'})
