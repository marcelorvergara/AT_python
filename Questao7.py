import threading
import requests


class Questao7(threading.Thread):
    def __init__(self):
        super().__init__()
        url = 'https://sites.google.com/site/dr2fundamentospython/arquivos/Winter_Olympics_Medals.csv'
        requisicao = requests.get(url, timeout=5)

        if requisicao.status_code != 200:
            requisicao.raise_for_status()
        else:
            print("Conectado")
        csv = requisicao.text
        linhas = csv.splitlines()

        # SWE
        suecia = 0
        sue_medalhas = []
        # DEN
        dinamarca = 0
        den_medalhas = []
        # NOR
        nor_medalhas = []
        noruega = 0
        for ln in range(1, len(linhas)):
            colunas = linhas[ln].split(',')
            # somente séc. XXI
            if int(colunas[0]) > 2000:
                # somente modalidades 'curling', 'skating', 'skiing', 'ice hockey'
                if colunas[2] == 'Curling' or colunas[2] == 'Skating' or colunas[2] == 'Skiing' or colunas[2] == 'Ice Hockey':
                    # se ouro
                    if colunas[7] == 'Gold':
                        gen = ''
                        if colunas[6] == 'M':
                            gen = 'masculino'
                        else:
                            gen = 'feminino'
                        if colunas[4] == 'SWE':
                            suecia += 1
                            sue_medalhas.append('Esporte: ' + colunas[2] + ' Ano: ' + colunas[0] + ' Cidade: ' + colunas[
                                1] + ' Gênero: ' + gen)
                        elif colunas[4] == 'DEN':
                            dinamarca += 1
                            den_medalhas.append('Esporte: ' + colunas[2] + ' Ano: ' + colunas[0] + ' Cidade: ' + colunas[
                                1] + ' Gênero: ' + gen)
                        elif colunas[4] == 'NOR':
                            noruega += 1
                            nor_medalhas.append('Esporte: ' + colunas[2] + ' Ano: ' + colunas[0] + ' Cidade: ' + colunas[
                                1] + ' Gênero: ' + gen)

        maior = ''
        num_medalhas = 0
        if suecia > dinamarca or suecia > noruega:
            maior = 'Suecia'
            num_medalhas = suecia
        if dinamarca > suecia or dinamarca > noruega:
            maior = 'Dinamarca'
            num_medalhas = dinamarca
        else:
            maior = 'Noruega'
            num_medalhas = noruega
        print('\nO país com o maior número de medalhas ouro nas modalidades especificadas é a', maior, 'com', num_medalhas, 'medalhas')
        print('\nRelatório dos países Suécia, Dinamarca e Noruega referente as medalhas ouro nos esportes Curling, Patinação no gelo, Esqui e Hóquei sobre o gelo no século XXI')
        print('\nSuécia:\n')
        if sue_medalhas:
            for ln in sue_medalhas:
                print(ln)
        else:
            print('Não obteve medalhas de ouro')
        print('\nDinamarca:\n')
        if den_medalhas:
            for ln in den_medalhas:
                print(ln)
        else:
            print('Não obteve medalhas de ouro')
        print('\nNoruega:\n')
        if nor_medalhas:
            for ln in nor_medalhas:
                print(ln)
        else:
            print('Não obteve medalhas de ouro')
