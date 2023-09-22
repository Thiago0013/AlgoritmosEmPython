'''29) Desenvolva um programa que leia o nome de um funcionário, seu salário,
quantos anos ele trabalha na empresa e mostre seu novo salário, reajustado de
acordo com a tabela a seguir:
 - Até 3 anos de empresa: aumento de 3%
 - entre 3 e 10 anos: aumento de 12.5%
 - 10 anos ou mais: aumento de 20%'''
nome = input('Nome: ')
salario = float(input('Digite seu salário: '))
anos = int(input('Quantos anos trabalha na empresa: '))
if anos <= 3:
    porcentagem = 3 / 100
    novo_salario = (salario * porcentagem) + salario
elif 3 < anos <= 10:
    porcentagem = 12.5 / 100
    novo_salario = (salario * porcentagem) + salario
else:
    porcentagem = 20 / 100
    novo_salario = (salario * porcentagem) + salario
print(f'{nome} trabalha na empresa por {anos} anos e recebe aumento de {porcentagem * 100:.0f}% que ficara com o salario de: R${novo_salario:.2f} ')
