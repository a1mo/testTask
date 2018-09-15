import argparse
import helpers
import sys


def cleanUpData(data):
    """
    Receives a string and returns it cleared from invalid characters.

    :param data: string to clear
    :return: cleared string
    """
    symbolsToRemove = ["\n", ".", ",", ":", ";", "-", "!", "?"]
    for symbol in symbolsToRemove:
        replaceTo = ""
        if symbol == "\n":
            replaceTo = " "
        data = data.replace(symbol, replaceTo)
    return data


def getUniqueWords(data):
    """
    Receives a string and returns a list of unique words.

    :param data: string
    :return: list of unique words
    """
    clearedData = cleanUpData(data)
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


def main():
    """
    Find unique words in text file and put them in a new file.

    :param: --file: path to file
    """

    logger = helpers.getLogger("findUniqueWords")
    argp = argparse.ArgumentParser()
    argp.add_argument("-f", "--file")
    arguments = argp.parse_args()

    logger.info("script started")

    if not arguments.file:
        message = "--file parameter is not passed"
        logger.error(message)
        sys.exit(message)

    logger.info("got arguments: --file: \"{}\"".format(arguments.file))

    try:
        data = helpers.readDataFromFile(arguments.file)
    except (FileNotFoundError, IOError) as e:
        logger.error(e)
        sys.exit(e)

    uniqueWords = getUniqueWords(data)
    if not uniqueWords:
        message = "not have unique words"
        logger.info(message)
        sys.exit(message)

    outputFileName = helpers.getNewFileNameForOutput()
    helpers.writeDataToOutputFile("\n".join(uniqueWords), outputFileName)

    message = "success: file saved to \"{}\"".format(outputFileName)
    logger.info(message)
    sys.exit(message)


if __name__ == "__main__":
    main()
