def MostrarMenu():
    while True:
        print("\n1 - Adicionar\n2 - Visualizar\n3 - Atualizar\n4 - Excluir\n5 - Visualizar gasto total\n6 - Sair do programa")
        opcao = int(input("\nDigite o código da opção desejada: "))
        if opcao == 1:
            Adicionar()
        elif opcao == 2:
            Visualizar()
        elif opcao == 3:
            Atualizar()
        elif opcao == 4:
            Excluir()
        elif opcao == 5:
            GastoTotal()
        elif opcao == 6:
            break

def Adicionar():
    nome = input("Digite o  nome do livro: ")
    autor = input("Digite o nome do autor: ")
    categoria = input("Digite a categoria: ")
    custo = float(input("Digite quanto o o livro custou: "))
    
    with open("lib.txt", 'a') as arquivo:
        arquivo.write("Nome: "+nome + '\n')
        arquivo.write("Autor: "+autor + '\n')
        arquivo.write("Categoria: "+categoria + '\n')
        arquivo.write(f"Custo: R${custo}\n")
        arquivo.write("\n")
    
    print("Livro adicionado com sucesso!")

def Visualizar():
    arquivo = open("lib.txt", 'r')
    print(arquivo.read())

def Atualizar():
    nome = input("Digite o nome do livro cujas informações serão atualizadas: ")
    novo_nome = input("Digite o novo nome do livro: ")
    novo_autor = input("Digite o novo nome do autor: ")
    nova_categoria = input("Digite a nova categoria: ")
    novo_custo = float(input("Digite o novo custo do livro: "))

    with open("lib.txt", 'r') as arquivo:
        linhas = arquivo.readlines()

        index = None
        for i, linha in enumerate(linhas):
            if linha.startswith(f"Nome: {nome}"):
                index = i
                break
    
        if index != None:
            linhas[index] = f"Nome: {novo_nome}\n"
            linhas[index + 1] = f"Autor: {novo_autor}\n"
            linhas[index + 2] = f"Categoria: {nova_categoria}\n"
            linhas[index + 3] = f"Custo: R${novo_custo}\n"

            with open("lib.txt",'w') as arquivo:
                arquivo.writelines(linhas)

def Excluir():
    nome = input("Digite o nome do livro que será excluído: ")

    with open("lib.txt",'r') as arquivo:
        linhas = arquivo.readlines()

    index = None
    for i, linha in enumerate(linhas):
        if linha.startswith(f"Nome: {nome}"):
            index = i
            break
    
    if index != None:
        del linhas[index:index+4]

        with open("lib.txt",'w') as arquivo:
            arquivo.writelines(linhas)
                
def GastoTotal():
    gasto = 0
    with open("lib.txt",'r') as arquivo:
        linhas = arquivo.readlines()

    for linha in linhas:
        if linha.startswith("Custo: R$"):
            gasto += float(linha.split('R$')[1])
        
    print(f"\nO gasto total com a biblioteca foi de {gasto:.2f} reais.")

MostrarMenu()