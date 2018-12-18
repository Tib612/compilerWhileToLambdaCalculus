from gen.whileLangVisitor import whileLangVisitor
from gen.whileLangParser import whileLangParser
from myVisitors.codePrinter import codePrinter
cp = codePrinter()

class myWhileLangVisitor(whileLangVisitor):

    def __init__(self,nbVar):
        self.nbVar = nbVar

    def visitProg(self, ctx: whileLangParser.ProgContext):
        print("visitProg")
        res = ""
        if ctx.instr():
            res = self.visitInstr(ctx.instr())
        with open("output.txt", "a") as myfile:
            myfile.write(res)
            myfile.write("(init " + str(self.nbVar) + ")")

    def visitQuote(self, ctx: whileLangParser.QuoteContext):
        if ctx.LPAR():
            return self.visitQuote(ctx.quote())
        elif ctx.QUOTE():
            return self.visitA(ctx.a())
        return "problem Quote"


    def visitAexpr(self, ctx: whileLangParser.AexprContext):
        print("visitAexpr")

        ctx = self.checkForList(ctx)

        if ctx.var():
            return r"(\s." + self.visitVar(ctx.var()) +")"
        elif ctx.quote():
            return self.visitQuote(ctx.quote())
        elif ctx.PLUS():
            return r"(\s." + cp.add() + " " +self.visitAexpr(ctx.aexpr(0))+ " " +self.visitAexpr(ctx.aexpr(1)) +")"
        elif ctx.MINUS():
            return r"(\s." + cp.sub() + " " +self.visitAexpr(ctx.aexpr(0))+ " " +self.visitAexpr(ctx.aexpr(1)) +")"
        elif ctx.MULT():
            return r"(\s." + cp.mult() + " " +self.visitAexpr(ctx.aexpr(0))+ " " +self.visitAexpr(ctx.aexpr(1)) +")"
        elif ctx.LPAR():
            return self.visitAexpr(ctx.aexpr())

        return "problem Aexpr"


    def visitA(self, ctx:whileLangParser.AContext):
        print("visitA")
        if ctx.NUM():
            return ctx.NUM().__str__()
        elif ctx.NIL():
            return cp.false()

        return "problem A"

    def visitInstr(self, ctx: whileLangParser.InstrContext):
        print("visitInstr")

        ctx = self.checkForList(ctx)
        print(ctx.getText())

        if ctx.LPAR():
            return self.visitInstr(ctx.instr())
        elif ctx.ATTR():
            return r"(\s." + self.visitVar(ctx.var(),True)+\
                   self.visitExpr(ctx.expr())+")"
        elif ctx.SEMICOLON():
            return self.visitInstr(ctx.instr(1)) + "(" + self.visitInstr(ctx.instr(0))+")"
        elif ctx.WHILE():
            return cp.recursion() + r"(\bIJs.I s (b IJ (J s))  s ) " + self.visitExpr(ctx.expr()) + " " + self.visitInstr(ctx.instr())
        return "problem Instr"

    def visitVar(self, ctx: whileLangParser.VarContext, setter=False):
        print("visitVar")
        if ctx.var():
            return self.visitVar(ctx.var(),setter)
        elif ctx.NUM():
            if setter:
                return "(\sve.set s v e) s " + ctx.NUM().__str__()
            else:
                return "(\sv.get s v) s "+ctx.NUM().__str__()
        return "problem Var"


    def visitExpr(self, ctx: whileLangParser.ExprContext):
        print("visitExpr")

        ctx = self.checkForList(ctx)

        if ctx.aexpr():
            return self.visitAexpr(ctx.aexpr())
        elif ctx.CONS():
            return r"(\sw.w"+self.visitExpr(ctx.expr(0)) + " " + self.visitExpr(ctx.expr(1))+")"
        elif ctx.ISEQUAL():
            print("ISEQUAL")
            return r"(\s." + cp.eq() + " " + self.visitExpr(ctx.expr(0)) + " s " + self.visitExpr(ctx.expr(1))+" s)"
        elif ctx.LPAR():
            return self.visitExpr(ctx.expr())
        elif ctx.HD():
            return r"(\s." + self.visitExpr(ctx.expr()) + " " + cp.true() + ")"
        elif ctx.TL():
            return r"(\s." + self.visitExpr(ctx.expr()) + " " + cp.false() + ")"

        return "problem Expr"


    def visitBexpr(self, ctx: whileLangParser.BexprContext):
        print("visitBexpr")
        return "problem Bexpr"

    def checkForList(self,ctx):
        print(type(ctx))
        if isinstance(ctx, list):
            if len(ctx) > 1:
                print("problemos")
                print(ctx)
                return "yololo"
            print(type(ctx[0]))
            return ctx[0]
        if isinstance(ctx, whileLangParser):
            pass
        return ctx
