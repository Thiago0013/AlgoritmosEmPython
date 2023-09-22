'''23) Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos
para todos, mas especialmente para mulheres. Faça um programa que leia nome,
sexo e o valor das compras do cliente e calcule o preço com desconto. Sabendo
que:
 - Homens ganham 5% de desconto
 - Mulheres ganham 13% de desconto'''
nome = input('Nome: ')
sexo = input('Sexo: ').lower().strip()
compra = float(input('Digite o valor das compras: R$'))
if sexo == 'm':
    desconto = (5/100) * compra
    preço_final = compra - desconto  
    print(f'Homens sai com desconto de 13% que fica R${preço_final:.2f}')
elif sexo == 'f':
    desconto = (13/100) * compra
    preço_final = compra - desconto
    print(f'Mulheres saem com desconto de 13% que fica R${preço_final:.2f}')
else:
    print('Sexo não reconhecido. Digite "m" para masculino ou "f" para feminino.')