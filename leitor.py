import os
import pandas as pd
import Functions as fun

pasta_extratos = fun.pegar_nome_pasta()

# Verifique se o caminho da pasta é válido
if os.path.exists(pasta_extratos) and os.path.isdir(pasta_extratos):
    # Percorra todos os arquivos na pasta
    for nome_arquivo in os.listdir(pasta_extratos):
        # Obtenha o caminho completo de cada arquivo
        if "Caixa - " in nome_arquivo:
            caminho_completo = os.path.join(pasta_extratos, nome_arquivo)
            # Ler e colocar na planiha as movimentações e o saldo do fundo
        else:
            print('Não é caixa')
else:
    print("A pasta não existe ou não é válida.")