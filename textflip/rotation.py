from unicodedata import normalize, name
import regex

from .data import hacky_pairs, dia_pairs, rotations


def decompose(text):
    text = normalize("NFD", text)
    for a, b in hacky_pairs:
        text = text.replace(b, a)
    return text


def _maybe_westernize(match):
    # Sadly, i does not decompose into ı and combining dot above.
    # Therefore, we have to transform ı + diacritics into i + diacritics.
    # However, if we always do this we end up with double dots if the i is
    # supposed to be upside-down.
    diacritic = match.group(1)
    if name(diacritic).endswith("BELOW"):
        return "ı{}".format(diacritic)
    return "i{}".format(diacritic)


def compose(text):
    for a, b in hacky_pairs:
        text = text.replace(a, b)
    return regex.sub(r"ı(\p{Mn})", _maybe_westernize, text)


def get_dia_map():
    for pair in dia_pairs:
        assert len(pair) == 4, pair

    dmap = {}

    for _, a, __, b in dia_pairs:
        dmap[a] = b
        dmap[b] = a
    return dmap


dia_map = get_dia_map()


def get_rotation_map():
    rmap = {}

    for a, b in rotations:
        rmap[a] = b
        rmap[b] = a
    return rmap


rotation_map = get_rotation_map()


def flip(text):
    return "".join(
        flop(char)
        for char in reversed(regex.findall(r"\P{Mn}\p{Mn}*", decompose(text)))
    )


def flop(char):
    dia = ""
    if len(char) > 1:
        char, *_, dia = char
        dia = dia_map.get(dia, dia)
    return compose(rotation_map.get(char, char) + dia)
