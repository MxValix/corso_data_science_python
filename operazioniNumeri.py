def is_even(n)->int:
    if n%2==0:
        return True
    else:
        return False


def is_div(a, b):
    return a % b == 0


def is_primo(n)->bool:
    for i in range(2, n-1):
        if is_div(n, i):
            return False;
        return True


def gen_primi(n):
    for i in range(2, n):
        if is_primo(i):
            yield i

            
def operazioni_Numeri():
    print(is_primo(7))
    for i in gen_primi(10):
        print(i)
