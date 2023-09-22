'''27) Crie um programa que leia duas notas de um aluno e calcule a sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
 - Média até 4.9: REPROVADO
 - Média entre 5.0 e 6.9: RECUPERAÇÃO
 - Média 7.0 ou superior: APROVADO'''
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7:
    print(f'A média foi {media} e o aluno foi APROVADO!')
elif 5 <= media < 7:
    print(f'A media foi {media} e o aluno está na RECUPERAÇÃO!')
elif media < 5:
    print(f'A media foi {media} e o aluno foi REPROVADO!')