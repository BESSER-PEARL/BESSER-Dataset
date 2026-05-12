from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class conta_AccountType(Enum):
    pass
class transacao_TransactionType(Enum):
    pass

############################################
# Definition of Classes
############################################










class NewClass:

    pass


class Login:

    def __init__(self, username: str, password: str, lastLoginTime: date, cliente3: "cliente_Customer" = None):
        self.username = username
        self.password = password
        self.lastLoginTime = lastLoginTime
        self.cliente3 = cliente3
        
        pass
    @property
    def lastLoginTime(self):
        return self.__lastLoginTime
    @lastLoginTime.setter
    def lastLoginTime(self, lastLoginTime: date):
        self.__lastLoginTime = lastLoginTime

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def cliente3(self):
        return self.__cliente3
    @cliente3.setter
    def cliente3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Login__cliente3", None)
        self.__cliente3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "login2"):
                opp_val = getattr(old_value, "login2", None)
                if opp_val == self:
                    setattr(old_value, "login2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "login2"):
                opp_val = getattr(value, "login2", None)
                setattr(value, "login2", self)



class conta:

    def __init__(self, _attr: str):
        self._attr = _attr
        
        pass
    @property
    def _attr(self):
        return self.___attr
    @_attr.setter
    def _attr(self, _attr: str):
        self.___attr = _attr



class conta_Conta:

    def __init__(self, tipo: conta_AccountType, saldo: float, cliente0: "cliente_Customer" = None, transacao4: set["transacao_transacao"] = None):
        self.tipo = tipo
        self.saldo = saldo
        self.cliente0 = cliente0
        self.transacao4 = transacao4 if transacao4 is not None else set()
        
        pass
    @property
    def tipo(self):
        return self.__tipo
    @tipo.setter
    def tipo(self, tipo: conta_AccountType):
        self.__tipo = tipo

    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self, saldo: float):
        self.__saldo = saldo

    @property
    def transacao4(self):
        return self.__transacao4
    @transacao4.setter
    def transacao4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conta_Conta__transacao4", None)
        self.__transacao4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "conta5"):
                    opp_val = getattr(item, "conta5", None)
                    
                    if opp_val == self:
                        setattr(item, "conta5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "conta5"):
                    opp_val = getattr(item, "conta5", None)
                    
                    setattr(item, "conta5", self)
                    

    @property
    def cliente0(self):
        return self.__cliente0
    @cliente0.setter
    def cliente0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conta_Conta__cliente0", None)
        self.__cliente0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conta1"):
                opp_val = getattr(old_value, "conta1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conta1"):
                opp_val = getattr(value, "conta1", None)
                if opp_val is None:
                    setattr(value, "conta1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class conta_CheckingAccount:

    pass


class conta_Poupan_a:

    def __init__(self, juros: float, tempo: int):
        self.juros = juros
        self.tempo = tempo
        
        pass
    @property
    def juros(self):
        return self.__juros
    @juros.setter
    def juros(self, juros: float):
        self.__juros = juros

    @property
    def tempo(self):
        return self.__tempo
    @tempo.setter
    def tempo(self, tempo: int):
        self.__tempo = tempo



class conta_investimento:

    def __init__(self, taxaDeJuros: float):
        self.taxaDeJuros = taxaDeJuros
        
        pass
    @property
    def taxaDeJuros(self):
        return self.__taxaDeJuros
    @taxaDeJuros.setter
    def taxaDeJuros(self, taxaDeJuros: float):
        self.__taxaDeJuros = taxaDeJuros



class transacao_Class:

    pass


class transacao_transferencia:

    def __init__(self, contaAlvo: conta_Conta, contaOrigem: conta_Conta):
        self.contaAlvo = contaAlvo
        self.contaOrigem = contaOrigem
        
        pass
    @property
    def contaOrigem(self):
        return self.__contaOrigem
    @contaOrigem.setter
    def contaOrigem(self, contaOrigem: conta_Conta):
        self.__contaOrigem = contaOrigem

    @property
    def contaAlvo(self):
        return self.__contaAlvo
    @contaAlvo.setter
    def contaAlvo(self, contaAlvo: conta_Conta):
        self.__contaAlvo = contaAlvo



class transacao_saque:

    def __init__(self, valor: str):
        self.valor = valor
        
        pass
    @property
    def valor(self):
        return self.__valor
    @valor.setter
    def valor(self, valor: str):
        self.__valor = valor



class transacao_deposito:

    def __init__(self, valor: str):
        self.valor = valor
        
        pass
    @property
    def valor(self):
        return self.__valor
    @valor.setter
    def valor(self, valor: str):
        self.__valor = valor



class transacao_transacao:

    def __init__(self, id: int, type: str, amount: float, conta5: "conta_Conta" = None):
        self.id = id
        self.type = type
        self.amount = amount
        self.conta5 = conta5
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: float):
        self.__amount = amount

    @property
    def conta5(self):
        return self.__conta5
    @conta5.setter
    def conta5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transacao_transacao__conta5", None)
        self.__conta5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transacao4"):
                opp_val = getattr(old_value, "transacao4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transacao4"):
                opp_val = getattr(value, "transacao4", None)
                if opp_val is None:
                    setattr(value, "transacao4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class cliente_Customer:

    def __init__(self, nome: str, dataNascimento: date, endere_o: str, numeroTel: str, email: str, conta1: set["conta_Conta"] = None, login2: "Login" = None):
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.endere_o = endere_o
        self.numeroTel = numeroTel
        self.email = email
        self.conta1 = conta1 if conta1 is not None else set()
        self.login2 = login2
        
        pass
    @property
    def dataNascimento(self):
        return self.__dataNascimento
    @dataNascimento.setter
    def dataNascimento(self, dataNascimento: date):
        self.__dataNascimento = dataNascimento

    @property
    def endere_o(self):
        return self.__endere_o
    @endere_o.setter
    def endere_o(self, endere_o: str):
        self.__endere_o = endere_o

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def numeroTel(self):
        return self.__numeroTel
    @numeroTel.setter
    def numeroTel(self, numeroTel: str):
        self.__numeroTel = numeroTel

    @property
    def login2(self):
        return self.__login2
    @login2.setter
    def login2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cliente_Customer__login2", None)
        self.__login2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cliente3"):
                opp_val = getattr(old_value, "cliente3", None)
                if opp_val == self:
                    setattr(old_value, "cliente3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cliente3"):
                opp_val = getattr(value, "cliente3", None)
                setattr(value, "cliente3", self)

    @property
    def conta1(self):
        return self.__conta1
    @conta1.setter
    def conta1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cliente_Customer__conta1", None)
        self.__conta1 = value if value is not None else set()
        
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
                    

