from __future__ import annotations

import io
import pathlib
import shutil
import tempfile
from urllib.request import urlopen
from zipfile import ZipFile

from django.core.management.base import BaseCommand
from tabler_icons import icon_directory


class Command(BaseCommand):
    """Django management command "download_icons".

    Download the icon set from the Tabler Icons GitHub repository and
    extract it.
    """

    help = "Downloads the icon set from the Tabler Icons GitHub repository."

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.NOTICE("Downloading icons to %s" % icon_directory))

        icon_directory.mkdir(parents=True, exist_ok=True)

        tmp_dir = tempfile.TemporaryDirectory()
        svg_source_dir = pathlib.Path(tmp_dir.name) / "svg"

        with urlopen(
            (
                "https://github.com/tabler/tabler-icons/releases/"
                "download/v2.4.0/tabler-icons-2.4.0.zip"
            ),
        ) as zipresp:
            with ZipFile(io.BytesIO(zipresp.read())) as zfile:
                zfile.extractall(tmp_dir.name)

        for svg_file in svg_source_dir.iterdir():
            shutil.copy(svg_file, icon_directory)

        tmp_dir.cleanup()
