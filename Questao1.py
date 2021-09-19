import threading


class Questao1(threading.Thread):
    def __init__(self):
        super().__init__()
        tupla = tuple(input("Entre com 3 números"))
        print(sorted(tupla))
