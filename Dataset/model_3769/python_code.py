from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class ecore_EClass:

    def __init__(self, abstract: str):
        self.abstract = abstract
        
    @property
    def abstract(self) -> str:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: str):
        self.__abstract = abstract
