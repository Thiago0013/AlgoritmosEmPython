'''15) Crie um programa que leia o número de dias trabalhados em um mês e mostre o
salário de um funcionário, sabendo que ele trabalha 8 horas por dia e ganha R$25
por hora trabalhada.'''
dias_trabalhado = int(input('Dias trabalhado em um mês: '))
salario = dias_trabalhado * 8 * 25
print(f'O salario por horas trabalhado é de R${salario:.2f}')