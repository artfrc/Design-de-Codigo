from test_interface import TestInterface

class BloodTest(TestInterface):
   def approver(self):
      print("Blood test approved!")
      
   def verify_conditions_test(self):
      print('Checking conditions...')