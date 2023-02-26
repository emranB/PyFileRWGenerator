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