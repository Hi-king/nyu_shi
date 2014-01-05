#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'hiking'
__email__ = 'hikingko1@gmail.com'
import os
import sys
import argparse
script_path = os.path.dirname(__file__)
script_path = script_path if len(script_path) else "."
sys.path.append(script_path+"/..")
from lib import JapaneseVectorizer
from lib.solver import TrueFalseSolver

def _argparser(rawarglist):
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('descriptions', type=str, nargs="+", default=[])
        args = parser.parse_args(rawarglist)
    except:
        raise
    return args

def argmax(sequence):
    return sequence.index(max(sequence))

def main(descriptions):
    """
    入力された文章の内,最も適当or不適当なものを出力する
    :type descriptions: [str]
    """
    print(descriptions[0])
    descriptions = [JapaneseVectorizer.refine_string(description) for description in descriptions]
    print(descriptions[0])
    scores = [TrueFalseSolver.solve(description) for description in descriptions]
    scores = zip(scores, range(len(scores)))
    scores.sort()
    print [score[0] for score in scores]
    print "answer:", [score[1] for score in scores]
    return [score[1] for score in scores]

if __name__ == '__main__':
    args = _argparser(sys.argv[1:])
    main(args.descriptions)
