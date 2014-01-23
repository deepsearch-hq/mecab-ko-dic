#!/bin/bash

if [ -z "`command -v gawk`" ]; then
    AWK=awk
    MIN_LENGTH=9
else
    AWK=gawk
    MIN_LENGTH=3
fi
TARGET_DIR='../final'
for each in `ls $TARGET_DIR/Person*.csv $TARGET_DIR/Place*.csv`; do
    echo "change word cost in $each ..."
    cat $each | $AWK -F ',' -v min_length=$MIN_LENGTH 'BEGIN {
        OFS = ","
    }
    {
        if (length($1) >= min_length) {
            decr_cost = int($4 * 0.6);
        } else {
            decr_cost = $4
        }
        print($1,$2,$3,decr_cost,$5,$6,$7,$8,$9,$10,$11,$12,$13)
    }' > $each.tmp
    rm -f $each
    mv $each.tmp $each
done
