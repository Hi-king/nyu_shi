# -*- coding: utf-8 -*-
__author__ = 'hiking'
__email__ = 'hikingko1@gmail.com'
import unittest
from ScoreEvaluator import WikipediaScoreEvaluator


class WikipediaScoreEvaluatorTestCase(unittest.TestCase):
    def test_validatedInput(self):
        """Match input"""
        input_token = ["イギリス", "ロンドン"]
        count = WikipediaScoreEvaluator.evaluate(input_token)
        self.assertGreater(count, 0)

    def test_unvalidatedInput(self):
        """Unmatch input"""
        input_token = ["ほげ", "huga"]
        count = WikipediaScoreEvaluator.evaluate(input_token)
        self.assertEqual(count, 0)
