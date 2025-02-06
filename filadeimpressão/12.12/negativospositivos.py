"""VAMOS FAZER UM PROGRAMA QUE LEIA 10 NUMEROS REAIS E OS ARMAZENE EM UMA
LISTA. CALCULE E MOSTRE A QUANTIDADE DE NUMEROS NEGATIVOS E A SOMA DOS NUMEROS POSITIVOS."""

#CRIANDO UM VETOR

numero = []

#CRIANDO UMA ESTRUTURA DO TIPO PARA QUE VAI RECEBER 5 ELEMENTOS, SE QUISESSE QUE RECEBESSE MAIS ELEMENTOS É SO TROCAR

for i in range(10):
    notaunitaria = float(input("DIGITE A NOTA DO ALUNO: "))
    numero.append(notaunitaria)
    
quantidade_negativos = 0
soma_positivos = 0

#PARA PASSAR DENTRO DE TODOS OS ITENS DO VETOR USAMOS:

for numerounitario in numero:
    if numerounitario <0:
        quantidade_negativos += 1 
    if numerounitario > 0:
        soma_positivos += numerounitario

print(f"Quantidde de números negativos é: {quantidade_negativos}, e a soma dos positivos é: {soma_positivos}")