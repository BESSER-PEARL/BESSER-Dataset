from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class myDsl_Greeting:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class myDsl_Model:

    def __init__(self, greetings: str):
        self.greetings = greetings
        
    @property
    def greetings(self) -> str:
        return self.__greetings

    @greetings.setter
    def greetings(self, greetings: str):
        self.__greetings = greetings
