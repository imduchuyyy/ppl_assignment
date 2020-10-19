import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_variable_declare(self):
        """Simple program: int main() {} """
        input = """Var: x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))
    
    def test_variables_declare(self):
        """Simple program: int main() {} """
        input = """Var: x,y,z;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))

    def test_variable_declare_with_value(self):
        """Simple program: int main() {} """
        input = """Var: x = 1;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test_variables_declare_with_value(self):
        """Simple program: int main() {} """
        input = """Var: x = 1, y = 2, z = 3;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,204))
    
    def test_array_variables_declare(self):
        """Simple program: int main() {} """
        input = """Var: x[1];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))

    def test_array_multi_dimensional_variables_declare(self):
        """Simple program: int main() {} """
        input = """Var: x[1][2];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))
    
    def test_array_multi_dimensional_variables_declare_with_value(self):
        """Simple program: int main() {} """
        input = """Var: x[3] = {1,2,3};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))

    def test_function_declare(self):
        """Simple program: int main() {} """
        input = """
        Function: foo 
        Parameter: x,y, a[12]
        Body:
            Var: x = 1;
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))
    
    def test_variable_declare_with_string_1(self):
        input = """
        Var: string = "hello world";
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))
    
    def test_variable_declare_with_interger(self):
        input = """
        Var: int = 123;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))

    def test_variable_declare_with_float_1(self):
        input = """
        Var: float = 1.23;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))
    
    def test_variable_declare_with_float_2(self):
        input = """
        Var: float = 3.31e1;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))

    def test_variable_declare_with_float_3(self):
        input = """
        Var: float = 3.31e-1;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,213))

    def test_variable_declare_with_float_4(self):
        input = """
        Var: float = 3.;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))

    def test_variable_declare_with_boolean_1(self):
        input = """
        Var: a = True;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,215))

    def test_variable_declare_with_boolean_2(self):
        input = """
        Var: a = False;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))
    
    def test_variable_declare_with_string_2(self):
        input = """
        Var: string = "hello world\\t";
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))

    def test_variable_declare_with_string_3(self):
        input = """
        Var: string = "hello world\\b";
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))

    def test_variable_declare_with_string_4(self):
        input = """
        Var: string = "hello world\\f";
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))

    def test_variable_declare_with_string_5(self):
        input = """
        Var: string = "hello world\\r";
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,220))
    
    def test_variable_declare_with_string_6(self):
        input = """
        Var: string = "hello world\\n";
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))

    def test_variable_declare_with_string_7(self):
        input = """
        Var: string = "hello '"duc huy '"";
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))
    
    def test_null(self):
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))

    def test_miss_comma(self):
        input = """
            Var: a b c;
        """
        expect = "Error on line 2 col 19: b"
        self.assertTrue(TestParser.checkParser(input,expect,224))
    
    def test_wrong_identify(self):
        input = """
            Var: !a;
        """
        expect = "Error on line 2 col 17: !"
        self.assertTrue(TestParser.checkParser(input,expect,225))

    def test_wrong_declare(self):
        input = """
            Var: a = 1 + 2;
        """
        expect = "Error on line 2 col 23: +"
        self.assertTrue(TestParser.checkParser(input,expect,226))

    def test_missing_semi(self):
        input = """
            Var: a = 1
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,227))

    def test_many_declare(self):
        input = """
            Var: a = 1, b =2, c;
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,228))

    def test_wrong_declare_1(self):
        input = """
            Var: 9x;
        """
        expect = "Error on line 2 col 17: 9"
        self.assertTrue(TestParser.checkParser(input,expect,229))
    
    def test_many_type_declare(self):
        input = """
            Var: x = 1, b = 2.0, c = "hello world";
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,230))

    def test_simple_function(self):
        input = """
            Function: myFunc 
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.checkParser(input,expect,231))
    
    def test_simple_function_1(self):
        input = """
            Function: myFunc
            Body:
                Var: x;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))

    def test_simple_function_parameter(self):
        input = """
            Function: myFunc
            Parameter: a, b, c
            Body:
                Var: x;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))
    
    def test_simple_function_complex_parameter(self):
        input = """
            Function: myFunc
            Parameter: param, b, c
            Body:
                Var: x;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))    

    def test_if_statement(self):
        input = """
            Var: x;
            Function: myFunc
            Parameter: n, p
            Body:
                If a == b 
                    Then a = 1;
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))    
    
    def test_complex_if_statement(self):
        input = """
            Var: x;
            Function: myFunc
            Parameter: n, p
            Body:
                If (a > b) && (b < a)  
                    Then a = 1;
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))    
    
    def test_if_else_if_statement  (self):
        input = """
            Var: x;
            Function: myFunc
            Parameter: n, p
            Body:
                If (a > b) && (b < a)  
                    Then a = 1;
                ElseIf (c > a) Then c = 1;
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,237))

    def test_if_else_statement  (self):
        input = """
            Var: x;
            Function: myFunc
            Parameter: n, p
            Body:
                If (a > b) && (b < a)  
                    Then a = 1;
                Else c = 1;
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))
    
    def test_if_many_else_if_statement  (self):
        input = """
            Var: x;
            Function: myFunc
            Parameter: n, p
            Body:
                If (a > b) && (b < a)  
                    Then a = 1;
                ElseIf (c > 1) Then c = 1;
                ElseIf (c > 2) Then c = 1;
                ElseIf (c > 3) Then c = 1;
                ElseIf (c > 4) Then c = 1;
                ElseIf (c > 5) Then c = 1;
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,239))

    def test_if_else_with_no_expression  (self):
        input = """
            Var: x;
            Function: myFunc
            Parameter: n, p
            Body:
                If (a > b) && (b < a)  
                    Then
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,240))
    
    def test_for_statement  (self):
        input = """
            Var: x;
            Function: myFunc
            Parameter: n, p
            Body:
                For(a = 1, a > 1, 2) Do  
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,241))

    def test_complex_for_statement  (self):
        input = """
            Var: x;
            Function: myFunc
            Parameter: n, p
            Body:
                For(a = 1, a > 1, a  = a +1) Do  
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))

    def test_if_for_statement  (self):
        input = """
            Var: x;
            Function: myFunc
            Parameter: b
            Body:
                For(a = 1, a > 1, a  = a +1) Do
                    If a == b Then Return a;
                    EndIf.
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))

    def test_complex_if_statement_1  (self):
        input = """
            Var: x;
            Function: myFunc
            Parameter: b
            Body:
                If a > b Then Return a;
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))
    
    def test_complex_if_statement_2  (self):
        input = """
            Var: x;
            Function: myFunc
            Parameter: b
            Body:
                If a =/= b Then Return a;
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))

    def test_complex_if_statement_3  (self):
        input = """
            Var: x;
            Function: myFunc
            Parameter: b
            Body:
                If a != b Then Return a;
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,246))

    def test_complex_for_if_statement_4  (self):
        input = """
            Var: x;
            Function: myFunc
            Parameter: b
            Body:
                For(a = 1, a > 1, a  = a +1) Do
                    If a + 1 == b Then 
                        Return a;
                    EndIf.
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))

    def test_complex_for_if_statement_5(self):
        input = """
            Var: x;
            Function: myFunc
            Parameter: b
            Body:
                For(a = 1, a / b == 2, a  = a +1) Do
                    If a + 1 == b Then 
                        Return a;
                    EndIf.
                EndFor.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))
    
    def test_variable_condition_in_if_statement  (self):
        input = """
            Var: x;
            Function: myFunc
            Parameter: b
            Body:
                If a Then Return a;
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))

    def test_missing_endfor  (self):
        input = """
            Var: x;
            Function: myFunc
            Parameter: b
            Body:
                For(a = 1, a / b == 2, a  = a +1) Do
                    If a + 1 == b Then 
                        Return a;
                    EndIf.
                
            EndBody.
        """
        expect = "Error on line 11 col 12: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,250))

    def test_break_statement  (self):
        input = """
            Var: x;
            Function: myFunc
            Parameter: b
            Body:
                Break;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,251))
    
    def test_while_statement  (self):
        input = """
            Var: x;
            Function: myFunc
            Parameter: b
            Body:
                While a == b Do a = 1; EndWhile.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,252))

    def test_while_for_statement  (self):
        input = """
            Var: x;
            Function: myFunc
            Parameter: b
            Body:
                While a == b Do 
                    For(a = 1, a > 1, a  = a +1) Do
                        a = a + 1;
                    EndFor.
                EndWhile.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))
    
    def test_while_for_if_statement  (self):
        input = """
            Var: x;
            Function: myFunc
            Parameter: b
            Body:
                While a == b Do 
                    For(a = 1, a / b == 2, a  = a +1) Do
                        If a + 1 == b Then 
                            Return a;
                        EndIf.
                    EndFor.
                EndWhile.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))
    
    def test_do_while_statement  (self):
        input = """
            Var: x;
            Function: myFunc
            Parameter: b
            Body:
                Do 
                    For(a = 1, a / b == 2, a  = a +1) Do
                        If a + 1 == b Then 
                            Return a;
                        EndIf.
                    EndFor.
                While a == b
                EndWhile.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))

    def test_do_while_statement_1  (self):
        input = """
            Var: x;
            Function: myFunc
            Parameter: b
            Body:
                Do 
                    a = a + 1;
                While a == b
                EndWhile.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,256))

    def test_do_while_statement_2  (self):
        input = """
            Var: x;
            Function: myFunc
            Parameter: b
            Body:
                Do 
                    If a == 10 Then Return a;
                    EndIf.
                While a == b
                EndWhile.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))
    
    def test_do_while_statement_3  (self):
        input = """
            Var: x;
            Function: myFunc
            Parameter: b
            Body:
                Do 
                    If a[1][2] == 10 Then Return a;
                    EndIf.
                While a == b
                EndWhile.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))
    
    def test_continue_statement  (self):
        input = """
            Var: x;
            Function: myFunc
            Parameter: b
            Body:
                Do 
                    If a == 10 Then Continue;
                    a = a + 1;
                    EndIf.
                While a == b
                EndWhile.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,259))
    
    def test_call_function  (self):
        input = """
            Var: x;
            Function: myFunc
            Parameter: b
            Body:
                foo();
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))
    
    def test_call_function_with_parameter  (self):
        input = """
            Var: x;
            Function: myFunc
            Parameter: b
            Body:
                foo(a, b, c);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))

    def test_call_function_with_expression  (self):
        input = """
            Var: x;
            Function: myFunc
            Parameter: b
            Body:
                foo(a + 1, a / 2, 1 + 1 / 2);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,262))
    
    def test_return_statement (self):
        input = """
            Var: x;
            Function: myFunc
            Parameter: b
            Body:
                Return a;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,263))
    
    def test_complex_return_statement (self):
        input = """
            Var: x;
            Function: myFunc
            Parameter: b
            Body:
                Return a /3 + c/2 + b*2;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,264))
    
    def test_print_ln_function (self):
        input = """
            Var: x;
            Function: myFunc
            Parameter: b
            Body:
                printLn();
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,265))
    
    def test_print_function (self):
        input = """
            Var: x;
            Function: myFunc
            Parameter: b
            Body:
                print("hello world!");
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,266))

    def test_print_str_ln_function (self):
        input = """
            Var: x;
            Function: myFunc
            Parameter: b
            Body:
                printStrLn("hello world!");
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,267))
    
    def test_read_function (self):
        input = """
            Var: x;
            Function: myFunc
            Parameter: b
            Body:
                read();
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,268))

    def test_hello_world_program (self):
        input = """
            Var: x;
            Function: helloWorldProgram
            Parameter: b
            Body:
                print("hello world!");
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,269))

    def test_read_name_program (self):
        input = """
            Var: x;
            Function: readNameProgram
            Parameter: b
            Body:
                Var: x, hello;
                x = read();
                hello = "Hello "+ x;
                print(hello);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,270))
    
    def test_sum_program (self):
        input = """
            Function: sumProgram
            Body:
                Var: x, y, sum;
                print("input x: ");
                x = read();
                print("input y: ");
                y = read();
                sum = x + y;
                print(sum);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,271))

    def test_mul_program (self):
        input = """
            Function: mulProgram
            Body:
                Var: x, y, mul;
                print("input x: ");
                x = read();
                print("input y: ");
                y = read();
                mul = x * y;
                print(mul);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,272))
    
    def test_recursive_program (self):
        input = """
            Function: recursive
            Parameter: n
            Body:
                print (n);
                recursive(n -1);
            EndBody.
            Function: recursiveProgram
            Body:
                Var: n, result;
                print("input n: ");
                n = read();
                recursive(n);
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,273))
    
    def test_if_in_if (self):
        input = """
            Function: recursiveProgram
            Body:
                If a == b Then
                    If b == c Then
                        If c == d Then
                            print(d);
                        EndIf.
                    EndIf.
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,274))
    
    def test_missing_endif(self):
        input = """
            Function: recursiveProgram
            Body:
                If a == b Then
                    If b == c Then
                        If c == d Then
                            print(d);
                    EndIf.
                EndIf.
            EndBody.
        """
        expect = "Error on line 10 col 12: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,275))
    
    def test_declare_array(self):
        input = """
            Function: recursiveProgram
            Body:
                Var: a[1][2][3];
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,276))
    
    def test_while_without_end(self):
        input = """
            Function: recursiveProgram
            Body:
                While a == b Do a = a + 1;
            EndBody.
        """
        expect = "Error on line 5 col 12: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,277))

    def test_while_without_do(self):
        input = """
            Function: recursiveProgram
            Body:
                While a == b EndWhile.;
            EndBody.
        """
        expect = "Error on line 4 col 16: While"
        self.assertTrue(TestParser.checkParser(input,expect,278))

    def test_complex_program(self):
        input = """
            Function: recursive
            Parameter: n
            Body:
                print (n);
                recursive(n -1);
            EndBody.
            Function: recursiveProgram
            Body:
                Var: n, result;
                print("input n: ");
                n = read();
                recursive(n);
                If a == b Then
                    If b == c Then
                        If c == d Then
                            print(d);
                        EndIf.
                    EndIf.
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,279))

    def test_complex_if_statement_4(self):
        input = """
            Function: recursive
            Parameter: n
            Body:
                print (n);
                recursive(n -1);
            EndBody.
            Function: recursiveProgram
            Body:
                If 4.5 <=. foo() *. (3 *. 1.0) Then
                    EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,280))

    def test_array_declare(self):
        input = """
            Function: recursive
            Parameter: n
            Body:
                print (n);
                recursive(n -1);
            EndBody.
            Function: recursiveProgram
            Body:
                Var: a[2] = {123,1};
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,281))
    
    def test_using_array(self):
        input = """
            Function: recursive
            Parameter: n
            Body:
                print (n);
                recursive(n -1);
            EndBody.
            Function: recursiveProgram
            Body:
                Var: a[2] = {123,1};
                a[1] = 1;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,282))
    
    def test_array_string(self):
        input = """
            Function: arrayFun
            Parameter: array, n
            Body:
                Var: array[2] = {"hello","world"};
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,283))
    
    def test_array_string_1(self):
        input = """
            Function: arrayFun
            Parameter: array, n
            Body:
                Var: array[2] = {"hell","world"};
                array[0] = "hello";
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,284))
    
    def test_while_continue(self):
        input = """
            Function: arrayFun
            Parameter: array, n
            Body:
                While array[1] == 3 Do Continue;
                EndWhile.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,285))
        
    def test_if_continue(self):
        input = """
            Function: arrayFun
            Parameter: array, n
            Body:
                If array[1] == 3 Then Continue;
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,286))

    def test_if_with_string(self):
        input = """
            Function: arrayFun
            Parameter: array, n
            Body:
                If array[0] == "hello" Then array[1] = "world";
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,287))
    
    def test_array_boolean(self):
        input = """
            Function: arrayFun
            Parameter: array, n
            Body:
                If array[0] == True Then array[1] = False;
                EndIf.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,288))
    
    def test_assign_boolean(self):
        input = """
            Function: arrayFun
            Parameter: array, n
            Body:
                array[0] = True;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,289))
    
    def test_logic(self):
        input = """
            Function: arrayFun
            Parameter: array, n
            Body:
                array[0] = True;
                array[0] = array[0] + 1; 
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,290))
    
    def test_many_while(self):
        input = """
            Function: arrayFun
            Parameter: array, n
            Body:
                While 1 == 1 Do a = 1 + 1;
                    While 1 == 1 Do a = 1 + 1;
                        While 1 == 1 Do a = 1 + 1;
                            While 1 == 1 Do a = 1 + 1;
                            EndWhile.
                        EndWhile.
                    EndWhile.
                EndWhile.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,291))
    
    def test_simple_function_2(self):
        input = """
            Function: arrayFun
            Parameter: array, n
            Body:
                a = 1;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,292))
    
    def test_simple_function_3(self):
        input = """
            Function: arrayFun
            Parameter: array, n
            Body:
                x = "hello";
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,293))
    
    def test_simple_function_4(self):
        input = """
            Function: arrayFun
            Parameter: array, n
            Body:
                x = "hello";
                y = 1.1;
                z = x + y;
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,294))
    
    def test_simple_function_5(self):
        input = """
            Function: arrayFun
            Parameter: array, n
            Body:
                Var: x = 1;
                x = array[1];
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,295))
    
    def test_print_array(self):
        input = """
            Function: arrayFun
            Parameter: array, n
            Body:
                Var: x = 0, temp;
                While x <= n Do 
                    temp = array[x];
                    print(temp);
                EndWhile.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,296))
    
    def test_search_array(self):
        input = """
            Function: arrayFun
            Parameter: array, n, target
            Body:
                Var: x, temp;
                x = 0 ;
                While x <= n Do 
                    If array[x] == target Then print(x);
                    EndIf.
                EndWhile.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,297))
    
    def test_plus_array(self):
        input = """
            Function: arrayFun
            Parameter: array, n, target
            Body:
                Var: x, temp;
                x = 0 ;
                While x <= n Do 
                    x = array[x];
                EndWhile.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,298))
    
    def test_while_break(self):
        input = """
            Function: arrayFun
            Parameter: array, n, target
            Body:
                While x <= n Do 
                    Break;
                EndWhile.
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,299))
    
    def test_done_function(self):
        input = """
            Function: arrayFun
            Parameter: array, n, target
            Body:
                print("Done Parser!");
            EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,300))