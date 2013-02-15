#!/bin/bash

# matrix.def의 연접 비용을 변경하는 스크립트

DIC_PATH='../final'
MATRIX_DEF=matrix.def
LEFT_ID_DEF=left-id.def
RIGHT_ID_DEF=right-id.def

function get_left_id()
{
    local tag=$1
    local reading=$2

    grep -E -m 1 "^[0-9]+ $tag,\*,$reading" $DIC_PATH/$LEFT_ID_DEF | cut -d ' ' -f 1
}

function get_right_id()
{
    local tag=$1
    local has_last_jongsung=$2

    grep -E -m 1 "^[0-9]+ $tag,$has_last_jongsung" $DIC_PATH/$RIGHT_ID_DEF | cut -d ' ' -f 1
}

function get_connection_cost()
{
    local left_id=$1
    local right_id=$2

    grep -E -m 1 "^$right_id $left_id " $DIC_PATH/$MATRIX_DEF | cut -d ' ' -f 3
}

function get_sed_command_for_increasing_cost()
{
    local left_id=$1
    local right_id=$2
    local incr_num=$3

    local cost=$(get_connection_cost $left_id $right_id)
    local new_cost=$((cost + incr_num))
    echo "s/$right_id $left_id $cost\$/$right_id $left_id $new_cost/g"
}

## MAIN
ORG_MATRIX_DEF=matrix.def.org
cp $DIC_PATH/$MATRIX_DEF $DIC_PATH/$ORG_MATRIX_DEF

sed_patterns=''

# 종성으로 끝나는 명사와 주격 조사 '이'의 연접 비용을 늘림
incr_num=2400 # '김영삼 시절 이양호'가 제대로 분석되는 최소값 (백단위로 테스트)
right_id=$(get_right_id "NN" "T")
left_id=$(get_left_id "JKS" "이")
sed_patterns="$sed_patterns$(get_sed_command_for_increasing_cost $left_id $right_id $incr_num);"

echo "connection cost change... '$sed_patterns'"
sed "$sed_patterns" $DIC_PATH/$ORG_MATRIX_DEF > $DIC_PATH/$MATRIX_DEF
