from chatbot.filtro import contiene_palabra_prohibida

PROHIBIDAS = {"tonto", "puta"}


def test_bloquea_insulto():
    '''"eres un tonto" debería bloquearse'''
    assert contiene_palabra_prohibida("eres un tonto", PROHIBIDAS) is True


def test_bloquea_con_signos_y_mayusculas():
    '''"¡Eres un TONTO!" debería bloquearse (pista: separar_palabras ya quita signos y mayúsculas)'''
    assert contiene_palabra_prohibida("¡Eres un TONTO!", PROHIBIDAS) is True


def test_compara_palabras_completas():
    '''"mi computadora no enciende" NO debería bloquearse: hay que comparar palabras completas'''
    assert contiene_palabra_prohibida("mi computadora no enciende", PROHIBIDAS) is False


def test_mensaje_limpio():
    '''"dónde está mi pedido" (o un mensaje vacío) NO debería bloquearse'''
    assert contiene_palabra_prohibida("dónde está mi pedido", PROHIBIDAS) is False
    assert contiene_palabra_prohibida("", PROHIBIDAS) is False
