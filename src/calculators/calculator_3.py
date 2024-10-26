from flask import request as FlaskRequest
from typing import Dict, List
from src.main.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator_3:
   """
   - N números são enviados
   - Retornar a média desses números
   """
   def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
      body = request.json
      list_numbers = self.__validate(body)
      process = self.__process(list_numbers)
      
      return self.__format_result(process)
   
   def __validate(self, body: List[float]) -> List[float]:
      if "numbers" not in body:
         raise HttpUnprocessableEntityError("Invalid body.")
      
      return body["numbers"]
   
   def __process(self,numbers: List[float]) -> float:      
      return sum(numbers) / len(numbers)
   
   def __format_result(self, calc_result: float) -> Dict:
      return {
         "data": {
            "Calculator": 3,
            "Result": round(calc_result, 4)
         }
      }