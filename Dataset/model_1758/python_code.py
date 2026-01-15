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
        
    @property
    def pages(self) -> str:
        return self.__pages

    @pages.setter
    def pages(self, pages: str):
        self.__pages = pages

    @property
    def published(self) -> str:
        return self.__published

    @published.setter
    def published(self, published: str):
        self.__published = published

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title
