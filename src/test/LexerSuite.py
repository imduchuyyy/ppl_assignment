import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("x","x,<EOF>",101))

    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("newVariable","newVariable,<EOF>",102))

    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?svn","ab,Error Token ?",103))
    
    def test_keyword_token(self):
        self.assertTrue(TestLexer.checkLexeme("Var","Var,<EOF>", 104))

    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("123","123,<EOF>",105))

    def test_float(self):
        self.assertTrue(TestLexer.checkLexeme("123.12515","123.12515,<EOF>",106))

    def test_float_with_e(self):
        self.assertTrue(TestLexer.checkLexeme("123e-1551","123e-1551,<EOF>",107))

    def test_keyword(self):
        self.assertTrue(TestLexer.checkLexeme("Body","Body,<EOF>",108))

    def test_lessop(self):
        self.assertTrue(TestLexer.checkLexeme("<","<,<EOF>",109))

