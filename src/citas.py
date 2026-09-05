from datetime import datetime


def validar_fecha(fecha):
    try:
        fecha_ingresada = datetime.strptime(fecha, "%Y-%m-%d").date()
        fecha_actual = datetime.now().date()

        return fecha_ingresada >= fecha_actual
    except ValueError:
        return False