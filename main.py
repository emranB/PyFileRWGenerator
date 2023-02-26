"""
This script should read text from a text file. It should split the text on comma
and output each resulting string in lowercase with the corresponding line number
prefixed. The script should also print the total number of lines at the end.

Identify and correct any problems with the code and modify it to be more
robust and maintainable.

Example usage:

$ python line_numbers.py input.txt output.txt
Total number of lines in output file: 7

Example input file:
Beautiful is better than ugly,Explicit is better than implicit,Simple is better than complex,Complex is better than complicated, Flat is better than nested, Sparse is better than dense, Readability counts

Example output file:
1 beautiful is better than ugly
2 explicit is better than implicit
3 simple is better than complex
4 complex is better than complicated
5 flat is better than nested
6 sparse is better than dense
7 readability counts

Note:
1. This is NOT a trick question.
2. Expectation is to write bug-free, clean, robust, maintainable and testable code.
3. The script should work for small and large files.
"""

import sys
from modules.FileHandler import *

def main(argc, argv):
    match argc:
        case 2: # missing input and output file paths
            print('Input file path detected: ', argv[1])
            print('Missing output file path param')
        case 3: # input and output file paths OK
            try:
                fh = FileHandler(argv[1], argv[2])
                fh.readAndWrite()
            except Exception as e:
                print('Error handding files', e)
        case _:
            print('Usage: main.py arg_1 arg_2 -> main.py <input_file_path> <output_file_path')

main(len(sys.argv), sys.argv)