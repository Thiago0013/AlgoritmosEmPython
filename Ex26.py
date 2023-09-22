'''26) Escreva um algoritmo que leia dois números inteiros e compare-os, mostrando
na tela uma das mensagens abaixo:
 - O primeiro valor é o maior
 - O segundo valor é o maior
 - Não existe valor maior, os dois são iguais'''
valor1 = int(input('Digite um valor inteiro: '))
valor2 = int(input('Digite outro valor inteiro: '))
if valor1 > valor2:
    print(f'{valor1} é maior que o {valor2}')
elif valor2 > valor1:
    print(f'{valor2} é maior que o {valor1}')
elif valor1 == valor2:
    print(f'O valor {valor1} e {valor2} são iguais')