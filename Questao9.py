import threading
from BuscaEstados import BuscaEstados
import EstadosMenu


def roda_programa(estado):
    dic_infos = {}
    programa = BuscaEstados()
    infos = programa.get_estado()
    for idx, value in infos.items():
        print('Infos. Estados Centro Oeste: ' + estado)
        for i in value:
            if i == 'titulo-0' or value[i][0] == estado:
                dic_infos['Nome'] = value[i][1]
                dic_infos['Capital'] = value[i][2]
                dic_infos['População'] = value[i][3]
                dic_infos['Área'] = value[i][4]
        print('{Nome} / {Capital} / {População} / {Área}'.format(**dic_infos))
    return infos


def switch_menu(arg):
    if arg == 1:
        print("Distrito Federal")
        roda_programa('DF')
    elif arg == 2:
        print("Goiás")
        roda_programa('GO')
    elif arg == 3:
        print("Mato Grosso")
        roda_programa('MT')
    elif arg == 4:
        print("Mato Grosso do Sul")
        roda_programa('MS')
    elif arg == 0:
        print("")
    else:
        print("\n--------\nOpção inválida!\n--------\n")


class Questao9(threading.Thread):
    def __init__(self):
        super().__init__()
        ent_ok = False
        while not ent_ok:
            try:
                menu_loop = False
                while not menu_loop:
                    menu_items = EstadosMenu.EstadosMenu()
                    menu_items.start()
                    num = int(input("Entre com o número correspondente ao estado: "))
                    if num == 0:
                        menu_loop = True
                        print("Inté!")
                    switch_menu(num)
                    print()
                    ent_ok = True
            except ValueError:
                print('\n-----------------\nEntrada inválida!\n-----------------')

