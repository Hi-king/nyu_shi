__author__ = 'hiking'
__email__ = 'hikingko1@gmail.com'

class DocumentDB:
    def __init__(self):
        self.tokens = set()

    def append(self, tokens):
        """
        :type tokens: [str]
        """
        self.tokens.add(tokens)

    def load(self):

    def get_score(self, tokens):
        """
        :type tokens: [str]
        """

