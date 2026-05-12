from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class transaction_TransactionType(Enum):
    pass
class account_AccountType(Enum):
    pass

############################################
# Definition of Classes
############################################










class Direccion:

    def __init__(self, idDireccion: int, idEstado: int, estado: str, idMunicipio: int, municipio: str, ciudad: str, zona: str, cp: int, asentamiento: str, tipo: str):
        self.idDireccion = idDireccion
        self.idEstado = idEstado
        self.estado = estado
        self.idMunicipio = idMunicipio
        self.municipio = municipio
        self.ciudad = ciudad
        self.zona = zona
        self.cp = cp
        self.asentamiento = asentamiento
        self.tipo = tipo
        
        pass
    @property
    def idDireccion(self):
        return self.__idDireccion
    @idDireccion.setter
    def idDireccion(self, idDireccion: int):
        self.__idDireccion = idDireccion

    @property
    def idMunicipio(self):
        return self.__idMunicipio
    @idMunicipio.setter
    def idMunicipio(self, idMunicipio: int):
        self.__idMunicipio = idMunicipio

    @property
    def municipio(self):
        return self.__municipio
    @municipio.setter
    def municipio(self, municipio: str):
        self.__municipio = municipio

    @property
    def tipo(self):
        return self.__tipo
    @tipo.setter
    def tipo(self, tipo: str):
        self.__tipo = tipo

    @property
    def idEstado(self):
        return self.__idEstado
    @idEstado.setter
    def idEstado(self, idEstado: int):
        self.__idEstado = idEstado

    @property
    def asentamiento(self):
        return self.__asentamiento
    @asentamiento.setter
    def asentamiento(self, asentamiento: str):
        self.__asentamiento = asentamiento

    @property
    def zona(self):
        return self.__zona
    @zona.setter
    def zona(self, zona: str):
        self.__zona = zona

    @property
    def ciudad(self):
        return self.__ciudad
    @ciudad.setter
    def ciudad(self, ciudad: str):
        self.__ciudad = ciudad

    @property
    def estado(self):
        return self.__estado
    @estado.setter
    def estado(self, estado: str):
        self.__estado = estado

    @property
    def cp(self):
        return self.__cp
    @cp.setter
    def cp(self, cp: int):
        self.__cp = cp



class Personas:

    def __init__(self, idPersona: int, nombre: str, aPaterno: str, aMaterno: str, telefono: str, estado: str):
        self.idPersona = idPersona
        self.nombre = nombre
        self.aPaterno = aPaterno
        self.aMaterno = aMaterno
        self.telefono = telefono
        self.estado = estado
        
        pass
    @property
    def telefono(self):
        return self.__telefono
    @telefono.setter
    def telefono(self, telefono: str):
        self.__telefono = telefono

    @property
    def idPersona(self):
        return self.__idPersona
    @idPersona.setter
    def idPersona(self, idPersona: int):
        self.__idPersona = idPersona

    @property
    def aMaterno(self):
        return self.__aMaterno
    @aMaterno.setter
    def aMaterno(self, aMaterno: str):
        self.__aMaterno = aMaterno

    @property
    def estado(self):
        return self.__estado
    @estado.setter
    def estado(self, estado: str):
        self.__estado = estado

    @property
    def aPaterno(self):
        return self.__aPaterno
    @aPaterno.setter
    def aPaterno(self, aPaterno: str):
        self.__aPaterno = aPaterno

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: str):
        self.__nombre = nombre



class Login1:

    def __init__(self, usuario: str, password: str):
        self.usuario = usuario
        self.password = password
        
        pass
    @property
    def usuario(self):
        return self.__usuario
    @usuario.setter
    def usuario(self, usuario: str):
        self.__usuario = usuario

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password



class Cliente:

    def __init__(self, idCliente: int, noTarjeta: str, idPersona: int, idDireccion: int, idPrestamo: int, idDiaPago: int, idAval: int, contactoReferencia: str, fechaInicio: date):
        self.idCliente = idCliente
        self.noTarjeta = noTarjeta
        self.idPersona = idPersona
        self.idDireccion = idDireccion
        self.idPrestamo = idPrestamo
        self.idDiaPago = idDiaPago
        self.idAval = idAval
        self.contactoReferencia = contactoReferencia
        self.fechaInicio = fechaInicio
        
        pass
    @property
    def idDireccion(self):
        return self.__idDireccion
    @idDireccion.setter
    def idDireccion(self, idDireccion: int):
        self.__idDireccion = idDireccion

    @property
    def contactoReferencia(self):
        return self.__contactoReferencia
    @contactoReferencia.setter
    def contactoReferencia(self, contactoReferencia: str):
        self.__contactoReferencia = contactoReferencia

    @property
    def noTarjeta(self):
        return self.__noTarjeta
    @noTarjeta.setter
    def noTarjeta(self, noTarjeta: str):
        self.__noTarjeta = noTarjeta

    @property
    def idPrestamo(self):
        return self.__idPrestamo
    @idPrestamo.setter
    def idPrestamo(self, idPrestamo: int):
        self.__idPrestamo = idPrestamo

    @property
    def idAval(self):
        return self.__idAval
    @idAval.setter
    def idAval(self, idAval: int):
        self.__idAval = idAval

    @property
    def idPersona(self):
        return self.__idPersona
    @idPersona.setter
    def idPersona(self, idPersona: int):
        self.__idPersona = idPersona

    @property
    def fechaInicio(self):
        return self.__fechaInicio
    @fechaInicio.setter
    def fechaInicio(self, fechaInicio: date):
        self.__fechaInicio = fechaInicio

    @property
    def idCliente(self):
        return self.__idCliente
    @idCliente.setter
    def idCliente(self, idCliente: int):
        self.__idCliente = idCliente

    @property
    def idDiaPago(self):
        return self.__idDiaPago
    @idDiaPago.setter
    def idDiaPago(self, idDiaPago: int):
        self.__idDiaPago = idDiaPago



class gerente:

    def __init__(self, idGerente: int, idPersona: str, id: str, idZona: int, idUsuario: int):
        self.idGerente = idGerente
        self.idPersona = idPersona
        self.id = id
        self.idZona = idZona
        self.idUsuario = idUsuario
        
        pass
    @property
    def idUsuario(self):
        return self.__idUsuario
    @idUsuario.setter
    def idUsuario(self, idUsuario: int):
        self.__idUsuario = idUsuario

    @property
    def idZona(self):
        return self.__idZona
    @idZona.setter
    def idZona(self, idZona: int):
        self.__idZona = idZona

    @property
    def idGerente(self):
        return self.__idGerente
    @idGerente.setter
    def idGerente(self, idGerente: int):
        self.__idGerente = idGerente

    @property
    def idPersona(self):
        return self.__idPersona
    @idPersona.setter
    def idPersona(self, idPersona: str):
        self.__idPersona = idPersona

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id



class Class:

    def __init__(self, attribute: str, attribute2: str):
        self.attribute = attribute
        self.attribute2 = attribute2
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: str):
        self.__attribute2 = attribute2



class account_Account:

    def __init__(self, accountNo: str, type: account_AccountType, balance: float, customer0: "Customer" = None, transactions2: set["transaction_Transaction"] = None):
        self.accountNo = accountNo
        self.type = type
        self.balance = balance
        self.customer0 = customer0
        self.transactions2 = transactions2 if transactions2 is not None else set()
        
        pass
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: account_AccountType):
        self.__type = type

    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, balance: float):
        self.__balance = balance

    @property
    def accountNo(self):
        return self.__accountNo
    @accountNo.setter
    def accountNo(self, accountNo: str):
        self.__accountNo = accountNo

    @property
    def customer0(self):
        return self.__customer0
    @customer0.setter
    def customer0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_account_Account__customer0", None)
        self.__customer0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "a1"):
                opp_val = getattr(old_value, "a1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "a1"):
                opp_val = getattr(value, "a1", None)
                if opp_val is None:
                    setattr(value, "a1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def transactions2(self):
        return self.__transactions2
    @transactions2.setter
    def transactions2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_account_Account__transactions2", None)
        self.__transactions2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "account3"):
                    opp_val = getattr(item, "account3", None)
                    
                    if opp_val == self:
                        setattr(item, "account3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "account3"):
                    opp_val = getattr(item, "account3", None)
                    
                    setattr(item, "account3", self)
                    



class account_CheckingAccount:

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name



class account_CertificatesOfDepositAccount:

    def __init__(self, timePeriod: int, interestRate: float):
        self.timePeriod = timePeriod
        self.interestRate = interestRate
        
        pass
    @property
    def interestRate(self):
        return self.__interestRate
    @interestRate.setter
    def interestRate(self, interestRate: float):
        self.__interestRate = interestRate

    @property
    def timePeriod(self):
        return self.__timePeriod
    @timePeriod.setter
    def timePeriod(self, timePeriod: int):
        self.__timePeriod = timePeriod



class account_SavingsAccount:

    def __init__(self, interestRate: float):
        self.interestRate = interestRate
        
        pass
    @property
    def interestRate(self):
        return self.__interestRate
    @interestRate.setter
    def interestRate(self, interestRate: float):
        self.__interestRate = interestRate



class transaction_TransferTransaction:

    def __init__(self, targetAccount: account_Account, sourceAccount: account_Account):
        self.targetAccount = targetAccount
        self.sourceAccount = sourceAccount
        
        pass
    @property
    def sourceAccount(self):
        return self.__sourceAccount
    @sourceAccount.setter
    def sourceAccount(self, sourceAccount: account_Account):
        self.__sourceAccount = sourceAccount

    @property
    def targetAccount(self):
        return self.__targetAccount
    @targetAccount.setter
    def targetAccount(self, targetAccount: account_Account):
        self.__targetAccount = targetAccount



class transaction_WithdrawTransaction:

    pass


class transaction_DepositTransaction:

    pass


class transaction_Transaction:

    def __init__(self, id: int, type: transaction_TransactionType, transactionTime: date, amount: float, account3: "account_Account" = None):
        self.id = id
        self.type = type
        self.transactionTime = transactionTime
        self.amount = amount
        self.account3 = account3
        
        pass
    @property
    def transactionTime(self):
        return self.__transactionTime
    @transactionTime.setter
    def transactionTime(self, transactionTime: date):
        self.__transactionTime = transactionTime

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: transaction_TransactionType):
        self.__type = type

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: float):
        self.__amount = amount

    @property
    def account3(self):
        return self.__account3
    @account3.setter
    def account3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transaction_Transaction__account3", None)
        self.__account3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transactions2"):
                opp_val = getattr(old_value, "transactions2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transactions2"):
                opp_val = getattr(value, "transactions2", None)
                if opp_val is None:
                    setattr(value, "transactions2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Login:

    def __init__(self, username: str, securityAnswer: str, password: str, securityQuestion: str, lastLoginTime: date, customer5: "Customer" = None):
        self.username = username
        self.securityAnswer = securityAnswer
        self.password = password
        self.securityQuestion = securityQuestion
        self.lastLoginTime = lastLoginTime
        self.customer5 = customer5
        
        pass
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def lastLoginTime(self):
        return self.__lastLoginTime
    @lastLoginTime.setter
    def lastLoginTime(self, lastLoginTime: date):
        self.__lastLoginTime = lastLoginTime

    @property
    def securityAnswer(self):
        return self.__securityAnswer
    @securityAnswer.setter
    def securityAnswer(self, securityAnswer: str):
        self.__securityAnswer = securityAnswer

    @property
    def securityQuestion(self):
        return self.__securityQuestion
    @securityQuestion.setter
    def securityQuestion(self, securityQuestion: str):
        self.__securityQuestion = securityQuestion

    @property
    def customer5(self):
        return self.__customer5
    @customer5.setter
    def customer5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Login__customer5", None)
        self.__customer5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "login4"):
                opp_val = getattr(old_value, "login4", None)
                if opp_val == self:
                    setattr(old_value, "login4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "login4"):
                opp_val = getattr(value, "login4", None)
                setattr(value, "login4", self)



class Customer:

    def __init__(self, name: str, dateOfBirth: date, address: str, phoneNumber: str, emailAddress: str, a1: set["account_Account"] = None, login4: "Login" = None):
        self.name = name
        self.dateOfBirth = dateOfBirth
        self.address = address
        self.phoneNumber = phoneNumber
        self.emailAddress = emailAddress
        self.a1 = a1 if a1 is not None else set()
        self.login4 = login4
        
        pass
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def emailAddress(self):
        return self.__emailAddress
    @emailAddress.setter
    def emailAddress(self, emailAddress: str):
        self.__emailAddress = emailAddress

    @property
    def dateOfBirth(self):
        return self.__dateOfBirth
    @dateOfBirth.setter
    def dateOfBirth(self, dateOfBirth: date):
        self.__dateOfBirth = dateOfBirth

    @property
    def phoneNumber(self):
        return self.__phoneNumber
    @phoneNumber.setter
    def phoneNumber(self, phoneNumber: str):
        self.__phoneNumber = phoneNumber

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def login4(self):
        return self.__login4
    @login4.setter
    def login4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__login4", None)
        self.__login4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer5"):
                opp_val = getattr(old_value, "customer5", None)
                if opp_val == self:
                    setattr(old_value, "customer5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer5"):
                opp_val = getattr(value, "customer5", None)
                setattr(value, "customer5", self)

    @property
    def a1(self):
        return self.__a1
    @a1.setter
    def a1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__a1", None)
        self.__a1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "customer0"):
                    opp_val = getattr(item, "customer0", None)
                    
                    if opp_val == self:
                        setattr(item, "customer0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "customer0"):
                    opp_val = getattr(item, "customer0", None)
                    
                    setattr(item, "customer0", self)
                    

