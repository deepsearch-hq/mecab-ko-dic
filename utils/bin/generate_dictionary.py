#!/usr/bin/python3
# -*-coding:utf-8-*-
import getpass

from sqlalchemy import create_engine

engine = None
db_conn = None


def connect_db(db_type, host, database, user, password):
    global engine
    global db_conn
    if db_type == 'mysql':
        url = 'mysql+mysqlconnector://%s:%s@%s/%s' % \
              (user, password, host, database)
        print('connect to ' + url)
        engine = create_engine(url)
        db_conn = engine.connect()
        return db_conn
    else:
        raise RuntimeError('Invalid db type: ' + type)


def get_pos_and_type_names():
    output = []
    sql = """
    SELECT pos, `type` FROM lexicon_new WHERE class IS NULL GROUP BY pos, `type`
    """
    rows = db_conn.execute(sql).fetchall()
    for row in rows:
        pos = row['pos']
        dic_type = row['type']
        if dic_type == '*':
            output.append(pos)
        else:
            output.append(pos + '-' + dic_type)
    return output


def main():
    user = input('User: ')
    password = getpass.getpass()
    connect_db('mysql', 'eunjeon.vps.phps.kr', 'eunjeon', user, password)
    names = get_pos_and_type_names()
    print(names)


if __name__ == '__main__':
    main()
