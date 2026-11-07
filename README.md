# 🤖 MercaBot

Hoy empiezas como **AI engineer junior** en MercaBot, una tienda online.
El chatbot de atención al cliente está casi listo, pero quedan **3 tickets** abiertos.

**Tu misión:** cerrarlos y lanzar el bot. Tienes unos 30 minutos.

Te acompaña **Lucía**, desarrolladora senior, en el panel de la derecha (✳ Claude Code).
Te dará pistas y revisará tu código, pero no te dará la solución: ¡el código lo escribes tú!

## Cómo funciona MercaBot

Cada mensaje de un cliente pasa por 4 pasos, en orden. Si un paso lo para,
el mensaje **no llega a la IA**, y no gastamos dinero en él.

```
Cliente: "  ¿Dónde está mi PEDIDO?  "
   │
   ▼
1. validacion.py  Limpia el mensaje        → "¿dónde está mi pedido?"   TICKET-01
   │              ¿Vacío o muy largo?      → se para aquí
   ▼
2. filtro.py      ¿Tiene insultos?         → se para aquí               TICKET-02
   │
   ▼
3. rutas.py       ¿De qué tema es?         → "pedidos"                  TICKET-03
   │
   ▼
4. llm.py         La IA responde, sabiendo el tema                      ya hecho
```

`main.py` une los 4 pasos en un chat (ya hecho). **Tú escribes los pasos 1, 2 y 3.**

## Cómo se trabaja

1. **Lee el ticket** en la carpeta `tickets/`.
2. **Edita el archivo** que indica el ticket, en `chatbot/`. Busca el comentario `# TICKET-…`.
3. **Comprueba** escribiendo en la terminal:
   ```
   pytest
   ```
   ✅ = ticket terminado · ❌ = algo falla (te dice qué) · 🚧 = sin empezar
4. **¿Te atascas?** Pregúntale a Lucía en el panel de la derecha.

## Tickets

| # | Ticket | Archivo |
|---|---|---|
| 01 | [Limpiar y validar el mensaje](tickets/01-limpiar-y-validar.md) | `chatbot/validacion.py` |
| 02 | [Palabras prohibidas](tickets/02-palabras-prohibidas.md) | `chatbot/filtro.py` |
| 03 | [Detectar intención](tickets/03-detectar-intencion.md) | `chatbot/rutas.py` |

## 🏁 Al terminar

Cuando `pytest` muestre 🚀, habla con tu bot:
```
python -m chatbot.main
```
Escribe como un cliente. Prueba también un mensaje vacío o un insulto: ¿qué paso lo para?
Para salir del chat, escribe `salir` (o pulsa `Ctrl+C`).

Cuando acabes, cierra la pestaña: el Codespace se apaga solo al rato de no usarlo.
