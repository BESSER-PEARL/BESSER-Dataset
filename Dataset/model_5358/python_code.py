from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Test_Foo:

    def __init__(self, bar: str):
        self.bar = bar
        
    @property
    def bar(self) -> str:
        return self.__bar

    @bar.setter
    def bar(self, bar: str):
        self.__bar = bar
