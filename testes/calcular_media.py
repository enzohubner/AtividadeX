def retorna_inform():
    with open("alunos.txt", "r") as arquivo:
        aluno_dict = {}
        idades = []
        for linha in arquivo:
            chave, valor = linha.split(":")
            aluno_dict[chave] = valor
            if chave == "idade":
                idade = int(valor)
                idades.append(idade)
    calc_media(idades)


def calc_media(idades):
    media = sum(idades)/len(idades)
    print(media)
    
retorna_inform()         