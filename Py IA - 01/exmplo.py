# import json

# def criar_arquivo_json():
#     usuarios = [
#         {"nome": "João", "idade": 25},
#         {"nome": "Maria", "idade": 30}
#     ]
#     with open("usuarios.json", "w") as arquivo:
#         json.dump(usuarios, arquivo, indent=4)
#     print("Arquivo JSON criado com sucesso!")

# def adicionar_usuario():
    
#     try:
#         with open("usuarios.json", "r") as arquivo:
#             usuarios = json.load(arquivo)
        
#         nome = input("Digite o nome do usuário: ")
#         idade = int(input("Digite a idade do usuário: "))
#         novo_usuario = {"nome": nome, "idade": idade}

#         usuarios.append(novo_usuario)

#         with open("usuarios.json", "w") as arquivo:
#             json.dump(usuarios, arquivo, indent=4)
#         print("Usuário adicionado com sucesso!")
#     except FileNotFoundError:
#         print("Arquivo não encontrado. Crie o arquivo primeiro.")
#     except ValueError:
#         print("Por favor, insira uma idade válida.")

# def exibir_usuarios():
#     try:
#         with open("usuarios.json", "r") as arquivo:
#             usuarios = json.load(arquivo)

#         print("Usuários registrados:")
#         for usuario in usuarios:
#             print(f"Nome: {usuario['nome']}, Idade: {usuario['idade']}")
#     except FileNotFoundError:
#         print("Arquivo não encontrado. Crie o arquivo primeiro.")

# print("Bem-vindo ao Gerenciador de Usuários JSON!")
# while True:
#     print("\nEscolha uma opção:")
#     print("1. Criar arquivo JSON")
#     print("2. Adicionar usuário")
#     print("3. Exibir usuários")
#     print("4. Sair")

#     opcao = input("Digite sua escolha: ")

#     if opcao == "1":
#         criar_arquivo_json()
#     elif opcao == "2":
#         adicionar_usuario()
#     elif opcao == "3":
#         exibir_usuarios()
#     elif opcao == "4":
#         print("Saindo... Até mais!")
#         break
#     else:
#         print("Opção inválida. Tente novamente.")


#################################################################



import json

def criar_arquivo_json():
    try:
        usuarios = [
            {"nome": "Joao", "idade": 25},
            {"nome": "Maria", "idade": 30}
        ]
        with open("usuarios.json", "w") as arquivo:
            json.dump(usuarios, arquivo, indent=4)
        print("Arquivo JSON criado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao criar o arquivo JSON: {e}")

def adicionar_usuario():
    try:
        # Tenta abrir o arquivo
        with open("usuarios.json", "r") as arquivo:
            usuarios = json.load(arquivo)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Arquivo não encontrado ou vazio. Crie o arquivo primeiro (opção 1).")
        return

    # Solicita as informações do novo usuário
    nome = input("Digite o nome do usuário: ").strip()
    if not nome:
        print("O nome não pode ser vazio.")
        return

    try:
        idade = int(input("Digite a idade do usuário: "))
        if idade <= 0:
            print("A idade deve ser maior que zero.")
            return
    except ValueError:
        print("Por favor, insira uma idade válida.")
        return

    # Adiciona o novo usuário
    novo_usuario = {"nome": nome, "idade": idade}
    usuarios.append(novo_usuario)

    # Salva os dados atualizados no arquivo
    try:
        with open("usuarios.json", "w") as arquivo:
            json.dump(usuarios, arquivo, indent=4)
        print("Usuário adicionado com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro ao salvar os dados: {e}")

def exibir_usuarios():
    try:
        with open("usuarios.json", "r") as arquivo:
            usuarios = json.load(arquivo)

        if not usuarios:
            print("Nenhum usuário registrado.")
            return

        print("\nUsuários registrados:")
        for usuario in usuarios:
            print(f"Nome: {usuario['nome']}, Idade: {usuario['idade']}")
    except FileNotFoundError:
        print("Arquivo não encontrado. Crie o arquivo primeiro (opção 1).")
    except json.JSONDecodeError:
        print("O arquivo está vazio ou corrompido. Crie um novo arquivo (opção 1).")

# Menu principal
def main():
    print("Bem-vindo ao Gerenciador de Usuários JSON!")
    while True:
        print("\nEscolha uma opção:")
        print("1. Criar arquivo JSON")
        print("2. Adicionar usuário")
        print("3. Exibir usuários")
        print("4. Sair")

        opcao = input("Digite sua escolha: ").strip()

        if opcao == "1":
            criar_arquivo_json()
        elif opcao == "2":
            adicionar_usuario()
        elif opcao == "3":
            exibir_usuarios()
        elif opcao == "4":
            print("Saindo... Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
