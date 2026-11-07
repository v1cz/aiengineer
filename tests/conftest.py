"""Salida de pytest en español: una línea por ticket.

- `pytest`            -> solo la lista de tickets (modo alumno).
- `pytest -v ...`     -> salida normal de pytest + la lista al final (modo tutor).
"""
import sys

import pytest

TICKETS = {
    "01": "Limpiar y validar el mensaje",
    "02": "Palabras prohibidas",
    "03": "Detectar intención",
}
ANCHO = max(len(titulo) for titulo in TICKETS.values()) + 14

_resultados: dict[str, list] = {}  # ticket -> [(estado, frase), ...]
_errores: dict[str, str] = {}      # ticket -> error al importar el código del alumno
_modo_alumno = False


def _ticket(nodeid: str):
    archivo = nodeid.split("::")[0].split("/")[-1]  # test_01_xxx.py
    numero = archivo[5:7]
    return numero if archivo.startswith("test_") and numero in TICKETS else None


@pytest.hookimpl(trylast=True)
def pytest_configure(config):
    global _modo_alumno
    _modo_alumno = config.option.verbose < 0
    if _modo_alumno:
        reporter = config.pluginmanager.getplugin("terminalreporter")
        if reporter is not None:
            config.pluginmanager.unregister(reporter)  # quitamos la salida normal


def pytest_collectreport(report):
    ticket = _ticket(report.nodeid)
    if report.failed and ticket:
        lineas = [l[1:].strip() for l in str(report.longrepr).splitlines() if l.startswith("E ")]
        _errores[ticket] = lineas[-1] if lineas else "no se pudo importar el archivo"


@pytest.hookimpl(wrapper=True)
def pytest_runtest_makereport(item, call):
    report = yield
    ticket = _ticket(item.nodeid)
    if ticket and (report.when == "call" or report.failed):
        if report.passed:
            estado = "ok"
        elif call.excinfo is not None and call.excinfo.errisinstance(NotImplementedError):
            estado = "pendiente"
        else:
            estado = "fallo"
        frase = (item.function.__doc__ or item.name).strip()
        _resultados.setdefault(ticket, []).append((estado, frase))
    return report


def _lineas() -> list[str]:
    lineas = []
    listos = 0
    for ticket, titulo in TICKETS.items():
        cabecera = f"TICKET-{ticket} · {titulo}".ljust(ANCHO)
        resultados = _resultados.get(ticket, [])
        if ticket in _errores:
            lineas.append(f"{cabecera} 💥 tu código tiene un error: {_errores[ticket]}")
            continue
        if not resultados:
            continue  # este ticket no se ejecutó (p. ej. pytest de un solo archivo)
        estados = [estado for estado, _ in resultados]
        ok, total = estados.count("ok"), len(estados)
        if ok == total:
            listos += 1
            lineas.append(f"{cabecera} ✅ {ok}/{total}")
        elif estados.count("pendiente") == total:
            lineas.append(f"{cabecera} 🚧 sin empezar")
        else:
            primer_fallo = [frase for estado, frase in resultados if estado != "ok"][0]
            lineas.append(f"{cabecera} ❌ {ok}/{total}  → {primer_fallo}")
    if listos == len(TICKETS):
        lineas.append("")
        lineas.append("🚀 ¡MercaBot listo para lanzar! Prueba: python -m chatbot.main")
    return lineas


def pytest_sessionfinish(session):
    if _modo_alumno:
        sys.__stdout__.write("\n".join(_lineas()) + "\n")


def pytest_terminal_summary(terminalreporter):
    if not _modo_alumno:
        terminalreporter.write_sep("=", "MercaBot")
        for linea in _lineas():
            terminalreporter.write_line(linea)
