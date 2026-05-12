from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class NuRightAnswer(Enum):
    pass
class OtherAnswer(Enum):
    pass

############################################
# Definition of Classes
############################################










class NumericAnswers:

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        
        pass
    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name



class MCRightAnswer:

    def __init__(self, quantity: int, price: float):
        self.quantity = quantity
        self.price = price
        
        pass
    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: float):
        self.__price = price



class MultipleChoicesAnswers:

    def __init__(self, number: int, ordered: date, shipped: bool, shipTo: str, total: float, status: OtherAnswer):
        self.number = number
        self.ordered = ordered
        self.shipped = shipped
        self.shipTo = shipTo
        self.total = total
        self.status = status
        
        pass
    @property
    def ordered(self):
        return self.__ordered
    @ordered.setter
    def ordered(self, ordered: date):
        self.__ordered = ordered

    @property
    def total(self):
        return self.__total
    @total.setter
    def total(self, total: float):
        self.__total = total

    @property
    def shipTo(self):
        return self.__shipTo
    @shipTo.setter
    def shipTo(self, shipTo: str):
        self.__shipTo = shipTo

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: OtherAnswer):
        self.__status = status

    @property
    def number(self):
        return self.__number
    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def shipped(self):
        return self.__shipped
    @shipped.setter
    def shipped(self, shipped: bool):
        self.__shipped = shipped



class AnswerdBuilder:

    def __init__(self, login: str, password: str, state: NuRightAnswer, customer0: "ConcreteRightAnswers" = None, account2: "ConcreteOtherAnswers" = None):
        self.login = login
        self.password = password
        self.state = state
        self.customer0 = customer0
        self.account2 = account2
        
        pass
    @property
    def state(self):
        return self.__state
    @state.setter
    def state(self, state: NuRightAnswer):
        self.__state = state

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def login(self):
        return self.__login
    @login.setter
    def login(self, login: str):
        self.__login = login

    @property
    def account2(self):
        return self.__account2
    @account2.setter
    def account2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AnswerdBuilder__account2", None)
        self.__account2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer3"):
                opp_val = getattr(old_value, "customer3", None)
                if opp_val == self:
                    setattr(old_value, "customer3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer3"):
                opp_val = getattr(value, "customer3", None)
                setattr(value, "customer3", self)

    @property
    def customer0(self):
        return self.__customer0
    @customer0.setter
    def customer0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AnswerdBuilder__customer0", None)
        self.__customer0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "webUser1"):
                opp_val = getattr(old_value, "webUser1", None)
                if opp_val == self:
                    setattr(old_value, "webUser1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "webUser1"):
                opp_val = getattr(value, "webUser1", None)
                setattr(value, "webUser1", self)



class ConcreteOtherAnswers:

    def __init__(self, billingAddress: str, open: date, closed: date, isClosed: bool, customer3: "AnswerdBuilder" = None):
        self.billingAddress = billingAddress
        self.open = open
        self.closed = closed
        self.isClosed = isClosed
        self.customer3 = customer3
        
        pass
    @property
    def closed(self):
        return self.__closed
    @closed.setter
    def closed(self, closed: date):
        self.__closed = closed

    @property
    def isClosed(self):
        return self.__isClosed
    @isClosed.setter
    def isClosed(self, isClosed: bool):
        self.__isClosed = isClosed

    @property
    def open(self):
        return self.__open
    @open.setter
    def open(self, open: date):
        self.__open = open

    @property
    def billingAddress(self):
        return self.__billingAddress
    @billingAddress.setter
    def billingAddress(self, billingAddress: str):
        self.__billingAddress = billingAddress

    @property
    def customer3(self):
        return self.__customer3
    @customer3.setter
    def customer3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ConcreteOtherAnswers__customer3", None)
        self.__customer3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "account2"):
                opp_val = getattr(old_value, "account2", None)
                if opp_val == self:
                    setattr(old_value, "account2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "account2"):
                opp_val = getattr(value, "account2", None)
                setattr(value, "account2", self)



class Choices:

    def __init__(self, creationDate: date):
        self.creationDate = creationDate
        
        pass
    @property
    def creationDate(self):
        return self.__creationDate
    @creationDate.setter
    def creationDate(self, creationDate: date):
        self.__creationDate = creationDate



class Answers:

    def __init__(self, paidDate: date, total: float, details: str):
        self.paidDate = paidDate
        self.total = total
        self.details = details
        
        pass
    @property
    def total(self):
        return self.__total
    @total.setter
    def total(self, total: float):
        self.__total = total

    @property
    def paidDate(self):
        return self.__paidDate
    @paidDate.setter
    def paidDate(self, paidDate: date):
        self.__paidDate = paidDate

    @property
    def details(self):
        return self.__details
    @details.setter
    def details(self, details: str):
        self.__details = details



class ConcreteRightAnswers:

    def __init__(self, address: str, phone: str, email: str, webUser1: "AnswerdBuilder" = None):
        self.address = address
        self.phone = phone
        self.email = email
        self.webUser1 = webUser1
        
        pass
    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def webUser1(self):
        return self.__webUser1
    @webUser1.setter
    def webUser1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ConcreteRightAnswers__webUser1", None)
        self.__webUser1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer0"):
                opp_val = getattr(old_value, "customer0", None)
                if opp_val == self:
                    setattr(old_value, "customer0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer0"):
                opp_val = getattr(value, "customer0", None)
                setattr(value, "customer0", self)

