from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class myDsl_Atributo:

    pass
class myDsl_OperacaoCascada:

    def __init__(self, operacao: str, myDsl_OperacaoCascada: "myDsl_Operacao" = None, myDsl_OperacaoCascada33: "myDsl_Operacao" = None):
        self.operacao = operacao
        self.myDsl_OperacaoCascada = myDsl_OperacaoCascada
        self.myDsl_OperacaoCascada33 = myDsl_OperacaoCascada33
        
    @property
    def operacao(self) -> str:
        return self.__operacao

    @operacao.setter
    def operacao(self, operacao: str):
        self.__operacao = operacao

    @property
    def myDsl_OperacaoCascada33(self):
        return self.__myDsl_OperacaoCascada33

    @myDsl_OperacaoCascada33.setter
    def myDsl_OperacaoCascada33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_OperacaoCascada__myDsl_OperacaoCascada33", None)
        self.__myDsl_OperacaoCascada33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Operacao32"):
                opp_val = getattr(old_value, "myDsl_Operacao32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Operacao32"):
                opp_val = getattr(value, "myDsl_Operacao32", None)
                if opp_val is None:
                    setattr(value, "myDsl_Operacao32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_OperacaoCascada(self):
        return self.__myDsl_OperacaoCascada

    @myDsl_OperacaoCascada.setter
    def myDsl_OperacaoCascada(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_OperacaoCascada__myDsl_OperacaoCascada", None)
        self.__myDsl_OperacaoCascada = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Operacao30"):
                opp_val = getattr(old_value, "myDsl_Operacao30", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Operacao30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Operacao30"):
                opp_val = getattr(value, "myDsl_Operacao30", None)
                setattr(value, "myDsl_Operacao30", self)

class myDsl_Operacao:

    pass
class myDsl_Associacao:

    def __init__(self, associacao: str, myDsl_Associacao: "myDsl_Atributo" = None):
        self.associacao = associacao
        self.myDsl_Associacao = myDsl_Associacao
        
    @property
    def associacao(self) -> str:
        return self.__associacao

    @associacao.setter
    def associacao(self, associacao: str):
        self.__associacao = associacao

    @property
    def myDsl_Associacao(self):
        return self.__myDsl_Associacao

    @myDsl_Associacao.setter
    def myDsl_Associacao(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Associacao__myDsl_Associacao", None)
        self.__myDsl_Associacao = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Atributo26"):
                opp_val = getattr(old_value, "myDsl_Atributo26", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Atributo26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Atributo26"):
                opp_val = getattr(value, "myDsl_Atributo26", None)
                setattr(value, "myDsl_Atributo26", self)

class myDsl_AtributoTipo:

    def __init__(self, tipoPrimitivo: str, tipoColecao: str, tipoObjeto: str, myDsl_AtributoTipo: "myDsl_Atributo" = None):
        self.tipoPrimitivo = tipoPrimitivo
        self.tipoColecao = tipoColecao
        self.tipoObjeto = tipoObjeto
        self.myDsl_AtributoTipo = myDsl_AtributoTipo
        
    @property
    def tipoColecao(self) -> str:
        return self.__tipoColecao

    @tipoColecao.setter
    def tipoColecao(self, tipoColecao: str):
        self.__tipoColecao = tipoColecao

    @property
    def tipoPrimitivo(self) -> str:
        return self.__tipoPrimitivo

    @tipoPrimitivo.setter
    def tipoPrimitivo(self, tipoPrimitivo: str):
        self.__tipoPrimitivo = tipoPrimitivo

    @property
    def tipoObjeto(self) -> str:
        return self.__tipoObjeto

    @tipoObjeto.setter
    def tipoObjeto(self, tipoObjeto: str):
        self.__tipoObjeto = tipoObjeto

    @property
    def myDsl_AtributoTipo(self):
        return self.__myDsl_AtributoTipo

    @myDsl_AtributoTipo.setter
    def myDsl_AtributoTipo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_AtributoTipo__myDsl_AtributoTipo", None)
        self.__myDsl_AtributoTipo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Atributo24"):
                opp_val = getattr(old_value, "myDsl_Atributo24", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Atributo24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Atributo24"):
                opp_val = getattr(value, "myDsl_Atributo24", None)
                setattr(value, "myDsl_Atributo24", self)

class myDsl_Nome_Atributo:

    def __init__(self, nome: str, myDsl_Nome_Atributo: "myDsl_Atributo" = None):
        self.nome = nome
        self.myDsl_Nome_Atributo = myDsl_Nome_Atributo
        
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def myDsl_Nome_Atributo(self):
        return self.__myDsl_Nome_Atributo

    @myDsl_Nome_Atributo.setter
    def myDsl_Nome_Atributo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Nome_Atributo__myDsl_Nome_Atributo", None)
        self.__myDsl_Nome_Atributo = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Atributo22"):
                opp_val = getattr(old_value, "myDsl_Atributo22", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Atributo22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Atributo22"):
                opp_val = getattr(value, "myDsl_Atributo22", None)
                setattr(value, "myDsl_Atributo22", self)

class myDsl_Atributos:

    pass
class myDsl_Nome:

    def __init__(self, nome: str, myDsl_Nome: "myDsl_Entidade" = None):
        self.nome = nome
        self.myDsl_Nome = myDsl_Nome
        
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def myDsl_Nome(self):
        return self.__myDsl_Nome

    @myDsl_Nome.setter
    def myDsl_Nome(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Nome__myDsl_Nome", None)
        self.__myDsl_Nome = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Entidade13"):
                opp_val = getattr(old_value, "myDsl_Entidade13", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Entidade13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Entidade13"):
                opp_val = getattr(value, "myDsl_Entidade13", None)
                setattr(value, "myDsl_Entidade13", self)

class myDsl_Entidade:

    pass
class myDsl_Entidades:

    pass
class myDsl_ApiNome:

    def __init__(self, nome: str, myDsl_ApiNome: "myDsl_Api" = None):
        self.nome = nome
        self.myDsl_ApiNome = myDsl_ApiNome
        
    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def myDsl_ApiNome(self):
        return self.__myDsl_ApiNome

    @myDsl_ApiNome.setter
    def myDsl_ApiNome(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_ApiNome__myDsl_ApiNome", None)
        self.__myDsl_ApiNome = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_Api4"):
                opp_val = getattr(old_value, "myDsl_Api4", None)
                if opp_val == self:
                    setattr(old_value, "myDsl_Api4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_Api4"):
                opp_val = getattr(value, "myDsl_Api4", None)
                setattr(value, "myDsl_Api4", self)

class myDsl_Api:

    pass
class myDsl_Greeting:

    pass
class myDsl_Model:

    pass