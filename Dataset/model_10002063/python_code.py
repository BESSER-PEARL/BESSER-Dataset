from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class float:

    pass


class Exame:

    def __init__(self, codigo: int, descricao: str, valor: float, procedimentos: str):
        self.codigo = codigo
        self.descricao = descricao
        self.valor = valor
        self.procedimentos = procedimentos
        
        pass
    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @property
    def valor(self):
        return self.__valor
    @valor.setter
    def valor(self, valor: float):
        self.__valor = valor

    @property
    def procedimentos(self):
        return self.__procedimentos
    @procedimentos.setter
    def procedimentos(self, procedimentos: str):
        self.__procedimentos = procedimentos

    @property
    def descricao(self):
        return self.__descricao
    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao



class Medico:

    def __init__(self, crm: int, nome: str, pedido_Exame6: set["Pedido_Exame"] = None):
        self.crm = crm
        self.nome = nome
        self.pedido_Exame6 = pedido_Exame6 if pedido_Exame6 is not None else set()
        
        pass
    @property
    def crm(self):
        return self.__crm
    @crm.setter
    def crm(self, crm: int):
        self.__crm = crm

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def pedido_Exame6(self):
        return self.__pedido_Exame6
    @pedido_Exame6.setter
    def pedido_Exame6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Medico__pedido_Exame6", None)
        self.__pedido_Exame6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "medico7"):
                    opp_val = getattr(item, "medico7", None)
                    
                    if opp_val == self:
                        setattr(item, "medico7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "medico7"):
                    opp_val = getattr(item, "medico7", None)
                    
                    setattr(item, "medico7", self)
                    



class Pedido_Exame:

    def __init__(self, codigo: int, paciente4: "Paciente" = None, medico7: "Medico" = None):
        self.codigo = codigo
        self.paciente4 = paciente4
        self.medico7 = medico7
        
        pass
    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @property
    def medico7(self):
        return self.__medico7
    @medico7.setter
    def medico7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pedido_Exame__medico7", None)
        self.__medico7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pedido_Exame6"):
                opp_val = getattr(old_value, "pedido_Exame6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pedido_Exame6"):
                opp_val = getattr(value, "pedido_Exame6", None)
                if opp_val is None:
                    setattr(value, "pedido_Exame6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def paciente4(self):
        return self.__paciente4
    @paciente4.setter
    def paciente4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pedido_Exame__paciente4", None)
        self.__paciente4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pedido_Exame5"):
                opp_val = getattr(old_value, "pedido_Exame5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pedido_Exame5"):
                opp_val = getattr(value, "pedido_Exame5", None)
                if opp_val is None:
                    setattr(value, "pedido_Exame5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class UF:

    def __init__(self, sigla: str, nome: str, cidade2: "Cidade" = None):
        self.sigla = sigla
        self.nome = nome
        self.cidade2 = cidade2
        
        pass
    @property
    def sigla(self):
        return self.__sigla
    @sigla.setter
    def sigla(self, sigla: str):
        self.__sigla = sigla

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def cidade2(self):
        return self.__cidade2
    @cidade2.setter
    def cidade2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UF__cidade2", None)
        self.__cidade2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "UF3"):
                opp_val = getattr(old_value, "UF3", None)
                if opp_val == self:
                    setattr(old_value, "UF3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "UF3"):
                opp_val = getattr(value, "UF3", None)
                setattr(value, "UF3", self)



class Cidade:

    def __init__(self, codigo: int, nome: str, ddd: int, paciente0: set["Paciente"] = None, UF3: "UF" = None):
        self.codigo = codigo
        self.nome = nome
        self.ddd = ddd
        self.paciente0 = paciente0 if paciente0 is not None else set()
        self.UF3 = UF3
        
        pass
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @property
    def ddd(self):
        return self.__ddd
    @ddd.setter
    def ddd(self, ddd: int):
        self.__ddd = ddd

    @property
    def UF3(self):
        return self.__UF3
    @UF3.setter
    def UF3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cidade__UF3", None)
        self.__UF3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cidade2"):
                opp_val = getattr(old_value, "cidade2", None)
                if opp_val == self:
                    setattr(old_value, "cidade2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cidade2"):
                opp_val = getattr(value, "cidade2", None)
                setattr(value, "cidade2", self)

    @property
    def paciente0(self):
        return self.__paciente0
    @paciente0.setter
    def paciente0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cidade__paciente0", None)
        self.__paciente0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cidade1"):
                    opp_val = getattr(item, "cidade1", None)
                    
                    if opp_val == self:
                        setattr(item, "cidade1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cidade1"):
                    opp_val = getattr(item, "cidade1", None)
                    
                    setattr(item, "cidade1", self)
                    



class Paciente:

    def __init__(self, codigo: int, nome: str, endereco: str, cep: str, telefone: str, dataNascimento: str, rg: str, cpf: str, cidade1: "Cidade" = None, pedido_Exame5: set["Pedido_Exame"] = None):
        self.codigo = codigo
        self.nome = nome
        self.endereco = endereco
        self.cep = cep
        self.telefone = telefone
        self.dataNascimento = dataNascimento
        self.rg = rg
        self.cpf = cpf
        self.cidade1 = cidade1
        self.pedido_Exame5 = pedido_Exame5 if pedido_Exame5 is not None else set()
        
        pass
    @property
    def telefone(self):
        return self.__telefone
    @telefone.setter
    def telefone(self, telefone: str):
        self.__telefone = telefone

    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self, cpf: str):
        self.__cpf = cpf

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def rg(self):
        return self.__rg
    @rg.setter
    def rg(self, rg: str):
        self.__rg = rg

    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @property
    def dataNascimento(self):
        return self.__dataNascimento
    @dataNascimento.setter
    def dataNascimento(self, dataNascimento: str):
        self.__dataNascimento = dataNascimento

    @property
    def cep(self):
        return self.__cep
    @cep.setter
    def cep(self, cep: str):
        self.__cep = cep

    @property
    def endereco(self):
        return self.__endereco
    @endereco.setter
    def endereco(self, endereco: str):
        self.__endereco = endereco

    @property
    def cidade1(self):
        return self.__cidade1
    @cidade1.setter
    def cidade1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Paciente__cidade1", None)
        self.__cidade1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "paciente0"):
                opp_val = getattr(old_value, "paciente0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "paciente0"):
                opp_val = getattr(value, "paciente0", None)
                if opp_val is None:
                    setattr(value, "paciente0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pedido_Exame5(self):
        return self.__pedido_Exame5
    @pedido_Exame5.setter
    def pedido_Exame5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Paciente__pedido_Exame5", None)
        self.__pedido_Exame5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "paciente4"):
                    opp_val = getattr(item, "paciente4", None)
                    
                    if opp_val == self:
                        setattr(item, "paciente4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "paciente4"):
                    opp_val = getattr(item, "paciente4", None)
                    
                    setattr(item, "paciente4", self)
                    

