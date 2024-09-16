from __future__ import annotations

import os
import pathlib

from django.conf import settings

# Check if django is loaded and setting is set
if "DJANGO_SETTINGS_MODULE" in os.environ and hasattr(settings, "TABLER_ICONS_DIR"):
    icon_directory = pathlib.Path(settings.TABLER_ICONS_DIR)
else:
    icon_directory = (
        pathlib.Path(
            os.environ.get("XDG_DATA_HOME", pathlib.Path.home() / ".local" / "share")
        )
        / "django-tabler-icons"
        / "icons"
    )
