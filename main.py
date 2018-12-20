import sys
from antlr4 import *
from gen.whileLangLexer import whileLangLexer
from gen.whileLangParser import whileLangParser
from myVisitors.myWhileLangVisitor import myWhileLangVisitor
from myVisitors.semantiqueVisitor import semantiqueVisitor

# var to change
test = True

def run(source,destination):

    input = FileStream(source)
    lexer = whileLangLexer(input)
    stream = CommonTokenStream(lexer)
    parser = whileLangParser(stream)
    tree = parser.prog()
    mySemantiqueVisitor = semantiqueVisitor()
    mySemantiqueVisitor.visit(tree)
    nbVar = len(mySemantiqueVisitor.getVarList())
    visitor = myWhileLangVisitor(nbVar,destination)
    visitor.visit(tree)

def main(argv):

    if test:
        nbTests = 9
        for i in range(nbTests):
            run("tests/input"+str(i+1)+".txt", "tests/output"+str(i+1)+".txt")
    else:
        run("tests/input1.txt", "tests/output1.txt")

if __name__ == '__main__':
    main(sys.argv)