from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Size(Enum):
    pass
class CardType(Enum):
    pass

############################################
# Definition of Classes
############################################










class Management_Director:

    def __init__(self, budget: float, directortest6: "Management_DirectorTest" = None):
        self.budget = budget
        self.directortest6 = directortest6
        
        pass
    @property
    def budget(self):
        return self.__budget
    @budget.setter
    def budget(self, budget: float):
        self.__budget = budget

    @property
    def directortest6(self):
        return self.__directortest6
    @directortest6.setter
    def directortest6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Management_Director__directortest6", None)
        self.__directortest6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "director7"):
                opp_val = getattr(old_value, "director7", None)
                if opp_val == self:
                    setattr(old_value, "director7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "director7"):
                opp_val = getattr(value, "director7", None)
                setattr(value, "director7", self)



class GiftCard:

    def __init__(self, cardType: CardType, isPresent: bool):
        self.cardType = cardType
        self.isPresent = isPresent
        
        pass
    @property
    def isPresent(self):
        return self.__isPresent
    @isPresent.setter
    def isPresent(self, isPresent: bool):
        self.__isPresent = isPresent

    @property
    def cardType(self):
        return self.__cardType
    @cardType.setter
    def cardType(self, cardType: CardType):
        self.__cardType = cardType



class Ticket:

    def __init__(self, eventCity: str, eventCountry: str, isLastMinute: bool):
        self.eventCity = eventCity
        self.eventCountry = eventCountry
        self.isLastMinute = isLastMinute
        
        pass
    @property
    def isLastMinute(self):
        return self.__isLastMinute
    @isLastMinute.setter
    def isLastMinute(self, isLastMinute: bool):
        self.__isLastMinute = isLastMinute

    @property
    def eventCity(self):
        return self.__eventCity
    @eventCity.setter
    def eventCity(self, eventCity: str):
        self.__eventCity = eventCity

    @property
    def eventCountry(self):
        return self.__eventCountry
    @eventCountry.setter
    def eventCountry(self, eventCountry: str):
        self.__eventCountry = eventCountry



class Fashion:

    def __init__(self, size: Size, category: str, increaseBy: int):
        self.size = size
        self.category = category
        self.increaseBy = increaseBy
        
        pass
    @property
    def increaseBy(self):
        return self.__increaseBy
    @increaseBy.setter
    def increaseBy(self, increaseBy: int):
        self.__increaseBy = increaseBy

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, size: Size):
        self.__size = size

    @property
    def category(self):
        return self.__category
    @category.setter
    def category(self, category: str):
        self.__category = category



class Taxi:

    def __init__(self, isVip: bool):
        self.isVip = isVip
        
        pass
    @property
    def isVip(self):
        return self.__isVip
    @isVip.setter
    def isVip(self, isVip: bool):
        self.__isVip = isVip



class Travel:

    pass


class Flight:

    def __init__(self, hasConnection: bool):
        self.hasConnection = hasConnection
        
        pass
    @property
    def hasConnection(self):
        return self.__hasConnection
    @hasConnection.setter
    def hasConnection(self, hasConnection: bool):
        self.__hasConnection = hasConnection



class TransportationProduct:

    def __init__(self, destination: str, source: str, distance: float):
        self.destination = destination
        self.source = source
        self.distance = distance
        
        pass
    @property
    def source(self):
        return self.__source
    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def distance(self):
        return self.__distance
    @distance.setter
    def distance(self, distance: float):
        self.__distance = distance

    @property
    def destination(self):
        return self.__destination
    @destination.setter
    def destination(self, destination: str):
        self.__destination = destination



class Product:

    def __init__(self, title: str, creationDate: date, price: float, supportDiscount: bool):
        self.title = title
        self.creationDate = creationDate
        self.price = price
        self.supportDiscount = supportDiscount
        
        pass
    @property
    def creationDate(self):
        return self.__creationDate
    @creationDate.setter
    def creationDate(self, creationDate: date):
        self.__creationDate = creationDate

    @property
    def supportDiscount(self):
        return self.__supportDiscount
    @supportDiscount.setter
    def supportDiscount(self, supportDiscount: bool):
        self.__supportDiscount = supportDiscount

    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: float):
        self.__price = price



class Class:

    pass


class techStaff_DeveloperTest:

    pass


class techStaff_DatabaseAdminTest:

    pass


class techStaff_Developer:

    pass


class techStaff_DatabaseAdmin:

    pass


class Staff_Employee(ABC):

    def __init__(self, name: str, nationalInsurance: str, salary: float):
        self.name = name
        self.nationalInsurance = nationalInsurance
        self.salary = salary
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def nationalInsurance(self):
        return self.__nationalInsurance
    @nationalInsurance.setter
    def nationalInsurance(self, nationalInsurance: str):
        self.__nationalInsurance = nationalInsurance

    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, salary: float):
        self.__salary = salary



class Management_ManagerTest:

    pass


class Management_DirectorTest:

    pass


class Management_Manager:

    def __init__(self, deptName: str, managertest4: "Management_ManagerTest" = None):
        self.deptName = deptName
        self.managertest4 = managertest4
        
        pass
    @property
    def deptName(self):
        return self.__deptName
    @deptName.setter
    def deptName(self, deptName: str):
        self.__deptName = deptName

    @property
    def managertest4(self):
        return self.__managertest4
    @managertest4.setter
    def managertest4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Management_Manager__managertest4", None)
        self.__managertest4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "manager5"):
                opp_val = getattr(old_value, "manager5", None)
                if opp_val == self:
                    setattr(old_value, "manager5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "manager5"):
                opp_val = getattr(value, "manager5", None)
                setattr(value, "manager5", self)

