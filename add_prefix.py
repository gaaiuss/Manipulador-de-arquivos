import os

# Diretório onde os arquivos estão localizados
diretorio = './'

# Prefixo que você deseja adicionar
prefixo = 'Bleach'

# Lista todos os arquivos no diretório
for nome_arquivo in os.listdir(diretorio):
    # Verifica se é um arquivo (ignora pastas)
    if os.path.isfile(os.path.join(diretorio, nome_arquivo)):
        # Adiciona o prefixo ao nome do arquivo
        novo_nome = prefixo + nome_arquivo
        caminho_antigo = os.path.join(diretorio, nome_arquivo)
        caminho_novo = os.path.join(diretorio, novo_nome)
        os.rename(caminho_antigo, caminho_novo)
        print(f'Renomeado: {nome_arquivo} -> {novo_nome}')