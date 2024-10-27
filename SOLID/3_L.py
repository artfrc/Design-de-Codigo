class Animal:
   def eat(self):
      print('Animal eating')
      
   def wal(self):
      print('Animal walking')
      
class Feline(Animal):
   def lick(self):
      print('Feline licking')
      
   # def eat(self):
   #    print('Feline eating') essa função n deve existir, queremos algo bem genérico para usar como herança sem modificações.