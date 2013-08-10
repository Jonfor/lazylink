#!/usr/bin/env python2

from argparse import ArgumentParser
import re

BUG_REG = re.compile(r'(bug\s?)([0-9]+)', re.IGNORECASE)

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
    for line in f:
        match = BUG_REG.search(line)
        if match is None:
            print line
            continue
        bug_no = match.group(2)
        desc = get_bugzilla_desc(bug_no)

        out = line[:match.start(1)]
        out += '{{Bug|' + bug_no + '}} - '
        out += desc
        out +=  ' ' + line[match.end(2):]
        print out

def get_bugzilla_desc(bug_no):
    # TODO: Scrape some webpages. Or find an API. Or something.
    return 'placeholder description'

if __name__ == '__main__':
    main()
