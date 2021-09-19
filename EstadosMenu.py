import threading


class EstadosMenu(threading.Thread):
    def __init__(self):
        super().__init__()
        print("\n-------Menu--------\n")
        print("Escolha um estado:")
        print("1 - DF - Distrito Federal")
        print("2 - GO - Goiás")
        print("3 - MT - Mato Grosso")
        print("4 - MS - Mato Grosso do Sul")
        print("0 - Digite 0 (Zero) para sair\n")
