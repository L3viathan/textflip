import argparse
import sys

from .rotation import flip


def flip_cli():
    if not sys.stdin.isatty():
        lines = input().splitlines()
        for line in lines:
            print(flip(line))

        return

    parser = argparse.ArgumentParser()
    parser.add_argument('text')

    args = parser.parse_args()
    print(flip(args.text))
