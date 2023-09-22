'''16) [DESAFIO] Escreva um programa para calcular a redução do tempo de vida de um
fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele
já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. Calcule
quantos dias de vida um fumante perderá e exiba o total em dias.'''
cigarrosPdia = int(input('Qual a quantidade de cigarros fumados por dias: '))
TempoCirgarro = cigarrosPdia * 10
VidaDia = TempoCirgarro / 1440
print(f'Você perdeu {VidaDia} dias de vida')
