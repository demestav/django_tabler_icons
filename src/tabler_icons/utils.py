from __future__ import annotations

import io
import pathlib
import shutil
import tempfile
from functools import lru_cache
from urllib.request import urlopen
from zipfile import ZipFile

from tabler_icons import icon_directory


@lru_cache(maxsize=128)
def read_icon(icon_name):
    """Read the icon code from the icon file."""
    icon_path = icon_directory / f"{icon_name}.svg"

    if not icon_path:
        raise ValueError("Icon %s not found" % icon_name)

    with open(icon_path) as f:
        icon_code = f.read()

    return icon_code


def download_icons(download_diretory):
    """Download the icon set to the provided directory."""
    download_diretory.mkdir(parents=True, exist_ok=True)

    tmp_dir = tempfile.TemporaryDirectory()
    svg_source_dir = pathlib.Path(tmp_dir.name) / "svg"

    with urlopen(
        (
            "https://github.com/tabler/tabler-icons/releases/"
            "download/v3.17.0/tabler-icons-3.17.0.zip"
        ),
    ) as zipresp:
        with ZipFile(io.BytesIO(zipresp.read())) as zfile:
            zfile.extractall(tmp_dir.name)

    for svg_file in svg_source_dir.iterdir():
        shutil.copy(svg_file, download_diretory)

    tmp_dir.cleanup()
