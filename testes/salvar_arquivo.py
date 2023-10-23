def criar_arquivo(dados_alunos):
    with open("alunos.txt", "w") as arquivo:
        for aluno in dados_alunos:
            for chave, valor in aluno.items():
                linha = f'{chave}:{valor}\n'
                arquivo.write(linha)