import unittest
from Sentiment import calSentimentLevel
class Testlab03(unittest.TestCase):

    def testcalSentimentLevel(self):
        v1 = 10
        num = calSentimentLevel(v1)
        self.assertEqual(2,num)



if __name__ == '__main__':
    unittest.main()