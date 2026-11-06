# TICKET-01 · Limpiar y validar el mensaje

**Archivo:** `chatbot/validacion.py` · **Tiempo:** ~10 min

## 💬 Lucía (Senior Dev)
> ¡Bienvenido/a! Los clientes escriben `"   HOLA   "`, pulsan Enter sin escribir nada
> o pegan textos enormes. Cada mensaje que mandamos a la IA **cuesta dinero**, así que
> antes hay que limpiarlo y comprobar que tiene sentido enviarlo.

## ✅ Criterios de aceptación
- [ ] `normalizar("  Hola TiendaBot  ")` devuelve `"hola tiendabot"`: sin espacios en los extremos y en minúsculas.
- [ ] `es_valido(mensaje)` devuelve `True` si el mensaje **no** está vacío **y** tiene como mucho `LONGITUD_MAXIMA` (500) caracteres.
- [ ] `pytest` muestra `TICKET-01 ✅ 4/4`.

## 🧠 Conceptos
`str.strip()`, `str.lower()`, `len()`, comparaciones (`<=`, `==`), `and` / `not`, `return`.

## 🏢 ¿Por qué importa en un trabajo real?
Validar lo que entra es la primera defensa de cualquier sistema: evita errores, abusos
y gasto. En IA, cada carácter que envías al modelo se paga.
