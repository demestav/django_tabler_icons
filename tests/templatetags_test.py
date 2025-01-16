from __future__ import annotations

from django.template import Context
from django.template import Template


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
