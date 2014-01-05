# -*- coding: utf-8 -*-
__author__ = 'hiking'
__email__ = 'hikingko1@gmail.com'
import sys
import os
script_path = os.path.dirname(__file__)
sys.path.append(script_path+"/../..")
from lib import JapaneseVectorizer
from lib import WikipediaScoreEvaluator
from lib import BingScoreEvaluator


class TrueFalseSolver(object):
    EVALUATOR = BingScoreEvaluator
    @classmethod
    def solve(cls, description):
        tokens = JapaneseVectorizer.vectorize(description)
        basescore = cls.EVALUATOR._evaluate(tokens)
        basescore = float(basescore)
        score_rates = []
        for i in xrange(len(tokens)):
            thisscore = cls.EVALUATOR._evaluate(tokens[:i]+tokens[i+1:])
            print thisscore
            score_rates.append(basescore/thisscore)
        print score_rates
        return min(score_rates)
