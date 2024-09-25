# Generated from hm.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .hmParser import hmParser
else:
    from hmParser import hmParser

# This class defines a complete generic visitor for a parse tree produced by hmParser.

class hmVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by hmParser#root.
    def visitRoot(self, ctx:hmParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#declarations.
    def visitDeclarations(self, ctx:hmParser.DeclarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#left_value.
    def visitLeft_value(self, ctx:hmParser.Left_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#uniType.
    def visitUniType(self, ctx:hmParser.UniTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#multiType.
    def visitMultiType(self, ctx:hmParser.MultiTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#sType.
    def visitSType(self, ctx:hmParser.STypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#cType.
    def visitCType(self, ctx:hmParser.CTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#par.
    def visitPar(self, ctx:hmParser.ParContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#aplication.
    def visitAplication(self, ctx:hmParser.AplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#abstraction.
    def visitAbstraction(self, ctx:hmParser.AbstractionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hmParser#value.
    def visitValue(self, ctx:hmParser.ValueContext):
        return self.visitChildren(ctx)



del hmParser