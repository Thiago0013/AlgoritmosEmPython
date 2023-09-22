'''30) [DESAFIO] Refaça o algoritmo 25, acrescentando o recurso de mostrar que tipo
de triângulo será formado:
 - EQUILÁTERO: todos os lados iguais
 - ISÓSCELES: dois lados iguais
 - ESCALENO: todos os lados diferentes'''
a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))
if a + b > c and a + c > b and c + b > a:
    if a == b and a == c and b == c:
        print(f'Forma um triangulo do tipo EQUILÁTERO')
    elif a == b:
        print(f'Forma um triangulo do tipo ISÓSCELES')
    elif a != b and a != c and b != c:
        print(f'Forma um triangulo do tipo ESCALENO')

else:
    print(f'Não formar um triangulo!')