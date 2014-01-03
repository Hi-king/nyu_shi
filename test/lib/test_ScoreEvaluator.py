# -*- coding: utf-8 -*-
__author__ = 'hiking'
__email__ = 'hikingko1@gmail.com'
import unittest
from ScoreEvaluator import WikipediaScoreEvaluator
from ScoreEvaluator import BingScoreEvaluator


class WikipediaScoreEvaluatorTestCase(unittest.TestCase):
    def test_validatedInput(self):
        """Match input"""
        input_token = ["イギリス", "ロンドン"]
        count = WikipediaScoreEvaluator._evaluate(input_token)
        self.assertGreater(count, 0)

    def test_unvalidatedInput(self):
        """Unmatch input"""
        input_token = ["ほげ", "huga"]
        count = WikipediaScoreEvaluator._evaluate(input_token)
        self.assertEqual(count, 0)

class BingScoreEvaluatorTestCase(unittest.TestCase):
    def test_validated_input(self):
        """共起する入力"""
        input_token = ["イギリス", "ロンドン"]
        count = BingScoreEvaluator._evaluate(input_token)
        self.assertGreater(count, 6000000)

    def test_unvalidated_input(self):
        """共起しない入力"""
        input_token = ["イギリス", "ベルリン"]
        count = BingScoreEvaluator._evaluate(input_token)
        self.assertLess(count, 6000000)
