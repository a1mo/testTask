import logging
import os
import sys
from datetime import datetime
from Finder import Finder
from ArgumentParser import ThrowingArgumentParser, ArgumentParserError


OUTPUT_FOLDER = "output"


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


def getOutputFilePath() -> str:
    if not os.path.exists(OUTPUT_FOLDER):
        os.mkdir(OUTPUT_FOLDER)

    outputFileName = "output_{}.txt".format(datetime.timestamp(datetime.utcnow()))
    return os.path.join(OUTPUT_FOLDER, outputFileName)


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

    outputFilePath = getOutputFilePath()
    with open(outputFilePath, mode="w", encoding="utf8") as outputFile:
        processedDataWithNewLines = [dataItem + "\n" for dataItem in processedData]
        outputFile.writelines(processedDataWithNewLines)
    message = "success: saved to {}".format(outputFilePath)
    logger.info(message)
    sys.exit(message)


if __name__ == "__main__":
    main()
