from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class MyEnum(Enum):
    ABC = "ABC"
    DEF = "DEF"


############################################
# Definition of Classes
############################################

class B:

    pass
class mytest_C(B):

    pass
class mytest_MyRoot:

    pass
class mytest_B:

    def __init__(self, enumatt: str, mytest_B: "mytest_MyRoot" = None, mytest_B5: "mytest_MyRoot" = None):
        self.enumatt = enumatt
        self.mytest_B = mytest_B
        self.mytest_B5 = mytest_B5
        
    @property
    def enumatt(self) -> str:
        return self.__enumatt

    @enumatt.setter
    def enumatt(self, enumatt: str):
        self.__enumatt = enumatt

    @property
    def mytest_B(self):
        return self.__mytest_B

    @mytest_B.setter
    def mytest_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mytest_B__mytest_B", None)
        self.__mytest_B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mytest_MyRoot2"):
                opp_val = getattr(old_value, "mytest_MyRoot2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mytest_MyRoot2"):
                opp_val = getattr(value, "mytest_MyRoot2", None)
                if opp_val is None:
                    setattr(value, "mytest_MyRoot2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mytest_B5(self):
        return self.__mytest_B5

    @mytest_B5.setter
    def mytest_B5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mytest_B__mytest_B5", None)
        self.__mytest_B5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mytest_MyRoot4"):
                opp_val = getattr(old_value, "mytest_MyRoot4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mytest_MyRoot4"):
                opp_val = getattr(value, "mytest_MyRoot4", None)
                if opp_val is None:
                    setattr(value, "mytest_MyRoot4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mytest_A:

    def __init__(self, name: str, mytest_A: "mytest_MyRoot" = None):
        self.name = name
        self.mytest_A = mytest_A
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mytest_A(self):
        return self.__mytest_A

    @mytest_A.setter
    def mytest_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mytest_A__mytest_A", None)
        self.__mytest_A = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mytest_MyRoot"):
                opp_val = getattr(old_value, "mytest_MyRoot", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mytest_MyRoot"):
                opp_val = getattr(value, "mytest_MyRoot", None)
                if opp_val is None:
                    setattr(value, "mytest_MyRoot", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
