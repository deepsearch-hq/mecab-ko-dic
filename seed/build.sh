#/bin/bash

date
MECAB_EXEC_PATH=/usr/local/libexec/mecab
DICT_INDEX=$MECAB_EXEC_PATH/mecab-dict-index
DICT_GEN=$MECAB_EXEC_PATH/mecab-dict-gen
COST_TRAIN=$MECAB_EXEC_PATH/mecab-cost-train

# clear final directory
rm -f ../final/*.csv ../final/*.def ../final/*.def.org ../final/*.bin ../final/*.dic ../final/dicrc 
pushd ../final
./clean
popd

# clear seed directory
rm -f *.dic *.bin model model.txt
$DICT_INDEX -p -d . -c UTF-8 -t UTF-8 -f UTF-8

first="yes"
model_file="model"
for file in `ls corpus/*.txt`; do
	echo $file
	if [ "$first" == "yes" ]; then
		$COST_TRAIN -p 2 -c 1.0 $file ${model_file}.tmp
        if [ "$?" != 0 ]; then
            exit -1
        fi
		first="no"
	else
		$COST_TRAIN -p 2 -c 1.0 -M ${model_file} $file ${model_file}.tmp
        if [ "$?" != 0 ]; then
            exit -1
        fi
	fi

	rm -f ${model_file}
	mv ${model_file}.tmp ${model_file}
done

cp pos-id.def ../final/.
$DICT_GEN -o ../final -m $model_file

./change_word_cost.sh
#./change_connection_cost.sh

pushd ../final
./configure; make
popd
date
