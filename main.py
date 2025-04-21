def cadastrar_carta():
    pass

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
