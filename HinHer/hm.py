from __future__ import annotations
from antlr4 import *
from hmLexer import hmLexer
from hmParser import hmParser
from hmVisitor import hmVisitor
from random import *
import streamlit as st
import pandas as pd
from dataclasses import dataclass


lastnode = 0


@dataclass
class Buit:
    pass


@dataclass
class Aplication:
    esq: Arbre
    dre: Arbre
    type: list


@dataclass
class Abstraction:
    esq: Arbre
    dre: Arbre
    type: list


@dataclass
class Leaf:
    val: str
    type: list


Arbre = Aplication | Abstraction | Leaf


def write_type(l):
    ty = ""
    if isinstance(l[0], str):
        ty += str(l[0])
    else:
        ty += write_type(l[0])

    if len(l) > 1:
        ty = "(" + ty + " -> " + write_type(l[1:]) + ")"

    return ty


def getValue(t: Arbre):
    match t:
        case Aplication(_, _, _):
            return "@"
        case Abstraction(_, _, _):
            return "λ"
        case Leaf(val, _):
            return val


def getType(t: Arbre):
    match t:
        case Aplication(_, _, type):
            return type
        case Abstraction(_, _, type):
            return type
        case Leaf(_, type):
            return type


def getEsq(t: Arbre):
    match t:
        case Aplication(esq, _, _):
            return esq
        case Abstraction(esq, _, _):
            return esq
        case Leaf(_, _):
            return None


def getDret(t: Arbre):
    match t:
        case Aplication(_, dre, _):
            return dre
        case Abstraction(_, dre, _):
            return dre
        case Leaf(_, _):
            return None


def modifyType(t: Arbre, newType):
    match t:
        case Aplication(esq, dre, _):
            return Aplication(esq, dre, newType)
        case Abstraction(esq, dre, _):
            return Abstraction(esq, dre, newType)
        case Leaf(val, _):
            return Leaf(val, newType)


def drawTree(t: Arbre):
    global lastnode
    match t:
        case Buit():
            return "", ""
        case Aplication(esq, dre, type) | Abstraction(esq, dre, type):
            subg_e, node_e = drawTree(esq)
            subg_d, node_d = drawTree(dre)
            node = str(lastnode)
            lastnode += 1
            graph = node + '[label= "@  \n' + write_type(type) + '"] '
            graph += node + ' -- ' + node_e + ' '
            graph += node + ' -- ' + node_d + ' '
            return (graph + subg_e + subg_d), node

        case Leaf(val, type):
            node = str(lastnode)
            lastnode += 1
            graph = node + '[label= "' + \
                str(val) + '\n' + write_type(type) + '"] '
            return graph, node


def getNoDeclaredTypes(tVis: Arbre, tEval: Arbre):
    match tVis, tEval:
        case Buit(), Buit():
            return [], []

        case Leaf(_, Vtype), Leaf(_, Etype):
            if generic(Vtype):
                return [Vtype], [write_type(Etype)]

            return [], []

        case (Aplication(Vesq, Vdret, Vtype), Aplication(Eesq, Edret, Etype)) | (Abstraction(Vesq, Vdret, Vtype), Abstraction(Eesq, Edret, Etype)):
            VTypesE, ETypesE = getNoDeclaredTypes(Vesq, Eesq)
            VTypesD, ETypesD = getNoDeclaredTypes(Vdret, Edret)

            VTypes = VTypesE + VTypesD
            ETypes = ETypesE + ETypesD

            if generic(Vtype):
                VTypes.append(Vtype)
                ETypes.append(write_type(Etype))

            return VTypes, ETypes


class TreeVisitor(hmVisitor):
    def __init__(self):
        self.tree = Buit()
        self.symtable = dict([])
        self.lasttype = 97

    def visitRoot(self, ctx):
        self.visit(ctx.declarations())
        if ctx.expr():
            self.tree = self.visit(ctx.expr())

    def visitDeclarations(self, ctx):
        for i in range(len(ctx.left_value())):
            self.symtable[ctx.left_value(i).getText()] = (
                self.visit(ctx.ty(i)), "DECLARED")

    def visitSType(self, ctx):
        return ctx.getText()

    def visitCType(self, ctx):
        t1 = [ctx.getChild(1).getText()]
        t2 = self.visit(ctx.simple_type())
        if len(t2) == 1:
            return t1 + [t2]
        else:
            return t1 + t2

    def visitUniType(self, ctx):
        return [self.visit(ctx.simple_type())]

    def visitMultiType(self, ctx):
        t1 = self.visit(ctx.simple_type())
        t2 = self.visit(ctx.ty())
        return [t1] + t2

    def visitLeft_value(self, ctx):
        type = self.symtable.get(ctx.getText(), "NOT FOUND")
        if type == "NOT FOUND":
            type = chr(self.lasttype)
            self.symtable[ctx.getText()] = (type, "NO DECLARED")
            self.lasttype += 1
        else:
            type = type[0]
        return Leaf(ctx.getText(), type)

    def visitValue(self, ctx):
        return self.visit(ctx.left_value())

    def visitAplication(self, ctx):
        type = chr(self.lasttype)
        self.lasttype += 1
        node_esq = self.visit(ctx.expr(0))
        node_dre = self.visit(ctx.expr(1))
        return Aplication(node_esq, node_dre, type)

    def visitAbstraction(self, ctx):
        type = chr(self.lasttype)
        self.lasttype += 1
        node_esq = self.visit(ctx.left_value())
        node_dre = self.visit(ctx.expr())
        return Abstraction(node_esq, node_dre, type)

    def visitPar(self, ctx):
        return self.visit(ctx.expr())


def generic(t):
    for subt in t:
        if ord(subt) >= 97:
            return True
    return False


def t2_in_t1(t1, t2):
    if t1[:len(t2)] == t2:
        return True, t1[:len(t2)] + t1[1 + len(t2):]
    return False, ""


class EvalVisitor(hmVisitor):
    def __init__(self, symtable):
        self.symtable = symtable
        self.tree = Buit()
        self.why_error = ""

    def visitRoot(self, ctx):
        if ctx.expr():
            self.tree = self.visit(ctx.expr())

    def visitLeft_value(self, ctx):
        type = self.symtable[ctx.getText()][0]
        return Leaf(ctx.getText(), type)

    def visitAplication(self, ctx):
        t1 = self.visit(ctx.expr(0))
        t2 = self.visit(ctx.expr(1))
        if t1 is None or t2 is None:
            return None
        if generic(getType(t2)):
            self.symtable[getValue(t2)] = ([getType(t1)[0]], "NO DECLARED")
            t2 = modifyType(t2, [getType(t1)[0]])

        found, type = t2_in_t1(getType(t1), getType(t2))
        if found:
            return Aplication(t1, t2, type)
        else:
            self.why_error = write_type(
                getType(t1)[0]) + " vs " + write_type(getType(t2)[0])
            return None

    def visitAbstraction(self, ctx):
        t2 = self.visit(ctx.expr())
        t1 = self.visit(ctx.left_value())
        if t1 is None or t2 is None:
            return None
        return Abstraction(t1, t2, getType(t1) + getType(t2))

    def visitPar(self, ctx):
        return self.visit(ctx.expr())


def main():
    container = st.container()
    input = st.text_area("Expressió:")
    symbol_table = dict([])

    if (st.button("fer")):
        input_stream = InputStream(input)
        lexer = hmLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        parser = hmParser(token_stream)
        tree = parser.root()
        errors = parser.getNumberOfSyntaxErrors()

        if errors > 0:
            st.write(errors, 'errors de sintaxi.')
        else:
            visitor = TreeVisitor()
            visitor.visit(tree)
            arbre = visitor.tree
            symbol_table = visitor.symtable.copy()
            if arbre is not None:
                g, _ = drawTree(arbre)
                graph = "graph { " + g + "}"

                if graph != "graph { }":
                    st.graphviz_chart(graph, False)

            if len(symbol_table) > 0:
                vars = list(symbol_table.keys())
                types = list(symbol_table.values())
                for var in vars:
                    type = symbol_table[var]
                    if type[1] == "NO DECLARED":
                        del symbol_table[var]
                vars = list(symbol_table.keys())
                types = [write_type(x[0]) for x in list(symbol_table.values())]
                with container:
                    st.table(
                        pd.DataFrame(
                            types,
                            index=vars,
                            columns=["Tipus"]))

            evaluator = EvalVisitor(visitor.symtable)
            evaluator.visit(tree)
            arbre_eval = evaluator.tree
            if arbre_eval is not None:
                g, _ = drawTree(arbre_eval)
                graph = "graph { " + g + "}"

                if graph != "graph { }":
                    st.graphviz_chart(graph, False)

                VTypesE, ETypesE = getNoDeclaredTypes(arbre, arbre_eval)
                if len(VTypesE) > 0:
                    st.table(dict([(i, j) for i, j in zip(VTypesE, ETypesE)]))
            else:
                st.write("Type error: " + evaluator.why_error)


main()
