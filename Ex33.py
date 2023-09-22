'''33) Escreva um programa para aprovar ou não o empréstimo bancário para a compra
de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e
em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que
ela não pode exceder 30% do salário ou então o empréstimo será negado.'''
valorCasa = float(input('Digite o valor da casa: R$'))
salario = float(input('Seu salário: R$'))
anos = int(input('Quantos anos vai pagar: '))
exceder = (salario*(30/100)) + salario
prestação = valorCasa / (anos * 12)
print(exceder, prestação)
if prestação <= exceder:
    print(f'O valor mensal será de R${prestação:.2f} por mês sem exceder os 30%, no entando o empréstimo foi aprovado!')
else:
    print(f'O valor mensal de R${prestação:.2f} por mês, passou dos 30%, no entando o empréstimo foi negado!')