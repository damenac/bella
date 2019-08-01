import sys

from antlr4 import *
from BellaLexer import BellaLexer
from BellaListener import BellaListener
from BellaParser import BellaParser


class BellaPrintListener(BellaListener):

    def enterUp(self, ctx):
        print("up: %s" % ctx.ID())

    def enterDown(self, ctx):
        print("down: %s" % ctx.ID())


def main():
    lexer = BellaLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = BellaParser(stream)
    tree = parser.program()
    printer = BellaPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    main()
