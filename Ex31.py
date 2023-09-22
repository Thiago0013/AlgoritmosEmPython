import random
jogo = ['Pedra', 'Papel', 'Tesoura']
'''31) [DESAFIO] Crie um jogo de JoKenPo (Pedra-Papel-Tesoura)'''
print(f'[0] Pedra\n[1] Papel\n[2]Tesoura')
player1 = int(input('escolha: '))
maquina = random.randint(0,2)
if player1 < 3:
    if player1 == maquina:
        print(f'A você jogou: "{jogo[player1]}" e a maquina: "{jogo[maquina]}"... EMPATOU!')
    elif player1 == 0 and maquina == 2 or player1 == 1 and maquina == 0 or player1 == 2 and maquina == 1:
        print(f'A você jogou: "{jogo[player1]}" e a maquina: "{jogo[maquina]}"... Você GANHOU!')
    else:
        print(f'A você jogou: "{jogo[player1]}" e a maquina: "{jogo[maquina]}"... Você PERDEU!')
else:
    print(f'Valor digitado incorreto!')
