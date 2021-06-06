"""
Unit tests for the calculator library
"""

import unittest
import calculator

# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)
#
#     def test_addition_positives(self):
#         assert 4 == calculator.add(2, 2)
#
#     def test_addition_negatives(self):
#         assert 4 == calculator.add(-2, -2)
#
#     def test_subtraction(self):
#         assert 2 == calculator.subtract(4, 2)
#
# if __name__ == '__main__':
#     unittest.main()


class TestCalculator:
    # def test_something(self):
    #     self.assertEqual(True, False)

    def test_addition_positives(self):
        assert 4 == calculator.add(2, 2)

    def test_addition_negatives(self):
        assert 4 == calculator.add(-2, -2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)
