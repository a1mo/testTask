import unittest
from Finder import Finder


class FinderTests(unittest.TestCase):

    def testGetLinesByRegExp(self):
        finder = Finder("\[(.*?)\]")
        data = ["some text with [special] words\n", "in [square] brackets\n", "separated by lines"]
        processedData = finder.processData(data)
        self.assertEqual(data[:2], processedData)

    def testGetUniqueWords(self):
        finder = Finder()
        data = ["text, without.\n", "meaning! with? repetitive words\n", "in words without meaning?"]
        uniqueWords = ["text\n", "with\n", "repetitive\n", "in\n"]
        processedData = finder.processData(data)
        self.assertEqual(sorted(uniqueWords), sorted(processedData))
