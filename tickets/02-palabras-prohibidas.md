# TICKET-02 · Palabras prohibidas

**Archivo:** `chatbot/filtro.py` · **Tiempo:** ~10 min

## 💬 Lucía (Senior Dev)
> Legal no quiere que el bot conteste a insultos. La lista está en `data/bad_words.txt`
> y ya la cargamos en un `set`. También tienes `separar_palabras()`, que trocea un texto
> en palabras sin signos ni mayúsculas. Ojo: compara **palabras completas**, o acabarás
> bloqueando a quien escribe *"mi computadora no enciende"*.

## ✅ Criterios de aceptación
- [ ] `contiene_palabra_prohibida("eres un tonto", {"tonto"})` devuelve `True`.
- [ ] `"¡Eres un TONTO!"` también se bloquea.
- [ ] `"mi computadora no enciende"` **no** se bloquea.
- [ ] `pytest` muestra `TICKET-02 ✅ 4/4`.

## 🧠 Conceptos
Bucle `for` sobre una lista, `set`, el operador `in`, `return` dentro de un bucle.

## 🏢 ¿Por qué importa en un trabajo real?
Moderar contenido es parte de cualquier producto con usuarios. Y buscar en un `set` es
instantáneo aunque tenga millones de elementos; en una lista, no.
