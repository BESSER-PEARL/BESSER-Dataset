from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Enumeration(Enum):
    pass

############################################
# Definition of Classes
############################################










class Deposito:

    def __init__(self, Valor: float, Nome: str):
        self.Valor = Valor
        self.Nome = Nome
        
        pass
    @property
    def Nome(self):
        return self.__Nome
    @Nome.setter
    def Nome(self, Nome: str):
        self.__Nome = Nome

    @property
    def Valor(self):
        return self.__Valor
    @Valor.setter
    def Valor(self, Valor: float):
        self.__Valor = Valor



class Transferencia:

    def __init__(self, Nome: str, Valor: float):
        self.Nome = Nome
        self.Valor = Valor
        
        pass
    @property
    def Nome(self):
        return self.__Nome
    @Nome.setter
    def Nome(self, Nome: str):
        self.__Nome = Nome

    @property
    def Valor(self):
        return self.__Valor
    @Valor.setter
    def Valor(self, Valor: float):
        self.__Valor = Valor



class Cofre:

    def __init__(self, Dinheiro_Armazenado: float, Emprestimo_Total: float):
        self.Dinheiro_Armazenado = Dinheiro_Armazenado
        self.Emprestimo_Total = Emprestimo_Total
        
        pass
    @property
    def Dinheiro_Armazenado(self):
        return self.__Dinheiro_Armazenado
    @Dinheiro_Armazenado.setter
    def Dinheiro_Armazenado(self, Dinheiro_Armazenado: float):
        self.__Dinheiro_Armazenado = Dinheiro_Armazenado

    @property
    def Emprestimo_Total(self):
        return self.__Emprestimo_Total
    @Emprestimo_Total.setter
    def Emprestimo_Total(self, Emprestimo_Total: float):
        self.__Emprestimo_Total = Emprestimo_Total



class Emprestimo:

    def __init__(self, Valor: float):
        self.Valor = Valor
        
        pass
    @property
    def Valor(self):
        return self.__Valor
    @Valor.setter
    def Valor(self, Valor: float):
        self.__Valor = Valor



class Conta_Normal:

    def __init__(self, id: int):
        self.id = id
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id



class Conta_Conjunta:

    def __init__(self, id: int):
        self.id = id
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id



class Remover_Conta:

    pass


class CRUD:

    def __init__(self, Adicionar_Conta: str, Remover_Conta: str):
        self.Adicionar_Conta = Adicionar_Conta
        self.Remover_Conta = Remover_Conta
        
        pass
    @property
    def Remover_Conta(self):
        return self.__Remover_Conta
    @Remover_Conta.setter
    def Remover_Conta(self, Remover_Conta: str):
        self.__Remover_Conta = Remover_Conta

    @property
    def Adicionar_Conta(self):
        return self.__Adicionar_Conta
    @Adicionar_Conta.setter
    def Adicionar_Conta(self, Adicionar_Conta: str):
        self.__Adicionar_Conta = Adicionar_Conta



class Conta_Poupan_a:

    def __init__(self, Nome: str, CPF: int, Senha: float):
        self.Nome = Nome
        self.CPF = CPF
        self.Senha = Senha
        
        pass
    @property
    def Senha(self):
        return self.__Senha
    @Senha.setter
    def Senha(self, Senha: float):
        self.__Senha = Senha

    @property
    def Nome(self):
        return self.__Nome
    @Nome.setter
    def Nome(self, Nome: str):
        self.__Nome = Nome

    @property
    def CPF(self):
        return self.__CPF
    @CPF.setter
    def CPF(self, CPF: int):
        self.__CPF = CPF



class Conta_Corrente:

    def __init__(self, Nome: str, CPF: int, Senha: float, Taxa_de_Movimenta__o: float):
        self.Nome = Nome
        self.CPF = CPF
        self.Senha = Senha
        self.Taxa_de_Movimenta__o = Taxa_de_Movimenta__o
        
        pass
    @property
    def Nome(self):
        return self.__Nome
    @Nome.setter
    def Nome(self, Nome: str):
        self.__Nome = Nome

    @property
    def Taxa_de_Movimenta__o(self):
        return self.__Taxa_de_Movimenta__o
    @Taxa_de_Movimenta__o.setter
    def Taxa_de_Movimenta__o(self, Taxa_de_Movimenta__o: float):
        self.__Taxa_de_Movimenta__o = Taxa_de_Movimenta__o

    @property
    def Senha(self):
        return self.__Senha
    @Senha.setter
    def Senha(self, Senha: float):
        self.__Senha = Senha

    @property
    def CPF(self):
        return self.__CPF
    @CPF.setter
    def CPF(self, CPF: int):
        self.__CPF = CPF



class Class:

    pass


class Autenticavel:

    def __init__(self, Autenticar: str, Senha: str, contaBancaria4: "ContaBancaria" = None):
        self.Autenticar = Autenticar
        self.Senha = Senha
        self.contaBancaria4 = contaBancaria4
        
        pass
    @property
    def Autenticar(self):
        return self.__Autenticar
    @Autenticar.setter
    def Autenticar(self, Autenticar: str):
        self.__Autenticar = Autenticar

    @property
    def Senha(self):
        return self.__Senha
    @Senha.setter
    def Senha(self, Senha: str):
        self.__Senha = Senha

    @property
    def contaBancaria4(self):
        return self.__contaBancaria4
    @contaBancaria4.setter
    def contaBancaria4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Autenticavel__contaBancaria4", None)
        self.__contaBancaria4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "autenticavel5"):
                opp_val = getattr(old_value, "autenticavel5", None)
                if opp_val == self:
                    setattr(old_value, "autenticavel5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "autenticavel5"):
                opp_val = getattr(value, "autenticavel5", None)
                setattr(value, "autenticavel5", self)



class IAutenticavel:

    def __init__(self, Autenticar: str, i2: "IAutenticavel" = None, i3: "IAutenticavel" = None):
        self.Autenticar = Autenticar
        self.i2 = i2
        self.i3 = i3
        
        pass
    @property
    def Autenticar(self):
        return self.__Autenticar
    @Autenticar.setter
    def Autenticar(self, Autenticar: str):
        self.__Autenticar = Autenticar

    @property
    def i3(self):
        return self.__i3
    @i3.setter
    def i3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_IAutenticavel__i3", None)
        self.__i3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "i2"):
                opp_val = getattr(old_value, "i2", None)
                if opp_val == self:
                    setattr(old_value, "i2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "i2"):
                opp_val = getattr(value, "i2", None)
                setattr(value, "i2", self)

    @property
    def i2(self):
        return self.__i2
    @i2.setter
    def i2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_IAutenticavel__i2", None)
        self.__i2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "i3"):
                opp_val = getattr(old_value, "i3", None)
                if opp_val == self:
                    setattr(old_value, "i3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "i3"):
                opp_val = getattr(value, "i3", None)
                setattr(value, "i3", self)



class SistemaInterno:

    def __init__(self, Entrar: IAutenticavel, _attr: IAutenticavel, _attr1: str):
        self.Entrar = Entrar
        self._attr = _attr
        self._attr1 = _attr1
        
        pass
    @property
    def _attr1(self):
        return self.___attr1
    @_attr1.setter
    def _attr1(self, _attr1: str):
        self.___attr1 = _attr1

    @property
    def _attr(self):
        return self.___attr
    @_attr.setter
    def _attr(self, _attr: IAutenticavel):
        self.___attr = _attr

    @property
    def Entrar(self):
        return self.__Entrar
    @Entrar.setter
    def Entrar(self, Entrar: IAutenticavel):
        self.__Entrar = Entrar



class FixedAccount:

    def __init__(self, chequeBookNo: str):
        self.chequeBookNo = chequeBookNo
        
        pass
    @property
    def chequeBookNo(self):
        return self.__chequeBookNo
    @chequeBookNo.setter
    def chequeBookNo(self, chequeBookNo: str):
        self.__chequeBookNo = chequeBookNo



class SalvarConta:

    def __init__(self, interestRate: float, noticeGiven: bool):
        self.interestRate = interestRate
        self.noticeGiven = noticeGiven
        
        pass
    @property
    def interestRate(self):
        return self.__interestRate
    @interestRate.setter
    def interestRate(self, interestRate: float):
        self.__interestRate = interestRate

    @property
    def noticeGiven(self):
        return self.__noticeGiven
    @noticeGiven.setter
    def noticeGiven(self, noticeGiven: bool):
        self.__noticeGiven = noticeGiven



class ContaBancaria:

    def __init__(self, NumeroConta: int, NomeConta: str, Saldo: float, bank1: "Banco" = None, autenticavel5: "Autenticavel" = None):
        self.NumeroConta = NumeroConta
        self.NomeConta = NomeConta
        self.Saldo = Saldo
        self.bank1 = bank1
        self.autenticavel5 = autenticavel5
        
        pass
    @property
    def Saldo(self):
        return self.__Saldo
    @Saldo.setter
    def Saldo(self, Saldo: float):
        self.__Saldo = Saldo

    @property
    def NomeConta(self):
        return self.__NomeConta
    @NomeConta.setter
    def NomeConta(self, NomeConta: str):
        self.__NomeConta = NomeConta

    @property
    def NumeroConta(self):
        return self.__NumeroConta
    @NumeroConta.setter
    def NumeroConta(self, NumeroConta: int):
        self.__NumeroConta = NumeroConta

    @property
    def bank1(self):
        return self.__bank1
    @bank1.setter
    def bank1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ContaBancaria__bank1", None)
        self.__bank1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bankAccount0"):
                opp_val = getattr(old_value, "bankAccount0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bankAccount0"):
                opp_val = getattr(value, "bankAccount0", None)
                if opp_val is None:
                    setattr(value, "bankAccount0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def autenticavel5(self):
        return self.__autenticavel5
    @autenticavel5.setter
    def autenticavel5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ContaBancaria__autenticavel5", None)
        self.__autenticavel5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contaBancaria4"):
                opp_val = getattr(old_value, "contaBancaria4", None)
                if opp_val == self:
                    setattr(old_value, "contaBancaria4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contaBancaria4"):
                opp_val = getattr(value, "contaBancaria4", None)
                setattr(value, "contaBancaria4", self)



class Banco:

    def __init__(self, NomeBanco: str, bankAccount0: set["ContaBancaria"] = None):
        self.NomeBanco = NomeBanco
        self.bankAccount0 = bankAccount0 if bankAccount0 is not None else set()
        
        pass
    @property
    def NomeBanco(self):
        return self.__NomeBanco
    @NomeBanco.setter
    def NomeBanco(self, NomeBanco: str):
        self.__NomeBanco = NomeBanco

    @property
    def bankAccount0(self):
        return self.__bankAccount0
    @bankAccount0.setter
    def bankAccount0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Banco__bankAccount0", None)
        self.__bankAccount0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bank1"):
                    opp_val = getattr(item, "bank1", None)
                    
                    if opp_val == self:
                        setattr(item, "bank1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bank1"):
                    opp_val = getattr(item, "bank1", None)
                    
                    setattr(item, "bank1", self)
                    

