def inverter_string(texto):
    return texto[::-1]

def eh_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    return texto == texto[::-1]
