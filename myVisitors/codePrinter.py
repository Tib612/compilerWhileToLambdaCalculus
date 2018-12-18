import sys

class codePrinter():

    humanReadable = True

    def __init__(self):
        pass

    def setHumanReadable(self,bool):
        self.humanReadable = bool

    def true(self):
        if self.humanReadable:
            return sys._getframe(0).f_code.co_name
        return r"(\xy.x)"

    def false(self):
        if self.humanReadable:
            return sys._getframe(0).f_code.co_name
        return r"(\xy.y)"

    def is0(self):
        if self.humanReadable:
            return sys._getframe(0).f_code.co_name
        return r"(\n.n (\x." + self.false()+")"+" " + self.true()+")"

    def le(self):
        if self.humanReadable:
            return sys._getframe(0).f_code.co_name
        return r"\mn."+self.is0()+" ("+self.sub()+" m n)"

    def p_and(self):
        if self.humanReadable:
            return sys._getframe(0).f_code.co_name
        return r"(\pq.p q p)"

    def eq(self):
        if self.humanReadable:
            return sys._getframe(0).f_code.co_name
        return r"(\mn." + self.p_and() + "(" + self.le() + "m n)(" + self.le() + "nm))"

    def sub(self):
        if self.humanReadable:
            return sys._getframe(0).f_code.co_name
        return r"(\mn.n " + self.pred() + " m)"

    def add(self):
        if self.humanReadable:
            return sys._getframe(0).f_code.co_name
        return r"(\mn.n " + self.succ() + " m)"

    def mult(self):
        if self.humanReadable:
            return sys._getframe(0).f_code.co_name
        return r"(\mnf.n (m f) )"

    def pred(self):
        if self.humanReadable:
            return sys._getframe(0).f_code.co_name
        return r"(\n.n(\pz.z("+self.succ()+"(pT))(pT))(\z.z(\sz.z)(\sz.z))F)"

    def succ(self):
        if self.humanReadable:
            return sys._getframe(0).f_code.co_name
        return r"(\wyx.y(wyx)"

    def recursion(self):
        if self.humanReadable:
            return sys._getframe(0).f_code.co_name
        return r"(\y.(\x. y (x x)) (\x. y (x x)) )"

    def init(self):
        if self.humanReadable:
            return sys._getframe(0).f_code.co_name
        return self.recursion()+r"(\bn.Zn0(\z.z0(b Pn)))"

    def int(self,val):
        if self.humanReadable:
            return val
        return r"(\sz."+"(s"*val+"z"+")"*val+")"

    def p_while(self):
        if self.humanReadable:
            return sys._getframe(0).f_code.co_name
        return self.recursion() + r"(\bIJs.I s (b IJ (J s))  s ) "
