# -*- coding: utf-8 -*-
__author__ = 'hiking'
__email__ = 'hikingko1@gmail.com'
import os
import sys
import unittest
sys.path.append(os.path.dirname(__file__)+'/../..')
from lib import YearDetector
from lib import JapaneseVectorizer

class YearDetectorTestCase(unittest.TestCase):
    def test_100years_correct(self):
        """100年以内の誤差で出来事の年代を当てられる"""
        event = "ニケーアの公会議が行われる"
        year = YearDetector.detect(JapaneseVectorizer.vectorize(event))
        self.assertAlmostEqual(year, 325, delta=100)
