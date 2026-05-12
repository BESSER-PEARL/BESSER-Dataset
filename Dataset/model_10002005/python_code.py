from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class MyClass4:

    pass


class MyClass3:

    def __init__(self, attribute: str, dfgd5: "MyClass2" = None, myClass1: "MyClass" = None):
        self.attribute = attribute
        self.dfgd5 = dfgd5
        self.myClass1 = myClass1
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def myClass1(self):
        return self.__myClass1
    @myClass1.setter
    def myClass1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MyClass3__myClass1", None)
        self.__myClass1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myClass30"):
                opp_val = getattr(old_value, "myClass30", None)
                if opp_val == self:
                    setattr(old_value, "myClass30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myClass30"):
                opp_val = getattr(value, "myClass30", None)
                setattr(value, "myClass30", self)

    @property
    def dfgd5(self):
        return self.__dfgd5
    @dfgd5.setter
    def dfgd5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MyClass3__dfgd5", None)
        self.__dfgd5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myClass34"):
                opp_val = getattr(old_value, "myClass34", None)
                if opp_val == self:
                    setattr(old_value, "myClass34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myClass34"):
                opp_val = getattr(value, "myClass34", None)
                setattr(value, "myClass34", self)



class MyClass2:

    pass


class MyClass:

    def __init__(self, asdf: str, myClass46: "MyClass4" = None, myClass30: "MyClass3" = None):
        self.asdf = asdf
        self.myClass46 = myClass46
        self.myClass30 = myClass30
        
        pass
    @property
    def asdf(self):
        return self.__asdf
    @asdf.setter
    def asdf(self, asdf: str):
        self.__asdf = asdf

    @property
    def myClass46(self):
        return self.__myClass46
    @myClass46.setter
    def myClass46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MyClass__myClass46", None)
        self.__myClass46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myClass7"):
                opp_val = getattr(old_value, "myClass7", None)
                if opp_val == self:
                    setattr(old_value, "myClass7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myClass7"):
                opp_val = getattr(value, "myClass7", None)
                setattr(value, "myClass7", self)

    @property
    def myClass30(self):
        return self.__myClass30
    @myClass30.setter
    def myClass30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MyClass__myClass30", None)
        self.__myClass30 = value
        
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

