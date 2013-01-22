#!/usr/bin/python3
# -*-coding:utf-8-*-
'''
세종 XML 전자사전에서 복합명사를 제외한 명사(NN)를 뽑아서 출력하는 스크립트.
@author: bibreen <bibreen@gmail.com>
'''

import os
from bs4 import BeautifulSoup

def extract(dir):
    for fileName in os.listdir(dir):
        if fileName[-4:] != '.xml':
            continue
        with open(dir + '/' + fileName, mode='r', encoding='utf-8') as file:
            soup = BeautifulSoup(file.read())
            strValue = '*'
            if soup.entry.str != None:
                strValue = soup.entry.str.string
                if  strValue != None:
                    strValue = soup.entry.str.string.strip()
                if strValue != None and strValue != '':
                    if strValue.find('+') > 0:
                        continue
                    if strValue.find('-') > 0:
                        continue
               
            if strValue == None:
                strValue = '*'
#            print(strValue + ':' + fileName[0:-5])
            print(fileName[0:-4])
#        break

if __name__ == '__main__':
    extract('/home/deicide/Shared/01. 체언_기초')
