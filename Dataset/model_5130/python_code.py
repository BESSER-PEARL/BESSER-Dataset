from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class CardinalidadeMaxima(Enum):
    OR = "OR"
    XOR = "XOR"
class Qualidade(Enum):
    Baixo = "Baixo"
    Alto = "Alto"
class OperadorRelacional(Enum):
    MAIOR = "MAIOR"
    MENOR = "MENOR"
    IGUAL = "IGUAL"
    MAIORIGUAL = "MAIORIGUAL"
    MENORIGUAL = "MENORIGUAL"
    DIFERENTE = "DIFERENTE"
class Origem(Enum):
    Sentida = "Sentida"
    Usuario = "Usuario"
    Perfil = "Perfil"
    Derivada = "Derivada"
class OperadorLogico(Enum):
    AND = "AND"
    OR = "OR"
class OperadorAcaoLogico(Enum):
    AND = "AND"
class TipoValor(Enum):
    TInteger = "TInteger"
    TString = "TString"
    TFloat = "TFloat"
    TBoolean = "TBoolean"
class Validade(Enum):
    Volatil = "Volatil"
    Frequente = "Frequente"
    Raramente = "Raramente"
    Permanente = "Permanente"
class Presenca(Enum):
    PRESENTE = "PRESENTE"
    AUSENTE = "AUSENTE"


############################################
# Definition of Classes
############################################

class caracteristica_Estado:

    def __init__(self, nome: str, safe: bool, caracteristica_Estado: "caracteristica_Simulacao" = None, caracteristica_Estado97: "caracteristica_Transicao" = None, caracteristica_Estado100: "caracteristica_Transicao" = None, caracteristica_Estado108: "caracteristica_CaracteristicaProduto" = None):
        self.nome = nome
        self.safe = safe
        self.caracteristica_Estado = caracteristica_Estado
        self.caracteristica_Estado97 = caracteristica_Estado97
        self.caracteristica_Estado100 = caracteristica_Estado100
        self.caracteristica_Estado108 = caracteristica_Estado108
        
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def safe(self) -> bool:
        return self.__safe

    @safe.setter
    def safe(self, safe: bool):
        self.__safe = safe

    @property
    def caracteristica_Estado108(self):
        return self.__caracteristica_Estado108

    @caracteristica_Estado108.setter
    def caracteristica_Estado108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Estado__caracteristica_Estado108", None)
        self.__caracteristica_Estado108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_CaracteristicaProduto109"):
                opp_val = getattr(old_value, "caracteristica_CaracteristicaProduto109", None)
                if opp_val == self:
                    setattr(old_value, "caracteristica_CaracteristicaProduto109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_CaracteristicaProduto109"):
                opp_val = getattr(value, "caracteristica_CaracteristicaProduto109", None)
                setattr(value, "caracteristica_CaracteristicaProduto109", self)

    @property
    def caracteristica_Estado100(self):
        return self.__caracteristica_Estado100

    @caracteristica_Estado100.setter
    def caracteristica_Estado100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Estado__caracteristica_Estado100", None)
        self.__caracteristica_Estado100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_Transicao99"):
                opp_val = getattr(old_value, "caracteristica_Transicao99", None)
                if opp_val == self:
                    setattr(old_value, "caracteristica_Transicao99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_Transicao99"):
                opp_val = getattr(value, "caracteristica_Transicao99", None)
                setattr(value, "caracteristica_Transicao99", self)

    @property
    def caracteristica_Estado(self):
        return self.__caracteristica_Estado

    @caracteristica_Estado.setter
    def caracteristica_Estado(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Estado__caracteristica_Estado", None)
        self.__caracteristica_Estado = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_Simulacao94"):
                opp_val = getattr(old_value, "caracteristica_Simulacao94", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_Simulacao94"):
                opp_val = getattr(value, "caracteristica_Simulacao94", None)
                if opp_val is None:
                    setattr(value, "caracteristica_Simulacao94", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def caracteristica_Estado97(self):
        return self.__caracteristica_Estado97

    @caracteristica_Estado97.setter
    def caracteristica_Estado97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Estado__caracteristica_Estado97", None)
        self.__caracteristica_Estado97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_Transicao96"):
                opp_val = getattr(old_value, "caracteristica_Transicao96", None)
                if opp_val == self:
                    setattr(old_value, "caracteristica_Transicao96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_Transicao96"):
                opp_val = getattr(value, "caracteristica_Transicao96", None)
                setattr(value, "caracteristica_Transicao96", self)

class caracteristica_Transicao:

    def __init__(self, safe: bool, etiqueta: str, caracteristica_Transicao: "caracteristica_Simulacao" = None, caracteristica_Transicao96: "caracteristica_Estado" = None, caracteristica_Transicao99: "caracteristica_Estado" = None, caracteristica_Transicao102: set["caracteristica_RegraDeComposicao"] = None, caracteristica_Transicao105: set["caracteristica_Acao"] = None):
        self.safe = safe
        self.etiqueta = etiqueta
        self.caracteristica_Transicao = caracteristica_Transicao
        self.caracteristica_Transicao96 = caracteristica_Transicao96
        self.caracteristica_Transicao99 = caracteristica_Transicao99
        self.caracteristica_Transicao102 = caracteristica_Transicao102 if caracteristica_Transicao102 is not None else set()
        self.caracteristica_Transicao105 = caracteristica_Transicao105 if caracteristica_Transicao105 is not None else set()
        
    @property
    def safe(self) -> bool:
        return self.__safe

    @safe.setter
    def safe(self, safe: bool):
        self.__safe = safe

    @property
    def etiqueta(self) -> str:
        return self.__etiqueta

    @etiqueta.setter
    def etiqueta(self, etiqueta: str):
        self.__etiqueta = etiqueta

    @property
    def caracteristica_Transicao99(self):
        return self.__caracteristica_Transicao99

    @caracteristica_Transicao99.setter
    def caracteristica_Transicao99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Transicao__caracteristica_Transicao99", None)
        self.__caracteristica_Transicao99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_Estado100"):
                opp_val = getattr(old_value, "caracteristica_Estado100", None)
                if opp_val == self:
                    setattr(old_value, "caracteristica_Estado100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_Estado100"):
                opp_val = getattr(value, "caracteristica_Estado100", None)
                setattr(value, "caracteristica_Estado100", self)

    @property
    def caracteristica_Transicao96(self):
        return self.__caracteristica_Transicao96

    @caracteristica_Transicao96.setter
    def caracteristica_Transicao96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Transicao__caracteristica_Transicao96", None)
        self.__caracteristica_Transicao96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_Estado97"):
                opp_val = getattr(old_value, "caracteristica_Estado97", None)
                if opp_val == self:
                    setattr(old_value, "caracteristica_Estado97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_Estado97"):
                opp_val = getattr(value, "caracteristica_Estado97", None)
                setattr(value, "caracteristica_Estado97", self)

    @property
    def caracteristica_Transicao(self):
        return self.__caracteristica_Transicao

    @caracteristica_Transicao.setter
    def caracteristica_Transicao(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Transicao__caracteristica_Transicao", None)
        self.__caracteristica_Transicao = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_Simulacao92"):
                opp_val = getattr(old_value, "caracteristica_Simulacao92", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_Simulacao92"):
                opp_val = getattr(value, "caracteristica_Simulacao92", None)
                if opp_val is None:
                    setattr(value, "caracteristica_Simulacao92", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def caracteristica_Transicao102(self):
        return self.__caracteristica_Transicao102

    @caracteristica_Transicao102.setter
    def caracteristica_Transicao102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Transicao__caracteristica_Transicao102", None)
        self.__caracteristica_Transicao102 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "caracteristica_RegraDeComposicao103"):
                    opp_val = getattr(item, "caracteristica_RegraDeComposicao103", None)
                    
                    if opp_val == self:
                        setattr(item, "caracteristica_RegraDeComposicao103", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "caracteristica_RegraDeComposicao103"):
                    opp_val = getattr(item, "caracteristica_RegraDeComposicao103", None)
                    
                    setattr(item, "caracteristica_RegraDeComposicao103", self)
                    

    @property
    def caracteristica_Transicao105(self):
        return self.__caracteristica_Transicao105

    @caracteristica_Transicao105.setter
    def caracteristica_Transicao105(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Transicao__caracteristica_Transicao105", None)
        self.__caracteristica_Transicao105 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "caracteristica_Acao106"):
                    opp_val = getattr(item, "caracteristica_Acao106", None)
                    
                    if opp_val == self:
                        setattr(item, "caracteristica_Acao106", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "caracteristica_Acao106"):
                    opp_val = getattr(item, "caracteristica_Acao106", None)
                    
                    setattr(item, "caracteristica_Acao106", self)
                    

class Acao:

    pass
class caracteristica_AcaoLogico(Acao):

    def __init__(self, operadorAcaoLogico: str, caracteristica_AcaoLogico: "caracteristica_Acao" = None, caracteristica_AcaoLogico77: "caracteristica_Acao" = None):
        self.operadorAcaoLogico = operadorAcaoLogico
        self.caracteristica_AcaoLogico = caracteristica_AcaoLogico
        self.caracteristica_AcaoLogico77 = caracteristica_AcaoLogico77
        
    @property
    def operadorAcaoLogico(self) -> str:
        return self.__operadorAcaoLogico

    @operadorAcaoLogico.setter
    def operadorAcaoLogico(self, operadorAcaoLogico: str):
        self.__operadorAcaoLogico = operadorAcaoLogico

    @property
    def caracteristica_AcaoLogico77(self):
        return self.__caracteristica_AcaoLogico77

    @caracteristica_AcaoLogico77.setter
    def caracteristica_AcaoLogico77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_AcaoLogico__caracteristica_AcaoLogico77", None)
        self.__caracteristica_AcaoLogico77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_Acao78"):
                opp_val = getattr(old_value, "caracteristica_Acao78", None)
                if opp_val == self:
                    setattr(old_value, "caracteristica_Acao78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_Acao78"):
                opp_val = getattr(value, "caracteristica_Acao78", None)
                setattr(value, "caracteristica_Acao78", self)

    @property
    def caracteristica_AcaoLogico(self):
        return self.__caracteristica_AcaoLogico

    @caracteristica_AcaoLogico.setter
    def caracteristica_AcaoLogico(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_AcaoLogico__caracteristica_AcaoLogico", None)
        self.__caracteristica_AcaoLogico = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_Acao75"):
                opp_val = getattr(old_value, "caracteristica_Acao75", None)
                if opp_val == self:
                    setattr(old_value, "caracteristica_Acao75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_Acao75"):
                opp_val = getattr(value, "caracteristica_Acao75", None)
                setattr(value, "caracteristica_Acao75", self)

class Antecedente:

    pass
class caracteristica_ExpressaoRelacional(Antecedente):

    def __init__(self, operadorRelacional: str, valor: str, caracteristica_ExpressaoRelacional: "caracteristica_Atributo" = None):
        self.operadorRelacional = operadorRelacional
        self.valor = valor
        self.caracteristica_ExpressaoRelacional = caracteristica_ExpressaoRelacional
        
    @property
    def operadorRelacional(self) -> str:
        return self.__operadorRelacional

    @operadorRelacional.setter
    def operadorRelacional(self, operadorRelacional: str):
        self.__operadorRelacional = operadorRelacional

    @property
    def valor(self) -> str:
        return self.__valor

    @valor.setter
    def valor(self, valor: str):
        self.__valor = valor

    @property
    def caracteristica_ExpressaoRelacional(self):
        return self.__caracteristica_ExpressaoRelacional

    @caracteristica_ExpressaoRelacional.setter
    def caracteristica_ExpressaoRelacional(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_ExpressaoRelacional__caracteristica_ExpressaoRelacional", None)
        self.__caracteristica_ExpressaoRelacional = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_Atributo88"):
                opp_val = getattr(old_value, "caracteristica_Atributo88", None)
                if opp_val == self:
                    setattr(old_value, "caracteristica_Atributo88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_Atributo88"):
                opp_val = getattr(value, "caracteristica_Atributo88", None)
                setattr(value, "caracteristica_Atributo88", self)

class caracteristica_LiteralComposicao(Antecedente):

    def __init__(self, presenca: str, caracteristica_LiteralComposicao: "caracteristica_ElementoCaracteristico" = None):
        self.presenca = presenca
        self.caracteristica_LiteralComposicao = caracteristica_LiteralComposicao
        
    @property
    def presenca(self) -> str:
        return self.__presenca

    @presenca.setter
    def presenca(self, presenca: str):
        self.__presenca = presenca

    @property
    def caracteristica_LiteralComposicao(self):
        return self.__caracteristica_LiteralComposicao

    @caracteristica_LiteralComposicao.setter
    def caracteristica_LiteralComposicao(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_LiteralComposicao__caracteristica_LiteralComposicao", None)
        self.__caracteristica_LiteralComposicao = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_ElementoCaracteristico90"):
                opp_val = getattr(old_value, "caracteristica_ElementoCaracteristico90", None)
                if opp_val == self:
                    setattr(old_value, "caracteristica_ElementoCaracteristico90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_ElementoCaracteristico90"):
                opp_val = getattr(value, "caracteristica_ElementoCaracteristico90", None)
                setattr(value, "caracteristica_ElementoCaracteristico90", self)

class caracteristica_ExpressaoLogica(Antecedente):

    def __init__(self, operadorLogico: str, caracteristica_ExpressaoLogica: "caracteristica_Antecedente" = None, caracteristica_ExpressaoLogica85: "caracteristica_Antecedente" = None):
        self.operadorLogico = operadorLogico
        self.caracteristica_ExpressaoLogica = caracteristica_ExpressaoLogica
        self.caracteristica_ExpressaoLogica85 = caracteristica_ExpressaoLogica85
        
    @property
    def operadorLogico(self) -> str:
        return self.__operadorLogico

    @operadorLogico.setter
    def operadorLogico(self, operadorLogico: str):
        self.__operadorLogico = operadorLogico

    @property
    def caracteristica_ExpressaoLogica85(self):
        return self.__caracteristica_ExpressaoLogica85

    @caracteristica_ExpressaoLogica85.setter
    def caracteristica_ExpressaoLogica85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_ExpressaoLogica__caracteristica_ExpressaoLogica85", None)
        self.__caracteristica_ExpressaoLogica85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_Antecedente86"):
                opp_val = getattr(old_value, "caracteristica_Antecedente86", None)
                if opp_val == self:
                    setattr(old_value, "caracteristica_Antecedente86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_Antecedente86"):
                opp_val = getattr(value, "caracteristica_Antecedente86", None)
                setattr(value, "caracteristica_Antecedente86", self)

    @property
    def caracteristica_ExpressaoLogica(self):
        return self.__caracteristica_ExpressaoLogica

    @caracteristica_ExpressaoLogica.setter
    def caracteristica_ExpressaoLogica(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_ExpressaoLogica__caracteristica_ExpressaoLogica", None)
        self.__caracteristica_ExpressaoLogica = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_Antecedente83"):
                opp_val = getattr(old_value, "caracteristica_Antecedente83", None)
                if opp_val == self:
                    setattr(old_value, "caracteristica_Antecedente83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_Antecedente83"):
                opp_val = getattr(value, "caracteristica_Antecedente83", None)
                setattr(value, "caracteristica_Antecedente83", self)

class caracteristica_Designar(Acao):

    def __init__(self, valor: str, tipoValor: str, caracteristica_Designar: "caracteristica_Atributo" = None, caracteristica_Designar118: "caracteristica_InconsistenciaRegraAdaptacao" = None):
        self.valor = valor
        self.tipoValor = tipoValor
        self.caracteristica_Designar = caracteristica_Designar
        self.caracteristica_Designar118 = caracteristica_Designar118
        
    @property
    def valor(self) -> str:
        return self.__valor

    @valor.setter
    def valor(self, valor: str):
        self.__valor = valor

    @property
    def tipoValor(self) -> str:
        return self.__tipoValor

    @tipoValor.setter
    def tipoValor(self, tipoValor: str):
        self.__tipoValor = tipoValor

    @property
    def caracteristica_Designar118(self):
        return self.__caracteristica_Designar118

    @caracteristica_Designar118.setter
    def caracteristica_Designar118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Designar__caracteristica_Designar118", None)
        self.__caracteristica_Designar118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_InconsistenciaRegraAdaptacao117"):
                opp_val = getattr(old_value, "caracteristica_InconsistenciaRegraAdaptacao117", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_InconsistenciaRegraAdaptacao117"):
                opp_val = getattr(value, "caracteristica_InconsistenciaRegraAdaptacao117", None)
                if opp_val is None:
                    setattr(value, "caracteristica_InconsistenciaRegraAdaptacao117", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def caracteristica_Designar(self):
        return self.__caracteristica_Designar

    @caracteristica_Designar.setter
    def caracteristica_Designar(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Designar__caracteristica_Designar", None)
        self.__caracteristica_Designar = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_Atributo81"):
                opp_val = getattr(old_value, "caracteristica_Atributo81", None)
                if opp_val == self:
                    setattr(old_value, "caracteristica_Atributo81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_Atributo81"):
                opp_val = getattr(value, "caracteristica_Atributo81", None)
                setattr(value, "caracteristica_Atributo81", self)

class caracteristica_LiteralAcao(Acao):

    def __init__(self, presenca: str, caracteristica_LiteralAcao: "caracteristica_ElementoCaracteristico" = None, caracteristica_LiteralAcao115: "caracteristica_InconsistenciaRegraAdaptacao" = None):
        self.presenca = presenca
        self.caracteristica_LiteralAcao = caracteristica_LiteralAcao
        self.caracteristica_LiteralAcao115 = caracteristica_LiteralAcao115
        
    @property
    def presenca(self) -> str:
        return self.__presenca

    @presenca.setter
    def presenca(self, presenca: str):
        self.__presenca = presenca

    @property
    def caracteristica_LiteralAcao115(self):
        return self.__caracteristica_LiteralAcao115

    @caracteristica_LiteralAcao115.setter
    def caracteristica_LiteralAcao115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_LiteralAcao__caracteristica_LiteralAcao115", None)
        self.__caracteristica_LiteralAcao115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_InconsistenciaRegraAdaptacao114"):
                opp_val = getattr(old_value, "caracteristica_InconsistenciaRegraAdaptacao114", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_InconsistenciaRegraAdaptacao114"):
                opp_val = getattr(value, "caracteristica_InconsistenciaRegraAdaptacao114", None)
                if opp_val is None:
                    setattr(value, "caracteristica_InconsistenciaRegraAdaptacao114", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def caracteristica_LiteralAcao(self):
        return self.__caracteristica_LiteralAcao

    @caracteristica_LiteralAcao.setter
    def caracteristica_LiteralAcao(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_LiteralAcao__caracteristica_LiteralAcao", None)
        self.__caracteristica_LiteralAcao = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_ElementoCaracteristico"):
                opp_val = getattr(old_value, "caracteristica_ElementoCaracteristico", None)
                if opp_val == self:
                    setattr(old_value, "caracteristica_ElementoCaracteristico", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_ElementoCaracteristico"):
                opp_val = getattr(value, "caracteristica_ElementoCaracteristico", None)
                setattr(value, "caracteristica_ElementoCaracteristico", self)

class Regra:

    pass
class caracteristica_RegraDeComposicao(Regra):

    pass
class Evento:

    pass
class caracteristica_EventoRelacional(Evento):

    def __init__(self, operadorRelacional: str, valor: str, caracteristica_EventoRelacional: "caracteristica_InformacaoDeContexto" = None):
        self.operadorRelacional = operadorRelacional
        self.valor = valor
        self.caracteristica_EventoRelacional = caracteristica_EventoRelacional
        
    @property
    def operadorRelacional(self) -> str:
        return self.__operadorRelacional

    @operadorRelacional.setter
    def operadorRelacional(self, operadorRelacional: str):
        self.__operadorRelacional = operadorRelacional

    @property
    def valor(self) -> str:
        return self.__valor

    @valor.setter
    def valor(self, valor: str):
        self.__valor = valor

    @property
    def caracteristica_EventoRelacional(self):
        return self.__caracteristica_EventoRelacional

    @caracteristica_EventoRelacional.setter
    def caracteristica_EventoRelacional(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_EventoRelacional__caracteristica_EventoRelacional", None)
        self.__caracteristica_EventoRelacional = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_InformacaoDeContexto"):
                opp_val = getattr(old_value, "caracteristica_InformacaoDeContexto", None)
                if opp_val == self:
                    setattr(old_value, "caracteristica_InformacaoDeContexto", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_InformacaoDeContexto"):
                opp_val = getattr(value, "caracteristica_InformacaoDeContexto", None)
                setattr(value, "caracteristica_InformacaoDeContexto", self)

class caracteristica_EventoLogico(Evento):

    def __init__(self, operadorLogico: str, caracteristica_EventoLogico: "caracteristica_Evento" = None, caracteristica_EventoLogico71: "caracteristica_Evento" = None):
        self.operadorLogico = operadorLogico
        self.caracteristica_EventoLogico = caracteristica_EventoLogico
        self.caracteristica_EventoLogico71 = caracteristica_EventoLogico71
        
    @property
    def operadorLogico(self) -> str:
        return self.__operadorLogico

    @operadorLogico.setter
    def operadorLogico(self, operadorLogico: str):
        self.__operadorLogico = operadorLogico

    @property
    def caracteristica_EventoLogico71(self):
        return self.__caracteristica_EventoLogico71

    @caracteristica_EventoLogico71.setter
    def caracteristica_EventoLogico71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_EventoLogico__caracteristica_EventoLogico71", None)
        self.__caracteristica_EventoLogico71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_Evento72"):
                opp_val = getattr(old_value, "caracteristica_Evento72", None)
                if opp_val == self:
                    setattr(old_value, "caracteristica_Evento72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_Evento72"):
                opp_val = getattr(value, "caracteristica_Evento72", None)
                setattr(value, "caracteristica_Evento72", self)

    @property
    def caracteristica_EventoLogico(self):
        return self.__caracteristica_EventoLogico

    @caracteristica_EventoLogico.setter
    def caracteristica_EventoLogico(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_EventoLogico__caracteristica_EventoLogico", None)
        self.__caracteristica_EventoLogico = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_Evento69"):
                opp_val = getattr(old_value, "caracteristica_Evento69", None)
                if opp_val == self:
                    setattr(old_value, "caracteristica_Evento69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_Evento69"):
                opp_val = getattr(value, "caracteristica_Evento69", None)
                setattr(value, "caracteristica_Evento69", self)

class Expressao:

    pass
class caracteristica_Antecedente(Expressao):

    pass
class caracteristica_Acao(Expressao):

    pass
class caracteristica_Evento(Expressao):

    pass
class caracteristica_RegraDeContexto(Regra):

    pass
class ElementoDeProduto:

    pass
class caracteristica_VarianteProduto(ElementoDeProduto):

    def __init__(self, selecionado: str, variantesProduto: "caracteristica_VariacaoProduto" = None, VarianteProduto: "caracteristica_VariacaoProduto" = None):
        self.selecionado = selecionado
        self.variantesProduto = variantesProduto
        self.VarianteProduto = VarianteProduto
        
    @property
    def selecionado(self) -> str:
        return self.__selecionado

    @selecionado.setter
    def selecionado(self, selecionado: str):
        self.__selecionado = selecionado

    @property
    def VarianteProduto(self):
        return self.__VarianteProduto

    @VarianteProduto.setter
    def VarianteProduto(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_VarianteProduto__VarianteProduto", None)
        self.__VarianteProduto = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "variacaoProdutoPai"):
                opp_val = getattr(old_value, "variacaoProdutoPai", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "variacaoProdutoPai"):
                opp_val = getattr(value, "variacaoProdutoPai", None)
                if opp_val is None:
                    setattr(value, "variacaoProdutoPai", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def variantesProduto(self):
        return self.__variantesProduto

    @variantesProduto.setter
    def variantesProduto(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_VarianteProduto__variantesProduto", None)
        self.__variantesProduto = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VariacaoProduto"):
                opp_val = getattr(old_value, "VariacaoProduto", None)
                if opp_val == self:
                    setattr(old_value, "VariacaoProduto", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VariacaoProduto"):
                opp_val = getattr(value, "VariacaoProduto", None)
                setattr(value, "VariacaoProduto", self)

class caracteristica_CaracteristicaProduto(ElementoDeProduto):

    pass
class caracteristica_VariacaoProduto(ElementoDeProduto):

    def __init__(self, cardinalidadeMinima: str, cardinalidadeMaxima: str, caracteristica_VariacaoProduto: "caracteristica_CaracteristicaProduto" = None, VariacaoProduto: "caracteristica_VarianteProduto" = None, variacaoProdutoPai: set["caracteristica_VarianteProduto"] = None):
        self.cardinalidadeMinima = cardinalidadeMinima
        self.cardinalidadeMaxima = cardinalidadeMaxima
        self.caracteristica_VariacaoProduto = caracteristica_VariacaoProduto
        self.VariacaoProduto = VariacaoProduto
        self.variacaoProdutoPai = variacaoProdutoPai if variacaoProdutoPai is not None else set()
        
    @property
    def cardinalidadeMinima(self) -> str:
        return self.__cardinalidadeMinima

    @cardinalidadeMinima.setter
    def cardinalidadeMinima(self, cardinalidadeMinima: str):
        self.__cardinalidadeMinima = cardinalidadeMinima

    @property
    def cardinalidadeMaxima(self) -> str:
        return self.__cardinalidadeMaxima

    @cardinalidadeMaxima.setter
    def cardinalidadeMaxima(self, cardinalidadeMaxima: str):
        self.__cardinalidadeMaxima = cardinalidadeMaxima

    @property
    def variacaoProdutoPai(self):
        return self.__variacaoProdutoPai

    @variacaoProdutoPai.setter
    def variacaoProdutoPai(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_VariacaoProduto__variacaoProdutoPai", None)
        self.__variacaoProdutoPai = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VarianteProduto"):
                    opp_val = getattr(item, "VarianteProduto", None)
                    
                    if opp_val == self:
                        setattr(item, "VarianteProduto", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VarianteProduto"):
                    opp_val = getattr(item, "VarianteProduto", None)
                    
                    setattr(item, "VarianteProduto", self)
                    

    @property
    def caracteristica_VariacaoProduto(self):
        return self.__caracteristica_VariacaoProduto

    @caracteristica_VariacaoProduto.setter
    def caracteristica_VariacaoProduto(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_VariacaoProduto__caracteristica_VariacaoProduto", None)
        self.__caracteristica_VariacaoProduto = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_CaracteristicaProduto"):
                opp_val = getattr(old_value, "caracteristica_CaracteristicaProduto", None)
                if opp_val == self:
                    setattr(old_value, "caracteristica_CaracteristicaProduto", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_CaracteristicaProduto"):
                opp_val = getattr(value, "caracteristica_CaracteristicaProduto", None)
                setattr(value, "caracteristica_CaracteristicaProduto", self)

    @property
    def VariacaoProduto(self):
        return self.__VariacaoProduto

    @VariacaoProduto.setter
    def VariacaoProduto(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_VariacaoProduto__VariacaoProduto", None)
        self.__VariacaoProduto = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "variantesProduto"):
                opp_val = getattr(old_value, "variantesProduto", None)
                if opp_val == self:
                    setattr(old_value, "variantesProduto", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "variantesProduto"):
                opp_val = getattr(value, "variantesProduto", None)
                setattr(value, "variantesProduto", self)

class CaracteristicaProduto:

    pass
class caracteristica_CaracteristicaOpcionalProduto(CaracteristicaProduto):

    pass
class caracteristica_VariacaoDoisProduto(CaracteristicaProduto):

    def __init__(self, cardinalidadeMaxima: str, cardinalidadeMinimaOr: str, cardinalidadeMaximaOr: str):
        self.cardinalidadeMaxima = cardinalidadeMaxima
        self.cardinalidadeMinimaOr = cardinalidadeMinimaOr
        self.cardinalidadeMaximaOr = cardinalidadeMaximaOr
        
    @property
    def cardinalidadeMinimaOr(self) -> str:
        return self.__cardinalidadeMinimaOr

    @cardinalidadeMinimaOr.setter
    def cardinalidadeMinimaOr(self, cardinalidadeMinimaOr: str):
        self.__cardinalidadeMinimaOr = cardinalidadeMinimaOr

    @property
    def cardinalidadeMaximaOr(self) -> str:
        return self.__cardinalidadeMaximaOr

    @cardinalidadeMaximaOr.setter
    def cardinalidadeMaximaOr(self, cardinalidadeMaximaOr: str):
        self.__cardinalidadeMaximaOr = cardinalidadeMaximaOr

    @property
    def cardinalidadeMaxima(self) -> str:
        return self.__cardinalidadeMaxima

    @cardinalidadeMaxima.setter
    def cardinalidadeMaxima(self, cardinalidadeMaxima: str):
        self.__cardinalidadeMaxima = cardinalidadeMaxima

class caracteristica_CaracteristicaAgrupadaProduto(CaracteristicaProduto):

    pass
class caracteristica_CaracteristicaMandatoriaProduto(CaracteristicaProduto):

    pass
class caracteristica_AtributoProduto(ElementoDeProduto):

    def __init__(self, valor: str, tipoValor: str, AtributoProduto: "caracteristica_CaracteristicaProduto" = None, atributoProduto: "caracteristica_CaracteristicaProduto" = None):
        self.valor = valor
        self.tipoValor = tipoValor
        self.AtributoProduto = AtributoProduto
        self.atributoProduto = atributoProduto
        
    @property
    def tipoValor(self) -> str:
        return self.__tipoValor

    @tipoValor.setter
    def tipoValor(self, tipoValor: str):
        self.__tipoValor = tipoValor

    @property
    def valor(self) -> str:
        return self.__valor

    @valor.setter
    def valor(self, valor: str):
        self.__valor = valor

    @property
    def atributoProduto(self):
        return self.__atributoProduto

    @atributoProduto.setter
    def atributoProduto(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_AtributoProduto__atributoProduto", None)
        self.__atributoProduto = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CaracteristicaProduto55"):
                opp_val = getattr(old_value, "CaracteristicaProduto55", None)
                if opp_val == self:
                    setattr(old_value, "CaracteristicaProduto55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CaracteristicaProduto55"):
                opp_val = getattr(value, "CaracteristicaProduto55", None)
                setattr(value, "CaracteristicaProduto55", self)

    @property
    def AtributoProduto(self):
        return self.__AtributoProduto

    @AtributoProduto.setter
    def AtributoProduto(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_AtributoProduto__AtributoProduto", None)
        self.__AtributoProduto = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristicaProdutoPai53"):
                opp_val = getattr(old_value, "caracteristicaProdutoPai53", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristicaProdutoPai53"):
                opp_val = getattr(value, "caracteristicaProdutoPai53", None)
                if opp_val is None:
                    setattr(value, "caracteristicaProdutoPai53", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PontoDeVariacao:

    pass
class ElementoCaracteristico:

    pass
class Caracteristica:

    pass
class caracteristica_CaracteristicaOpcional(Caracteristica, ElementoCaracteristico):

    pass
class caracteristica_VariacaoDois(Caracteristica, ElementoCaracteristico):

    def __init__(self, cardinalidadeMaxima: str, cardinalidadeMinimaOr: str, cardinalidadeMaximaOr: str):
        self.cardinalidadeMaxima = cardinalidadeMaxima
        self.cardinalidadeMinimaOr = cardinalidadeMinimaOr
        self.cardinalidadeMaximaOr = cardinalidadeMaximaOr
        
    @property
    def cardinalidadeMinimaOr(self) -> str:
        return self.__cardinalidadeMinimaOr

    @cardinalidadeMinimaOr.setter
    def cardinalidadeMinimaOr(self, cardinalidadeMinimaOr: str):
        self.__cardinalidadeMinimaOr = cardinalidadeMinimaOr

    @property
    def cardinalidadeMaximaOr(self) -> str:
        return self.__cardinalidadeMaximaOr

    @cardinalidadeMaximaOr.setter
    def cardinalidadeMaximaOr(self, cardinalidadeMaximaOr: str):
        self.__cardinalidadeMaximaOr = cardinalidadeMaximaOr

    @property
    def cardinalidadeMaxima(self) -> str:
        return self.__cardinalidadeMaxima

    @cardinalidadeMaxima.setter
    def cardinalidadeMaxima(self, cardinalidadeMaxima: str):
        self.__cardinalidadeMaxima = cardinalidadeMaxima

class caracteristica_Variante(PontoDeVariacao, Caracteristica, ElementoCaracteristico):

    pass
class caracteristica_CaracteristicaMandatoria(Caracteristica):

    pass
class caracteristica_CaracteristicaAgrupada(Caracteristica, ElementoCaracteristico):

    pass
class caracteristica_Regra:

    def __init__(self, nome: str, conteudo: str, caracteristica_Regra: "caracteristica_LPS" = None):
        self.nome = nome
        self.conteudo = conteudo
        self.caracteristica_Regra = caracteristica_Regra
        
    @property
    def conteudo(self) -> str:
        return self.__conteudo

    @conteudo.setter
    def conteudo(self, conteudo: str):
        self.__conteudo = conteudo

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def caracteristica_Regra(self):
        return self.__caracteristica_Regra

    @caracteristica_Regra.setter
    def caracteristica_Regra(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Regra__caracteristica_Regra", None)
        self.__caracteristica_Regra = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_LPS6"):
                opp_val = getattr(old_value, "caracteristica_LPS6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_LPS6"):
                opp_val = getattr(value, "caracteristica_LPS6", None)
                if opp_val is None:
                    setattr(value, "caracteristica_LPS6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class caracteristica_ElementoExterno:

    def __init__(self, nome: str, caracteristica_ElementoExterno: "caracteristica_LPS" = None, caracteristica_ElementoExterno22: "caracteristica_Caracteristica" = None):
        self.nome = nome
        self.caracteristica_ElementoExterno = caracteristica_ElementoExterno
        self.caracteristica_ElementoExterno22 = caracteristica_ElementoExterno22
        
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def caracteristica_ElementoExterno(self):
        return self.__caracteristica_ElementoExterno

    @caracteristica_ElementoExterno.setter
    def caracteristica_ElementoExterno(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_ElementoExterno__caracteristica_ElementoExterno", None)
        self.__caracteristica_ElementoExterno = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_LPS4"):
                opp_val = getattr(old_value, "caracteristica_LPS4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_LPS4"):
                opp_val = getattr(value, "caracteristica_LPS4", None)
                if opp_val is None:
                    setattr(value, "caracteristica_LPS4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def caracteristica_ElementoExterno22(self):
        return self.__caracteristica_ElementoExterno22

    @caracteristica_ElementoExterno22.setter
    def caracteristica_ElementoExterno22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_ElementoExterno__caracteristica_ElementoExterno22", None)
        self.__caracteristica_ElementoExterno22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_Caracteristica"):
                opp_val = getattr(old_value, "caracteristica_Caracteristica", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_Caracteristica"):
                opp_val = getattr(value, "caracteristica_Caracteristica", None)
                if opp_val is None:
                    setattr(value, "caracteristica_Caracteristica", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class caracteristica_Elemento:

    def __init__(self, nome: str, caracteristica_Elemento: "caracteristica_LPS" = None, caracteristica_Elemento46: "caracteristica_ElementoDeProduto" = None):
        self.nome = nome
        self.caracteristica_Elemento = caracteristica_Elemento
        self.caracteristica_Elemento46 = caracteristica_Elemento46
        
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def caracteristica_Elemento46(self):
        return self.__caracteristica_Elemento46

    @caracteristica_Elemento46.setter
    def caracteristica_Elemento46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Elemento__caracteristica_Elemento46", None)
        self.__caracteristica_Elemento46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_ElementoDeProduto45"):
                opp_val = getattr(old_value, "caracteristica_ElementoDeProduto45", None)
                if opp_val == self:
                    setattr(old_value, "caracteristica_ElementoDeProduto45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_ElementoDeProduto45"):
                opp_val = getattr(value, "caracteristica_ElementoDeProduto45", None)
                setattr(value, "caracteristica_ElementoDeProduto45", self)

    @property
    def caracteristica_Elemento(self):
        return self.__caracteristica_Elemento

    @caracteristica_Elemento.setter
    def caracteristica_Elemento(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Elemento__caracteristica_Elemento", None)
        self.__caracteristica_Elemento = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_LPS2"):
                opp_val = getattr(old_value, "caracteristica_LPS2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_LPS2"):
                opp_val = getattr(value, "caracteristica_LPS2", None)
                if opp_val is None:
                    setattr(value, "caracteristica_LPS2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class caracteristica_PontoDeVariacao:

    pass
class caracteristica_LPS:

    def __init__(self, valoresContextuais: str, erro: str, nome: str, caracteristica_LPS8: set["caracteristica_Produto"] = None, caracteristica_LPS10: set["caracteristica_Expressao"] = None, caracteristica_LPS12: set["caracteristica_ElementoDeProduto"] = None, LpsDoSistema: "caracteristica_CaracteristicaRaiz" = None, caracteristica_LPS15: set["caracteristica_Atributo"] = None, caracteristica_LPS17: set["caracteristica_Simulacao"] = None, caracteristica_LPS19: set["caracteristica_InconsistenciaRegraAdaptacao"] = None, caracteristica_LPS: set["caracteristica_PontoDeVariacao"] = None, caracteristica_LPS2: set["caracteristica_Elemento"] = None, caracteristica_LPS4: set["caracteristica_ElementoExterno"] = None, caracteristica_LPS6: set["caracteristica_Regra"] = None, LPS: "caracteristica_CaracteristicaRaiz" = None):
        self.valoresContextuais = valoresContextuais
        self.erro = erro
        self.nome = nome
        self.caracteristica_LPS8 = caracteristica_LPS8 if caracteristica_LPS8 is not None else set()
        self.caracteristica_LPS10 = caracteristica_LPS10 if caracteristica_LPS10 is not None else set()
        self.caracteristica_LPS12 = caracteristica_LPS12 if caracteristica_LPS12 is not None else set()
        self.LpsDoSistema = LpsDoSistema
        self.caracteristica_LPS15 = caracteristica_LPS15 if caracteristica_LPS15 is not None else set()
        self.caracteristica_LPS17 = caracteristica_LPS17 if caracteristica_LPS17 is not None else set()
        self.caracteristica_LPS19 = caracteristica_LPS19 if caracteristica_LPS19 is not None else set()
        self.caracteristica_LPS = caracteristica_LPS if caracteristica_LPS is not None else set()
        self.caracteristica_LPS2 = caracteristica_LPS2 if caracteristica_LPS2 is not None else set()
        self.caracteristica_LPS4 = caracteristica_LPS4 if caracteristica_LPS4 is not None else set()
        self.caracteristica_LPS6 = caracteristica_LPS6 if caracteristica_LPS6 is not None else set()
        self.LPS = LPS
        
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def erro(self) -> str:
        return self.__erro

    @erro.setter
    def erro(self, erro: str):
        self.__erro = erro

    @property
    def valoresContextuais(self) -> str:
        return self.__valoresContextuais

    @valoresContextuais.setter
    def valoresContextuais(self, valoresContextuais: str):
        self.__valoresContextuais = valoresContextuais

    @property
    def caracteristica_LPS8(self):
        return self.__caracteristica_LPS8

    @caracteristica_LPS8.setter
    def caracteristica_LPS8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_LPS__caracteristica_LPS8", None)
        self.__caracteristica_LPS8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "caracteristica_Produto"):
                    opp_val = getattr(item, "caracteristica_Produto", None)
                    
                    if opp_val == self:
                        setattr(item, "caracteristica_Produto", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "caracteristica_Produto"):
                    opp_val = getattr(item, "caracteristica_Produto", None)
                    
                    setattr(item, "caracteristica_Produto", self)
                    

    @property
    def caracteristica_LPS17(self):
        return self.__caracteristica_LPS17

    @caracteristica_LPS17.setter
    def caracteristica_LPS17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_LPS__caracteristica_LPS17", None)
        self.__caracteristica_LPS17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "caracteristica_Simulacao"):
                    opp_val = getattr(item, "caracteristica_Simulacao", None)
                    
                    if opp_val == self:
                        setattr(item, "caracteristica_Simulacao", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "caracteristica_Simulacao"):
                    opp_val = getattr(item, "caracteristica_Simulacao", None)
                    
                    setattr(item, "caracteristica_Simulacao", self)
                    

    @property
    def caracteristica_LPS12(self):
        return self.__caracteristica_LPS12

    @caracteristica_LPS12.setter
    def caracteristica_LPS12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_LPS__caracteristica_LPS12", None)
        self.__caracteristica_LPS12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "caracteristica_ElementoDeProduto"):
                    opp_val = getattr(item, "caracteristica_ElementoDeProduto", None)
                    
                    if opp_val == self:
                        setattr(item, "caracteristica_ElementoDeProduto", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "caracteristica_ElementoDeProduto"):
                    opp_val = getattr(item, "caracteristica_ElementoDeProduto", None)
                    
                    setattr(item, "caracteristica_ElementoDeProduto", self)
                    

    @property
    def caracteristica_LPS15(self):
        return self.__caracteristica_LPS15

    @caracteristica_LPS15.setter
    def caracteristica_LPS15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_LPS__caracteristica_LPS15", None)
        self.__caracteristica_LPS15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "caracteristica_Atributo"):
                    opp_val = getattr(item, "caracteristica_Atributo", None)
                    
                    if opp_val == self:
                        setattr(item, "caracteristica_Atributo", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "caracteristica_Atributo"):
                    opp_val = getattr(item, "caracteristica_Atributo", None)
                    
                    setattr(item, "caracteristica_Atributo", self)
                    

    @property
    def caracteristica_LPS4(self):
        return self.__caracteristica_LPS4

    @caracteristica_LPS4.setter
    def caracteristica_LPS4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_LPS__caracteristica_LPS4", None)
        self.__caracteristica_LPS4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "caracteristica_ElementoExterno"):
                    opp_val = getattr(item, "caracteristica_ElementoExterno", None)
                    
                    if opp_val == self:
                        setattr(item, "caracteristica_ElementoExterno", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "caracteristica_ElementoExterno"):
                    opp_val = getattr(item, "caracteristica_ElementoExterno", None)
                    
                    setattr(item, "caracteristica_ElementoExterno", self)
                    

    @property
    def LPS(self):
        return self.__LPS

    @LPS.setter
    def LPS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_LPS__LPS", None)
        self.__LPS = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sistema"):
                opp_val = getattr(old_value, "sistema", None)
                if opp_val == self:
                    setattr(old_value, "sistema", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sistema"):
                opp_val = getattr(value, "sistema", None)
                setattr(value, "sistema", self)

    @property
    def caracteristica_LPS19(self):
        return self.__caracteristica_LPS19

    @caracteristica_LPS19.setter
    def caracteristica_LPS19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_LPS__caracteristica_LPS19", None)
        self.__caracteristica_LPS19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "caracteristica_InconsistenciaRegraAdaptacao"):
                    opp_val = getattr(item, "caracteristica_InconsistenciaRegraAdaptacao", None)
                    
                    if opp_val == self:
                        setattr(item, "caracteristica_InconsistenciaRegraAdaptacao", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "caracteristica_InconsistenciaRegraAdaptacao"):
                    opp_val = getattr(item, "caracteristica_InconsistenciaRegraAdaptacao", None)
                    
                    setattr(item, "caracteristica_InconsistenciaRegraAdaptacao", self)
                    

    @property
    def caracteristica_LPS2(self):
        return self.__caracteristica_LPS2

    @caracteristica_LPS2.setter
    def caracteristica_LPS2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_LPS__caracteristica_LPS2", None)
        self.__caracteristica_LPS2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "caracteristica_Elemento"):
                    opp_val = getattr(item, "caracteristica_Elemento", None)
                    
                    if opp_val == self:
                        setattr(item, "caracteristica_Elemento", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "caracteristica_Elemento"):
                    opp_val = getattr(item, "caracteristica_Elemento", None)
                    
                    setattr(item, "caracteristica_Elemento", self)
                    

    @property
    def caracteristica_LPS10(self):
        return self.__caracteristica_LPS10

    @caracteristica_LPS10.setter
    def caracteristica_LPS10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_LPS__caracteristica_LPS10", None)
        self.__caracteristica_LPS10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "caracteristica_Expressao"):
                    opp_val = getattr(item, "caracteristica_Expressao", None)
                    
                    if opp_val == self:
                        setattr(item, "caracteristica_Expressao", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "caracteristica_Expressao"):
                    opp_val = getattr(item, "caracteristica_Expressao", None)
                    
                    setattr(item, "caracteristica_Expressao", self)
                    

    @property
    def LpsDoSistema(self):
        return self.__LpsDoSistema

    @LpsDoSistema.setter
    def LpsDoSistema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_LPS__LpsDoSistema", None)
        self.__LpsDoSistema = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CaracteristicaRaiz"):
                opp_val = getattr(old_value, "CaracteristicaRaiz", None)
                if opp_val == self:
                    setattr(old_value, "CaracteristicaRaiz", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CaracteristicaRaiz"):
                opp_val = getattr(value, "CaracteristicaRaiz", None)
                setattr(value, "CaracteristicaRaiz", self)

    @property
    def caracteristica_LPS6(self):
        return self.__caracteristica_LPS6

    @caracteristica_LPS6.setter
    def caracteristica_LPS6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_LPS__caracteristica_LPS6", None)
        self.__caracteristica_LPS6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "caracteristica_Regra"):
                    opp_val = getattr(item, "caracteristica_Regra", None)
                    
                    if opp_val == self:
                        setattr(item, "caracteristica_Regra", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "caracteristica_Regra"):
                    opp_val = getattr(item, "caracteristica_Regra", None)
                    
                    setattr(item, "caracteristica_Regra", self)
                    

    @property
    def caracteristica_LPS(self):
        return self.__caracteristica_LPS

    @caracteristica_LPS.setter
    def caracteristica_LPS(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_LPS__caracteristica_LPS", None)
        self.__caracteristica_LPS = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "caracteristica_PontoDeVariacao"):
                    opp_val = getattr(item, "caracteristica_PontoDeVariacao", None)
                    
                    if opp_val == self:
                        setattr(item, "caracteristica_PontoDeVariacao", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "caracteristica_PontoDeVariacao"):
                    opp_val = getattr(item, "caracteristica_PontoDeVariacao", None)
                    
                    setattr(item, "caracteristica_PontoDeVariacao", self)
                    

class Elemento:

    pass
class caracteristica_Variacao(PontoDeVariacao, Elemento):

    def __init__(self, cardinalidadeMinima: str, cardinalidadeMaxima: str, Variacao: "caracteristica_Caracteristica" = None, variacaoPai: set["caracteristica_Variante"] = None, variacoes: "caracteristica_Caracteristica" = None, Variacao38: "caracteristica_Variante" = None):
        self.cardinalidadeMinima = cardinalidadeMinima
        self.cardinalidadeMaxima = cardinalidadeMaxima
        self.Variacao = Variacao
        self.variacaoPai = variacaoPai if variacaoPai is not None else set()
        self.variacoes = variacoes
        self.Variacao38 = Variacao38
        
    @property
    def cardinalidadeMaxima(self) -> str:
        return self.__cardinalidadeMaxima

    @cardinalidadeMaxima.setter
    def cardinalidadeMaxima(self, cardinalidadeMaxima: str):
        self.__cardinalidadeMaxima = cardinalidadeMaxima

    @property
    def cardinalidadeMinima(self) -> str:
        return self.__cardinalidadeMinima

    @cardinalidadeMinima.setter
    def cardinalidadeMinima(self, cardinalidadeMinima: str):
        self.__cardinalidadeMinima = cardinalidadeMinima

    @property
    def variacaoPai(self):
        return self.__variacaoPai

    @variacaoPai.setter
    def variacaoPai(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Variacao__variacaoPai", None)
        self.__variacaoPai = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Variante"):
                    opp_val = getattr(item, "Variante", None)
                    
                    if opp_val == self:
                        setattr(item, "Variante", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Variante"):
                    opp_val = getattr(item, "Variante", None)
                    
                    setattr(item, "Variante", self)
                    

    @property
    def Variacao(self):
        return self.__Variacao

    @Variacao.setter
    def Variacao(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Variacao__Variacao", None)
        self.__Variacao = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristicaPai30"):
                opp_val = getattr(old_value, "caracteristicaPai30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristicaPai30"):
                opp_val = getattr(value, "caracteristicaPai30", None)
                if opp_val is None:
                    setattr(value, "caracteristicaPai30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def variacoes(self):
        return self.__variacoes

    @variacoes.setter
    def variacoes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Variacao__variacoes", None)
        self.__variacoes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Caracteristica36"):
                opp_val = getattr(old_value, "Caracteristica36", None)
                if opp_val == self:
                    setattr(old_value, "Caracteristica36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Caracteristica36"):
                opp_val = getattr(value, "Caracteristica36", None)
                setattr(value, "Caracteristica36", self)

    @property
    def Variacao38(self):
        return self.__Variacao38

    @Variacao38.setter
    def Variacao38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Variacao__Variacao38", None)
        self.__Variacao38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "variantes"):
                opp_val = getattr(old_value, "variantes", None)
                if opp_val == self:
                    setattr(old_value, "variantes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "variantes"):
                opp_val = getattr(value, "variantes", None)
                setattr(value, "variantes", self)

class caracteristica_Caracteristica(Elemento):

    pass
class caracteristica_InformacaoDeContexto(Elemento):

    def __init__(self, origem: str, validade: str, qualidade: str, tipoValor: str, valor: str, InformacaoDeContexto: "caracteristica_EntidadeDeContexto" = None, informacoesDeContexto: "caracteristica_EntidadeDeContexto" = None, caracteristica_InformacaoDeContexto: "caracteristica_EventoRelacional" = None):
        self.origem = origem
        self.validade = validade
        self.qualidade = qualidade
        self.tipoValor = tipoValor
        self.valor = valor
        self.InformacaoDeContexto = InformacaoDeContexto
        self.informacoesDeContexto = informacoesDeContexto
        self.caracteristica_InformacaoDeContexto = caracteristica_InformacaoDeContexto
        
    @property
    def validade(self) -> str:
        return self.__validade

    @validade.setter
    def validade(self, validade: str):
        self.__validade = validade

    @property
    def origem(self) -> str:
        return self.__origem

    @origem.setter
    def origem(self, origem: str):
        self.__origem = origem

    @property
    def valor(self) -> str:
        return self.__valor

    @valor.setter
    def valor(self, valor: str):
        self.__valor = valor

    @property
    def tipoValor(self) -> str:
        return self.__tipoValor

    @tipoValor.setter
    def tipoValor(self, tipoValor: str):
        self.__tipoValor = tipoValor

    @property
    def qualidade(self) -> str:
        return self.__qualidade

    @qualidade.setter
    def qualidade(self, qualidade: str):
        self.__qualidade = qualidade

    @property
    def informacoesDeContexto(self):
        return self.__informacoesDeContexto

    @informacoesDeContexto.setter
    def informacoesDeContexto(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_InformacaoDeContexto__informacoesDeContexto", None)
        self.__informacoesDeContexto = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EntidadeDeContexto43"):
                opp_val = getattr(old_value, "EntidadeDeContexto43", None)
                if opp_val == self:
                    setattr(old_value, "EntidadeDeContexto43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EntidadeDeContexto43"):
                opp_val = getattr(value, "EntidadeDeContexto43", None)
                setattr(value, "EntidadeDeContexto43", self)

    @property
    def caracteristica_InformacaoDeContexto(self):
        return self.__caracteristica_InformacaoDeContexto

    @caracteristica_InformacaoDeContexto.setter
    def caracteristica_InformacaoDeContexto(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_InformacaoDeContexto__caracteristica_InformacaoDeContexto", None)
        self.__caracteristica_InformacaoDeContexto = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_EventoRelacional"):
                opp_val = getattr(old_value, "caracteristica_EventoRelacional", None)
                if opp_val == self:
                    setattr(old_value, "caracteristica_EventoRelacional", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_EventoRelacional"):
                opp_val = getattr(value, "caracteristica_EventoRelacional", None)
                setattr(value, "caracteristica_EventoRelacional", self)

    @property
    def InformacaoDeContexto(self):
        return self.__InformacaoDeContexto

    @InformacaoDeContexto.setter
    def InformacaoDeContexto(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_InformacaoDeContexto__InformacaoDeContexto", None)
        self.__InformacaoDeContexto = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "elementoPai"):
                opp_val = getattr(old_value, "elementoPai", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "elementoPai"):
                opp_val = getattr(value, "elementoPai", None)
                if opp_val is None:
                    setattr(value, "elementoPai", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class caracteristica_EntidadeDeContexto(Elemento):

    pass
class caracteristica_RaizDeContexto(Elemento):

    pass
class caracteristica_ElementoCaracteristico(Elemento):

    pass
class ElementoExterno:

    pass
class caracteristica_CasoDeTeste(ElementoExterno):

    pass
class caracteristica_CasoDeUso(ElementoExterno):

    pass
class caracteristica_InconsistenciaRegraAdaptacao:

    pass
class caracteristica_Simulacao:

    def __init__(self, nome: str, caracteristica_Simulacao: "caracteristica_LPS" = None, caracteristica_Simulacao92: set["caracteristica_Transicao"] = None, caracteristica_Simulacao94: set["caracteristica_Estado"] = None):
        self.nome = nome
        self.caracteristica_Simulacao = caracteristica_Simulacao
        self.caracteristica_Simulacao92 = caracteristica_Simulacao92 if caracteristica_Simulacao92 is not None else set()
        self.caracteristica_Simulacao94 = caracteristica_Simulacao94 if caracteristica_Simulacao94 is not None else set()
        
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def caracteristica_Simulacao94(self):
        return self.__caracteristica_Simulacao94

    @caracteristica_Simulacao94.setter
    def caracteristica_Simulacao94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Simulacao__caracteristica_Simulacao94", None)
        self.__caracteristica_Simulacao94 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "caracteristica_Estado"):
                    opp_val = getattr(item, "caracteristica_Estado", None)
                    
                    if opp_val == self:
                        setattr(item, "caracteristica_Estado", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "caracteristica_Estado"):
                    opp_val = getattr(item, "caracteristica_Estado", None)
                    
                    setattr(item, "caracteristica_Estado", self)
                    

    @property
    def caracteristica_Simulacao(self):
        return self.__caracteristica_Simulacao

    @caracteristica_Simulacao.setter
    def caracteristica_Simulacao(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Simulacao__caracteristica_Simulacao", None)
        self.__caracteristica_Simulacao = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_LPS17"):
                opp_val = getattr(old_value, "caracteristica_LPS17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_LPS17"):
                opp_val = getattr(value, "caracteristica_LPS17", None)
                if opp_val is None:
                    setattr(value, "caracteristica_LPS17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def caracteristica_Simulacao92(self):
        return self.__caracteristica_Simulacao92

    @caracteristica_Simulacao92.setter
    def caracteristica_Simulacao92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Simulacao__caracteristica_Simulacao92", None)
        self.__caracteristica_Simulacao92 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "caracteristica_Transicao"):
                    opp_val = getattr(item, "caracteristica_Transicao", None)
                    
                    if opp_val == self:
                        setattr(item, "caracteristica_Transicao", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "caracteristica_Transicao"):
                    opp_val = getattr(item, "caracteristica_Transicao", None)
                    
                    setattr(item, "caracteristica_Transicao", self)
                    

class caracteristica_Atributo(Elemento):

    def __init__(self, tipoValor: str, caracteristica_Atributo: "caracteristica_LPS" = None, Atributo: "caracteristica_Caracteristica" = None, atributo: "caracteristica_Caracteristica" = None, caracteristica_Atributo81: "caracteristica_Designar" = None, caracteristica_Atributo88: "caracteristica_ExpressaoRelacional" = None):
        self.tipoValor = tipoValor
        self.caracteristica_Atributo = caracteristica_Atributo
        self.Atributo = Atributo
        self.atributo = atributo
        self.caracteristica_Atributo81 = caracteristica_Atributo81
        self.caracteristica_Atributo88 = caracteristica_Atributo88
        
    @property
    def tipoValor(self) -> str:
        return self.__tipoValor

    @tipoValor.setter
    def tipoValor(self, tipoValor: str):
        self.__tipoValor = tipoValor

    @property
    def caracteristica_Atributo81(self):
        return self.__caracteristica_Atributo81

    @caracteristica_Atributo81.setter
    def caracteristica_Atributo81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Atributo__caracteristica_Atributo81", None)
        self.__caracteristica_Atributo81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_Designar"):
                opp_val = getattr(old_value, "caracteristica_Designar", None)
                if opp_val == self:
                    setattr(old_value, "caracteristica_Designar", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_Designar"):
                opp_val = getattr(value, "caracteristica_Designar", None)
                setattr(value, "caracteristica_Designar", self)

    @property
    def caracteristica_Atributo88(self):
        return self.__caracteristica_Atributo88

    @caracteristica_Atributo88.setter
    def caracteristica_Atributo88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Atributo__caracteristica_Atributo88", None)
        self.__caracteristica_Atributo88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_ExpressaoRelacional"):
                opp_val = getattr(old_value, "caracteristica_ExpressaoRelacional", None)
                if opp_val == self:
                    setattr(old_value, "caracteristica_ExpressaoRelacional", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_ExpressaoRelacional"):
                opp_val = getattr(value, "caracteristica_ExpressaoRelacional", None)
                setattr(value, "caracteristica_ExpressaoRelacional", self)

    @property
    def Atributo(self):
        return self.__Atributo

    @Atributo.setter
    def Atributo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Atributo__Atributo", None)
        self.__Atributo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristicaPai32"):
                opp_val = getattr(old_value, "caracteristicaPai32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristicaPai32"):
                opp_val = getattr(value, "caracteristicaPai32", None)
                if opp_val is None:
                    setattr(value, "caracteristicaPai32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def caracteristica_Atributo(self):
        return self.__caracteristica_Atributo

    @caracteristica_Atributo.setter
    def caracteristica_Atributo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Atributo__caracteristica_Atributo", None)
        self.__caracteristica_Atributo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_LPS15"):
                opp_val = getattr(old_value, "caracteristica_LPS15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_LPS15"):
                opp_val = getattr(value, "caracteristica_LPS15", None)
                if opp_val is None:
                    setattr(value, "caracteristica_LPS15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def atributo(self):
        return self.__atributo

    @atributo.setter
    def atributo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Atributo__atributo", None)
        self.__atributo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Caracteristica"):
                opp_val = getattr(old_value, "Caracteristica", None)
                if opp_val == self:
                    setattr(old_value, "Caracteristica", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Caracteristica"):
                opp_val = getattr(value, "Caracteristica", None)
                setattr(value, "Caracteristica", self)

class caracteristica_CaracteristicaRaiz(Caracteristica):

    pass
class caracteristica_ElementoDeProduto:

    def __init__(self, nome: str, caracteristica_ElementoDeProduto: "caracteristica_LPS" = None, caracteristica_ElementoDeProduto45: "caracteristica_Elemento" = None):
        self.nome = nome
        self.caracteristica_ElementoDeProduto = caracteristica_ElementoDeProduto
        self.caracteristica_ElementoDeProduto45 = caracteristica_ElementoDeProduto45
        
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def caracteristica_ElementoDeProduto(self):
        return self.__caracteristica_ElementoDeProduto

    @caracteristica_ElementoDeProduto.setter
    def caracteristica_ElementoDeProduto(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_ElementoDeProduto__caracteristica_ElementoDeProduto", None)
        self.__caracteristica_ElementoDeProduto = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_LPS12"):
                opp_val = getattr(old_value, "caracteristica_LPS12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_LPS12"):
                opp_val = getattr(value, "caracteristica_LPS12", None)
                if opp_val is None:
                    setattr(value, "caracteristica_LPS12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def caracteristica_ElementoDeProduto45(self):
        return self.__caracteristica_ElementoDeProduto45

    @caracteristica_ElementoDeProduto45.setter
    def caracteristica_ElementoDeProduto45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_ElementoDeProduto__caracteristica_ElementoDeProduto45", None)
        self.__caracteristica_ElementoDeProduto45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_Elemento46"):
                opp_val = getattr(old_value, "caracteristica_Elemento46", None)
                if opp_val == self:
                    setattr(old_value, "caracteristica_Elemento46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_Elemento46"):
                opp_val = getattr(value, "caracteristica_Elemento46", None)
                setattr(value, "caracteristica_Elemento46", self)

class caracteristica_Expressao:

    def __init__(self, nome: str, caracteristica_Expressao: "caracteristica_LPS" = None):
        self.nome = nome
        self.caracteristica_Expressao = caracteristica_Expressao
        
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def caracteristica_Expressao(self):
        return self.__caracteristica_Expressao

    @caracteristica_Expressao.setter
    def caracteristica_Expressao(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Expressao__caracteristica_Expressao", None)
        self.__caracteristica_Expressao = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_LPS10"):
                opp_val = getattr(old_value, "caracteristica_LPS10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_LPS10"):
                opp_val = getattr(value, "caracteristica_LPS10", None)
                if opp_val is None:
                    setattr(value, "caracteristica_LPS10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class caracteristica_Produto(CaracteristicaProduto):

    pass