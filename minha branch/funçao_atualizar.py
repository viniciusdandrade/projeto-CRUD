def Atualizar():
    nome_do_livro=input("Digite o nome do livro que você deseja excluir: ")
    livro_presente=False
    novo_conteudo=""
    with open("lib.txt","r") as arquivo:
        conteudo=arquivo.read()
        livros=conteudo.split("---\n")
        for livro in livros:
            if "Nome: " + nome_do_livro in livro:
               livro_presente=True
               print("Atualize as informações do livro: ")
               novo_nome = input("Digite o  nome do livro: ")
               novo_autor = input("Digite o nome do autor: ")
               nova_categoria = input("Digite a categoria: ")
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
        with open("lib.txt","w") as arquivo:
            arquivo.write(novo_conteudo)
        print("Livro atualizado.")    
        
    else:
        print("Livro não encontrado.")                        
