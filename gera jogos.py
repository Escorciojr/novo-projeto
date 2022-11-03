import time
import random
import sys
e = 1
for e in range(e+5):
    print()
    print("jogo" + str(e))
    for i in range(6):
        r = random.randint(1, 60)
        time.sleep(2)
        sys.stdout.write(str(r))
        valor = i
        if valor != 5:
           sys.stdout.write("-")
