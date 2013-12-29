__author__ = 'hiking'
__email__ = 'hikingko1@gmail.com'
import urllib2
from BeautifulSoup import BeautifulSoup

class ScoreEvaluator:
    @staticmethod
    def evaluate(queries):
        """
        :type inputstr: str
        """
        print queries

class WikipediaScoreEvaluator(ScoreEvaluator):
    @staticmethod
    def evaluate(queries):
        """
        :type queries: [str]
        """
        query = "+".join(queries)
        hoge = "http://ja.wikipedia.org/w/index.php?fulltext=Search&search=%s" % query
        page = urllib2.urlopen(hoge)
        soup = BeautifulSoup(page)

        try:
            countstr = soup.find('div', {"class": "results-info"}).findAll('b')[1].contents[0]
            return int("".join(countstr.split(",")))
        except AttributeError:
            return 0
