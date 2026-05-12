from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Search_books_UseCase:

    pass


class Librarian_Actor:

    pass


class Member_Actor:

    pass





class Update_member_profile_external:

    pass


class Return_book_external:

    pass


class Issue_book_external:

    pass


class Issue_member_card_external:

    pass


class Person:

    def __init__(self, address: str, phone: str):
        self.address = address
        self.phone = phone
        
        pass
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone



class Customer:

    def __init__(self, recruitmentDate: date):
        self.recruitmentDate = recruitmentDate
        
        pass
    @property
    def recruitmentDate(self):
        return self.__recruitmentDate
    @recruitmentDate.setter
    def recruitmentDate(self, recruitmentDate: date):
        self.__recruitmentDate = recruitmentDate



class Library_Management_Component:

    pass


class Request_book_return_external:

    pass


class Request_book_external:

    pass


class Inquiry_for_membership_external:

    pass
