
from string_utils import inverter_string, eh_palindromo

# Testes de inverter_string
def test_inverter_string():
    assert inverter_string("python") == "nohtyp"

def test_inverter_string_vazia():
    assert inverter_string("") == ""

def test_inverter_string_com_espacos():
    assert inverter_string("ola mundo") == "odnum alo"

# Testes de eh_palindromo
def test_eh_palindromo():
    assert eh_palindromo("arara") is True

def test_eh_palindromo_com_maiusculas():
    assert eh_palindromo("Ana") is True

def test_nao_eh_palindromo():
    assert eh_palindromo("python") is False

def test_eh_palindromo_com_espacos():
    assert eh_palindromo("roma me tem amor") is True

def test_eh_palindromo_com_texto_vazio():
    assert eh_palindromo("") is True
