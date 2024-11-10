

def soma(a: int , b: int):
    return a+b

def sub(a: int , b: int):
    return a-b

def multi(a: int , b: int):
    try:
        result = a*b
    except:
        raise Exception("Erro interno")
    return result

def div(a: int , b: int):
    return a/b
