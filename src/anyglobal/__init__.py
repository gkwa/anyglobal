import argparse
import logging
import sys


def parse_args(args):
    parser = argparse.ArgumentParser(description="Just a demonstration")
    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        const=logging.INFO,
    )
    parser.add_argument(
        "-vv",
        "--very-verbose",
        dest="loglevel",
        help="set loglevel to DEBUG",
        action="store_const",
        const=logging.DEBUG,
    )
    parser.add_argument(
        "-p",
        "--path",
        dest="path",
        help="path to input file",
    )

    return parser.parse_args(args)


def hello():
    return "Hello from anyglobal!"


def main(args):
    args = parse_args(args)

    if args.path:
        print(f"Path: {args.path}")

    print(hello())


def run():
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
