# -*- coding: utf-8 -*-
import unittest
import choice
class ChoiceTestCase(unittest.TestCase):
    def test_choice(self):
        ans = choice.main("イギリスの首都", ["ロンドン", "ベルリン"])
        self.assertEqual(ans, "ロンドン")
