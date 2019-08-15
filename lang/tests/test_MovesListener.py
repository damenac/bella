import unittest
import sys
import StringIO

from antlr4 import *
from Bella import MovesListener
from BellaLexer import BellaLexer
from BellaListener import BellaListener
from BellaParser import BellaParser
from Position import Position


class MovesListenerTest(unittest.TestCase):

    def testNominalUp(self):
        self.assertEqual(self.interpret("up 10").position.x, 10)

    def testNominalDown(self):
        self.assertEqual(self.interpret("down 10").position.x, -10)

    def interpret(self, code):
        stream = InputStream(code)
        lexer = BellaLexer(stream)
        stream = CommonTokenStream(lexer)
        parser = BellaParser(stream)
        tree = parser.program()
        printer = MovesListener()
        printer.position = Position()
        walker = ParseTreeWalker()
        walker.walk(printer, tree)
        return printer

if __name__ == '__main__':
    unittest.main()
