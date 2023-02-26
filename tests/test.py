import unittest
from modules.FileHandler import *

class Tests(unittest.TestCase):
    def testNoArgs(self):
        fh = FileHandler()
        assert(fh.readAndWrite(), False)

    def filePathsOk(self):
        fh = FileHandler('./config/inputFile.txt', './config/outputFile.txt')
        assert(fh.readAndWrite(), True)

unittest.main()
