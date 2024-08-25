import unittest

from interpreter import Interpreter


class TestArithmeticInterpreter(unittest.TestCase):
    def setUp(self):
        self.interpreter = Interpreter()
        pass

    def interpret(self, expression):
        return self.interpreter.interpret(expression)

    def test_basic_operations(self):
        self.assertEqual(self.interpret("1 + 2"), 3)
        self.assertEqual(self.interpret("4 - 3"), 1)
        self.assertEqual(self.interpret("2 * 3"), 6)
        self.assertEqual(self.interpret("8 / 4"), 2)

    def test_operator_precedence(self):
        self.assertEqual(self.interpret("1 + 2 * 3"), 7)
        self.assertEqual(self.interpret("4 * 3 - 2"), 10)
        self.assertEqual(self.interpret("8 / 2 + 3"), 7)
        self.assertEqual(self.interpret("10 - 4 / 2"), 8)

    def test_parentheses(self):
        self.assertEqual(self.interpret("(1 + 2) * 3"), 9)
        self.assertEqual(self.interpret("4 * (3 - 2)"), 4)
        self.assertEqual(self.interpret("(8 / 2) + 3"), 7)
        self.assertEqual(self.interpret("10 - (4 / 2)"), 8)
        self.assertEqual(self.interpret("((1 + 2) * 3) - 4"), 5)

    def test_mixed_operations_with_parentheses(self):
        self.assertEqual(self.interpret("1 + (2 * (3 + 4))"), 15)
        self.assertEqual(self.interpret("(1 + 2) * (3 + 4)"), 21)
        self.assertEqual(self.interpret("(10 - 3) * (2 + 2) / 4"), 7)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.interpret("4 / 0")

    def test_whitespace_handling(self):
        self.assertEqual(self.interpret(" 1 + 2 "), 3)
        self.assertEqual(self.interpret("  4 - ( 3 + 2 ) * 2 "), -6)

    def test_large_numbers_and_multiple_operations(self):
        self.assertEqual(self.interpret("1000 + 2000 * 3000"), 6001000)
        self.assertEqual(self.interpret("1000000 / (2 + 3)"), 200000)

    def test_nested_parentheses(self):
        self.assertEqual(self.interpret("((2 + 3) * (4 + 5)) / (1 + 1)"), 22.5)
        self.assertEqual(self.interpret("(((1 + 2) * 3) + 4) / 2"), 6.5)

    def test_complex_expressions(self):
        self.assertEqual(self.interpret("3 + 4 * 2 / (1 - 5) * 2"), -1)

    def test_invalid_expressions(self):
        with self.assertRaises(Exception):
            self.interpret("2 +")

        with self.assertRaises(Exception):
            self.interpret("4 * (3 - ")

    def test_zero_multiplication_and_addition_of_zero(self):
        self.assertEqual(self.interpret("0 * (5 + 2)"), 0)
        self.assertEqual(self.interpret("0 + 5"), 5)


if __name__ == '__main__':
    unittest.main()
