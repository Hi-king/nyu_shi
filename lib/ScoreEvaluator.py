# -*- coding: utf-8 -*-
__author__ = 'hiking'
__email__ = 'hikingko1@gmail.com'
import urllib2
import os
import yaml
import json
from BeautifulSoup import BeautifulSoup
from Vectorizer import JapaneseVectorizer

class ScoreEvaluator:
    @classmethod
    def evaluate(cls, sentence):
        """
        :type sentence: str
        """
        return cls._evaluate(JapaneseVectorizer.vectorize(sentence))

    @classmethod
    def _evaluate(cls, queries):
        """
        :type queries: [str]
        """
        return 0

class WikipediaScoreEvaluator(ScoreEvaluator):
    @classmethod
    def _evaluate(cls, queries):
        """
        :type queries: [str]
        """
        print "queries=", queries
        query = "+".join(queries)
        #url = "http://ja.wikipedia.org/w/index.php?fulltext=Search&search=%s" % query.encode('utf-8')
        url = "http://ja.wikipedia.org/w/index.php?fulltext=Search&search=%s" % query
        print url
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page)

        try:
            countstr = soup.find('div', {"class": "results-info"}).findAll('b')[1].contents[0]
            return int("".join(countstr.split(",")))
        except AttributeError:
            return 0

class BingScoreEvaluator(ScoreEvaluator):
    CONF_PATH = os.path.dirname(__file__)+"/../conf/conf.yaml"

    @classmethod
    def _basic_auth_open(cls, url):
        #url = 'https://api.datamarket.azure.com/Data.ashx/Bing/Search/v1/Composite\?Sources\=%27web%27\&Query\=%27hoge%27\&\$format\=json'
        #url = "https://api.datamarket.azure.com/Bing/Search/v1/Composite?Sources='web'&Query='イギリス'&$format=JSON"
        data = yaml.safe_load(open(cls.CONF_PATH).read())
        account = data["bing"]["account"]

        # create a password manager
        password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
        # Add the username and password.
        top_level_url = "https://api.datamarket.azure.com"
        password_mgr.add_password(None, top_level_url, account, account)
        handler = urllib2.HTTPBasicAuthHandler(password_mgr)
        opener = urllib2.build_opener(handler)
        return opener.open(url).read()
        #urllib2.install_opener(opener)


    @classmethod
    def _evaluate(cls, queries):
        """
        :type queries: [str]
        """
        print "queries=", queries
        query = "　".join(queries)
        url = "https://api.datamarket.azure.com/Bing/Search/v1/Composite?Sources='web'&Query='"+query+"'&$format=JSON"
        print url
        page = cls._basic_auth_open(url)
        data = json.loads(page)
        return int(data["d"]["results"][0]["WebTotal"])

