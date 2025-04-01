from __future__ import annotations

import re

from django import template
from django.utils.html import mark_safe

from tabler_icons.utils import read_icon

register = template.Library()


@register.simple_tag
def tabler_icon(icon_name, classes=None, keep_default_classes="yes"):
    return tabler_icon_outline(icon_name, classes, keep_default_classes)


@register.simple_tag
def tabler_icon_outline(icon_name, classes=None, keep_default_classes="yes"):
    return _load_icon("outline", icon_name, classes, keep_default_classes)


@register.simple_tag
def tabler_icon_filled(icon_name, classes=None, keep_default_classes="yes"):
    return _load_icon("filled", icon_name, classes, keep_default_classes)


def _load_icon(icon_style, icon_name, classes, keep_default_classes):
    if classes is None:
        classes = []
    elif isinstance(classes, str):
        classes = classes.split(",")

    icon_code = mark_safe(read_icon(icon_style, icon_name))

    class_attribute_regex = re.compile(r'class="(.*?)"')
    match = class_attribute_regex.search(icon_code)

    # Set classes
    existing_classes = match.group(1).split(" ") if match else []

    if keep_default_classes == "yes":
        classes = existing_classes + classes

    class_string = " ".join(classes)

    if match:
        updated_icon_code = class_attribute_regex.sub(
            f'class="{class_string}"',
            icon_code,
        )
    else:
        updated_icon_code = icon_code.replace(">", f' class="{class_string}">', 1)

    updated_icon_code = updated_icon_code.strip()

    return mark_safe(updated_icon_code)
