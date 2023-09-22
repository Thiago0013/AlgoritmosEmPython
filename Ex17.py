'''17) Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse
80Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba
o valor da multa, cobrando R$5 por cada Km acima da velocidade permitida.'''
velocidade = float(input('Qual a velocidade do carro: '))
velocidadeMax = 80
if velocidade > 80:
    ultrapassouMax = velocidade - velocidadeMax
    multa = ultrapassouMax * 5
    print(f'Você foi multado por passar do limite de velocidade... Multa de R${multa:.2f}')
else:
    print(f'Você está dentro da velocidade maxima!')
print(f'Não beba quando for dirigir... Dirija com cuidado!')