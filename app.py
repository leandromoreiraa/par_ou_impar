numero = input('Digite um numero inteiro: ')

if numero.isdigit():
   numero = int(numero)

   if numero % 2 == 0:
       print('Par')
   else:
       print('Ímpar')
else:
    print('Valor Digitado não é um número inteiro.')