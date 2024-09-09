lista_nomes = []
dicionario = {}

for n in range(0, 2):
    nome = input('Digite um nome: ')
    dicionario['nome'] = nome
    lista_nomes.append(dicionario.copy())
    dicionario.clear()

print(lista_nomes[0].items())