def decorador_maisculo(function):
    def wrapper():
        func = function()
        cria_maiusculo = func.upper()
        return cria_maiusculo
    return wrapper

def diga_oi():
    return 'hello there'

funcao_decorada = decorador_maisculo(diga_oi)

print(funcao_decorada())

@decorador_maisculo
def diga_oi2():
    return 'hello there'

print(diga_oi2())