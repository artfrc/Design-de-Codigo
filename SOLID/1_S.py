# bad example
# def  handle():
#    print('Banco de dados acesso...')
#    print('Verifica existencia do usuário...')
#    print('Cadastro do usuáirio...')

# good
def handle():
   bd_access()
   get_user()
   add_user()

def bd_access():
   print('Base date accessed...')

def get_user():   
   print('Checks for user existence...')
   
def add_user():
   print('User registration...')
   

   