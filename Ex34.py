'''34) O Índice de Massa Corpórea (IMC) é um valor calculado baseado na altura e no
peso de uma pessoa. De acordo com o valor do IMC, podemos classificar o
indivíduo dentro de certas faixas.
 - abaixo de 18.5: Abaixo do peso
 - entre 18.5 e 25: Peso ideal
 - entre 25 e 30: Sobrepeso
 - entre 30 e 40: Obesidade
 - acima de 40: Obesidade mórbida'''
altura = float(input('Digitet sua altura em metros: '))
peso = float(input('Digite seu peso em kg: '))
IMC = peso / (altura ** 2)
if IMC < 18.5:
    print(f'IMC; {IMC:.2f} --> Abaixo do peso!')
elif 18.5 <= IMC < 25:
    print(f'IMC; {IMC:.2f} --> Peso ideal!')
elif 25 <= IMC < 30:
    print(f'IMC; {IMC:.2f} --> Sobrepeso!')
elif 30 <= IMC < 40:
    print(f'IMC; {IMC:.2f} --> Obesidade!')
else:
    print(f'IMC;{IMC:.2f} --> Obesidade mórbida!')