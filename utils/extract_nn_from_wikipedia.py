#!/usr/bin/python3
# -*-coding:utf-8-*-
'''
한국 위키피디아에서 명사로 생각되는 단어를 뽑아서 출력하는 스크립트.
정확한 명사만 뽑아내지는 못하지만, 부족한 명사를 보충하기 위한 작업이다.
다음과 같이 사용한다. 

cat kowiki-latest-pages-articles.xml | ./extract_nn_from_wikipedia.py > wiki.txt
@author: bibreen <bibreen@gmail.com>
'''

import sys
import os
from io import StringIO
import sys
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from write_dic import isHangul


surfaceHashTable = dict()

#
#from blueplate.parsing.tsv import create_default_writer

__docformat__ = "restructuredtext"


class WPXMLHandler(ContentHandler):
    """Parse the enwiki-latest-pages-meta-history.xml file.

    This parser looks for just the things we're interested in.  It maintains a
    tag stack because the XML format actually does have some depth and context
    does actually matter.

    """

    def __init__(self, page_handler):
        """Do some setup.

        page_handler
            This is a callback.  It will be a called with a page in the form
            of a dict such as::

                {'id': u'8',
                 'revisions': [{'timestamp': u'2001-01-20T15:01:12Z',
                                'user': u'ip:pD950754B.dip.t-dialin.net'},
                               {'timestamp': u'2002-02-25T15:43:11Z',
                                'user': u'ip:Conversion script'},
                               {'timestamp': u'2006-09-08T04:16:46Z',
                                'user': u'username:Rory096'},
                               {'timestamp': u'2007-05-24T14:41:48Z',
                                'user': u'username:Ngaiklin'},
                               {'timestamp': u'2007-05-25T17:12:09Z',
                                'user': u'username:Gurch'}],
                 'title': u'AppliedEthics'}

        """
        self._tag_stack = []
        self._page_handler = page_handler

    def _try_calling(self, method_name, *args):
        """Try calling the method with the given method_name.

        If it doesn't exist, just return.

        Note, I don't want to accept **kargs because:

         a) I don't need them yet.
         b) They're really expensive, and this function is going to get called
            a lot.

        Let's not think of it as permature optimization, let's think of it as
        avoiding premature flexibility ;)

        """
        try:
            f = getattr(self, method_name)
        except AttributeError:
            pass
        else:
            return f(*args)

    def startElement(self, name, attr):
        """Dispatch to methods like _start_tagname."""
        self._tag_stack.append(name)
        self._try_calling('_start_' + name, attr)
        self._setup_characters()

    def _start_page(self, attr):
        self._page = dict(revisions=[])

    def _start_revision(self, attr):
        self._page['revisions'].append({})

    def _start_redirect(self, attr):
        self._page['redirect'] = attr['title']

    def endElement(self, name):
        """Dispatch to methods like _end_tagname."""
        self._teardown_characters()
        self._try_calling('_end_' + name)
        self._tag_stack.pop()

    def _end_page(self):
        self._page_handler(self._page)

    def _setup_characters(self):
        """Setup the callbacks to receive character data.

 The Parser will call the "characters" method to report each chunk of
 character data.  SAX parsers may return all contiguous character data
 in a single chunk, or they may split it into several chunks.  Hence,
 this class has to take care of some buffering.

        """
        method_name = '_characters_' + '_'.join(self._tag_stack)
        if hasattr(self, method_name):
            self._characters_buf = StringIO()
        else:
            self._characters_buf = None

    def characters(self, s):
        """Buffer the given characters."""
        if self._characters_buf is not None:
            self._characters_buf.write(s)

    def _teardown_characters(self):
        """Now that we have the entire string, put it where it needs to go.

 Dispatch to methods like _characters_some_stack_of_tags.  Drop strings
 that are just whitespace.

        """
        if self._characters_buf is None:
            return
        s = self._characters_buf.getvalue()
        if s.strip() == '':
            return
        method_name = '_characters_' + '_'.join(self._tag_stack)
        self._try_calling(method_name, s)

    def _characters_mediawiki_page_title(self, s):
        self._page['title'] = s
   
    def _characters_mediawiki_page_id(self, s):
        self._page['id'] = s

    def _characters_mediawiki_page_revision_timestamp(self, s):
        self._page['revisions'][-1]['timestamp'] = s

    def _characters_mediawiki_page_revision_text(self, s):
        self._page['revisions'][-1]['text'] = s

    def _characters_mediawiki_page_revision_contributor_username(self, s):
        self._page['revisions'][-1]['user'] = 'username:' + s

    def _characters_mediawiki_page_revision_contributor_ip(self, s):
        self._page['revisions'][-1]['user'] = 'ip:' + s

def parsewpxml(file, page_handler):
    """Call WPXMLHandler.
    file
        This is the name of the file to parse.

    page_handler
        See WPXMLHandler.__init__.
    """
    parser = make_parser()
    wpxmlhandler = WPXMLHandler(page_handler)
    parser.setContentHandler(wpxmlhandler)
    parser.parse(file)

def printNounFromWikipediaTitle(title):
    if len(title) > 7:
        return

    pos = title.find(':')
    if pos > -1:
        return

    pos = title.find('(')
    if pos > -1:
        return

    keywords = title.split(' ')
    if len(keywords) > 2:
        return

    # 조사를 가지고 있다고 의심되는 문장이 타이틀인 경우 키워드를 추출하지
    # 않는다.
    hasJosa = False
    for k in keywords:
        if (len(keywords) > 1 and
            ((len(k) >= 2 and k[-1] == '의') or
            (len(k) >= 2 and k[-1] == '은') or
            (len(k) >= 2 and k[-1] == '는') or
            (len(k) >= 2 and k[-1] == '에') or
            (len(k) >= 2 and  k[-1] == '을') or
            (len(k) >= 2 and k[-1] == '를'))):
            hasJosa = True
            break
    if hasJosa:
        return

    # 특정 키워드로 끝나는 키워드는 제외한다.
    for k in keywords:
        if (len(k) >= 2 and
            (k[-2:] == '학교' or
            k[-2:] == '에서' or
            k[-2:] == '공사' or
            k[-2:] == '공원' or
            k[-2:] == '원회' or
            k[-2:] == '교회' or
            k[-2:] == '대학' or
            k[-2:] == '병원' or
            k[-1:] == '법' or
            k[-1:] == '죄')):
            continue

        if isHangul(k) and hasNoun(k) == False:
            print(k)

def createNounSurfaceHashTable():
    global surfaceHashTable
    seedDir = '../seed'
    for fileName in os.listdir(seedDir):
        if fileName[0:2] != 'NN' or fileName[-3:] != 'csv':
            continue
        srcFileName = seedDir + '/' + fileName
        with open(srcFileName, mode='r', encoding='utf-8') as dicFile:
            for line in dicFile:
                items = line.split(',')
                surface = items[0]
                surfaceHashTable[surface] = True

def hasNoun(s):
    global surfaceHashTable
    return s in surfaceHashTable

def main(argv=None,  # Defaults to sys.argv.
         input=sys.stdin, _open=open):

    """Run the application.

    The arguments are really there for dependency injection.
    """
    def page_handler(page):
        try:
            if 'redirect' in page:
                #print(page['title'] + '->' + page['redirect'])
                return
            """Write the right bits to the right files."""
            title = page['title']
            printNounFromWikipediaTitle(title)
        except Exception as e:
            print >> sys.stderr, "invoked error. id : %s, %s" % (page['id'], e)

    parsewpxml(input, page_handler)

if __name__ == '__main__':
    createNounSurfaceHashTable()
    main()
