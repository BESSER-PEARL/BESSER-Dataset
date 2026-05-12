from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Librarian_Actor:

    pass


class Member_Actor:

    pass





class Request_book_return_external:

    pass


class Request_book_external:

    pass


class Inquiry_for_membership_external:

    pass


class UserProperties:

    def __init__(self, roles: str, Roles: str):
        self.roles = roles
        self.Roles = Roles
        
        pass
    @property
    def Roles(self):
        return self.__Roles
    @Roles.setter
    def Roles(self, Roles: str):
        self.__Roles = Roles

    @property
    def roles(self):
        return self.__roles
    @roles.setter
    def roles(self, roles: str):
        self.__roles = roles



class Library_Management_Component:

    pass


class Cancel_membership_external:

    pass


class Maintain_book_in_records_external:

    pass


class Update_member_profile_external:

    pass


class Return_book_external:

    pass


class Issue_book_external:

    pass


class Issue_member_card_external:

    pass


class Search_books_external:

    pass
