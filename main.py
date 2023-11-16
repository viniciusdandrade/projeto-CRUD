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
    
    with open("biblioteca.txt", 'a') as arquivo:
        arquivo.write("Nome: "+nome + '\n')
        arquivo.write("Autor: "+autor + '\n')
        arquivo.write("Categoria: "+categoria + '\n')
        arquivo.write(f"Custo: R${custo}\n")
        gasto += custo
        arquivo.write("\n")
    
    print("Livro adicionado com sucesso!")

def Visualizar():
    arquivo = open("biblioteca.txt", 'r')
    print(arquivo.read())

def GastoTotal():
    gasto = 0
    with open("biblioteca.txt",'r') as arquivo:
        linhas = arquivo.readlines()

    for linha in linhas:
        if linhas.startswith("Custo: R$"):
            gasto += float(linha.split('R$')[1])
        
    print(f"O gasto total com a biblioteca foi de {gasto:.2f} reais.")

MostrarMenu()
