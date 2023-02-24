from __future__ import annotations

import re

from django import template
from django.utils.html import mark_safe
from tabler_icons.utils import read_icon

register = template.Library()


@register.simple_tag
def tabler_icon(icon_name, classes=None, keep_default_classes="yes"):
    if classes is None:
        classes = []
    elif isinstance(classes, str):
        classes = classes.split(",")

    icon_code = mark_safe(read_icon(icon_name))

    class_attribute_regex = re.compile(r'class="(.*?)"')
    match = class_attribute_regex.search(icon_code)

    # Set classes
    if match is None:
        updated_icon_code = class_attribute_regex.sub(
            'class="%s"' % " ".join(classes),
            icon_code,
        )
    else:
        if keep_default_classes == "yes":
            classes = match.group(1).split(" ") + classes
        updated_icon_code = class_attribute_regex.sub(
            'class="%s"' % " ".join(classes),
            icon_code,
        )
    updated_icon_code = updated_icon_code.strip()

    return mark_safe(updated_icon_code)
