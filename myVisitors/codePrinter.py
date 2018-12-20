import sys

class codePrinter():

    humanReadable = True
    shortcut = True

    def __init__(self):
        pass

    def setHumanReadable(self,bool):
        self.humanReadable = bool

    def setShortcut(self,bool):
        self.shortcut = bool

    def true(self):
        if self.humanReadable:
            if self.shortcut:
                return "True"
            return sys._getframe(0).f_code.co_name
        content = "x"
        return self.expression(content, ["x", "y"])

    def false(self):
        if self.humanReadable:
            if self.shortcut:
                return "False"
            return sys._getframe(0).f_code.co_name
        content = "y"
        return self.expression(content, ["x", "y"])

    def is0(self):
        if self.humanReadable:
            if self.shortcut:
                return "IsZero"
            return sys._getframe(0).f_code.co_name
        return r"(\n.n (\x." + self.false()+") " + self.true()+")"

    def le(self):
        if self.humanReadable:
            return sys._getframe(0).f_code.co_name
        content = self.is0()+" ("+self.sub()+" m n)"
        return self.expression(content, ["m", "n"])

    def p_and(self):
        if self.humanReadable:
            return sys._getframe(0).f_code.co_name
        content = "p q p"
        return self.expression(content, ["p", "q"])

    def eq(self):
        if self.humanReadable:
            if self.shortcut:
                return "Equal"
            return sys._getframe(0).f_code.co_name
        content = self.p_and() + " (" + self.le() + " m n) (" + self.le() + " n m)"
        return self.expression(content, ["m", "n"])

    def sub(self):
        if self.humanReadable:
            return sys._getframe(0).f_code.co_name
        content = "n " + self.pred() + " m"
        return self.expression(content, ["m", "n"])

    def add(self):
        if self.humanReadable:
            if self.shortcut:
                return "Add"
            return sys._getframe(0).f_code.co_name
        content = "n " + self.succ() + " m"
        return self.expression(content, ["m", "n"])

    def mult(self):
        if self.humanReadable:
            return sys._getframe(0).f_code.co_name
        content = "n (m f)"
        return self.expression(content,["m","n","f"])

    def pred(self):
        if self.humanReadable:
            if self.shortcut:
                return "Pred"
            return sys._getframe(0).f_code.co_name
        content = "z (" + self.succ() + " (p " + self.true() + ")) (p " + self.true() + ")"
        return r"(\n.n " + self.expression(content,["p","z"]) + " (\z.z "+self.int(0) + " " + self.int(0) + ") " + self.false() + ")"

    def succ(self):
        if self.humanReadable:
            return sys._getframe(0).f_code.co_name
        content = "y (w y x)"
        return self.expression(content,["w","y","x"])

    def recursion(self):
        if self.humanReadable:
            if self.shortcut:
                return "Y"
            return sys._getframe(0).f_code.co_name
        return r"(\y.(\x. y (x x)) (\x.y (x x)))"

    def init(self):
        if self.humanReadable:
            if self.shortcut:
                return "Init"
            return sys._getframe(0).f_code.co_name
        content = self.is0()+" n "+self.int(0)+" (\z.z "+self.int(0)+" (b ("+self.pred()+" n)))"
        return self.recursion() + " " + self.expression(content,["b","n"])

    def int(self,val):
        if self.humanReadable:
            return str(val)
        content = "(s "*val+"z"+")"*val
        return self.expression(content,["s","z"])

    def p_while(self):
        if self.humanReadable:
            if self.shortcut:
                return "While"
            return sys._getframe(0).f_code.co_name
        content = "i s (b i j (j s)) s"
        return self.recursion() + " " + self.expression(content,["b","i","j","s"])

    def get(self):
        if self.humanReadable:
            if self.shortcut:
                return "Get"
            return sys._getframe(0).f_code.co_name
        content = self.is0()+" n (s "+self.true()+") (b (s "+self.false()+") ("+self.pred()+" n))"
        return self.recursion() + " " + self.expression(content,["b","s","n"])

    def set(self):
        if self.humanReadable:
            if self.shortcut:
                return "Sett"
            return sys._getframe(0).f_code.co_name
        content = self.is0()+" n ("+self.cons()+" v (s "+self.false()+")) (\z.z (s "+self.true()+") (b (s "+self.false()+") ("+self.pred()+" n) v))"
        return self.recursion()+ " " + self.expression(content,["b","s","n","v"])

    def cons(self):
        if self.humanReadable:
            if self.shortcut:
                return "Cons"
            return sys._getframe(0).f_code.co_name
        return self.expression(r"(\z.z a b)",["a","b"])

    def expression(self,content,vars):
        if len(vars) == 0:
            return content
        return self.expression("(\{}.{})".format(vars.pop(),content),vars)