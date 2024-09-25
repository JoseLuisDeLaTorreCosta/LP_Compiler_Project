# Generated from hm.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,10,66,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,3,0,15,8,0,1,0,1,0,1,1,1,1,1,1,1,1,5,1,23,8,1,10,1,12,1,26,9,1,
        1,2,1,2,1,3,1,3,1,3,1,3,1,3,3,3,35,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,3,4,44,8,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,57,
        8,5,1,5,1,5,5,5,61,8,5,10,5,12,5,64,9,5,1,5,0,1,10,6,0,2,4,6,8,10,
        0,2,2,0,6,7,9,9,1,0,8,9,66,0,12,1,0,0,0,2,24,1,0,0,0,4,27,1,0,0,
        0,6,34,1,0,0,0,8,43,1,0,0,0,10,56,1,0,0,0,12,14,3,2,1,0,13,15,3,
        10,5,0,14,13,1,0,0,0,14,15,1,0,0,0,15,16,1,0,0,0,16,17,5,0,0,1,17,
        1,1,0,0,0,18,19,3,4,2,0,19,20,5,1,0,0,20,21,3,6,3,0,21,23,1,0,0,
        0,22,18,1,0,0,0,23,26,1,0,0,0,24,22,1,0,0,0,24,25,1,0,0,0,25,3,1,
        0,0,0,26,24,1,0,0,0,27,28,7,0,0,0,28,5,1,0,0,0,29,35,3,8,4,0,30,
        31,3,8,4,0,31,32,5,2,0,0,32,33,3,6,3,0,33,35,1,0,0,0,34,29,1,0,0,
        0,34,30,1,0,0,0,35,7,1,0,0,0,36,44,7,1,0,0,37,38,5,3,0,0,38,39,7,
        1,0,0,39,40,5,2,0,0,40,41,3,8,4,0,41,42,5,4,0,0,42,44,1,0,0,0,43,
        36,1,0,0,0,43,37,1,0,0,0,44,9,1,0,0,0,45,46,6,5,-1,0,46,57,3,4,2,
        0,47,48,5,5,0,0,48,49,3,4,2,0,49,50,5,2,0,0,50,51,3,10,5,2,51,57,
        1,0,0,0,52,53,5,3,0,0,53,54,3,10,5,0,54,55,5,4,0,0,55,57,1,0,0,0,
        56,45,1,0,0,0,56,47,1,0,0,0,56,52,1,0,0,0,57,62,1,0,0,0,58,59,10,
        3,0,0,59,61,3,10,5,4,60,58,1,0,0,0,61,64,1,0,0,0,62,60,1,0,0,0,62,
        63,1,0,0,0,63,11,1,0,0,0,64,62,1,0,0,0,6,14,24,34,43,56,62
    ]

class hmParser ( Parser ):

    grammarFileName = "hm.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'::'", "'->'", "'('", "')'", "'\\'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "OPERATOR", "INTVAL", "USTRING", 
                      "LSTRING", "WS" ]

    RULE_root = 0
    RULE_declarations = 1
    RULE_left_value = 2
    RULE_ty = 3
    RULE_simple_type = 4
    RULE_expr = 5

    ruleNames =  [ "root", "declarations", "left_value", "ty", "simple_type", 
                   "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    OPERATOR=6
    INTVAL=7
    USTRING=8
    LSTRING=9
    WS=10

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declarations(self):
            return self.getTypedRuleContext(hmParser.DeclarationsContext,0)


        def EOF(self):
            return self.getToken(hmParser.EOF, 0)

        def expr(self):
            return self.getTypedRuleContext(hmParser.ExprContext,0)


        def getRuleIndex(self):
            return hmParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = hmParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.declarations()
            self.state = 14
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 744) != 0):
                self.state = 13
                self.expr(0)


            self.state = 16
            self.match(hmParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def left_value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(hmParser.Left_valueContext)
            else:
                return self.getTypedRuleContext(hmParser.Left_valueContext,i)


        def ty(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(hmParser.TyContext)
            else:
                return self.getTypedRuleContext(hmParser.TyContext,i)


        def getRuleIndex(self):
            return hmParser.RULE_declarations

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclarations" ):
                return visitor.visitDeclarations(self)
            else:
                return visitor.visitChildren(self)




    def declarations(self):

        localctx = hmParser.DeclarationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declarations)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 18
                    self.left_value()
                    self.state = 19
                    self.match(hmParser.T__0)
                    self.state = 20
                    self.ty() 
                self.state = 26
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Left_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSTRING(self):
            return self.getToken(hmParser.LSTRING, 0)

        def INTVAL(self):
            return self.getToken(hmParser.INTVAL, 0)

        def OPERATOR(self):
            return self.getToken(hmParser.OPERATOR, 0)

        def getRuleIndex(self):
            return hmParser.RULE_left_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLeft_value" ):
                return visitor.visitLeft_value(self)
            else:
                return visitor.visitChildren(self)




    def left_value(self):

        localctx = hmParser.Left_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_left_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 704) != 0)):
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


    class TyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return hmParser.RULE_ty

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class UniTypeContext(TyContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.TyContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def simple_type(self):
            return self.getTypedRuleContext(hmParser.Simple_typeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUniType" ):
                return visitor.visitUniType(self)
            else:
                return visitor.visitChildren(self)


    class MultiTypeContext(TyContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.TyContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def simple_type(self):
            return self.getTypedRuleContext(hmParser.Simple_typeContext,0)

        def ty(self):
            return self.getTypedRuleContext(hmParser.TyContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiType" ):
                return visitor.visitMultiType(self)
            else:
                return visitor.visitChildren(self)



    def ty(self):

        localctx = hmParser.TyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ty)
        try:
            self.state = 34
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = hmParser.UniTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.simple_type()
                pass

            elif la_ == 2:
                localctx = hmParser.MultiTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.simple_type()
                self.state = 31
                self.match(hmParser.T__1)
                self.state = 32
                self.ty()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return hmParser.RULE_simple_type

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class STypeContext(Simple_typeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.Simple_typeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LSTRING(self):
            return self.getToken(hmParser.LSTRING, 0)
        def USTRING(self):
            return self.getToken(hmParser.USTRING, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSType" ):
                return visitor.visitSType(self)
            else:
                return visitor.visitChildren(self)


    class CTypeContext(Simple_typeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.Simple_typeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def simple_type(self):
            return self.getTypedRuleContext(hmParser.Simple_typeContext,0)

        def LSTRING(self):
            return self.getToken(hmParser.LSTRING, 0)
        def USTRING(self):
            return self.getToken(hmParser.USTRING, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCType" ):
                return visitor.visitCType(self)
            else:
                return visitor.visitChildren(self)



    def simple_type(self):

        localctx = hmParser.Simple_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_simple_type)
        self._la = 0 # Token type
        try:
            self.state = 43
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9]:
                localctx = hmParser.STypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                _la = self._input.LA(1)
                if not(_la==8 or _la==9):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [3]:
                localctx = hmParser.CTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                self.match(hmParser.T__2)
                self.state = 38
                _la = self._input.LA(1)
                if not(_la==8 or _la==9):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 39
                self.match(hmParser.T__1)
                self.state = 40
                self.simple_type()
                self.state = 41
                self.match(hmParser.T__3)
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return hmParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(hmParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPar" ):
                return visitor.visitPar(self)
            else:
                return visitor.visitChildren(self)


    class AplicationContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(hmParser.ExprContext)
            else:
                return self.getTypedRuleContext(hmParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAplication" ):
                return visitor.visitAplication(self)
            else:
                return visitor.visitChildren(self)


    class AbstractionContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def left_value(self):
            return self.getTypedRuleContext(hmParser.Left_valueContext,0)

        def expr(self):
            return self.getTypedRuleContext(hmParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbstraction" ):
                return visitor.visitAbstraction(self)
            else:
                return visitor.visitChildren(self)


    class ValueContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hmParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def left_value(self):
            return self.getTypedRuleContext(hmParser.Left_valueContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = hmParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 7, 9]:
                localctx = hmParser.ValueContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 46
                self.left_value()
                pass
            elif token in [5]:
                localctx = hmParser.AbstractionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 47
                self.match(hmParser.T__4)
                self.state = 48
                self.left_value()
                self.state = 49
                self.match(hmParser.T__1)
                self.state = 50
                self.expr(2)
                pass
            elif token in [3]:
                localctx = hmParser.ParContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 52
                self.match(hmParser.T__2)
                self.state = 53
                self.expr(0)
                self.state = 54
                self.match(hmParser.T__3)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 62
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = hmParser.AplicationContext(self, hmParser.ExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 58
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 59
                    self.expr(4) 
                self.state = 64
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         




