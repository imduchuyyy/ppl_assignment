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
        Parameter: x,y
        Body: 
        EndBody.
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))
    
    # def test_wrong_miss_close(self):
    #     """Miss variable"""
    #     input = """Var: ;"""
    #     expect = "Error on line 1 col 5: ;"
    #     self.assertTrue(TestParser.checkParser(input,expect,202))