from scripts.strings import *


def test_add_prefix_un_returns_unhappy():
    assert add_prefix_un("happy") == "unhappy"


def test_add_prefix_un_returns_unmanageable():
    assert add_prefix_un("manageable")


def test_make_word_groups_en():
    assert make_word_groups(
        ['en', 'close', 'joy', 'lighten']) == 'en :: enclose :: enjoy :: enlighten'


def test_make_word_groups_pre():
    assert make_word_groups(['pre', 'serve', 'dispose', 'position']
                            ) == 'pre :: preserve :: predispose :: preposition'
