from sys import argv

inputFile, outputFile = argv[1:]
with open(inputFile) as input,\
    open(outputFile, "w") as output:
    output.write(input.read())

    