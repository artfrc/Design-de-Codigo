from typing import Dict

from pytest import raises
from src.calculators.calculator_1 import Calculator_1

class MockRequest:
   def __init__(self, body: Dict):
      self.json = body
      

def test_calculate():
   mock_request = MockRequest(body={ "number": 19 })
   
   calcultor_1 = Calculator_1()
   response = calcultor_1.calculate(mock_request)
   
   assert "data" in response
   assert "Calculator" in response["data"]
   assert "Result" in response["data"]
   assert response["data"]["Result"] == 141.2792
   
def test_calculate_with_body_error():
   mock_request = MockRequest(body={"something": 1})
   calculator_1 = Calculator_1()
   
   with raises(Exception) as exinfo:
      calculator_1.calculate(mock_request)
      
      assert str(exinfo.value) == "Invalid body."
   
   