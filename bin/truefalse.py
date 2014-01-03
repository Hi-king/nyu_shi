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
from lib.solver import TrueFalseSolver

def _argparser(rawarglist):
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('description', type=str)
        args = parser.parse_args(rawarglist)
    except:
        raise
    return args

def argmax(sequence):
    return sequence.index(max(sequence))

def main(description):
    """
    正誤と最低ゲインを出力する
    :param description: 問題文
    :type description: str
    """
    score = TrueFalseSolver.solve(description)
    print score

if __name__ == '__main__':
    args = _argparser(sys.argv[1:])
    main(args.description)
