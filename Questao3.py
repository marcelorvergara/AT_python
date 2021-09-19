import threading

def pow(a,b):
    tot = 1
    for i in range(0,b):
        print('tot', tot)
        tot = tot * a
    return tot


class Questao3(threading.Thread):
    def __init__(self):
        super().__init__()
        pri = int(input("Entre com o primeiro número:"))
        sec = int(input("Entre com o segundo número:"))
        res = pow(pri,sec)
        print("Pow sem usar pow é", res)

