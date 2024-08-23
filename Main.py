#lê um vetor de 8 posições e, em seguida, lê dois valores X e Y
#quaisquer correspondentes a duas posições no vetor.
#O programa então imprime a soma dos valores encontrados nas
# respectivas pisições X e Y.


def main():
    from Funcs import soma

    #Declara um vetor de 8 posições
    vetor = [0] * 8

    #lê os valores do vetor
    for i in range(8):
        vetor[i] = int(input("Digite o valor da posição {}: ".format(i)))

    #lê os valores X e Y
    x = int(input("Digite o valor de X: "))
    y = int(input("Digite o valor de Y: "))

    # Calcula a soma dos valores nas posições X e Y
    soma= soma(vetor[x],vetor[y])
    #soma = vetor[x] + vetor[y]

    # Imprime a soma
    print("A soma dos valores nas posições X e Y é {}.".format(soma))

# Exibir a soma dos elementos do Vetor com suas características principais.
if __name__ == "__main__":
    main()
