#bad example
from abc import ABC, abstractmethod

# class Document(ABC):
#    @abstractmethod
#    def load(self):
#       pass
   
#    @abstractmethod
#    def view(self):
#       pass

#    @abstractmethod
#    def format(self):
#       pass
   
# class Pdf(Document):
#    def load(self):
#       print('Load pdf.')

#    def view(self):
#       print('View pdf.')
      
#    def format(self):
#       print('Format pdf.')  Um pdf não quer essa função de formatar.

class DocumentPDF(ABC):
   @abstractmethod
   def load(self):
      pass
   
   @abstractmethod
   def view(self):
      pass
   
class DocumentTXT(ABC):
   @abstractmethod
   def load(self):
      pass
   
   @abstractmethod
   def view(self):
      pass

   @abstractmethod
   def format(self):
      pass
   
