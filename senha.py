
import random
import string

#
def password(len=8):
    ascii=string.ascii_letters
    number=string.digits
    opcao=ascii+number

    pass_user=""

  
    for i in range(0,len):
      dig=random.choice(opcao)  
      pass_user=pass_user+dig

    return pass_user

choice_user=input("Senha de quantos digitos:")   
if choice_user.isdigit():
    choice_user=int(choice_user) 
else:
    print("Entrada inválida")  
    quit()
response=password(len=choice_user) 
print(f'senha gerada: {response}')         

