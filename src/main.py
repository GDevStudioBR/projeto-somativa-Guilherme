import os
import shutil  # para deletar pastas e arquivos

# Caminho da pasta onde as cartas serão salvas
PASTA_CARTAS = "cartas"

# Garante que a pasta "cartas" existe
if not os.path.exists(PASTA_CARTAS):
    os.makedirs(PASTA_CARTAS)

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

    # Limpa o nome do arquivo (sem caracteres inválidos)
    nome_limpo = "".join(c for c in nome if c.isalnum() or c in (' ', '-', '_')).rstrip()
    nome_arquivo = os.path.join(PASTA_CARTAS, f"{nome_limpo}.txt")

    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo.strip())

    print(f"\n[Carta salva como {nome_arquivo}]\n")


# Função para listar todas as cartas salvas
def listar_cartas():
    print("\n=== Cartas Cadastradas ===")
    arquivos = os.listdir(PASTA_CARTAS)
    if not arquivos:
        print("Nenhuma carta encontrada.")
    else:
        for arquivo in arquivos:
            if arquivo.endswith(".txt"):
                print(f"- {arquivo}")
    print()

# Função para apagar todas as cartas
def apagar_todas_as_cartas():
    confirmacao = input("Tem certeza que deseja apagar TODAS as cartas? (s/n): ").lower()
    if confirmacao == "s":
        for arquivo in os.listdir(PASTA_CARTAS):
            caminho_arquivo = os.path.join(PASTA_CARTAS, arquivo)
            if os.path.isfile(caminho_arquivo):
                os.remove(caminho_arquivo)
        print("\n[Cartas apagadas com sucesso!]\n")
    else:
        print("\n[Operação cancelada. Nenhuma carta foi apagada.]\n")

# Função principal de menu interativo.
# Exibe as opções disponíveis e chama a função correspondente com base na escolha do usuário.
def menu():
    while True:
        print("=== Menu ===")
        print("1. Cadastrar nova carta")
        print("2. Listar cartas")
        print("3. Apagar todas as cartas")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_carta()
        elif opcao == "2":
            listar_cartas()
        elif opcao == "3":
            apagar_todas_as_cartas()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida.\n")

# Este bloco garante que o menu só será executado se o arquivo for rodado diretamente.
# Se o script for importado em outro projeto, o menu não será executado automaticamente.
if __name__ == "__main__":
    menu()
