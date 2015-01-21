__author__ = 'budditao'

import pprint
from datetime import datetime
from sqlalchemy import or_

from dictionary.lexicon import Lexicon
from tools.editors.editor import Editor


class CompoundEditor(Editor):

    # @override
    def get_lexicons(self):
        # TODO: write select query
        return self.get_session().query(Lexicon). \
            filter(or_(Lexicon.type_name == 'Compound',
                       Lexicon.type_name == 'Preanalysis')). \
            filter(Lexicon.pos == 'NNG').all()
            #filter(Lexicon.surface=='수륙양용기').all()

    # @override
    def modify(self, lexicon):
        new_lexicons = []
        # TODO: rebuild lexicon object
        expression = []
        lexicon.start_pos = 'NNG'
        lexicon.end_pos = 'NNG'
        lexicon.index_expression = self.make_new_index_expression(lexicon.index_expression)
        lexicon.last_modified = datetime.now()
        #lexicon.is_available = '0'
        return new_lexicons

    def make_new_index_expression(self, old_expression):
        result = []
        for token in old_expression.split('+'):
            token_part = token.split('/')
            if token_part[3] == '1':
                result.append(token_part[0])
                result.append(token_part[1])
                result.append(token_part[2])
        print(result)
        return '/'.join(result)


