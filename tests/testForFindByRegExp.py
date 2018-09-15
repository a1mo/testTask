import unittest
import re
import findByRegExp


class Tests(unittest.TestCase):

    def testRegExp(self):
        compiledRegExp = re.compile("\[(.*?)\]")
        data = "some text with [special] words in [square] brackets"
        result = findByRegExp.getMatchesForRegExpInData(compiledRegExp, data)
        self.assertEqual(["special", "square"], result)
