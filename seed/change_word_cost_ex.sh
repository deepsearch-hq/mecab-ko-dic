#!/bin/bash -x

# '이'로 시작하는 인명의 출현 비용을 낮춤
#   -- 이/MM+승기/NNG와 같이 분석되는 것을 방지
cost=3500
sed -i -re "s/(^이[^,]+,[0-9]+,[0-9]+,)([-0-9]+)(,NNP,인명,)/\\1$cost\\3/g" ../final/Person.csv
sed -i -re "s/(^이[^,]+,[0-9]+,[0-9]+,)([-0-9]+)(,NNP,인명,)/\\1$cost\\3/g" ../final/Person-actor.csv
