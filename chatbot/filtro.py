"""TICKET-02 · Palabras prohibidas. Lee tickets/02-palabras-prohibidas.md"""

SIGNOS: str = ".,;:!¡?¿"


def separar_palabras(texto: str) -> list[str]:
    """PROVISTO · "¡Hola, qué tal!" -> ["hola", "qué", "tal"] (sin signos)."""
    palabras = []
    actual = ""
    for letra in texto + " ":
        if letra == " ":
            if actual.strip(SIGNOS) != "":
                palabras.append(actual.strip(SIGNOS).lower())
            actual = ""
        else:
            actual = actual + letra
    return palabras


def cargar_palabras_prohibidas(ruta: str = "data/bad_words.txt") -> set[str]:
    """PROVISTO · Lee el archivo (una palabra por línea) y devuelve un set."""
    prohibidas = set()
    with open(ruta, encoding="utf-8") as archivo:
        for linea in archivo:
            if linea.strip() != "" and linea[0] != "#":
                prohibidas.add(linea.strip().lower())
    return prohibidas


def contiene_palabra_prohibida(mensaje: str, prohibidas: set[str]) -> bool:
    """True si alguna palabra del mensaje está en el set `prohibidas`.

    Ejemplo: contiene_palabra_prohibida("eres un tonto", {"tonto"}) -> True
    """
    # TICKET-02: recorre separar_palabras(mensaje) y comprueba cada palabra con `in`.
    raise NotImplementedError("TICKET-02")
