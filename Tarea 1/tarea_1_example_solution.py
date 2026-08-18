"""Modulo con las funciones filtrar_vocales y encontrar_extremos.

Este archivo implementa las dos funciones solicitadas en la Tarea 1:
filtrar_vocales, que extrae vocales o consonantes de una cadena de
texto, y encontrar_extremos, que encuentra el valor minimo y maximo
de una lista de numeros. Ambas funciones validan sus parametros de
entrada y retornan codigos de error especificos cuando alguna
validacion falla.
"""

# Codigos de retorno esperados
# Caso de exito => 0

# Errores esperados metodo filtrar_vocales
# Error en caso de que cadena no sea un string => -100
# Error en caso de que cadena posea algo distinto a letras => -200
# Error en caso de que cadena sea un string vacio => -300
# Error en caso de que cadena sea mayor a 30 caracteres => -400
# Error en caso de que bandera no sea un booleano => -500

# Errores esperados metodo encontrar_extremos
# Error en caso de que el parametro no sea una lista => -600
# Error en caso de que la lista contenga elementos no numericos => -700
# Error en caso de que la lista este vacia => -800
# Error en caso de que la lista tenga mas de 15 elementos => -900

EXITO = 0

CADENA_NO_ES_STRING = -100
CADENA_CONTIENE_NO_LETRAS = -200
CADENA_VACIA = -300
CADENA_EXCEDE_LONGITUD = -400
BANDERA_NO_ES_BOOLEANO = -500

LISTA_NO_ES_LISTA = -600
LISTA_CONTIENE_NO_NUMERICOS = -700
LISTA_VACIA = -800
LISTA_EXCEDE_TAMANO = -900

LONGITUD_MAXIMA_CADENA = 30
TAMANO_MAXIMO_LISTA = 15
VOCALES = "aeiouAEIOU"


def filtrar_vocales(cadena, bandera):
    """Filtra las vocales o consonantes de una cadena de texto.

    Parametros de entrada:
        cadena (str): Texto del cual se desean extraer las vocales o
            las consonantes. Debe ser un string no vacio, compuesto
            unicamente por letras del abecedario, con una longitud
            maxima de 30 caracteres.
        bandera (bool): Indica que se debe filtrar de la cadena.
            Si es True, se filtran las vocales. Si es False, se
            filtran las consonantes.

    Retorna:
        tuple: Una tupla de dos elementos (estado, resultado).
            - estado (int): Codigo que indica si la funcion se
              ejecuto correctamente (0) o el tipo de error
              encontrado (ver codigos de retorno al inicio del
              archivo).
            - resultado (str o None): String filtrado (solo vocales
              o solo consonantes, manteniendo el orden original de
              aparicion) cuando la ejecucion es exitosa, o None
              cuando ocurre cualquier error de validacion.
    """
    # Se valida que el parametro 'cadena' sea efectivamente un
    # string. Se descarta explicitamente bool, ya que en Python
    # bool es subclase de int y no corresponde a un str de todas
    # formas, pero se deja explicito por claridad.
    if not isinstance(cadena, str):
        return CADENA_NO_ES_STRING, None

    # Se valida que la cadena no sea un string vacio. Esta
    # validacion se realiza antes de revisar si contiene solo
    # letras, ya que un string vacio no debe reportarse con el
    # error de "caracteres invalidos" (un string vacio no tiene
    # letras que validar).
    if len(cadena) == 0:
        return CADENA_VACIA, None

    # Se valida que la cadena contenga unicamente letras del
    # abecedario (sin numeros, espacios ni simbolos).
    if not cadena.isalpha():
        return CADENA_CONTIENE_NO_LETRAS, None

    # Se valida que la cadena no exceda la longitud maxima
    # permitida de 30 caracteres.
    if len(cadena) > LONGITUD_MAXIMA_CADENA:
        return CADENA_EXCEDE_LONGITUD, None

    # Se valida que el parametro 'bandera' sea de tipo booleano.
    if not isinstance(bandera, bool):
        return BANDERA_NO_ES_BOOLEANO, None

    # Si la bandera es True, se construye un string unicamente con
    # las vocales de la cadena original, respetando su orden.
    if bandera:
        resultado = "".join(
            letra for letra in cadena if letra in VOCALES
        )
    # Si la bandera es False, se construye un string unicamente con
    # las consonantes de la cadena original, respetando su orden.
    else:
        resultado = "".join(
            letra for letra in cadena if letra not in VOCALES
        )

    return EXITO, resultado


def encontrar_extremos(lista_numeros):
    """Encuentra el valor minimo y maximo de una lista de numeros.

    Parametros de entrada:
        lista_numeros (list): Lista de la cual se desea obtener el
            valor minimo y maximo. Debe ser una lista no vacia,
            compuesta unicamente por numeros (int o float), con un
            maximo de 15 elementos.

    Retorna:
        tuple: Una tupla de tres elementos
            (estado, minimo, maximo).
            - estado (int): Codigo que indica si la funcion se
              ejecuto correctamente (0) o el tipo de error
              encontrado (ver codigos de retorno al inicio del
              archivo).
            - minimo (int, float o None): Valor minimo encontrado
              en la lista cuando la ejecucion es exitosa, o None
              cuando ocurre cualquier error de validacion.
            - maximo (int, float o None): Valor maximo encontrado
              en la lista cuando la ejecucion es exitosa, o None
              cuando ocurre cualquier error de validacion.
    """
    # Se valida que el parametro de entrada sea efectivamente una
    # lista.
    if not isinstance(lista_numeros, list):
        return LISTA_NO_ES_LISTA, None, None

    # Se valida que todos los elementos de la lista sean numeros
    # (int o float). Se excluye explicitamente bool, ya que en
    # Python bool es subclase de int y no debe considerarse un
    # numero valido para este proposito.
    todos_numericos = all(
        isinstance(elemento, (int, float))
        and not isinstance(elemento, bool)
        for elemento in lista_numeros
    )
    if not todos_numericos:
        return LISTA_CONTIENE_NO_NUMERICOS, None, None

    # Se valida que la lista no este vacia.
    if len(lista_numeros) == 0:
        return LISTA_VACIA, None, None

    # Se valida que la lista no tenga mas de 15 elementos.
    if len(lista_numeros) > TAMANO_MAXIMO_LISTA:
        return LISTA_EXCEDE_TAMANO, None, None

    # Se calculan el valor minimo y el valor maximo de la lista.
    valor_minimo = min(lista_numeros)
    valor_maximo = max(lista_numeros)

    return EXITO, valor_minimo, valor_maximo
