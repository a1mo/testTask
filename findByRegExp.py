import argparse
import re
import sys
import helpers


def getMatchesForRegExpInData(regExp, data):
    """

    :param regExp: compiled regular expression pattern
    :param data: data to process
    :return: list of stings
    """

    return re.findall(regExp, data)


def main():
    """
    Find lines in text file and put them in a new file.

    :param --regexp: regular expression pattern
    :param --file: path to file
    """

    logger = helpers.getLogger("findByRegExp")

    argp = argparse.ArgumentParser()
    argp.add_argument("-r", "--regexp")
    argp.add_argument("-f", "--file")
    arguments = argp.parse_args()

    logger.info("script stared")

    if not arguments.regexp or not arguments.file:
        message = "required arguments are not passed"
        logger.error(message)
        sys.exit(message)

    logger.info("got arguments: --regexp: \"{}\"; --file: \"{}\"".format(arguments.regexp, arguments.file))

    try:
        compiledRegExp = re.compile(arguments.regexp)
    except (TypeError, re.error) as e:
        logger.error(e)
        sys.exit(e)

    try:
        data = helpers.readDataFromFile(arguments.file)
    except (FileNotFoundError, IOError) as e:
        logger.error(e)
        sys.exit(e)

    if not data:
        message = "file {} is empty".format(arguments.file)
        logger.error(message)
        sys.exit(message)

    results = getMatchesForRegExpInData(compiledRegExp, data)

    if not results:
        message = "not have results for \"{}\" expression. nothing to save".format(arguments.regexp)
        logger.info(message)
        sys.exit(message)

    outputFileName = helpers.getNewFileNameForOutput()
    helpers.writeDataToOutputFile("\n".join(results), outputFileName)

    message = "success: file saved to \"{}\"".format(outputFileName)
    logger.info(message)
    sys.exit(message)


if __name__ == "__main__":
    main()
