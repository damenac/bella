import sys

from antlr4 import *
from BellaLexer import BellaLexer
from BellaListener import BellaListener
from BellaParser import BellaParser


class BellaPrintListener(BellaListener):
    def enterHi(self, ctx):
        print("Hello: %s" % ctx.ID())

class BellaConcatListener(BellaListener):
    concat = ""
    def enterHi(self, ctx):
        self.concat = self.concat + ctx.ID().getText()

def main():
    lexer = BellaLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = BellaParser(stream)
    tree = parser.hi()
    printer = BellaPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    concatenator = BellaConcatListener()
    walker.walk(concatenator, tree)
    print("concatenator.concat: " + concatenator.concat)

if __name__ == '__main__':
    main()
