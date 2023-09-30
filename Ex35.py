'''35) Uma empresa de aluguel de carros precisa cobrar pelos seus serviços. O
aluguel de um carro custa R$90 por dia para carro popular e R$150 por dia para
carro de luxo. Além disso, o cliente paga por Km percorrido. Faça um programa
que leia o tipo de carro alugado (popular ou luxo), quantos dias de aluguel e
quantos Km foram percorridos. No final mostre o preço a ser pago de acordo com a
tabela a seguir:
 Carros populares (aluguel de R$90 por dia)
 - Até 100Km percorridos: R$0,20 por Km
 - Acima de 100Km percorridos: R$0,10 por Km
 - Carros de luxo (aluguel de R$150 por dia)
 - Até 200Km percorridos: R$0,30 por Km
 - Acima de 200Km percorridos: R$0,25 por Km'''

carro = input('Qual tipo de carro você deseja pegar? [Popular] e [Luxo]: ').capitalize()
dias = int(input('Quantos dias o carro foi usado: '))
km = float(input('Quantos km foram percorridos: '))
if carro == 'Popular':
    if km <= 100:
        preço = (dias * 90) + (km * 0.20)
    else:
        preço = (dias * 90) + (km * 0.10)
    print(f'O carro Popular fica com alguel de: R${preço:.2f}')
elif carro == 'Luxo':
    if km <= 200:
        preço = (dias * 150) + (km * 0.30)
    else:
        preço = (dias * 150) + (km * 0.25)
    print(f'O carro de Luxo fica com alguel de: R${preço:.2f}')
else:
    print(f'ERRO! Escolha de carro incorreta')