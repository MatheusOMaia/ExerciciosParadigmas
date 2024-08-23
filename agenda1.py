# Coleta Dados do Usuário: Recebe uma lista de nomes, idades e telefones.
# Armazena Dados em um Dicionário: Usa um dicionário para associar
# cada nome à sua idade.


def coletar_dados():

    #Coleta nomes e idades do usuário e os armazena em uma lista de dicionários.

    dados = []
    while True:
        nome = input("Digite o nome (ou 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break
        idade = input("Digite a idade: ")
        try:
            idade = int(idade)
        except ValueError:
            print("Idade deve ser um número inteiro. Tente novamente.")
            continue
        telefone = input("Digite o telefone: ")

        dados.append({'nome' : nome, 'idade': idade,'telefone' : telefone})
    return dados

def salvar_em_arquivos(dados, nome_arquivo):
    #Salva a lista de dicionários em um arquivo de texto.

    with open(nome_arquivo, 'w') as arquivo:
        for item in dados:
            linha = f"Nome: {item['nome']}, Idade: {item['idade']}, Telefone: {item['telefone']}\n"
            arquivo.write(linha)

def main():
    #Função principal que coordena o fluxo do programa.

    dados = coletar_dados()
    if dados:
        salvar_em_arquivos(dados, 'dados_pessoais.txt')
        print("Dados salvos no arquivo 'dados_pessoais.txt'.")
        salvar_em_arquivos(dados,'dados_pessoais.csv')
        print("Dados salvos no arquivo 'dadis_pessoais.csv")
        salvar_em_arquivos(dados, 'dados_pessoais.json')
        print("Dados salvos no arquivo 'dados_pessoais.json'.")
    else:
        print("Nenhum dado foi coletado.")
if __name__ == "__main__":
    