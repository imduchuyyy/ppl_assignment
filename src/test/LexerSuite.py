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

    def test_string_type_with_backspace_character(self):
        self.assertTrue(TestLexer.checkLexeme(""" "hello\\b worlds" """, """"hello\\b worlds",<EOF>""",124))

    def test_string_type_with_from_feed_character(self):
        self.assertTrue(TestLexer.checkLexeme(""" "hello\\f worlds" """, """"hello\\f worlds",<EOF>""",125))

    def test_string_type_with_many_carriage_return_character(self):
        self.assertTrue(TestLexer.checkLexeme(""" "hello\\r worlds" """, """"hello\\r worlds",<EOF>""",126))
    
    def test_string_type_with_newline_character(self):
        self.assertTrue(TestLexer.checkLexeme(""" "hello\\n worlds" """, """"hello\\n worlds",<EOF>""",127))

    def test_string_type_with_horizontal_tab_character(self):
        self.assertTrue(TestLexer.checkLexeme(""" "hello\\t worlds" """, """"hello\\t worlds",<EOF>""",128))

    def test_string_type_with_sing_quote_character(self):
        self.assertTrue(TestLexer.checkLexeme(""" "hello\\' worlds" """, """"hello\\' worlds",<EOF>""",129))

    def test_string_type_with_backslash_character(self):
        self.assertTrue(TestLexer.checkLexeme(""" "hello worlds" """, """"hello worlds",<EOF>""",130))

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
        self.assertTrue(TestLexer.checkLexeme(">>=",">,>=,<EOF>",139))

    def test_operator_8(self):
        self.assertTrue(TestLexer.checkLexeme(">>=",">,>=,<EOF>",140))

    def test_float_without_decimal_part(self):
        self.assertTrue(TestLexer.checkLexeme("132.","132.,<EOF>",141))
    
    def test_return_stm(self):
        self.assertTrue(TestLexer.checkLexeme("Return 10a","Return,10,a,<EOF>",142))

    def test_time(self):
        self.assertTrue(TestLexer.checkLexeme("12:10 p.m","12,:,10,p,.,m,<EOF>",143))

    def test_power(self):
        self.assertTrue(TestLexer.checkLexeme("12^10","12,Error Token ^",144))
    
    def test_array(self):
        self.assertTrue(TestLexer.checkLexeme("a[1]","a[1],<EOF>",145))
    
    def test_array_with_many_interger(self):
        self.assertTrue(TestLexer.checkLexeme("a[2]","a[2],<EOF>",146))

    def test_variable_declare_1(self):
        self.assertTrue(TestLexer.checkLexeme("Var a","Var,a,<EOF>",147))
    
    def test_variable_declare_2(self):
        self.assertTrue(TestLexer.checkLexeme("Var a = 1","Var,a,=,1,<EOF>",148))
    
    def test_variable_declare_3(self):
        self.assertTrue(TestLexer.checkLexeme("Var a = 1.2","Var,a,=,1.2,<EOF>",149))

    def test_variable_declare_4(self):
        self.assertTrue(TestLexer.checkLexeme("Var a[1]","Var,a[1],<EOF>",150))

    def test_function_declare_1(self):
        self.assertTrue(TestLexer.checkLexeme("Function: a","Function,:,a,<EOF>",151))
    
    def test_function_declare_2(self):
        self.assertTrue(TestLexer.checkLexeme("Function: Hello","Function,:,Error Token H",152))

    def test_function_declare_3(self):
        self.assertTrue(TestLexer.checkLexeme("Function: 123","Function,:,123,<EOF>",153))
    
    def test_add_number_1(self):
        self.assertTrue(TestLexer.checkLexeme("a = b + c","a,=,b,+,c,<EOF>",154))

    def test_add_number_2(self):
        self.assertTrue(TestLexer.checkLexeme("a = 1 + 2","a,=,1,+,2,<EOF>",155))
    
    def test_add_number_3(self):
        self.assertTrue(TestLexer.checkLexeme("a = 1 + 2.2","a,=,1,+,2.2,<EOF>",156))
    
    def test_add_number_4(self):
        self.assertTrue(TestLexer.checkLexeme("a = 1.1 + 2.2","a,=,1.1,+,2.2,<EOF>",157))

    def test_sub_number_1(self):
        self.assertTrue(TestLexer.checkLexeme("a = 1 - 2","a,=,1,-,2,<EOF>",158))

    def test_sub_number_2(self):
        self.assertTrue(TestLexer.checkLexeme("a = 1.1 - 2","a,=,1.1,-,2,<EOF>",159))

    def test_mul_number(self):
        self.assertTrue(TestLexer.checkLexeme("a = 1 * 2","a,=,1,*,2,<EOF>",160))

    def test_div_number(self):
        self.assertTrue(TestLexer.checkLexeme("a = 1 / 2","a,=,1,/,2,<EOF>",161))

    def test_file_name(self):
        self.assertTrue(TestLexer.checkLexeme("file.txt","file,.,txt,<EOF>",162))