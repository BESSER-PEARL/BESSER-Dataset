from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class MyClass19:

    pass


class MyClass18:

    pass


class StopButton:

    pass


class MyClass13:

    pass


class MyClass12:

    pass


class MyClass9:

    def __init__(self, h: int, myClass190: "MyClass19" = None):
        self.h = h
        self.myClass190 = myClass190
        
        pass
    @property
    def h(self):
        return self.__h
    @h.setter
    def h(self, h: int):
        self.__h = h

    @property
    def myClass190(self):
        return self.__myClass190
    @myClass190.setter
    def myClass190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MyClass9__myClass190", None)
        self.__myClass190 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myClass91"):
                opp_val = getattr(old_value, "myClass91", None)
                if opp_val == self:
                    setattr(old_value, "myClass91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myClass91"):
                opp_val = getattr(value, "myClass91", None)
                setattr(value, "myClass91", self)



class MyClass7:

    pass


class MyClass6:

    pass


class MyClass4:

    pass


class MyClass3:

    pass


class MyClass2:

    pass


class MyClass:

    pass


class MonoBehaviour:

    pass
