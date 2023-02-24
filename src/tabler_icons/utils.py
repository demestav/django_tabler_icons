from __future__ import annotations

from functools import lru_cache

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
