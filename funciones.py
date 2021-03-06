def calcular_precio_producto(coste_producto):
    
    """
    num -> num
    se ingresa un numero y se obtiene el precio del producto sumandole el 50% al coste
    :param coste_producto: valor numerico del coste
    :return: precio del producto
    >>> calcular_precio_producto(1000)
    1500.0
    >>> calcular_precio_producto(2000)
    3000.0
    """
    if(coste_producto <= 0):
        return 'El costo del producto debe ser mayor a cero.'

    precioProducto = (coste_producto * 0.5) + coste_producto

    return precioProducto


def calcular_precio_servicio(cantidad_horas):
    """
    num -> float
    opera un numeros para dar como resultado el precio del servicio
    :param cantidad_horas: Entero de las horas trabajadas
    :return: el precio del servicio
    >>> calcular_precio_servicio(4)
    400000.0
    >>> calcular_precio_servicio(5)
    500000.0
    """

    if (cantidad_horas <= 0):
        return 'Las horas deben ser mayor a cero.'

    total = cantidad_horas * 100000
    return float(total)

def calcular_precio_servicio_extras(cantidad_horas):
    
    """
    num -> num
    opera dos numeros y suma lo que tiene la funcion anterior
    :param cantidad_horas: Entero con las horas extras trabajadas
    :return: EL precio del servicio con las horas extras
    >>> calcular_precio_servicio_extras(1)
    125000.0
    >>> calcular_precio_servicio_extras(2)
    250000.0
    """

    if (cantidad_horas == 0):
        return 'El servicio no genera horas extras.'

    if (cantidad_horas < 0):
        return 'Las horas deben ser mayor a cero.'

    precioServicio = calcular_precio_servicio(cantidad_horas)
    precioServicioExtras = (precioServicio * 0.25) + precioServicio

    return precioServicioExtras


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

    if (kilometros < 0):
        return 'El numero de kilometros debe ser mayor a cero.'

    return float(kilometros * 115)


def calcular_precio_producto_extra(coste_producto,kilometros):
    """
    num -> float
    se operan dos numeros para dar como resultado del costo de envio fuera
    
    :param coste_producto: Es el numero que representa costo del producto
    :param kilometros: los kilometros recorridos del envio
    :return: El precio del producto fuera de la ciudad
    >>> calcular_precio_producto_extra(1000,1)
    1615.0
    >>> calcular_precio_producto_extra(500,5)
    1325.0
    """

    if (coste_producto <= 0):
        return 'El costo del producto debe ser mayor a cero.'
    tprecio_producto_envio_fuera = calcular_precio_producto(coste_producto) + calcular_costo_envio(kilometros)

    return float(tprecio_producto_envio_fuera)


def calcular_iva_producto(coste_producto, tasa):
    """
    num -> num
    num -> num
    entran dos numers que multiplicados, dan el valor del iva
    :param coste_producto: Es el dato que corresponde al costo del producto
    :param tasa: El numero por el cual se multiplica el costo del producto y determinar el iva
    :return: El valor del iva
    >>> calcular_iva_producto(1000,0.19)
    285.0
    >>> calcular_iva_producto(1000,0)
    0.0
    """

    if (coste_producto <= 0):
        return 'El costo del producto debe ser mayor a cero.'

    iva_final = calcular_precio_producto(coste_producto) * tasa
    return float(iva_final)


def calcular_iva_servicio(cantidad_horas, tasa):
    """
    num -> num
    num -> num
    entran dos numeros, que al ser operados, se obtiene el valor del iva de un servicio
    :param cantidad_horas: Numero de la cantidad de horas trabajadas
    :param tasa: Porcentaje para operar
    :return: el valor del iva del servicio
    >>> calcular_iva_servicio(4, 0.19)
    76000.0
    """

    if (cantidad_horas <= 0):
        return 'El numero de horas debe ser mayor a cero.'

    iva_servicio = (calcular_precio_servicio(cantidad_horas)) * tasa
    return float(iva_servicio)

def calcular_iva_envio(kilometros, tasa):
    """
    num -> num
    num -> num
    entran dos numeros para calcular el iva del envio
    :param kilometros: Cantidad de kilometros recorridos
    :param tasa: la tasa para multiplicar los kilometros
    :return: el iva del envio
    >>> calcular_iva_envio(1,0.19)
    21.85
    >>> calcular_iva_envio(2,0.19)
    43.7
    """
    if(kilometros < 0):
        return 'El numero de kilometros no debe ser menor a cero.'

    iva_envio = calcular_costo_envio(kilometros) * tasa
    return float(iva_envio)

def calcular_iva_servicio_extra(cantidad_horas, tasa):

    """
    num -> num
    num -> num
    entran dos numeros para poder calcular el iva del servicio
    :param cantidad_horas: numero de horas trabajadas
    :param tasa: porcentaje de iva
    :return: iva del servicio
    >>> calcular_iva_servicio_extra(1,0.19)
    23750.0
    >>> calcular_iva_servicio_extra(3,0.19)
    71250.0
    """
    if (cantidad_horas <= 0):
        return 'El numero de horas no debe ser menor o igual a cero.'

    iva_servicio_fuera = ((calcular_precio_servicio(cantidad_horas) * 0.25) + calcular_precio_servicio(cantidad_horas)) * tasa
    return iva_servicio_fuera

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

    >>> calcular_recaudo_locales(3000,1500,800)
    5300.0
    
    """
    if (coste_producto_1<=0 or coste_producto_2<=0 or coste_producto_3<=0):
        return 'El costo del producto debe ser mayor a cero.'
    
    recaudo_local = coste_producto_1+coste_producto_2+coste_producto_3
    return float(recaudo_local)

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
    >>> calcular_recaudo_horas_extra(4,5,4,1)
    1750000.0
    """

    if (horas_1 <= 0 or horas_2 <= 0 or horas_3 <= 0 or horas_4 <= 0):
        return 'El numero de horas no debe ser menor o igual a cero.'

    recaudo_extras = ((horas_1*100000)*0.25+(horas_1*100000))+((horas_2*100000)*0.25+(horas_2*100000))+((horas_3*100000)*0.25+(horas_3*100000))+((horas_4*100000)*0.25+(horas_4*100000))
    return float(recaudo_extras)

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
    >>> calcular_recaudo_mixto_local(2000,1000,8,10)
    2254500.0
    """
    if (coste_producto_1 <= 0 or coste_producto_2 <= 0):
        return 'El costo del producto debe ser mayor a cero.'

    if (horas_1 <= 0 or horas_2 <= 0):
        return 'El numero de horas no debe ser menor o igual a cero.'


    recaudo_mix = (coste_producto_1+(coste_producto_1*0.5))+(coste_producto_2+(coste_producto_2*0.5))+((horas_1*100000)*0.25+(horas_1*100000))+((horas_2*100000)*0.25+(horas_2*100000))
    return float(recaudo_mix)
