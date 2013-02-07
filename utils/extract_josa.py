#!/usr/bin/python3
# -*-coding:utf-8-*-
'''
세종 XML 전자사전에서 조사를 뽑아서 출력하는 스크립트.
@author: bibreen <bibreen@gmail.com>
'''

import os
import re
from bs4 import BeautifulSoup
from write_dic import getEndWithJongSung

def extract(dir):
    for fileName in os.listdir(dir):
        if fileName[-4:] != '.xml':
            continue
        with open(dir + '/' + fileName, mode='r', encoding='utf-8') as file:
            soup = BeautifulSoup(file.read())

            surface = fileName[0:-4]
            posTags = soup.find_all('je_subtype')
            for tag in posTags:
                if tag.string[0] == 'j':
                    print('%s,0,0,0,%s,%s,%s,*,*,*,*' %
                          (surface,
                           tag.string.upper(),
                           getEndWithJongSung(surface),
                           surface))
 

if __name__ == '__main__':
    extract('/home/deicide/Shared/10. 조사_상세')
