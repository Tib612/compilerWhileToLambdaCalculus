from gen.whileLangVisitor import whileLangVisitor
from gen.whileLangParser import whileLangParser


class semantiqueVisitor(whileLangVisitor):

    variables = set()

    def getVarList(self):
        return self.variables

    def visitBexpr(self, ctx: whileLangParser.BexprContext):
        return super().visitBexpr(ctx)

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

    def visitAexpr(self, ctx: whileLangParser.AexprContext):
        return super().visitAexpr(ctx)

    def visitInstr(self, ctx: whileLangParser.InstrContext):
        return super().visitInstr(ctx)
