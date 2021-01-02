import sys

from .rotation import flip


def flip_cli():
    if len(sys.argv) > 1:
        print(flip(sys.argv[1]))
        return

    try:
        for line in sys.stdin:
            print(flip(line.rstrip()))
    except KeyboardInterrupt:
        print()
