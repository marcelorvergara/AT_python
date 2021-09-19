import threading


class Questao5(threading.Thread):

    def __init__(self):
        super().__init__()
        print("Entre com cinco números inteiros:")
        tupla_nums = (3, 6, 2, 7, 8, 3, 4, 8, 9, 8, 3, 1)
        pares = []
        impares = ()
        for n in tupla_nums:
            if n % 2 == 0:
                pares.append(n)
            else:
                impares = impares + (n,)
        print("Lista de pares", pares)
        print("Tupla de ímpares", impares)
