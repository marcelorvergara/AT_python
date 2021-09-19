import threading
from datetime import datetime

import requests
from dateutil.relativedelta import relativedelta


class Questao8(threading.Thread):
    def __init__(self):
        super().__init__()
        url = 'https://sites.google.com/site/dr2fundamentospython/arquivos/Video_Games_Sales_as_at_22_Dec_2016.csv'
        requisicao = requests.get(url, timeout=5)

        if requisicao.status_code != 200:
            requisicao.raise_for_status()
        else:
            print("Conectado")
        csv = requisicao.text
        linhas = csv.splitlines()
        publishers_dict = {}
        publishers_dict_vendas = {}
        publishers_dict_jp_act = {}
        publishers_dict_jp_sho = {}
        publishers_dict_jp_pla = {}
        publishers_dict_jp_act_v = {}
        publishers_dict_jp_sho_v = {}
        publishers_dict_jp_pla_v = {}
        # 10 anos atrás JP
        dez_anos = datetime.now() - relativedelta(years=10)
        print('dez anos atrás', dez_anos.year)
        for ln in range(1, len(linhas)):
            colunas = linhas[ln].split(',')
            if colunas[3] == 'Action' or colunas[3] == 'Shooter' or colunas[3] == 'Platform':
                # incremento de jogos pelos gêneros acima
                if colunas[4] not in publishers_dict:
                    publishers_dict[colunas[4]] = 1
                    publishers_dict_vendas[colunas[4]] = 0.0
                else:
                    publishers_dict[colunas[4]] = publishers_dict[colunas[4]] + 1
                    publishers_dict_vendas[colunas[4]] += float(colunas[9])
                # útlimos 10 anos no japão
                if colunas[2] != 'N/A':
                    # testa o ano E se teve vendas maior que zero(0)
                    if int(colunas[2]) > int(str(dez_anos).split('-')[0]) and float(colunas[7]) > 0:
                        if colunas[3] == 'Action':
                            if colunas[4] not in publishers_dict_jp_act:
                                publishers_dict_jp_act[colunas[4]] = 1
                                publishers_dict_jp_act_v[colunas[4]] = 0.0
                            else:
                                publishers_dict_jp_act[colunas[4]] = publishers_dict_jp_act[colunas[4]] + 1
                                publishers_dict_jp_act_v[colunas[4]] = publishers_dict_jp_act_v[colunas[4]] + float(colunas[7])
                        elif colunas[3] == 'Shooter':
                            if colunas[4] not in publishers_dict_jp_sho:
                                publishers_dict_jp_sho[colunas[4]] = 1
                                publishers_dict_jp_sho_v[colunas[4]] = 0.0
                            else:
                                publishers_dict_jp_sho[colunas[4]] = publishers_dict_jp_sho[colunas[4]] + 1
                                publishers_dict_jp_sho_v[colunas[4]] = publishers_dict_jp_sho_v[colunas[4]] + float(colunas[7])
                        elif colunas[3] == 'Platform':
                            if colunas[4] not in publishers_dict_jp_pla:
                                publishers_dict_jp_pla[colunas[4]] = 1
                                publishers_dict_jp_pla_v[colunas[4]] = 0.0
                            else:
                                publishers_dict_jp_pla[colunas[4]] = publishers_dict_jp_pla[colunas[4]] + 1
                                publishers_dict_jp_pla_v[colunas[4]] = publishers_dict_jp_pla_v[colunas[4]] + float(colunas[7])

        # printar os que mais publicaram jogos nos três gêneros
        max_n = max(publishers_dict.values())
        pub = list(publishers_dict.keys())[list(publishers_dict.values()).index(max_n)]
        print('O publisher com maior quantidade de jogos nos generos selecionados é', pub, 'com', max_n, 'jogos')
        # pegar o segundo maior
        publishers_dict_2 = publishers_dict
        del publishers_dict_2[pub]
        max_n_2 = max(publishers_dict_2.values())
        pub_2 = list(publishers_dict_2.keys())[list(publishers_dict_2.values()).index(max_n_2)]
        print('O segundo maior publisher em quantidade de jogos nos generos selecionados é', pub_2, 'com', max_n_2,
              'jogos')
        publishers_dict_3 = publishers_dict_2
        del publishers_dict_3[pub_2]
        max_n_3 = max(publishers_dict_3.values())
        pub_3 = list(publishers_dict_3.keys())[list(publishers_dict_3.values()).index(max_n_3)]
        print('E o terceiro lugar vair para', pub_3, 'com', max_n_3, 'jogos')
        # printar os que mais venderam
        max_n = max(publishers_dict_vendas.values())
        pub = list(publishers_dict_vendas.keys())[list(publishers_dict_vendas.values()).index(max_n)]
        print('O publisher com maior valor em vendas nos gêneros selecionados é', pub, 'com', round(max_n, 2),
              'dólares')
        # pegar o segundo maior
        publishers_dict_vendas_2 = publishers_dict_vendas
        del publishers_dict_vendas_2[pub]
        max_n_2 = max(publishers_dict_vendas_2.values())
        pub_2 = list(publishers_dict_vendas_2.keys())[list(publishers_dict_vendas_2.values()).index(max_n_2)]
        print('O segundo maior publisher em valor de vendas nos generos selecionados é', pub_2, 'com',
              round(max_n_2, 2), 'dólares')
        publishers_dict_vendas_3 = publishers_dict_vendas_2
        del publishers_dict_vendas_3[pub_2]
        max_n_3 = max(publishers_dict_vendas_3.values())
        pub_3 = list(publishers_dict_vendas_3.keys())[list(publishers_dict_vendas_3.values()).index(max_n_3)]
        print('E o terceiro lugar vair para', pub_3, 'com', round(max_n_3, 2), 'dólares')
        # Japão meu filho Action
        max_jp_act = max(publishers_dict_jp_act.values())
        pub_jp_act = list(publishers_dict_jp_act.keys())[list(publishers_dict_jp_act.values()).index(max_jp_act)]
        print('No japão a publisher que mais vendeu em 10 anos o gênero action foi', pub_jp_act, 'com o total de títulos:', max_jp_act)
        # Japão meu filho Shooter
        max_jp_sh = max(publishers_dict_jp_sho.values())
        pub_jp_act = list(publishers_dict_jp_sho.keys())[list(publishers_dict_jp_sho.values()).index(max_jp_sh)]
        print('No japão a publisher que mais vendeu em 10 anos o gênero shooter foi', pub_jp_act, 'com o total de títulos:', max_jp_sh)
        # Japão meu filho Platform
        max_jp_pl = max(publishers_dict_jp_pla.values())
        pub_jp_pl = list(publishers_dict_jp_pla.keys())[list(publishers_dict_jp_pla.values()).index(max_jp_pl)]
        print('No japão a publisher que mais vendeu em 10 anos o gênero platform foi', pub_jp_pl, 'com o total de títulos:', max_jp_pl)
        # Vendas Japão
        max_jp_act_ven = max(publishers_dict_jp_act_v.values())
        pub_jp_act_ven = list(publishers_dict_jp_act_v.keys())[list(publishers_dict_jp_act_v.values()).index(max_jp_act_ven)]
        print('No japão, nos últimos 10 anos, no gênero action, a publisher que mais vendeu foi', pub_jp_act_ven,'com um total de', round(max_jp_act_ven,2))
        max_jp_sh_ven = max(publishers_dict_jp_sho_v.values())
        pub_jp_sho_ven = list(publishers_dict_jp_sho_v.keys())[list(publishers_dict_jp_sho_v.values()).index(max_jp_sh_ven)]
        print('No japão, nos últimos 10 anos, no gênero shooting, a publisher que mais vendeu foi', pub_jp_sho_ven,'com um total de', round(max_jp_sh_ven,2))
        max_jp_pl_ven = max(publishers_dict_jp_pla_v.values())
        pub_jp_pla_ven = list(publishers_dict_jp_pla_v.keys())[list(publishers_dict_jp_pla_v.values()).index(max_jp_pl_ven)]
        print('No japão, nos últimos 10 anos, no gênero platform, a publisher que mais vendeu foi', pub_jp_pla_ven,'com um total de', round(max_jp_pl_ven,2))
