''' Uma empresa precisa reajustar o salário dos seus funcionários, dando um
aumento de acordo com alguns fatores. Faça um programa que leia o salário atual,
o gênero do funcionário e há quantos anos esse funcionário trabalha na empresa.
No final, mostre o seu novo salário, baseado na tabela a seguir:
- Mulheres
- menos de 15 anos de empresa: +5%
- de 15 até 20 anos de empresa: +12%
- mais de 20 anos de empresa: +23%
- Homens
- menos de 20 anos de empresa: +3%
- de 20 até 30 anos de empresa: +13%
- mais de 30 anos de empresa: +25%'''

nome = input('Nome: ')
sexo = input('Sexo [M/F]: ').upper().strip()
tempo = int(input('Quantos anos trabalha na empresa: '))
salario = float(input('Salário: R$'))
aumento_percentual = 0  
if sexo == 'F':
    if tempo < 15:
        aumento_percentual = 0.05
    elif 15 <= tempo < 20:
        aumento_percentual = 0.12
    else:
        aumento_percentual = 0.23
elif sexo == 'M':
    if tempo < 20:
        aumento_percentual = 0.03
    elif 20 <= tempo < 30:
        aumento_percentual = 0.13
    else:
        aumento_percentual = 0.25
else:
    print(f'Valor digitado incorreto! Digite o sexo M(Masculino) ou F(Feminino)...')
    exit()
novo_salario = salario + (aumento_percentual * salario)
print(f'O salário de {nome} teve um aumento de {aumento_percentual * 100}% e passou a ser R${novo_salario:.2f}')
