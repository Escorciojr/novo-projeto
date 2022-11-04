import os
import time
import random
import sys

e = 1
os.system('clear')
while True:
    try:
        jogos = int(input("quantos jogos quer fazer=>"))
        break
    except:
        print('\a')
        print("!!!apenas numeros por favor !!")
        print()
        time.sleep(1)
        os.system('clear')

for e in range(e+jogos-1):
    print()
    print("jogo" + str(e+1))
    for i in range(6):
        r = random.randint(1, 60)
        time.sleep(0.01)
        sys.stdout.write(str(r))
        valor = i
        if valor != 5:
            sys.stdout.write("-")
        else:
            print()
            print("fim de jogatina")
