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
from lib import WikipediaScoreEvaluator

def _argparser(rawarglist):
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('description', type=str)
        parser.add_argument('options', type=str, nargs="+", default=[])
        args = parser.parse_args(rawarglist)
    except:
        raise
    return args

def argmax(sequence):
    return sequence.index(max(sequence))

def main(description, options):
    """
    入力された４択から最も回答である確率が高いものを出力する
    :param description: 問題文
    :type description: str
    :param options: 選択肢
    :type options: [str]
    """
    description_token = JapaneseVectorizer.vectorize(description)
    print description_token

    scores = [WikipediaScoreEvaluator._evaluate(description_token + JapaneseVectorizer.vectorize(option)) for option in options]
    print scores
    ansindex = argmax(scores)
    return options[ansindex]

if __name__ == '__main__':
    args = _argparser(sys.argv[1:])
    main(args.description, args.options)
