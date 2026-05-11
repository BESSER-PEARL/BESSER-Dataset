from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Test_Foo:

    def __init__(self, bar: str):
        self.bar = bar
        
        pass
    @property
    def bar(self):
        return self.__bar

    @bar.setter
    def bar(self, bar: str):
        self.__bar = bar

