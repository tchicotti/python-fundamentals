# Crie um TODO LIST com as opções de LISTAR, ADICIONAR, ALTERAR, REMOVER, MARCAR COMO CONCLUIDO, SAIR


lista = []
opcao = None

def adicionar_item():
    # 2 - Adicionar item na lista
    descricao = input("Informe o nome da atividade: ")
    item = {
        "descricao": descricao,
        "situacao": "pendente"
    }
    lista.append(item)
    print(f"O item '{descricao}' foi adicionado com sucesso.")
    mostrar_lista()
    
def mostrar_lista():
    # 1 - Mostrar a lista
    if len(lista) == 0:
        print("Lista Vazia")
    else:
        for posicao, atividade in enumerate(lista, start=1):
            if atividade["situacao"] == "concluido":
                print(f"{posicao} - [x] Atividade: {atividade["descricao"]}")    
            else: 
                print(f"{posicao} - [ ] Atividade: {atividade["descricao"]}") 
                
def alterar_item():
    # 3 - Alterar um item
    posicao = input("Informe a posição que deseja alterar: ")
    posicao = int(posicao)
    nova_descricao = input("Informe o novo texto: ")
    lista[posicao - 1]["descricao"] = nova_descricao
    print(f"O item na posição '{posicao}' foi alterado com sucesso.")

def marcar_concluido():
    # 5 - Marcar como concluído
    posicao = input("Informe a posição que deseja concluir: ")
    posicao = int(posicao)
    lista[posicao - 1]["situacao"] = "concluido"
    print(f"O item na posição '{posicao}' foi concluído.")

def remover_item():
    # 4 - Remover um item
    posicao = input("Informe a posição que deseja remover: ")
    posicao = int(posicao)
    lista.pop(posicao - 1)
    print(f"O item na posição '{posicao}' foi removido.")
      
while opcao != 0:
    print("Menu: ")
    print("1 - Mostrar a lista")
    print("2 - Adicionar item")
    print("3 - Alterar item")
    print("4 - Remover item")
    print("5 - Marcar como concluído")
    print("0 - Sair")

    opcao = input("Informe a opção desejada: ")
    opcao = int(opcao)

    if opcao == 2:
        adicionar_item()

    elif opcao == 1:
        mostrar_lista() 

    elif opcao == 3:
       alterar_item()

    elif opcao == 5:
        marcar_concluido()

    elif opcao == 4:
        remover_item()

