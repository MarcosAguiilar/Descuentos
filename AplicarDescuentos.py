import descuentos

precios = [0, 10, 50, 150, 250, 350]
# Aplicar descuento fijo

print(descuentos.aplicarDescuentos(precios, descuentos.descuento_fijo))
# Aplicar un descuento del 5%
print(descuentos.aplicarDescuentos(precios, descuentos.descuento_5))
# Aplicar un descuento del 15%
print(descuentos.aplicarDescuentos(precios, descuentos.descuento_15))
# Aplicar descuento escalonado generado con porcentajes personalizados
print(descuentos.aplicarDescuentos(precios, descuentos.descuento_escalonado))