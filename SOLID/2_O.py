# bad example
# class Company:
#    def do_work(self, work: int):
#       if work == 1:
#          print('Prorammer creating code.')
#       if work == 2:
#          print('Seller selling the product.')
#       else:
#          print('Error.')
                 
class Company:
   def do_work(self, worker: any):
         worker.make()
         
class Programmer:
   def make(self):
      print('Prorammer creating code.')
      
class Seller:
   def make(self):
      print('Seller selling the product.')
      
programmer = Programmer()
seller = Seller()
company = Company()
company.do_work(programmer)
company.do_work(seller)
      