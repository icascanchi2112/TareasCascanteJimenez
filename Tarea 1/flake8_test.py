"""Modulo de practica utilizado para el ejercicio de branches.

Este archivo contiene una funcion simple cuyo unico proposito es
servir de base para el punto de la tarea en el que se debe crear un
commit con errores identificables por flake8, y posteriormente otro
commit que los corrija.
"""


def calcular_area_rectangulo(base, altura):
    """Calcula el area de un rectangulo.

    Parametros:
        base (float): longitud de la base del rectangulo.
        altura (float): longitud de la altura del rectangulo.

    Retorna:
        float: area resultante de multiplicar base por altura.
    """
    resultado = base * altura
    return resultado
