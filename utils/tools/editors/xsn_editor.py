__author__ = 'budditao'

import pprint
from datetime import datetime

from dictionary.lexicon import Lexicon
from tools.editors.editor import Editor


class XsnEditor(Editor):

    def get_query(self):
        # TODO: write select query
        return self.get_session().query(Lexicon). \
            filter(Lexicon.type_name == 'Compound'). \
            filter(Lexicon.pos == 'NNG'). \
            filter(Lexicon.is_available == '1')
            #filter(Lexicon.surface=='수륙양용기')


    def modify(self, lexicon):
        new_lexicons = []
        if lexicon.compound_expression.split('+')[-1] in XSN:

            # TODO: rebuild lexicon object
            lexicon.type_name = 'Preanalysis'
            mophemes = lexicon.compound_expression.split('+')
            expression = []
            surface = ''
            for index, mopheme in enumerate(mophemes):
                surface += mopheme
                length = index + 1
                if index == 0:
                    expression.append('%s/NNG/1/%s' % (surface, length))
                    # 처음(single) 단어 추가
                    new_lexicons.append(Lexicon(surface=surface,
                                                pos='NNG',
                                                read=surface))
                else:
                    expression.append('%s/NNG/0/%s' % (surface, length))
                    # 중간 단어들(compound) 추가
                    if len(mophemes) != index+1:
                        new_lexicons.append(build_prenaisis_lexicon(mophemes[0:index+1]))

            lexicon.start_pos = 'NNG'
            lexicon.end_pos = 'NNG'
            lexicon.index_expression = '+'.join(expression)
            lexicon.last_modified = datetime.now()
            #lexicon.is_available = '0'

        return new_lexicons


def build_prenaisis_lexicon(word_list):
    index_expression = []
    surface = ''
    for index, mopheme in enumerate(word_list):
        surface += mopheme
        length = index + 1
        if index == 0:
            index_expression.append('%s/NNG/1/%s' % (surface, length))
        else:
            index_expression.append('%s/NNG/0/%s' % (surface, length))


    return Lexicon(surface=''.join(word_list),
                   pos='NNG',
                   read=''.join(word_list),
                   start_pos='NNG',
                   end_pos='NNG',
                   compound_expression='+'.join(word_list),
                   index_expression = '+'.join(index_expression))



XSN = {
    'ㅁ',
    '丈',
    '上',
    '下',
    '串',
    '主',
    '事',
    '亭',
    '人',
    '代',
    '令',
    '作',
    '係',
    '値',
    '假量',
    '傳',
    '價',
    '兒',
    '公',
    '具',
    '分',
    '分之',
    '判',
    '別',
    '制',
    '券',
    '劑',
    '力',
    '化',
    '口',
    '史',
    '品',
    '員',
    '哥',
    '商',
    '器',
    '囊',
    '囚',
    '圈',
    '國',
    '園',
    '圖',
    '團',
    '地',
    '型',
    '場',
    '士',
    '委',
    '媽',
    '孃',
    '子',
    '孫',
    '學',
    '宅',
    '官',
    '客',
    '室',
    '家',
    '寺',
    '局',
    '屆',
    '屋',
    '展',
    '層',
    '岸',
    '島',
    '嶺',
    '巖',
    '川',
    '工',
    '帖',
    '師',
    '席',
    '帳',
    '帶',
    '帽',
    '年',
    '店',
    '度',
    '座',
    '庵',
    '廠',
    '廳',
    '式',
    '張',
    '形',
    '律',
    '徒',
    '心',
    '性',
    '愛',
    '感',
    '慾',
    '成',
    '戰',
    '所',
    '手',
    '整',
    '文',
    '料',
    '族',
    '日',
    '旬',
    '曆',
    '曲',
    '會',
    '服',
    '朝',
    '期',
    '本',
    '材',
    '村',
    '林',
    '業',
    '樓',
    '機',
    '權',
    '次',
    '欲',
    '歌',
    '殿',
    '氏',
    '民',
    '氣',
    '池',
    '油',
    '法',
    '波',
    '洋',
    '洞',
    '派',
    '流',
    '海',
    '港',
    '湯',
    '漢',
    '然',
    '爐',
    '版',
    '物',
    '犯',
    '狀',
    '狂',
    '王',
    '生',
    '産',
    '用',
    '男',
    '界',
    '畢',
    '畫',
    '當',
    '症',
    '發',
    '白',
    '的',
    '社',
    '祖',
    '祭',
    '種',
    '策',
    '米',
    '系',
    '紙',
    '綠',
    '綴',
    '線',
    '群',
    '翁',
    '者',
    '腺',
    '臺',
    '船',
    '艇',
    '莊',
    '菴',
    '葬',
    '處',
    '號',
    '行',
    '術',
    '街',
    '補',
    '裡',
    '製',
    '視',
    '觀',
    '計',
    '記',
    '許',
    '詞',
    '誌',
    '語',
    '說',
    '課',
    '談',
    '論',
    '證',
    '責',
    '費',
    '路',
    '輩',
    '辭',
    '農',
    '通',
    '選',
    '部',
    '酒',
    '錄',
    '錠',
    '鏡',
    '鑛',
    '長',
    '間',
    '閣',
    '附',
    '院',
    '陣',
    '集',
    '難',
    '靴',
    '頃',
    '順',
    '領',
    '額',
    '類',
    '風',
    '餘',
    '館',
    '體',
    '高',
    '가',
    '가들의',
    '간',
    '감',
    '강',
    '개',
    '거리',
    '격',
    '경',
    '계',
    '관',
    '광',
    '군',
    '군',
    '권',
    '급',
    '기',
    '껏',
    '께',
    '꼴',
    '꾼',
    '끼',
    '끼리',
    '날',
    '네',
    '년',
    '년경',
    '논',
    '는',
    '니임',
    '님',
    '당',
    '대',
    '댁',
    '덜',
    '되',
    '드을',
    '득',
    '들',
    '들이',
    '떨',
    '란',
    '량',
    '력',
    '론',
    '류',
    '률',
    '리',
    '만여',
    '만큼',
    '면',
    '명',
    '무',
    '문화권',
    '민',
    '바기',
    '박이',
    '발',
    '방',
    '배기',
    '변',
    '별',
    '부',
    '분',
    '뻘',
    '산',
    '상',
    '생',
    '설',
    '성',
    '소',
    '순',
    '스',
    '승',
    '시',
    '식',
    '식',
    '심',
    '씨',
    '씩',
    '아',
    '아',
    '액',
    '어',
    '어치',
    '업',
    '여',
    '용',
    '유',
    '율',
    '이',
    '인',
    '자',
    '잡이',
    '장이',
    '재',
    '재',
    '재이',
    '쟁이',
    '쟁이',
    '저',
    '적',
    '전',
    '점',
    '제',
    '주의',
    '중',
    '즈',
    '즘',
    '지',
    '직',
    '질',
    '짓',
    '짜',
    '짜리',
    '째',
    '쫌',
    '쯤',
    '찌리',
    '차',
    '채',
    '측',
    '층',
    '치',
    '치레',
    '투성이',
    '틱',
    '파',
    '판',
    '편',
    '풍',
    '하',
    '학',
    '학년',
    '행',
    '형',
    '호',
    '화',
    '회',
    '金',
    '率',
    '女',
    '律',
    '率',
    '狀',
}