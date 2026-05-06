# ============================================================
#  CAPA VISTA — vista_formulario.py
#  Muestra información al usuario y recibe la entrada.
#  No contiene lógica de negocio.
# ============================================================

class Vista_formulario:

    def __init__(self):
        self.titulo: str               = "=== Programa de Números ==="
        self.pregunta_campo_numero: str = "Ingrese un número entero: "
        self.campo_dato_numero: int    = 0

    # ── Entrada ─────────────────────────────────────────────
    def pedir_numero(self) -> int:
        """Muestra el formulario y retorna el número ingresado por el usuario."""
        print(self.titulo)
        try:
            self.campo_dato_numero = int(input(self.pregunta_campo_numero))
        except ValueError:
            self.campo_dato_numero = 0
            print("[Vista] Entrada inválida. Se asignó 0 por defecto.")
        return self.campo_dato_numero

    # ── Salida ──────────────────────────────────────────────
    def imprimir_mensaje(self, dato_mensaje: str) -> None:
        """Imprime cualquier mensaje de texto al usuario."""
        print(dato_mensaje)

    def imprimir_numero(self, dato_numero: int) -> None:
        """Imprime el número almacenado/procesado."""
        print(f"Número registrado: {dato_numero}")
