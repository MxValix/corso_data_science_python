import pandas as pd
import matplotlib.pyplot as plt

def apertura_file():
    with open("text.txt", mode="a") as f:
        t = f.write("prova di scrittura")
        print(f)


#dizionario con chiave parola e valore numero occorrenze
def numero_occorrenze(key):
    frase = "Ma in Italia, o dolce Italia, la gente è più sincera, la vita è più vera."
    s = frase.split(key)
    dim = len(s)-1
    return dim


def lettura_file(nome_file, replace, replace_with):
    with open(nome_file) as f:
        str = f.read()
    s = str.replace(replace, replace_with).split(replace_with)
    return s


def crea_dizionario(s):
    dizionario = {}
    for parola in s:
        if parola in dizionario:
            dizionario[parola] +=1
        else:
            dizionario[parola] =1
    return dizionario


def open_csv(nome_file, dizionario):
    with open(nome_file, mode="w") as f:
        #f.write("parola,conteggio")
        for parola in dizionario.keys():
            f.write(str(parola) + "," + str(dizionario[parola]) + "\n")


if __name__ == '__main__':
    # print("Inserisci la parola da ricercare: ")
    # a = input()
    # n = numero_occorrenze(a)
    # print("Ci sono", n, "occorrenze della parola", a)
    #apertura_file()
    nome_file = "addresses.csv"
    replace = ","
    replace_with = " "
    s = lettura_file(nome_file, replace, replace_with)
    dizionario = crea_dizionario(s)
    nome_file = "parola.csv"
    open_csv(nome_file,dizionario)

    df = pd.read_csv(nome_file)
    print(df[""])
