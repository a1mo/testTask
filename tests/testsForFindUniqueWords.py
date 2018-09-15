import unittest
from findUniqueWords import cleanUpData, getUniqueWords


class Tests(unittest.TestCase):

    def testCleanUpData(self):
        clearText = "just text with some characters that need to be removed"
        dirtyText = "just text with some: characters, that. need to? be\nremoved!!"
        clearedText = cleanUpData(dirtyText)
        self.assertEqual(clearText, clearedText)

    def testGetUniqueWords(self):
        text = "text without meaning with repetitive words in words without meaning"
        uniqueWords = ["text", "with", "repetitive", "in"]
        result = getUniqueWords(text)
        self.assertEqual(sorted(uniqueWords), sorted(result))
