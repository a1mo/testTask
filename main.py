import argparse
from actionModule import ActionModule


def main():
    argp = argparse.ArgumentParser()
    argp.add_argument("file")
    argp.add_argument("-r", "--regexp")
    arguments = argp.parse_args()

    actionModule = ActionModule(arguments)

    with open(actionModule.file, encoding="utf8") as fileData:
        data = fileData.readlines()

    processedData = actionModule.processData(data)

    with open("output.txt", mode="w", encoding="utf8") as outputFile:
        outputFile.writelines(processedData)


if __name__ == "__main__":
    main()
