from src.calculators.calculator_2 import Calculator_2
from src.main.drivers.numpy_handler import NumpyHandler

def Calculator_2_factory():
   calc_2 = Calculator_2(NumpyHandler())
   return calc_2
