from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Calcular_el_promedio_de_edad_de_todos_los_caninos__UseCase:

    pass


class Calcular_el_numero_de_ejemplares_por_raza__UseCase:

    pass


class Buscar_un_ejemplar_por_su_nombre__UseCase:

    pass


class Desplazarse_hasta_el_ultimo_ejemplar__UseCase:

    pass


class Desplazarse_hasta_el_primer_ejemplar_UseCase:

    pass


class Regresar_hacia_el_anterior_ejemplar__UseCase:

    pass


class Avanzar_hacia_el_siguiendo_ejemplar__UseCase:

    pass


class Visualizar_hoja_de_vida_de_cada_perrito__UseCase:

    pass


class Usuario_Actor:

    pass





class String_pNombre__String_pRaza_int_pEdad_int_pPeso__int_pAltura_String_pObservaciones2:

    pass


class Int2:

    pass


class String_pNombre__String_pRaza_int_pEdad_int_pPeso__int_pAltura_String_pObservaciones:

    pass


class Int:

    pass


class double:

    pass


class void:

    pass


class Empresa:

    def __init__(self, ejemplaresCaninos: str):
        self.ejemplaresCaninos = ejemplaresCaninos
        
        pass
    @property
    def ejemplaresCaninos(self):
        return self.__ejemplaresCaninos
    @ejemplaresCaninos.setter
    def ejemplaresCaninos(self, ejemplaresCaninos: str):
        self.__ejemplaresCaninos = ejemplaresCaninos



class Canino:

    def __init__(self, nombre: str, raza: str, edad: Int, peso: Int, altura: Int, observaciones: str):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.altura = altura
        self.observaciones = observaciones
        
        pass
    @property
    def raza(self):
        return self.__raza
    @raza.setter
    def raza(self, raza: str):
        self.__raza = raza

    @property
    def peso(self):
        return self.__peso
    @peso.setter
    def peso(self, peso: Int):
        self.__peso = peso

    @property
    def observaciones(self):
        return self.__observaciones
    @observaciones.setter
    def observaciones(self, observaciones: str):
        self.__observaciones = observaciones

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def altura(self):
        return self.__altura
    @altura.setter
    def altura(self, altura: Int):
        self.__altura = altura

    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self, edad: Int):
        self.__edad = edad

