#abre arquivo
arquivo = open ("arquivo.txt")
# le linhas do arquivo
linhas =  arquivo.readlines()
print(linhas)
#le arquivo completo
texto_completo =  arquivo.read()
print(texto_completo)
#cria arquivo
w = open("arquivo2.txt", "w")
#gravar dados no arquivo
w.write("este meu arquivo")
# fechar arquivos
w.close()
arquivo.close()

# abre arquivo e quebra lina /n
w = open("arquivo2.txt", "a")
w.write("este é meu arquivo de novo\n")
w.close()


