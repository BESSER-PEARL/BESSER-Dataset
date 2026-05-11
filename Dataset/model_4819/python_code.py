from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class AttributeType(Enum):
    primaryKey = "primaryKey"
    ordinary = "ordinary"
class TipoModelElementEntity(Enum):
    entity = "entity"
    relation = "relation"
class NombreCampo(Enum):
    ID = "ID"
    ESTADO_TRANSACCION = "ESTADO_TRANSACCION"
    HORA = "HORA"
    TIPO = "TIPO"
    DESCRIPCION = "DESCRIPCION"
    CATEGORIA = "CATEGORIA"
    VALOR = "VALOR"
    CADENA_TRAMA = "CADENA_TRAMA"
    NUMERO_MOVIL = "NUMERO_MOVIL"
    FECHA = "FECHA"
    CEDULA_CONDUCTOR = "CEDULA_CONDUCTOR"
    CONDUCTOR = "CONDUCTOR"
    TOTAL = "TOTAL"
    TOTAL_RECAUDO_BRUTO = "TOTAL_RECAUDO_BRUTO"
    TOTAL_RECAUDO_NETO = "TOTAL_RECAUDO_NETO"
    TOTAL_DEPOSITO = "TOTAL_DEPOSITO"
    TOTAL_GASTOS = "TOTAL_GASTOS"
    LIQUIDADO = "LIQUIDADO"
    USUARIO = "USUARIO"
    NOMBRE_PERSONA = "NOMBRE_PERSONA"
    APELLIDO = "APELLIDO"
    CEDULA = "CEDULA"
    HORA_MODIFICACION = "HORA_MODIFICACION"
    NOMBRE = "NOMBRE"
    REGISTRO = "REGISTRO"
    TOTAL_RECAUDO_TARIFA = "TOTAL_RECAUDO_TARIFA"
    REGISTRO_RECAUDO = "REGISTRO_RECAUDO"
    COSTO_TARIFA = "COSTO_TARIFA"
    RUTA_DESPACHO = "RUTA_DESPACHO"
    HORA_DESPACHO = "HORA_DESPACHO"
    REGISTRO_CONSOLIDADO = "REGISTRO_CONSOLIDADO"
    TOTAL_RECAUDO_RUTO = "TOTAL_RECAUDO_RUTO"
    TOTAL_RECAUDO_DESPACHO = "TOTAL_RECAUDO_DESPACHO"
    ESTADO_CONSOLIDADO = "ESTADO_CONSOLIDADO"
    ESTADO_IMPRESION = "ESTADO_IMPRESION"
    default = "default"
class Type(Enum):
    string = "string"
    int = "int"
    float = "float"
    date = "date"
class Multiplicity(Enum):
    one_to_many = "one_to_many"
    many_to_one = "many_to_one"
    one_to_one = "one_to_one"


############################################
# Definition of Classes
############################################

class ElementoConsulta:

    pass
class gestionmodelosconsultas_cotracir_Consolidado(ElementoConsulta):

    pass
class gestionmodelosconsultas_cotracir_Detallado(ElementoConsulta):

    pass
class gestionmodelosconsultas_cotracir_Propietario(ElementoConsulta):

    pass
class gestionmodelosconsultas_cotracir_Trama(ElementoConsulta):

    pass
class gestionmodelosconsultas_cotracir_Transaccion(ElementoConsulta):

    pass
class gestionmodelosconsultas_cotracir_Planilla(ElementoConsulta):

    pass
class gestionmodelosconsultas_resultcotracir_NewClass:

    pass
class gestionmodelosconsultas_resultset_ResultElement(ABC):

    pass
class ElementoModeloResultado:

    pass
class gestionmodelosconsultas_resultcotracir_Transaccion(ElementoModeloResultado):

    def __init__(self, ESTADO_TRANSACCION: str, HORA: str, TIPO: str, DESCRIPCION: str, CATEGORIA: str, ID: str, VALOR: str):
        self.ESTADO_TRANSACCION = ESTADO_TRANSACCION
        self.HORA = HORA
        self.TIPO = TIPO
        self.DESCRIPCION = DESCRIPCION
        self.CATEGORIA = CATEGORIA
        self.ID = ID
        self.VALOR = VALOR
        
        pass
    @property
    def ESTADO_TRANSACCION(self):
        return self.__ESTADO_TRANSACCION

    @ESTADO_TRANSACCION.setter
    def ESTADO_TRANSACCION(self, ESTADO_TRANSACCION: str):
        self.__ESTADO_TRANSACCION = ESTADO_TRANSACCION


    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID


    @property
    def HORA(self):
        return self.__HORA

    @HORA.setter
    def HORA(self, HORA: str):
        self.__HORA = HORA


    @property
    def VALOR(self):
        return self.__VALOR

    @VALOR.setter
    def VALOR(self, VALOR: str):
        self.__VALOR = VALOR


    @property
    def CATEGORIA(self):
        return self.__CATEGORIA

    @CATEGORIA.setter
    def CATEGORIA(self, CATEGORIA: str):
        self.__CATEGORIA = CATEGORIA


    @property
    def DESCRIPCION(self):
        return self.__DESCRIPCION

    @DESCRIPCION.setter
    def DESCRIPCION(self, DESCRIPCION: str):
        self.__DESCRIPCION = DESCRIPCION


    @property
    def TIPO(self):
        return self.__TIPO

    @TIPO.setter
    def TIPO(self, TIPO: str):
        self.__TIPO = TIPO


class gestionmodelosconsultas_resultcotracir_Propietario(ElementoModeloResultado):

    def __init__(self, ID: str, NOMBRE: str, CEDULA: str):
        self.ID = ID
        self.NOMBRE = NOMBRE
        self.CEDULA = CEDULA
        
        pass
    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID


    @property
    def CEDULA(self):
        return self.__CEDULA

    @CEDULA.setter
    def CEDULA(self, CEDULA: str):
        self.__CEDULA = CEDULA


    @property
    def NOMBRE(self):
        return self.__NOMBRE

    @NOMBRE.setter
    def NOMBRE(self, NOMBRE: str):
        self.__NOMBRE = NOMBRE


class gestionmodelosconsultas_resultcotracir_Detallado(ElementoModeloResultado):

    def __init__(self, ID: str, NOMBRE: str, REGISTRO: str, TOTAL_RECAUDO_TARIFA: str, REGISTRO_RECAUDO: str, COSTO_TARIFA: str):
        self.ID = ID
        self.NOMBRE = NOMBRE
        self.REGISTRO = REGISTRO
        self.TOTAL_RECAUDO_TARIFA = TOTAL_RECAUDO_TARIFA
        self.REGISTRO_RECAUDO = REGISTRO_RECAUDO
        self.COSTO_TARIFA = COSTO_TARIFA
        
        pass
    @property
    def REGISTRO(self):
        return self.__REGISTRO

    @REGISTRO.setter
    def REGISTRO(self, REGISTRO: str):
        self.__REGISTRO = REGISTRO


    @property
    def REGISTRO_RECAUDO(self):
        return self.__REGISTRO_RECAUDO

    @REGISTRO_RECAUDO.setter
    def REGISTRO_RECAUDO(self, REGISTRO_RECAUDO: str):
        self.__REGISTRO_RECAUDO = REGISTRO_RECAUDO


    @property
    def NOMBRE(self):
        return self.__NOMBRE

    @NOMBRE.setter
    def NOMBRE(self, NOMBRE: str):
        self.__NOMBRE = NOMBRE


    @property
    def COSTO_TARIFA(self):
        return self.__COSTO_TARIFA

    @COSTO_TARIFA.setter
    def COSTO_TARIFA(self, COSTO_TARIFA: str):
        self.__COSTO_TARIFA = COSTO_TARIFA


    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID


    @property
    def TOTAL_RECAUDO_TARIFA(self):
        return self.__TOTAL_RECAUDO_TARIFA

    @TOTAL_RECAUDO_TARIFA.setter
    def TOTAL_RECAUDO_TARIFA(self, TOTAL_RECAUDO_TARIFA: str):
        self.__TOTAL_RECAUDO_TARIFA = TOTAL_RECAUDO_TARIFA


class gestionmodelosconsultas_resultcotracir_Trama(ElementoModeloResultado):

    def __init__(self, ID: str, CADENA_TRAMA: str):
        self.ID = ID
        self.CADENA_TRAMA = CADENA_TRAMA
        
        pass
    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID


    @property
    def CADENA_TRAMA(self):
        return self.__CADENA_TRAMA

    @CADENA_TRAMA.setter
    def CADENA_TRAMA(self, CADENA_TRAMA: str):
        self.__CADENA_TRAMA = CADENA_TRAMA


class gestionmodelosconsultas_resultcotracir_Planilla(ElementoModeloResultado):

    def __init__(self, ID: str, NUMERO_MOVIL: str, FECHA: str, CEDULA_CONDUCTOR: str, CONDUCTOR: str, TOTAL: str, TOTAL_RECAUDO_BRUTO: str, TOTAL_RECAUDO_NETO: str, TOTAL_GASTOS: str, LIQUIDADO: str, USUARIO: str, NOMBRE_PERSONA: str, APELLIDO: str, CEDULA: str, HORA_MODIFICACION: str, TOTAL_DEPOSITO: str):
        self.ID = ID
        self.NUMERO_MOVIL = NUMERO_MOVIL
        self.FECHA = FECHA
        self.CEDULA_CONDUCTOR = CEDULA_CONDUCTOR
        self.CONDUCTOR = CONDUCTOR
        self.TOTAL = TOTAL
        self.TOTAL_RECAUDO_BRUTO = TOTAL_RECAUDO_BRUTO
        self.TOTAL_RECAUDO_NETO = TOTAL_RECAUDO_NETO
        self.TOTAL_GASTOS = TOTAL_GASTOS
        self.LIQUIDADO = LIQUIDADO
        self.USUARIO = USUARIO
        self.NOMBRE_PERSONA = NOMBRE_PERSONA
        self.APELLIDO = APELLIDO
        self.CEDULA = CEDULA
        self.HORA_MODIFICACION = HORA_MODIFICACION
        self.TOTAL_DEPOSITO = TOTAL_DEPOSITO
        
        pass
    @property
    def TOTAL_RECAUDO_BRUTO(self):
        return self.__TOTAL_RECAUDO_BRUTO

    @TOTAL_RECAUDO_BRUTO.setter
    def TOTAL_RECAUDO_BRUTO(self, TOTAL_RECAUDO_BRUTO: str):
        self.__TOTAL_RECAUDO_BRUTO = TOTAL_RECAUDO_BRUTO


    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID


    @property
    def TOTAL_GASTOS(self):
        return self.__TOTAL_GASTOS

    @TOTAL_GASTOS.setter
    def TOTAL_GASTOS(self, TOTAL_GASTOS: str):
        self.__TOTAL_GASTOS = TOTAL_GASTOS


    @property
    def TOTAL_DEPOSITO(self):
        return self.__TOTAL_DEPOSITO

    @TOTAL_DEPOSITO.setter
    def TOTAL_DEPOSITO(self, TOTAL_DEPOSITO: str):
        self.__TOTAL_DEPOSITO = TOTAL_DEPOSITO


    @property
    def NUMERO_MOVIL(self):
        return self.__NUMERO_MOVIL

    @NUMERO_MOVIL.setter
    def NUMERO_MOVIL(self, NUMERO_MOVIL: str):
        self.__NUMERO_MOVIL = NUMERO_MOVIL


    @property
    def LIQUIDADO(self):
        return self.__LIQUIDADO

    @LIQUIDADO.setter
    def LIQUIDADO(self, LIQUIDADO: str):
        self.__LIQUIDADO = LIQUIDADO


    @property
    def CEDULA_CONDUCTOR(self):
        return self.__CEDULA_CONDUCTOR

    @CEDULA_CONDUCTOR.setter
    def CEDULA_CONDUCTOR(self, CEDULA_CONDUCTOR: str):
        self.__CEDULA_CONDUCTOR = CEDULA_CONDUCTOR


    @property
    def CONDUCTOR(self):
        return self.__CONDUCTOR

    @CONDUCTOR.setter
    def CONDUCTOR(self, CONDUCTOR: str):
        self.__CONDUCTOR = CONDUCTOR


    @property
    def USUARIO(self):
        return self.__USUARIO

    @USUARIO.setter
    def USUARIO(self, USUARIO: str):
        self.__USUARIO = USUARIO


    @property
    def TOTAL(self):
        return self.__TOTAL

    @TOTAL.setter
    def TOTAL(self, TOTAL: str):
        self.__TOTAL = TOTAL


    @property
    def HORA_MODIFICACION(self):
        return self.__HORA_MODIFICACION

    @HORA_MODIFICACION.setter
    def HORA_MODIFICACION(self, HORA_MODIFICACION: str):
        self.__HORA_MODIFICACION = HORA_MODIFICACION


    @property
    def APELLIDO(self):
        return self.__APELLIDO

    @APELLIDO.setter
    def APELLIDO(self, APELLIDO: str):
        self.__APELLIDO = APELLIDO


    @property
    def CEDULA(self):
        return self.__CEDULA

    @CEDULA.setter
    def CEDULA(self, CEDULA: str):
        self.__CEDULA = CEDULA


    @property
    def TOTAL_RECAUDO_NETO(self):
        return self.__TOTAL_RECAUDO_NETO

    @TOTAL_RECAUDO_NETO.setter
    def TOTAL_RECAUDO_NETO(self, TOTAL_RECAUDO_NETO: str):
        self.__TOTAL_RECAUDO_NETO = TOTAL_RECAUDO_NETO


    @property
    def NOMBRE_PERSONA(self):
        return self.__NOMBRE_PERSONA

    @NOMBRE_PERSONA.setter
    def NOMBRE_PERSONA(self, NOMBRE_PERSONA: str):
        self.__NOMBRE_PERSONA = NOMBRE_PERSONA


    @property
    def FECHA(self):
        return self.__FECHA

    @FECHA.setter
    def FECHA(self, FECHA: str):
        self.__FECHA = FECHA


class gestionmodelosconsultas_resultcotracir_Consolidado(ElementoModeloResultado):

    def __init__(self, ID: str, RUTA_DESPACHO: str, HORA_DESPACHO: str, REGISTRO_CONSOLIDADO: str, TOTAL_RECAUDO_BRUTO: str, TOTAL_RECAUDO_DESPACHO: str, ESTADO_CONSOLIDADO: str, ESTADO_IMPRESION: str):
        self.ID = ID
        self.RUTA_DESPACHO = RUTA_DESPACHO
        self.HORA_DESPACHO = HORA_DESPACHO
        self.REGISTRO_CONSOLIDADO = REGISTRO_CONSOLIDADO
        self.TOTAL_RECAUDO_BRUTO = TOTAL_RECAUDO_BRUTO
        self.TOTAL_RECAUDO_DESPACHO = TOTAL_RECAUDO_DESPACHO
        self.ESTADO_CONSOLIDADO = ESTADO_CONSOLIDADO
        self.ESTADO_IMPRESION = ESTADO_IMPRESION
        
        pass
    @property
    def TOTAL_RECAUDO_BRUTO(self):
        return self.__TOTAL_RECAUDO_BRUTO

    @TOTAL_RECAUDO_BRUTO.setter
    def TOTAL_RECAUDO_BRUTO(self, TOTAL_RECAUDO_BRUTO: str):
        self.__TOTAL_RECAUDO_BRUTO = TOTAL_RECAUDO_BRUTO


    @property
    def RUTA_DESPACHO(self):
        return self.__RUTA_DESPACHO

    @RUTA_DESPACHO.setter
    def RUTA_DESPACHO(self, RUTA_DESPACHO: str):
        self.__RUTA_DESPACHO = RUTA_DESPACHO


    @property
    def ESTADO_CONSOLIDADO(self):
        return self.__ESTADO_CONSOLIDADO

    @ESTADO_CONSOLIDADO.setter
    def ESTADO_CONSOLIDADO(self, ESTADO_CONSOLIDADO: str):
        self.__ESTADO_CONSOLIDADO = ESTADO_CONSOLIDADO


    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID


    @property
    def ESTADO_IMPRESION(self):
        return self.__ESTADO_IMPRESION

    @ESTADO_IMPRESION.setter
    def ESTADO_IMPRESION(self, ESTADO_IMPRESION: str):
        self.__ESTADO_IMPRESION = ESTADO_IMPRESION


    @property
    def TOTAL_RECAUDO_DESPACHO(self):
        return self.__TOTAL_RECAUDO_DESPACHO

    @TOTAL_RECAUDO_DESPACHO.setter
    def TOTAL_RECAUDO_DESPACHO(self, TOTAL_RECAUDO_DESPACHO: str):
        self.__TOTAL_RECAUDO_DESPACHO = TOTAL_RECAUDO_DESPACHO


    @property
    def HORA_DESPACHO(self):
        return self.__HORA_DESPACHO

    @HORA_DESPACHO.setter
    def HORA_DESPACHO(self, HORA_DESPACHO: str):
        self.__HORA_DESPACHO = HORA_DESPACHO


    @property
    def REGISTRO_CONSOLIDADO(self):
        return self.__REGISTRO_CONSOLIDADO

    @REGISTRO_CONSOLIDADO.setter
    def REGISTRO_CONSOLIDADO(self, REGISTRO_CONSOLIDADO: str):
        self.__REGISTRO_CONSOLIDADO = REGISTRO_CONSOLIDADO


class model_Relacion:

    pass
class resultset_ElementoModeloResultado:

    pass
class ResultElement:

    pass
class gestionmodelosconsultas_resultset_ElementoModeloResultado(ResultElement):

    def __init__(self, key: str, ElementoModeloResultado: set["resultset_ElementoModeloResultado"] = None, listElementoModeloResultado: "resultset_ElementoModeloResultado" = None):
        self.key = key
        self.ElementoModeloResultado = ElementoModeloResultado if ElementoModeloResultado is not None else set()
        self.listElementoModeloResultado = listElementoModeloResultado
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def ElementoModeloResultado(self):
        return self.__ElementoModeloResultado

    @ElementoModeloResultado.setter
    def ElementoModeloResultado(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_resultset_ElementoModeloResultado__ElementoModeloResultado", None)
        self.__ElementoModeloResultado = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ElementoModeloResultado106"):
                    opp_val = getattr(item, "ElementoModeloResultado106", None)
                    
                    if opp_val == self:
                        setattr(item, "ElementoModeloResultado106", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ElementoModeloResultado106"):
                    opp_val = getattr(item, "ElementoModeloResultado106", None)
                    
                    setattr(item, "ElementoModeloResultado106", self)
                    

    @property
    def listElementoModeloResultado(self):
        return self.__listElementoModeloResultado

    @listElementoModeloResultado.setter
    def listElementoModeloResultado(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_resultset_ElementoModeloResultado__listElementoModeloResultado", None)
        self.__listElementoModeloResultado = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ElementoModeloResultado108"):
                opp_val = getattr(old_value, "ElementoModeloResultado108", None)
                if opp_val == self:
                    setattr(old_value, "ElementoModeloResultado108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ElementoModeloResultado108"):
                opp_val = getattr(value, "ElementoModeloResultado108", None)
                setattr(value, "ElementoModeloResultado108", self)

class resultset_ResultElement:

    pass
class gestionmodelosconsultas_resultset_Resultado:

    def __init__(self, nombre: str, listResultado: "ModeloConsulta" = None, Resultado104: set["resultset_ResultElement"] = None):
        self.nombre = nombre
        self.listResultado = listResultado
        self.Resultado104 = Resultado104 if Resultado104 is not None else set()
        
        pass
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre


    @property
    def Resultado104(self):
        return self.__Resultado104

    @Resultado104.setter
    def Resultado104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_resultset_Resultado__Resultado104", None)
        self.__Resultado104 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ResultElement"):
                    opp_val = getattr(item, "ResultElement", None)
                    
                    if opp_val == self:
                        setattr(item, "ResultElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ResultElement"):
                    opp_val = getattr(item, "ResultElement", None)
                    
                    setattr(item, "ResultElement", self)
                    

    @property
    def listResultado(self):
        return self.__listResultado

    @listResultado.setter
    def listResultado(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_resultset_Resultado__listResultado", None)
        self.__listResultado = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModeloConsulta102"):
                opp_val = getattr(old_value, "ModeloConsulta102", None)
                if opp_val == self:
                    setattr(old_value, "ModeloConsulta102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModeloConsulta102"):
                opp_val = getattr(value, "ModeloConsulta102", None)
                setattr(value, "ModeloConsulta102", self)

class model_ElementoModelo:

    pass
class gestionmodelosconsultas_model_ElementoModelo:

    def __init__(self, nombre: str, to: set["model_ElementoModelo"] = None, from_: set["model_ElementoModelo"] = None):
        self.nombre = nombre
        self.to = to if to is not None else set()
        self.from_ = from_ if from_ is not None else set()
        
        pass
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre


    @property
    def from_(self):
        return self.__from_

    @from_.setter
    def from_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_model_ElementoModelo__from_", None)
        self.__from_ = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ElementoModelo100"):
                    opp_val = getattr(item, "ElementoModelo100", None)
                    
                    if opp_val == self:
                        setattr(item, "ElementoModelo100", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ElementoModelo100"):
                    opp_val = getattr(item, "ElementoModelo100", None)
                    
                    setattr(item, "ElementoModelo100", self)
                    

    @property
    def to(self):
        return self.__to

    @to.setter
    def to(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_model_ElementoModelo__to", None)
        self.__to = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ElementoModelo"):
                    opp_val = getattr(item, "ElementoModelo", None)
                    
                    if opp_val == self:
                        setattr(item, "ElementoModelo", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ElementoModelo"):
                    opp_val = getattr(item, "ElementoModelo", None)
                    
                    setattr(item, "ElementoModelo", self)
                    

class model_Campo:

    pass
class EADiagram:

    pass
class gestionmodelosconsultas_model_Proyeccion(EADiagram):

    pass
class gestionmodelosconsultas_model_ViewModel(EADiagram):

    pass
class model_ElementoConsulta:

    pass
class gestionmodelosconsultas_model_EADiagram(ABC):

    def __init__(self, nombre: str, EADiagram93: set["model_ElementoConsulta"] = None, EADiagram89: set["model_Relacion"] = None, listEADiagram: "ModeloConsulta" = None):
        self.nombre = nombre
        self.EADiagram93 = EADiagram93 if EADiagram93 is not None else set()
        self.EADiagram89 = EADiagram89 if EADiagram89 is not None else set()
        self.listEADiagram = listEADiagram
        
        pass
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre


    @property
    def listEADiagram(self):
        return self.__listEADiagram

    @listEADiagram.setter
    def listEADiagram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_model_EADiagram__listEADiagram", None)
        self.__listEADiagram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModeloConsulta91"):
                opp_val = getattr(old_value, "ModeloConsulta91", None)
                if opp_val == self:
                    setattr(old_value, "ModeloConsulta91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModeloConsulta91"):
                opp_val = getattr(value, "ModeloConsulta91", None)
                setattr(value, "ModeloConsulta91", self)

    @property
    def EADiagram89(self):
        return self.__EADiagram89

    @EADiagram89.setter
    def EADiagram89(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_model_EADiagram__EADiagram89", None)
        self.__EADiagram89 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Relacion"):
                    opp_val = getattr(item, "Relacion", None)
                    
                    if opp_val == self:
                        setattr(item, "Relacion", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Relacion"):
                    opp_val = getattr(item, "Relacion", None)
                    
                    setattr(item, "Relacion", self)
                    

    @property
    def EADiagram93(self):
        return self.__EADiagram93

    @EADiagram93.setter
    def EADiagram93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_model_EADiagram__EADiagram93", None)
        self.__EADiagram93 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ElementoConsulta94"):
                    opp_val = getattr(item, "ElementoConsulta94", None)
                    
                    if opp_val == self:
                        setattr(item, "ElementoConsulta94", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ElementoConsulta94"):
                    opp_val = getattr(item, "ElementoConsulta94", None)
                    
                    setattr(item, "ElementoConsulta94", self)
                    

class gestionmodelosconsultas_model_Campo:

    def __init__(self, nombreCampo: str, criterio: str, seleccion: bool, listCampos: "model_ElementoConsulta" = None):
        self.nombreCampo = nombreCampo
        self.criterio = criterio
        self.seleccion = seleccion
        self.listCampos = listCampos
        
        pass
    @property
    def criterio(self):
        return self.__criterio

    @criterio.setter
    def criterio(self, criterio: str):
        self.__criterio = criterio


    @property
    def nombreCampo(self):
        return self.__nombreCampo

    @nombreCampo.setter
    def nombreCampo(self, nombreCampo: str):
        self.__nombreCampo = nombreCampo


    @property
    def seleccion(self):
        return self.__seleccion

    @seleccion.setter
    def seleccion(self, seleccion: bool):
        self.__seleccion = seleccion


    @property
    def listCampos(self):
        return self.__listCampos

    @listCampos.setter
    def listCampos(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_model_Campo__listCampos", None)
        self.__listCampos = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ElementoConsulta"):
                opp_val = getattr(old_value, "ElementoConsulta", None)
                if opp_val == self:
                    setattr(old_value, "ElementoConsulta", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ElementoConsulta"):
                opp_val = getattr(value, "ElementoConsulta", None)
                setattr(value, "ElementoConsulta", self)

class gestionmodelosconsultas_entitymodel_ElementoRealizacionVisibleAttribute:

    def __init__(self, nombre: str, realizacionVisibleAttribute: "RealizacionDiagramEntity" = None, ElementoRealizacionVisibleAttribute61: set["Attribute"] = None):
        self.nombre = nombre
        self.realizacionVisibleAttribute = realizacionVisibleAttribute
        self.ElementoRealizacionVisibleAttribute61 = ElementoRealizacionVisibleAttribute61 if ElementoRealizacionVisibleAttribute61 is not None else set()
        
        pass
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre


    @property
    def realizacionVisibleAttribute(self):
        return self.__realizacionVisibleAttribute

    @realizacionVisibleAttribute.setter
    def realizacionVisibleAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_entitymodel_ElementoRealizacionVisibleAttribute__realizacionVisibleAttribute", None)
        self.__realizacionVisibleAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RealizacionDiagramEntity59"):
                opp_val = getattr(old_value, "RealizacionDiagramEntity59", None)
                if opp_val == self:
                    setattr(old_value, "RealizacionDiagramEntity59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RealizacionDiagramEntity59"):
                opp_val = getattr(value, "RealizacionDiagramEntity59", None)
                setattr(value, "RealizacionDiagramEntity59", self)

    @property
    def ElementoRealizacionVisibleAttribute61(self):
        return self.__ElementoRealizacionVisibleAttribute61

    @ElementoRealizacionVisibleAttribute61.setter
    def ElementoRealizacionVisibleAttribute61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_entitymodel_ElementoRealizacionVisibleAttribute__ElementoRealizacionVisibleAttribute61", None)
        self.__ElementoRealizacionVisibleAttribute61 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Attribute62"):
                    opp_val = getattr(item, "Attribute62", None)
                    
                    if opp_val == self:
                        setattr(item, "Attribute62", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Attribute62"):
                    opp_val = getattr(item, "Attribute62", None)
                    
                    setattr(item, "Attribute62", self)
                    

class ElementoModelo:

    pass
class gestionmodelosconsultas_model_ElementoConsulta(ElementoModelo):

    def __init__(self, order: str, listElementoConsulta: "model_EADiagram" = None, ownedElementoConsulta: set["model_Campo"] = None):
        self.order = order
        self.listElementoConsulta = listElementoConsulta
        self.ownedElementoConsulta = ownedElementoConsulta if ownedElementoConsulta is not None else set()
        
        pass
    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, order: str):
        self.__order = order


    @property
    def listElementoConsulta(self):
        return self.__listElementoConsulta

    @listElementoConsulta.setter
    def listElementoConsulta(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_model_ElementoConsulta__listElementoConsulta", None)
        self.__listElementoConsulta = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EADiagram96"):
                opp_val = getattr(old_value, "EADiagram96", None)
                if opp_val == self:
                    setattr(old_value, "EADiagram96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EADiagram96"):
                opp_val = getattr(value, "EADiagram96", None)
                setattr(value, "EADiagram96", self)

    @property
    def ownedElementoConsulta(self):
        return self.__ownedElementoConsulta

    @ownedElementoConsulta.setter
    def ownedElementoConsulta(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_model_ElementoConsulta__ownedElementoConsulta", None)
        self.__ownedElementoConsulta = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Campo"):
                    opp_val = getattr(item, "Campo", None)
                    
                    if opp_val == self:
                        setattr(item, "Campo", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Campo"):
                    opp_val = getattr(item, "Campo", None)
                    
                    setattr(item, "Campo", self)
                    

class gestionmodelosconsultas_model_Relacion(ElementoModelo):

    def __init__(self, estereotipo: str, order: str, listRelacion: "model_EADiagram" = None, gestionmodelosconsultas_model_Relacion: "model_ElementoConsulta" = None, gestionmodelosconsultas_model_Relacion85: "model_ElementoConsulta" = None):
        self.estereotipo = estereotipo
        self.order = order
        self.listRelacion = listRelacion
        self.gestionmodelosconsultas_model_Relacion = gestionmodelosconsultas_model_Relacion
        self.gestionmodelosconsultas_model_Relacion85 = gestionmodelosconsultas_model_Relacion85
        
        pass
    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, order: str):
        self.__order = order


    @property
    def estereotipo(self):
        return self.__estereotipo

    @estereotipo.setter
    def estereotipo(self, estereotipo: str):
        self.__estereotipo = estereotipo


    @property
    def gestionmodelosconsultas_model_Relacion(self):
        return self.__gestionmodelosconsultas_model_Relacion

    @gestionmodelosconsultas_model_Relacion.setter
    def gestionmodelosconsultas_model_Relacion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_model_Relacion__gestionmodelosconsultas_model_Relacion", None)
        self.__gestionmodelosconsultas_model_Relacion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ElementoConsulta"):
                opp_val = getattr(old_value, "model_ElementoConsulta", None)
                if opp_val == self:
                    setattr(old_value, "model_ElementoConsulta", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ElementoConsulta"):
                opp_val = getattr(value, "model_ElementoConsulta", None)
                setattr(value, "model_ElementoConsulta", self)

    @property
    def listRelacion(self):
        return self.__listRelacion

    @listRelacion.setter
    def listRelacion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_model_Relacion__listRelacion", None)
        self.__listRelacion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EADiagram82"):
                opp_val = getattr(old_value, "EADiagram82", None)
                if opp_val == self:
                    setattr(old_value, "EADiagram82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EADiagram82"):
                opp_val = getattr(value, "EADiagram82", None)
                setattr(value, "EADiagram82", self)

    @property
    def gestionmodelosconsultas_model_Relacion85(self):
        return self.__gestionmodelosconsultas_model_Relacion85

    @gestionmodelosconsultas_model_Relacion85.setter
    def gestionmodelosconsultas_model_Relacion85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_model_Relacion__gestionmodelosconsultas_model_Relacion85", None)
        self.__gestionmodelosconsultas_model_Relacion85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ElementoConsulta86"):
                opp_val = getattr(old_value, "model_ElementoConsulta86", None)
                if opp_val == self:
                    setattr(old_value, "model_ElementoConsulta86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ElementoConsulta86"):
                opp_val = getattr(value, "model_ElementoConsulta86", None)
                setattr(value, "model_ElementoConsulta86", self)

class modeloconsultas_gestionmodelosconsultas_ModelFactory:

    pass
class gestionmodelosconsultas_modeloconsultas_FactoryModeloConsulta:

    pass
class resultset_Resultado:

    pass
class model_EADiagram:

    pass
class gestionmodelosconsultas_modeloconsultas_ModeloConsulta:

    def __init__(self, nombre: str, ModeloConsulta68: "RealizacionDiagramEntity" = None, listModeloConsulta: "FactoryModeloConsulta" = None, ModeloConsulta73: set["model_EADiagram"] = None, ModeloConsulta75: set["resultset_Resultado"] = None):
        self.nombre = nombre
        self.ModeloConsulta68 = ModeloConsulta68
        self.listModeloConsulta = listModeloConsulta
        self.ModeloConsulta73 = ModeloConsulta73 if ModeloConsulta73 is not None else set()
        self.ModeloConsulta75 = ModeloConsulta75 if ModeloConsulta75 is not None else set()
        
        pass
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre


    @property
    def listModeloConsulta(self):
        return self.__listModeloConsulta

    @listModeloConsulta.setter
    def listModeloConsulta(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_modeloconsultas_ModeloConsulta__listModeloConsulta", None)
        self.__listModeloConsulta = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FactoryModeloConsulta71"):
                opp_val = getattr(old_value, "FactoryModeloConsulta71", None)
                if opp_val == self:
                    setattr(old_value, "FactoryModeloConsulta71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FactoryModeloConsulta71"):
                opp_val = getattr(value, "FactoryModeloConsulta71", None)
                setattr(value, "FactoryModeloConsulta71", self)

    @property
    def ModeloConsulta73(self):
        return self.__ModeloConsulta73

    @ModeloConsulta73.setter
    def ModeloConsulta73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_modeloconsultas_ModeloConsulta__ModeloConsulta73", None)
        self.__ModeloConsulta73 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EADiagram"):
                    opp_val = getattr(item, "EADiagram", None)
                    
                    if opp_val == self:
                        setattr(item, "EADiagram", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EADiagram"):
                    opp_val = getattr(item, "EADiagram", None)
                    
                    setattr(item, "EADiagram", self)
                    

    @property
    def ModeloConsulta68(self):
        return self.__ModeloConsulta68

    @ModeloConsulta68.setter
    def ModeloConsulta68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_modeloconsultas_ModeloConsulta__ModeloConsulta68", None)
        self.__ModeloConsulta68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RealizacionDiagramEntity69"):
                opp_val = getattr(old_value, "RealizacionDiagramEntity69", None)
                if opp_val == self:
                    setattr(old_value, "RealizacionDiagramEntity69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RealizacionDiagramEntity69"):
                opp_val = getattr(value, "RealizacionDiagramEntity69", None)
                setattr(value, "RealizacionDiagramEntity69", self)

    @property
    def ModeloConsulta75(self):
        return self.__ModeloConsulta75

    @ModeloConsulta75.setter
    def ModeloConsulta75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_modeloconsultas_ModeloConsulta__ModeloConsulta75", None)
        self.__ModeloConsulta75 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Resultado"):
                    opp_val = getattr(item, "Resultado", None)
                    
                    if opp_val == self:
                        setattr(item, "Resultado", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Resultado"):
                    opp_val = getattr(item, "Resultado", None)
                    
                    setattr(item, "Resultado", self)
                    

class gestionmodelosconsultas_entitymodel_Value:

    def __init__(self, value: str, values: set["ElementoRealizacionValueAttribute"] = None, listValues: "RealizacionDiagramEntity" = None):
        self.value = value
        self.values = values if values is not None else set()
        self.listValues = listValues
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def listValues(self):
        return self.__listValues

    @listValues.setter
    def listValues(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_entitymodel_Value__listValues", None)
        self.__listValues = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RealizacionDiagramEntity66"):
                opp_val = getattr(old_value, "RealizacionDiagramEntity66", None)
                if opp_val == self:
                    setattr(old_value, "RealizacionDiagramEntity66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RealizacionDiagramEntity66"):
                opp_val = getattr(value, "RealizacionDiagramEntity66", None)
                setattr(value, "RealizacionDiagramEntity66", self)

    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_entitymodel_Value__values", None)
        self.__values = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ElementoRealizacionValueAttribute64"):
                    opp_val = getattr(item, "ElementoRealizacionValueAttribute64", None)
                    
                    if opp_val == self:
                        setattr(item, "ElementoRealizacionValueAttribute64", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ElementoRealizacionValueAttribute64"):
                    opp_val = getattr(item, "ElementoRealizacionValueAttribute64", None)
                    
                    setattr(item, "ElementoRealizacionValueAttribute64", self)
                    

class gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity:

    def __init__(self, nombreModelElementEntity: str, tipo: str, ElementoRealizacionDiagramEntity44: "ModelElementEntity" = None, listElementoRealizacionDiagramEntity: "RealizacionDiagramEntity" = None, ElementoRealizacionDiagramEntity48: set["ElementoRealizacionValueAttribute"] = None):
        self.nombreModelElementEntity = nombreModelElementEntity
        self.tipo = tipo
        self.ElementoRealizacionDiagramEntity44 = ElementoRealizacionDiagramEntity44
        self.listElementoRealizacionDiagramEntity = listElementoRealizacionDiagramEntity
        self.ElementoRealizacionDiagramEntity48 = ElementoRealizacionDiagramEntity48 if ElementoRealizacionDiagramEntity48 is not None else set()
        
        pass
    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo: str):
        self.__tipo = tipo


    @property
    def nombreModelElementEntity(self):
        return self.__nombreModelElementEntity

    @nombreModelElementEntity.setter
    def nombreModelElementEntity(self, nombreModelElementEntity: str):
        self.__nombreModelElementEntity = nombreModelElementEntity


    @property
    def ElementoRealizacionDiagramEntity44(self):
        return self.__ElementoRealizacionDiagramEntity44

    @ElementoRealizacionDiagramEntity44.setter
    def ElementoRealizacionDiagramEntity44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity__ElementoRealizacionDiagramEntity44", None)
        self.__ElementoRealizacionDiagramEntity44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ModelElementEntity"):
                opp_val = getattr(old_value, "ModelElementEntity", None)
                if opp_val == self:
                    setattr(old_value, "ModelElementEntity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ModelElementEntity"):
                opp_val = getattr(value, "ModelElementEntity", None)
                setattr(value, "ModelElementEntity", self)

    @property
    def listElementoRealizacionDiagramEntity(self):
        return self.__listElementoRealizacionDiagramEntity

    @listElementoRealizacionDiagramEntity.setter
    def listElementoRealizacionDiagramEntity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity__listElementoRealizacionDiagramEntity", None)
        self.__listElementoRealizacionDiagramEntity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RealizacionDiagramEntity46"):
                opp_val = getattr(old_value, "RealizacionDiagramEntity46", None)
                if opp_val == self:
                    setattr(old_value, "RealizacionDiagramEntity46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RealizacionDiagramEntity46"):
                opp_val = getattr(value, "RealizacionDiagramEntity46", None)
                setattr(value, "RealizacionDiagramEntity46", self)

    @property
    def ElementoRealizacionDiagramEntity48(self):
        return self.__ElementoRealizacionDiagramEntity48

    @ElementoRealizacionDiagramEntity48.setter
    def ElementoRealizacionDiagramEntity48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity__ElementoRealizacionDiagramEntity48", None)
        self.__ElementoRealizacionDiagramEntity48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ElementoRealizacionValueAttribute49"):
                    opp_val = getattr(item, "ElementoRealizacionValueAttribute49", None)
                    
                    if opp_val == self:
                        setattr(item, "ElementoRealizacionValueAttribute49", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ElementoRealizacionValueAttribute49"):
                    opp_val = getattr(item, "ElementoRealizacionValueAttribute49", None)
                    
                    setattr(item, "ElementoRealizacionValueAttribute49", self)
                    

class Value:

    pass
class gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute:

    def __init__(self, nombre: str, ElementoRealizacionValueAttribute51: set["Attribute"] = None, listElementoRealizacionAttribute: "ElementoRealizacionDiagramEntity" = None, ElementoRealizacionValueAttribute56: set["Value"] = None):
        self.nombre = nombre
        self.ElementoRealizacionValueAttribute51 = ElementoRealizacionValueAttribute51 if ElementoRealizacionValueAttribute51 is not None else set()
        self.listElementoRealizacionAttribute = listElementoRealizacionAttribute
        self.ElementoRealizacionValueAttribute56 = ElementoRealizacionValueAttribute56 if ElementoRealizacionValueAttribute56 is not None else set()
        
        pass
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre


    @property
    def ElementoRealizacionValueAttribute56(self):
        return self.__ElementoRealizacionValueAttribute56

    @ElementoRealizacionValueAttribute56.setter
    def ElementoRealizacionValueAttribute56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute__ElementoRealizacionValueAttribute56", None)
        self.__ElementoRealizacionValueAttribute56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Value57"):
                    opp_val = getattr(item, "Value57", None)
                    
                    if opp_val == self:
                        setattr(item, "Value57", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Value57"):
                    opp_val = getattr(item, "Value57", None)
                    
                    setattr(item, "Value57", self)
                    

    @property
    def ElementoRealizacionValueAttribute51(self):
        return self.__ElementoRealizacionValueAttribute51

    @ElementoRealizacionValueAttribute51.setter
    def ElementoRealizacionValueAttribute51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute__ElementoRealizacionValueAttribute51", None)
        self.__ElementoRealizacionValueAttribute51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Attribute52"):
                    opp_val = getattr(item, "Attribute52", None)
                    
                    if opp_val == self:
                        setattr(item, "Attribute52", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Attribute52"):
                    opp_val = getattr(item, "Attribute52", None)
                    
                    setattr(item, "Attribute52", self)
                    

    @property
    def listElementoRealizacionAttribute(self):
        return self.__listElementoRealizacionAttribute

    @listElementoRealizacionAttribute.setter
    def listElementoRealizacionAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute__listElementoRealizacionAttribute", None)
        self.__listElementoRealizacionAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ElementoRealizacionDiagramEntity54"):
                opp_val = getattr(old_value, "ElementoRealizacionDiagramEntity54", None)
                if opp_val == self:
                    setattr(old_value, "ElementoRealizacionDiagramEntity54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ElementoRealizacionDiagramEntity54"):
                opp_val = getattr(value, "ElementoRealizacionDiagramEntity54", None)
                setattr(value, "ElementoRealizacionDiagramEntity54", self)

class RealizacionDiagramEntity:

    pass
class gestionmodelosconsultas_entitymodel_Attribute:

    def __init__(self, type: str, value: str, visible: bool, attributeType: str, name: str, listAttributes: "Entity" = None, valueAttribute: set["ElementoRealizacionValueAttribute"] = None, visibleAttribute: set["ElementoRealizacionVisibleAttribute"] = None):
        self.type = type
        self.value = value
        self.visible = visible
        self.attributeType = attributeType
        self.name = name
        self.listAttributes = listAttributes
        self.valueAttribute = valueAttribute if valueAttribute is not None else set()
        self.visibleAttribute = visibleAttribute if visibleAttribute is not None else set()
        
        pass
    @property
    def attributeType(self):
        return self.__attributeType

    @attributeType.setter
    def attributeType(self, attributeType: str):
        self.__attributeType = attributeType


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def visible(self):
        return self.__visible

    @visible.setter
    def visible(self, visible: bool):
        self.__visible = visible


    @property
    def valueAttribute(self):
        return self.__valueAttribute

    @valueAttribute.setter
    def valueAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_entitymodel_Attribute__valueAttribute", None)
        self.__valueAttribute = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ElementoRealizacionValueAttribute"):
                    opp_val = getattr(item, "ElementoRealizacionValueAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "ElementoRealizacionValueAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ElementoRealizacionValueAttribute"):
                    opp_val = getattr(item, "ElementoRealizacionValueAttribute", None)
                    
                    setattr(item, "ElementoRealizacionValueAttribute", self)
                    

    @property
    def visibleAttribute(self):
        return self.__visibleAttribute

    @visibleAttribute.setter
    def visibleAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_entitymodel_Attribute__visibleAttribute", None)
        self.__visibleAttribute = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ElementoRealizacionVisibleAttribute"):
                    opp_val = getattr(item, "ElementoRealizacionVisibleAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "ElementoRealizacionVisibleAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ElementoRealizacionVisibleAttribute"):
                    opp_val = getattr(item, "ElementoRealizacionVisibleAttribute", None)
                    
                    setattr(item, "ElementoRealizacionVisibleAttribute", self)
                    

    @property
    def listAttributes(self):
        return self.__listAttributes

    @listAttributes.setter
    def listAttributes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_entitymodel_Attribute__listAttributes", None)
        self.__listAttributes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Entity26"):
                opp_val = getattr(old_value, "Entity26", None)
                if opp_val == self:
                    setattr(old_value, "Entity26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Entity26"):
                opp_val = getattr(value, "Entity26", None)
                setattr(value, "Entity26", self)

class EntityRelation:

    pass
class gestionmodelosconsultas_entitymodel_SimpleRelation(EntityRelation):

    pass
class ModeloConsulta:

    pass
class gestionmodelosconsultas_entitymodel_RealizacionDiagramEntity:

    pass
class entitymodel_gestionmodelosconsultas_ModelFactory:

    pass
class gestionmodelosconsultas_entitymodel_DiagramEntity:

    pass
class ElementoRealizacionDiagramEntity:

    pass
class gestionmodelosconsultas_entitymodel_ModelElementEntity(ABC):

    def __init__(self, name: str, stereotype: str, modelElementEntity: set["ElementoRealizacionDiagramEntity"] = None):
        self.name = name
        self.stereotype = stereotype
        self.modelElementEntity = modelElementEntity if modelElementEntity is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def stereotype(self):
        return self.__stereotype

    @stereotype.setter
    def stereotype(self, stereotype: str):
        self.__stereotype = stereotype


    @property
    def modelElementEntity(self):
        return self.__modelElementEntity

    @modelElementEntity.setter
    def modelElementEntity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_entitymodel_ModelElementEntity__modelElementEntity", None)
        self.__modelElementEntity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ElementoRealizacionDiagramEntity"):
                    opp_val = getattr(item, "ElementoRealizacionDiagramEntity", None)
                    
                    if opp_val == self:
                        setattr(item, "ElementoRealizacionDiagramEntity", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ElementoRealizacionDiagramEntity"):
                    opp_val = getattr(item, "ElementoRealizacionDiagramEntity", None)
                    
                    setattr(item, "ElementoRealizacionDiagramEntity", self)
                    

class ElementoRealizacionVisibleAttribute:

    pass
class ElementoRealizacionValueAttribute:

    pass
class gestionmodelosconsultas_factoryrules_Rule:

    def __init__(self, name: str, listRuleDiagramEntity: "factoryrules_RulesFactory" = None, Rule12: set["factoryrules_ChildRule"] = None):
        self.name = name
        self.listRuleDiagramEntity = listRuleDiagramEntity
        self.Rule12 = Rule12 if Rule12 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def listRuleDiagramEntity(self):
        return self.__listRuleDiagramEntity

    @listRuleDiagramEntity.setter
    def listRuleDiagramEntity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_factoryrules_Rule__listRuleDiagramEntity", None)
        self.__listRuleDiagramEntity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RulesFactory10"):
                opp_val = getattr(old_value, "RulesFactory10", None)
                if opp_val == self:
                    setattr(old_value, "RulesFactory10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RulesFactory10"):
                opp_val = getattr(value, "RulesFactory10", None)
                setattr(value, "RulesFactory10", self)

    @property
    def Rule12(self):
        return self.__Rule12

    @Rule12.setter
    def Rule12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_factoryrules_Rule__Rule12", None)
        self.__Rule12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ChildRule"):
                    opp_val = getattr(item, "ChildRule", None)
                    
                    if opp_val == self:
                        setattr(item, "ChildRule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ChildRule"):
                    opp_val = getattr(item, "ChildRule", None)
                    
                    setattr(item, "ChildRule", self)
                    

class Entity:

    pass
class gestionmodelosconsultas_entitymodel_AssociativeEntity(Entity):

    pass
class Attribute:

    pass
class ModelElementEntity:

    pass
class gestionmodelosconsultas_entitymodel_EntityRelation(ModelElementEntity):

    def __init__(self, atributteForeingKeySource: str, atributtePrimaryKeyTarget: str, multiplicitySource: str, multiplicityTarget: str, listEntityRelation: "DiagramEntity" = None, gestionmodelosconsultas_entitymodel_EntityRelation: "Entity" = None, gestionmodelosconsultas_entitymodel_EntityRelation23: "Entity" = None, ModelElementEntity: "gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity" = None):
        self.atributteForeingKeySource = atributteForeingKeySource
        self.atributtePrimaryKeyTarget = atributtePrimaryKeyTarget
        self.multiplicitySource = multiplicitySource
        self.multiplicityTarget = multiplicityTarget
        self.listEntityRelation = listEntityRelation
        self.gestionmodelosconsultas_entitymodel_EntityRelation = gestionmodelosconsultas_entitymodel_EntityRelation
        self.gestionmodelosconsultas_entitymodel_EntityRelation23 = gestionmodelosconsultas_entitymodel_EntityRelation23
        
        pass
    @property
    def multiplicitySource(self):
        return self.__multiplicitySource

    @multiplicitySource.setter
    def multiplicitySource(self, multiplicitySource: str):
        self.__multiplicitySource = multiplicitySource


    @property
    def atributteForeingKeySource(self):
        return self.__atributteForeingKeySource

    @atributteForeingKeySource.setter
    def atributteForeingKeySource(self, atributteForeingKeySource: str):
        self.__atributteForeingKeySource = atributteForeingKeySource


    @property
    def atributtePrimaryKeyTarget(self):
        return self.__atributtePrimaryKeyTarget

    @atributtePrimaryKeyTarget.setter
    def atributtePrimaryKeyTarget(self, atributtePrimaryKeyTarget: str):
        self.__atributtePrimaryKeyTarget = atributtePrimaryKeyTarget


    @property
    def multiplicityTarget(self):
        return self.__multiplicityTarget

    @multiplicityTarget.setter
    def multiplicityTarget(self, multiplicityTarget: str):
        self.__multiplicityTarget = multiplicityTarget


    @property
    def listEntityRelation(self):
        return self.__listEntityRelation

    @listEntityRelation.setter
    def listEntityRelation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_entitymodel_EntityRelation__listEntityRelation", None)
        self.__listEntityRelation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DiagramEntity19"):
                opp_val = getattr(old_value, "DiagramEntity19", None)
                if opp_val == self:
                    setattr(old_value, "DiagramEntity19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagramEntity19"):
                opp_val = getattr(value, "DiagramEntity19", None)
                setattr(value, "DiagramEntity19", self)

    @property
    def gestionmodelosconsultas_entitymodel_EntityRelation23(self):
        return self.__gestionmodelosconsultas_entitymodel_EntityRelation23

    @gestionmodelosconsultas_entitymodel_EntityRelation23.setter
    def gestionmodelosconsultas_entitymodel_EntityRelation23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_entitymodel_EntityRelation__gestionmodelosconsultas_entitymodel_EntityRelation23", None)
        self.__gestionmodelosconsultas_entitymodel_EntityRelation23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Entity24"):
                opp_val = getattr(old_value, "Entity24", None)
                if opp_val == self:
                    setattr(old_value, "Entity24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Entity24"):
                opp_val = getattr(value, "Entity24", None)
                setattr(value, "Entity24", self)

    @property
    def gestionmodelosconsultas_entitymodel_EntityRelation(self):
        return self.__gestionmodelosconsultas_entitymodel_EntityRelation

    @gestionmodelosconsultas_entitymodel_EntityRelation.setter
    def gestionmodelosconsultas_entitymodel_EntityRelation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_entitymodel_EntityRelation__gestionmodelosconsultas_entitymodel_EntityRelation", None)
        self.__gestionmodelosconsultas_entitymodel_EntityRelation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Entity21"):
                opp_val = getattr(old_value, "Entity21", None)
                if opp_val == self:
                    setattr(old_value, "Entity21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Entity21"):
                opp_val = getattr(value, "Entity21", None)
                setattr(value, "Entity21", self)

class gestionmodelosconsultas_entitymodel_Entity(ModelElementEntity):

    pass
class ChildRule:

    pass
class gestionmodelosconsultas_factoryrules_RelationName(ChildRule):

    pass
class gestionmodelosconsultas_factoryrules_EntityName(ChildRule):

    pass
class gestionmodelosconsultas_factoryrules_ChildRule(ABC):

    def __init__(self, name: str, listChildRule: "factoryrules_Rule" = None):
        self.name = name
        self.listChildRule = listChildRule
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def listChildRule(self):
        return self.__listChildRule

    @listChildRule.setter
    def listChildRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_factoryrules_ChildRule__listChildRule", None)
        self.__listChildRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Rule14"):
                opp_val = getattr(old_value, "Rule14", None)
                if opp_val == self:
                    setattr(old_value, "Rule14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Rule14"):
                opp_val = getattr(value, "Rule14", None)
                setattr(value, "Rule14", self)

class factoryrules_ChildRule:

    pass
class factoryrules_Rule:

    pass
class factoryrules_gestionmodelosconsultas_ModelFactory:

    pass
class gestionmodelosconsultas_factoryrules_RulesFactory:

    pass
class DiagramEntity:

    pass
class FactoryModeloConsulta:

    pass
class factoryrules_RulesFactory:

    pass
class gestionmodelosconsultas_ModelFactory:

    def __init__(self, ModelFactory: "factoryrules_RulesFactory" = None, ModelFactory2: "FactoryModeloConsulta" = None, ModelFactory4: "DiagramEntity" = None):
        self.ModelFactory = ModelFactory
        self.ModelFactory2 = ModelFactory2
        self.ModelFactory4 = ModelFactory4
        
        pass
    @property
    def ModelFactory(self):
        return self.__ModelFactory

    @ModelFactory.setter
    def ModelFactory(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_ModelFactory__ModelFactory", None)
        self.__ModelFactory = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RulesFactory"):
                opp_val = getattr(old_value, "RulesFactory", None)
                if opp_val == self:
                    setattr(old_value, "RulesFactory", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RulesFactory"):
                opp_val = getattr(value, "RulesFactory", None)
                setattr(value, "RulesFactory", self)

    @property
    def ModelFactory2(self):
        return self.__ModelFactory2

    @ModelFactory2.setter
    def ModelFactory2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_ModelFactory__ModelFactory2", None)
        self.__ModelFactory2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "FactoryModeloConsulta"):
                opp_val = getattr(old_value, "FactoryModeloConsulta", None)
                if opp_val == self:
                    setattr(old_value, "FactoryModeloConsulta", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "FactoryModeloConsulta"):
                opp_val = getattr(value, "FactoryModeloConsulta", None)
                setattr(value, "FactoryModeloConsulta", self)

    @property
    def ModelFactory4(self):
        return self.__ModelFactory4

    @ModelFactory4.setter
    def ModelFactory4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_ModelFactory__ModelFactory4", None)
        self.__ModelFactory4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "DiagramEntity"):
                opp_val = getattr(old_value, "DiagramEntity", None)
                if opp_val == self:
                    setattr(old_value, "DiagramEntity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "DiagramEntity"):
                opp_val = getattr(value, "DiagramEntity", None)
                setattr(value, "DiagramEntity", self)

    def salvar(self):
        # TODO: Implement salvar method
        pass

    def cargar(self) :
        # TODO: Implement cargar method
        pass
