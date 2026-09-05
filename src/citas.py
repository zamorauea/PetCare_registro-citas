from datetime import date


def validar_fecha(fecha):
    fecha_cita = date.fromisoformat(fecha)
    return fecha_cita >= date.today()