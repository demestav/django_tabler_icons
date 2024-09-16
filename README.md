> If you are upgrading from 0.4.0, note that the default download location for icons has changed. Icons are now downloaded to the directory specified by the `XDG_DATA_HOME` environment variable, defaulting to `<user_home_directory>/.local/share/django-tabler-icons/icons` if not set. This change aligns with the XDG Base Directory Specification. If you have `TABLER_ICONS_DIR` set in your Django settings, it will take precedence. The previous default location was `<user_home_directory>/.config/django-tabler-icons/icons`, which you may want to remove if no longer needed.

# Django tabler icons
Use [the tabler](https://github.com/tabler/tabler-icons) icon set in your Django project.

## Installation
Install the package from PyPI:
```bash
python -m pip install django-tabler-icons
```

Add `tabler_icons` to your `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...
    'tabler_icons',
    ...
]
```

Download the icon set:
```bash
python manage.py download_icons
```

Icons will be downloaded to `<user_home_directory>/.config/django-tabler-icons`. You can override this by setting the `TABLER_ICONS_DIR` setting, in project settings. This command requires to load Django.

### Alternative download method

Icons can also be downloaded without loading Django using:
```bash
django_tabler_icons download
```
which will download the icon set to `<user_home_directory>/.config/django-tabler-icons`. This requires user confirmation to proceed. By passing `--yes` or `-y` as an argument, the confirmation is skipped.

## Usage

To add an icon to your template, use the `tabler_icon` template tag:
```django
{% load tabler_icons %}

{% tabler_icon '<icon_name>' %}
```

If you need to add classes to the icon, use the second argument:
```django
{% tabler_icon '<icon_name>' '<class_name_1> <class_name_2>' %}
```

The icons come with some default classes which you can remove by passing `no` to the third argument (`keep_default_classes`)
```django
{% tabler_icon '<icon_name>' '<class_name_1> <class_name_2>' 'no' %}
```

> The default is to keep the default classes so you can omit the third argument if you want to keep them.

## Relevant projects

[Heroicons](https://github.com/adamchainz/heroicons) is a package for using [heroicons](https://heroicons.com) in Django projects, which is also the inspiration for this package.
