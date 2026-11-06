# TICKET-03 · Detectar intención

**Archivo:** `chatbot/rutas.py` · **Tiempo:** ~10 min

## 💬 Lucía (Senior Dev)
> Casi todos los mensajes van de **pedidos**, **devoluciones** u **horario**. Si sabemos
> el tema, la IA responde mejor. Para la v1 nos basta con buscar palabras clave: ya están
> en el diccionario `PALABRAS_CLAVE`. Si un mensaje encaja en dos temas, como
> *"quiero devolver mi pedido"*, gana **devoluciones**, luego **pedidos**, luego **horario**.

## ✅ Criterios de aceptación
- [ ] `detectar_intencion("¿dónde está mi pedido?")` devuelve `"pedidos"`.
- [ ] Si no encaja en ningún tema, devuelve `"otro"`.
- [ ] Respeta la prioridad: devoluciones > pedidos > horario.
- [ ] Usa `PALABRAS_CLAVE` en vez de escribir los textos a mano.
- [ ] `pytest` muestra `TICKET-03 ✅ 4/4` y 🚀.

## 🧠 Conceptos
`dict` (leer un valor por su clave), el operador `in` con textos, `if / elif / else`.

## 🏢 ¿Por qué importa en un trabajo real?
Esto se llama *routing*: decidir qué camino sigue cada petición. Los sistemas de IA
reales combinan reglas baratas como esta con modelos, y guardar las palabras en un
diccionario permite cambiarlas sin tocar la lógica.
