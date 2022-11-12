vogais = ['a', 'e', 'i', 'o', 'u']
achei = []
word = input("Digite seu Nome")
    for letra in word:
        if letra in vogais:
            if letra not in achei:
            achei.append(letra)
print(achei)
