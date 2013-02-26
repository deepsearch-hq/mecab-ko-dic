#!/usr/bin/python3
# -*-coding:utf-8-*-
'''
ksd_dic2.txt에서 한자 사전을 뽑아서 출력하는 스크립트. 명사, 어근, 접두사,
접미사를 뽑았으며 각각의 표제어를 뽑는 쉘 명령어는 다음과 같다.

grep 「명사」 ~/Shared/ksd_dic2.txt | awk 'BEGIN {FS="|"} {if (index($1, "-") == 0 && index($1, "^") == 0) {print $0}}' | cut -f 1
grep '의 어근.' ~/Shared/ksd_dic2.txt | grep -v 「명사」 | awk 'BEGIN {FS="|"} {if (index($1, "-") == 0 && index($1, "^") == 0) {print $0}}' | cut -f 1
grep 「접사」 ~/Shared/ksd_dic2.txt | grep '접미사.' | cut -f 1 | sed 's/-//g'
grep 「접사」 ~/Shared/ksd_dic2.txt | grep '접두사.' | cut -f 1 | sed 's/-//g'
'''

import sys

def hasAscii(s):
    for c in s:
        uni = ord(c)
        if (0x0021 >= uni and uni <= 0x002F) or \
            (0x003A >= uni and uni <= 0x0040) or \
            (0x005B >= uni and uni <= 0x0060) or \
            (0x007B >= uni and uni <= 0x007E):
            return True
    return False

def getEndWithJongSung(s):
    if not isHangul(s[-1]):
        return '*'
    if endWithJongSung(s):
        return 'T'
    else:
        return 'F'

def isHangul(s):
    for c in s:
        uni = ord(c)
        if not ((0xAC00 <= uni and uni <= 0xD7A3) or
               (0x3130 <= uni and uni <= 0x318F) or
               (0x1100 <= uni and uni <= 0x11FF)):
            return False
    return True

def isHanja(s):
    for c in s:
        uni = ord(c)
        if not ((0x2E80 <= uni and uni <= 0x2EF3) or
               (0x3400 <= uni and uni <= 0x4DB5) or
               (0x4E00 <= uni and uni <= 0x9FA5) or
               (0xF900 <= uni and uni <= 0xFA2D) or
               (0xFA30 <= uni and uni <= 0xFA6A)):
            return False
    return True

def endWithJongSung(s):
    if not isHangul(s[-1]):
        return False
    lastChar = s[-1]
    uni = ord(lastChar)
    if uni >= 44032 and uni <= 55203 and ((uni - 44032) % 28 > 0):
        return True
    else:
        return False

if __name__ == '__main__':
    tag = sys.argv[1]

    for line in sys.stdin:
        line = line.strip()
        if line == '':
            continue
        items = line.split('|')
        if len(items) < 3:
            continue
        surface = items[0]
        pron = items[1]
        hanjaStrings = items[2].split('/')

        if not isHangul(pron):
            continue

        for hanja in hanjaStrings:
            if isHanja(hanja):
                jongSungType = 'F'
                if endWithJongSung(pron):
                    jongSungType = 'T'
                print('%s,0,0,0,%s,%s,%s,*,*,*,*' %
                        (hanja,
                        tag,
                        jongSungType,
                        pron))
