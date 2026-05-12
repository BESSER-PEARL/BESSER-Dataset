from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Actor2_Actor:

    pass


class mypackage_UseCase3_UseCase:

    pass


class mypackage_UseCase2_UseCase:

    pass


class mypackage_UseCase_UseCase:

    pass


class Actor_Actor:

    pass





class mypackage3_MyClass5:

    def __init__(self, attribute: str):
        self.attribute = attribute
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute



class mypackage3_MyClass3:

    def __init__(self, attribute3_1: str, This_is_a1: set["mypackage2_MyClass2"] = None):
        self.attribute3_1 = attribute3_1
        self.This_is_a1 = This_is_a1 if This_is_a1 is not None else set()
        
        pass
    @property
    def attribute3_1(self):
        return self.__attribute3_1
    @attribute3_1.setter
    def attribute3_1(self, attribute3_1: str):
        self.__attribute3_1 = attribute3_1

    @property
    def This_is_a1(self):
        return self.__This_is_a1
    @This_is_a1.setter
    def This_is_a1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mypackage3_MyClass3__This_is_a1", None)
        self.__This_is_a1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "This_is_a0"):
                    opp_val = getattr(item, "This_is_a0", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "This_is_a0"):
                    opp_val = getattr(item, "This_is_a0", None)
                    
                    if opp_val is None:
                        setattr(item, "This_is_a0", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class mypackage2_MyClass2:

    def __init__(self, attribute2_1: str, attribute2_2: float, This_is_a0: set["mypackage3_MyClass3"] = None):
        self.attribute2_1 = attribute2_1
        self.attribute2_2 = attribute2_2
        self.This_is_a0 = This_is_a0 if This_is_a0 is not None else set()
        
        pass
    @property
    def attribute2_1(self):
        return self.__attribute2_1
    @attribute2_1.setter
    def attribute2_1(self, attribute2_1: str):
        self.__attribute2_1 = attribute2_1

    @property
    def attribute2_2(self):
        return self.__attribute2_2
    @attribute2_2.setter
    def attribute2_2(self, attribute2_2: float):
        self.__attribute2_2 = attribute2_2

    @property
    def This_is_a0(self):
        return self.__This_is_a0
    @This_is_a0.setter
    def This_is_a0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mypackage2_MyClass2__This_is_a0", None)
        self.__This_is_a0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "This_is_a1"):
                    opp_val = getattr(item, "This_is_a1", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "This_is_a1"):
                    opp_val = getattr(item, "This_is_a1", None)
                    
                    if opp_val is None:
                        setattr(item, "This_is_a1", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

