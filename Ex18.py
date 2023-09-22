'''18) Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade
dela e depois mostre se ela pode ou não votar'''
import datetime
ano_atual = datetime.datetime.now().year
ano_de_nascimento = int(input('Qual ano você nasceu: '))
idade = ano_atual - ano_de_nascimento  
if idade < 16:
    print(f'Tem {idade} anos e o voto: NÃO PODE VOTAR')
elif idade < 18 or idade > 70:
    print(f'Tem {idade} anos e o voto: NÃO É OBRIGATÓRIO')
else:
    print(f'Tem {idade} anos e o voto: OBRIGATÓRIO')