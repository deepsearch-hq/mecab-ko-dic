# mecab-ko-dic

mecab-ko-dic은 오픈 소스 형태소 분석 엔진인 [MeCab](http://mecab.googlecode.com/svn/trunk/mecab/doc/index.html)을 사용하여, 한국어 형태소 분석을 하기위한 프로젝트입니다. 말뭉치 학습과 사전 목록은 모두 [21세기 세종계획](http://www.sejong.or.kr/)의 성과물을 사용하였습니다.

## 사전 설명

각 사전(CSV 파일)에 대한 설명은 다음과 같습니다.

  * CoinedWord.csv - 신조어, 준말, 비속어
  * EC.csv - 연결 어미
  * EF.csv - 종결 어미
  * EP.csv - 선어말 어미
  * ETM.csv - 관형형 전성 어미
  * ETN.csv - 명사형 전성 어미
  * IC.csv - 감탄사
  * Inflect.csv - 활용된 형태소
  * J.csv - 조사
  * MAG.csv - 부사
  * MAJ.csv - 접속 부사
  * MM.csv - 관형사
  * NN-Compound.csv - 복합 명사
  * NN-Foreign.csv - 외래어

    복합명사가 구분되어 있지 않습니다.

  * NN-Name.csv - 인물 이름을 제외한 회사, 상품 등의 이름
  * NN-Person-Preanalysis.csv - 인물 이름 기분석 사전
  * NN-Person.csv - 인물 이름
  * NN-Place - 지역 이름 (ex: 행정 지역명, 산 이름 등)
  * NN.csv - 명사

    세종 사전에서 명확하게 복합 명사가 구분되지 않아서, 다수의 복합 명사를 포함하고 있습니다.

  * NNB-Classfier.csv - 분류사
  * NNB.csv - 의존 명사
  * NP.csv - 대명사
  * NR.csv - 수사
  * Preanalysis.csv - 기분석 사전
  * SH-NN.csv - 한자 명사
  * SH-XPN.csv - 한자 접두사
  * SH-XR.csv - 한자 어근
  * SH-XSN.csv - 한자 접미사
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
  * \_Wikipedia.csv - 한국어 위키백과에서 추출한 명사
  * \_Wikipedia-Compound.csv - 한국어 위키백과에서 추출한 복합명사

    _Wikipedia*.csv는 다소 거칠게 추출한 사전이라 잘못된 명사가 있을 수 있지만, 인명이나 여러 고유 명사의 보충을 위해 사용되었습니다.
