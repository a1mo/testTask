import unittest
from libs.Finder import Finder


class FinderTest(unittest.TestCase):

    def testFinderReturnsMatchedLinesOnRegExpPassed(self):
        finder = Finder("\[(.*?)\]")
        expectedResult = ["some text with [special] words", "in [square] brackets"]
        processedData = finder.processData(expectedResult + ["separated by lines"])
        self.assertEqual(expectedResult, processedData)

    def testFinderReturnsUniqueWordsWithoutRegExpPassed(self):
        finder = Finder()
        data = ["text, without.", "meaning! with? repetitive words", "in words without meaning?"]
        uniqueWords = ["text", "with", "repetitive", "in"]
        processedData = finder.processData(data)
        self.assertEqual(sorted(uniqueWords), sorted(processedData))
