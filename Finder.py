import re
from typing import List


class Finder:
    regexp = None

    def __init__(self, regexp: str = ""):
        self.regexp = regexp

    def getLinesListByRegExp(self, data: List[str]) -> List[str]:
        matchLinesList = []
        for line in data:
            if re.findall(self.regexp, line):
                matchLinesList.append(line)
        return matchLinesList

    def getUniqueWordsList(self, data: List[str]) -> List[str]:
        joinedData = ' '.join(data)
        clearedData = self.__cleanUpData(joinedData)
        splittedData = clearedData.split()
        wordCounter = {}
        for word in splittedData:
            if not wordCounter.get(word):
                wordCounter[word] = 0
            wordCounter[word] += 1

        uniqueWords = []
        for word, count in wordCounter.items():
            if count == 1:
                uniqueWords.append(word)

        return uniqueWords

    def processData(self, data: List[str]) -> List[str]:
        if self.regexp:
            return self.getLinesListByRegExp(data)
        return self.getUniqueWordsList(data)

    def __cleanUpData(self, data: str) -> str:
        symbolsToRemove = [
            ".", ",", ":", ";", "_", "-", "+", "=", "!", "?",
            "*", "/", "\\", "\"", "'", "~",
            "[", "]", "{", "}", "(", ")",
        ]
        for symbol in symbolsToRemove:
            data = data.replace(symbol, "")
        return data
