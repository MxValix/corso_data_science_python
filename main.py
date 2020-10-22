def is_even(n)->int:
    if n%2==0:
        return True
    else:
        return False


def is_div(a, b):
    return a % b == 0

if __name__ == '__main__':
    print("inserisci il numero di cui vuoi sapere se è pari o dispari: ")
    a = int(input());
    is_even = is_even(a)
    response = "il numero è "
    if (is_even):
        response += "pari e "
    else:
        response += "dispari e "
    print("inserisci il divisore: ")
    b = int(input())
    is_div = is_div(a, b)
    if (is_div):
        response += "divisibile per "
    else:
        response += "non è divisibile per "
    print(response, b)
