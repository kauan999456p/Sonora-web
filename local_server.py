#!/usr/bin/env python3
"""Servidor local mínimo para executar o Sonora em http://localhost."""
from __future__ import annotations

import os
import socket
import threading
import webbrowser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PORT_START = 8765
PORT_END = 8785


class SonoraHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def log_message(self, fmt: str, *args) -> None:
        # Mantém o terminal limpo: mostra apenas erros HTTP.
        if args and str(args[0]).startswith(("4", "5")):
            super().log_message(fmt, *args)


def build_server() -> ThreadingHTTPServer:
    last_error = None
    for port in range(PORT_START, PORT_END + 1):
        try:
            server = ThreadingHTTPServer(("127.0.0.1", port), SonoraHandler)
            server.daemon_threads = True
            return server
        except OSError as exc:
            last_error = exc
    raise RuntimeError(f"Não consegui encontrar uma porta livre entre {PORT_START} e {PORT_END}.") from last_error


def main() -> None:
    os.chdir(ROOT)
    server = build_server()
    url = f"http://127.0.0.1:{server.server_port}/"
    print("=" * 58)
    print(" SONORA WEB - SERVIDOR LOCAL")
    print("=" * 58)
    print(f"Endereço: {url}")
    print("Deixe esta janela aberta enquanto usa o Sonora.")
    print("Para encerrar, pressione Ctrl+C.")
    threading.Timer(0.8, lambda: webbrowser.open(url)).start()
    try:
        server.serve_forever(poll_interval=0.5)
    except KeyboardInterrupt:
        print("\nEncerrando o Sonora...")
    finally:
        server.shutdown()
        server.server_close()


if __name__ == "__main__":
    main()
