from logchange.utils import dedent


def test_dedent():
    assert dedent("  a\n  b") == "a\nb"
    assert dedent("  a\n b") == " a\nb"
    assert dedent("\n  a\n b\n   \n") == " a\nb"
