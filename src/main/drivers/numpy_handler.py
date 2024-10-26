from typing import List
import numpy
from src.main.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class NumpyHandler(DriverHandlerInterface):
   def __init__(self):
      self.__np = numpy
   
   def standard_deviation(self, numbers: List[float]) -> float:
      return float( self.__np.std(numbers) )