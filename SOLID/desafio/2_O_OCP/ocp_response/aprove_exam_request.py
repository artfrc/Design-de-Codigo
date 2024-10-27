from test_x_ray import Test_X_Ray
from blood_test import BloodTest

class ApproveExamRequest:
   def approver(self, exam: any):
      exam.approver()
      
   def verify_conditions(self, exam: any):
      exam.verify_conditions_test()
      
approver = ApproveExamRequest()
blood = BloodTest()
approver.verify_conditions(blood)
approver.approver(blood)

print()

ray = Test_X_Ray()
approver.verify_conditions(ray)
approver.approver(ray)