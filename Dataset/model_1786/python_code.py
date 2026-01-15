from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class extlibrary_Book:

    def __init__(self, title: str, pages: int):
        self.title = title
        self.pages = pages
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def pages(self) -> int:
        return self.__pages

    @pages.setter
    def pages(self, pages: int):
        self.__pages = pages
