"""TICKET-03 · Detectar intención. Lee tickets/03-detectar-intencion.md"""

# Si el mensaje contiene este texto, es de ese tema. "devol" vale para devolver, devolución...
PALABRAS_CLAVE: dict[str, str] = {
    "devoluciones": "devol",
    "pedidos": "pedido",
    "horario": "horario",
}


def detectar_intencion(mensaje: str) -> str:
    """Devuelve "devoluciones", "pedidos", "horario" u "otro" (en ese orden de prioridad).

    Ejemplo: "quiero devolver mi pedido" -> "devoluciones"
    """
    # TICKET-03: usa if / elif / else, el operador `in` y el diccionario PALABRAS_CLAVE.
    raise NotImplementedError("TICKET-03")
