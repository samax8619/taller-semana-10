# ============================================================
#  CAPA CONTROLADOR — controlador.py
#  Intermediario entre la Vista y el Modelo.
#  Coordina operaciones; no almacena datos propios.
# ============================================================

from vista_formulario import Vista_formulario
from numero import Numero


class Controlador:

    def __init__(self):
        # Composición: el controlador crea (y posee) sus dependencias
        self.obj_vista:   Vista_formulario = Vista_formulario()
        self.obj_numero:  Numero           = Numero()

    # ── Flujo: pedir número ─────────────────────────────────
    def tomar_numero(self) -> None:
        """
        Solicita el número a través de la vista y lo
        almacena en el modelo.
        """
        numero_ingresado = self.obj_vista.pedir_numero()
        self.obj_numero.set_numero(numero_ingresado)

    # ── Flujo: validar e imprimir ───────────────────────────
    def imprimir_numero(self) -> None:
        """
        Obtiene el número del modelo, solicita la validación
        y delega la impresión a la vista.
        """
        numero = self.obj_numero.get_numero()
        resultado = self.obj_numero.validar_numero(numero)

        self.obj_vista.imprimir_numero(numero)
        self.obj_vista.imprimir_mensaje(resultado)
