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

    # def test_variable_declare_with_boolean_1(self):
    #     input = """
    #     Var: bool = True;
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,215))

    # def test_variable_declare_with_boolean_2(self):
    #     input = """
    #     Var: bool = False;
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,216))
    
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
    
    # def test_variable_declare_with_array_1(self):
    #     input = """
    #     Var: array[1] = { 1 };
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect,223))