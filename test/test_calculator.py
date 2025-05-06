# each test we wreite can have 1 or more test methods
# unittest is part of standard library
# subclass unittest.TestCase
# will recognise tests starting with test_
# assertion methods: assertisinstance, assertisequal, assertTrue. 
# validation of output = expected value.
# python -m unittest file_name
'''
    module docstring
'''
import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_calculator_class_exists(self):
        calc = Calculator()
        self.assertIsInstance(calc, Calculator)

    def test_add_method_exists(self):
        calc = Calculator()
        self.assertTrue(callable(getattr(calc, "add", None)))

    def test_add_method_takes_two_inputs(self):
        calc = Calculator()
        self.assertEqual(calc.add(0, 0), 0)

    def test_add_method_input_validation(self):
        calc = Calculator()
        with self.assertRaisesRegex(TypeError, "Custom Error: input should be numeric"):
            calc.add("a", 5)

    def test_add_method_additition(self):
        calc = Calculator()
        self.assertEqual(calc.add(2, 3), 5)
        self.assertEqual(calc.add(-1, -1), -2)
        self.assertEqual(calc.add(0, 0), 0)
        self.assertEqual(calc.add(200, 300), 500)

