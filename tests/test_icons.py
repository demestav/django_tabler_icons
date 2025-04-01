from __future__ import annotations

import pathlib

from django.template import Context
from django.template import Template

from tabler_icons import get_icon_directory


def test_icon_load():
    template = Template(
        "{% load tabler_icons %}{% tabler_icon 'number-123' %}",
    )

    result = template.render(Context())
    assert (
        result.strip()
        == """<svg
  xmlns="http://www.w3.org/2000/svg"
  width="24"
  height="24"
  viewBox="0 0 24 24"
  fill="none"
  stroke="currentColor"
  stroke-width="2"
  stroke-linecap="round"
  stroke-linejoin="round"
  class="icon icon-tabler icons-tabler-outline icon-tabler-number-123"
>
  <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
  <path d="M3 10l2 -2v8" />
  <path d="M9 8h3a1 1 0 0 1 1 1v2a1 1 0 0 1 -1 1h-2a1 1 0 0 0 -1 1v2a1 1 0 0 0 1 1h3" />
  <path d="M17 8h2.5a1.5 1.5 0 0 1 1.5 1.5v1a1.5 1.5 0 0 1 -1.5 1.5h-1.5h1.5a1.5 1.5 0 0 1 1.5 1.5v1a1.5 1.5 0 0 1 -1.5 1.5h-2.5" />
</svg>""".strip()
    )


def test_icon_load_dont_keep_default_classes():
    template = Template(
        "{% load tabler_icons %}{% tabler_icon 'number-123' keep_default_classes='no' %}",
    )

    result = template.render(Context())
    assert (
        result.strip()
        == """<svg
  xmlns="http://www.w3.org/2000/svg"
  width="24"
  height="24"
  viewBox="0 0 24 24"
  fill="none"
  stroke="currentColor"
  stroke-width="2"
  stroke-linecap="round"
  stroke-linejoin="round"
  class=""
>
  <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
  <path d="M3 10l2 -2v8" />
  <path d="M9 8h3a1 1 0 0 1 1 1v2a1 1 0 0 1 -1 1h-2a1 1 0 0 0 -1 1v2a1 1 0 0 0 1 1h3" />
  <path d="M17 8h2.5a1.5 1.5 0 0 1 1.5 1.5v1a1.5 1.5 0 0 1 -1.5 1.5h-1.5h1.5a1.5 1.5 0 0 1 1.5 1.5v1a1.5 1.5 0 0 1 -1.5 1.5h-2.5" />
</svg>""".strip()
    )


def test_icon_load_add_extra_classes():
    template = Template(
        "{% load tabler_icons %}{% tabler_icon 'number-123' 'class-1 class-2' %}",
    )

    result = template.render(Context())
    assert (
        result.strip()
        == """<svg
  xmlns="http://www.w3.org/2000/svg"
  width="24"
  height="24"
  viewBox="0 0 24 24"
  fill="none"
  stroke="currentColor"
  stroke-width="2"
  stroke-linecap="round"
  stroke-linejoin="round"
  class="icon icon-tabler icons-tabler-outline icon-tabler-number-123 class-1 class-2"
>
  <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
  <path d="M3 10l2 -2v8" />
  <path d="M9 8h3a1 1 0 0 1 1 1v2a1 1 0 0 1 -1 1h-2a1 1 0 0 0 -1 1v2a1 1 0 0 0 1 1h3" />
  <path d="M17 8h2.5a1.5 1.5 0 0 1 1.5 1.5v1a1.5 1.5 0 0 1 -1.5 1.5h-1.5h1.5a1.5 1.5 0 0 1 1.5 1.5v1a1.5 1.5 0 0 1 -1.5 1.5h-2.5" />
</svg>""".strip()
    )


def test_icon_directory_from_settings(settings):
    """
    The `get_icon_directory` should return the directory defined in django settings.
    """
    # Arrange
    settings.TABLER_ICONS_DIR = "/test_icon_dir"

    # Act
    get_icon_directory.cache_clear()
    icon_directory = get_icon_directory()

    # Assert
    assert icon_directory == pathlib.Path("/test_icon_dir")


def test_icon_directory_default(settings):
    """
    If not defined in settings, the icon directory should be based on XDG_DATA_HOME.

    *Not sure how to test this, since each system has different path as XDG_DATA_HOME.*
    """
    # Arrange
    delattr(settings, "TABLER_ICONS_DIR")

    # Act
    get_icon_directory.cache_clear()
    icon_directory = get_icon_directory()

    # Assert
    assert icon_directory.as_posix().endswith(".local/share/django-tabler-icons/icons")
