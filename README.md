# mecab-ko-dic 소개

[mecab-ko-dic](https://bitbucket.org/bibreen/mecab-ko-dic)은 오픈 소스 형태소 분석 엔진인 [MeCab](http://mecab.googlecode.com/svn/trunk/mecab/doc/index.html)을 사용하여, 한국어 형태소 분석을 하기 위한 프로젝트입니다. 말뭉치 학습과 사전 목록은 모두 21세기 세종계획의 성과물을 사용하였습니다.

형태소 분석 학습에 사용된 말뭉치는 다음과 같습니다.

  - 일상대화_삼십대 - 5CT_0017
  - 강의_언어와사회 - 5CT_0048
  - 독백_여행이야기#2 - 6CT_0013
  - 주제대화_광고토론 - 8CT_0039
  - 조선일보 경제(90) - BTAA0002
  - 조선일보 사설 - BTAA0004
  - 조선일보 과학(93) - BTAA0013
  - 미학 오디세이 - BTHO0367
  - 슬픈 시인의 바다 - BTEO0085
  - 해남 가는 길 - BTEO0088

# 설치 및 사용

mecab-ko-dic을 설치하고 사용하기 위해서 다음과 같은 작업이 필요합니다. 모든 작업은 Linux 기준입니다. 양해바랍니다.

## MeCab 설치

http://code.google.com/p/mecab/downloads/detail?name=mecab-0.994.tar.gz&can=1&q= 에서 MeCab의 소스를 다운 받고 설치합니다. (현재 mecab-ko-dic을 0.994 버전에서 테스트 하였기 때문에, 해당 버전을 추천합니다.)
tar.gz를 압축 해제하시고 일반적인 자유 소프트웨어와 같은 순서로 설치할 수 있습니다.

    $ tar zxfv mecab-XXtar.gz
    $ cd mecab-XX
    $ ./configure 
    $ make
    $ make check
    $ su
    # make install

## mecab-ko-dic 설치

https://bitbucket.org/bibreen/mecab-ko-dic/downloads 에서 mecab-ko-dic의 최신 버전을 다운 받습니다.
tar.gz를 압축 해제하시고 일반적인 자유 소프트웨어와 같은 순서로 설치할 수 있습니다.
기본으로 /usr/local/lib/mecab/dic/mecab-ko-dic에 설치됩니다.

    $ tar zxfv mecab-ko-dic-XX.tar.gz
    $ cd mecab-ko-dic-XX
    $ ./configure 
    $ make
    $ su
    # make install

## 사용

다음과 같이 mecab을 실행하여 한국어 형태소 분석 결과를 보실 수 있습니다. 

    $ mecab -d /usr/local/lib/mecab/dic/mecab-ko-dic
    mecab-ko-dic은 MeCab을 사용하여, 한국어 형태소 분석을 하기 위한 프로젝트입니다.
    mecab   SL,*,*,*,*,*,*
    -   SY,*,*,*,*,*,*
    ko  SL,*,*,*,*,*,*
    -   SY,*,*,*,*,*,*
    dic SL,*,*,*,*,*,*
    은  J,T,은,*,*,*,*
    MeCab   SL,*,*,*,*,*,*
    을  J,T,을,*,*,*,*
    사용    NN,T,사용,*,*,*,*
    하  XSV,F,하,*,*,*,*
    여  E,F,여,*,*,*,*
    ,   SY,*,*,*,*,*,*
    한국어  NN,F,한국어,*,*,*,*
    형태    NN,F,형태,*,*,*,*
    소  VCP+E,F,소,Inflect,VCP,E,이/VCP+소/E
    분석    NN,T,분석,*,*,*,*
    을  J,T,을,*,*,*,*
    하  VV,F,하,*,*,*,*
    기  E,F,기,*,*,*,*
    위한    VV+E,T,위한,Inflect,VV,E,위하/VV+ㄴ/E
    프로젝트    NN,F,프로젝트,*,*,*,*
    입니다  VCP+E,F,입니다,Inflect,VCP,E,이/VCP+ㅂ니다/E
    .   SF,*,*,*,*,*,*
    EOS

mecab-ko-dic에서 사용하는 사전 형식이나 품사 태그에 대한 정보는 다음의 페이지에서 보실 수 있습니다.

  - [mecab-ko-dic 품사 태그 설명](https://docs.google.com/spreadsheet/ccc?key=0ApcJghR6UMXxdEdURGY2YzIwb3dSZ290RFpSaUkzZ0E&usp=sharing)
