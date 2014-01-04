# -*- coding: utf-8 -*-
__author__ = 'hiking'
__email__ = 'hikingko1@gmail.com'
import urllib2
import re
import numpy
from BeautifulSoup import BeautifulSoup, NavigableString, Comment, Declaration

class YearDetector(object):
    LIMIT_RANK = 1 #上位何検索まで見るか

    @classmethod
    def getNavigableStrings(cls, soup):
        if isinstance(soup, NavigableString):
            if type(soup) not in (Comment,
                Declaration) and soup.strip():
                yield soup
        elif soup.name not in ('script', 'style'):
            for c in soup.contents:
                for g in cls.getNavigableStrings(c):
                    yield g

    @classmethod
    def _extract_years(cls, url):
        url = "http://ja.wikipedia.org" + url
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page).find("div", id="content")
        #print soup.prettify()
        text = "\n".join(cls.getNavigableStrings(soup))
        #print soup.prettify()
        years = re.findall(u'([0-9]+)年', text)
        years = [int(year) for year in years]
        return years

    @classmethod
    def detect(cls, queries):
        for query in queries:
            print query
            #print query.decode()
        query = "+".join(queries)
        url = "http://ja.wikipedia.org/w/index.php?fulltext=Search&search=%s" % query
        print url
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page)
        try:
            soup = soup.find('ul', {"class": "mw-search-results"})
            soup = soup.findAll('li')
            years = []
            for i in xrange(cls.LIMIT_RANK):
                link = soup[i].find("a")["href"]
                years += cls._extract_years(link)
            print years
            print numpy.median(years)
            return numpy.median(years)
        except AttributeError:
            raise ValueError
