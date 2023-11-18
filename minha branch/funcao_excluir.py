def func_excluir():
    nome_do_livro=input("Digite o nome do livro que você deseja excluir: ")
    livro_presente=False
    novo_conteudo=""
    with open("lib.txt","r") as arquivo:
        conteudo=arquivo.read()
        livros=conteudo.split("---\n")
        for livro in livros:
            if "Nome: " + nome_do_livro not in livro:
                novo_conteudo=novo_conteudo+livro+"---\n"
            else:
                livro_presente==True

    if livro_presente==True:
        with open("lib.txt","w") as arquivo:
            arquivo.write(novo_conteudo)
    else:
        print("Livro não encontrado")                        
