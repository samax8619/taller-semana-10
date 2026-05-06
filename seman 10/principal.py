# ============================================================
#  PUNTO DE ENTRADA — principal.py
#  Solo instancia el Controlador y lanza el flujo principal.
# ============================================================

from controlador import Controlador


class Principal:

    @staticmethod
    def main() -> None:
        ctrl = Controlador()
        ctrl.tomar_numero()       # 1. Pedir dato al usuario
        ctrl.imprimir_numero()    # 2. Validar y mostrar resultado


# ── Ejecución ───────────────────────────────────────────────
if __name__ == "__main__":
    Principal.main()
