from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class CustomerType(Enum):
    pass

############################################
# Definition of Classes
############################################







class Send_for_Repair_UseCase:

    pass


class Purchase_Car_UseCase:

    pass


class Enquire_for_Cars_UseCase:

    pass


class Customer_Actor:

    pass


class Manufacturer_Actor:

    pass


class Order_Cars_UseCase:

    pass


class Compute_Billables_UseCase:

    pass


class Check_Car_Stock_UseCase:

    pass


class Check_for_Parts_UseCase:

    pass


class Repair_Part_Purchase_UseCase:

    pass


class Maintenance_Team_Actor:

    pass


class Dealer_Actor:

    pass





class Repair:

    def __init__(self, car: Car, customer: Customer, part: RepairPart, date: date):
        self.car = car
        self.customer = customer
        self.part = part
        self.date = date
        
        pass
    @property
    def customer(self):
        return self.__customer
    @customer.setter
    def customer(self, customer: Customer):
        self.__customer = customer

    @property
    def car(self):
        return self.__car
    @car.setter
    def car(self, car: Car):
        self.__car = car

    @property
    def part(self):
        return self.__part
    @part.setter
    def part(self, part: RepairPart):
        self.__part = part

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: date):
        self.__date = date



class RepairPart:

    def __init__(self, name: str, cost: str, stock: int):
        self.name = name
        self.cost = cost
        self.stock = stock
        
        pass
    @property
    def cost(self):
        return self.__cost
    @cost.setter
    def cost(self, cost: str):
        self.__cost = cost

    @property
    def stock(self):
        return self.__stock
    @stock.setter
    def stock(self, stock: int):
        self.__stock = stock

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name



class Sale:

    def __init__(self, date: date, customer: Customer, car: Car, billable: str):
        self.date = date
        self.customer = customer
        self.car = car
        self.billable = billable
        
        pass
    @property
    def car(self):
        return self.__car
    @car.setter
    def car(self, car: Car):
        self.__car = car

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def customer(self):
        return self.__customer
    @customer.setter
    def customer(self, customer: Customer):
        self.__customer = customer

    @property
    def billable(self):
        return self.__billable
    @billable.setter
    def billable(self, billable: str):
        self.__billable = billable



class Car:

    def __init__(self, name: str, manufacturer: str, stock: int, cost: str):
        self.name = name
        self.manufacturer = manufacturer
        self.stock = stock
        self.cost = cost
        
        pass
    @property
    def manufacturer(self):
        return self.__manufacturer
    @manufacturer.setter
    def manufacturer(self, manufacturer: str):
        self.__manufacturer = manufacturer

    @property
    def cost(self):
        return self.__cost
    @cost.setter
    def cost(self, cost: str):
        self.__cost = cost

    @property
    def stock(self):
        return self.__stock
    @stock.setter
    def stock(self, stock: int):
        self.__stock = stock

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name



class ConnectionInterface_Interface:

    pass


class ActiveRecord:

    def __init__(self, connection: ConnectionInterface_Interface, id: int):
        self.connection = connection
        self.id = id
        
        pass
    @property
    def connection(self):
        return self.__connection
    @connection.setter
    def connection(self, connection: ConnectionInterface_Interface):
        self.__connection = connection

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id



class Customer:

    def __init__(self, name: str, address: str, type: CustomerType):
        self.name = name
        self.address = address
        self.type = type
        
        pass
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: CustomerType):
        self.__type = type

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

