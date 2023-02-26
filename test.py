import unittest, sys
from modules.FileHandler import FileHandler

class Tests(unittest.TestCase):
    def testNoArgs(self):
        fh = FileHandler('bad_path', 'bad_path')
        self.assertEqual(fh.readAndWrite(), False)
        
    def filePathsOk(self):
        fh = FileHandler('./config/inputFile.txt', './config/outputFile.txt')
        self.assertEqual(fh.readAndWrite(), True)

if __name__=='__main__':
    suite = unittest.TestSuite()
    suite.addTest(Tests('testNoArgs'))
    suite.addTest(Tests('filePathsOk'))
    unittest.TextTestRunner().run(suite)
