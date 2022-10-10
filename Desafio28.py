# Jogo de advinhação de um número com base em uma lista.
from random import randint
from time import sleep
n = randint(0, 5)
print('-=-' * 20)
s = int(input('Tente acertar o númrero de 0 a 5 que o computador pensou: '))
print('-=-' * 20)
print('PROCESSANDO...')
sleep(2)
if n == s:
    print('Parabéns, você acertou o número')
else:
    print('Sinto muito, você errou. O número correto é o {}.'.format(n))
print('---fim---')
