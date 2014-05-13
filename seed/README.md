# mecab-ko-dic

mecab-ko-dic은 오픈 소스 형태소 분석 엔진인 [MeCab](http://mecab.googlecode.com/svn/trunk/mecab/doc/index.html)을 사용하여, 한국어 형태소 분석을 하기위한 프로젝트입니다. 말뭉치 학습과 사전 목록은 모두 [21세기 세종계획](http://www.sejong.or.kr/)의 성과물을 사용하였습니다.

## 사전 설명

각 사전(CSV 파일)에 대한 설명은 다음과 같습니다.

  - CoinedWord.csv - 신조어, 준말, 비속어
  - EC.csv - 연결 어미
  - EF.csv - 종결 어미
  - EP.csv - 선어말 어미
  - ETM.csv - 관형형 전성 어미
  - ETN.csv - 명사형 전성 어미
  - Foreign.csv - 외래어
  - Group.csv - 회사나 집단의 이름
  - Hanja.csv - 한자어
  - IC.csv - 감탄사
  - Inflect.csv - 활용된 형태소
  - J.csv - 조사
  - MAG.csv - 부사
  - MAJ.csv - 접속 부사
  - MM.csv - 관형사
  - NNB.csv - 의존 명사
  - NNBC.csv - 분류사
  - NNG.csv - 보통 명사
  - NNP.csv - 고유 명사
  - NP.csv - 대명사
  - NR.csv - 수사
  - NorthKorea.csv - 북한어
  - Person-actor.csv - 배우 인명
  - Person.csv - 인명
  - Place-address.csv - 주소
  - Place.csv - 지명
  - Preanalysis.csv - 기분석 사전
  - Symbol.csv - 기호
  - VA.csv - 형용사
  - VCN.csv - 부정 지정사
  - VCP.csv - 긍정 지정사
  - VV.csv - 동사
  - VX.csv - 보조 용언
  - XPN.csv - 체언 접두사
  - XR.csv - 어근
  - XSA.csv - 형용사 파생 접미사
  - XSN.csv - 명사 파생 접미사
  - XSV.csv - 동사 파생 접미사
  - Wikipedia.csv - 한국어 위키백과에서 추출한 명사

    Wikipedia*.csv는 다소 거칠게 추출한 사전이라 잘못된 명사가 있을 수 있지만, 인명이나 여러 고유 명사의 보충을 위해 사용되었습니다.
