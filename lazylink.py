#!/usr/bin/env python2

from argparse import ArgumentParser
import json
import re
import urllib2

# BZ_URL = 'https://api-dev.bugzilla.mozilla.org/test/1.3/'
BZ_URL = 'https://api-dev.bugzilla.mozilla.org/1.3/'

BUG_REG = re.compile(r'(bug\s?)([0-9]+)', re.IGNORECASE)

# TODO: PEP8
# TODO: Cache JSON in /tmp.
# TODO: Use API to search for bugs assigned in the past week?
def main():
    args = set_and_parse_args()

    for f in args.files:
        lazylink_file(f)

def set_and_parse_args():
    # TODO: ArgumentParser desc.
    parser = ArgumentParser()
    parser.add_argument('files', type=file, nargs='+')

    return parser.parse_args()

def lazylink_file(f):
    for line in f:
        # TODO: Extract this out so more regex can be registered.
        match = BUG_REG.search(line)
        if match is None:
            print line
            continue
        bug_no = match.group(2)
        desc = get_bugzilla_desc(bug_no)

        if not desc:
            continue

        out = line[:match.start(1)]
        out += '{{Bug|' + bug_no + '}} - '
        out += desc
        out +=  ' ' + line[match.end(2):]
        print out

def get_bugzilla_desc(bug_no):
    url = BZ_URL + 'bug/' + bug_no
    try:
        bug_info = json.load(urllib2.urlopen(url))
    except urllib2.HTTPError, err:
        if err.code == 400:
            print 'Cannot access bug #' + bug_no + '. It may be security locked.\n'
            return ''
    return bug_info['summary']

if __name__ == '__main__':
    main()
