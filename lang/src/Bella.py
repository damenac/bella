import sys

from antlr4 import *
from BellaLexer import BellaLexer
from BellaListener import BellaListener
from BellaParser import BellaParser

class Position(object):
    x = 0;

    def up(self, distance):
        self.x = self.x + distance;

    def down(self, distance):
        self.x = self.x - distance;


class MovesListener(BellaListener):

    position = Position()

    def enterUp(self, ctx):
        """
        Flying! This method moves up the position of the drone.
        @param ctx.NUMBER the distance to fly.
        """
        self.position.up(int(ctx.NUMBER().getText()))
        print("current.x: %s" % self.position.x)

    def enterDown(self, ctx):
        self.position.down(int(ctx.NUMBER().getText()))
        print("current.x: %s" % self.position.x)


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
