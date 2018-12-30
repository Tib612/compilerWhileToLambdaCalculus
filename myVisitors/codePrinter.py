import sys

'''
Helper class to print lambda calculus expressions or the name of the function ( 

'''


class codePrinter():

    humanReadable = True

    def __init__(self):
        pass

    def setHumanReadable(self,bool):
        self.humanReadable = bool


    def true(self):
        if self.humanReadable:
            return "True"
        return r'(\x.(\y.x))'


    def false(self):
        if self.humanReadable:
            return "False"
        return r'(\x.(\y.y))'

    def is0(self):
        if self.humanReadable:
            return "IsZero"
        return r"(\n.n (\x." + self.false()+") " + self.true()+")"

    def le(self):
        if self.humanReadable:
            return "Leq"
        return r"(\m.(\n."+self.is0()+" ("+self.sub()+" m n)))"

    def p_and(self):
        if self.humanReadable:
            return "And"
        return r"(\p.(\q.p q p))"

    def eq(self):
        if self.humanReadable:
            return "Equal"
        return r"(\m.(\n."+self.p_and() + " (" + self.le() + " m n) (" + self.le() + " n m)))"

    def sub(self):
        if self.humanReadable:
            return "Monus"
        return r"(\m.(\n.n " + self.pred() + " m))"

    def add(self):
        if self.humanReadable:
            return "Add"
        return r"(\m.(\n.n " + self.succ() + " m))"

    def mult(self):
        if self.humanReadable:
            return "Mult"
        return r"(\m.(\n.(\f.n (m f))))"

    def pred(self):
        if self.humanReadable:
            return "Pred"
        return r"(\x.\y.\z.x(\p.\q.q(p y))(\y.z)(\x.x))"
        content = "z (" + self.succ() + " (p " + self.true() + ")) (p " + self.true() + ")"
        return r"(\n.n " + r"(\p.(\z."+content+"))" + " (\z.z "+self.int(0) + " " + self.int(0) + ") " + self.false() + ")"

    def succ(self):
        if self.humanReadable:
            return "Succ"
        content = "w x (x y)"
        return r"(\w.(\x.(\y."+content+")))"

    def recursion(self):
        if self.humanReadable:
            return "Y"
        return r"(\y.(\x. y (x x)) (\x.y (x x)))"

    def init(self):
        if self.humanReadable:
            return "Init"
        content = self.is0()+" n "+self.int(0)+" (\z.z "+self.int(0)+" (b ("+self.pred()+" n)))"
        return self.recursion() + " " + r"(\b.(\n."+content+"))"

    def int(self,val):
        if self.humanReadable:
            return str(val)
        content = "(s "*val+"z"+")"*val
        return r"(\s.(\z."+content+"))"

    def p_while(self):
        if self.humanReadable:
            return "While"
        content = "i s (b i j (j s)) s"
        return self.recursion() + " " + r"(\b.(\i.(\j.(\s."+content+"))))"

    def get(self):
        if self.humanReadable:
            return "Get"
        content = self.is0()+" n (s "+self.true()+") (b (s "+self.false()+") ("+self.pred()+" n))"
        return self.recursion() + " " + r"(\b.(\s.(\n."+content+")))"

    def set(self):
        if self.humanReadable:
            return "Sett"
        content = self.is0()+" n ("+self.cons()+" v (s "+self.false()+")) (\z.z (s "+self.true()+") (b (s "+self.false()+") ("+self.pred()+" n) v))"
        return self.recursion()+ " " + r"(\b.(\s.(\n.(\v."+content+"))))"

    def cons(self):
        if self.humanReadable:
            return "Cons"
        return r"(\a.(\b.(\z.z a b)))"

    def isBoolean(self):
        return r"(\z. " + self.is0() + " (" + self.isNil() + " z " + self.false() + " " + self.false()+ " " + self.false() + "))"

    def isNil(self):
        if self.humanReadable:
            return "IsNil"
        return r"(\p.p (\x.(\y." + self.false() + ")))"

    def booleanEval(self):
        if self.humanReadable:
            return "BooleanEval"
        return r"(\z. " + self.isBoolean() + " z z " + self.true() + ")"

    def isList(self):
        if self.humanReadable:
            return "IsList"
        return r"(\z. " + self.isBoolean() + " z " + self.false()+ r" (z (\a.(\b.(\x.x))) " + self.true()+"))"

    def equalList(self):
        if self.humanReadable:
            return "EqualList"
        content = "((" + self.booleanEval() + " a) (" + self.booleanEval() + " b) " + self.false()+ ")   (" + self.equalAny()+ r" (a "\
                  + self.true() +") (b " + self.true() + ")  (r (a " + self.false() + ") (b" + self.false() + "))   " +\
                  self.false() + "  ) " + self.true()
        return self.recursion()+ " " + r"(\r.(\a.(\b."+content+")))"

    def isInt(self):
        if self.humanReadable:
            return "IsInt"
        return "(\z. " + self.isBoolean() + " z (z " + self.false() +" "+ self.true() + ") (" + self.isList() + " z " + self.false() +" "+ self.true() + ") )"

    def p_or(self):
        if self.humanReadable:
            return "Or"
        content = "(x " + self.true() + " (y " + self.true() +" "+ self.false() + "))"
        return r"(\x.(\y."+content+"))"

    def equalAny(self):
        if self.humanReadable:
                return "EqualAny"
        contentEqualList = "((" + self.booleanEval() + " a) (" + self.booleanEval() + " b) " + self.false()+ ") (w (a "\
                  + self.true() +") (b " + self.true() + ")  (r (a " + self.false() + ") (b " + self.false() + "))   " +\
                  self.false() + "  ) " + self.true()
        contentEqualList = self.recursion()+ " " + r"(\r.(\a.(\b."+contentEqualList+")))"
        content = "(" + self.p_or() + " (" + self.isBoolean() + " a) (" + self.isBoolean() + " b))  ( (" + \
                  self.booleanEval() + " a) (" + self.booleanEval() + " b) ((" + self.booleanEval() + " b) " + \
                  self.false() +" "+ self.true() + ")) ((" + self.p_and() + " (" + self.isList() + " a) (" + self.isList()\
                  + " b) ) ((" + contentEqualList + ") a b) ((" + self.p_and() + " (" + self.isInt() + " a) (" + \
                  self.isInt() + " b)) (" + self.eq() + " a b) " + self.false() + "))"
        return self.recursion()+ " " + r"(\w.(\a.(\b."+content+")))"
