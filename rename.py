import os

# Diretório onde estão os arquivos de vídeo
diretorio = './'

# Novo prefixo que você deseja adicionar
novo_prefixo = ''

# Caracteres que você deseja remover (opcional)
caracteres_para_remover = ['_']  # Exemplo: remove "_old" e "-copy"

# Lista todos os arquivos no diretório
for nome_arquivo in os.listdir(diretorio):
    # Verifica se é um arquivo de vídeo (ajuste as extensões conforme necessário)
    if nome_arquivo.endswith(('.mp4', '.mkv', '.avi', '.mov')):
        # Remove os caracteres indesejados
        novo_nome = nome_arquivo
        for caractere in caracteres_para_remover:
            novo_nome = novo_nome.replace(caractere, ' ')
        
        # Adiciona o novo prefixo
        novo_nome = novo_prefixo + novo_nome

        # Renomeia o arquivo
        caminho_antigo = os.path.join(diretorio, nome_arquivo)
        caminho_novo = os.path.join(diretorio, novo_nome)
        os.rename(caminho_antigo, caminho_novo)
        print(f'Renomeado: {nome_arquivo} -> {novo_nome}')