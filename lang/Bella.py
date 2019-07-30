from antlr4 import *
from bellaLexer import bellaLexer
from bellaListener import bellaListener
from bellaParser import bellaParser
import sys

class BellaPrintListener(bellaListener):
    def enterHi(self, ctx):
        print("Hello: %s" % ctx.ID())

def main():
    lexer = bellaLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = bellaParser(stream)
    tree = parser.hi()
    printer = bellaPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    main()