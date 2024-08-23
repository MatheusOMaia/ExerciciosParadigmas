

def soma(x, y):
    soma = x+y
    return soma

def encMaior(vetor):
    maior = vetor[0]
    for i in range(1, len(vetor)):
        if vetor[i] > maior:
            maior = vetor[i]
    return maior
def encMenor(vetor):
    menor = vetor[0]
    for i in range(1, len(vetor)):
        if vetor[i] < menor:
            menor = vetor[i]

    return menor


