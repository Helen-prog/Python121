import unittest
from simple_calculator import SimpleCalculator


class AdditionTestSuite(unittest.TestCase):
    def setUp(self):
        """ Executed before every test case """
        self.calculator = SimpleCalculator()

    def test_addition_two_integers(self):
        result = self.calculator.sum(5, 6)
        self.assertEqual(result, 11)

    def test_addition_integer_string(self):
        result = self.calculator.sum(5, "6")
        self.assertEqual(result, "ERROR")

    def test_addition_negative_integers(self):
        result = self.calculator.sum(-5, -6)
        self.assertEqual(result, -11)
        self.assertNotEqual(result, 11)


class SubtractionTestSuite(unittest.TestCase):
    def setUp(self):
        """ Executed before every test case """
        self.calculator = SimpleCalculator()

    def test_substration_two_integers(self):
        result = self.calculator.subtract(6, 5)
        self.assertEqual(result, 1)

    def test_subtraction_integer_string(self):
        result = self.calculator.subtract(5, "6")
        self.assertEqual(result, "ERROR")

    def test_subtraction_negative_integers(self):
        result = self.calculator.subtract(-5, -6)
        self.assertEqual(result, 1)
        self.assertNotEqual(result, -11)

    @unittest.skipIf(a > b, "Skip over this routine")
    def testsub(self):
        """sub"""
        result = self.a - self.b
        self.assertTrue(result == -10)


class MultiplicationTestSuite(unittest.TestCase):
    def setUp(self):
        """ Executed before every test case """
        self.calculator = SimpleCalculator()

    def test_multiplication_two_integers(self):
        result = self.calculator.multiply(6, 5)
        self.assertEqual(result, 30)

    def test_multiplication_integer_string(self):
        result = self.calculator.subtract(5, "6")
        self.assertEqual(result, "ERROR")

    def test_multiplication_negative_integers(self):
        result = self.calculator.multiply(-5, -6)
        self.assertEqual(result, 30)
        self.assertNotEqual(result, -30)


class DivisionTestSuite(unittest.TestCase):
    def setUp(self):
        """ Executed before every test case """
        self.calculator = SimpleCalculator()

    def test_division_two_integers(self):
        result = self.calculator.divide(30, 5)
        self.assertEqual(result, 6)

    def test_division_integer_string(self):
        result = self.calculator.divide(5, "6")
        self.assertEqual(result, "ERROR")

    def test_division_negative_integers(self):
        result = self.calculator.divide(-30, -6)
        self.assertEqual(result, 5)
        self.assertNotEqual(result, -5)

    def test_divide_by_zero_exception(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(10, 0)


# Выполнять все тесты при запуске файла
if __name__ == "__main__":
    unittest.main()
