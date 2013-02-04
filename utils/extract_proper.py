#!/usr/bin/python3
# -*-coding:utf-8-*-
'''
세종 XML 전자사전에서 고유명사(사람 이름, 집단 이름, 지역 이름)를 뽑아서
출력하는 스크립트.
@author: bibreen <bibreen@gmail.com>
'''

import os
import re
from bs4 import BeautifulSoup

def extract(dir, tagName, name, needEachTerm, maxLength=0):
    for fileName in os.listdir(dir):
        if fileName[-4:] != '.xml':
            continue
        with open(dir + '/' + fileName, mode='r', encoding='utf-8') as file:
            soup = BeautifulSoup(file.read())
            findTagName = soup.entry.find(tagName).string
            if findTagName == None or re.match(name, findTagName) == None:
                continue

            surface = fileName[0:-4]
            if maxLength > 0 and len(surface) > maxLength:
                continue

            strValue = None
            if soup.entry.str != None:
                strValue = soup.entry.str.string
                if  strValue != None:
                    strValue = soup.entry.str.string.strip()
                if strValue == None or strValue == '':
                    strValue = surface
            else:
                strValue = surface
           
            strValue = strValue.replace('+', ' ')

            items = strValue.split()
            if len(items) > 1:
                surface = surface.replace(' ', '')
                print(surface + "," + '+'.join(items))
                if needEachTerm == True:
                    for each in items:
                        print(each)
            else:
                print(surface)

if __name__ == '__main__':
    # 인명
    #extract('/home/deicide/Shared/18. 특수어_기초/1', 'class', '인명', True)
    #extract('/home/deicide/Shared/18. 특수어_기초/2', 'class', '구체물:구체자연물:생물:인간', True)
    # 집단 이름
    #extract('/home/deicide/Shared/18. 특수어_기초/1', 'class', '집단', False, 8)
    #extract('/home/deicide/Shared/18. 특수어_기초/2', 'class', '집단:인간집단:단체:기업', False, 8)
    # 장소
    extract('/home/deicide/Shared/17. 고유명사_기초', 'dom', '지리', True)
