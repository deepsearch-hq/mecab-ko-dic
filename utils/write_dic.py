#!/usr/bin/python3
# -*-coding:utf-8-*-

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
        if not (0x0AC00 <= uni and uni <= 0xD7A3):
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
        items = line.split(',')
        surface = items[0]
        form = None
        if len(items) > 1:
            form = items[1]
        if not isHangul(surface):
            continue
        jongSungType = 'F'
        if endWithJongSung(surface):
            jongSungType = 'T'
        if form:
            print('%s,0,0,0,%s,%s,%s,Compound,*,*,%s' %
                    (surface,
                    tag,
                    getEndWithJongSung(surface),
                    surface,
                    form))
        else:
            print('%s,0,0,0,%s,%s,%s,*,*,*,*' %
                    (surface,
                    tag,
                    getEndWithJongSung(surface),
                    surface))
