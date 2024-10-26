from typing import Dict, List
from flask import request as FlaskRequest
from src.main.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from src.main.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class Calculator_2:
   """
   - N números são enviados
   - Todos os N números são multiplicados por 11 e elevados à potência de 0.95
   - Por fim, é retirado o desvio padrão desses resultados e retornado o inverso desses valores (1/result)
   """
   def __init__(self, driver_handler: DriverHandlerInterface):
      self.__driver_handler = driver_handler
   
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
      first_part =  [(num * 11) ** 0.95 for num in numbers]
      response = self.__driver_handler.standard_deviation(first_part)
      
      return 1 / response
   
   def __format_result(self, calc_result: float) -> Dict:
      return {
         "data": {
            "Calculator": 2,
            "Result": round(calc_result, 4)
         }
      }