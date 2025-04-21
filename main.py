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


def listar_cartas():
    pass

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

if __name__ == "__main__":
    menu()
