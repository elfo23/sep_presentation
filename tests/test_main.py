import unittest
from src.calculator import calculator as calc

class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calculator = calc.Calculator()

    def test_add(self):
        result = self.calculator.add(5, 3)
        self.assertEqual(result, 8)
        result = self.calculator.add(-1, 1)
        self.assertEqual(result, 0)
        result = self.calculator.add(0, 0)
        self.assertEqual(result, 0)

    def test_subtract(self):
        result = self.calculator.subtract(5, 3)
        self.assertEqual(result, 2)
        result = self.calculator.subtract(-1, 1)
        self.assertEqual(result, -2)
        result = self.calculator.subtract(0, 0)
        self.assertEqual(result, 0)

    def test_multiply(self):
        result = self.calculator.multiply(5, 3)
        self.assertEqual(result, 15)
        result = self.calculator.multiply(-1, 1)
        self.assertEqual(result, -1)
        result = self.calculator.multiply(0, 5)
        self.assertEqual(result, 0)

    def test_divide(self):
        result = self.calculator.divide(8, 4)
        self.assertEqual(result, 2)
        result = self.calculator.divide(-10, 5)
        self.assertEqual(result, -2)
        result = self.calculator.divide(7, 2)
        self.assertEqual(result, 3.5)
        with self.assertRaises(ValueError):
            self.calculator.divide(5, 0)

if __name__ == '__main__':
    unittest.main()
