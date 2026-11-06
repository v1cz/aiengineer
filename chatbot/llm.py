"""PROVISTO · Envía un mensaje al modelo de IA y devuelve su respuesta."""
import anthropic

MODELO: str = "anthropic/claude-haiku-5.5"
SISTEMA: str = (
    "Eres el agente de atención al cliente de TiendaBot, una tienda online. "
    "Responde en español, con amabilidad y en 2 o 3 frases."
)


def preguntar(mensaje: str) -> str:
    cliente = anthropic.Anthropic()  # la dirección y la clave vienen del entorno
    respuesta = cliente.messages.create(
        model=MODELO, max_tokens=300, system=SISTEMA,
        thinking={"type": "disabled"},  # respuesta directa, sin "pensar" antes
        messages=[{"role": "user", "content": mensaje}],
    )
    return respuesta.content[0].text
