# -*- coding: utf-8 -*-
__author__ = 'hiking'
__email__ = 'hikingko1@gmail.com'
from BeautifulSoup import BeautifulSoup
import urllib2
import re

class Vectorizer(object):
    @staticmethod
    def refine_string(inputstr):
        """
        :type inputstr: str
        """
        return re.sub(u"\([^\(\)]*\)", "", inputstr, re.U)

    @staticmethod
    def vectorize(inputstr):
        """
        :type inputstr: str
        """
        return inputstr.split()

class JapaneseVectorizer(Vectorizer):
    @staticmethod
    def vectorize(inputstr):
        """
        :type inputstr: str
        :rtype: [str]
        """
        #inputstr = urllib2.quote(inputstr)
        url = "http://jlp.yahooapis.jp/MAService/V1/parse?appid=dj0zaiZpPTVwcmNDWHNvVm1waiZzPWNvbnN1bWVyc2VjcmV0Jng9YWY-&sentence=%s" % inputstr
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page)
        words = soup.find("word_list").findAll("word")

        print words
        nouns = []
        flag_quote = False
        #名詞だけを抽出
        for i in xrange(len(words)):
            #ダブルクォーテーションで囲まれているのは一つの名詞
            if flag_quote:
                if words[i].find("surface").contents[0] == u"&quot;":
                    flag_quote = False
                    continue
                else:
                    nouns[-1] += words[i].find("surface").contents[0].encode('utf-8')
                    continue
            elif words[i].find("surface").contents[0] == u"&quot;":
                nouns.append("")
                flag_quote = True
                continue


            #接尾辞は前にくっつける
            #"世紀"とか
            if nouns and words[i].find("pos").contents[0] == u"接尾辞":
                #接尾辞は前にくっつける
                #"世紀"とか
                nouns[-1] += words[i].find("surface").contents[0].encode('utf-8')
                continue
            elif words[i].find("pos").contents[0] != u"名詞":
                continue

            #複合名詞は一つにする
            if nouns and words[i-1].find("pos").contents[0] == u"名詞":
                nouns[-1] += words[i].find("surface").contents[0].encode('utf-8')
            else:
                nouns.append(words[i].find("surface").contents[0].encode('utf-8'))

        #nouns = [word for word in words if word.find("pos").contents[0] == u"名詞"]
        #print "nouns=", nouns
        return nouns
