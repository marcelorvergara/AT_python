import threading


class MenuItems(threading.Thread):
    def __init__(self):
        super().__init__()
        print("\n-------Menu--------\n")
        print("1 - Tuplas crescente")
        print("2 - Soma até N")
        print("3 - Not a pow")
        print("4 - Ordenar 5 números")
        print("5 - Lista de ímpares e tupla de pares")
        print("6 - Quadrado amarelo")
        print("7 - Olimpíadas de Inverno")
        print("8 - VC disse Games?")
        print("9 - Centro Oeste")
        print("10 - Pyladies")
        print("\n")
        print("0 - Digite 0 (Zero) para sair\n")
