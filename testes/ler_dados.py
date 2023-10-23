def ler_dados():
    nome = input("Digite o nome do aluno: ")
    idade = input("Digite a idade do aluno: ")
    curso = input("digite o curso do aluno: ")

    dados_alunos = {
        "nome":nome,
        "idade":idade,
        "curso":curso
    }
    return dados_alunos

def ler_varios():
    quantidade = int(input("Digite a quantidade: "))
    alunos = []
    for x in range(0, quantidade):
        aluno = ler_dados()
        alunos.append(aluno)
    return alunos    