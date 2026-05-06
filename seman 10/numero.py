# ============================================================
#  CAPA MODELO — numero.py
#  Contiene los datos del dominio y la lógica de negocio.
#  No depende de la vista ni del controlador.
# ============================================================

class Numero:

    def __init__(self):
        self.__dato_numero: int = 0          # atributo privado

    # ── Getter ──────────────────────────────────────────────
    def get_numero(self) -> int:
        return self.__dato_numero

    # ── Setter ──────────────────────────────────────────────
    def set_numero(self, nuevo_numero: int) -> None:
        self.__dato_numero = nuevo_numero

    # ── Lógica de negocio ───────────────────────────────────
    def validar_numero(self, dato_numero: int) -> str:
        """
        Retorna una cadena con dos validaciones:
          • Si el número es par o impar.
          • Si el número es positivo, negativo o neutro (cero).
        """
        # Validación par / impar
        paridad = "par" if dato_numero % 2 == 0 else "impar"

        # Validación positivo / negativo / neutro
        if dato_numero > 0:
            signo = "positivo"
        elif dato_numero < 0:
            signo = "negativo"
        else:
            signo = "neutro (cero)"

        return f"El número {dato_numero} es {paridad} y {signo}."
