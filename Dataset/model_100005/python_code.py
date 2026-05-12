from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Publication_Publication:

    def __init__(self, title: str, authors: str, nbPages: str):
        self.title = title
        self.authors = authors
        self.nbPages = nbPages
        
        pass
    @property
    def nbPages(self):
        return self.__nbPages

    @nbPages.setter
    def nbPages(self, nbPages: str):
        self.__nbPages = nbPages


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, authors: str):
        self.__authors = authors

