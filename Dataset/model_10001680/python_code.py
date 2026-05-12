from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class library_data_base:

    def __init__(self, list_of_books: str, members_information: str, record_patron_borrowing_book: int):
        self.list_of_books = list_of_books
        self.members_information = members_information
        self.record_patron_borrowing_book = record_patron_borrowing_book
        
        pass
    @property
    def list_of_books(self):
        return self.__list_of_books
    @list_of_books.setter
    def list_of_books(self, list_of_books: str):
        self.__list_of_books = list_of_books

    @property
    def record_patron_borrowing_book(self):
        return self.__record_patron_borrowing_book
    @record_patron_borrowing_book.setter
    def record_patron_borrowing_book(self, record_patron_borrowing_book: int):
        self.__record_patron_borrowing_book = record_patron_borrowing_book

    @property
    def members_information(self):
        return self.__members_information
    @members_information.setter
    def members_information(self, members_information: str):
        self.__members_information = members_information



class Book:

    def __init__(self, Book_ISBN: int, book_name: str, Book_Author: int):
        self.Book_ISBN = Book_ISBN
        self.book_name = book_name
        self.Book_Author = Book_Author
        
        pass
    @property
    def Book_ISBN(self):
        return self.__Book_ISBN
    @Book_ISBN.setter
    def Book_ISBN(self, Book_ISBN: int):
        self.__Book_ISBN = Book_ISBN

    @property
    def Book_Author(self):
        return self.__Book_Author
    @Book_Author.setter
    def Book_Author(self, Book_Author: int):
        self.__Book_Author = Book_Author

    @property
    def book_name(self):
        return self.__book_name
    @book_name.setter
    def book_name(self, book_name: str):
        self.__book_name = book_name



class patron:

    def __init__(self, Address: str, Name: str, Contact_number: int):
        self.Address = Address
        self.Name = Name
        self.Contact_number = Contact_number
        
        pass
    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def Contact_number(self):
        return self.__Contact_number
    @Contact_number.setter
    def Contact_number(self, Contact_number: int):
        self.__Contact_number = Contact_number

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name



class librarian:

    def __init__(self, name: str, username: int):
        self.name = name
        self.username = username
        
        pass
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: int):
        self.__username = username

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

