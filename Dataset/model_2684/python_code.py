from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class simplecont_C:

    def __init__(self, id: str, simplecont_C4: "simplecont_B" = None, simplecont_C: "simplecont_A" = None):
        self.id = id
        self.simplecont_C4 = simplecont_C4
        self.simplecont_C = simplecont_C
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def simplecont_C(self):
        return self.__simplecont_C

    @simplecont_C.setter
    def simplecont_C(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplecont_C__simplecont_C", None)
        self.__simplecont_C = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplecont_A2"):
                opp_val = getattr(old_value, "simplecont_A2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplecont_A2"):
                opp_val = getattr(value, "simplecont_A2", None)
                if opp_val is None:
                    setattr(value, "simplecont_A2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simplecont_C4(self):
        return self.__simplecont_C4

    @simplecont_C4.setter
    def simplecont_C4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplecont_C__simplecont_C4", None)
        self.__simplecont_C4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplecont_B5"):
                opp_val = getattr(old_value, "simplecont_B5", None)
                if opp_val == self:
                    setattr(old_value, "simplecont_B5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplecont_B5"):
                opp_val = getattr(value, "simplecont_B5", None)
                setattr(value, "simplecont_B5", self)

class simplecont_B:

    def __init__(self, name: str, simplecont_B5: "simplecont_C" = None, simplecont_B: "simplecont_A" = None):
        self.name = name
        self.simplecont_B5 = simplecont_B5
        self.simplecont_B = simplecont_B
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simplecont_B(self):
        return self.__simplecont_B

    @simplecont_B.setter
    def simplecont_B(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplecont_B__simplecont_B", None)
        self.__simplecont_B = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplecont_A"):
                opp_val = getattr(old_value, "simplecont_A", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplecont_A"):
                opp_val = getattr(value, "simplecont_A", None)
                if opp_val is None:
                    setattr(value, "simplecont_A", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simplecont_B5(self):
        return self.__simplecont_B5

    @simplecont_B5.setter
    def simplecont_B5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplecont_B__simplecont_B5", None)
        self.__simplecont_B5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplecont_C4"):
                opp_val = getattr(old_value, "simplecont_C4", None)
                if opp_val == self:
                    setattr(old_value, "simplecont_C4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplecont_C4"):
                opp_val = getattr(value, "simplecont_C4", None)
                setattr(value, "simplecont_C4", self)

class simplecont_X:

    pass
class simplecont_A:

    def __init__(self, name: str, simplecont_A7: "simplecont_X" = None, simplecont_A: set["simplecont_B"] = None, simplecont_A2: set["simplecont_C"] = None):
        self.name = name
        self.simplecont_A7 = simplecont_A7
        self.simplecont_A = simplecont_A if simplecont_A is not None else set()
        self.simplecont_A2 = simplecont_A2 if simplecont_A2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def simplecont_A(self):
        return self.__simplecont_A

    @simplecont_A.setter
    def simplecont_A(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplecont_A__simplecont_A", None)
        self.__simplecont_A = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simplecont_B"):
                    opp_val = getattr(item, "simplecont_B", None)
                    
                    if opp_val == self:
                        setattr(item, "simplecont_B", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simplecont_B"):
                    opp_val = getattr(item, "simplecont_B", None)
                    
                    setattr(item, "simplecont_B", self)
                    

    @property
    def simplecont_A7(self):
        return self.__simplecont_A7

    @simplecont_A7.setter
    def simplecont_A7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplecont_A__simplecont_A7", None)
        self.__simplecont_A7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simplecont_X"):
                opp_val = getattr(old_value, "simplecont_X", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simplecont_X"):
                opp_val = getattr(value, "simplecont_X", None)
                if opp_val is None:
                    setattr(value, "simplecont_X", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def simplecont_A2(self):
        return self.__simplecont_A2

    @simplecont_A2.setter
    def simplecont_A2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_simplecont_A__simplecont_A2", None)
        self.__simplecont_A2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "simplecont_C"):
                    opp_val = getattr(item, "simplecont_C", None)
                    
                    if opp_val == self:
                        setattr(item, "simplecont_C", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "simplecont_C"):
                    opp_val = getattr(item, "simplecont_C", None)
                    
                    setattr(item, "simplecont_C", self)
                    
