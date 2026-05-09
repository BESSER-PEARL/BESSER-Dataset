from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class PaymentType(Enum):
    CASH = "CASH"
    CHEQUE = "CHEQUE"
    ELECTRONIC = "ELECTRONIC"


############################################
# Definition of Classes
############################################

class Payment:

    pass
class shop_CashPayment(Payment):

    pass
class shop_ElectronicPayment(Payment):

    pass
class shop_ChequePayment(Payment):

    def __init__(self, deposited: bool, depositDate: date):
        self.deposited = deposited
        self.depositDate = depositDate
        
        pass
    @property
    def deposited(self):
        return self.__deposited

    @deposited.setter
    def deposited(self, deposited: bool):
        self.__deposited = deposited


    @property
    def depositDate(self):
        return self.__depositDate

    @depositDate.setter
    def depositDate(self, depositDate: date):
        self.__depositDate = depositDate


class shop_Valuable(ABC):

    def __init__(self, date: date, value: float):
        self.date = date
        self.value = value
        
        pass
    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value


class shop_Person(ABC):

    def __init__(self, firstName: str, lastName: str, birthDate: date, phoneNumbers: str, address: str, emails: str):
        self.firstName = firstName
        self.lastName = lastName
        self.birthDate = birthDate
        self.phoneNumbers = phoneNumbers
        self.address = address
        self.emails = emails
        
        pass
    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address


    @property
    def emails(self):
        return self.__emails

    @emails.setter
    def emails(self, emails: str):
        self.__emails = emails


    @property
    def birthDate(self):
        return self.__birthDate

    @birthDate.setter
    def birthDate(self, birthDate: date):
        self.__birthDate = birthDate


    @property
    def phoneNumbers(self):
        return self.__phoneNumbers

    @phoneNumbers.setter
    def phoneNumbers(self, phoneNumbers: str):
        self.__phoneNumbers = phoneNumbers


    @property
    def firstName(self):
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName


    @property
    def lastName(self):
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName


    def getDisplayName(self) :
        # TODO: Implement getDisplayName method
        pass

class Valuable:

    pass
class shop_BankOperation(Valuable):

    def __init__(self, description: str, shop_BankOperation: "shop_AccountBook" = None):
        self.description = description
        self.shop_BankOperation = shop_BankOperation
        
        pass
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def shop_BankOperation(self):
        return self.__shop_BankOperation

    @shop_BankOperation.setter
    def shop_BankOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shop_BankOperation__shop_BankOperation", None)
        self.__shop_BankOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shop_AccountBook"):
                opp_val = getattr(old_value, "shop_AccountBook", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shop_AccountBook"):
                opp_val = getattr(value, "shop_AccountBook", None)
                if opp_val is None:
                    setattr(value, "shop_AccountBook", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class shop_Payment(Valuable):

    def __init__(self, type: str, Payment: "shop_Sale" = None, payments: "shop_Sale" = None, shop_Payment: "shop_AccountBook" = None):
        self.type = type
        self.Payment = Payment
        self.payments = payments
        self.shop_Payment = shop_Payment
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def payments(self):
        return self.__payments

    @payments.setter
    def payments(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shop_Payment__payments", None)
        self.__payments = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Sale14"):
                opp_val = getattr(old_value, "Sale14", None)
                if opp_val == self:
                    setattr(old_value, "Sale14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Sale14"):
                opp_val = getattr(value, "Sale14", None)
                setattr(value, "Sale14", self)

    @property
    def shop_Payment(self):
        return self.__shop_Payment

    @shop_Payment.setter
    def shop_Payment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shop_Payment__shop_Payment", None)
        self.__shop_Payment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shop_AccountBook18"):
                opp_val = getattr(old_value, "shop_AccountBook18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shop_AccountBook18"):
                opp_val = getattr(value, "shop_AccountBook18", None)
                if opp_val is None:
                    setattr(value, "shop_AccountBook18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Payment(self):
        return self.__Payment

    @Payment.setter
    def Payment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shop_Payment__Payment", None)
        self.__Payment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sale"):
                opp_val = getattr(old_value, "sale", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sale"):
                opp_val = getattr(value, "sale", None)
                if opp_val is None:
                    setattr(value, "sale", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class shop_AccountBook:

    def __init__(self, cashFlow: float, AccountBook: "shop_Shop" = None, shop_AccountBook: set["shop_BankOperation"] = None, accountBook: "shop_Shop" = None, shop_AccountBook18: set["shop_Payment"] = None):
        self.cashFlow = cashFlow
        self.AccountBook = AccountBook
        self.shop_AccountBook = shop_AccountBook if shop_AccountBook is not None else set()
        self.accountBook = accountBook
        self.shop_AccountBook18 = shop_AccountBook18 if shop_AccountBook18 is not None else set()
        
        pass
    @property
    def cashFlow(self):
        return self.__cashFlow

    @cashFlow.setter
    def cashFlow(self, cashFlow: float):
        self.__cashFlow = cashFlow


    @property
    def shop_AccountBook18(self):
        return self.__shop_AccountBook18

    @shop_AccountBook18.setter
    def shop_AccountBook18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shop_AccountBook__shop_AccountBook18", None)
        self.__shop_AccountBook18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shop_Payment"):
                    opp_val = getattr(item, "shop_Payment", None)
                    
                    if opp_val == self:
                        setattr(item, "shop_Payment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shop_Payment"):
                    opp_val = getattr(item, "shop_Payment", None)
                    
                    setattr(item, "shop_Payment", self)
                    

    @property
    def shop_AccountBook(self):
        return self.__shop_AccountBook

    @shop_AccountBook.setter
    def shop_AccountBook(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shop_AccountBook__shop_AccountBook", None)
        self.__shop_AccountBook = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "shop_BankOperation"):
                    opp_val = getattr(item, "shop_BankOperation", None)
                    
                    if opp_val == self:
                        setattr(item, "shop_BankOperation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "shop_BankOperation"):
                    opp_val = getattr(item, "shop_BankOperation", None)
                    
                    setattr(item, "shop_BankOperation", self)
                    

    @property
    def accountBook(self):
        return self.__accountBook

    @accountBook.setter
    def accountBook(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shop_AccountBook__accountBook", None)
        self.__accountBook = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Shop"):
                opp_val = getattr(old_value, "Shop", None)
                if opp_val == self:
                    setattr(old_value, "Shop", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Shop"):
                opp_val = getattr(value, "Shop", None)
                setattr(value, "Shop", self)

    @property
    def AccountBook(self):
        return self.__AccountBook

    @AccountBook.setter
    def AccountBook(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shop_AccountBook__AccountBook", None)
        self.__AccountBook = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shop"):
                opp_val = getattr(old_value, "shop", None)
                if opp_val == self:
                    setattr(old_value, "shop", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shop"):
                opp_val = getattr(value, "shop", None)
                setattr(value, "shop", self)

    def depositCheques(self, shop_date, shop_cheques):
        # TODO: Implement depositCheques method
        pass

    def depositCash(self, shop_cashValue, shop_date):
        # TODO: Implement depositCash method
        pass

class shop_Sale(Valuable):

    def __init__(self, description: str, sales: "shop_Customer" = None, sales9: set["shop_Employee"] = None, sale: set["shop_Payment"] = None, Sale12: "shop_Employee" = None, Sale14: "shop_Payment" = None, Sale: "shop_Customer" = None, shop_Sale: "shop_Shop" = None):
        self.description = description
        self.sales = sales
        self.sales9 = sales9 if sales9 is not None else set()
        self.sale = sale if sale is not None else set()
        self.Sale12 = Sale12
        self.Sale14 = Sale14
        self.Sale = Sale
        self.shop_Sale = shop_Sale
        
        pass
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def Sale(self):
        return self.__Sale

    @Sale.setter
    def Sale(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shop_Sale__Sale", None)
        self.__Sale = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer"):
                opp_val = getattr(old_value, "customer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer"):
                opp_val = getattr(value, "customer", None)
                if opp_val is None:
                    setattr(value, "customer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Sale14(self):
        return self.__Sale14

    @Sale14.setter
    def Sale14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shop_Sale__Sale14", None)
        self.__Sale14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "payments"):
                opp_val = getattr(old_value, "payments", None)
                if opp_val == self:
                    setattr(old_value, "payments", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "payments"):
                opp_val = getattr(value, "payments", None)
                setattr(value, "payments", self)

    @property
    def sale(self):
        return self.__sale

    @sale.setter
    def sale(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shop_Sale__sale", None)
        self.__sale = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Payment"):
                    opp_val = getattr(item, "Payment", None)
                    
                    if opp_val == self:
                        setattr(item, "Payment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Payment"):
                    opp_val = getattr(item, "Payment", None)
                    
                    setattr(item, "Payment", self)
                    

    @property
    def sales9(self):
        return self.__sales9

    @sales9.setter
    def sales9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shop_Sale__sales9", None)
        self.__sales9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Employee"):
                    opp_val = getattr(item, "Employee", None)
                    
                    if opp_val == self:
                        setattr(item, "Employee", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Employee"):
                    opp_val = getattr(item, "Employee", None)
                    
                    setattr(item, "Employee", self)
                    

    @property
    def sales(self):
        return self.__sales

    @sales.setter
    def sales(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shop_Sale__sales", None)
        self.__sales = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Customer"):
                opp_val = getattr(old_value, "Customer", None)
                if opp_val == self:
                    setattr(old_value, "Customer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Customer"):
                opp_val = getattr(value, "Customer", None)
                setattr(value, "Customer", self)

    @property
    def shop_Sale(self):
        return self.__shop_Sale

    @shop_Sale.setter
    def shop_Sale(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shop_Sale__shop_Sale", None)
        self.__shop_Sale = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "shop_Shop2"):
                opp_val = getattr(old_value, "shop_Shop2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "shop_Shop2"):
                opp_val = getattr(value, "shop_Shop2", None)
                if opp_val is None:
                    setattr(value, "shop_Shop2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Sale12(self):
        return self.__Sale12

    @Sale12.setter
    def Sale12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_shop_Sale__Sale12", None)
        self.__Sale12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employees"):
                opp_val = getattr(old_value, "employees", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employees"):
                opp_val = getattr(value, "employees", None)
                if opp_val is None:
                    setattr(value, "employees", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class shop_Shop:

    pass
class Person:

    pass
class shop_Employee(Person):

    pass
class shop_Customer(Person):

    pass