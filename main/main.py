def MostrarMenu():
    while True:
        print("\n1 - Adicionar")
        print("2 - Visualizar")
        print("3 - Atualizar")
        print("4 - Excluir")
        print("5 - Extrato por Categoria")
        print("6 - Visualizar por Categoria")
        print("7 - Visualizar Gasto Total")
        print("8 - Visualizar Autor")
        print("9 - Sair do Programa")
        opcao = int(input("\nDigite o código da opção desejada: "))
        try:
            if opcao == 1:
                Adicionar()
            elif opcao == 2:
                Visualizar()
            elif opcao == 3:
                Atualizar()
            elif opcao == 4:
                Excluir()
            elif opcao == 5:
                ExtratoCategoria()
            elif opcao == 6:
                VisualizarCategoria()    
            elif opcao == 7:
                GastoTotal()
            elif opcao==8:
                VisualizarAutor()
            elif opcao == 9:
                break
        except ValueError:
            print("Insira um valor inteiro entre 1 e 9.")    

#Opção 1
def Adicionar():
    
    try : 
        nome = input("Digite o  nome do livro: ")
        autor = input("Digite o nome do autor: ")
        categoria = padronizar_entrada(input("Digite a categoria: "))
        custo = float(input("Digite quanto o o livro custou: "))
    
        with open("lib.txt", 'a', encoding="utf8") as arquivo:
            arquivo.write("Nome: "+nome + '\n')
            arquivo.write("Autor: "+autor + '\n')
            arquivo.write("Categoria: " + categoria + '\n')
            arquivo.write(f"Custo: R${custo:.2f}\n")
            arquivo.write("---\n")  # Delimitador para separar os livros
    
            print("Livro adicionado com sucesso!")
    except ValueError :
        print("Digite um valor numérico") #tratamento de erro caso não se digite o valor esperado
        

#Opção 2
def Visualizar():
    try:
        arquivo = open("lib.txt", 'r')
        print(arquivo.read())
    except FileNotFoundError:
        print("Arquivo não encontrado. Crie o mesmo adicionando um livro.")    

#Opção 3
def Atualizar():
    try:
        nome_do_livro=input("Digite o nome do livro que você deseja atualizar : ")
        livro_presente=False
        novo_conteudo=""
        
        with open("lib.txt", "r", encoding="utf8") as arquivo:
            conteudo=arquivo.read()
            livros=conteudo.split("---\n")
            
            for livro in livros:
                if "Nome: " + nome_do_livro in livro:
                    livro_presente=True
                    print("Atualize as informações do livro: ")
                    novo_nome = input("Digite o  nome do livro: ")
                    novo_autor = input("Digite o nome do autor: ")
                    nova_categoria = padronizar_entrada(input("Digite a categoria: "))
                    novo_custo = float(input("Digite quanto o o livro custou: "))
                    
                    #Altera as informações do livro.
                    livro_atualizado = "Nome: " + novo_nome + "\n"
                    livro_atualizado = livro_atualizado + "Autor: " + novo_autor + "\n"
                    livro_atualizado = livro_atualizado + "Categoria: " + nova_categoria + "\n"
                    livro_atualizado = livro_atualizado + "Custo: R$" + novo_custo + "\n"
                    
                    novo_conteudo=novo_conteudo+livro_atualizado+"\n"
                
            else:
                novo_conteudo=novo_conteudo+livro+"---\n"

        if livro_presente==True:
            with open("lib.txt", "w", encoding="utf8") as arquivo:
                arquivo.write(novo_conteudo)
            print("Livro atualizado.")    
            
        else:
            print("Livro não encontrado.")
    
    except FileNotFoundError:
        print("Arquivo não encontrado. Crie o mesmo adicionando um livro.")     

#Opção 4
def Excluir():
    try:
        nome_do_livro=input("Digite o nome do livro que você deseja excluir: ")
        livro_presente=False
        novo_conteudo=""
        
        with open("lib.txt","r",encoding="utf8") as arquivo:
            conteudo=arquivo.read()
            
            # Divide os livros como unidade e transforma em lista.
            livros=conteudo.split("---\n")
            for livro in livros:
                if "Nome: " + nome_do_livro not in livro:
                    novo_conteudo=novo_conteudo+livro+"---\n"
                else:
                    livro_presente=True

        if livro_presente==True:
            with open("lib.txt","w") as arquivo:
                arquivo.write(novo_conteudo)
        else:
            print("Livro não encontrado.")
    
    except FileNotFoundError:
        print("Arquivo não encontrado. Crie o mesmo adicionando um livro.")              

#Opção 5
def ExtratoCategoria():
    try:
        categorias={}
        
        with open("lib.txt","r", encoding="utf8") as arquivo:
            linhas=arquivo.readlines()
        
        #Processa por livro, considerando cada um como um bloco de 4 linhas + delimitador
        for i in range(0, len(linhas),5):
            #Verifica o índice.
            if i+4< len(linhas):
            #Considera a categoria como o terceiro elemento de cada livro, remove os espaços e quebras de linha, transforma em lista e separa a descrição da categoria em si.
                categoria=(linhas[i+2]).strip().split(": ")[1]
            #Concatena em uma string a lista "linhas" que foi fatiada de forma a representar os livros.
                info_livro=("".join(linhas[i:i+4]))
                
            #Cria as categorias dentro do dicionário caso não existam, e em seguida adiciona as informações do livro em sua respectiva categoria.
                if categoria not in categorias:
                    categorias[categoria]=[]
                categorias[categoria].append(info_livro)
        
        #Gera o cabeçalho com o nome do gênero.
        for categoria in categorias:
            print(f"\nCategoria: {categoria}\n")
        #Imprime os livros da categoria referida.
        for livro in categorias[categoria]:
            print(livro)
    
    except FileNotFoundError:
        print("Arquivo não encontrado. Crie o mesmo adicionando um livro.")         

#Opção 6
def VisualizarCategoria():
    try:
        categoria_desejada=padronizar_entrada(input("Digite a categoria que você deseja visualizar: "))
        categoria_encontrada=False
        
        with open("lib.txt","r",encoding="utf8") as arquivo:
            linhas=arquivo.readlines()
        
        #Processa por livro, considerando cada um como um bloco de 4 linhas + delimitador
        for i in range(0, len(linhas),5):
        #Considera a categoria como o terceiro elemento de cada livro, verifica o índice
            if  i+2< len(linhas) and categoria_desejada in linhas[i+2]:
            #Concatena em uma string a lista "linhas" que foi fatiada de forma a representar os livros nos quais a categoria desejada foi encontrada
                print("".join(linhas[i:i+4])) 
                categoria_encontrada=True

        if categoria_encontrada==False:
            print("Não existem livros de tal categoria na biblioteca.")
    
    except FileNotFoundError:
        print("Arquivo não encontrado. Crie o mesmo adicionando um livro.") 

#Opção 7
def GastoTotal():
    try:
        gasto = 0
        with open("lib.txt",'r',encoding="utf8") as arquivo:
            linhas = arquivo.readlines()

        for linha in linhas:
            if linha.startswith("Custo: R$"):
                gasto += float(linha.split('R$')[1])
            
        print(f"\nO gasto total com a biblioteca foi de {gasto:.2f} reais.")
    except FileNotFoundError:
        print("Arquivo não encontrado. Crie o mesmo adicionando um livro.")     

#Opção 8
def VisualizarAutor():
    try:
        autor_procurado=input("Digite o autor/a autora que você deseja visualizar: ")
        autor_encontrado=False
        
        with open("lib.txt","r",encoding="utf8") as arquivo:
            linhas=arquivo.readlines()
        
        #Processa por livro, considerando cada um como um bloco de 4 linhas + delimitador.
        for i in range(0, len(linhas),5):
        #Considera o autor como o segundo elemento de cada livro, verifica o índice.
            if  i+1< len(linhas) and autor_procurado in linhas[i+1]:
            #Concatena em uma string a lista "linhas" que foi fatiada de forma a representar os livros nos quais o autor desejado foi encontrado.
                print("".join(linhas[i:i+4])) 
                autor_encontrado=True

        if autor_encontrado==False:
            print("Não existem livros de tal autor/autora na biblioteca.")
    
    except FileNotFoundError:
        print("Arquivo não encontrado. Crie o mesmo adicionando um livro.")         

#Função auxiliar para entradas, padroniza todas as entradas relevantes, no caso, a categoria.
def padronizar_entrada(entrada):
    entrada = entrada.strip().lower()  # Remove espaços em branco no começo e no fim e converte para todas as letras para minúsculas.
    palavras = entrada.split()  # Transforma a string em lista.
    entrada_padronizada = ' '.join(palavra.capitalize() for palavra in palavras)  # Coloca a primeira letra de cada palavra em maiúsculo. (Ex: Ficção Científica.)
    return entrada_padronizada

#Inicializa o programa
MostrarMenu()
