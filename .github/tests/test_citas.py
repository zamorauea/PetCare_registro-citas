from src.citas import validar_fecha


def test_no_permite_fecha_pasada():
    assert validar_fecha("2020-01-01") == False
    