# Generated from C:/Users/thibaut/PycharmProjects/compilerWhileToLambdaCalculus\whileLang.g4 by ANTLR 4.7
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\34")
        buf.write("X\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\5\3!\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\66")
        buf.write("\n\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4A\n\4\f\4")
        buf.write("\16\4D\13\4\3\5\3\5\3\5\3\5\3\5\3\5\5\5L\n\5\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\5\6T\n\6\3\7\3\7\3\7\2\3\6\b\2\4\6\b\n")
        buf.write("\f\2\3\3\2\31\32\2_\2\16\3\2\2\2\4 \3\2\2\2\6\65\3\2\2")
        buf.write("\2\bK\3\2\2\2\nS\3\2\2\2\fU\3\2\2\2\16\17\5\4\3\2\17\3")
        buf.write("\3\2\2\2\20\21\7\f\2\2\21\22\5\4\3\2\22\23\7\r\2\2\23")
        buf.write("!\3\2\2\2\24\25\7\3\2\2\25\26\5\n\6\2\26\27\5\6\4\2\27")
        buf.write("!\3\2\2\2\30\31\7\4\2\2\31\32\5\4\3\2\32\33\5\4\3\2\33")
        buf.write("!\3\2\2\2\34\35\7\6\2\2\35\36\5\6\4\2\36\37\5\4\3\2\37")
        buf.write("!\3\2\2\2 \20\3\2\2\2 \24\3\2\2\2 \30\3\2\2\2 \34\3\2")
        buf.write("\2\2!\5\3\2\2\2\"#\b\4\1\2#$\7\f\2\2$%\5\6\4\2%&\7\r\2")
        buf.write("\2&\66\3\2\2\2\'(\7\t\2\2()\5\6\4\2)*\5\6\4\13*\66\3\2")
        buf.write("\2\2+,\7\n\2\2,\66\5\6\4\n-.\7\13\2\2.\66\5\6\4\t/\60")
        buf.write("\7\5\2\2\60\61\5\6\4\2\61\62\5\6\4\b\62\66\3\2\2\2\63")
        buf.write("\66\5\b\5\2\64\66\5\n\6\2\65\"\3\2\2\2\65\'\3\2\2\2\65")
        buf.write("+\3\2\2\2\65-\3\2\2\2\65/\3\2\2\2\65\63\3\2\2\2\65\64")
        buf.write("\3\2\2\2\66B\3\2\2\2\678\f\5\2\289\7\16\2\29A\5\6\4\6")
        buf.write(":;\f\4\2\2;<\7\17\2\2<A\5\6\4\5=>\f\3\2\2>?\7\20\2\2?")
        buf.write("A\5\6\4\4@\67\3\2\2\2@:\3\2\2\2@=\3\2\2\2AD\3\2\2\2B@")
        buf.write("\3\2\2\2BC\3\2\2\2C\7\3\2\2\2DB\3\2\2\2EF\7\f\2\2FG\5")
        buf.write("\b\5\2GH\7\r\2\2HL\3\2\2\2IJ\7\b\2\2JL\5\f\7\2KE\3\2\2")
        buf.write("\2KI\3\2\2\2L\t\3\2\2\2MN\7\f\2\2NO\5\n\6\2OP\7\r\2\2")
        buf.write("PT\3\2\2\2QR\7\7\2\2RT\7\31\2\2SM\3\2\2\2SQ\3\2\2\2T\13")
        buf.write("\3\2\2\2UV\t\2\2\2V\r\3\2\2\2\b \65@BKS")
        return buf.getvalue()


class whileLangParser ( Parser ):

    grammarFileName = "whileLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':='", "';'", "'=?'", "'while'", "'var'", 
                     "'quote'", "'cons'", "'hd'", "'tl'", "'('", "')'", 
                     "'+'", "'-'", "'*'", "'/'", "'true'", "'false'", "'='", 
                     "'<'", "'>'", "'and'", "'or'", "<INVALID>", "'nil'" ]

    symbolicNames = [ "<INVALID>", "ATTR", "SEMICOLON", "ISEQUAL", "WHILE", 
                      "VAR", "QUOTE", "CONS", "HD", "TL", "LPAR", "RPAR", 
                      "PLUS", "MINUS", "MULT", "DIV", "TRUE", "FALSE", "EQUAL", 
                      "SMALLER", "BIGGER", "AND", "OR", "NUM", "NIL", "NEWLINE", 
                      "WS" ]

    RULE_prog = 0
    RULE_instr = 1
    RULE_expr = 2
    RULE_quote = 3
    RULE_var = 4
    RULE_a = 5

    ruleNames =  [ "prog", "instr", "expr", "quote", "var", "a" ]

    EOF = Token.EOF
    ATTR=1
    SEMICOLON=2
    ISEQUAL=3
    WHILE=4
    VAR=5
    QUOTE=6
    CONS=7
    HD=8
    TL=9
    LPAR=10
    RPAR=11
    PLUS=12
    MINUS=13
    MULT=14
    DIV=15
    TRUE=16
    FALSE=17
    EQUAL=18
    SMALLER=19
    BIGGER=20
    AND=21
    OR=22
    NUM=23
    NIL=24
    NEWLINE=25
    WS=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instr(self):
            return self.getTypedRuleContext(whileLangParser.InstrContext,0)


        def getRuleIndex(self):
            return whileLangParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = whileLangParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.instr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class InstrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAR(self):
            return self.getToken(whileLangParser.LPAR, 0)

        def instr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(whileLangParser.InstrContext)
            else:
                return self.getTypedRuleContext(whileLangParser.InstrContext,i)


        def RPAR(self):
            return self.getToken(whileLangParser.RPAR, 0)

        def ATTR(self):
            return self.getToken(whileLangParser.ATTR, 0)

        def var(self):
            return self.getTypedRuleContext(whileLangParser.VarContext,0)


        def expr(self):
            return self.getTypedRuleContext(whileLangParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(whileLangParser.SEMICOLON, 0)

        def WHILE(self):
            return self.getToken(whileLangParser.WHILE, 0)

        def getRuleIndex(self):
            return whileLangParser.RULE_instr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstr" ):
                listener.enterInstr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstr" ):
                listener.exitInstr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstr" ):
                return visitor.visitInstr(self)
            else:
                return visitor.visitChildren(self)




    def instr(self):

        localctx = whileLangParser.InstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_instr)
        try:
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [whileLangParser.LPAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 14
                self.match(whileLangParser.LPAR)
                self.state = 15
                self.instr()
                self.state = 16
                self.match(whileLangParser.RPAR)
                pass
            elif token in [whileLangParser.ATTR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.match(whileLangParser.ATTR)
                self.state = 19
                self.var()
                self.state = 20
                self.expr(0)
                pass
            elif token in [whileLangParser.SEMICOLON]:
                self.enterOuterAlt(localctx, 3)
                self.state = 22
                self.match(whileLangParser.SEMICOLON)
                self.state = 23
                self.instr()
                self.state = 24
                self.instr()
                pass
            elif token in [whileLangParser.WHILE]:
                self.enterOuterAlt(localctx, 4)
                self.state = 26
                self.match(whileLangParser.WHILE)
                self.state = 27
                self.expr(0)
                self.state = 28
                self.instr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAR(self):
            return self.getToken(whileLangParser.LPAR, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(whileLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(whileLangParser.ExprContext,i)


        def RPAR(self):
            return self.getToken(whileLangParser.RPAR, 0)

        def CONS(self):
            return self.getToken(whileLangParser.CONS, 0)

        def HD(self):
            return self.getToken(whileLangParser.HD, 0)

        def TL(self):
            return self.getToken(whileLangParser.TL, 0)

        def ISEQUAL(self):
            return self.getToken(whileLangParser.ISEQUAL, 0)

        def quote(self):
            return self.getTypedRuleContext(whileLangParser.QuoteContext,0)


        def var(self):
            return self.getTypedRuleContext(whileLangParser.VarContext,0)


        def PLUS(self):
            return self.getToken(whileLangParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(whileLangParser.MINUS, 0)

        def MULT(self):
            return self.getToken(whileLangParser.MULT, 0)

        def getRuleIndex(self):
            return whileLangParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = whileLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 33
                self.match(whileLangParser.LPAR)
                self.state = 34
                self.expr(0)
                self.state = 35
                self.match(whileLangParser.RPAR)
                pass

            elif la_ == 2:
                self.state = 37
                self.match(whileLangParser.CONS)
                self.state = 38
                self.expr(0)
                self.state = 39
                self.expr(9)
                pass

            elif la_ == 3:
                self.state = 41
                self.match(whileLangParser.HD)
                self.state = 42
                self.expr(8)
                pass

            elif la_ == 4:
                self.state = 43
                self.match(whileLangParser.TL)
                self.state = 44
                self.expr(7)
                pass

            elif la_ == 5:
                self.state = 45
                self.match(whileLangParser.ISEQUAL)
                self.state = 46
                self.expr(0)
                self.state = 47
                self.expr(6)
                pass

            elif la_ == 6:
                self.state = 49
                self.quote()
                pass

            elif la_ == 7:
                self.state = 50
                self.var()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 64
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 62
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = whileLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 53
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 54
                        self.match(whileLangParser.PLUS)
                        self.state = 55
                        self.expr(4)
                        pass

                    elif la_ == 2:
                        localctx = whileLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 56
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 57
                        self.match(whileLangParser.MINUS)
                        self.state = 58
                        self.expr(3)
                        pass

                    elif la_ == 3:
                        localctx = whileLangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 59
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 60
                        self.match(whileLangParser.MULT)
                        self.state = 61
                        self.expr(2)
                        pass

             
                self.state = 66
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class QuoteContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAR(self):
            return self.getToken(whileLangParser.LPAR, 0)

        def quote(self):
            return self.getTypedRuleContext(whileLangParser.QuoteContext,0)


        def RPAR(self):
            return self.getToken(whileLangParser.RPAR, 0)

        def QUOTE(self):
            return self.getToken(whileLangParser.QUOTE, 0)

        def a(self):
            return self.getTypedRuleContext(whileLangParser.AContext,0)


        def getRuleIndex(self):
            return whileLangParser.RULE_quote

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuote" ):
                listener.enterQuote(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuote" ):
                listener.exitQuote(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuote" ):
                return visitor.visitQuote(self)
            else:
                return visitor.visitChildren(self)




    def quote(self):

        localctx = whileLangParser.QuoteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_quote)
        try:
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [whileLangParser.LPAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.match(whileLangParser.LPAR)
                self.state = 68
                self.quote()
                self.state = 69
                self.match(whileLangParser.RPAR)
                pass
            elif token in [whileLangParser.QUOTE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.match(whileLangParser.QUOTE)
                self.state = 72
                self.a()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAR(self):
            return self.getToken(whileLangParser.LPAR, 0)

        def var(self):
            return self.getTypedRuleContext(whileLangParser.VarContext,0)


        def RPAR(self):
            return self.getToken(whileLangParser.RPAR, 0)

        def VAR(self):
            return self.getToken(whileLangParser.VAR, 0)

        def NUM(self):
            return self.getToken(whileLangParser.NUM, 0)

        def getRuleIndex(self):
            return whileLangParser.RULE_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = whileLangParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var)
        try:
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [whileLangParser.LPAR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 75
                self.match(whileLangParser.LPAR)
                self.state = 76
                self.var()
                self.state = 77
                self.match(whileLangParser.RPAR)
                pass
            elif token in [whileLangParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 79
                self.match(whileLangParser.VAR)
                self.state = 80
                self.match(whileLangParser.NUM)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(whileLangParser.NUM, 0)

        def NIL(self):
            return self.getToken(whileLangParser.NIL, 0)

        def getRuleIndex(self):
            return whileLangParser.RULE_a

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterA" ):
                listener.enterA(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitA" ):
                listener.exitA(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitA" ):
                return visitor.visitA(self)
            else:
                return visitor.visitChildren(self)




    def a(self):

        localctx = whileLangParser.AContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_a)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            _la = self._input.LA(1)
            if not(_la==whileLangParser.NUM or _la==whileLangParser.NIL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         




