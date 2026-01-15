from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class extlibrary_Book:

    def __init__(self, title: str):
        self.title = title
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title
