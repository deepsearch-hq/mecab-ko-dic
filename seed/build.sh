#/bin/bash

date
MECAB_EXEC_PATH=/usr/local/libexec/mecab
DICT_INDEX=$MECAB_EXEC_PATH/mecab-dict-index
DICT_GEN=$MECAB_EXEC_PATH/mecab-dict-gen
COST_TRAIN=$MECAB_EXEC_PATH/mecab-cost-train

rm -f *.dic *.bin model model.txt
$DICT_INDEX -p -d . -c UTF-8 -t UTF-8 -f UTF-8

first="yes"
model_file="model"
for file in `ls corpus/*.txt`; do
	echo $file
	if [ "$first" == "yes" ]; then
		$COST_TRAIN -c 1.0 $file ${model_file}.tmp
		first="no"
	else
		$COST_TRAIN -c 1.0 -M ${model_file} $file ${model_file}.tmp
	fi

	rm -f ${model_file}
	mv ${model_file}.tmp ${model_file}
done

rm -f ../final/* 
$DICT_GEN -o ../final -m $model_file

pushd ../final
$DICT_INDEX -d . -c UTF-8 -t UTF-8 -f UTF-8
popd
date
