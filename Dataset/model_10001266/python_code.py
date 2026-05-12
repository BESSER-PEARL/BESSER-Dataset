from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Discription:

    def __init__(self, Emil: str, Discription: str):
        self.Emil = Emil
        self.Discription = Discription
        
        pass
    @property
    def Emil(self):
        return self.__Emil
    @Emil.setter
    def Emil(self, Emil: str):
        self.__Emil = Emil

    @property
    def Discription(self):
        return self.__Discription
    @Discription.setter
    def Discription(self, Discription: str):
        self.__Discription = Discription



class Payment:

    def __init__(self, Amount: int, Date_off: str):
        self.Amount = Amount
        self.Date_off = Date_off
        
        pass
    @property
    def Amount(self):
        return self.__Amount
    @Amount.setter
    def Amount(self, Amount: int):
        self.__Amount = Amount

    @property
    def Date_off(self):
        return self.__Date_off
    @Date_off.setter
    def Date_off(self, Date_off: str):
        self.__Date_off = Date_off



class User:

    def __init__(self, Name_: str, Address_: str, Phone_number: int, Email_: str, Phone_number1: int):
        self.Name_ = Name_
        self.Address_ = Address_
        self.Phone_number = Phone_number
        self.Email_ = Email_
        self.Phone_number1 = Phone_number1
        
        pass
    @property
    def Email_(self):
        return self.__Email_
    @Email_.setter
    def Email_(self, Email_: str):
        self.__Email_ = Email_

    @property
    def Name_(self):
        return self.__Name_
    @Name_.setter
    def Name_(self, Name_: str):
        self.__Name_ = Name_

    @property
    def Address_(self):
        return self.__Address_
    @Address_.setter
    def Address_(self, Address_: str):
        self.__Address_ = Address_

    @property
    def Phone_number1(self):
        return self.__Phone_number1
    @Phone_number1.setter
    def Phone_number1(self, Phone_number1: int):
        self.__Phone_number1 = Phone_number1

    @property
    def Phone_number(self):
        return self.__Phone_number
    @Phone_number.setter
    def Phone_number(self, Phone_number: int):
        self.__Phone_number = Phone_number



class Delivery:

    def __init__(self, Date: str, Name: str, Type: str):
        self.Date = Date
        self.Name = Name
        self.Type = Type
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Date(self):
        return self.__Date
    @Date.setter
    def Date(self, Date: str):
        self.__Date = Date

    @property
    def Type(self):
        return self.__Type
    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type



class Order:

    def __init__(self, ID_: int, Type_: str, Size_: int, Quantity: int):
        self.ID_ = ID_
        self.Type_ = Type_
        self.Size_ = Size_
        self.Quantity = Quantity
        
        pass
    @property
    def ID_(self):
        return self.__ID_
    @ID_.setter
    def ID_(self, ID_: int):
        self.__ID_ = ID_

    @property
    def Size_(self):
        return self.__Size_
    @Size_.setter
    def Size_(self, Size_: int):
        self.__Size_ = Size_

    @property
    def Type_(self):
        return self.__Type_
    @Type_.setter
    def Type_(self, Type_: str):
        self.__Type_ = Type_

    @property
    def Quantity(self):
        return self.__Quantity
    @Quantity.setter
    def Quantity(self, Quantity: int):
        self.__Quantity = Quantity

