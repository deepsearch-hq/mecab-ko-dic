__author__ = 'budditao'

import getpass
import os
import sys
import argparse
import pprint

script_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(script_path + '/..')
from tools.editors.xsn_editor import XsnEditor

def main():
    parser = argparse.ArgumentParser(prog='PROG')
    parser.add_argument('--host', help='host')
    parser.add_argument('-u', '--user', help='user')
    parser.add_argument('-p', '--password', default=None, help='password')
    parser.add_argument('-a', '--apply', default=False, action='store_true',
                        help='apply to database')
    args = parser.parse_args()
    if args.password is None:
        args.password = getpass.getpass()

    editor = XsnEditor('mysql', args.host, 'eunjeon', args.user, args.password)
    editor.edit(args.apply)


if __name__ == '__main__':
    main()
