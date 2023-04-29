dados = []

with open("entrada.txt", "r") as arquivo:
    for linha in arquivo:
        linha = linha.strip().split()
        dados.append(linha)

print(dados)

print(" ")

dados_reverso = dados[::-1]

print(dados_reverso)



with open("TabelaInvertida.txt", "w") as arquivo:
    for linha in dados_reverso:
        arquivo.write("\t".join(linha) + "\n")