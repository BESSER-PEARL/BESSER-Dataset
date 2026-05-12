from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class HouseKeeping_Actor:

    pass


class Chef_Actor:

    pass


class Receptionist_Actor:

    pass


class Hotel_Guest_Actor:

    pass


class Room_Cleaning_UseCase:

    pass


class Menu_Preparation_UseCase:

    pass


class Food_Serving_UseCase:

    pass


class Check_Out_UseCase:

    pass


class Check_In_UseCase:

    pass


class Cancel_Reservation_UseCase:

    pass


class Book_Room_UseCase:

    pass


class Search_Avalibility_UseCase:

    pass





class Customer:

    pass


class Inventory:

    def __init__(self, Type: str, Status: str):
        self.Type = Type
        self.Status = Status
        
        pass
    @property
    def Type(self):
        return self.__Type
    @Type.setter
    def Type(self, Type: str):
        self.__Type = Type

    @property
    def Status(self):
        return self.__Status
    @Status.setter
    def Status(self, Status: str):
        self.__Status = Status



class Manager:

    def __init__(self, Name: str, Id: int, Phone_No: int):
        self.Name = Name
        self.Id = Id
        self.Phone_No = Phone_No
        
        pass
    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: int):
        self.__Id = Id

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Phone_No(self):
        return self.__Phone_No
    @Phone_No.setter
    def Phone_No(self, Phone_No: int):
        self.__Phone_No = Phone_No

