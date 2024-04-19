#Descuento fijo
def descuento_fijo(price):
    result = 0
    if price > 20:
        result = price - 20
    else:
        result = "No se puede aplicar el descuento. Precio menor a 20€"
    return result


#Descuentos porcentuales
def descuento_5(price):
    return price * .95

def descuento_10(price):
    return price * .9

def descuento_15(price):
    return price * .85

def descuento_20(price):
    return price * .8


#Descuentos escalonados
def descuento_escalonado(price):
    if price > 200:
        result = price * .8
    elif price <= 200 and price >= 100:
        result = price * .9
    elif price < 100 and price > 0:
        result = price * .95
    else:
        result = "Descuento no aplicable. Precio inferior o igual a 0."
    return result


#Descuentos aplicados
def aplicarDescuentos(priceList, func):
    result = []
    for element in priceList:
        discount = func(element)
        result.append(discount)
    return result
