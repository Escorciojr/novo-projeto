import os
import time
import random
import sys

listas = []
e = 1
os.system('clear')
while True:
    try:
        concurso = int(input("nr dop concurso=> "))
        jogos = int(input("quantos jogos quer fazer=> "))
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
    jogo = ("jogo" + str(e+1))
    listas.append(jogo)
    for i in range(6):
        r = random.randint(1, 60)
        time.sleep(0.01)
        sys.stdout.write(str(r))
        listas.append(r)
        valor = i
        if valor != 5:
            sys.stdout.write("-")
        else:
            print()
            print("##")
            listas.append("##")

print(listas)
w = open("concurso nr"+str(concurso)+".txt", "w")
w.write(str(listas))