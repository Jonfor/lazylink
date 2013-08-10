#!/usr/bin/env python2

from argparse import ArgumentParser

def main():
    args = set_and_parse_args()
    for f in args.files:
        lazylink_file(f)

def set_and_parse_args():
    # TODO: ArgumentParser desc.
    parser = ArgumentParser()
    parser.add_argument('files', type=file, nargs='*')
    return parser.parse_args()

def lazylink_file(f):
    pass

if __name__ == '__main__':
    main()
