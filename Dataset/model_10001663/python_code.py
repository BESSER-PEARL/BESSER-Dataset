from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










class Invoice:

    def __init__(self, num: str, product: str, quantity: int, amount: float):
        self.num = num
        self.product = product
        self.quantity = quantity
        self.amount = amount
        
        pass
    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: float):
        self.__amount = amount

    @property
    def num(self):
        return self.__num
    @num.setter
    def num(self, num: str):
        self.__num = num

    @property
    def product(self):
        return self.__product
    @product.setter
    def product(self, product: str):
        self.__product = product



class SalariedEmployee:

    def __init__(self, salary: float):
        self.salary = salary
        
        pass
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, salary: float):
        self.__salary = salary



class Payable_Interface:

    pass


class Employee(ABC):

    def __init__(self, firstname: str, lastname: str, ssn: str):
        self.firstname = firstname
        self.lastname = lastname
        self.ssn = ssn
        
        pass
    @property
    def firstname(self):
        return self.__firstname
    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname

    @property
    def ssn(self):
        return self.__ssn
    @ssn.setter
    def ssn(self, ssn: str):
        self.__ssn = ssn

    @property
    def lastname(self):
        return self.__lastname
    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname

