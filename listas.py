lista = ["metal","rock","blues"]
print(lista)

#indices inicio sempre 0
print(lista[1])

#lacos
for item in lista:
    print(item)

#tamanho da lista   
tamanho  = len(lista)
print(tamanho)

# adicionar itens a lista
lista.append("samba")
print(lista)

# verificar se o item esta na na lista

if "samba" in lista:
    print ("existe")

# remover itens da lista /  apagar lista inteira [:]
del lista [0]  
print(lista)

# criar lista em branco
lista2 =[]

