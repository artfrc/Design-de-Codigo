from test_interface import TestInterface

class Test_X_Ray(TestInterface):
   def approver(self):
      print("X-ray approved!")
      
   def verify_conditions_test(self):
      print('Checking conditions...')