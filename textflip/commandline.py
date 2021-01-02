import argparse

from .rotation import flip


def flip_cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('text')

    args = parser.parse_args()
    print(flip(args.text))
