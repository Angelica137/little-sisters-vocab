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


def test_make_word_groups_auto():
    assert make_word_groups(['auto', 'didactic', 'graph', 'mate']
                            ) == 'auto :: autodidactic :: autograph :: automate'


def test_make_word_groups_inter():
    assert make_word_groups(['inter', 'twine', 'connected', 'dependent']
                            ) == 'inter :: intertwine :: interconnected :: interdependent'


def test_remove_suffix_ness_y():
    assert remove_suffix_ness('heaviness') == 'heavy'


def test_remove_suffix_ness():
    assert remove_suffix_ness('sadness') == 'sad'


def test_adjective_to_verb_bright():
    assert adjective_to_verb('I need to make that bright.', -1) == 'brighten'


def test_adjective_to_verb_darken():
    assert adjective_to_verb('It got dark as the sun set.', 2) == 'darken'
