# -*- coding: utf-8 -*-
__author__ = 'hiking'
__email__ = 'hikingko1@gmail.com'
import unittest
from Vectorizer import JapaneseVectorizer

class JapaneseVectorizerTestCase(unittest.TestCase):
    def test_vectorize(self):
        """名詞を抽出することの確認
        """
        tokens = JapaneseVectorizer.vectorize("イギリスの首都はロンドン")
        self.assertListEqual(tokens, [u"イギリス", u"首都", u"ロンドン"])
