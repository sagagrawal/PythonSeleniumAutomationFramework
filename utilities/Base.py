import pytest


@pytest.mark.usefixtures("setup")
class Base:

    def clear_textbox(self, txtbox):
        txtbox.clear()
