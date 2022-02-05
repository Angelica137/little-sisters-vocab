from scripts.strings import *


def test_add_prefix_un_returns_unhappy():
    assert add_prefix_un("happy") == "unhappy"


def test_add_prefix_un_returns_unmanageable():
    assert add_prefix_un("manageable")
