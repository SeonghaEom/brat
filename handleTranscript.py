

import sys
import getopt
import re


print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

# usage: test.py -i <inputfile> -o <outputfile>


def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print('Input file is ', inputfile)
    print('Output file is ', outputfile)

    with open(inputfile) as fp:
        script = fp.read()

    # print(script)
    tmp = script.split('\n')
    joined = ' '.join(tmp)

    print(joined)

    with open(outputfile, 'w') as f:
        f.write(joined)

if __name__ == "__main__":
    main(sys.argv[1:])
