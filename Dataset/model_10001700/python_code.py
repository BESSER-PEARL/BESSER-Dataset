from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class C1:

    def __init__(self, C1ID: int, c20: set["C2"] = None, c32: "C3" = None):
        self.C1ID = C1ID
        self.c20 = c20 if c20 is not None else set()
        self.c32 = c32
        
        pass
    @property
    def C1ID(self):
        return self.__C1ID
    @C1ID.setter
    def C1ID(self, C1ID: int):
        self.__C1ID = C1ID

    @property
    def c20(self):
        return self.__c20
    @c20.setter
    def c20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C1__c20", None)
        self.__c20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "c11"):
                    opp_val = getattr(item, "c11", None)
                    
                    if opp_val == self:
                        setattr(item, "c11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "c11"):
                    opp_val = getattr(item, "c11", None)
                    
                    setattr(item, "c11", self)
                    

    @property
    def c32(self):
        return self.__c32
    @c32.setter
    def c32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C1__c32", None)
        self.__c32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "c13"):
                opp_val = getattr(old_value, "c13", None)
                if opp_val == self:
                    setattr(old_value, "c13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c13"):
                opp_val = getattr(value, "c13", None)
                setattr(value, "c13", self)



class C3:

    pass


class C2:

    def __init__(self, C2ID: int, C1ID: int, attribute: str, c11: "C1" = None):
        self.C2ID = C2ID
        self.C1ID = C1ID
        self.attribute = attribute
        self.c11 = c11
        
        pass
    @property
    def C2ID(self):
        return self.__C2ID
    @C2ID.setter
    def C2ID(self, C2ID: int):
        self.__C2ID = C2ID

    @property
    def C1ID(self):
        return self.__C1ID
    @C1ID.setter
    def C1ID(self, C1ID: int):
        self.__C1ID = C1ID

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def c11(self):
        return self.__c11
    @c11.setter
    def c11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_C2__c11", None)
        self.__c11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "c20"):
                opp_val = getattr(old_value, "c20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "c20"):
                opp_val = getattr(value, "c20", None)
                if opp_val is None:
                    setattr(value, "c20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

