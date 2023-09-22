'''24) Faça um algoritmo que pergunte a distância que um passageiro deseja
percorrer em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para
viagens até 200Km e R$0.45 para viagens mais longas.'''
km = float(input('digite a distancia que deseja percorrer: '))
if km <= 200:
    preço = km * 0.50
else:
    preço = km * 0.45
print(f'O preço da passagem é de {preço}')