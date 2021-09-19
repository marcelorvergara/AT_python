import threading


class Questao4(threading.Thread):
    def __init__(self):
        super().__init__()
        super().__init__()
        print("Entre com cinco números inteiros:")
        nums = []
        for i in range(5):
            nums.append(int(input("Entre com o " + str(i+1) + "º" + " número: ")))
        rev = []
        for i in reversed(nums):
            rev.append(i)
        print("Ordem reversa é", rev)
