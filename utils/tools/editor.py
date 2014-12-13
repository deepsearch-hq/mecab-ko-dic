#!/usr/bin/python3
# -*-coding:utf-8-*-

"""
DB에 오류가 있을 때, 사용되는 스크립트의 샘플
"""
import getpass
import os
import sys
import argparse
import pprint

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


script_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(script_path + '/..')
from dictionary.lexicon import Lexicon


class Editor(object):
    def __init__(self, db_type, host, database, user, password):
        self.db_type = db_type
        self.host = host
        self.database = database
        self.user = user
        self.password = password

        self.db_session = None

    def get_session(self):
        if self.db_session is None:
            self.__connect_db()
        return self.db_session

    def __connect_db(self):
        if self.db_type == 'mysql':
            url = 'mysql+mysqlconnector://%s:%s@%s/%s' % \
                  (self.user, self.password, self.host, self.database)
            print('connect to ' + url)
            engine = create_engine(url)
            Session = sessionmaker(bind=engine)

            self.db_session = Session()
        else:
            raise RuntimeError('Invalid db type: ' + type)

    def edit(self, is_apply):
        if is_apply is False:
            print("##################################################")
            print("This is TEST MODE. it's not aplplied to database.")
            print("for applying to database, use '-a' parameter.")
            print("##################################################")
        # rows = self.get_session().execute(query).fetchall()
        rows = self.get_query().all()
        for row in rows:
            if is_apply:
                print('writing to database.')
                self.modify(row)
            else:
                pprint.pprint(row.__dict__)

        if is_apply:
            self.get_session().commit()

    def get_query(self):
        # TODO: write select query
        return self.get_session().query(Lexicon).limit(1)

    def modify(self, lexicon):
        # TODO: rebuild lexicon object
        pass


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

    editor = Editor('mysql', args.host, 'eunjeon', args.user, args.password)
    editor.edit(args.apply)


if __name__ == '__main__':
    main()
