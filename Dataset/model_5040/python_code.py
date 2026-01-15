from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class bank_OnlineTransaction:

    pass
class bank_TokenTransaction:

    pass
class bank_BankerTransaction:

    pass
class Account:

    pass
class bank_InternalAccount(Account):

    pass
class bank_DeviceTransaction:

    pass
class Device:

    pass
class bank_Card(Device):

    def __init__(self, virtual: bool, id: str, issued: date, activated: date, deactivated: date, expires: date, bank_Card: "bank_Merchant" = None, bank_Card28: "bank_Card" = None, bank_Card26: "bank_Card" = None):
        self.virtual = virtual
        self.id = id
        self.issued = issued
        self.activated = activated
        self.deactivated = deactivated
        self.expires = expires
        self.bank_Card = bank_Card
        self.bank_Card28 = bank_Card28
        self.bank_Card26 = bank_Card26
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def expires(self) -> date:
        return self.__expires

    @expires.setter
    def expires(self, expires: date):
        self.__expires = expires

    @property
    def activated(self) -> date:
        return self.__activated

    @activated.setter
    def activated(self, activated: date):
        self.__activated = activated

    @property
    def deactivated(self) -> date:
        return self.__deactivated

    @deactivated.setter
    def deactivated(self, deactivated: date):
        self.__deactivated = deactivated

    @property
    def virtual(self) -> bool:
        return self.__virtual

    @virtual.setter
    def virtual(self, virtual: bool):
        self.__virtual = virtual

    @property
    def issued(self) -> date:
        return self.__issued

    @issued.setter
    def issued(self, issued: date):
        self.__issued = issued

    @property
    def bank_Card28(self):
        return self.__bank_Card28

    @bank_Card28.setter
    def bank_Card28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bank_Card__bank_Card28", None)
        self.__bank_Card28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bank_Card26"):
                opp_val = getattr(old_value, "bank_Card26", None)
                if opp_val == self:
                    setattr(old_value, "bank_Card26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bank_Card26"):
                opp_val = getattr(value, "bank_Card26", None)
                setattr(value, "bank_Card26", self)

    @property
    def bank_Card(self):
        return self.__bank_Card

    @bank_Card.setter
    def bank_Card(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bank_Card__bank_Card", None)
        self.__bank_Card = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bank_Merchant25"):
                opp_val = getattr(old_value, "bank_Merchant25", None)
                if opp_val == self:
                    setattr(old_value, "bank_Merchant25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bank_Merchant25"):
                opp_val = getattr(value, "bank_Merchant25", None)
                setattr(value, "bank_Merchant25", self)

    @property
    def bank_Card26(self):
        return self.__bank_Card26

    @bank_Card26.setter
    def bank_Card26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bank_Card__bank_Card26", None)
        self.__bank_Card26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bank_Card28"):
                opp_val = getattr(old_value, "bank_Card28", None)
                if opp_val == self:
                    setattr(old_value, "bank_Card28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bank_Card28"):
                opp_val = getattr(value, "bank_Card28", None)
                setattr(value, "bank_Card28", self)

class bank_MobilePhone(Device):

    def __init__(self, number: str, key: str):
        self.number = number
        self.key = key
        
    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

class TransactionInitiator:

    pass
class bank_Token(TransactionInitiator):

    def __init__(self, value: str, bank_Token: "bank_Device" = None, bank_Token38: "bank_Merchant" = None):
        self.value = value
        self.bank_Token = bank_Token
        self.bank_Token38 = bank_Token38
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def bank_Token(self):
        return self.__bank_Token

    @bank_Token.setter
    def bank_Token(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bank_Token__bank_Token", None)
        self.__bank_Token = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bank_Device"):
                opp_val = getattr(old_value, "bank_Device", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bank_Device"):
                opp_val = getattr(value, "bank_Device", None)
                if opp_val is None:
                    setattr(value, "bank_Device", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bank_Token38(self):
        return self.__bank_Token38

    @bank_Token38.setter
    def bank_Token38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bank_Token__bank_Token38", None)
        self.__bank_Token38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bank_Merchant39"):
                opp_val = getattr(old_value, "bank_Merchant39", None)
                if opp_val == self:
                    setattr(old_value, "bank_Merchant39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bank_Merchant39"):
                opp_val = getattr(value, "bank_Merchant39", None)
                setattr(value, "bank_Merchant39", self)

class bank_Device(TransactionInitiator):

    pass
class bank_PointOfSale:

    def __init__(self, id: str, bank_PointOfSale: "bank_Merchant" = None, bank_PointOfSale22: "bank_PostalAddress" = None, bank_PointOfSale30: "bank_DeviceTransaction" = None):
        self.id = id
        self.bank_PointOfSale = bank_PointOfSale
        self.bank_PointOfSale22 = bank_PointOfSale22
        self.bank_PointOfSale30 = bank_PointOfSale30
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def bank_PointOfSale30(self):
        return self.__bank_PointOfSale30

    @bank_PointOfSale30.setter
    def bank_PointOfSale30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bank_PointOfSale__bank_PointOfSale30", None)
        self.__bank_PointOfSale30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bank_DeviceTransaction"):
                opp_val = getattr(old_value, "bank_DeviceTransaction", None)
                if opp_val == self:
                    setattr(old_value, "bank_DeviceTransaction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bank_DeviceTransaction"):
                opp_val = getattr(value, "bank_DeviceTransaction", None)
                setattr(value, "bank_DeviceTransaction", self)

    @property
    def bank_PointOfSale(self):
        return self.__bank_PointOfSale

    @bank_PointOfSale.setter
    def bank_PointOfSale(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bank_PointOfSale__bank_PointOfSale", None)
        self.__bank_PointOfSale = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bank_Merchant20"):
                opp_val = getattr(old_value, "bank_Merchant20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bank_Merchant20"):
                opp_val = getattr(value, "bank_Merchant20", None)
                if opp_val is None:
                    setattr(value, "bank_Merchant20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bank_PointOfSale22(self):
        return self.__bank_PointOfSale22

    @bank_PointOfSale22.setter
    def bank_PointOfSale22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bank_PointOfSale__bank_PointOfSale22", None)
        self.__bank_PointOfSale22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bank_PostalAddress"):
                opp_val = getattr(old_value, "bank_PostalAddress", None)
                if opp_val == self:
                    setattr(old_value, "bank_PostalAddress", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bank_PostalAddress"):
                opp_val = getattr(value, "bank_PostalAddress", None)
                setattr(value, "bank_PostalAddress", self)

class bank_Statement:

    def __init__(self, openingBalance: str, openingDate: date, closingBalance: str, closingDate: date, bank_Statement: "bank_Account" = None, Statement: "bank_Transaction" = None, Statement17: "bank_Transaction" = None):
        self.openingBalance = openingBalance
        self.openingDate = openingDate
        self.closingBalance = closingBalance
        self.closingDate = closingDate
        self.bank_Statement = bank_Statement
        self.Statement = Statement
        self.Statement17 = Statement17
        
    @property
    def closingBalance(self) -> str:
        return self.__closingBalance

    @closingBalance.setter
    def closingBalance(self, closingBalance: str):
        self.__closingBalance = closingBalance

    @property
    def openingBalance(self) -> str:
        return self.__openingBalance

    @openingBalance.setter
    def openingBalance(self, openingBalance: str):
        self.__openingBalance = openingBalance

    @property
    def openingDate(self) -> date:
        return self.__openingDate

    @openingDate.setter
    def openingDate(self, openingDate: date):
        self.__openingDate = openingDate

    @property
    def closingDate(self) -> date:
        return self.__closingDate

    @closingDate.setter
    def closingDate(self, closingDate: date):
        self.__closingDate = closingDate

    @property
    def bank_Statement(self):
        return self.__bank_Statement

    @bank_Statement.setter
    def bank_Statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bank_Statement__bank_Statement", None)
        self.__bank_Statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bank_Account14"):
                opp_val = getattr(old_value, "bank_Account14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bank_Account14"):
                opp_val = getattr(value, "bank_Account14", None)
                if opp_val is None:
                    setattr(value, "bank_Account14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Statement17(self):
        return self.__Statement17

    @Statement17.setter
    def Statement17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bank_Statement__Statement17", None)
        self.__Statement17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "credits"):
                opp_val = getattr(old_value, "credits", None)
                if opp_val == self:
                    setattr(old_value, "credits", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "credits"):
                opp_val = getattr(value, "credits", None)
                setattr(value, "credits", self)

    @property
    def Statement(self):
        return self.__Statement

    @Statement.setter
    def Statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bank_Statement__Statement", None)
        self.__Statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "debits"):
                opp_val = getattr(old_value, "debits", None)
                if opp_val == self:
                    setattr(old_value, "debits", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "debits"):
                opp_val = getattr(value, "debits", None)
                setattr(value, "debits", self)

class bank_OnlineSession(TransactionInitiator):

    def __init__(self, internetAddress: str, start: date, end: date, bank_OnlineSession: "bank_Customer" = None):
        self.internetAddress = internetAddress
        self.start = start
        self.end = end
        self.bank_OnlineSession = bank_OnlineSession
        
    @property
    def start(self) -> date:
        return self.__start

    @start.setter
    def start(self, start: date):
        self.__start = start

    @property
    def internetAddress(self) -> str:
        return self.__internetAddress

    @internetAddress.setter
    def internetAddress(self, internetAddress: str):
        self.__internetAddress = internetAddress

    @property
    def end(self) -> date:
        return self.__end

    @end.setter
    def end(self, end: date):
        self.__end = end

    @property
    def bank_OnlineSession(self):
        return self.__bank_OnlineSession

    @bank_OnlineSession.setter
    def bank_OnlineSession(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bank_OnlineSession__bank_OnlineSession", None)
        self.__bank_OnlineSession = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bank_Customer12"):
                opp_val = getattr(old_value, "bank_Customer12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bank_Customer12"):
                opp_val = getattr(value, "bank_Customer12", None)
                if opp_val is None:
                    setattr(value, "bank_Customer12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bank_TransactionInitiator(ABC):

    pass
class bank_Transaction(ABC):

    def __init__(self, amount: str, date: date, comment: str, id: str, debits: "bank_Statement" = None, credits: "bank_Statement" = None, bank_Transaction: "bank_TransactionInitiator" = None):
        self.amount = amount
        self.date = date
        self.comment = comment
        self.id = id
        self.debits = debits
        self.credits = credits
        self.bank_Transaction = bank_Transaction
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def amount(self) -> str:
        return self.__amount

    @amount.setter
    def amount(self, amount: str):
        self.__amount = amount

    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def credits(self):
        return self.__credits

    @credits.setter
    def credits(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bank_Transaction__credits", None)
        self.__credits = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Statement17"):
                opp_val = getattr(old_value, "Statement17", None)
                if opp_val == self:
                    setattr(old_value, "Statement17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Statement17"):
                opp_val = getattr(value, "Statement17", None)
                setattr(value, "Statement17", self)

    @property
    def bank_Transaction(self):
        return self.__bank_Transaction

    @bank_Transaction.setter
    def bank_Transaction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bank_Transaction__bank_Transaction", None)
        self.__bank_Transaction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bank_TransactionInitiator"):
                opp_val = getattr(old_value, "bank_TransactionInitiator", None)
                if opp_val == self:
                    setattr(old_value, "bank_TransactionInitiator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bank_TransactionInitiator"):
                opp_val = getattr(value, "bank_TransactionInitiator", None)
                setattr(value, "bank_TransactionInitiator", self)

    @property
    def debits(self):
        return self.__debits

    @debits.setter
    def debits(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bank_Transaction__debits", None)
        self.__debits = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Statement"):
                opp_val = getattr(old_value, "Statement", None)
                if opp_val == self:
                    setattr(old_value, "Statement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Statement"):
                opp_val = getattr(value, "Statement", None)
                setattr(value, "Statement", self)

class bank_CustomerAccount(Account):

    pass
class bank_Account(ABC):

    def __init__(self, number: str, balance: str, description: str, periodStart: int, bank_Account: "bank_Bank" = None, bank_Account14: set["bank_Statement"] = None):
        self.number = number
        self.balance = balance
        self.description = description
        self.periodStart = periodStart
        self.bank_Account = bank_Account
        self.bank_Account14 = bank_Account14 if bank_Account14 is not None else set()
        
    @property
    def periodStart(self) -> int:
        return self.__periodStart

    @periodStart.setter
    def periodStart(self, periodStart: int):
        self.__periodStart = periodStart

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def balance(self) -> str:
        return self.__balance

    @balance.setter
    def balance(self, balance: str):
        self.__balance = balance

    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def bank_Account(self):
        return self.__bank_Account

    @bank_Account.setter
    def bank_Account(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bank_Account__bank_Account", None)
        self.__bank_Account = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bank_Bank5"):
                opp_val = getattr(old_value, "bank_Bank5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bank_Bank5"):
                opp_val = getattr(value, "bank_Bank5", None)
                if opp_val is None:
                    setattr(value, "bank_Bank5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bank_Account14(self):
        return self.__bank_Account14

    @bank_Account14.setter
    def bank_Account14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bank_Account__bank_Account14", None)
        self.__bank_Account14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bank_Statement"):
                    opp_val = getattr(item, "bank_Statement", None)
                    
                    if opp_val == self:
                        setattr(item, "bank_Statement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bank_Statement"):
                    opp_val = getattr(item, "bank_Statement", None)
                    
                    setattr(item, "bank_Statement", self)
                    

class bank_Product:

    def __init__(self, name: str, description: str, bank_Product: "bank_Bank" = None, bank_Product35: "bank_CustomerAccount" = None):
        self.name = name
        self.description = description
        self.bank_Product = bank_Product
        self.bank_Product35 = bank_Product35
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bank_Product(self):
        return self.__bank_Product

    @bank_Product.setter
    def bank_Product(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bank_Product__bank_Product", None)
        self.__bank_Product = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bank_Bank3"):
                opp_val = getattr(old_value, "bank_Bank3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bank_Bank3"):
                opp_val = getattr(value, "bank_Bank3", None)
                if opp_val is None:
                    setattr(value, "bank_Bank3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bank_Product35(self):
        return self.__bank_Product35

    @bank_Product35.setter
    def bank_Product35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bank_Product__bank_Product35", None)
        self.__bank_Product35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bank_CustomerAccount34"):
                opp_val = getattr(old_value, "bank_CustomerAccount34", None)
                if opp_val == self:
                    setattr(old_value, "bank_CustomerAccount34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bank_CustomerAccount34"):
                opp_val = getattr(value, "bank_CustomerAccount34", None)
                setattr(value, "bank_CustomerAccount34", self)

class Party:

    pass
class bank_Merchant(Party):

    pass
class bank_Banker(TransactionInitiator, Party):

    pass
class bank_Customer(Party):

    pass
class bank_Bank(Party):

    pass
class ContactMethod:

    pass
class bank_PostalAddress(ContactMethod):

    def __init__(self, country: str, stateProvince: str, city: str, postalCode: str, line1: str, line2: str, bank_PostalAddress: "bank_PointOfSale" = None):
        self.country = country
        self.stateProvince = stateProvince
        self.city = city
        self.postalCode = postalCode
        self.line1 = line1
        self.line2 = line2
        self.bank_PostalAddress = bank_PostalAddress
        
    @property
    def postalCode(self) -> str:
        return self.__postalCode

    @postalCode.setter
    def postalCode(self, postalCode: str):
        self.__postalCode = postalCode

    @property
    def country(self) -> str:
        return self.__country

    @country.setter
    def country(self, country: str):
        self.__country = country

    @property
    def line2(self) -> str:
        return self.__line2

    @line2.setter
    def line2(self, line2: str):
        self.__line2 = line2

    @property
    def stateProvince(self) -> str:
        return self.__stateProvince

    @stateProvince.setter
    def stateProvince(self, stateProvince: str):
        self.__stateProvince = stateProvince

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, city: str):
        self.__city = city

    @property
    def line1(self) -> str:
        return self.__line1

    @line1.setter
    def line1(self, line1: str):
        self.__line1 = line1

    @property
    def bank_PostalAddress(self):
        return self.__bank_PostalAddress

    @bank_PostalAddress.setter
    def bank_PostalAddress(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bank_PostalAddress__bank_PostalAddress", None)
        self.__bank_PostalAddress = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bank_PointOfSale22"):
                opp_val = getattr(old_value, "bank_PointOfSale22", None)
                if opp_val == self:
                    setattr(old_value, "bank_PointOfSale22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bank_PointOfSale22"):
                opp_val = getattr(value, "bank_PointOfSale22", None)
                setattr(value, "bank_PointOfSale22", self)

class bank_Phone(ContactMethod):

    def __init__(self, countryCode: int, areaCode: int, phoneNumber: int, extension: int):
        self.countryCode = countryCode
        self.areaCode = areaCode
        self.phoneNumber = phoneNumber
        self.extension = extension
        
    @property
    def countryCode(self) -> int:
        return self.__countryCode

    @countryCode.setter
    def countryCode(self, countryCode: int):
        self.__countryCode = countryCode

    @property
    def areaCode(self) -> int:
        return self.__areaCode

    @areaCode.setter
    def areaCode(self, areaCode: int):
        self.__areaCode = areaCode

    @property
    def extension(self) -> int:
        return self.__extension

    @extension.setter
    def extension(self, extension: int):
        self.__extension = extension

    @property
    def phoneNumber(self) -> int:
        return self.__phoneNumber

    @phoneNumber.setter
    def phoneNumber(self, phoneNumber: int):
        self.__phoneNumber = phoneNumber

class bank_WebAddress(ContactMethod):

    def __init__(self, url: str):
        self.url = url
        
    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

class bank_EMail(ContactMethod):

    def __init__(self, eMailAddress: str):
        self.eMailAddress = eMailAddress
        
    @property
    def eMailAddress(self) -> str:
        return self.__eMailAddress

    @eMailAddress.setter
    def eMailAddress(self, eMailAddress: str):
        self.__eMailAddress = eMailAddress

class bank_ContactMethod(ABC):

    def __init__(self, name: str, description: str, bank_ContactMethod: "bank_Party" = None):
        self.name = name
        self.description = description
        self.bank_ContactMethod = bank_ContactMethod
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def bank_ContactMethod(self):
        return self.__bank_ContactMethod

    @bank_ContactMethod.setter
    def bank_ContactMethod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bank_ContactMethod__bank_ContactMethod", None)
        self.__bank_ContactMethod = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bank_Party"):
                opp_val = getattr(old_value, "bank_Party", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bank_Party"):
                opp_val = getattr(value, "bank_Party", None)
                if opp_val is None:
                    setattr(value, "bank_Party", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class bank_Party(ABC):

    def __init__(self, name: str, bank_Party: set["bank_ContactMethod"] = None):
        self.name = name
        self.bank_Party = bank_Party if bank_Party is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bank_Party(self):
        return self.__bank_Party

    @bank_Party.setter
    def bank_Party(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bank_Party__bank_Party", None)
        self.__bank_Party = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bank_ContactMethod"):
                    opp_val = getattr(item, "bank_ContactMethod", None)
                    
                    if opp_val == self:
                        setattr(item, "bank_ContactMethod", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bank_ContactMethod"):
                    opp_val = getattr(item, "bank_ContactMethod", None)
                    
                    setattr(item, "bank_ContactMethod", self)
                    
