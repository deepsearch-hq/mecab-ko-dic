#!/usr/bin/python3
# -*-coding:utf-8-*-
'''
세종 XML 전자사전에서 복합명사(NN)를 뽑아서 출력하는 스크립트.
@author: bibreen <bibreen@gmail.com>
'''

import os
import re
from bs4 import BeautifulSoup

def makeMorphList(s):
    result = list()
    morphs = s.split('+')
    for item in morphs:
        if item == 'ㅅ':
            prevItem = result.pop()
            prevLastCharCode = ord(prevItem[-1])
            newItem = prevItem[0:-1] + chr(prevLastCharCode + 19)
            result.append(newItem)
        else:
            result.append(item)
    return result

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
                if strValue == None or strValue == '':
                    continue
                if strValue.find('+') < 0 and strValue.find('-') < 0:
                    continue
           
            surface = fileName[0:-4] 
            strValue = strValue.replace('-', '+')
            changedStrValue = re.sub(r'[{(n)}]', r'', strValue)
            morphs = makeMorphList(changedStrValue)
            joinStr = ''.join(morphs)
            if surface == joinStr:
                if morphs[-1] == '이':
                    # 단일 명사로 취급할 목록 표시
                    print(surface + ',' + '+'.join(morphs) + ',1')
                else: 
                    print(surface + ',' + '+'.join(morphs) + ',2')
            else:
                print(surface + ',' + strValue + ',10') # 손으로 수정할 표시
            #print(fileName[0:-4])
#        break

if __name__ == '__main__':
    extract('/home/deicide/Shared/01. 체언_기초')
