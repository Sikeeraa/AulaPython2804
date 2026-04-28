
titulo = 'Listas'
print(f'{titulo:^30}')
minhaLista=['café', 'água', 'açúcar', 'café', 'canela']
print(minhaLista)

# 0         1        2        3         4
# 'café', 'água', 'açúcar', 'café', 'canela'
print(f'primeiro elemento:{minhaLista[0]}')
print(f'segundo elemento:{minhaLista[1]}')
print(f'tamanho da lista:{len(minhaLista)}')
print(f'ultimo elemento:{minhaLista[4]}')
print(f'ultimo elemento:{minhaLista[len(minhaLista)-1]}')

# tentando acessar um indice que não existe
# print(f'ultimo elemento:{minhaLista[5]}')

# como acrescentar itens nome lista?
# o metodo append faz isso
print('\n')
print(minhaLista)
minhaLista.append('chantilly')
minhaLista.append('especiarias')
print(minhaLista)

# e para remover itens da lista
# usamos o metodo pop
minhaLista.pop()
print(minhaLista)
minhaLista.pop()
print(minhaLista)
# MAS EU POSSO REMOVER UM ITEM ESPECIFICO COM O POP
# BASTA PASSAR O INDICE
# removendo o acucar
minhaLista.pop()
print(minhaLista)

# TODO ELEMENTO ITERAVEL podemos percorrer atraves do FOR
for item in range(len(minhaLista)):
    print(minhaLista[i])
