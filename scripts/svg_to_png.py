import sys
import os
from cairosvg import svg2png
from pathlib import Path

workspace = os.getenv('GITHUB_WORKSPACE')
files = Path(workspace)/'assets'/'files'

if not files.exists():
    print("Invalid directory")
    sys.exit()

def svg_to_png(archive: Path) -> None:
    if archive.suffix.lower() != ".png":
        return
    output_path = archive.with_suffix(".png")
    output_width = 128
    output_height = 128
    svg2png(url=str(archive), write_to=str(output_path), output_width=output_width, output_height=output_height)
    archive.unlink()

for archive in files.iterdir():
    svg_to_png(archive)
