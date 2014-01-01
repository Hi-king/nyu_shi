__author__ = 'hiking'
__email__ = 'hikingko1@gmail.com'
import urllib2
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


