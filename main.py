import sys
from antlr4 import *
from gen.whileLangLexer import whileLangLexer
from gen.whileLangParser import whileLangParser
from myVisitors.myWhileLangVisitor import myWhileLangVisitor
from myVisitors.semantiqueVisitor import semantiqueVisitor


# run the compiler with the "while" program from "source" file and write the equivalent "lambda calculus" program in
# the "destination" file.
# This function need to receive a correct "while" program. (good syntax)
def run(source,destination):

    #get info from source file
    input = FileStream(source)
    lexer = whileLangLexer(input)
    stream = CommonTokenStream(lexer)

    # create a parser
    # and parse the input (creates a tree)
    parser = whileLangParser(stream)
    tree = parser.prog()

    # visit the tree to get the number of variables
    mySemantiqueVisitor = semantiqueVisitor()
    mySemantiqueVisitor.visit(tree)
    nbVar = len(mySemantiqueVisitor.getVarList())

    # visit the tree a second time to compile to lambda calculus
    visitor = myWhileLangVisitor(nbVar,destination)
    visitor.visit(tree)

    # the output is placed in the destination file

def main(argv):

    # run the compiler for all the input programs in tests folders
    nbTests = 12
    for i in range(nbTests):
        run("tests/input"+str(i+1)+".txt", "tests/output"+str(i+1)+".txt")


if __name__ == '__main__':
    main(sys.argv)