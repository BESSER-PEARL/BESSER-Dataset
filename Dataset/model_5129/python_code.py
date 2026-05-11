from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Validade(Enum):
    Volatil = "Volatil"
    Frequente = "Frequente"
    Raramente = "Raramente"
    Permanente = "Permanente"
class Origem(Enum):
    Sentida = "Sentida"
    Usuario = "Usuario"
    Perfil = "Perfil"
    Derivada = "Derivada"
class TipoValor(Enum):
    TInteger = "TInteger"
    TString = "TString"
    TFloat = "TFloat"
    TBoolean = "TBoolean"
class OperadorLogico(Enum):
    AND = "AND"
    OR = "OR"
class CardinalidadeMaxima(Enum):
    OR = "OR"
    XOR = "XOR"
class OperadorAcaoLogico(Enum):
    AND = "AND"
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
class Presenca(Enum):
    PRESENTE = "PRESENTE"
    AUSENTE = "AUSENTE"


############################################
# Definition of Classes
############################################

class PontoDeVariacao:

    pass
class caracteristica_PontoDeVariacao:

    pass
class ElementoCaracteristico:

    pass
class Caracteristica:

    pass
class caracteristica_CaracteristicaAgrupada(ElementoCaracteristico, Caracteristica):

    pass
class caracteristica_Variante(ElementoCaracteristico, PontoDeVariacao, Caracteristica):

    pass
class caracteristica_CaracteristicaOpcional(ElementoCaracteristico, Caracteristica):

    pass
class caracteristica_CaracteristicaRaiz(Caracteristica):

    pass
class caracteristica_VariacaoDois(ElementoCaracteristico, Caracteristica):

    def __init__(self, cardinalidadeMaxima: str, cardinalidadeMinimaOr: str, cardinalidadeMaximaOr: str):
        self.cardinalidadeMaxima = cardinalidadeMaxima
        self.cardinalidadeMinimaOr = cardinalidadeMinimaOr
        self.cardinalidadeMaximaOr = cardinalidadeMaximaOr
        
        pass
    @property
    def cardinalidadeMinimaOr(self):
        return self.__cardinalidadeMinimaOr

    @cardinalidadeMinimaOr.setter
    def cardinalidadeMinimaOr(self, cardinalidadeMinimaOr: str):
        self.__cardinalidadeMinimaOr = cardinalidadeMinimaOr


    @property
    def cardinalidadeMaximaOr(self):
        return self.__cardinalidadeMaximaOr

    @cardinalidadeMaximaOr.setter
    def cardinalidadeMaximaOr(self, cardinalidadeMaximaOr: str):
        self.__cardinalidadeMaximaOr = cardinalidadeMaximaOr


    @property
    def cardinalidadeMaxima(self):
        return self.__cardinalidadeMaxima

    @cardinalidadeMaxima.setter
    def cardinalidadeMaxima(self, cardinalidadeMaxima: str):
        self.__cardinalidadeMaxima = cardinalidadeMaxima


class caracteristica_CaracteristicaMandatoria(Caracteristica):

    pass
class Elemento:

    pass
class caracteristica_Atributo(Elemento):

    def __init__(self, tipoValor: str, Atributo: "caracteristica_Caracteristica" = None, atributo: "caracteristica_Caracteristica" = None):
        self.tipoValor = tipoValor
        self.Atributo = Atributo
        self.atributo = atributo
        
        pass
    @property
    def tipoValor(self):
        return self.__tipoValor

    @tipoValor.setter
    def tipoValor(self, tipoValor: str):
        self.__tipoValor = tipoValor


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
            if hasattr(old_value, "caracteristicaPai11"):
                opp_val = getattr(old_value, "caracteristicaPai11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristicaPai11"):
                opp_val = getattr(value, "caracteristicaPai11", None)
                if opp_val is None:
                    setattr(value, "caracteristicaPai11", set([self]))
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

class caracteristica_Variacao(Elemento, PontoDeVariacao):

    def __init__(self, cardinalidadeMinima: str, cardinalidadeMaxima: str, Variacao: "caracteristica_Caracteristica" = None, variacaoPai: set["caracteristica_Variante"] = None, variacoes: "caracteristica_Caracteristica" = None, Variacao18: "caracteristica_Variante" = None):
        self.cardinalidadeMinima = cardinalidadeMinima
        self.cardinalidadeMaxima = cardinalidadeMaxima
        self.Variacao = Variacao
        self.variacaoPai = variacaoPai if variacaoPai is not None else set()
        self.variacoes = variacoes
        self.Variacao18 = Variacao18
        
        pass
    @property
    def cardinalidadeMinima(self):
        return self.__cardinalidadeMinima

    @cardinalidadeMinima.setter
    def cardinalidadeMinima(self, cardinalidadeMinima: str):
        self.__cardinalidadeMinima = cardinalidadeMinima


    @property
    def cardinalidadeMaxima(self):
        return self.__cardinalidadeMaxima

    @cardinalidadeMaxima.setter
    def cardinalidadeMaxima(self, cardinalidadeMaxima: str):
        self.__cardinalidadeMaxima = cardinalidadeMaxima


    @property
    def Variacao18(self):
        return self.__Variacao18

    @Variacao18.setter
    def Variacao18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_Variacao__Variacao18", None)
        self.__Variacao18 = value
        
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
            if hasattr(old_value, "Caracteristica16"):
                opp_val = getattr(old_value, "Caracteristica16", None)
                if opp_val == self:
                    setattr(old_value, "Caracteristica16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Caracteristica16"):
                opp_val = getattr(value, "Caracteristica16", None)
                setattr(value, "Caracteristica16", self)

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
            if hasattr(old_value, "caracteristicaPai9"):
                opp_val = getattr(old_value, "caracteristicaPai9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristicaPai9"):
                opp_val = getattr(value, "caracteristicaPai9", None)
                if opp_val is None:
                    setattr(value, "caracteristicaPai9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class caracteristica_ElementoCaracteristico(Elemento):

    pass
class caracteristica_Elemento:

    def __init__(self, nome: str, caracteristica_Elemento: "caracteristica_LPS" = None):
        self.nome = nome
        self.caracteristica_Elemento = caracteristica_Elemento
        
        pass
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome


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
            if hasattr(old_value, "caracteristica_LPS"):
                opp_val = getattr(old_value, "caracteristica_LPS", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_LPS"):
                opp_val = getattr(value, "caracteristica_LPS", None)
                if opp_val is None:
                    setattr(value, "caracteristica_LPS", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class caracteristica_LPS:

    def __init__(self, nome: str, caracteristica_LPS: set["caracteristica_Elemento"] = None, caracteristica_LPS13: "caracteristica_CaracteristicaRaiz" = None):
        self.nome = nome
        self.caracteristica_LPS = caracteristica_LPS if caracteristica_LPS is not None else set()
        self.caracteristica_LPS13 = caracteristica_LPS13
        
        pass
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome


    @property
    def caracteristica_LPS13(self):
        return self.__caracteristica_LPS13

    @caracteristica_LPS13.setter
    def caracteristica_LPS13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caracteristica_LPS__caracteristica_LPS13", None)
        self.__caracteristica_LPS13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caracteristica_CaracteristicaRaiz"):
                opp_val = getattr(old_value, "caracteristica_CaracteristicaRaiz", None)
                if opp_val == self:
                    setattr(old_value, "caracteristica_CaracteristicaRaiz", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caracteristica_CaracteristicaRaiz"):
                opp_val = getattr(value, "caracteristica_CaracteristicaRaiz", None)
                setattr(value, "caracteristica_CaracteristicaRaiz", self)

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
                    

class caracteristica_Caracteristica(Elemento):

    pass