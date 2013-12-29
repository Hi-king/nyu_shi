__author__ = 'hiking'
__email__ = 'hikingko1@gmail.com'


import urllib2
from BeautifulSoup import BeautifulSoup

page = urllib2.urlopen("http://www.icc-ccs.org/prc/piracyreport.php")
soup = BeautifulSoup(page)

class GoogleSearch:
