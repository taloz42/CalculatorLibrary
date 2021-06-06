"""
Unit tests for the calculator library
"""

import calculator
import numpy as np


class TestCalculator:
    # def test_something(self):
    #     self.assertEqual(True, False)

    def test_addition_positives(self):
        assert 4 == calculator.add(2, 2)

    def test_random(self):
        rand_num = np.random.randint(0,2)
        assert 1 == rand_num

    def test_addition_negatives(self):
        assert -4 == calculator.add(-2, -2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)
