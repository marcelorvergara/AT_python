import threading


class Questao2(threading.Thread):
    def __init__(self):
        super().__init__()
        num = int(input("Digite um número para obter a soma dos pares que compões esse número:"))
        tot = 0
        for i in range(1, num):
            if i % 2 == 0:
                tot += i
        print("A soma dos número pares até", num, "é", tot)
