def ExtratoCategoria():
    categorias={}
    with open("lib.txt","r") as arquivo:
      linhas=arquivo.readlines()
    #Processa por livro, considerando cada um como um bloco de 4 linhas
    for i in range(0, len(linhas),4):
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
       print(f"\nCategoria: {categoria}")
       #Imprime os livros da categoria referida.
       for livro in categorias[categoria]:
          print(livro)            
          

    