#!/bin/bash
# 특정 형태소를 더 이상 분석하지 않도록 하는 사전(Atomic.csv)을 생성하는
# 스크립트
# 출현 비용을 낮춘 형태소를 새로 등록하는 방법으로 형태소 분석을 막는다.

DIC_PATH='../final'
CONF_FILE='atomic.txt'
DIC_FILE=$DIC_PATH/Atomic.csv
COST=-5000

while read line; do
    if [ "${line:0:1}" == "#" ]; then
        continue
    fi
    surface=$(echo $line | cut -d ',' -f 1)
    tag=$(echo $line | cut -d ',' -f 2)
    dic_line=$(grep -E -h -m 1 "^$surface,[0-9]+,[0-9]+,[0-9]+,$tag" $DIC_PATH/*.csv)
    echo $dic_line | cut -d ' ' -f 1 | awk -F ',' -v cost=$COST 'BEGIN {
        FS = ","
        OFS = ","
    }
    {
        print($1,$2,$3,cost,$5,$6,$7,$8,$9,$10,$11)
    }'
done < $CONF_FILE > $DIC_FILE
