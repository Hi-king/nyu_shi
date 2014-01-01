# -*- coding: utf-8 -*-
__author__ = 'hiking'
__email__ = 'hikingko1@gmail.com'
from BeautifulSoup import BeautifulSoup
import urllib2

class Vectorizer(object):
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
        for word in words:
            print word.find("pos").contents[0] == u"名詞"
        nouns = [word for word in words if word.find("pos").contents[0] == u"名詞"]
        print "nouns=", nouns
        return [noun.find("surface").contents[0].encode('utf-8') for noun in nouns]
