produto = float(input('Digite o valor do produto: R$'))
desconto = produto * 0.05
print(f'O produto com desconto de 5% foi R${desconto:.2f} que ficou com {produto - desconto:.2f}')