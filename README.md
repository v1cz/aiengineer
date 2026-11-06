# 🤖 TiendaBot

Hoy empiezas como **AI engineer junior** en TiendaBot, una tienda online.
El chatbot de atención al cliente está casi listo, pero quedan **3 tickets** abiertos.

**Tu misión:** cerrarlos y lanzar el bot. Tienes unos 30 minutos.

Te acompaña **Lucía**, desarrolladora senior. Te dará pistas y revisará tu código,
pero no te dará la solución: ¡el código lo escribes tú!

## Cómo se trabaja

1. **Lee el ticket** en la carpeta `tickets/`.
2. **Edita el archivo** que indica el ticket, en `chatbot/`. Busca el comentario `# TICKET-…`.
3. **Comprueba** escribiendo en la terminal:
   ```
   pytest
   ```
   ✅ = ticket terminado · ❌ = algo falla (te dice qué) · 🚧 = sin empezar
4. **¿Atascado/a?** Pregúntale a Lucía en el panel de **Claude** (icono en la barra lateral).

## Tickets

| # | Ticket | Archivo |
|---|---|---|
| 01 | [Limpiar y validar el mensaje](tickets/01-limpiar-y-validar.md) | `chatbot/validacion.py` |
| 02 | [Palabras prohibidas](tickets/02-palabras-prohibidas.md) | `chatbot/filtro.py` |
| 03 | [Detectar intención](tickets/03-detectar-intencion.md) | `chatbot/rutas.py` |

Cuando veas 🚀, habla con tu bot: `python -m chatbot.main`
