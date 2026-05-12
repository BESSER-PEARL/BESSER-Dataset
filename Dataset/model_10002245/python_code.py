from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class MyClass5:

    pass


class MyClass4:

    pass


class MyClass3:

    pass


class MyClass2:

    def __init__(self, attribute: int, attribute2: str, attribute3: str, myClass41: "MyClass4" = None):
        self.attribute = attribute
        self.attribute2 = attribute2
        self.attribute3 = attribute3
        self.myClass41 = myClass41
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: int):
        self.__attribute = attribute

    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: str):
        self.__attribute2 = attribute2

    @property
    def attribute3(self):
        return self.__attribute3
    @attribute3.setter
    def attribute3(self, attribute3: str):
        self.__attribute3 = attribute3

    @property
    def myClass41(self):
        return self.__myClass41
    @myClass41.setter
    def myClass41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MyClass2__myClass41", None)
        self.__myClass41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myClass20"):
                opp_val = getattr(old_value, "myClass20", None)
                if opp_val == self:
                    setattr(old_value, "myClass20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myClass20"):
                opp_val = getattr(value, "myClass20", None)
                setattr(value, "myClass20", self)



class T2:

    pass


class T:

    pass


class MyClass:

    pass
