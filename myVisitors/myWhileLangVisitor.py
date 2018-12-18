from gen.whileLangVisitor import whileLangVisitor
from gen.whileLangParser import whileLangParser
from myVisitors.codePrinter import codePrinter
cp = codePrinter()

class myWhileLangVisitor(whileLangVisitor):

    def __init__(self,nbVar):
        self.nbVar = nbVar

    def needState(self,ctx):
        return "var" in ctx.getText()

    def visitProg(self, ctx: whileLangParser.ProgContext):
        #print("visitProg")
        res = ""
        if ctx.instr():
            res = self.visitInstr(ctx.instr())[0]
        with open("output.txt", "a") as myfile:
            myfile.write(res)

    def visitQuote(self, ctx: whileLangParser.QuoteContext):
        if ctx.LPAR():
            return self.visitQuote(ctx.quote())
        elif ctx.QUOTE():
            return self.visitA(ctx.a())
        return "problem Quote"


    def visitAexpr(self, ctx: whileLangParser.AexprContext):
        #print("visitAexpr")

        ctx = self.checkForList(ctx)

        txt = "("
        if self.needState(ctx):
            txt = r"(\s."

        if ctx.var():
            return r"(\s." + self.visitVar(ctx.var()) +")"
        elif ctx.quote():
            return self.visitQuote(ctx.quote())
        elif ctx.LPAR():
            return self.visitAexpr(ctx.aexpr())

        s1 = " "
        s2 = ")"
        if self.needState(ctx.aexpr(0)):
            s1 = " s "
        if self.needState(ctx.aexpr(1)):
            s2 = " s)"

        if ctx.PLUS():
            return txt + cp.add() + " " +self.visitAexpr(ctx.aexpr(0))+ s1 +self.visitAexpr(ctx.aexpr(1)) + s2
        elif ctx.MINUS():
            return txt + cp.sub() + " " +self.visitAexpr(ctx.aexpr(0))+ s1 +self.visitAexpr(ctx.aexpr(1)) + s2
        elif ctx.MULT():
            return txt + cp.mult() + " " +self.visitAexpr(ctx.aexpr(0))+ s1 +self.visitAexpr(ctx.aexpr(1)) + s2

        return "problem Aexpr"


    def visitA(self, ctx:whileLangParser.AContext):
        #print("visitA")
        if ctx.NUM():
            return cp.int(ctx.NUM().__str__())
        elif ctx.NIL():
            return cp.false()

        return "problem A"

    firstVar = True
    def visitInstr(self, ctx: whileLangParser.InstrContext, needLBRA=False):
        #print("visitInstr")

        ctx = self.checkForList(ctx)
        nTot = 0
        txt = ""

        if ctx.LPAR():
            txt, n = self.visitInstr(ctx.instr(),needLBRA)
            nTot = n
        elif ctx.ATTR():
            txt = r"(\s." + self.visitVar(ctx.var(), True) + " " + self.visitExpr(ctx.expr())+")"
            if self.firstVar:
                txt += cp.init() + cp.int(str(self.nbVar))
                self.firstVar = False
        elif ctx.SEMICOLON():

            tmptxt = self.visitInstr(ctx.instr(0))[0]



            txt, n = self.visitInstr(ctx.instr(1), True)
            if needLBRA:
                txt = txt + "("
                n += 1
            nTot = n

            if not needLBRA:
                for _ in range(nTot):
                    tmptxt = tmptxt + ")"

            txt += tmptxt

        elif ctx.WHILE():
            txt = cp.p_while() + self.visitExpr(ctx.expr()) + " " + self.visitInstr(ctx.instr())[0]

        if needLBRA and not ctx.SEMICOLON() and not ctx.LPAR():
            txt = "(" + txt
            nTot += 1
        return txt, nTot


    def visitVar(self, ctx: whileLangParser.VarContext, setter=False):
        #print("visitVar")
        if ctx.var():
            return self.visitVar(ctx.var(),setter)
        elif ctx.NUM():
            if setter:
                return "(\sve.set s v e) s " + ctx.NUM().__str__()
            else:
                return "(\sv.get s v) s "+ctx.NUM().__str__()
        return "problem Var"


    def visitExpr(self, ctx: whileLangParser.ExprContext):
        #print("visitExpr")

        ctx = self.checkForList(ctx)

        s1 = " "
        txt = "("
        if self.needState(ctx):
            txt = r"(\s."
            s1 = " s "

        if ctx.aexpr():
            return self.visitAexpr(ctx.aexpr())
        elif ctx.LPAR():
            return self.visitExpr(ctx.expr())
        elif ctx.HD():
            return txt + self.visitExpr(ctx.expr()) + s1 + cp.true() + ")"
        elif ctx.TL():
            return txt + self.visitExpr(ctx.expr()) + s1 + cp.false() + ")"

        s1 = " "
        s2 = ")"
        if self.needState(ctx.expr(0)):
            s1 = " s "
        if self.needState(ctx.expr(1)):
            s2 = " s)"

        if ctx.CONS():
            return txt + "w.w"+self.visitExpr(ctx.expr(0)) + s1 + self.visitExpr(ctx.expr(1))+ s2
        elif ctx.ISEQUAL():
            return txt + cp.eq() + " " + self.visitExpr(ctx.expr(0)) + s1 + self.visitExpr(ctx.expr(1)) + s2

        return "problem Expr"


    def visitBexpr(self, ctx: whileLangParser.BexprContext):
        print("visitBexpr")
        return "problem Bexpr"


    def checkForList(self,ctx):
        if isinstance(ctx, list):
            if len(ctx) > 1:
                print("problemos")
                return "yololo"
            return ctx[0]
        if isinstance(ctx, whileLangParser):
            pass
        return ctx
