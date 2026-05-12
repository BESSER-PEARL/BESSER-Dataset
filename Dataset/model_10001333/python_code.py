from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class UseCase_UseCase:

    pass


class replace_books_with_updated_info_UseCase:

    pass


class retire_books_UseCase:

    pass


class help_people_with_research__UseCase:

    pass


class organize_books_UseCase:

    pass


class renew_UseCase:

    pass


class return__UseCase:

    pass


class reserve_UseCase:

    pass


class check_out__UseCase:

    pass


class Librarian__Actor:

    pass


class patron__Actor:

    pass


class Order_new_books_UseCase:

    pass


class renew_magazine_subscr_UseCase:

    pass


class UseCase4_UseCase:

    pass


class UseCase3_UseCase:

    pass


class UseCase2_UseCase:

    pass





class library_management__Library:

    def __init__(self, Books: str, Softwares: str, Videos: str, Computers: str, CD: str):
        self.Books = Books
        self.Softwares = Softwares
        self.Videos = Videos
        self.Computers = Computers
        self.CD = CD
        
        pass
    @property
    def CD(self):
        return self.__CD
    @CD.setter
    def CD(self, CD: str):
        self.__CD = CD

    @property
    def Books(self):
        return self.__Books
    @Books.setter
    def Books(self, Books: str):
        self.__Books = Books

    @property
    def Computers(self):
        return self.__Computers
    @Computers.setter
    def Computers(self, Computers: str):
        self.__Computers = Computers

    @property
    def Softwares(self):
        return self.__Softwares
    @Softwares.setter
    def Softwares(self, Softwares: str):
        self.__Softwares = Softwares

    @property
    def Videos(self):
        return self.__Videos
    @Videos.setter
    def Videos(self, Videos: str):
        self.__Videos = Videos



class library_management__librarian:

    def __init__(self, CollectFIne_fine_: int):
        self.CollectFIne_fine_ = CollectFIne_fine_
        
        pass
    @property
    def CollectFIne_fine_(self):
        return self.__CollectFIne_fine_
    @CollectFIne_fine_.setter
    def CollectFIne_fine_(self, CollectFIne_fine_: int):
        self.__CollectFIne_fine_ = CollectFIne_fine_



class library_management__patron:

    def __init__(self, PayFIne_Dt_date_: int):
        self.PayFIne_Dt_date_ = PayFIne_Dt_date_
        
        pass
    @property
    def PayFIne_Dt_date_(self):
        return self.__PayFIne_Dt_date_
    @PayFIne_Dt_date_.setter
    def PayFIne_Dt_date_(self, PayFIne_Dt_date_: int):
        self.__PayFIne_Dt_date_ = PayFIne_Dt_date_

