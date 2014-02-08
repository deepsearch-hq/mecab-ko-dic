#!/usr/bin/python3
# -*-coding:utf-8-*-
"""
DB에 오류가 있을 때, 사용되는 스크립트의 샘플
"""
import getpass
import os
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

script_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(script_path + '/..')

engine = None
db_session = None
base_dir = os.path.dirname(os.path.realpath(__file__))


def connect_db(db_type, host, database, user, password):
    global engine
    global db_session
    if db_type == 'mysql':
        url = 'mysql+mysqlconnector://%s:%s@%s/%s' % \
              (user, password, host, database)
        print('connect to ' + url)
        engine = create_engine(url)
        Session = sessionmaker(bind=engine)
        db_session = Session()
        return db_session
    else:
        raise RuntimeError('Invalid db type: ' + type)


def edit():
    global db_session
    sql = """
    select * from lexicon_new where `type`='Preanalysis';
    """
    rows = db_session.execute(sql).fetchall()
    for row in rows:
        id = row[0]
        semantic_class = row[3]
        index_expr = row[9]
        # print(row)
        modified_index_expr = index_expr.replace('*/*', '*/1')
        modified_index_expr = modified_index_expr.replace('*/인명', '인명/1')
        modified_index_expr = modified_index_expr.replace('*/지명', '지명/1')
        #print(id, modified_index_expr)
        if index_expr != modified_index_expr:
            print(index_expr, '->', modified_index_expr)
            sql = """
            UPDATE lexicon_new set index_expression=:expr where id=:id
            """
            db_session.execute(sql, {'expr': modified_index_expr, 'id': id})
    db_session.commit()


def main():
    host = input('Host: ')
    user = input('User: ')
    password = getpass.getpass()
    connect_db('mysql', host, 'eunjeon', user, password)
    edit()


if __name__ == '__main__':
    main()
