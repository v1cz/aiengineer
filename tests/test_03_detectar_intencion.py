from chatbot.rutas import detectar_intencion


def test_pedidos():
    '''"¿dónde está mi pedido?" debería ser "pedidos"'''
    assert detectar_intencion("¿dónde está mi pedido?") == "pedidos"


def test_horario():
    '''"¿cuál es vuestro horario?" debería ser "horario"'''
    assert detectar_intencion("¿cuál es vuestro horario?") == "horario"


def test_otro():
    '''"¿tenéis camisetas azules?" debería ser "otro"'''
    assert detectar_intencion("¿tenéis camisetas azules?") == "otro"


def test_prioridad():
    '''"quiero devolver mi pedido" debería ser "devoluciones" (devoluciones va antes que pedidos)'''
    assert detectar_intencion("quiero devolver mi pedido") == "devoluciones"
