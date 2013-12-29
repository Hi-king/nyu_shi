__author__ = 'hiking'
__email__ = 'hikingko1@gmail.com'
import unittest
import DocumentDB

class DocumentDBTestCase(unittest.TestCase):
    def setUp(self):
        self.db = DocumentDB()
        self.db.append(["a", "b"])

    def test_append(self):
        self.db.append(["a", "c"])

    def test_scoreing(self):


