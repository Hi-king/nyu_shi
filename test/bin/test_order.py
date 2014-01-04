# -*- coding: utf-8 -*-
import unittest
import os
import sys
script_path = os.path.dirname(__file__)
script_path = script_path if len(script_path) else "."
sys.path.append(script_path+"/../../bin")
import order


class OrderTestCase(unittest.TestCase):
    def test_order(self):
        """簡単な年代並べ替え問題が解ける"""
        ans = order.main([
            "世界恐慌",
            "第一次世界大戦",
            "第二次世界大戦"
        ])
        self.assertListEqual(ans, [1, 0, 2])
