import numpy as np


def genera_array_1d():
    arr = np.random.randint(1, 101, size=(10))
    print(arr)


def genera_array_float():
    arr = np.random.random(size=(3,3))
    print(arr)


def genera_array_interi_crescenti():
    arr = np.array(range(0, 11))
    print(arr)


def genera_tabelline():
    tabellina = []
    for y in range(1, 10):
        riga = []
        for x in range(1, 10):
            riga.append(x * y)
        tabellina.append(riga)
    tabellina = [[x * y for x in range(1, 10)] for y in range(1, 10)]
    print(tabellina)
    return tabellina


def estrai_valori():
    tabellina = genera_tabelline()
    estrai = []
    for value in tabellina:
        print("sto qua")
        for i in value:
            if i > 35:
                estrai.append(i)
    print(estrai)


if __name__ == '__main__':
    genera_array_1d()
    genera_array_float()
    genera_array_interi_crescenti()
    genera_tabelline()
    estrai_valori()
