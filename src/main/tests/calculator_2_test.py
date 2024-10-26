from typing import Dict
from src.calculators.calculator_2 import Calculator_2
from src.main.drivers.numpy_handler import NumpyHandler

class MockRequest:
   def __init__(self, body: Dict):
      self.json = body

def test_calculate():
   mock_request = MockRequest({"numbers": [2.12, 7.62, 1.32, 1.11]})   
   calculator_2 = Calculator_2(NumpyHandler())
   response = calculator_2.calculate(mock_request)
   
   assert "data" in response
   assert response == {'data': {'Calculator': 2, 'Result': 0.0433}}