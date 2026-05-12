from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Cirurgi_o_Actor:

    pass


class Cliente_Actor:

    pass





class Confirmar_Consulta_external:

    pass


class Marcar_consulta_external:

    pass


class Ver_consultas_external:

    pass


class Cancelar_Consulta_external:

    pass


class Cl_nica_Component:

    pass


class Consulta:

    def __init__(self, ConsultaId: int, DataHora: str, Cliente: Cliente, Cirurgiao: Cirurgiao, Observacoes: str, Situacao: str, cliente0: "Cliente" = None, cirurgiao3: "Cirurgiao" = None):
        self.ConsultaId = ConsultaId
        self.DataHora = DataHora
        self.Cliente = Cliente
        self.Cirurgiao = Cirurgiao
        self.Observacoes = Observacoes
        self.Situacao = Situacao
        self.cliente0 = cliente0
        self.cirurgiao3 = cirurgiao3
        
        pass
    @property
    def Cliente(self):
        return self.__Cliente
    @Cliente.setter
    def Cliente(self, Cliente: Cliente):
        self.__Cliente = Cliente

    @property
    def DataHora(self):
        return self.__DataHora
    @DataHora.setter
    def DataHora(self, DataHora: str):
        self.__DataHora = DataHora

    @property
    def ConsultaId(self):
        return self.__ConsultaId
    @ConsultaId.setter
    def ConsultaId(self, ConsultaId: int):
        self.__ConsultaId = ConsultaId

    @property
    def Cirurgiao(self):
        return self.__Cirurgiao
    @Cirurgiao.setter
    def Cirurgiao(self, Cirurgiao: Cirurgiao):
        self.__Cirurgiao = Cirurgiao

    @property
    def Situacao(self):
        return self.__Situacao
    @Situacao.setter
    def Situacao(self, Situacao: str):
        self.__Situacao = Situacao

    @property
    def Observacoes(self):
        return self.__Observacoes
    @Observacoes.setter
    def Observacoes(self, Observacoes: str):
        self.__Observacoes = Observacoes

    @property
    def cliente0(self):
        return self.__cliente0
    @cliente0.setter
    def cliente0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Consulta__cliente0", None)
        self.__cliente0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "consulta1"):
                opp_val = getattr(old_value, "consulta1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "consulta1"):
                opp_val = getattr(value, "consulta1", None)
                if opp_val is None:
                    setattr(value, "consulta1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def cirurgiao3(self):
        return self.__cirurgiao3
    @cirurgiao3.setter
    def cirurgiao3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Consulta__cirurgiao3", None)
        self.__cirurgiao3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "consulta2"):
                opp_val = getattr(old_value, "consulta2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "consulta2"):
                opp_val = getattr(value, "consulta2", None)
                if opp_val is None:
                    setattr(value, "consulta2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Cliente:

    def __init__(self, ClienteId: int, Nome: str, Cpf: str, Email: str, Telefone: str, consulta1: set["Consulta"] = None):
        self.ClienteId = ClienteId
        self.Nome = Nome
        self.Cpf = Cpf
        self.Email = Email
        self.Telefone = Telefone
        self.consulta1 = consulta1 if consulta1 is not None else set()
        
        pass
    @property
    def ClienteId(self):
        return self.__ClienteId
    @ClienteId.setter
    def ClienteId(self, ClienteId: int):
        self.__ClienteId = ClienteId

    @property
    def Cpf(self):
        return self.__Cpf
    @Cpf.setter
    def Cpf(self, Cpf: str):
        self.__Cpf = Cpf

    @property
    def Telefone(self):
        return self.__Telefone
    @Telefone.setter
    def Telefone(self, Telefone: str):
        self.__Telefone = Telefone

    @property
    def Nome(self):
        return self.__Nome
    @Nome.setter
    def Nome(self, Nome: str):
        self.__Nome = Nome

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def consulta1(self):
        return self.__consulta1
    @consulta1.setter
    def consulta1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cliente__consulta1", None)
        self.__consulta1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cliente0"):
                    opp_val = getattr(item, "cliente0", None)
                    
                    if opp_val == self:
                        setattr(item, "cliente0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cliente0"):
                    opp_val = getattr(item, "cliente0", None)
                    
                    setattr(item, "cliente0", self)
                    



class Cirurgiao:

    def __init__(self, CirurgiaoId: int, Nome: str, Especialidade: str, consulta2: set["Consulta"] = None):
        self.CirurgiaoId = CirurgiaoId
        self.Nome = Nome
        self.Especialidade = Especialidade
        self.consulta2 = consulta2 if consulta2 is not None else set()
        
        pass
    @property
    def Especialidade(self):
        return self.__Especialidade
    @Especialidade.setter
    def Especialidade(self, Especialidade: str):
        self.__Especialidade = Especialidade

    @property
    def CirurgiaoId(self):
        return self.__CirurgiaoId
    @CirurgiaoId.setter
    def CirurgiaoId(self, CirurgiaoId: int):
        self.__CirurgiaoId = CirurgiaoId

    @property
    def Nome(self):
        return self.__Nome
    @Nome.setter
    def Nome(self, Nome: str):
        self.__Nome = Nome

    @property
    def consulta2(self):
        return self.__consulta2
    @consulta2.setter
    def consulta2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cirurgiao__consulta2", None)
        self.__consulta2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cirurgiao3"):
                    opp_val = getattr(item, "cirurgiao3", None)
                    
                    if opp_val == self:
                        setattr(item, "cirurgiao3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cirurgiao3"):
                    opp_val = getattr(item, "cirurgiao3", None)
                    
                    setattr(item, "cirurgiao3", self)
                    

