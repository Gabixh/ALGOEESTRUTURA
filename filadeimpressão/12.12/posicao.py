""" UMA LISTA COM 10 VALORES E MOSTRAR A POSIÇÃO ONDE SE ENCONTRA O
MAIOR VALOR (SEM UTILIZAR FUNÇÕES PRONTAS)"""

lista = [2, 4, 6, 7, 10, 12, 18, 20, 22, 24]

maior = lista[0]
maior_posicao = 0

for i in range(1, len(lista)):
    if lista[i] > maior:
      maior = lista[i]
      maior_posicao = i

print(f"O maior valor é {maior} e está na posição {maior_posicao}.")