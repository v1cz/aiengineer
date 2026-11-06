from chatbot.validacion import es_valido, normalizar


def test_normalizar():
    '''"  Hola TiendaBot  " debería quedar "hola tiendabot" (sin espacios en los extremos y en minúsculas)'''
    assert normalizar("  Hola TiendaBot  ") == "hola tiendabot"
    assert normalizar("\n¿Dónde está mi PEDIDO?\t") == "¿dónde está mi pedido?"


def test_vacio_no_es_valido():
    '''un mensaje vacío ("") no debería ser válido'''
    assert es_valido("") is False


def test_mensaje_normal_es_valido():
    '''"hola" y un mensaje de exactamente 500 caracteres deberían ser válidos'''
    assert es_valido("hola") is True
    assert es_valido("a" * 500) is True


def test_mensaje_largo_no_es_valido():
    '''un mensaje de 501 caracteres no debería ser válido (el máximo es 500)'''
    assert es_valido("a" * 501) is False
