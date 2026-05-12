from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Patron_Actor:

    pass


class Cancel_UseCase:

    pass


class create_UseCase:

    pass


class Checkout_book_UseCase:

    pass


class Request_Book_UseCase:

    pass


class Create_library_account_UseCase:

    pass


class Renew_Patron_UseCase:

    pass


class Late_fees_UseCase:

    pass


class Update_Books_UseCase:

    pass


class Remove_Books_UseCase:

    pass


class Add_books_UseCase:

    pass


class Maintain_Patron_profile_UseCase:

    pass


class Return_book_UseCase:

    pass


class Issue_Book_UseCase:

    pass


class Manage_Books_UseCase:

    pass


class Issue_card_UseCase:

    pass


class Librarian_Actor:

    pass





class Library:

    def __init__(self, books: str):
        self.books = books
        
        pass
    @property
    def books(self):
        return self.__books
    @books.setter
    def books(self, books: str):
        self.__books = books



class MyClass:

    pass


class Library_Management_Component:

    pass
