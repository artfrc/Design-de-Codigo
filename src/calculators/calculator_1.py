from typing import Dict
from flask import request as FlaskRequest

class Calculator_1:
   
   """
   - Um número é dividido em tres partes iguais.
   
   * A primeira parte é dividida por 4 e seu resultado somado a 7.
   
      - Após, o resultado é elevado ao quadrado e multiplicado por 0.257
      
   * A segunda parte é elevada a potencia de 2.121, dividida por 5 e somada a 1
   
   * Terceira parte mantem o mesmo valor
   
   * Por fim, os três valores são somados e entregue o resultado.
   """
   
   def calculate(self, request: FlaskRequest) -> Dict:  # type: ignore
      body = request.json
      number = self.__validate(body)
      number_splitted_for_three = number / 3
      first_process = self.__first_process(number_splitted_for_three)
      second_process = self.__second_process(first_process)
      result = number + first_process + second_process

      return self.__format_result(result)      
      
   def __validate(self, body: Dict) -> float:
      if "number" not in body:
         raise Exception("Invalid Body.")
      
      number = body["number"]
      
      return number
   
   def __first_process(self, number: float) -> float:
      first = (number / 4) + 7
      second = (first ** 2) * 0.257
      
      return second
   
   def __second_process(self, number: float) -> float:
      return ( (number ** 2.121) / 5 ) + 1
   
   def __format_result(self, calc_result: float) -> Dict:
      return {
         "data": {
            "Calculator": 1,
            "Result": round(calc_result, 4)
         }
      }