class FileHandler:
    def __init__(self, inputFilePath, outputFilePath) -> None:
        self.inputFilePath = inputFilePath
        self.outputFilePath = outputFilePath

    def readAndWrite(self) -> None:
        with open(self.inputFilePath, 'r') as input, open(self.outputFilePath, 'w') as output:
            # Check in i/o file paths are valid
            if not input: 
                print('Invalid input at ', self.inputFilePath)
                return False
            if not output: 
                print('Invalid output at ', self.outputFilePath)
                return False

            # Read data and split data in to lines
            lines = input.read().split(',')
            lineCount = len(lines)
            if (lineCount == 0): 
                print(__name__, ': Empty input data')
                return False
            print('Total number of lines in input file: %s' % str(lineCount))

            # Save data in generator
            dataGen = self.dataGenerator(lines)

            # Print data from generator
            outputLineCount = 0
            for datum in dataGen: 
                output.write('%s%s' % (datum, '\n'))
                outputLineCount += 1
            print('Total number of lines in output file: %s' % str(outputLineCount))
            return True

    def dataGenerator(self, lines):
        yield from ( ('%s %s' % (str(i), str(line.lower()))) for (i, line) in enumerate(lines) )


