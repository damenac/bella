import sys

from antlr4 import *
from BellaLexer import BellaLexer
from BellaListener import BellaListener
from BellaParser import BellaParser
from Position import Position


class MovesListener(BellaListener):
    
    position = Position()

    def enterUp(self, ctx):
        """
        Flying! This method moves up the position of the drone.
        @param ctx.NUMBER the distance to fly.
        """
        self.position.up(int(ctx.NUMBER().getText()))
        print self.position.toString()

    def enterDown(self, ctx):
        """
        Flying! This method moves down the position of the drone.
        @param ctx.NUMBER the distance to fly.
        """
        self.position.down(int(ctx.NUMBER().getText()))
        print self.position.toString()


def main():
    lexer = BellaLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = BellaParser(stream)
    tree = parser.program()
    printer = MovesListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    main()
