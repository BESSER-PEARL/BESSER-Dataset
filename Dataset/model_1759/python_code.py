from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class library_book:

    def __init__(self, pages: str, title: str, author: str, published: str):
        self.pages = pages
        self.title = title
        self.author = author
        self.published = published
        
        pass
    @property
    def pages(self):
        return self.__pages

    @pages.setter
    def pages(self, pages: str):
        self.__pages = pages


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author


    @property
    def published(self):
        return self.__published

    @published.setter
    def published(self, published: str):
        self.__published = published

