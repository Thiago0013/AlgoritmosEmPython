'''28) Faça um programa que leia a largura e o comprimento de um terreno
retangular, calculando e mostrando a sua área em m². O programa também
devemostrar a classificação desse terreno, de acordo com a lista abaixo:
 - Abaixo de 100m² = TERRENO POPULAR
 - Entre 100m² e 500m² = TERRENO MASTER
 - Acima de 500m² = TERRENO VIP'''
largura = float(input('Digite a largura do terreno: '))
comprimento = float(input('Digite o comprimento do terreno: '))
area = largura * comprimento
if area < 100:
    print(f'O terreno tem {area}m² e é um terrono popular!')
elif 100 <= area < 500:
    print(f'O terreno tem {area}m² e é um terreno master!')
else:
    print(f'O terreno tem {area}m² e é um terreno vip!')
    