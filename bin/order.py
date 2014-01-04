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
from lib import YearDetector
from lib import JapaneseVectorizer

def _argparser(rawarglist):
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('events', type=str, nargs="+", default=[])
        args = parser.parse_args(rawarglist)
    except:
        raise
    return args

def main(events):
    """
    出来事の配列eventsを受け取って起こった順番に並べ替える
    :type events: [str]
    """
    years = [YearDetector.detect(JapaneseVectorizer.vectorize(event)) for event in events]
    years = zip(years, range(len(years)))
    years.sort()
    print [year[0] for year in years]
    print "answer=", [year[1] for year in years]
    return [year[1] for year in years]

if __name__ == '__main__':
    args = _argparser(sys.argv[1:])
    main(args.events)
