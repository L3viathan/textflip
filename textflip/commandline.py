import sys

from .rotation import flip


def flip_cli():
    if not sys.stdin.isatty():
        lines = sys.stdin.read().splitlines()
        for line in lines:
            print(flip(line))

        return

    if len(sys.argv) < 2:
        sys.stderr.write("Error: no text provided\n")
        sys.exit(1)

    print(flip(sys.argv[1]))
