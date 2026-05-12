from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Library_Staff_Actor:

    pass


class Patron_Actor:

    pass





class Search_for_Books_external:

    pass


class Checkout_Book_external:

    pass


class Database_external:

    pass


class Return_Book_external:

    pass


class Send_Book_external:

    pass


class librarymanagementsystem_Library:

    def __init__(self, books: str, CDs: str, software: str, videos: str, fine: str, maxFine: str, computers: int):
        self.books = books
        self.CDs = CDs
        self.software = software
        self.videos = videos
        self.fine = fine
        self.maxFine = maxFine
        self.computers = computers
        
        pass
    @property
    def software(self):
        return self.__software
    @software.setter
    def software(self, software: str):
        self.__software = software

    @property
    def videos(self):
        return self.__videos
    @videos.setter
    def videos(self, videos: str):
        self.__videos = videos

    @property
    def CDs(self):
        return self.__CDs
    @CDs.setter
    def CDs(self, CDs: str):
        self.__CDs = CDs

    @property
    def fine(self):
        return self.__fine
    @fine.setter
    def fine(self, fine: str):
        self.__fine = fine

    @property
    def books(self):
        return self.__books
    @books.setter
    def books(self, books: str):
        self.__books = books

    @property
    def maxFine(self):
        return self.__maxFine
    @maxFine.setter
    def maxFine(self, maxFine: str):
        self.__maxFine = maxFine

    @property
    def computers(self):
        return self.__computers
    @computers.setter
    def computers(self, computers: int):
        self.__computers = computers



class Library_Management_System_Component:

    pass
