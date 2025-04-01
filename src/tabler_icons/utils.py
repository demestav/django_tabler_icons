from __future__ import annotations

import io
import pathlib
import shutil
import tempfile
from functools import lru_cache
from urllib.request import urlopen
from zipfile import ZipFile

from tabler_icons import get_icon_directory


@lru_cache(maxsize=128)
def read_icon(icon_style, icon_name):
    """Read the icon code from the icon file."""
    if icon_style == "outline":
        icon_path = get_icon_directory() / "outline" / f"{icon_name}.svg"
    elif icon_style == "filled":
        icon_path = get_icon_directory() / "filled" / f"{icon_name}.svg"
    else:
        raise ValueError("Incompatible style %s" % icon_style)

    if not icon_path.exists():
        raise ValueError("Icon %s not found" % icon_name)

    try:
        with open(icon_path, encoding="utf-8") as f:
            icon_code = f.read()
    except Exception as e:
        raise ValueError(f"Error reading icon {icon_name}: {e}")
    else:
        return icon_code


def download_icons(download_diretory):
    """Download the icon set to the provided directory."""
    download_diretory.mkdir(parents=True, exist_ok=True)

    outline_dest_dir = download_diretory / "outline"
    outline_dest_dir.mkdir(exist_ok=True)
    filled_dest_dir = download_diretory / "filled"
    filled_dest_dir.mkdir(exist_ok=True)

    tmp_dir = tempfile.TemporaryDirectory()
    svg_source_dir = pathlib.Path(tmp_dir.name) / "svg"

    outline_source_dir = svg_source_dir / "outline"
    filled_source_dir = svg_source_dir / "filled"

    with urlopen(
        (
            "https://github.com/tabler/tabler-icons/releases/"
            "download/v3.31.0/tabler-icons-3.31.0.zip"
        ),
    ) as zipresp:
        with ZipFile(io.BytesIO(zipresp.read())) as zfile:
            zfile.extractall(tmp_dir.name)

    for svg_file in outline_source_dir.iterdir():
        shutil.copy(svg_file, outline_dest_dir)

    for svg_file in filled_source_dir.iterdir():
        shutil.copy(svg_file, filled_dest_dir)

    tmp_dir.cleanup()
