from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class TipoValor(Enum):
    TInteger = "TInteger"
    TString = "TString"
    TFloat = "TFloat"
    TBoolean = "TBoolean"
class OperadorLogico(Enum):
    AND = "AND"
    OR = "OR"
class Presenca(Enum):
    PRESENTE = "PRESENTE"
    AUSENTE = "AUSENTE"
class Origem(Enum):
    Sentida = "Sentida"
    Usuario = "Usuario"
    Perfil = "Perfil"
    Derivada = "Derivada"
class CardinalidadeMaxima(Enum):
    OR = "OR"
    XOR = "XOR"
class Qualidade(Enum):
    Baixo = "Baixo"
    Alto = "Alto"
class Validade(Enum):
    Volatil = "Volatil"
    Frequente = "Frequente"
    Raramente = "Raramente"
    Permanente = "Permanente"
class OperadorRelacional(Enum):
    MAIOR = "MAIOR"
    MENOR = "MENOR"
    IGUAL = "IGUAL"
    MAIORIGUAL = "MAIORIGUAL"
    MENORIGUAL = "MENORIGUAL"
    DIFERENTE = "DIFERENTE"
class OperadorAcaoLogico(Enum):
    AND = "AND"


############################################
# Definition of Classes
############################################

class caracteristica_Estado:

    def __init__(self, nome: str, safe: bool, caracteristica_Estado: "caracteristica_Simulacao" = None, caracteristica_Estado93: "caracteristica_Transicao" = None, caracteristica_Estado96: "caracteristica_Transicao" = None, caracteristica_Estado104: "caracteristica_CaracteristicaProduto" = None):
        self.nome = nome
        self.safe = safe
        self.caracteristica_Estado = caracteristica_Estado
        self.caracteristica_Estado93 = caracteristica_Estado93
        self.caracteristica_Estado96 = caracteristica_Estado96
        self.caracteristica_Estado104 = caracteristica_Estado104
        
    @property
    def safe(self) -> bool:
        return self.__safe

    @safe.setter
    def safe(self, safe: bool):
        self.__safe = safe

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def caracteristica_Estado96(self):
        return self.__caracteristica_Estado96

    @caracteristica_Estado96.setter
    def caracteristica_Estado96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Estado__caracteristica_Estado96", None)
        self.__caracteristica_Estado96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_Transicao95"):
                opp_val = getattr(old_value, "caracteristica_Transicao95", None)
                if opp_val == self:
                    setattr(old_value, "caracteristica_Transicao95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_Transicao95"):
                opp_val = getattr(value, "caracteristica_Transicao95", None)
                setattr(value, "caracteristica_Transicao95", self)

    @property
    def caracteristica_Estado93(self):
        return self.__caracteristica_Estado93

    @caracteristica_Estado93.setter
    def caracteristica_Estado93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Estado__caracteristica_Estado93", None)
        self.__caracteristica_Estado93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_Transicao92"):
                opp_val = getattr(old_value, "caracteristica_Transicao92", None)
                if opp_val == self:
                    setattr(old_value, "caracteristica_Transicao92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_Transicao92"):
                opp_val = getattr(value, "caracteristica_Transicao92", None)
                setattr(value, "caracteristica_Transicao92", self)

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
            if hasattr(old_value, "caracteristica_Simulacao90"):
                opp_val = getattr(old_value, "caracteristica_Simulacao90", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_Simulacao90"):
                opp_val = getattr(value, "caracteristica_Simulacao90", None)
                if opp_val is None:
                    setattr(value, "caracteristica_Simulacao90", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def caracteristica_Estado104(self):
        return self.__caracteristica_Estado104

    @caracteristica_Estado104.setter
    def caracteristica_Estado104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Estado__caracteristica_Estado104", None)
        self.__caracteristica_Estado104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_CaracteristicaProduto105"):
                opp_val = getattr(old_value, "caracteristica_CaracteristicaProduto105", None)
                if opp_val == self:
                    setattr(old_value, "caracteristica_CaracteristicaProduto105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_CaracteristicaProduto105"):
                opp_val = getattr(value, "caracteristica_CaracteristicaProduto105", None)
                setattr(value, "caracteristica_CaracteristicaProduto105", self)

class caracteristica_Transicao:

    def __init__(self, safe: bool, etiqueta: str, caracteristica_Transicao: "caracteristica_Simulacao" = None, caracteristica_Transicao92: "caracteristica_Estado" = None, caracteristica_Transicao95: "caracteristica_Estado" = None, caracteristica_Transicao98: set["caracteristica_RegraDeComposicao"] = None, caracteristica_Transicao101: set["caracteristica_Acao"] = None):
        self.safe = safe
        self.etiqueta = etiqueta
        self.caracteristica_Transicao = caracteristica_Transicao
        self.caracteristica_Transicao92 = caracteristica_Transicao92
        self.caracteristica_Transicao95 = caracteristica_Transicao95
        self.caracteristica_Transicao98 = caracteristica_Transicao98 if caracteristica_Transicao98 is not None else set()
        self.caracteristica_Transicao101 = caracteristica_Transicao101 if caracteristica_Transicao101 is not None else set()
        
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
    def caracteristica_Transicao92(self):
        return self.__caracteristica_Transicao92

    @caracteristica_Transicao92.setter
    def caracteristica_Transicao92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Transicao__caracteristica_Transicao92", None)
        self.__caracteristica_Transicao92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_Estado93"):
                opp_val = getattr(old_value, "caracteristica_Estado93", None)
                if opp_val == self:
                    setattr(old_value, "caracteristica_Estado93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_Estado93"):
                opp_val = getattr(value, "caracteristica_Estado93", None)
                setattr(value, "caracteristica_Estado93", self)

    @property
    def caracteristica_Transicao95(self):
        return self.__caracteristica_Transicao95

    @caracteristica_Transicao95.setter
    def caracteristica_Transicao95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Transicao__caracteristica_Transicao95", None)
        self.__caracteristica_Transicao95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_Estado96"):
                opp_val = getattr(old_value, "caracteristica_Estado96", None)
                if opp_val == self:
                    setattr(old_value, "caracteristica_Estado96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_Estado96"):
                opp_val = getattr(value, "caracteristica_Estado96", None)
                setattr(value, "caracteristica_Estado96", self)

    @property
    def caracteristica_Transicao98(self):
        return self.__caracteristica_Transicao98

    @caracteristica_Transicao98.setter
    def caracteristica_Transicao98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Transicao__caracteristica_Transicao98", None)
        self.__caracteristica_Transicao98 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "caracteristica_RegraDeComposicao99"):
                    opp_val = getattr(item, "caracteristica_RegraDeComposicao99", None)
                    
                    if opp_val == self:
                        setattr(item, "caracteristica_RegraDeComposicao99", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "caracteristica_RegraDeComposicao99"):
                    opp_val = getattr(item, "caracteristica_RegraDeComposicao99", None)
                    
                    setattr(item, "caracteristica_RegraDeComposicao99", self)
                    

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
            if hasattr(old_value, "caracteristica_Simulacao88"):
                opp_val = getattr(old_value, "caracteristica_Simulacao88", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_Simulacao88"):
                opp_val = getattr(value, "caracteristica_Simulacao88", None)
                if opp_val is None:
                    setattr(value, "caracteristica_Simulacao88", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def caracteristica_Transicao101(self):
        return self.__caracteristica_Transicao101

    @caracteristica_Transicao101.setter
    def caracteristica_Transicao101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Transicao__caracteristica_Transicao101", None)
        self.__caracteristica_Transicao101 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "caracteristica_Acao102"):
                    opp_val = getattr(item, "caracteristica_Acao102", None)
                    
                    if opp_val == self:
                        setattr(item, "caracteristica_Acao102", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "caracteristica_Acao102"):
                    opp_val = getattr(item, "caracteristica_Acao102", None)
                    
                    setattr(item, "caracteristica_Acao102", self)
                    

class Antecedente:

    pass
class caracteristica_ExpressaoRelacional(Antecedente):

    def __init__(self, operadorRelacional: str, valor: str, caracteristica_ExpressaoRelacional: "caracteristica_Atributo" = None):
        self.operadorRelacional = operadorRelacional
        self.valor = valor
        self.caracteristica_ExpressaoRelacional = caracteristica_ExpressaoRelacional
        
    @property
    def valor(self) -> str:
        return self.__valor

    @valor.setter
    def valor(self, valor: str):
        self.__valor = valor

    @property
    def operadorRelacional(self) -> str:
        return self.__operadorRelacional

    @operadorRelacional.setter
    def operadorRelacional(self, operadorRelacional: str):
        self.__operadorRelacional = operadorRelacional

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
            if hasattr(old_value, "caracteristica_Atributo84"):
                opp_val = getattr(old_value, "caracteristica_Atributo84", None)
                if opp_val == self:
                    setattr(old_value, "caracteristica_Atributo84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_Atributo84"):
                opp_val = getattr(value, "caracteristica_Atributo84", None)
                setattr(value, "caracteristica_Atributo84", self)

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
            if hasattr(old_value, "caracteristica_ElementoCaracteristico86"):
                opp_val = getattr(old_value, "caracteristica_ElementoCaracteristico86", None)
                if opp_val == self:
                    setattr(old_value, "caracteristica_ElementoCaracteristico86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_ElementoCaracteristico86"):
                opp_val = getattr(value, "caracteristica_ElementoCaracteristico86", None)
                setattr(value, "caracteristica_ElementoCaracteristico86", self)

class caracteristica_ExpressaoLogica(Antecedente):

    def __init__(self, operadorLogico: str, caracteristica_ExpressaoLogica: "caracteristica_Antecedente" = None, caracteristica_ExpressaoLogica81: "caracteristica_Antecedente" = None):
        self.operadorLogico = operadorLogico
        self.caracteristica_ExpressaoLogica = caracteristica_ExpressaoLogica
        self.caracteristica_ExpressaoLogica81 = caracteristica_ExpressaoLogica81
        
    @property
    def operadorLogico(self) -> str:
        return self.__operadorLogico

    @operadorLogico.setter
    def operadorLogico(self, operadorLogico: str):
        self.__operadorLogico = operadorLogico

    @property
    def caracteristica_ExpressaoLogica81(self):
        return self.__caracteristica_ExpressaoLogica81

    @caracteristica_ExpressaoLogica81.setter
    def caracteristica_ExpressaoLogica81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_ExpressaoLogica__caracteristica_ExpressaoLogica81", None)
        self.__caracteristica_ExpressaoLogica81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_Antecedente82"):
                opp_val = getattr(old_value, "caracteristica_Antecedente82", None)
                if opp_val == self:
                    setattr(old_value, "caracteristica_Antecedente82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_Antecedente82"):
                opp_val = getattr(value, "caracteristica_Antecedente82", None)
                setattr(value, "caracteristica_Antecedente82", self)

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
            if hasattr(old_value, "caracteristica_Antecedente79"):
                opp_val = getattr(old_value, "caracteristica_Antecedente79", None)
                if opp_val == self:
                    setattr(old_value, "caracteristica_Antecedente79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_Antecedente79"):
                opp_val = getattr(value, "caracteristica_Antecedente79", None)
                setattr(value, "caracteristica_Antecedente79", self)

class Acao:

    pass
class caracteristica_Designar(Acao):

    def __init__(self, valor: str, tipoValor: str, caracteristica_Designar: "caracteristica_Atributo" = None, caracteristica_Designar114: "caracteristica_InconsistenciaRegraAdaptacao" = None):
        self.valor = valor
        self.tipoValor = tipoValor
        self.caracteristica_Designar = caracteristica_Designar
        self.caracteristica_Designar114 = caracteristica_Designar114
        
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
    def caracteristica_Designar(self):
        return self.__caracteristica_Designar

    @caracteristica_Designar.setter
    def caracteristica_Designar(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Designar__caracteristica_Designar", None)
        self.__caracteristica_Designar = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_Atributo77"):
                opp_val = getattr(old_value, "caracteristica_Atributo77", None)
                if opp_val == self:
                    setattr(old_value, "caracteristica_Atributo77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_Atributo77"):
                opp_val = getattr(value, "caracteristica_Atributo77", None)
                setattr(value, "caracteristica_Atributo77", self)

    @property
    def caracteristica_Designar114(self):
        return self.__caracteristica_Designar114

    @caracteristica_Designar114.setter
    def caracteristica_Designar114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Designar__caracteristica_Designar114", None)
        self.__caracteristica_Designar114 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_InconsistenciaRegraAdaptacao113"):
                opp_val = getattr(old_value, "caracteristica_InconsistenciaRegraAdaptacao113", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_InconsistenciaRegraAdaptacao113"):
                opp_val = getattr(value, "caracteristica_InconsistenciaRegraAdaptacao113", None)
                if opp_val is None:
                    setattr(value, "caracteristica_InconsistenciaRegraAdaptacao113", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class caracteristica_LiteralAcao(Acao):

    def __init__(self, presenca: str, caracteristica_LiteralAcao: "caracteristica_ElementoCaracteristico" = None, caracteristica_LiteralAcao111: "caracteristica_InconsistenciaRegraAdaptacao" = None):
        self.presenca = presenca
        self.caracteristica_LiteralAcao = caracteristica_LiteralAcao
        self.caracteristica_LiteralAcao111 = caracteristica_LiteralAcao111
        
    @property
    def presenca(self) -> str:
        return self.__presenca

    @presenca.setter
    def presenca(self, presenca: str):
        self.__presenca = presenca

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

    @property
    def caracteristica_LiteralAcao111(self):
        return self.__caracteristica_LiteralAcao111

    @caracteristica_LiteralAcao111.setter
    def caracteristica_LiteralAcao111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_LiteralAcao__caracteristica_LiteralAcao111", None)
        self.__caracteristica_LiteralAcao111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_InconsistenciaRegraAdaptacao110"):
                opp_val = getattr(old_value, "caracteristica_InconsistenciaRegraAdaptacao110", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_InconsistenciaRegraAdaptacao110"):
                opp_val = getattr(value, "caracteristica_InconsistenciaRegraAdaptacao110", None)
                if opp_val is None:
                    setattr(value, "caracteristica_InconsistenciaRegraAdaptacao110", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class caracteristica_AcaoLogico(Acao):

    def __init__(self, operadorAcaoLogico: str, caracteristica_AcaoLogico73: "caracteristica_Acao" = None, caracteristica_AcaoLogico: "caracteristica_Acao" = None):
        self.operadorAcaoLogico = operadorAcaoLogico
        self.caracteristica_AcaoLogico73 = caracteristica_AcaoLogico73
        self.caracteristica_AcaoLogico = caracteristica_AcaoLogico
        
    @property
    def operadorAcaoLogico(self) -> str:
        return self.__operadorAcaoLogico

    @operadorAcaoLogico.setter
    def operadorAcaoLogico(self, operadorAcaoLogico: str):
        self.__operadorAcaoLogico = operadorAcaoLogico

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
            if hasattr(old_value, "caracteristica_Acao71"):
                opp_val = getattr(old_value, "caracteristica_Acao71", None)
                if opp_val == self:
                    setattr(old_value, "caracteristica_Acao71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_Acao71"):
                opp_val = getattr(value, "caracteristica_Acao71", None)
                setattr(value, "caracteristica_Acao71", self)

    @property
    def caracteristica_AcaoLogico73(self):
        return self.__caracteristica_AcaoLogico73

    @caracteristica_AcaoLogico73.setter
    def caracteristica_AcaoLogico73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_AcaoLogico__caracteristica_AcaoLogico73", None)
        self.__caracteristica_AcaoLogico73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_Acao74"):
                opp_val = getattr(old_value, "caracteristica_Acao74", None)
                if opp_val == self:
                    setattr(old_value, "caracteristica_Acao74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_Acao74"):
                opp_val = getattr(value, "caracteristica_Acao74", None)
                setattr(value, "caracteristica_Acao74", self)

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

    def __init__(self, operadorLogico: str, caracteristica_EventoLogico: "caracteristica_Evento" = None, caracteristica_EventoLogico67: "caracteristica_Evento" = None):
        self.operadorLogico = operadorLogico
        self.caracteristica_EventoLogico = caracteristica_EventoLogico
        self.caracteristica_EventoLogico67 = caracteristica_EventoLogico67
        
    @property
    def operadorLogico(self) -> str:
        return self.__operadorLogico

    @operadorLogico.setter
    def operadorLogico(self, operadorLogico: str):
        self.__operadorLogico = operadorLogico

    @property
    def caracteristica_EventoLogico67(self):
        return self.__caracteristica_EventoLogico67

    @caracteristica_EventoLogico67.setter
    def caracteristica_EventoLogico67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_EventoLogico__caracteristica_EventoLogico67", None)
        self.__caracteristica_EventoLogico67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_Evento68"):
                opp_val = getattr(old_value, "caracteristica_Evento68", None)
                if opp_val == self:
                    setattr(old_value, "caracteristica_Evento68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_Evento68"):
                opp_val = getattr(value, "caracteristica_Evento68", None)
                setattr(value, "caracteristica_Evento68", self)

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
            if hasattr(old_value, "caracteristica_Evento65"):
                opp_val = getattr(old_value, "caracteristica_Evento65", None)
                if opp_val == self:
                    setattr(old_value, "caracteristica_Evento65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_Evento65"):
                opp_val = getattr(value, "caracteristica_Evento65", None)
                setattr(value, "caracteristica_Evento65", self)

class Expressao:

    pass
class caracteristica_Acao(Expressao):

    pass
class caracteristica_Evento(Expressao):

    pass
class caracteristica_Antecedente(Expressao):

    pass
class Regra:

    pass
class caracteristica_RegraDeComposicao(Regra):

    pass
class caracteristica_RegraDeContexto(Regra):

    pass
class CaracteristicaProduto:

    pass
class caracteristica_CaracteristicaOpcionalProduto(CaracteristicaProduto):

    pass
class caracteristica_CaracteristicaMandatoriaProduto(CaracteristicaProduto):

    pass
class ElementoDeProduto:

    pass
class caracteristica_VariacaoDoisProduto(ElementoDeProduto, CaracteristicaProduto):

    def __init__(self, cardinalidadeMaxima: str):
        self.cardinalidadeMaxima = cardinalidadeMaxima
        
    @property
    def cardinalidadeMaxima(self) -> str:
        return self.__cardinalidadeMaxima

    @cardinalidadeMaxima.setter
    def cardinalidadeMaxima(self, cardinalidadeMaxima: str):
        self.__cardinalidadeMaxima = cardinalidadeMaxima

class caracteristica_VariacaoProduto(ElementoDeProduto):

    def __init__(self, cardinalidadeMinima: str, cardinalidadeMaxima: str, variacaoProdutoPai: set["caracteristica_VarianteProduto"] = None, caracteristica_VariacaoProduto: "caracteristica_CaracteristicaProduto" = None, VariacaoProduto: "caracteristica_VarianteProduto" = None):
        self.cardinalidadeMinima = cardinalidadeMinima
        self.cardinalidadeMaxima = cardinalidadeMaxima
        self.variacaoProdutoPai = variacaoProdutoPai if variacaoProdutoPai is not None else set()
        self.caracteristica_VariacaoProduto = caracteristica_VariacaoProduto
        self.VariacaoProduto = VariacaoProduto
        
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
                    

class caracteristica_AtributoProduto(ElementoDeProduto):

    def __init__(self, valor: str, tipoValor: str, AtributoProduto: "caracteristica_CaracteristicaProduto" = None, atributoProduto: "caracteristica_CaracteristicaProduto" = None):
        self.valor = valor
        self.tipoValor = tipoValor
        self.AtributoProduto = AtributoProduto
        self.atributoProduto = atributoProduto
        
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
    def atributoProduto(self):
        return self.__atributoProduto

    @atributoProduto.setter
    def atributoProduto(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_AtributoProduto__atributoProduto", None)
        self.__atributoProduto = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CaracteristicaProduto51"):
                opp_val = getattr(old_value, "CaracteristicaProduto51", None)
                if opp_val == self:
                    setattr(old_value, "CaracteristicaProduto51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CaracteristicaProduto51"):
                opp_val = getattr(value, "CaracteristicaProduto51", None)
                setattr(value, "CaracteristicaProduto51", self)

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
            if hasattr(old_value, "caracteristicaProdutoPai49"):
                opp_val = getattr(old_value, "caracteristicaProdutoPai49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristicaProdutoPai49"):
                opp_val = getattr(value, "caracteristicaProdutoPai49", None)
                if opp_val is None:
                    setattr(value, "caracteristicaProdutoPai49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class caracteristica_VarianteProduto(ElementoDeProduto):

    def __init__(self, selecionado: str, VarianteProduto: "caracteristica_VariacaoProduto" = None, variantesProduto: "caracteristica_VariacaoProduto" = None):
        self.selecionado = selecionado
        self.VarianteProduto = VarianteProduto
        self.variantesProduto = variantesProduto
        
    @property
    def selecionado(self) -> str:
        return self.__selecionado

    @selecionado.setter
    def selecionado(self, selecionado: str):
        self.__selecionado = selecionado

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

class caracteristica_CaracteristicaProduto(ElementoDeProduto):

    pass
class ElementoCaracteristico:

    pass
class Caracteristica:

    pass
class caracteristica_CaracteristicaAgrupada(ElementoCaracteristico, Caracteristica):

    pass
class caracteristica_VariacaoDois(ElementoCaracteristico, Caracteristica):

    def __init__(self, cardinalidadeMaxima: str, cardinalidadeMinimaOr: str, cardinalidadeMaximaOr: str):
        self.cardinalidadeMaxima = cardinalidadeMaxima
        self.cardinalidadeMinimaOr = cardinalidadeMinimaOr
        self.cardinalidadeMaximaOr = cardinalidadeMaximaOr
        
    @property
    def cardinalidadeMaxima(self) -> str:
        return self.__cardinalidadeMaxima

    @cardinalidadeMaxima.setter
    def cardinalidadeMaxima(self, cardinalidadeMaxima: str):
        self.__cardinalidadeMaxima = cardinalidadeMaxima

    @property
    def cardinalidadeMaximaOr(self) -> str:
        return self.__cardinalidadeMaximaOr

    @cardinalidadeMaximaOr.setter
    def cardinalidadeMaximaOr(self, cardinalidadeMaximaOr: str):
        self.__cardinalidadeMaximaOr = cardinalidadeMaximaOr

    @property
    def cardinalidadeMinimaOr(self) -> str:
        return self.__cardinalidadeMinimaOr

    @cardinalidadeMinimaOr.setter
    def cardinalidadeMinimaOr(self, cardinalidadeMinimaOr: str):
        self.__cardinalidadeMinimaOr = cardinalidadeMinimaOr

class caracteristica_CaracteristicaOpcional(ElementoCaracteristico, Caracteristica):

    pass
class caracteristica_CaracteristicaMandatoria(Caracteristica):

    pass
class PontoDeVariacao:

    pass
class caracteristica_Variante(ElementoCaracteristico, Caracteristica, PontoDeVariacao):

    pass
class caracteristica_PontoDeVariacao:

    pass
class Elemento:

    pass
class caracteristica_Caracteristica(Elemento):

    pass
class caracteristica_EntidadeDeContexto(Elemento):

    pass
class caracteristica_RaizDeContexto(Elemento):

    pass
class caracteristica_Variacao(PontoDeVariacao, Elemento):

    def __init__(self, cardinalidadeMinima: str, cardinalidadeMaxima: str, Variacao: "caracteristica_Caracteristica" = None, variacaoPai: set["caracteristica_Variante"] = None, variacoes: "caracteristica_Caracteristica" = None, Variacao34: "caracteristica_Variante" = None):
        self.cardinalidadeMinima = cardinalidadeMinima
        self.cardinalidadeMaxima = cardinalidadeMaxima
        self.Variacao = Variacao
        self.variacaoPai = variacaoPai if variacaoPai is not None else set()
        self.variacoes = variacoes
        self.Variacao34 = Variacao34
        
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
    def variacoes(self):
        return self.__variacoes

    @variacoes.setter
    def variacoes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Variacao__variacoes", None)
        self.__variacoes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Caracteristica32"):
                opp_val = getattr(old_value, "Caracteristica32", None)
                if opp_val == self:
                    setattr(old_value, "Caracteristica32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Caracteristica32"):
                opp_val = getattr(value, "Caracteristica32", None)
                setattr(value, "Caracteristica32", self)

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
            if hasattr(old_value, "caracteristicaPai26"):
                opp_val = getattr(old_value, "caracteristicaPai26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristicaPai26"):
                opp_val = getattr(value, "caracteristicaPai26", None)
                if opp_val is None:
                    setattr(value, "caracteristicaPai26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Variacao34(self):
        return self.__Variacao34

    @Variacao34.setter
    def Variacao34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Variacao__Variacao34", None)
        self.__Variacao34 = value
        
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

class caracteristica_InformacaoDeContexto(Elemento):

    def __init__(self, origem: str, validade: str, qualidade: str, tipoValor: str, valor: str, informacoesDeContexto: "caracteristica_EntidadeDeContexto" = None, InformacaoDeContexto: "caracteristica_EntidadeDeContexto" = None, caracteristica_InformacaoDeContexto: "caracteristica_EventoRelacional" = None):
        self.origem = origem
        self.validade = validade
        self.qualidade = qualidade
        self.tipoValor = tipoValor
        self.valor = valor
        self.informacoesDeContexto = informacoesDeContexto
        self.InformacaoDeContexto = InformacaoDeContexto
        self.caracteristica_InformacaoDeContexto = caracteristica_InformacaoDeContexto
        
    @property
    def validade(self) -> str:
        return self.__validade

    @validade.setter
    def validade(self, validade: str):
        self.__validade = validade

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
    def valor(self) -> str:
        return self.__valor

    @valor.setter
    def valor(self, valor: str):
        self.__valor = valor

    @property
    def origem(self) -> str:
        return self.__origem

    @origem.setter
    def origem(self, origem: str):
        self.__origem = origem

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
            if hasattr(old_value, "EntidadeDeContexto39"):
                opp_val = getattr(old_value, "EntidadeDeContexto39", None)
                if opp_val == self:
                    setattr(old_value, "EntidadeDeContexto39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EntidadeDeContexto39"):
                opp_val = getattr(value, "EntidadeDeContexto39", None)
                setattr(value, "EntidadeDeContexto39", self)

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

class caracteristica_ElementoCaracteristico(Elemento):

    pass
class caracteristica_InconsistenciaRegraAdaptacao:

    pass
class caracteristica_Simulacao:

    def __init__(self, nome: str, caracteristica_Simulacao: "caracteristica_LPS" = None, caracteristica_Simulacao88: set["caracteristica_Transicao"] = None, caracteristica_Simulacao90: set["caracteristica_Estado"] = None):
        self.nome = nome
        self.caracteristica_Simulacao = caracteristica_Simulacao
        self.caracteristica_Simulacao88 = caracteristica_Simulacao88 if caracteristica_Simulacao88 is not None else set()
        self.caracteristica_Simulacao90 = caracteristica_Simulacao90 if caracteristica_Simulacao90 is not None else set()
        
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

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
    def caracteristica_Simulacao90(self):
        return self.__caracteristica_Simulacao90

    @caracteristica_Simulacao90.setter
    def caracteristica_Simulacao90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Simulacao__caracteristica_Simulacao90", None)
        self.__caracteristica_Simulacao90 = value if value is not None else set()
        
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
    def caracteristica_Simulacao88(self):
        return self.__caracteristica_Simulacao88

    @caracteristica_Simulacao88.setter
    def caracteristica_Simulacao88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Simulacao__caracteristica_Simulacao88", None)
        self.__caracteristica_Simulacao88 = value if value is not None else set()
        
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

    def __init__(self, tipoValor: str, caracteristica_Atributo: "caracteristica_LPS" = None, atributo: "caracteristica_Caracteristica" = None, Atributo: "caracteristica_Caracteristica" = None, caracteristica_Atributo77: "caracteristica_Designar" = None, caracteristica_Atributo84: "caracteristica_ExpressaoRelacional" = None):
        self.tipoValor = tipoValor
        self.caracteristica_Atributo = caracteristica_Atributo
        self.atributo = atributo
        self.Atributo = Atributo
        self.caracteristica_Atributo77 = caracteristica_Atributo77
        self.caracteristica_Atributo84 = caracteristica_Atributo84
        
    @property
    def tipoValor(self) -> str:
        return self.__tipoValor

    @tipoValor.setter
    def tipoValor(self, tipoValor: str):
        self.__tipoValor = tipoValor

    @property
    def caracteristica_Atributo77(self):
        return self.__caracteristica_Atributo77

    @caracteristica_Atributo77.setter
    def caracteristica_Atributo77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Atributo__caracteristica_Atributo77", None)
        self.__caracteristica_Atributo77 = value
        
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

    @property
    def caracteristica_Atributo84(self):
        return self.__caracteristica_Atributo84

    @caracteristica_Atributo84.setter
    def caracteristica_Atributo84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Atributo__caracteristica_Atributo84", None)
        self.__caracteristica_Atributo84 = value
        
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
    def caracteristica_Atributo(self):
        return self.__caracteristica_Atributo

    @caracteristica_Atributo.setter
    def caracteristica_Atributo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Atributo__caracteristica_Atributo", None)
        self.__caracteristica_Atributo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_LPS13"):
                opp_val = getattr(old_value, "caracteristica_LPS13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_LPS13"):
                opp_val = getattr(value, "caracteristica_LPS13", None)
                if opp_val is None:
                    setattr(value, "caracteristica_LPS13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "caracteristicaPai28"):
                opp_val = getattr(old_value, "caracteristicaPai28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristicaPai28"):
                opp_val = getattr(value, "caracteristicaPai28", None)
                if opp_val is None:
                    setattr(value, "caracteristicaPai28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class caracteristica_CaracteristicaRaiz(Caracteristica):

    pass
class caracteristica_ElementoDeProduto:

    def __init__(self, nome: str, caracteristica_ElementoDeProduto: "caracteristica_LPS" = None, caracteristica_ElementoDeProduto41: "caracteristica_Elemento" = None):
        self.nome = nome
        self.caracteristica_ElementoDeProduto = caracteristica_ElementoDeProduto
        self.caracteristica_ElementoDeProduto41 = caracteristica_ElementoDeProduto41
        
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def caracteristica_ElementoDeProduto41(self):
        return self.__caracteristica_ElementoDeProduto41

    @caracteristica_ElementoDeProduto41.setter
    def caracteristica_ElementoDeProduto41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_ElementoDeProduto__caracteristica_ElementoDeProduto41", None)
        self.__caracteristica_ElementoDeProduto41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_Elemento42"):
                opp_val = getattr(old_value, "caracteristica_Elemento42", None)
                if opp_val == self:
                    setattr(old_value, "caracteristica_Elemento42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_Elemento42"):
                opp_val = getattr(value, "caracteristica_Elemento42", None)
                setattr(value, "caracteristica_Elemento42", self)

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
            if hasattr(old_value, "caracteristica_LPS8"):
                opp_val = getattr(old_value, "caracteristica_LPS8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_LPS8"):
                opp_val = getattr(value, "caracteristica_LPS8", None)
                if opp_val is None:
                    setattr(value, "caracteristica_LPS8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class caracteristica_Produto(CaracteristicaProduto):

    pass
class caracteristica_Regra:

    def __init__(self, nome: str, conteudo: str, caracteristica_Regra: "caracteristica_LPS" = None):
        self.nome = nome
        self.conteudo = conteudo
        self.caracteristica_Regra = caracteristica_Regra
        
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def conteudo(self) -> str:
        return self.__conteudo

    @conteudo.setter
    def conteudo(self, conteudo: str):
        self.__conteudo = conteudo

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

class caracteristica_Elemento:

    def __init__(self, nome: str, caracteristica_Elemento: "caracteristica_LPS" = None, caracteristica_Elemento42: "caracteristica_ElementoDeProduto" = None):
        self.nome = nome
        self.caracteristica_Elemento = caracteristica_Elemento
        self.caracteristica_Elemento42 = caracteristica_Elemento42
        
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def caracteristica_Elemento42(self):
        return self.__caracteristica_Elemento42

    @caracteristica_Elemento42.setter
    def caracteristica_Elemento42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Elemento__caracteristica_Elemento42", None)
        self.__caracteristica_Elemento42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_ElementoDeProduto41"):
                opp_val = getattr(old_value, "caracteristica_ElementoDeProduto41", None)
                if opp_val == self:
                    setattr(old_value, "caracteristica_ElementoDeProduto41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_ElementoDeProduto41"):
                opp_val = getattr(value, "caracteristica_ElementoDeProduto41", None)
                setattr(value, "caracteristica_ElementoDeProduto41", self)

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

class caracteristica_LPS:

    def __init__(self, valoresContextuais: str, erro: str, nome: str, caracteristica_LPS: set["caracteristica_PontoDeVariacao"] = None, caracteristica_LPS2: set["caracteristica_Elemento"] = None, caracteristica_LPS4: set["caracteristica_Regra"] = None, caracteristica_LPS6: set["caracteristica_Produto"] = None, caracteristica_LPS8: set["caracteristica_Expressao"] = None, caracteristica_LPS10: set["caracteristica_ElementoDeProduto"] = None, LpsDoSistema: "caracteristica_CaracteristicaRaiz" = None, caracteristica_LPS13: set["caracteristica_Atributo"] = None, caracteristica_LPS15: set["caracteristica_Simulacao"] = None, caracteristica_LPS17: set["caracteristica_InconsistenciaRegraAdaptacao"] = None, LPS: "caracteristica_CaracteristicaRaiz" = None):
        self.valoresContextuais = valoresContextuais
        self.erro = erro
        self.nome = nome
        self.caracteristica_LPS = caracteristica_LPS if caracteristica_LPS is not None else set()
        self.caracteristica_LPS2 = caracteristica_LPS2 if caracteristica_LPS2 is not None else set()
        self.caracteristica_LPS4 = caracteristica_LPS4 if caracteristica_LPS4 is not None else set()
        self.caracteristica_LPS6 = caracteristica_LPS6 if caracteristica_LPS6 is not None else set()
        self.caracteristica_LPS8 = caracteristica_LPS8 if caracteristica_LPS8 is not None else set()
        self.caracteristica_LPS10 = caracteristica_LPS10 if caracteristica_LPS10 is not None else set()
        self.LpsDoSistema = LpsDoSistema
        self.caracteristica_LPS13 = caracteristica_LPS13 if caracteristica_LPS13 is not None else set()
        self.caracteristica_LPS15 = caracteristica_LPS15 if caracteristica_LPS15 is not None else set()
        self.caracteristica_LPS17 = caracteristica_LPS17 if caracteristica_LPS17 is not None else set()
        self.LPS = LPS
        
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
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

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
    def caracteristica_LPS13(self):
        return self.__caracteristica_LPS13

    @caracteristica_LPS13.setter
    def caracteristica_LPS13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_LPS__caracteristica_LPS13", None)
        self.__caracteristica_LPS13 = value if value is not None else set()
        
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
