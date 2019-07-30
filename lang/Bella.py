from antlr4 import *
from BellaLexer import BellaLexer
from BellaListener import BellaListener
from BellaParser import BellaParser
import sys

class BellaPrintListener(BellaListener):
    def enterHi(self, ctx):
        print("Hello: %s" % ctx.ID())

def main():
    lexer = BellaLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = BellaParser(stream)
    tree = parser.hi()
    printer = BellaPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    main()