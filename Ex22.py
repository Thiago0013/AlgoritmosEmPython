'''22) Escreva um programa que leia o ano de nascimento de um rapaz e mostre a sua
situação em relação ao alistamento militar.
 - Se estiver antes dos 18 anos, mostre em quantos anos faltam para o
alistamento.
 - Se já tiver depois dos 18 anos, mostre quantos anos já se passaram do
alistamento.'''
import datetime
ano_atual = datetime.datetime.now().year
nascimento = int(input('Digite seu ano de nascimento: '))
idade = ano_atual - nascimento
if idade < 18:
    print(f'Você tem {idade} de idade, falta {18 - idade} anos para o alistamento!')
else:
    print(f'Você tem {idade} de idade, você tem idade para o alistamento...', end=' ')
    print(f'Já se passou {idade - 18} anos'if idade != 18 else 'Faça o alistamento!') 