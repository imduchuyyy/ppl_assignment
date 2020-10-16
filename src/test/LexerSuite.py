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
        self.assertTrue(TestLexer.checkLexeme("1.","1.,<EOF>",106))

    def test_wrong_decimal_interger(self):
        self.assertTrue(TestLexer.checkLexeme("0123","0123,<EOF>",107))
    
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
        self.assertTrue(TestLexer.checkLexeme(""" "hello" ""","hello,<EOF>",122))
    
    def test_string_type_with_many_character(self):
        self.assertTrue(TestLexer.checkLexeme(""" "hello worlds" ""","hello worlds,<EOF>",123))

    def test_string_type_with_backspace_character(self):
        self.assertTrue(TestLexer.checkLexeme(""" "hello\\b worlds" """, "hello\\b worlds,<EOF>",124))

    def test_string_type_with_from_feed_character(self):
        self.assertTrue(TestLexer.checkLexeme(""" "hello\\f worlds" """, "hello\\f worlds,<EOF>",125))

    def test_string_type_with_many_carriage_return_character(self):
        self.assertTrue(TestLexer.checkLexeme(""" "hello\\r worlds" """, "hello\\r worlds,<EOF>",126))
    
    def test_string_type_with_newline_character(self):
        self.assertTrue(TestLexer.checkLexeme(""" "hello\\n worlds" """, "hello\\n worlds,<EOF>",127))

    def test_string_type_with_horizontal_tab_character(self):
        self.assertTrue(TestLexer.checkLexeme(""" "hello\\t worlds" """, "hello\\t worlds,<EOF>",128))

    def test_string_type_with_sing_quote_character(self):
        self.assertTrue(TestLexer.checkLexeme(""" "hello\\' worlds" """, "hello\\' worlds,<EOF>",129))

    def test_string_type_with_backslash_character(self):
        self.assertTrue(TestLexer.checkLexeme(""" "hello worlds" """, "hello worlds,<EOF>",130))

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
    
    def test_array_1(self):
        self.assertTrue(TestLexer.checkLexeme("a[1][2]","a[1][2],<EOF>",154))

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

    def test_person_name(self):
        self.assertTrue(TestLexer.checkLexeme(""" "Bui Duc Huy" """, "Bui Duc Huy,<EOF>",163))
    
    def test_body_function(self):
        self.assertTrue(TestLexer.checkLexeme("Body: Var x = 120; EndBody", "Body,:,Var,x,=,120,;,EndBody,<EOF>",164))
    
    def test_assign_variable(self):
        self.assertTrue(TestLexer.checkLexeme("a = 2", "a,=,2,<EOF>""",165))

    def test_if_statement(self):
        self.assertTrue(TestLexer.checkLexeme("If(a == b) { Return a }", "If,(,a,==,b,),{,Return,a,},<EOF>",166))
    
    def test_parameter_declare(self):
        self.assertTrue(TestLexer.checkLexeme("Parameter: x, y,z; ", "Parameter,:,x,,,y,,,z,;,<EOF>",167))
    
    def test_string_declare(self):
        string = """ "Bui Duc Huy" """
        result = "Bui Duc Huy,<EOF>"
        self.assertTrue(TestLexer.checkLexeme("Var x = " + string, "Var,x,=,"+result,168))
    
    def test_float_declare(self):
        self.assertTrue(TestLexer.checkLexeme("Var x = 1.2", "Var,x,=,1.2,<EOF>",169))
    
    def test_many_colon(self):
        self.assertTrue(TestLexer.checkLexeme(":::::::::::::::", ":,:,:,:,:,:,:,:,:,:,:,:,:,:,:,<EOF>",170))
    
    def test_operator_9(self):
        self.assertTrue(TestLexer.checkLexeme("+-*/xyz", "+,-,*,/,xyz,<EOF>", 171))

    def test_upper_letter(self):
        self.assertTrue(TestLexer.checkLexeme("PPL", "Error Token P", 172))

    def test_while_statement(self):
        self.assertTrue(TestLexer.checkLexeme("While a == b Do x = 9", "While,a,==,b,Do,x,=,9,<EOF>", 173))
    
    def test_link(self):
        self.assertTrue(TestLexer.checkLexeme(""" "facebook.com" """, "facebook.com,<EOF>",174))
    
    def test_birth_day(self):
        self.assertTrue(TestLexer.checkLexeme("24/12/2000", "24,/,12,/,2000,<EOF>""",175))
    
    def test_variable_declare_5(self):
        self.assertTrue(TestLexer.checkLexeme("test_variable_declare_5", "test_variable_declare_5,<EOF>",176))
    
    def test_wrong_token_2(self):
        self.assertTrue(TestLexer.checkLexeme("Whitle", "Error Token W",177))
    
    def test_name(self):
        self.assertTrue(TestLexer.checkLexeme("ppl database blockchain", "ppl,database,blockchain,<EOF>",178))
    
    def test_variable_declare_6(self):
        self.assertTrue(TestLexer.checkLexeme("identify.", "identify,.,<EOF>",179))
    
    def test_operator_10(self):
        self.assertTrue(TestLexer.checkLexeme("3 > 4", "3,>,4,<EOF>",180))
    
    def test_operator_11(self):
        self.assertTrue(TestLexer.checkLexeme("3 = 5", "3,=,5,<EOF>",181))

    def test_null(self):
        self.assertTrue(TestLexer.checkLexeme("", "<EOF>",182))
    
    def test_(self):
        self.assertTrue(TestLexer.checkLexeme("_", "Error Token _",183))
    
    def test_for_statement(self):
        self.assertTrue(TestLexer.checkLexeme("For (i = 1; i < 10; i = i +1)", "For,(,i,=,1,;,i,<,10,;,i,=,i,+,1,),<EOF>",184))
    
    def test_many_dot(self):
        self.assertTrue(TestLexer.checkLexeme("hello............abc.........", "hello,.,.,.,.,.,.,.,.,.,.,.,.,abc,.,.,.,.,.,.,.,.,.,<EOF>", 185))
    
    def test_number_(self):
        self.assertTrue(TestLexer.checkLexeme("3_", "3,Error Token _",186))
    
    def test_diff_operator(self):
        self.assertTrue(TestLexer.checkLexeme("!", "!,<EOF>",187))
    
    def test_many_opearator(self):
        self.assertTrue(TestLexer.checkLexeme("!==", "!=,=,<EOF>",188))
    
    def test_many_div_operator(self):
        self.assertTrue(TestLexer.checkLexeme("//////", "/,/,/,/,/,/,<EOF>",189))

    def test_many_quotation_mark(self):
        self.assertTrue(TestLexer.checkLexeme("" "hello""", "hello,<EOF>", 190))

    def test_if_then(self):
        self.assertTrue(TestLexer.checkLexeme("If a == b Then Return c", "If,a,==,b,Then,Return,c,<EOF>", 191))
    
    def test_function(self):
        self.assertTrue(TestLexer.checkLexeme("Function: main; Body: a = a + 1; EndBody.", "Function,:,main,;,Body,:,a,=,a,+,1,;,EndBody,.,<EOF>", 192))
    
    def test_many_opearator_2(self):
        self.assertTrue(TestLexer.checkLexeme("{ }{}{}{}{}{}{}{}{}{}", "{,},{,},{,},{,},{,},{,},{,},{,},{,},{,},<EOF>", 193))
    
    def test_many_opearator_3(self):
        self.assertTrue(TestLexer.checkLexeme("((((((((()))))))))", "(,(,(,(,(,(,(,(,(,),),),),),),),),),<EOF>", 194))
    
    def test_many_identify(self):
        self.assertTrue(TestLexer.checkLexeme("blockchain is very interesting", "blockchain,is,very,interesting,<EOF>", 195))
    
    def test_date(self):
        self.assertTrue(TestLexer.checkLexeme("10:20 a.m 12/12/2020", "10,:,20,a,.,m,12,/,12,/,2020,<EOF>", 196))
    
    def test_id(self):
        self.assertTrue(TestLexer.checkLexeme("mssv: 1812336", "mssv,:,1812336,<EOF>", 197))
    
    def test_function_call(self):
        self.assertTrue(TestLexer.checkLexeme("main()", "main,(,),<EOF>", 198))
    
    def test_function_call_with_parameter(self):
        self.assertTrue(TestLexer.checkLexeme("main(a, b, c)", "main,(,a,,,b,,,c,),<EOF>", 199))
    
    def test_break_continue(self):
        self.assertTrue(TestLexer.checkLexeme("While a == b Do a = 1; Break", "While,a,==,b,Do,a,=,1,;,Break,<EOF>", 200))
