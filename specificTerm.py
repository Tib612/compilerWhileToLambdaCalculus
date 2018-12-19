import sys
from myVisitors.codePrinter import codePrinter
cp = codePrinter()
cp.setHumanReadable(False)

def main(argv):
    print(cp.init())

if __name__ == '__main__':
    main(sys.argv)