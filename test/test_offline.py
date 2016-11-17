import os


def test_semantic_patched(cssfile):
    assert cssfile.read().match(r'.*(?!http).*')
