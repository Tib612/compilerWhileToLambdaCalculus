from gen.whileLangVisitor import whileLangVisitor
from gen.whileLangParser import whileLangParser


class semantiqueVisitor(whileLangVisitor):

    def __init__(self):
        self.variables = set([])

    def getVarList(self):
        return self.variables

    def visitProg(self, ctx: whileLangParser.ProgContext):
        return super().visitProg(ctx)

    def visitVar(self, ctx: whileLangParser.VarContext):
        if ctx.VAR():
            self.variables.add(int(ctx.NUM().__str__() ))
        return super().visitVar(ctx)

    def visitExpr(self, ctx: whileLangParser.ExprContext):
        return super().visitExpr(ctx)

    def visitA(self, ctx: whileLangParser.AContext):
        return super().visitA(ctx)

    def visitInstr(self, ctx: whileLangParser.InstrContext):
        return super().visitInstr(ctx)
