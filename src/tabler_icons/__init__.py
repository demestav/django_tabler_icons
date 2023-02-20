from __future__ import annotations

import pathlib

from django.conf import settings

if hasattr(settings, "TABLER_ICONS_DIR"):
    icon_directory = pathlib.Path(settings.TABLER_ICONS_DIR)
else:
    icon_directory = pathlib.Path.home() / ".config" / "django-tabler-icons" / "icons"
