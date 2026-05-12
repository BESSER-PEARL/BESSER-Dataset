from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class UseCase2_UseCase:

    pass


class Actor_Actor:

    pass


class UseCase_UseCase:

    pass





class MyInterface_Interface:

    pass


class MyClass:

    def __init__(self, Abb: bool, ABC: MyClass, myInterface2: "MyInterface_Interface" = None):
        self.Abb = Abb
        self.ABC = ABC
        self.myInterface2 = myInterface2
        
        pass
    @property
    def Abb(self):
        return self.__Abb
    @Abb.setter
    def Abb(self, Abb: bool):
        self.__Abb = Abb

    @property
    def ABC(self):
        return self.__ABC
    @ABC.setter
    def ABC(self, ABC: MyClass):
        self.__ABC = ABC

    @property
    def myInterface2(self):
        return self.__myInterface2
    @myInterface2.setter
    def myInterface2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MyClass__myInterface2", None)
        self.__myInterface2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myClass3"):
                opp_val = getattr(old_value, "myClass3", None)
                if opp_val == self:
                    setattr(old_value, "myClass3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myClass3"):
                opp_val = getattr(value, "myClass3", None)
                setattr(value, "myClass3", self)

