import threading
import requests
from bs4 import BeautifulSoup

global response


class Questao10(threading.Thread):

    def __init__(self):
        global response
        super().__init__()
        self.url = 'http://brasil.pyladies.com/about'
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                html = response.text
                soup = BeautifulSoup(html, features="html.parser")
                divs = soup.body.find_all('div')
                text = []
                dic_text = {}
                for div in divs:
                    s1 = div.text.replace('\n', ' ').split()
                    for s in s1:
                        text.append(s)
                        if s not in dic_text:
                            dic_text[s] = 1
                        else:
                            dic_text[s] = dic_text[s] + 1
                print('O total de símbolos (palavras, caracteres ou números) com ao menos um caracter são', len(text))
                print('As palavras que aparecem apenas uma vez no corpo da página são:')
                tot_pal = 0
                for pal in dic_text.keys():
                    if dic_text.get(pal) == 1 and len(pal) > 1:
                        print(pal)
                        tot_pal += 1
                print('O total de palavras (strings com ao menos 2 caracteres) no corpo da página é:', tot_pal)
                print('A palavra ladies aparece', dic_text['ladies'], 'vez(es)')
            else:
                print('Else', response.reason)
        except:
            print('Except', response.reason)
