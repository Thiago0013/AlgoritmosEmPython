
km_perco = float(input("Qual a quantidade de km percorridos: "))
dias_usado = int(input('Quantos dias ele foi alugado: '))
km = 0.20
dia = 90
preço = (km_perco * km) + (dias_usado * dia)
print(f'O preço total a pagar é de R${preço:.2f}')
