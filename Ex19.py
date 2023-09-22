'''19) Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua
média e mostre na tela. No final, analise a média e mostre se o aluno teve ou
não um bom aproveitamento (se ficou acima da média 7.0).'''
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
média = (nota1 + nota2) / 2
if média >= 7:
    print(f'A média do aluno foi {média}, teve um bom aproveitamento e está APROVADO!')
elif 5 <= média < 7:
    print(f'A média do aluno foi {média}, teve um aproveitamento razoavel e está de RECUPERAÇÃO!')
else:
    print(f'A média do aluno foi {média}, não teve um bom aproveitamento e está REPROVADO!')