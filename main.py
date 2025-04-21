import os

# Função para cadastrar uma nova carta e salvar em arquivo .txt
def cadastrar_carta():
    print("\n===== Cadastro de Cartas =====")
    nome = input("Nome da carta: ").strip()
    tipo = input("Tipo: ").strip()
    ataque = input("Ataque: ").strip()
    defesa = input("Defesa: ").strip()
    descricao = input("Descrição: ").strip()

    conteudo = f"""
    Nome: {nome}
    Tipo: {tipo}
    Ataque: {ataque}
    Defesa: {defesa}
    Descrição: {descricao}
    """

    nome_arquivo = f"{nome}.txt"
    nome_arquivo = "".join(c for c in nome_arquivo if c.isalnum() or c in (' ', '-', '_')).rstrip()

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo.strip())

    print(f"\n[Carta salva como {nome_arquivo}]\n")

# Função que lista todos os arquivos .txt no diretório atual.
def listar_cartas():
    print("\n=== Cartas Cadastradas ===")
    for arquivo in os.listdir():
        if arquivo.endswith(".txt"):
            print(f"- {arquivo}")
    print()

# Função principal de menu interativo.
# Exibe as opções disponíveis e chama a função correspondente com base na escolha do usuário.
def menu():
    while True:
        print("=== Menu ===")
        print("1. Cadastrar nova carta")
        print("2. Listar cartas")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_carta()
        elif opcao == "2":
            listar_cartas()
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida.\n")

# Este bloco garante que o menu só será executado se o arquivo for rodado diretamente.
# Se o script for importado em outro projeto, o menu não será executado automaticamente.
if __name__ == "__main__":
    menu()
