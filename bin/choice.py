#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'hiking'
__email__ = 'hikingko1@gmail.com'
import os
import sys
script_path = os.path.dirname(__file__)
script_path = script_path if len(script_path) else "."
sys.path.append(script_path+"/../src/lib")

def argmax(sequence):
    return sequence.index(max(sequence))

def main(description, options):
    """
    入力された４択から尤も回答である確率が高いものを出力する
    :param description: 問題文
    :type description: str
    :param options: 選択肢
    :type options: [str]
    """
    description_token = Vectorizer.vectorize(description)
    scores = [ScoreEvaluator.evaluate(vectorizer_token + Vectorizer.vectorize(option)) for option in options]
    print scores
    print argmax(scores)


if __name__ == '__main__':
