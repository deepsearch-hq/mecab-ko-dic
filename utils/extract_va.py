#!/usr/bin/python3
# -*-coding:utf-8-*-
'''
세종 XML 전자사전에서 용언/형용사(VA)를 뽑아서 출력하는 스크립트.
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
                    #print(strValue)
                    if strValue[0] == 'N':
                        continue
                    if strValue[-2:] == '.하':
                        continue
                    if strValue[-3:] == '.이4':
                        continue
               
            if strValue == None:
                strValue = '*'
#            print(strValue + ':' + fileName[0:-5])
            print(fileName[0:-5])
#        break

if __name__ == '__main__':
    extract('/home/deicide/Shared/02. 용언_기초/va')
    # 기초에서 빠진 것 중에 들어가야 하는 형용사 출력
    tp = (
        '게을러빠지',
        '게을러터지',
        '괜하',
        '괴이쩍',
        '귀설',
        '그렁하',
        '길둥글',
        '까지',
        '깡마르',
        '끄므레하',
        '낡',
        '노오랗',
        '녹작지근하',
        '도드라지',
        '동떨어지',
        '되먹',
        '되바라지',
        '두드러지',
        '딱부러지',
        '막되',
        '뭉텅하',
        '뭉툭뭉툭하',
        '뭉툭하',
        '변변찮',
        '비',
        '새되',
        '수굿하',
        '쓸모없',
        '쓸모있',
        '애긋',
        '약아빠지',
        '엉거주춤하',
        '엔간하',
        '여북하',
        '웅숭깊',
        '으스름하',
        '잘빠지',
        '조붓하',
        '졸리',
        '주되',
        '째지',
        '척하',
        '켸켸묵',
        '파아랗',
        '편벽되',
        '푸르르',
        '하릴없',
        '한갓되',
        '해묵',
        '혼곤하',
        '흐벅지',
          )
    for each in tp:
        print(each)