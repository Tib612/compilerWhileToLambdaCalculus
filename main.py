import sys
from antlr4 import *
from gen.whileLangLexer import whileLangLexer
from gen.whileLangParser import whileLangParser
from myVisitors.myWhileLangVisitor import myWhileLangVisitor
from myVisitors.semantiqueVisitor import semantiqueVisitor

def main(argv):
    input = FileStream("input8.txt")
    lexer = whileLangLexer(input)
    stream = CommonTokenStream(lexer)
    parser = whileLangParser(stream)
    tree = parser.prog()
    mySemantiqueVisitor = semantiqueVisitor()
    mySemantiqueVisitor.visit(tree)
    nbVar = len(mySemantiqueVisitor.getVarList())
    print("nbVar = {}".format(nbVar))
    visitor = myWhileLangVisitor(nbVar)
    return visitor.visit(tree)

if __name__ == '__main__':
    main(sys.argv)