from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

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
class AttributeType(Enum):
    primaryKey = "primaryKey"
    ordinary = "ordinary"
class Multiplicity(Enum):
    one_to_many = "one_to_many"
    many_to_one = "many_to_one"
    one_to_one = "one_to_one"


############################################
# Definition of Classes
############################################

class ElementoConsulta:

    pass
class gestionmodelosconsultas_cotracir_Trama(ElementoConsulta):

    pass
class gestionmodelosconsultas_cotracir_Transaccion(ElementoConsulta):

    pass
class gestionmodelosconsultas_cotracir_Propietario(ElementoConsulta):

    pass
class gestionmodelosconsultas_cotracir_Detallado(ElementoConsulta):

    pass
class gestionmodelosconsultas_cotracir_Consolidado(ElementoConsulta):

    pass
class gestionmodelosconsultas_cotracir_Planilla(ElementoConsulta):

    pass
class gestionmodelosconsultas_resultcotracir_NewClass:

    pass
class gestionmodelosconsultas_model_ElementoModelo:

    def __init__(self, nombre: str, model123: set["model_ElementoModelo"] = None, model126: set["model_ElementoModelo"] = None):
        self.nombre = nombre
        self.model123 = model123 if model123 is not None else set()
        self.model126 = model126 if model126 is not None else set()
        
    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def model126(self):
        return self.__model126

    @model126.setter
    def model126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_model_ElementoModelo__model126", None)
        self.__model126 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "modeloconsultas127"):
                    opp_val = getattr(item, "modeloconsultas127", None)
                    
                    if opp_val == self:
                        setattr(item, "modeloconsultas127", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "modeloconsultas127"):
                    opp_val = getattr(item, "modeloconsultas127", None)
                    
                    setattr(item, "modeloconsultas127", self)
                    

    @property
    def model123(self):
        return self.__model123

    @model123.setter
    def model123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_model_ElementoModelo__model123", None)
        self.__model123 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "modeloconsultas124"):
                    opp_val = getattr(item, "modeloconsultas124", None)
                    
                    if opp_val == self:
                        setattr(item, "modeloconsultas124", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "modeloconsultas124"):
                    opp_val = getattr(item, "modeloconsultas124", None)
                    
                    setattr(item, "modeloconsultas124", self)
                    

class model_Campo:

    pass
class EADiagram:

    pass
class gestionmodelosconsultas_model_Proyeccion(EADiagram):

    pass
class gestionmodelosconsultas_model_ViewModel(EADiagram):

    pass
class model_Relacion:

    pass
class gestionmodelosconsultas_model_EADiagram(ABC):

    def __init__(self, nombre: str, model108: set["model_Relacion"] = None, ModeloConsulta111: "ModeloConsulta" = None, model114: set["model_ElementoConsulta"] = None):
        self.nombre = nombre
        self.model108 = model108 if model108 is not None else set()
        self.ModeloConsulta111 = ModeloConsulta111
        self.model114 = model114 if model114 is not None else set()
        
    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def ModeloConsulta111(self):
        return self.__ModeloConsulta111

    @ModeloConsulta111.setter
    def ModeloConsulta111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_model_EADiagram__ModeloConsulta111", None)
        self.__ModeloConsulta111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modeloconsultas112"):
                opp_val = getattr(old_value, "modeloconsultas112", None)
                if opp_val == self:
                    setattr(old_value, "modeloconsultas112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modeloconsultas112"):
                opp_val = getattr(value, "modeloconsultas112", None)
                setattr(value, "modeloconsultas112", self)

    @property
    def model114(self):
        return self.__model114

    @model114.setter
    def model114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_model_EADiagram__model114", None)
        self.__model114 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "modeloconsultas115"):
                    opp_val = getattr(item, "modeloconsultas115", None)
                    
                    if opp_val == self:
                        setattr(item, "modeloconsultas115", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "modeloconsultas115"):
                    opp_val = getattr(item, "modeloconsultas115", None)
                    
                    setattr(item, "modeloconsultas115", self)
                    

    @property
    def model108(self):
        return self.__model108

    @model108.setter
    def model108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_model_EADiagram__model108", None)
        self.__model108 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "modeloconsultas109"):
                    opp_val = getattr(item, "modeloconsultas109", None)
                    
                    if opp_val == self:
                        setattr(item, "modeloconsultas109", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "modeloconsultas109"):
                    opp_val = getattr(item, "modeloconsultas109", None)
                    
                    setattr(item, "modeloconsultas109", self)
                    

class ElementoModeloResultado:

    pass
class gestionmodelosconsultas_resultcotracir_Propietario(ElementoModeloResultado):

    def __init__(self, CEDULA: str, ID: str, NOMBRE: str):
        self.CEDULA = CEDULA
        self.ID = ID
        self.NOMBRE = NOMBRE
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def CEDULA(self) -> str:
        return self.__CEDULA

    @CEDULA.setter
    def CEDULA(self, CEDULA: str):
        self.__CEDULA = CEDULA

    @property
    def NOMBRE(self) -> str:
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
        
    @property
    def REGISTRO_RECAUDO(self) -> str:
        return self.__REGISTRO_RECAUDO

    @REGISTRO_RECAUDO.setter
    def REGISTRO_RECAUDO(self, REGISTRO_RECAUDO: str):
        self.__REGISTRO_RECAUDO = REGISTRO_RECAUDO

    @property
    def COSTO_TARIFA(self) -> str:
        return self.__COSTO_TARIFA

    @COSTO_TARIFA.setter
    def COSTO_TARIFA(self, COSTO_TARIFA: str):
        self.__COSTO_TARIFA = COSTO_TARIFA

    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def TOTAL_RECAUDO_TARIFA(self) -> str:
        return self.__TOTAL_RECAUDO_TARIFA

    @TOTAL_RECAUDO_TARIFA.setter
    def TOTAL_RECAUDO_TARIFA(self, TOTAL_RECAUDO_TARIFA: str):
        self.__TOTAL_RECAUDO_TARIFA = TOTAL_RECAUDO_TARIFA

    @property
    def NOMBRE(self) -> str:
        return self.__NOMBRE

    @NOMBRE.setter
    def NOMBRE(self, NOMBRE: str):
        self.__NOMBRE = NOMBRE

    @property
    def REGISTRO(self) -> str:
        return self.__REGISTRO

    @REGISTRO.setter
    def REGISTRO(self, REGISTRO: str):
        self.__REGISTRO = REGISTRO

class gestionmodelosconsultas_resultcotracir_Planilla(ElementoModeloResultado):

    def __init__(self, ID: str, NUMERO_MOVIL: str, FECHA: str, CEDULA_CONDUCTOR: str, CONDUCTOR: str, TOTAL: str, TOTAL_RECAUDO_BRUTO: str, TOTAL_RECAUDO_NETO: str, TOTAL_DEPOSITO: str, TOTAL_GASTOS: str, LIQUIDADO: str, USUARIO: str, NOMBRE_PERSONA: str, APELLIDO: str, CEDULA: str, HORA_MODIFICACION: str):
        self.ID = ID
        self.NUMERO_MOVIL = NUMERO_MOVIL
        self.FECHA = FECHA
        self.CEDULA_CONDUCTOR = CEDULA_CONDUCTOR
        self.CONDUCTOR = CONDUCTOR
        self.TOTAL = TOTAL
        self.TOTAL_RECAUDO_BRUTO = TOTAL_RECAUDO_BRUTO
        self.TOTAL_RECAUDO_NETO = TOTAL_RECAUDO_NETO
        self.TOTAL_DEPOSITO = TOTAL_DEPOSITO
        self.TOTAL_GASTOS = TOTAL_GASTOS
        self.LIQUIDADO = LIQUIDADO
        self.USUARIO = USUARIO
        self.NOMBRE_PERSONA = NOMBRE_PERSONA
        self.APELLIDO = APELLIDO
        self.CEDULA = CEDULA
        self.HORA_MODIFICACION = HORA_MODIFICACION
        
    @property
    def TOTAL_DEPOSITO(self) -> str:
        return self.__TOTAL_DEPOSITO

    @TOTAL_DEPOSITO.setter
    def TOTAL_DEPOSITO(self, TOTAL_DEPOSITO: str):
        self.__TOTAL_DEPOSITO = TOTAL_DEPOSITO

    @property
    def USUARIO(self) -> str:
        return self.__USUARIO

    @USUARIO.setter
    def USUARIO(self, USUARIO: str):
        self.__USUARIO = USUARIO

    @property
    def APELLIDO(self) -> str:
        return self.__APELLIDO

    @APELLIDO.setter
    def APELLIDO(self, APELLIDO: str):
        self.__APELLIDO = APELLIDO

    @property
    def TOTAL_RECAUDO_NETO(self) -> str:
        return self.__TOTAL_RECAUDO_NETO

    @TOTAL_RECAUDO_NETO.setter
    def TOTAL_RECAUDO_NETO(self, TOTAL_RECAUDO_NETO: str):
        self.__TOTAL_RECAUDO_NETO = TOTAL_RECAUDO_NETO

    @property
    def NOMBRE_PERSONA(self) -> str:
        return self.__NOMBRE_PERSONA

    @NOMBRE_PERSONA.setter
    def NOMBRE_PERSONA(self, NOMBRE_PERSONA: str):
        self.__NOMBRE_PERSONA = NOMBRE_PERSONA

    @property
    def NUMERO_MOVIL(self) -> str:
        return self.__NUMERO_MOVIL

    @NUMERO_MOVIL.setter
    def NUMERO_MOVIL(self, NUMERO_MOVIL: str):
        self.__NUMERO_MOVIL = NUMERO_MOVIL

    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def TOTAL(self) -> str:
        return self.__TOTAL

    @TOTAL.setter
    def TOTAL(self, TOTAL: str):
        self.__TOTAL = TOTAL

    @property
    def TOTAL_RECAUDO_BRUTO(self) -> str:
        return self.__TOTAL_RECAUDO_BRUTO

    @TOTAL_RECAUDO_BRUTO.setter
    def TOTAL_RECAUDO_BRUTO(self, TOTAL_RECAUDO_BRUTO: str):
        self.__TOTAL_RECAUDO_BRUTO = TOTAL_RECAUDO_BRUTO

    @property
    def FECHA(self) -> str:
        return self.__FECHA

    @FECHA.setter
    def FECHA(self, FECHA: str):
        self.__FECHA = FECHA

    @property
    def HORA_MODIFICACION(self) -> str:
        return self.__HORA_MODIFICACION

    @HORA_MODIFICACION.setter
    def HORA_MODIFICACION(self, HORA_MODIFICACION: str):
        self.__HORA_MODIFICACION = HORA_MODIFICACION

    @property
    def TOTAL_GASTOS(self) -> str:
        return self.__TOTAL_GASTOS

    @TOTAL_GASTOS.setter
    def TOTAL_GASTOS(self, TOTAL_GASTOS: str):
        self.__TOTAL_GASTOS = TOTAL_GASTOS

    @property
    def CEDULA(self) -> str:
        return self.__CEDULA

    @CEDULA.setter
    def CEDULA(self, CEDULA: str):
        self.__CEDULA = CEDULA

    @property
    def CEDULA_CONDUCTOR(self) -> str:
        return self.__CEDULA_CONDUCTOR

    @CEDULA_CONDUCTOR.setter
    def CEDULA_CONDUCTOR(self, CEDULA_CONDUCTOR: str):
        self.__CEDULA_CONDUCTOR = CEDULA_CONDUCTOR

    @property
    def LIQUIDADO(self) -> str:
        return self.__LIQUIDADO

    @LIQUIDADO.setter
    def LIQUIDADO(self, LIQUIDADO: str):
        self.__LIQUIDADO = LIQUIDADO

    @property
    def CONDUCTOR(self) -> str:
        return self.__CONDUCTOR

    @CONDUCTOR.setter
    def CONDUCTOR(self, CONDUCTOR: str):
        self.__CONDUCTOR = CONDUCTOR

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
        
    @property
    def HORA_DESPACHO(self) -> str:
        return self.__HORA_DESPACHO

    @HORA_DESPACHO.setter
    def HORA_DESPACHO(self, HORA_DESPACHO: str):
        self.__HORA_DESPACHO = HORA_DESPACHO

    @property
    def RUTA_DESPACHO(self) -> str:
        return self.__RUTA_DESPACHO

    @RUTA_DESPACHO.setter
    def RUTA_DESPACHO(self, RUTA_DESPACHO: str):
        self.__RUTA_DESPACHO = RUTA_DESPACHO

    @property
    def ESTADO_CONSOLIDADO(self) -> str:
        return self.__ESTADO_CONSOLIDADO

    @ESTADO_CONSOLIDADO.setter
    def ESTADO_CONSOLIDADO(self, ESTADO_CONSOLIDADO: str):
        self.__ESTADO_CONSOLIDADO = ESTADO_CONSOLIDADO

    @property
    def ESTADO_IMPRESION(self) -> str:
        return self.__ESTADO_IMPRESION

    @ESTADO_IMPRESION.setter
    def ESTADO_IMPRESION(self, ESTADO_IMPRESION: str):
        self.__ESTADO_IMPRESION = ESTADO_IMPRESION

    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def REGISTRO_CONSOLIDADO(self) -> str:
        return self.__REGISTRO_CONSOLIDADO

    @REGISTRO_CONSOLIDADO.setter
    def REGISTRO_CONSOLIDADO(self, REGISTRO_CONSOLIDADO: str):
        self.__REGISTRO_CONSOLIDADO = REGISTRO_CONSOLIDADO

    @property
    def TOTAL_RECAUDO_DESPACHO(self) -> str:
        return self.__TOTAL_RECAUDO_DESPACHO

    @TOTAL_RECAUDO_DESPACHO.setter
    def TOTAL_RECAUDO_DESPACHO(self, TOTAL_RECAUDO_DESPACHO: str):
        self.__TOTAL_RECAUDO_DESPACHO = TOTAL_RECAUDO_DESPACHO

    @property
    def TOTAL_RECAUDO_BRUTO(self) -> str:
        return self.__TOTAL_RECAUDO_BRUTO

    @TOTAL_RECAUDO_BRUTO.setter
    def TOTAL_RECAUDO_BRUTO(self, TOTAL_RECAUDO_BRUTO: str):
        self.__TOTAL_RECAUDO_BRUTO = TOTAL_RECAUDO_BRUTO

class gestionmodelosconsultas_resultcotracir_Trama(ElementoModeloResultado):

    def __init__(self, ID: str, CADENA_TRAMA: str):
        self.ID = ID
        self.CADENA_TRAMA = CADENA_TRAMA
        
    @property
    def CADENA_TRAMA(self) -> str:
        return self.__CADENA_TRAMA

    @CADENA_TRAMA.setter
    def CADENA_TRAMA(self, CADENA_TRAMA: str):
        self.__CADENA_TRAMA = CADENA_TRAMA

    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

class gestionmodelosconsultas_resultcotracir_Transaccion(ElementoModeloResultado):

    def __init__(self, ESTADO_TRANSACCION: str, HORA: str, TIPO: str, DESCRIPCION: str, CATEGORIA: str, ID: str, VALOR: str):
        self.ESTADO_TRANSACCION = ESTADO_TRANSACCION
        self.HORA = HORA
        self.TIPO = TIPO
        self.DESCRIPCION = DESCRIPCION
        self.CATEGORIA = CATEGORIA
        self.ID = ID
        self.VALOR = VALOR
        
    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

    @property
    def TIPO(self) -> str:
        return self.__TIPO

    @TIPO.setter
    def TIPO(self, TIPO: str):
        self.__TIPO = TIPO

    @property
    def VALOR(self) -> str:
        return self.__VALOR

    @VALOR.setter
    def VALOR(self, VALOR: str):
        self.__VALOR = VALOR

    @property
    def DESCRIPCION(self) -> str:
        return self.__DESCRIPCION

    @DESCRIPCION.setter
    def DESCRIPCION(self, DESCRIPCION: str):
        self.__DESCRIPCION = DESCRIPCION

    @property
    def ESTADO_TRANSACCION(self) -> str:
        return self.__ESTADO_TRANSACCION

    @ESTADO_TRANSACCION.setter
    def ESTADO_TRANSACCION(self, ESTADO_TRANSACCION: str):
        self.__ESTADO_TRANSACCION = ESTADO_TRANSACCION

    @property
    def HORA(self) -> str:
        return self.__HORA

    @HORA.setter
    def HORA(self, HORA: str):
        self.__HORA = HORA

    @property
    def CATEGORIA(self) -> str:
        return self.__CATEGORIA

    @CATEGORIA.setter
    def CATEGORIA(self, CATEGORIA: str):
        self.__CATEGORIA = CATEGORIA

class gestionmodelosconsultas_resultset_ResultElement(ABC):

    pass
class resultset_ElementoModeloResultado:

    pass
class ResultElement:

    pass
class gestionmodelosconsultas_resultset_ElementoModeloResultado(ResultElement):

    def __init__(self, key: str, resultset135: set["resultset_ElementoModeloResultado"] = None, resultset138: "resultset_ElementoModeloResultado" = None):
        self.key = key
        self.resultset135 = resultset135 if resultset135 is not None else set()
        self.resultset138 = resultset138
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def resultset135(self):
        return self.__resultset135

    @resultset135.setter
    def resultset135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_resultset_ElementoModeloResultado__resultset135", None)
        self.__resultset135 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "modeloconsultas136"):
                    opp_val = getattr(item, "modeloconsultas136", None)
                    
                    if opp_val == self:
                        setattr(item, "modeloconsultas136", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "modeloconsultas136"):
                    opp_val = getattr(item, "modeloconsultas136", None)
                    
                    setattr(item, "modeloconsultas136", self)
                    

    @property
    def resultset138(self):
        return self.__resultset138

    @resultset138.setter
    def resultset138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_resultset_ElementoModeloResultado__resultset138", None)
        self.__resultset138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modeloconsultas139"):
                opp_val = getattr(old_value, "modeloconsultas139", None)
                if opp_val == self:
                    setattr(old_value, "modeloconsultas139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modeloconsultas139"):
                opp_val = getattr(value, "modeloconsultas139", None)
                setattr(value, "modeloconsultas139", self)

class resultset_ResultElement:

    pass
class gestionmodelosconsultas_resultset_Resultado:

    def __init__(self, nombre: str, ModeloConsulta129: "ModeloConsulta" = None, resultset132: set["resultset_ResultElement"] = None):
        self.nombre = nombre
        self.ModeloConsulta129 = ModeloConsulta129
        self.resultset132 = resultset132 if resultset132 is not None else set()
        
    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def ModeloConsulta129(self):
        return self.__ModeloConsulta129

    @ModeloConsulta129.setter
    def ModeloConsulta129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_resultset_Resultado__ModeloConsulta129", None)
        self.__ModeloConsulta129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modeloconsultas130"):
                opp_val = getattr(old_value, "modeloconsultas130", None)
                if opp_val == self:
                    setattr(old_value, "modeloconsultas130", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modeloconsultas130"):
                opp_val = getattr(value, "modeloconsultas130", None)
                setattr(value, "modeloconsultas130", self)

    @property
    def resultset132(self):
        return self.__resultset132

    @resultset132.setter
    def resultset132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_resultset_Resultado__resultset132", None)
        self.__resultset132 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "modeloconsultas133"):
                    opp_val = getattr(item, "modeloconsultas133", None)
                    
                    if opp_val == self:
                        setattr(item, "modeloconsultas133", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "modeloconsultas133"):
                    opp_val = getattr(item, "modeloconsultas133", None)
                    
                    setattr(item, "modeloconsultas133", self)
                    

class model_ElementoModelo:

    pass
class gestionmodelosconsultas_model_Campo:

    def __init__(self, nombreCampo: str, criterio: str, seleccion: bool, model105: "model_ElementoConsulta" = None):
        self.nombreCampo = nombreCampo
        self.criterio = criterio
        self.seleccion = seleccion
        self.model105 = model105
        
    @property
    def nombreCampo(self) -> str:
        return self.__nombreCampo

    @nombreCampo.setter
    def nombreCampo(self, nombreCampo: str):
        self.__nombreCampo = nombreCampo

    @property
    def criterio(self) -> str:
        return self.__criterio

    @criterio.setter
    def criterio(self, criterio: str):
        self.__criterio = criterio

    @property
    def seleccion(self) -> bool:
        return self.__seleccion

    @seleccion.setter
    def seleccion(self, seleccion: bool):
        self.__seleccion = seleccion

    @property
    def model105(self):
        return self.__model105

    @model105.setter
    def model105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_model_Campo__model105", None)
        self.__model105 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modeloconsultas106"):
                opp_val = getattr(old_value, "modeloconsultas106", None)
                if opp_val == self:
                    setattr(old_value, "modeloconsultas106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modeloconsultas106"):
                opp_val = getattr(value, "modeloconsultas106", None)
                setattr(value, "modeloconsultas106", self)

class model_ElementoConsulta:

    pass
class ElementoModelo:

    pass
class gestionmodelosconsultas_model_ElementoConsulta(ElementoModelo):

    def __init__(self, order: str, model117: "model_EADiagram" = None, model120: set["model_Campo"] = None):
        self.order = order
        self.model117 = model117
        self.model120 = model120 if model120 is not None else set()
        
    @property
    def order(self) -> str:
        return self.__order

    @order.setter
    def order(self, order: str):
        self.__order = order

    @property
    def model117(self):
        return self.__model117

    @model117.setter
    def model117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_model_ElementoConsulta__model117", None)
        self.__model117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modeloconsultas118"):
                opp_val = getattr(old_value, "modeloconsultas118", None)
                if opp_val == self:
                    setattr(old_value, "modeloconsultas118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modeloconsultas118"):
                opp_val = getattr(value, "modeloconsultas118", None)
                setattr(value, "modeloconsultas118", self)

    @property
    def model120(self):
        return self.__model120

    @model120.setter
    def model120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_model_ElementoConsulta__model120", None)
        self.__model120 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "modeloconsultas121"):
                    opp_val = getattr(item, "modeloconsultas121", None)
                    
                    if opp_val == self:
                        setattr(item, "modeloconsultas121", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "modeloconsultas121"):
                    opp_val = getattr(item, "modeloconsultas121", None)
                    
                    setattr(item, "modeloconsultas121", self)
                    

class gestionmodelosconsultas_model_Relacion(ElementoModelo):

    def __init__(self, estereotipo: str, order: str, model98: "model_EADiagram" = None, gestionmodelosconsultas_model_Relacion: "model_ElementoConsulta" = None, gestionmodelosconsultas_model_Relacion102: "model_ElementoConsulta" = None):
        self.estereotipo = estereotipo
        self.order = order
        self.model98 = model98
        self.gestionmodelosconsultas_model_Relacion = gestionmodelosconsultas_model_Relacion
        self.gestionmodelosconsultas_model_Relacion102 = gestionmodelosconsultas_model_Relacion102
        
    @property
    def order(self) -> str:
        return self.__order

    @order.setter
    def order(self, order: str):
        self.__order = order

    @property
    def estereotipo(self) -> str:
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
    def gestionmodelosconsultas_model_Relacion102(self):
        return self.__gestionmodelosconsultas_model_Relacion102

    @gestionmodelosconsultas_model_Relacion102.setter
    def gestionmodelosconsultas_model_Relacion102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_model_Relacion__gestionmodelosconsultas_model_Relacion102", None)
        self.__gestionmodelosconsultas_model_Relacion102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ElementoConsulta103"):
                opp_val = getattr(old_value, "model_ElementoConsulta103", None)
                if opp_val == self:
                    setattr(old_value, "model_ElementoConsulta103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ElementoConsulta103"):
                opp_val = getattr(value, "model_ElementoConsulta103", None)
                setattr(value, "model_ElementoConsulta103", self)

    @property
    def model98(self):
        return self.__model98

    @model98.setter
    def model98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_model_Relacion__model98", None)
        self.__model98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modeloconsultas99"):
                opp_val = getattr(old_value, "modeloconsultas99", None)
                if opp_val == self:
                    setattr(old_value, "modeloconsultas99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modeloconsultas99"):
                opp_val = getattr(value, "modeloconsultas99", None)
                setattr(value, "modeloconsultas99", self)

class modeloconsultas_gestionmodelosconsultas_ModelFactory:

    pass
class gestionmodelosconsultas_modeloconsultas_FactoryModeloConsulta:

    pass
class gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute:

    def __init__(self, nombre: str, ElementoRealizacionDiagramEntity65: "ElementoRealizacionDiagramEntity" = None, Value68: set["Value"] = None, Attribute62: set["Attribute"] = None):
        self.nombre = nombre
        self.ElementoRealizacionDiagramEntity65 = ElementoRealizacionDiagramEntity65
        self.Value68 = Value68 if Value68 is not None else set()
        self.Attribute62 = Attribute62 if Attribute62 is not None else set()
        
    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def Attribute62(self):
        return self.__Attribute62

    @Attribute62.setter
    def Attribute62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute__Attribute62", None)
        self.__Attribute62 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "entitymodel63"):
                    opp_val = getattr(item, "entitymodel63", None)
                    
                    if opp_val == self:
                        setattr(item, "entitymodel63", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "entitymodel63"):
                    opp_val = getattr(item, "entitymodel63", None)
                    
                    setattr(item, "entitymodel63", self)
                    

    @property
    def ElementoRealizacionDiagramEntity65(self):
        return self.__ElementoRealizacionDiagramEntity65

    @ElementoRealizacionDiagramEntity65.setter
    def ElementoRealizacionDiagramEntity65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute__ElementoRealizacionDiagramEntity65", None)
        self.__ElementoRealizacionDiagramEntity65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entitymodel66"):
                opp_val = getattr(old_value, "entitymodel66", None)
                if opp_val == self:
                    setattr(old_value, "entitymodel66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entitymodel66"):
                opp_val = getattr(value, "entitymodel66", None)
                setattr(value, "entitymodel66", self)

    @property
    def Value68(self):
        return self.__Value68

    @Value68.setter
    def Value68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_entitymodel_ElementoRealizacionValueAttribute__Value68", None)
        self.__Value68 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "entitymodel69"):
                    opp_val = getattr(item, "entitymodel69", None)
                    
                    if opp_val == self:
                        setattr(item, "entitymodel69", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "entitymodel69"):
                    opp_val = getattr(item, "entitymodel69", None)
                    
                    setattr(item, "entitymodel69", self)
                    

class RealizacionDiagramEntity:

    pass
class gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity:

    def __init__(self, tipo: str, nombreModelElementEntity: str, ModelElementEntity: "ModelElementEntity" = None, RealizacionDiagramEntity: "RealizacionDiagramEntity" = None, ElementoRealizacionValueAttribute59: set["ElementoRealizacionValueAttribute"] = None):
        self.tipo = tipo
        self.nombreModelElementEntity = nombreModelElementEntity
        self.ModelElementEntity = ModelElementEntity
        self.RealizacionDiagramEntity = RealizacionDiagramEntity
        self.ElementoRealizacionValueAttribute59 = ElementoRealizacionValueAttribute59 if ElementoRealizacionValueAttribute59 is not None else set()
        
    @property
    def tipo(self) -> str:
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo: str):
        self.__tipo = tipo

    @property
    def nombreModelElementEntity(self) -> str:
        return self.__nombreModelElementEntity

    @nombreModelElementEntity.setter
    def nombreModelElementEntity(self, nombreModelElementEntity: str):
        self.__nombreModelElementEntity = nombreModelElementEntity

    @property
    def ModelElementEntity(self):
        return self.__ModelElementEntity

    @ModelElementEntity.setter
    def ModelElementEntity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity__ModelElementEntity", None)
        self.__ModelElementEntity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entitymodel55"):
                opp_val = getattr(old_value, "entitymodel55", None)
                if opp_val == self:
                    setattr(old_value, "entitymodel55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entitymodel55"):
                opp_val = getattr(value, "entitymodel55", None)
                setattr(value, "entitymodel55", self)

    @property
    def ElementoRealizacionValueAttribute59(self):
        return self.__ElementoRealizacionValueAttribute59

    @ElementoRealizacionValueAttribute59.setter
    def ElementoRealizacionValueAttribute59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity__ElementoRealizacionValueAttribute59", None)
        self.__ElementoRealizacionValueAttribute59 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "entitymodel60"):
                    opp_val = getattr(item, "entitymodel60", None)
                    
                    if opp_val == self:
                        setattr(item, "entitymodel60", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "entitymodel60"):
                    opp_val = getattr(item, "entitymodel60", None)
                    
                    setattr(item, "entitymodel60", self)
                    

    @property
    def RealizacionDiagramEntity(self):
        return self.__RealizacionDiagramEntity

    @RealizacionDiagramEntity.setter
    def RealizacionDiagramEntity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity__RealizacionDiagramEntity", None)
        self.__RealizacionDiagramEntity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entitymodel57"):
                opp_val = getattr(old_value, "entitymodel57", None)
                if opp_val == self:
                    setattr(old_value, "entitymodel57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entitymodel57"):
                opp_val = getattr(value, "entitymodel57", None)
                setattr(value, "entitymodel57", self)

class Value:

    pass
class resultset_Resultado:

    pass
class model_EADiagram:

    pass
class gestionmodelosconsultas_modeloconsultas_ModeloConsulta:

    def __init__(self, nombre: str, RealizacionDiagramEntity83: "RealizacionDiagramEntity" = None, FactoryModeloConsulta86: "FactoryModeloConsulta" = None, model: set["model_EADiagram"] = None, resultset: set["resultset_Resultado"] = None):
        self.nombre = nombre
        self.RealizacionDiagramEntity83 = RealizacionDiagramEntity83
        self.FactoryModeloConsulta86 = FactoryModeloConsulta86
        self.model = model if model is not None else set()
        self.resultset = resultset if resultset is not None else set()
        
    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def FactoryModeloConsulta86(self):
        return self.__FactoryModeloConsulta86

    @FactoryModeloConsulta86.setter
    def FactoryModeloConsulta86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_modeloconsultas_ModeloConsulta__FactoryModeloConsulta86", None)
        self.__FactoryModeloConsulta86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modeloconsultas87"):
                opp_val = getattr(old_value, "modeloconsultas87", None)
                if opp_val == self:
                    setattr(old_value, "modeloconsultas87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modeloconsultas87"):
                opp_val = getattr(value, "modeloconsultas87", None)
                setattr(value, "modeloconsultas87", self)

    @property
    def RealizacionDiagramEntity83(self):
        return self.__RealizacionDiagramEntity83

    @RealizacionDiagramEntity83.setter
    def RealizacionDiagramEntity83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_modeloconsultas_ModeloConsulta__RealizacionDiagramEntity83", None)
        self.__RealizacionDiagramEntity83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entitymodel84"):
                opp_val = getattr(old_value, "entitymodel84", None)
                if opp_val == self:
                    setattr(old_value, "entitymodel84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entitymodel84"):
                opp_val = getattr(value, "entitymodel84", None)
                setattr(value, "entitymodel84", self)

    @property
    def resultset(self):
        return self.__resultset

    @resultset.setter
    def resultset(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_modeloconsultas_ModeloConsulta__resultset", None)
        self.__resultset = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "modeloconsultas91"):
                    opp_val = getattr(item, "modeloconsultas91", None)
                    
                    if opp_val == self:
                        setattr(item, "modeloconsultas91", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "modeloconsultas91"):
                    opp_val = getattr(item, "modeloconsultas91", None)
                    
                    setattr(item, "modeloconsultas91", self)
                    

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_modeloconsultas_ModeloConsulta__model", None)
        self.__model = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "modeloconsultas89"):
                    opp_val = getattr(item, "modeloconsultas89", None)
                    
                    if opp_val == self:
                        setattr(item, "modeloconsultas89", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "modeloconsultas89"):
                    opp_val = getattr(item, "modeloconsultas89", None)
                    
                    setattr(item, "modeloconsultas89", self)
                    

class gestionmodelosconsultas_entitymodel_Value:

    def __init__(self, value: str, ElementoRealizacionValueAttribute77: set["ElementoRealizacionValueAttribute"] = None, RealizacionDiagramEntity80: "RealizacionDiagramEntity" = None):
        self.value = value
        self.ElementoRealizacionValueAttribute77 = ElementoRealizacionValueAttribute77 if ElementoRealizacionValueAttribute77 is not None else set()
        self.RealizacionDiagramEntity80 = RealizacionDiagramEntity80
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def RealizacionDiagramEntity80(self):
        return self.__RealizacionDiagramEntity80

    @RealizacionDiagramEntity80.setter
    def RealizacionDiagramEntity80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_entitymodel_Value__RealizacionDiagramEntity80", None)
        self.__RealizacionDiagramEntity80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entitymodel81"):
                opp_val = getattr(old_value, "entitymodel81", None)
                if opp_val == self:
                    setattr(old_value, "entitymodel81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entitymodel81"):
                opp_val = getattr(value, "entitymodel81", None)
                setattr(value, "entitymodel81", self)

    @property
    def ElementoRealizacionValueAttribute77(self):
        return self.__ElementoRealizacionValueAttribute77

    @ElementoRealizacionValueAttribute77.setter
    def ElementoRealizacionValueAttribute77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_entitymodel_Value__ElementoRealizacionValueAttribute77", None)
        self.__ElementoRealizacionValueAttribute77 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "entitymodel78"):
                    opp_val = getattr(item, "entitymodel78", None)
                    
                    if opp_val == self:
                        setattr(item, "entitymodel78", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "entitymodel78"):
                    opp_val = getattr(item, "entitymodel78", None)
                    
                    setattr(item, "entitymodel78", self)
                    

class gestionmodelosconsultas_entitymodel_ElementoRealizacionVisibleAttribute:

    def __init__(self, nombre: str, RealizacionDiagramEntity71: "RealizacionDiagramEntity" = None, Attribute74: set["Attribute"] = None):
        self.nombre = nombre
        self.RealizacionDiagramEntity71 = RealizacionDiagramEntity71
        self.Attribute74 = Attribute74 if Attribute74 is not None else set()
        
    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre

    @property
    def RealizacionDiagramEntity71(self):
        return self.__RealizacionDiagramEntity71

    @RealizacionDiagramEntity71.setter
    def RealizacionDiagramEntity71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_entitymodel_ElementoRealizacionVisibleAttribute__RealizacionDiagramEntity71", None)
        self.__RealizacionDiagramEntity71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entitymodel72"):
                opp_val = getattr(old_value, "entitymodel72", None)
                if opp_val == self:
                    setattr(old_value, "entitymodel72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entitymodel72"):
                opp_val = getattr(value, "entitymodel72", None)
                setattr(value, "entitymodel72", self)

    @property
    def Attribute74(self):
        return self.__Attribute74

    @Attribute74.setter
    def Attribute74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_entitymodel_ElementoRealizacionVisibleAttribute__Attribute74", None)
        self.__Attribute74 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "entitymodel75"):
                    opp_val = getattr(item, "entitymodel75", None)
                    
                    if opp_val == self:
                        setattr(item, "entitymodel75", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "entitymodel75"):
                    opp_val = getattr(item, "entitymodel75", None)
                    
                    setattr(item, "entitymodel75", self)
                    

class gestionmodelosconsultas_entitymodel_Attribute:

    def __init__(self, name: str, type: str, value: str, visible: bool, attributeType: str, ElementoRealizacionValueAttribute: set["ElementoRealizacionValueAttribute"] = None, ElementoRealizacionVisibleAttribute: set["ElementoRealizacionVisibleAttribute"] = None, Entity29: "Entity" = None):
        self.name = name
        self.type = type
        self.value = value
        self.visible = visible
        self.attributeType = attributeType
        self.ElementoRealizacionValueAttribute = ElementoRealizacionValueAttribute if ElementoRealizacionValueAttribute is not None else set()
        self.ElementoRealizacionVisibleAttribute = ElementoRealizacionVisibleAttribute if ElementoRealizacionVisibleAttribute is not None else set()
        self.Entity29 = Entity29
        
    @property
    def attributeType(self) -> str:
        return self.__attributeType

    @attributeType.setter
    def attributeType(self, attributeType: str):
        self.__attributeType = attributeType

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def visible(self) -> bool:
        return self.__visible

    @visible.setter
    def visible(self, visible: bool):
        self.__visible = visible

    @property
    def ElementoRealizacionValueAttribute(self):
        return self.__ElementoRealizacionValueAttribute

    @ElementoRealizacionValueAttribute.setter
    def ElementoRealizacionValueAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_entitymodel_Attribute__ElementoRealizacionValueAttribute", None)
        self.__ElementoRealizacionValueAttribute = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "entitymodel32"):
                    opp_val = getattr(item, "entitymodel32", None)
                    
                    if opp_val == self:
                        setattr(item, "entitymodel32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "entitymodel32"):
                    opp_val = getattr(item, "entitymodel32", None)
                    
                    setattr(item, "entitymodel32", self)
                    

    @property
    def Entity29(self):
        return self.__Entity29

    @Entity29.setter
    def Entity29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_entitymodel_Attribute__Entity29", None)
        self.__Entity29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entitymodel30"):
                opp_val = getattr(old_value, "entitymodel30", None)
                if opp_val == self:
                    setattr(old_value, "entitymodel30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entitymodel30"):
                opp_val = getattr(value, "entitymodel30", None)
                setattr(value, "entitymodel30", self)

    @property
    def ElementoRealizacionVisibleAttribute(self):
        return self.__ElementoRealizacionVisibleAttribute

    @ElementoRealizacionVisibleAttribute.setter
    def ElementoRealizacionVisibleAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_entitymodel_Attribute__ElementoRealizacionVisibleAttribute", None)
        self.__ElementoRealizacionVisibleAttribute = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "entitymodel34"):
                    opp_val = getattr(item, "entitymodel34", None)
                    
                    if opp_val == self:
                        setattr(item, "entitymodel34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "entitymodel34"):
                    opp_val = getattr(item, "entitymodel34", None)
                    
                    setattr(item, "entitymodel34", self)
                    

class EntityRelation:

    pass
class gestionmodelosconsultas_entitymodel_SimpleRelation(EntityRelation):

    pass
class Entity:

    pass
class gestionmodelosconsultas_entitymodel_AssociativeEntity(Entity):

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

    def __init__(self, name: str, stereotype: str, ElementoRealizacionDiagramEntity: set["ElementoRealizacionDiagramEntity"] = None):
        self.name = name
        self.stereotype = stereotype
        self.ElementoRealizacionDiagramEntity = ElementoRealizacionDiagramEntity if ElementoRealizacionDiagramEntity is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def stereotype(self) -> str:
        return self.__stereotype

    @stereotype.setter
    def stereotype(self, stereotype: str):
        self.__stereotype = stereotype

    @property
    def ElementoRealizacionDiagramEntity(self):
        return self.__ElementoRealizacionDiagramEntity

    @ElementoRealizacionDiagramEntity.setter
    def ElementoRealizacionDiagramEntity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_entitymodel_ModelElementEntity__ElementoRealizacionDiagramEntity", None)
        self.__ElementoRealizacionDiagramEntity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "entitymodel36"):
                    opp_val = getattr(item, "entitymodel36", None)
                    
                    if opp_val == self:
                        setattr(item, "entitymodel36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "entitymodel36"):
                    opp_val = getattr(item, "entitymodel36", None)
                    
                    setattr(item, "entitymodel36", self)
                    

class ElementoRealizacionVisibleAttribute:

    pass
class ElementoRealizacionValueAttribute:

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

    def __init__(self, factoryrules: "factoryrules_RulesFactory" = None, FactoryModeloConsulta: "FactoryModeloConsulta" = None, DiagramEntity: "DiagramEntity" = None):
        self.factoryrules = factoryrules
        self.FactoryModeloConsulta = FactoryModeloConsulta
        self.DiagramEntity = DiagramEntity
        
    @property
    def factoryrules(self):
        return self.__factoryrules

    @factoryrules.setter
    def factoryrules(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_ModelFactory__factoryrules", None)
        self.__factoryrules = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rules"):
                opp_val = getattr(old_value, "rules", None)
                if opp_val == self:
                    setattr(old_value, "rules", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rules"):
                opp_val = getattr(value, "rules", None)
                setattr(value, "rules", self)

    @property
    def DiagramEntity(self):
        return self.__DiagramEntity

    @DiagramEntity.setter
    def DiagramEntity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_ModelFactory__DiagramEntity", None)
        self.__DiagramEntity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entitymodel"):
                opp_val = getattr(old_value, "entitymodel", None)
                if opp_val == self:
                    setattr(old_value, "entitymodel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entitymodel"):
                opp_val = getattr(value, "entitymodel", None)
                setattr(value, "entitymodel", self)

    @property
    def FactoryModeloConsulta(self):
        return self.__FactoryModeloConsulta

    @FactoryModeloConsulta.setter
    def FactoryModeloConsulta(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_ModelFactory__FactoryModeloConsulta", None)
        self.__FactoryModeloConsulta = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "modeloconsultas"):
                opp_val = getattr(old_value, "modeloconsultas", None)
                if opp_val == self:
                    setattr(old_value, "modeloconsultas", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "modeloconsultas"):
                opp_val = getattr(value, "modeloconsultas", None)
                setattr(value, "modeloconsultas", self)

    def salvar(self):
        # TODO: Implement salvar method
        pass

    def cargar(self) -> str:
        # TODO: Implement cargar method
        pass

class Attribute:

    pass
class ModelElementEntity:

    pass
class gestionmodelosconsultas_entitymodel_EntityRelation(ModelElementEntity):

    def __init__(self, atributteForeingKeySource: str, atributtePrimaryKeyTarget: str, multiplicitySource: str, multiplicityTarget: str, DiagramEntity22: "DiagramEntity" = None, gestionmodelosconsultas_entitymodel_EntityRelation: "Entity" = None, gestionmodelosconsultas_entitymodel_EntityRelation26: "Entity" = None, entitymodel55: "gestionmodelosconsultas_entitymodel_ElementoRealizacionDiagramEntity"):
        self.atributteForeingKeySource = atributteForeingKeySource
        self.atributtePrimaryKeyTarget = atributtePrimaryKeyTarget
        self.multiplicitySource = multiplicitySource
        self.multiplicityTarget = multiplicityTarget
        self.DiagramEntity22 = DiagramEntity22
        self.gestionmodelosconsultas_entitymodel_EntityRelation = gestionmodelosconsultas_entitymodel_EntityRelation
        self.gestionmodelosconsultas_entitymodel_EntityRelation26 = gestionmodelosconsultas_entitymodel_EntityRelation26
        
    @property
    def multiplicityTarget(self) -> str:
        return self.__multiplicityTarget

    @multiplicityTarget.setter
    def multiplicityTarget(self, multiplicityTarget: str):
        self.__multiplicityTarget = multiplicityTarget

    @property
    def atributtePrimaryKeyTarget(self) -> str:
        return self.__atributtePrimaryKeyTarget

    @atributtePrimaryKeyTarget.setter
    def atributtePrimaryKeyTarget(self, atributtePrimaryKeyTarget: str):
        self.__atributtePrimaryKeyTarget = atributtePrimaryKeyTarget

    @property
    def multiplicitySource(self) -> str:
        return self.__multiplicitySource

    @multiplicitySource.setter
    def multiplicitySource(self, multiplicitySource: str):
        self.__multiplicitySource = multiplicitySource

    @property
    def atributteForeingKeySource(self) -> str:
        return self.__atributteForeingKeySource

    @atributteForeingKeySource.setter
    def atributteForeingKeySource(self, atributteForeingKeySource: str):
        self.__atributteForeingKeySource = atributteForeingKeySource

    @property
    def DiagramEntity22(self):
        return self.__DiagramEntity22

    @DiagramEntity22.setter
    def DiagramEntity22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_entitymodel_EntityRelation__DiagramEntity22", None)
        self.__DiagramEntity22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "entitymodel23"):
                opp_val = getattr(old_value, "entitymodel23", None)
                if opp_val == self:
                    setattr(old_value, "entitymodel23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "entitymodel23"):
                opp_val = getattr(value, "entitymodel23", None)
                setattr(value, "entitymodel23", self)

    @property
    def gestionmodelosconsultas_entitymodel_EntityRelation26(self):
        return self.__gestionmodelosconsultas_entitymodel_EntityRelation26

    @gestionmodelosconsultas_entitymodel_EntityRelation26.setter
    def gestionmodelosconsultas_entitymodel_EntityRelation26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_entitymodel_EntityRelation__gestionmodelosconsultas_entitymodel_EntityRelation26", None)
        self.__gestionmodelosconsultas_entitymodel_EntityRelation26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Entity27"):
                opp_val = getattr(old_value, "Entity27", None)
                if opp_val == self:
                    setattr(old_value, "Entity27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Entity27"):
                opp_val = getattr(value, "Entity27", None)
                setattr(value, "Entity27", self)

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
            if hasattr(old_value, "Entity"):
                opp_val = getattr(old_value, "Entity", None)
                if opp_val == self:
                    setattr(old_value, "Entity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Entity"):
                opp_val = getattr(value, "Entity", None)
                setattr(value, "Entity", self)

class gestionmodelosconsultas_entitymodel_Entity(ModelElementEntity):

    pass
class ChildRule:

    pass
class gestionmodelosconsultas_factoryrules_RelationName(ChildRule):

    pass
class gestionmodelosconsultas_factoryrules_EntityName(ChildRule):

    pass
class gestionmodelosconsultas_factoryrules_ChildRule(ABC):

    def __init__(self, name: str, factoryrules14: "factoryrules_Rule" = None):
        self.name = name
        self.factoryrules14 = factoryrules14
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def factoryrules14(self):
        return self.__factoryrules14

    @factoryrules14.setter
    def factoryrules14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_factoryrules_ChildRule__factoryrules14", None)
        self.__factoryrules14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rules15"):
                opp_val = getattr(old_value, "rules15", None)
                if opp_val == self:
                    setattr(old_value, "rules15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rules15"):
                opp_val = getattr(value, "rules15", None)
                setattr(value, "rules15", self)

class factoryrules_ChildRule:

    pass
class gestionmodelosconsultas_factoryrules_Rule:

    def __init__(self, name: str, factoryrules8: "factoryrules_RulesFactory" = None, factoryrules11: set["factoryrules_ChildRule"] = None):
        self.name = name
        self.factoryrules8 = factoryrules8
        self.factoryrules11 = factoryrules11 if factoryrules11 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def factoryrules11(self):
        return self.__factoryrules11

    @factoryrules11.setter
    def factoryrules11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_factoryrules_Rule__factoryrules11", None)
        self.__factoryrules11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "rules12"):
                    opp_val = getattr(item, "rules12", None)
                    
                    if opp_val == self:
                        setattr(item, "rules12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "rules12"):
                    opp_val = getattr(item, "rules12", None)
                    
                    setattr(item, "rules12", self)
                    

    @property
    def factoryrules8(self):
        return self.__factoryrules8

    @factoryrules8.setter
    def factoryrules8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gestionmodelosconsultas_factoryrules_Rule__factoryrules8", None)
        self.__factoryrules8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rules9"):
                opp_val = getattr(old_value, "rules9", None)
                if opp_val == self:
                    setattr(old_value, "rules9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rules9"):
                opp_val = getattr(value, "rules9", None)
                setattr(value, "rules9", self)
