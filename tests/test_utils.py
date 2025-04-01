import pytest

from tabler_icons.utils import read_icon


def test_unknown_icon_style_raises_exception():
    """
    Only "outline" and "filled" are valid icon styles.
    """

    with pytest.raises(ValueError) as excinfo:
        read_icon("email", "random-style")

    assert "Incompatible style" in str(excinfo.value)
