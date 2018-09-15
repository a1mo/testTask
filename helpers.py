import os
from datetime import datetime
import logging


def getLogger(logFileName):
    """
    Receive log file name and return configured logger object

    :param logFileName: string with log name
    :return: logger object
    """

    if not os.path.exists("logs"):
        os.mkdir("logs")

    logger = logging.getLogger(logFileName)
    logger.setLevel(logging.INFO)

    fileHandler = logging.FileHandler("logs/{}.log".format(logFileName))

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - line %(lineno)d: %(message)s')
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)
    return logger


def readDataFromFile(filePath):
    """
    Read data from received file path.

    :param filePath: file path
    :return:
    """

    with open(filePath, mode="r") as file:
        return file.read()


def getNewFileNameForOutput():
    """
    Create name of output file.

    :return: name for output file
    """

    return "output_{}.txt".format(datetime.timestamp(datetime.utcnow()))


def writeDataToOutputFile(data, fileName):
    """
    Write data to file in output directory.

    :param data: string to write
    :param fileName: name of file to write
    """

    outputDir = "output"
    if not os.path.exists(outputDir):
        os.mkdir(outputDir)

    with open(os.path.join(outputDir, fileName), mode="w") as file:
        file.write(data)
