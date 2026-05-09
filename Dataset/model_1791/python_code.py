from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class column_TestSchema:

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class column_Book:

    def __init__(self, title: str, pages: str, weight: str, author: str):
        self.title = title
        self.pages = pages
        self.weight = weight
        self.author = author
        
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
    def pages(self, pages: str):
        self.__pages = pages


    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight: str):
        self.__weight = weight


    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

