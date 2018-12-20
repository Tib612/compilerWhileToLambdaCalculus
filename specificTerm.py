import sys
from myVisitors.codePrinter import codePrinter
cp = codePrinter()
cp.setHumanReadable(False)

def main(argv):
    print(cp.succ())

if __name__ == '__main__':
    main(sys.argv)