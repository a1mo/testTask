import logging
import os
import sys
from datetime import datetime
from Finder import Finder
from ArgumentParser import ThrowingArgumentParser, ArgumentParserError


def getConfiguredLogger(logFileName: str):
    if not os.path.exists("logs"):
        os.mkdir("logs")

    logger = logging.getLogger(logFileName)
    logger.setLevel(logging.INFO)

    fileHandler = logging.FileHandler("logs/{}.log".format(logFileName))

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - line %(lineno)d: %(message)s')
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)
    return logger


def main():
    logger = getConfiguredLogger(__name__)
    logger.info('script started')

    argp = ThrowingArgumentParser()
    argp.add_argument("file")
    argp.add_argument("-r", "--regexp")
    try:
        arguments = argp.parse_args()
    except ArgumentParserError as e:
        logger.error(e)
        sys.exit(e)

    finder = Finder(arguments.regexp)

    try:
        with open(arguments.file, encoding="utf8") as fileData:
            data = fileData.read().split("\n")
    except (FileNotFoundError, IOError) as e:
        logger.error(e)
        sys.exit(e)

    processedData = finder.processData(data)
    logger.info("data processed")

    with open("output.txt", mode="w", encoding="utf8") as outputFile:
        processedDataWithNewLines = [dataItem + "\n" for dataItem in processedData]
        outputFile.writelines(processedDataWithNewLines)
    message = "success: saved to output file"
    logger.info(message)
    sys.exit(message)


if __name__ == "__main__":
    main()
