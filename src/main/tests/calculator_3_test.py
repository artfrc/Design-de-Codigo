from typing import Dict

from pytest import raises
from src.calculators.calculator_3 import Calculator_3

class MockRequest:
   def __init__(self, body: Dict):
      self.json = body
      

def test_calculate():
   mock_request = MockRequest(body={ "numbers": [7, 11, 21]})
   
   calcultor_3 = Calculator_3()
   response = calcultor_3.calculate(mock_request)
   
   assert "data" in response
   assert response["data"]== {'Calculator': 3, 'Result': 13.0}
   
def test_calculate_with_body_error():
   mock_request = MockRequest(body={"something": 1})
   calculator_3 = Calculator_3()
   
   with raises(Exception) as exinfo:
      calculator_3.calculate(mock_request)
      
      assert str(exinfo.value) == "Invalid body."
   
   