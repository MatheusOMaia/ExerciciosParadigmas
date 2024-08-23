#Faça um programa em Python que receba do usuario
#um vetor com 10 posições. Em seguida devera ser
#impresso o maior e o menor elemento do vetor. + Soma de todos
#elementos vetor.
from Funcs import encMaior,encMenor

def main():


    # Inicializar o vetor zerado.
    vetor = [0] * 10

    #fazer a leitura e preenchimento dos elementos do vetor.
    for i in range(10):
        vetor.append(int(input("Digite o elemento %d: "% i)))

    # Inicializando as variáveis Maior e Menor.
    maior = vetor[0]
    menor = vetor[0]

    # fazer o laço para armazenar os conteudos dos

    # Elementos nas variáveis maior e menor.
    maior = encMaior(vetor)
    menor = encMenor(vetor)

    #Exibir o resultado Final das variáveis Maior e Menor.
    print("O maior elemento do vetor é %d." % maior)
    print("O menor elemento do vetor é %d." % menor)

if __name__ == "__main__":
    main()
