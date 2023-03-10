from __future__ import annotations

from django.template import Context
from django.template import Template


def test_dummy():
    template = Template(
        "{% load tabler_icons %}{% tabler_icon '123' %}",
    )

    result = template.render(Context())
    assert (
        result == '<svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler'
        ' icon-tabler-123" width="24" height="24" viewBox="0 0 24 24"'
        ' stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round"'
        ' stroke-linejoin="round">\n  <path stroke="none" d="M0 0h24v24H0z"'
        ' fill="none"/>\n  <path d="M3 10l2 -2v8" />\n  <path d="M9 8h3a1 1 0 0 1 1'
        ' 1v2a1 1 0 0 1 -1 1h-2a1 1 0 0 0 -1 1v2a1 1 0 0 0 1 1h3" />\n  <path d="M17'
        " 8h2.5a1.5 1.5 0 0 1 1.5 1.5v1a1.5 1.5 0 0 1 -1.5 1.5h-1.5h1.5a1.5 1.5 0 0"
        ' 1 1.5 1.5v1a1.5 1.5 0 0 1 -1.5 1.5h-2.5" />\n</svg>'
    )
