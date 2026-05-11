from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class test_A:

    def __init__(self):
        
        pass
    def op1(self) :
        # TODO: Implement op1 method
        pass

class test_OptionTestClass:

    def __init__(self, attribute: str, attribute2: str):
        self.attribute = attribute
        self.attribute2 = attribute2
        
        pass
    @property
    def attribute2(self):
        return self.__attribute2

    @attribute2.setter
    def attribute2(self, attribute2: str):
        self.__attribute2 = attribute2


    @property
    def attribute(self):
        return self.__attribute

    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute


class test_D:

    def __init__(self, attr1: str):
        self.attr1 = attr1
        
        pass
    @property
    def attr1(self):
        return self.__attr1

    @attr1.setter
    def attr1(self, attr1: str):
        self.__attr1 = attr1


class A:

    pass
class test_C(A):

    pass
class test_B(A):

    pass