import pytest
from app.calculator import Calculator


   class TestCalc:
       def setup(self):
           self.calc = calculator

       def test_multiply_calculate(self):
           assert self.calc.multiply(self, 2, 2) == 4

       def test_division_calculate(self):
           assert self.calc.division(self, 6, 3) == 2

       def test_adding_calculate_correctly(self):
           assert self.calc.adding(self, 2, 1) == 3

       def test_subtraction_calculate(self):
           assert self.calc.subtraction(self, 2, 2) == 0
