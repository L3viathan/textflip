from unicodedata import normalize

import pytest
from .rotation import flip


@pytest.mark.parametrize(
    ["text"],
    [
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ",),
        ("abcdefghijklmnopqrstuvwxyz",),
        ("Ich grüße die schöne Straße",),
        ("Brânza pute, țânțar stinge",),
        (r"∑€®țΩ¨îø@∆ăºșªâℊ√©\≈~µ",),
        ("iîııîi",),
    ],
)
def test_double_is_nothing(text):
    flipped = flip(flip(text))

    assert normalize("NFD", flipped) == normalize("NFD", text)
