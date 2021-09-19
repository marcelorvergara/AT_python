import requests
from bs4 import BeautifulSoup


class BuscaEstados:

    def __init__(self):
        # 15, 16 tabela Estados Sudeste
        self.url = 'https://fgopassos.github.io/pagina_exemplo/estadosCentroOeste.html'

    def get_estado(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                html = response.text
                soup = BeautifulSoup(html, features="html.parser")
                dic = {}
                dic_head = {}
                dic_cel = {}
                linha = 0
                for div in soup.find_all('div', attrs={'class': True}):
                    # encontrando a tabela
                    if 'tabela' in div['class']:
                        # dentro da tabela, separar, célula - linha - titulo
                        key = ''
                        val = ''
                        for div2 in div.find_all('div'):
                            # pegando título e linhas
                            if 'celula' not in div2['class']:
                                key_tmp = div2['class']
                                key = str(key_tmp[0]) + '-' + str(linha)
                                # incrementa a linha para ser a 'cabeça' do dicionário (titulo-0, linha-1, linha-2, linha-3...)
                                linha += 1
                                celula = 0
                                dic_cel = {}
                            # aqui cai os valores das células
                            else:
                                dic_cel[celula] = div2.text
                                celula += 1
                            dic_head[key] = dic_cel
                        dic['tabela'] = dic_head
                print('Conteúdo da tabela:\n', dic)
                return dic
            else:
                return response.reason
        except:
            return response.reason

