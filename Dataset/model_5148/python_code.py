from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class A:

    pass
class TestMerge_C(A):

    pass
class TestMerge_A:

    def __init__(self, someNewAttribute: str):
        self.someNewAttribute = someNewAttribute
        
        pass
    @property
    def someNewAttribute(self):
        return self.__someNewAttribute

    @someNewAttribute.setter
    def someNewAttribute(self, someNewAttribute: str):
        self.__someNewAttribute = someNewAttribute

