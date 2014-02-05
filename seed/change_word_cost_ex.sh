#!/bin/bash

if [ -z "`command -v gawk`" ]; then
    AWK=awk
    LENGTH_3=9
    LENGTH_2=6
else
    AWK=gawk
    LENGTH_3=3
    LENGTH_2=2
fi
TARGET_DIR='../final'
for each in `ls $TARGET_DIR/Person*.csv $TARGET_DIR/Place*.csv`; do
    echo "change word cost in $each ..."
    cat $each | $AWK -F ',' -v length_3=$LENGTH_3 -v length_2=$LENGTH_2 'BEGIN {
        OFS = ","
    }
    {
        if (length($1) == length_2) {
            decr_cost = int($4 * 0.7);
        } else if (length($1) >= length_3) {
            decr_cost = int($4 * 0.6);
        } else {
            decr_cost = $4
        }
        print($1,$2,$3,decr_cost,$5,$6,$7,$8,$9,$10,$11,$12,$13)
    }' > $each.tmp
    rm -f $each
    mv $each.tmp $each
done
