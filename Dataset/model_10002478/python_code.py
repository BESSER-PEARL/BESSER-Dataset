from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







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


class Request_book_return_external:

    pass


class Request_book_external:

    pass


class Inquiry_for_membership_external:

    pass


class SR_AppBean:

    def __init__(self, time: bool):
        self.time = time
        
        pass
    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self, time: bool):
        self.__time = time



class qwsd:

    pass


class Library_Management_Component:

    pass


class Search_books_external:

    pass
