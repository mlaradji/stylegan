#!/usr/bin/python                                                  
"""
Draws heavily from https://stackoverflow.com/a/55029650/9954163.
"""

from PIL import Image                                              
import os, sys                       
from pathlib import Path

source_path = Path("/home/mlaradji/slow/projects/Produvia/tencent-ml-images/data/images")
target_path = Path("/home/mlaradji/slow/projects/Produvia/stylegan/data/tencent-ml-images/")
resolution = (1024, 1024)

def resize():
    for item in source_path.iterdir():
        if item.is_file():
            try:
                im = Image.open(item)
            except OSError:
                # Unable to open image.
                print(f"Unable to open image '{item}'. Skipping...")

            imResize = im.resize(resolution, Image.ANTIALIAS)
            imResize.save(target_path / item.with_suffix('.png').name, 'png', quality=100)

if __name__ == "__main__":
    assert source_path.is_dir(), source_path
    assert target_path.is_dir(), target_path
    resize()
