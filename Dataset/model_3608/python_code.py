from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class panamaRelational_PanamaOfficers:

    def __init__(self, name: str, company: str):
        self.name = name
        self.company = company
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def company(self):
        return self.__company

    @company.setter
    def company(self, company: str):
        self.__company = company

