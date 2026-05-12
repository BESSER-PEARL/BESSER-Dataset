from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Employee_Actor:

    pass


class Administrator_Actor:

    pass


class Salary_Management_UseCase:

    pass


class Authentication_UseCase:

    pass





class Employee_Management_System_Component:

    pass


class History:

    def __init__(self, Code_id: str, Code_amount: str):
        self.Code_id = Code_id
        self.Code_amount = Code_amount
        
        pass
    @property
    def Code_id(self):
        return self.__Code_id
    @Code_id.setter
    def Code_id(self, Code_id: str):
        self.__Code_id = Code_id

    @property
    def Code_amount(self):
        return self.__Code_amount
    @Code_amount.setter
    def Code_amount(self, Code_amount: str):
        self.__Code_amount = Code_amount



class Error_code:

    def __init__(self, Code_Id: str, Code_serial: str, Code_Exp: str):
        self.Code_Id = Code_Id
        self.Code_serial = Code_serial
        self.Code_Exp = Code_Exp
        
        pass
    @property
    def Code_Exp(self):
        return self.__Code_Exp
    @Code_Exp.setter
    def Code_Exp(self, Code_Exp: str):
        self.__Code_Exp = Code_Exp

    @property
    def Code_serial(self):
        return self.__Code_serial
    @Code_serial.setter
    def Code_serial(self, Code_serial: str):
        self.__Code_serial = Code_serial

    @property
    def Code_Id(self):
        return self.__Code_Id
    @Code_Id.setter
    def Code_Id(self, Code_Id: str):
        self.__Code_Id = Code_Id



class Scanner:

    def __init__(self, code_Id: int, code_serial: str, code_serial1: str, code_MOB: date, Code_EOD: date, Code_amount: float):
        self.code_Id = code_Id
        self.code_serial = code_serial
        self.code_serial1 = code_serial1
        self.code_MOB = code_MOB
        self.Code_EOD = Code_EOD
        self.Code_amount = Code_amount
        
        pass
    @property
    def Code_EOD(self):
        return self.__Code_EOD
    @Code_EOD.setter
    def Code_EOD(self, Code_EOD: date):
        self.__Code_EOD = Code_EOD

    @property
    def code_Id(self):
        return self.__code_Id
    @code_Id.setter
    def code_Id(self, code_Id: int):
        self.__code_Id = code_Id

    @property
    def Code_amount(self):
        return self.__Code_amount
    @Code_amount.setter
    def Code_amount(self, Code_amount: float):
        self.__Code_amount = Code_amount

    @property
    def code_serial1(self):
        return self.__code_serial1
    @code_serial1.setter
    def code_serial1(self, code_serial1: str):
        self.__code_serial1 = code_serial1

    @property
    def code_MOB(self):
        return self.__code_MOB
    @code_MOB.setter
    def code_MOB(self, code_MOB: date):
        self.__code_MOB = code_MOB

    @property
    def code_serial(self):
        return self.__code_serial
    @code_serial.setter
    def code_serial(self, code_serial: str):
        self.__code_serial = code_serial



class Logout_external:

    pass


class Login_external:

    pass
