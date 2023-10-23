from pprint import pprint
from ler_dados import ler_varios
from salvar_arquivo import criar_arquivo
if __name__ == '__main__':
    dados_alunos = ler_varios()
    criar_arquivo(dados_alunos=dados_alunos)