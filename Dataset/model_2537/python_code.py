from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class ref_unsettable_EU:

    def __init__(self, name: str, ids: str, labels: str, DU86: set["DU"] = None):
        self.name = name
        self.ids = ids
        self.labels = labels
        self.DU86 = DU86 if DU86 is not None else set()
        
    @property
    def ids(self) -> str:
        return self.__ids

    @ids.setter
    def ids(self, ids: str):
        self.__ids = ids

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def labels(self) -> str:
        return self.__labels

    @labels.setter
    def labels(self, labels: str):
        self.__labels = labels

    @property
    def DU86(self):
        return self.__DU86

    @DU86.setter
    def DU86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ref_unsettable_EU__DU86", None)
        self.__DU86 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "unsettable87"):
                    opp_val = getattr(item, "unsettable87", None)
                    
                    if opp_val == self:
                        setattr(item, "unsettable87", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "unsettable87"):
                    opp_val = getattr(item, "unsettable87", None)
                    
                    setattr(item, "unsettable87", self)
                    

class ref_unsettable_BU:

    pass
class CU:

    pass
class C2U:

    pass
class ref_unsettable_C3U:

    pass
class ref_unsettable_C4U:

    pass
class EU:

    pass
class ref_unsettable_DU:

    pass
class C4U:

    pass
class ref_unsettable_CU:

    pass
class DU:

    pass
class ref_E:

    def __init__(self, ids: str, labels: str, name: str, e: set["ref_D"] = None, E: "ref_D" = None):
        self.ids = ids
        self.labels = labels
        self.name = name
        self.e = e if e is not None else set()
        self.E = E
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def labels(self) -> str:
        return self.__labels

    @labels.setter
    def labels(self, labels: str):
        self.__labels = labels

    @property
    def ids(self) -> str:
        return self.__ids

    @ids.setter
    def ids(self, ids: str):
        self.__ids = ids

    @property
    def E(self):
        return self.__E

    @E.setter
    def E(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ref_E__E", None)
        self.__E = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "d24"):
                opp_val = getattr(old_value, "d24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "d24"):
                opp_val = getattr(value, "d24", None)
                if opp_val is None:
                    setattr(value, "d24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def e(self):
        return self.__e

    @e.setter
    def e(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ref_E__e", None)
        self.__e = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "D29"):
                    opp_val = getattr(item, "D29", None)
                    
                    if opp_val == self:
                        setattr(item, "D29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "D29"):
                    opp_val = getattr(item, "D29", None)
                    
                    setattr(item, "D29", self)
                    

class ref_unsettable_AU:

    pass
class ref_unsettable_C2U:

    pass
class BU:

    pass
class AU:

    pass
class ref_unsettable_C1U:

    pass
class ref_C3:

    pass
class ref_B:

    pass
class ref_A:

    pass
class ref_C4:

    pass
class ref_C1:

    pass
class ref_D:

    pass
class ref_C:

    pass
class ref_C2:

    pass