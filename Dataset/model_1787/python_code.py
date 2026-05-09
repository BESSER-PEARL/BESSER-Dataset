from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class extlibrary_Book:

    def __init__(self, title: str, pages: int):
        self.title = title
        self.pages = pages
        
        pass
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, pages: int):
        self.__pages = pages

