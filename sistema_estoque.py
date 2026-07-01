from asyncio.proactor_events import _ProactorDuplexPipeTransport


produtos = []

sair = False

print("Bem vindo ao sistema de estoque!")

while sair == False:
    print("-"*20)
    print("1- Listar produtos")
    print("2- Cadastra um novo produto")
    print("3- Deletar um produto")
    print("0- Sair do sistema")
    opcao = input("Sua Opcao: ")
    match opcao:
        case '0':
            sair = True 
        case '1':
            for p in produtos:
                print("-", p)
            print("#"*30)
            input("pressione enter para continuar...")
        case '2':
            print("cadastrar novo produto: ")  
            nome_produto = input("nome do produto: ")

            produtos.append(nome_produto)
        case '3':
            print("remover produto")
            nome_produto = input("qual deletado: ")
            if nome_produto in produtos:
                produtos.remove(nome_produto)
                print("removido com sucesso")
            else:
                print(nome_produto, "nao existe na lista!")
            input("pressione entrar para continuar...")                    