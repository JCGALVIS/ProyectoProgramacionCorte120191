def calcular_precio_producto(coste_producto):

    """
    num -> num
    print("Precio del producto = $", precioProducto)
    se ingresa un numero y se obtiene el precio del producto sumandole el 50% al coste

    :param coste_producto: valor numerico del coste
    :return: precio del producto
    >>> calcular_precio_producto(1000)
    1500.0
    >>> calcular_precio_producto(2000)
    3000.0
    >>> calcular_precio_producto(0)
    0.0
    """
    precioProducto = coste_producto * 0.5 + coste_producto

    return float(precioProducto)
    pass

def calcular_precio_servicio(cantidad_horas):

    """
    num -> float
    opera dos numeros para dar como resultado el precio del servicio
    :param cantidad_horas: Entero de las horas trabajadas
    :return: el precio del servicio
    >>> calcular_precio_servicio(4)
    400000.0
    >>> calcular_precio_servicio(5)
    500000.0
    """
    total=cantidad_horas*100000
    return float(total)
    pass

def calcular_precio_servicio_extras(cantidad_horas_extra, cantidad_horas):

    """
    num -> float
    opera dos numeros y suma lo que tiene la funcion anterior
    :param cantidad_horas: Entero con las horas extras trabajadas
    :return: EL precio del servicio con las horas extras
    >>> calcular_precio_servicio_extras(1,4)
    525000.0
    >>> calcular_precio_servicio_extras(2,1)
    350000.0
    """
    thoras_extra = ((cantidad_horas_extra * 100000) * 0.25) + (cantidad_horas_extra * 100000) + calcular_precio_servicio(cantidad_horas)

    return float(thoras_extra)
    pass


def calcular_costo_envio(kilometros):

    """
    num -> float
    opera dos numeros para dar como resultado el costo de envio
    :param kilometros: se ingresan la cantidad de kilometros recorridos
    :return: el costo del envio
    >>> calcular_costo_envio(1)
    115.0
    >>> calcular_costo_envio(0)
    0.0
    """
    tcosto_envio = kilometros * 115

    return float(tcosto_envio)
    pass

def calcular_precio_producto_fuera(coste_producto,kilometros):

    """
    num -> num
    :param coste_producto: Es el numero que representa costo del producto
    :param kilometros: los kilometros recorridos del envio
    :return: El precio del producto fuera de la ciudad
    >>> calcular_precio_producto_fuera(1000,1)
    1615.0
    >>> calcular_precio_producto_fuera(2000,1)
    3115.0
    """
    tprecio_producto_envio=calcular_precio_producto(coste_producto) + calcular_costo_envio(kilometros)

    return float(tprecio_producto_envio)
    pass

def calcular_iva_producto(coste_producto, tasa):

    """
    num -> num
    num -> num
    entran dos numers que multiplicados, dan el valor del iva
    :param coste_producto: Es el dato que corresponde al costo del producto
    :param tasa: El numero por el cual se multiplica el costo del producto y determinar el iva
    :return: El valor del iva
    >>> calcular_iva_producto(1000,0.19)
    190.0
    >>> calcular_iva_producto(1000,0)
    0
    """
    iva_final=coste_producto*tasa
    return float(iva_final)
    pass

def calcular_iva_servicio(cantidad_horas, tasa_iva):

    """
    num -> num
    num -> num
    entran dos numeros, que al ser operados, se obtiene el valor del iva de un servicio
    :param cantidad_horas: Numero de la cantidad de horas trabajadas
    :param tasa: Porcentaje para operar
    :return: el valor del iva del servicio
    >>> calcular_iva_servicio(4, 0.19)
    76000.0
    >>> calcular_iva_servicio(2, 0.16)
    32000.0
    """
    iva_servicio = calcular_precio_servicio(cantidad_horas)*tasa_iva
    return float(iva_servicio)
    pass

def calcular_iva_envio(kilometros, tasa_iva):

    """
    num -> num
    num -> num
    entran dos numeros para calcular el iva del envio
    :param kilometros: Cantidad de kilometros recorridos
    :param tasa: la tasa para multiplicar los kilometros
    :return: el iva del envio
    >>> calcular_iva_envio(1, 0.19)
    21.85
    >>> calcular_iva_envio(0, 0.19)
    0.0
    """
    iva_envio = calcular_costo_envio(kilometros) * tasa_iva
    return float(iva_envio)
    pass

def calcular_iva_servicio_fuera(cantidad_horas, tasa_iva):

    """
    num -> num
    num -> num
    entran dos numeros para poder calcular el iva del servicio
    :param cantidad_horas: numero de horas trabajadas
    :param tasa: porcentaje de iva
    :return: iva del servicio
    >>> calcular_iva_servicio_fuera(1,0.19)
    23750.0
    >>> calcular_iva_servicio_fuera(0,0.19)
    0.0
    """
    iva_servicio_fuera = ((calcular_precio_servicio(cantidad_horas) * 0.25) + calcular_precio_servicio(cantidad_horas)) * tasa_iva
    return iva_servicio_fuera
    pass

def calcular_recaudo_locales(coste_producto_1,coste_producto_2,coste_producto_3):

    """
    num -> num
    num -> num
    num -> num
    entran 3 numeros que sumados, dan el recaudo total
    :param coste_producto_1: costo del primer producto
    :param coste_producto_2: costo del segundo producto
    :param coste_producto_3: costo del tercer producto
    :return: recaudo total de los locales
    >>> calcular_recaudo_locales(1000,1500,2000)
    4500.0
    >>> calcular_recaudo_locales(0,1500,0)
    1500.0
    """
    recaudo_local = coste_producto_1 + coste_producto_2 + coste_producto_3

    return float(recaudo_local)
    pass

def calcular_recaudo_horas_extra(horas_1,horas_2,horas_3,horas_4):

    """
    num -> num
    num -> num
    num -> num
    num -> num
    Multiplica las horas por 100000 y le incrementa un 25% para después sumarla
    :param horas_1: Cantidad de horas uno
    :param horas_2: Cantidad de horas dos
    :param horas_3: Cantidad de horas tres
    :param horas_4: Cantidad de horas cuatro
    :return: La sumatoria de las horas extras
    >>> calcular_recaudo_horas_extra(3,4,5,6)
    2250000.0
    >>> calcular_recaudo_horas_extra(0,5,4,1)
    1250000.0
    """
    recaudo_extras = ((horas_1*100000)*0.25+(horas_1*100000))+((horas_2*100000)*0.25+(horas_2*100000))+((horas_3*100000)*0.25+(horas_3*100000))+((horas_4*100000)*0.25+(horas_4*100000))
    return recaudo_extras
    pass

def calcular_recaudo_mixto_local(coste_producto_1,coste_producto_2,horas_1,horas_2):
    """
    num -> num
    num -> num
    num -> num
    num -> num
    Multiplica el coste del producto por el 50% y suma el coste del producto, además las horas por 100000 y ls suma
    :param coste_producto_1: Valor del coste del producto uno
    :param coste_producto_2: Valor del coste del producto dos
    :param horas_1: Cantidad de horas trabajadas uno
    :param horas_2: Cantidad de horas trabajadas dos
    :return: La suma de las 4 cantidades
    >>> calcular_recaudo_mixto_local(1000,1500,1,1)
    253750.0
    >>> calcular_recaudo_mixto_local(2000,0,8,10)
    2253000.0
    """
    recaudo_mix = (coste_producto_1+(coste_producto_1*0.5))+(coste_producto_2+(coste_producto_2*0.5))+((horas_1*100000)*0.25+(horas_1*100000))+((horas_2*100000)*0.25+(horas_2*100000))
    return recaudo_mix
    pass
