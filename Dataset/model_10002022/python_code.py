from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class MyClass9:

    pass


class MyClass8:

    pass


class MyClass7:

    pass


class MyClass6:

    pass


class T1:

    pass


class MyClass5:

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



class MyClass4:

    pass


class MyClass3:

    pass


class MyClass2:

    pass


class T:

    pass


class MyClass:

    def __init__(self, attribute: str, attribute2: str, attribute3: str, attribute4: str, myClass80: "MyClass8" = None):
        self.attribute = attribute
        self.attribute2 = attribute2
        self.attribute3 = attribute3
        self.attribute4 = attribute4
        self.myClass80 = myClass80
        
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

    @property
    def attribute3(self):
        return self.__attribute3
    @attribute3.setter
    def attribute3(self, attribute3: str):
        self.__attribute3 = attribute3

    @property
    def attribute4(self):
        return self.__attribute4
    @attribute4.setter
    def attribute4(self, attribute4: str):
        self.__attribute4 = attribute4

    @property
    def myClass80(self):
        return self.__myClass80
    @myClass80.setter
    def myClass80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MyClass__myClass80", None)
        self.__myClass80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myClass1"):
                opp_val = getattr(old_value, "myClass1", None)
                if opp_val == self:
                    setattr(old_value, "myClass1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myClass1"):
                opp_val = getattr(value, "myClass1", None)
                setattr(value, "myClass1", self)

