'''32) [DESAFIO] Crie um jogo onde o computador vai sortear um número entre 1 e 5 o
jogador vai tentar descobrir qual foi o valor sorteado'''
import random
maquina = random.randint(1,5)
tentativas = 0
while True:
    jogador = int(input('Digite um numero entre 1 a 5: '))
    if jogador == maquina:
        print(f'Você acertou! com {tentativas} tentativas!')
        break
    elif jogador < maquina:
        tentativas += 1
        print(f'Você errou! Tente chutar um numero maior...')
    else:
        tentativas += 1
        print(f'Você errou! Tente chutar um numero menor...')
print(f'Até a próxima!')