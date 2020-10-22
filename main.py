def is_even(n)->int:
    if n%2==0:
        return True
    else:
        return False



if __name__ == '__main__':
    is_even = is_even(int(input()))
    response = "il numero è "
    if (is_even):
        response += "pari"
    else:
        response += "dispari"
    print(response)
