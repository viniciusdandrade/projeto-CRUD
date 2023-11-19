def VisualizarCategoria():
    categoria_desejada=input("Digite a categoria que você deseja visualizar: ")
    categoria_encontrada=False
    with open("lib.txt","r") as arquivo:
      linhas=arquivo.readlines()
    #Processa por livro, considerando cada um como um bloco de 4 linhas
    for i in range(0, len(linhas),4):
       #Considera a categoria como o terceiro elemento de cada livro
       if categoria_desejada in linhas[i+2]:
          #Concatena em uma string a lista "linhas" que foi fatiada de forma a representar os livros nos quais a categoria desejada foi encontrada
          print("".join(linhas[i:i+4])) 
          categoria_encontrada=True

    if categoria_encontrada==False:
       print("Não existem livros de tal categoria na biblioteca.")
     
        