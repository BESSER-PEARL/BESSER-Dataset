from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Railway_website_Actor:

    pass


class Clerk_Actor:

    pass


class Refund_money_UseCase:

    pass


class Cancel_ticket_UseCase:

    pass


class Fill_the_details_UseCase:

    pass


class Book_ticket_UseCase:

    pass


class Pay_fare_amount_UseCase:

    pass


class Check_ticket_availability_UseCase:

    pass


class Traveler_Actor:

    pass





class Pessanger:

    def __init__(self, AadharNo: int, Children: int):
        self.AadharNo = AadharNo
        self.Children = Children
        
        pass
    @property
    def Children(self):
        return self.__Children
    @Children.setter
    def Children(self, Children: int):
        self.__Children = Children

    @property
    def AadharNo(self):
        return self.__AadharNo
    @AadharNo.setter
    def AadharNo(self, AadharNo: int):
        self.__AadharNo = AadharNo



class Information_Interface:

    pass


class Express1:

    def __init__(self, SecondSitting: str):
        self.SecondSitting = SecondSitting
        
        pass
    @property
    def SecondSitting(self):
        return self.__SecondSitting
    @SecondSitting.setter
    def SecondSitting(self, SecondSitting: str):
        self.__SecondSitting = SecondSitting



class SuperFast1:

    def __init__(self, AC_1: str, AC_2: str, AC_3: str, Sleeper: str, Ladies: str, Handicamp: str):
        self.AC_1 = AC_1
        self.AC_2 = AC_2
        self.AC_3 = AC_3
        self.Sleeper = Sleeper
        self.Ladies = Ladies
        self.Handicamp = Handicamp
        
        pass
    @property
    def AC_1(self):
        return self.__AC_1
    @AC_1.setter
    def AC_1(self, AC_1: str):
        self.__AC_1 = AC_1

    @property
    def Sleeper(self):
        return self.__Sleeper
    @Sleeper.setter
    def Sleeper(self, Sleeper: str):
        self.__Sleeper = Sleeper

    @property
    def AC_2(self):
        return self.__AC_2
    @AC_2.setter
    def AC_2(self, AC_2: str):
        self.__AC_2 = AC_2

    @property
    def Handicamp(self):
        return self.__Handicamp
    @Handicamp.setter
    def Handicamp(self, Handicamp: str):
        self.__Handicamp = Handicamp

    @property
    def Ladies(self):
        return self.__Ladies
    @Ladies.setter
    def Ladies(self, Ladies: str):
        self.__Ladies = Ladies

    @property
    def AC_3(self):
        return self.__AC_3
    @AC_3.setter
    def AC_3(self, AC_3: str):
        self.__AC_3 = AC_3



class Express:

    def __init__(self, SecondSitting: str, General: str):
        self.SecondSitting = SecondSitting
        self.General = General
        
        pass
    @property
    def SecondSitting(self):
        return self.__SecondSitting
    @SecondSitting.setter
    def SecondSitting(self, SecondSitting: str):
        self.__SecondSitting = SecondSitting

    @property
    def General(self):
        return self.__General
    @General.setter
    def General(self, General: str):
        self.__General = General



class SuperFast:

    def __init__(self, AC_1: str, AC_2: str, AC_3: str, Sleeper: str):
        self.AC_1 = AC_1
        self.AC_2 = AC_2
        self.AC_3 = AC_3
        self.Sleeper = Sleeper
        
        pass
    @property
    def AC_1(self):
        return self.__AC_1
    @AC_1.setter
    def AC_1(self, AC_1: str):
        self.__AC_1 = AC_1

    @property
    def AC_2(self):
        return self.__AC_2
    @AC_2.setter
    def AC_2(self, AC_2: str):
        self.__AC_2 = AC_2

    @property
    def Sleeper(self):
        return self.__Sleeper
    @Sleeper.setter
    def Sleeper(self, Sleeper: str):
        self.__Sleeper = Sleeper

    @property
    def AC_3(self):
        return self.__AC_3
    @AC_3.setter
    def AC_3(self, AC_3: str):
        self.__AC_3 = AC_3



class Class:

    pass
