mecab-ko-dic
============
mecab-ko-dic은 오픈 소스 형태소 분석 엔진인 [MeCab](http://mecab.googlecode.com/svn/trunk/mecab/doc/index.html)을 사용하여, 한국어 형태소 분석을 하기위한 프로젝트입니다. 말뭉치 학습과 사전 목록은 모두 [21세기 세종계획](http://www.sejong.or.kr/)의 성과물을 사용하였습니다.

설치 방법
---------
TODO: MeCab 설치 설명
TODO: mecab-ko-dic 설치 설명

사용 방법
---------
TODO: mecab 실행파일을 이용하여 테스트하는 방법 설명

사전 설명
---------
각 사전(CSV 파일)에 대한 설명은 다음과 같습니다.
* E.csv - 선어말 어미, 어말 어미
* IC.csv - 감탄사
* Inflected.csv - 활용된 형태소
* J.csv - 조사
* MAG.csv - 부사
* MAJ.csv - 접속 부사
* MM.csv - 관형사
* NN-Compound.csv - 복합 명사
* NN-Proper.csv - 고유 명사
  현재는 세종 말뭉치에서 나온 고유 명사를 모아 놓았습니다. 합성 명사 구분이 되어있지 않고, 인명, 지명등이 구분없이 모여있습니다. 정리가 필요합니다.
* NN.csv - 명사
  세종 사전에서 명확하게 복합 명사가 구분되지 않아서, 다수의 복합 명사를 포함하고 있습니다.
* NNB-Classfier.csv - 분류사
* NNB.csv - 의존 명사
* NP.csv - 대명사
* NR.csv - 수사
* Symbol.csv - 형태소 분석에 사용하는 기호 모음
* VA.csv - 형용사
* VCN.csv - 부정 지정사
* VCP.csv - 긍정 지정사
* VV.csv - 동사
* VX.csv - 보조 용언
* XPN.csv - 체언 접두사
* XR.csv - 어근
* XSA.csv - 형용사 파생 접미사
* XSN.csv - 명사 파생 접미사
* XSV.csv - 동사 파생 접미사
