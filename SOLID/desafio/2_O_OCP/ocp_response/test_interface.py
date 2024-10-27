from abc import ABC, abstractmethod

class TestInterface(ABC):
   @abstractmethod
   def approver(message: str):
      pass
   
   def verify_conditions_test():
      pass