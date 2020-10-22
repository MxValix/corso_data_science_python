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


def lettura_file():
    with open("text.txt") as f:
        str = f.read()
    s = str.replace(",", " ").split(" ")
    return s


def crea_dizionario(s):
    dizionario = {}
    for parola in s:
        if parola in dizionario:
            dizionario[parola] +=1
        else:
            dizionario[parola] =1
    return dizionario


if __name__ == '__main__':
    # print("Inserisci la parola da ricercare: ")
    # a = input()
    # n = numero_occorrenze(a)
    # print("Ci sono", n, "occorrenze della parola", a)
    #apertura_file()
    s = lettura_file()
    print(crea_dizionario(s))
