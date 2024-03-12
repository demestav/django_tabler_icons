from __future__ import annotations

from django.core.management.base import BaseCommand
from tabler_icons import icon_directory
from tabler_icons.utils import download_icons


class Command(BaseCommand):
    """Django management command "download_icons".

    Download the icon set from the Tabler Icons GitHub repository and
    extract it.
    """

    help = "Downloads the icon set from the Tabler Icons GitHub repository."

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.NOTICE("Downloading icons to %s" % icon_directory))
        download_icons(icon_directory)
