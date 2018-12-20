from gen.whileLangVisitor import whileLangVisitor
from gen.whileLangParser import whileLangParser
from myVisitors.codePrinter import codePrinter
cp = codePrinter()
cp.setHumanReadable(False)
cp.setShortcut(True)

class myWhileLangVisitor(whileLangVisitor):

    def __init__(self,nbVar,outputfile=""):
        self.nbVar = nbVar
        self.outputfile = outputfile

    def needState(self,ctx):
        return "var" in ctx.getText()

    def visitProg(self, ctx: whileLangParser.ProgContext):
        #print("visitProg")
        res = ""
        if ctx.instr():
            res = self.visitInstr(ctx.instr())[0]
            res += " ("+ cp.init() + " " + cp.int(int(str(self.nbVar))) + ")"
        with open(self.outputfile, "w") as myfile:
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

        s1 = ") "
        s2 = "))"
        if self.needState(ctx.aexpr(0)):
            s1 = " s) ("
        if self.needState(ctx.aexpr(1)):
            s2 = " s))"

        if ctx.PLUS():
            return txt + cp.add() + " (" +self.visitAexpr(ctx.aexpr(0))+ s1 +self.visitAexpr(ctx.aexpr(1)) + s2
        elif ctx.MINUS():
            return txt + cp.sub() + " (" +self.visitAexpr(ctx.aexpr(0))+ s1 +self.visitAexpr(ctx.aexpr(1)) + s2
        elif ctx.MULT():
            return txt + cp.mult() + " (" +self.visitAexpr(ctx.aexpr(0))+ s1 +self.visitAexpr(ctx.aexpr(1)) + s2

        return "problem Aexpr"


    def visitA(self, ctx:whileLangParser.AContext):
        #print("visitA")
        if ctx.NUM():
            return cp.int(int(ctx.NUM().__str__()))
        elif ctx.NIL():
            return cp.false()

        return "problem A"

    #firstVar = True
    def visitInstr(self, ctx: whileLangParser.InstrContext, needLBRA=None):
        #print("in: "+str(needLBRA))
        #print("visitInstr")

        ctx = self.checkForList(ctx)
        txt = ""

        if needLBRA is None:
            needLBRA = []

        if ctx.LPAR():
            txt, needLBRA = self.visitInstr(ctx.instr(),needLBRA)
        elif ctx.ATTR():

            s0 = " "
            s1 = " "
            if self.needState(ctx.expr()):
                s0 = " ("
                s1 = " s)"
            txt = r"(\s." + self.visitVar(ctx.var(), True) + s0 + self.visitExpr(ctx.expr())+s1+")"

        elif ctx.SEMICOLON():

            txt0 = self.visitInstr(ctx.instr(0))[0]
            needLBRA.append(txt0)
            txt1, list = self.visitInstr(ctx.instr(1), needLBRA)
            txt = r"(\s. {} ({} s))".format(txt1,needLBRA.pop(-1))

        elif ctx.WHILE():

            #print("in while")
            txt = r" (\s. "+cp.p_while() +" "+ self.visitExpr(ctx.expr()) + " " + self.visitInstr(ctx.instr())[0]+" s)"

        #print("out: "+str(needLBRA))

        return txt, needLBRA

    def visitVar(self, ctx: whileLangParser.VarContext, setter=False):
        #print("visitVar")
        if ctx.var():
            return self.visitVar(ctx.var(),setter)
        elif ctx.NUM():
            if setter:
                return cp.set() + " s " + cp.int(int(ctx.NUM().__str__()))
            else:
                return cp.get() + " s " + cp.int(int(ctx.NUM().__str__()))
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

        s1 = ") ("
        s2 = "))"
        if self.needState(ctx.expr(0)):
            s1 = " s) ("
        if self.needState(ctx.expr(1)):
            s2 = " s))"

        if ctx.CONS():
            return txt + "w.w"+self.visitExpr(ctx.expr(0)) + s1 + self.visitExpr(ctx.expr(1))+ s2
        elif ctx.ISEQUAL():
            return txt + cp.eq() + " (" + self.visitExpr(ctx.expr(0)) + s1 + self.visitExpr(ctx.expr(1)) + s2

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
