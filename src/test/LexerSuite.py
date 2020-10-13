import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    def test_lower_identifier(self):
        self.assertTrue(TestLexer.checkLexeme("x","x,<EOF>",101))

    def test_upper_identifier(self):
        self.assertTrue(TestLexer.checkLexeme("X","Error Token X",102))

    def test_lower_upper_identifier(self):
        self.assertTrue(TestLexer.checkLexeme("newVariable","newVariable,<EOF>",103))

    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?svn","ab,Error Token ?",104))
    
    def test_var_keyword(self):
        self.assertTrue(TestLexer.checkLexeme("Var","Var,<EOF>", 105))

    def test_decimal_integer(self):
        self.assertTrue(TestLexer.checkLexeme("123","123,<EOF>",106))

    # def test_wrong_decimal_interger(self):
    #     self.assertTrue(TestLexer.checkLexeme("0123","0123,<EOF>",107))
    
    def test_hexadecimal_interger(self):
        self.assertTrue(TestLexer.checkLexeme("0x123","0x123,<EOF>",108))

    def test_hexadecimal_interger_with_characters(self):
        self.assertTrue(TestLexer.checkLexeme("0xABC","0xABC,<EOF>",109))
    
    def test_hexadecimal_interger_with_upper_x(self):
        self.assertTrue(TestLexer.checkLexeme("0XABC","0XABC,<EOF>",110))
    
    def test_wrong_hexadecimal_interger_with_upper_x(self):
        self.assertTrue(TestLexer.checkLexeme("0XABCG","0XABC,Error Token G",111))

    def test_octal_interger_with_lower_o(self):
        self.assertTrue(TestLexer.checkLexeme("0o123","0o123,<EOF>",112))

    def test_octal_interger_with_upper_o(self):
        self.assertTrue(TestLexer.checkLexeme("0O123","0O123,<EOF>",113))

    def test_float(self):
        self.assertTrue(TestLexer.checkLexeme("123.12515","123.12515,<EOF>",114))

    def test_float_with_lower_e(self):
        self.assertTrue(TestLexer.checkLexeme("123e-1551","123e-1551,<EOF>",115))

    def test_float_with_upper_e(self):
        self.assertTrue(TestLexer.checkLexeme("123E-1551","123E-1551,<EOF>",116))
    
    def test_float_with_upper_e_without_sign(self):
        self.assertTrue(TestLexer.checkLexeme("123E1551","123E1551,<EOF>",117))

    def test_float_with_lower_e_without_sign(self):
        self.assertTrue(TestLexer.checkLexeme("123e1551","123e1551,<EOF>",118))
    
    def test_boolean_type_with_true(self):
        self.assertTrue(TestLexer.checkLexeme("True","True,<EOF>",119))

    def test_boolean_type_with_false(self):
        self.assertTrue(TestLexer.checkLexeme("False","False,<EOF>",120))

    def test_many_boolean_type_with_false(self):
        self.assertTrue(TestLexer.checkLexeme("False True False","False,True,False,<EOF>",121))
    
    def test_string_type(self):
        self.assertTrue(TestLexer.checkLexeme(""" "hello" """,""""hello",<EOF>""",122))
    
    def test_string_type_with_many_character(self):
        self.assertTrue(TestLexer.checkLexeme(""" "hello worlds" """,""""hello worlds",<EOF>""",123))

    # def test_string_type_with_backspace_character(self):
    #     self.assertTrue(TestLexer.checkLexeme(""" "hello worlds \b" """,""""hello worlds",<EOF>""",124))

    # def test_string_type_with_from_feed_character(self):
    #     self.assertTrue(TestLexer.checkLexeme(""" "hello worlds" """,""""hello worlds",<EOF>""",125))

    # def test_string_type_with_many_carriage_return_character(self):
    #     self.assertTrue(TestLexer.checkLexeme(""" "hello worlds" """,""""hello worlds",<EOF>""",126))
    
    # def test_string_type_with_newline_character(self):
    #     self.assertTrue(TestLexer.checkLexeme(""" "hello worlds" """,""""hello worlds",<EOF>""",127))

    # def test_string_type_with_horizontal_tab_character(self):
    #     self.assertTrue(TestLexer.checkLexeme(""" "hello worlds" """,""""hello worlds",<EOF>""",128))

    # def test_string_type_with_sing_quote_character(self):
    #     self.assertTrue(TestLexer.checkLexeme(""" "hello worlds" """,""""hello worlds",<EOF>""",129))

    # def test_string_type_with_backslash_character(self):
    #     self.assertTrue(TestLexer.checkLexeme(""" "hello worlds" """,""""hello worlds",<EOF>""",130))

    def test_body_keyword(self):
        self.assertTrue(TestLexer.checkLexeme("Body","Body,<EOF>",131))
    
    def test_many_keyword(self):
        self.assertTrue(TestLexer.checkLexeme("Then Do For Return","Then,Do,For,Return,<EOF>",132))
    
    def test_operator_1(self):
        self.assertTrue(TestLexer.checkLexeme("<","<,<EOF>",133))

    def test_operator_2(self):
        self.assertTrue(TestLexer.checkLexeme(">",">,<EOF>",134))

    def test_operator_3(self):
        self.assertTrue(TestLexer.checkLexeme("=","=,<EOF>",135))

    def test_operator_4(self):
        self.assertTrue(TestLexer.checkLexeme("==","==,<EOF>",136))
    
    def test_operator_5(self):
        self.assertTrue(TestLexer.checkLexeme("===","==,=,<EOF>",137))
    
    def test_operator_6(self):
        self.assertTrue(TestLexer.checkLexeme(">=",">=,<EOF>",138))
    
    def test_operator_7(self):
        self.assertTrue(TestLexer.checkLexeme(">>=",">,>=,<EOF>",138))

    # def test_lessop(self):
    #     self.assertTrue(TestLexer.checkLexeme("<","<,<EOF>",110))
    
    # def test_true_keyword(self):
    #     self.assertTrue(TestLexer.checkLexeme("True","True,<EOF>",111))

    # def test_false_keyword(self):
    #     self.assertTrue(TestLexer.checkLexeme("False","False,<EOF>",112))
    
    # def test_keyword_3(self):
    #     self.assertTrue(TestLexer.checkLexeme("Continue Do","Continue,Do,<EOF>",113))

    # def test_keyword_4(self):
    #     self.assertTrue(TestLexer.checkLexeme("Parameter","Parameter,<EOF>",114))

    # def test_keyword_5(self):
    #     self.assertTrue(TestLexer.checkLexeme("Function","Function,<EOF>",115))
    
    # de

