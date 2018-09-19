import logging
import os
import sys
from datetime import datetime
from libs.Finder import Finder
from libs.ArgumentParser import ThrowingArgumentParser, ArgumentParserError


OUTPUT_FOLDER = "output"


def createLogger(loggerName: str):
    if not os.path.exists("logs"):
        os.mkdir("logs")

    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.INFO)

    fileHandler = logging.FileHandler("logs/report.log")

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - line %(lineno)d: %(message)s')
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)
    return logger


def getOutputFilePath() -> str:
    if not os.path.exists(OUTPUT_FOLDER):
        os.mkdir(OUTPUT_FOLDER)

    outputFileName = "output_{}.txt".format(datetime.timestamp(datetime.utcnow()))
    return os.path.join(OUTPUT_FOLDER, outputFileName)


def main():
    logger = createLogger(__name__)
    logger.info('script started')

    argp = ThrowingArgumentParser()
    argp.add_argument("file", type = str)
    argp.add_argument("-r", "--regexp", type = str)
    try:
        arguments = argp.parse_args()
    except ArgumentParserError as e:
        logger.error(e)
        sys.exit(e)

    finder = Finder(arguments.regexp)

    if not os.path.isfile(arguments.file):
        message = "\"{}\" is not a file".format(arguments.file)
        logger.error(message)
        sys.exit(message)

    try:
        with open(arguments.file, encoding="utf8") as fileData:
            data = fileData.read().split("\n")
    except IOError as e:
        logger.error(e)
        sys.exit(e)

    processedData = finder.processData(data)
    logger.info("data processed")
    processedDataWithNewLines = [it + "\n" for it in processedData]

    outputFilePath = getOutputFilePath()
    with open(outputFilePath, mode="w", encoding="utf8") as outputFile:
        outputFile.writelines(processedDataWithNewLines)
    message = "success: saved to {}".format(outputFilePath)
    logger.info(message)
    print(message)


if __name__ == "__main__":
    main()
