"""PROVISTO · MercaBot. Ejecuta: python -m chatbot.main"""
from chatbot.validacion import normalizar, es_valido
from chatbot.filtro import cargar_palabras_prohibidas, contiene_palabra_prohibida
from chatbot.rutas import detectar_intencion
from chatbot.llm import preguntar


def main() -> None:
    prohibidas = cargar_palabras_prohibidas()
    # Comprobamos que los 3 tickets están hechos antes de abrir el chat.
    es_valido(normalizar(" hola "))
    contiene_palabra_prohibida("hola", prohibidas)
    detectar_intencion("hola")

    print("MercaBot · escribe 'salir' para terminar\n")
    while True:
        mensaje = normalizar(input("Tú: "))
        if mensaje == "salir":
            break
        if not es_valido(mensaje):
            print("MercaBot: Escribe un mensaje de hasta 500 caracteres, por favor.\n")
        elif contiene_palabra_prohibida(mensaje, prohibidas):
            print("MercaBot: Prefiero que hablemos con respeto 🙂\n")
        else:
            tema = detectar_intencion(mensaje)
            try:
                respuesta = preguntar(f"[Tema: {tema}] {mensaje}")
            except Exception:
                respuesta = "Lo siento, ahora no puedo responder. Inténtalo en un momento."
            print(f"MercaBot: {respuesta}\n")


if __name__ == "__main__":
    try:
        main()
    except NotImplementedError:
        print("🚧 Termina los tickets para lanzar MercaBot")
