import descuentos


#Prueba de descuento fijo
def test_descuento_fijo():
    assert descuentos.descuento_fijo(21) == 1
    assert descuentos.descuento_fijo(20) == "No se puede aplicar el descuento. Precio menor a 20€"


#Preuba de descuentos porcentuales
def test_descuento_5():
    assert descuentos.descuento_5(1) == 0.95
def test_descuento_10():
    assert descuentos.descuento_10(1) == 0.9
def test_descuento_15():
    assert descuentos.descuento_15(1) == 0.85
def test_descuento_20():
    assert descuentos.descuento_20(1) == 0.8


#Prueba descuentos escalonados
def test_descuentos_escalonados():
    assert descuentos.descuento_escalonado(400) == 320
    assert descuentos.descuento_escalonado(100) == 90
    assert descuentos.descuento_escalonado(50) == 47.5
    assert descuentos.descuento_escalonado(0) == "Descuento no aplicable. Precio inferior o igual a 0."

    