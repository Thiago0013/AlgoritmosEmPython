'''20) Desenvolva um programa que leia um número inteiro e mostre se ele é PAR ou
ÍMPAR.'''
numero = int(input('Digite um numero: '))
if numero % 2 == 0:
    print(f'O numero {numero} é par')
else:
    print(f'O numero {numero} é impar')