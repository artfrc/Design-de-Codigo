# bad example

# file serivce_client
# from notificator_email import NotificatorEmail

# class ServiceClient:
#    def __init__(self, notificator: NotificatorEmail):
#       self.notificator = notificator
      
#    def send(self, message: str):
#       self.notificator.send_notification(message)
      
#  file notificator_email
# class NotificatorEmail:
#    def send_notification(self, message: str):
#       print('Sending email.')
      
#  file notificator_sms
# class NotificatorSms:
#    def send_notification(self, message: str):
#       print('Sending sms.')


# CRIAR UMA INTERFACE PARA SERVICE CLIENT NÃO DEPENDER DE EMAIL OU SMS
from abc import ABC, abstractmethod
class NotificatorInterface(ABC):
   @abstractmethod
   def send_notification(self, message):
      pass
   
class NotificatorSms(NotificatorInterface):
   def send_notification(self, message: str):
      print('Sending sms.')  
      
class NotificatorEmail(NotificatorInterface):
   def send_notification(self, message: str):
      print('Sending email.')
   
   
from notificator_interface import NotificatorInterface

class ServiceClient:
    def __init__(self, notificator: NotificatorInterface):
        self.__notificator = notificator

    def notify(self, message: str):
        self.__notificator.send_notification(message)
