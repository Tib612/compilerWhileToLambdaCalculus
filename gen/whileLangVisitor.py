# Generated from C:/Users/thibaut/PycharmProjects/compilerWhileToLambdaCalculus\whileLang.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .whileLangParser import whileLangParser
else:
    from whileLangParser import whileLangParser

# This class defines a complete generic visitor for a parse tree produced by whileLangParser.

class whileLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by whileLangParser#prog.
    def visitProg(self, ctx:whileLangParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by whileLangParser#instr.
    def visitInstr(self, ctx:whileLangParser.InstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by whileLangParser#expr.
    def visitExpr(self, ctx:whileLangParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by whileLangParser#quote.
    def visitQuote(self, ctx:whileLangParser.QuoteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by whileLangParser#var.
    def visitVar(self, ctx:whileLangParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by whileLangParser#a.
    def visitA(self, ctx:whileLangParser.AContext):
        return self.visitChildren(ctx)



del whileLangParser