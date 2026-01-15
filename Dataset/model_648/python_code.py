from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class mm4_Medium:

    def __init__(self, name: str, type: str, mm4_Medium: "mm4_Library" = None, mm4_Medium5: "mm4_Member" = None):
        self.name = name
        self.type = type
        self.mm4_Medium = mm4_Medium
        self.mm4_Medium5 = mm4_Medium5
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def mm4_Medium5(self):
        return self.__mm4_Medium5

    @mm4_Medium5.setter
    def mm4_Medium5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm4_Medium__mm4_Medium5", None)
        self.__mm4_Medium5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mm4_Member4"):
                opp_val = getattr(old_value, "mm4_Member4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mm4_Member4"):
                opp_val = getattr(value, "mm4_Member4", None)
                if opp_val is None:
                    setattr(value, "mm4_Member4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mm4_Medium(self):
        return self.__mm4_Medium

    @mm4_Medium.setter
    def mm4_Medium(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm4_Medium__mm4_Medium", None)
        self.__mm4_Medium = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mm4_Library2"):
                opp_val = getattr(old_value, "mm4_Library2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mm4_Library2"):
                opp_val = getattr(value, "mm4_Library2", None)
                if opp_val is None:
                    setattr(value, "mm4_Library2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mm4_Member:

    def __init__(self, name: str, mm4_Member: "mm4_Library" = None, mm4_Member4: set["mm4_Medium"] = None):
        self.name = name
        self.mm4_Member = mm4_Member
        self.mm4_Member4 = mm4_Member4 if mm4_Member4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mm4_Member4(self):
        return self.__mm4_Member4

    @mm4_Member4.setter
    def mm4_Member4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm4_Member__mm4_Member4", None)
        self.__mm4_Member4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mm4_Medium5"):
                    opp_val = getattr(item, "mm4_Medium5", None)
                    
                    if opp_val == self:
                        setattr(item, "mm4_Medium5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mm4_Medium5"):
                    opp_val = getattr(item, "mm4_Medium5", None)
                    
                    setattr(item, "mm4_Medium5", self)
                    

    @property
    def mm4_Member(self):
        return self.__mm4_Member

    @mm4_Member.setter
    def mm4_Member(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm4_Member__mm4_Member", None)
        self.__mm4_Member = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mm4_Library"):
                opp_val = getattr(old_value, "mm4_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mm4_Library"):
                opp_val = getattr(value, "mm4_Library", None)
                if opp_val is None:
                    setattr(value, "mm4_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mm4_Library:

    def __init__(self, name: str, mm4_Library: set["mm4_Member"] = None, mm4_Library2: set["mm4_Medium"] = None):
        self.name = name
        self.mm4_Library = mm4_Library if mm4_Library is not None else set()
        self.mm4_Library2 = mm4_Library2 if mm4_Library2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mm4_Library(self):
        return self.__mm4_Library

    @mm4_Library.setter
    def mm4_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm4_Library__mm4_Library", None)
        self.__mm4_Library = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mm4_Member"):
                    opp_val = getattr(item, "mm4_Member", None)
                    
                    if opp_val == self:
                        setattr(item, "mm4_Member", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mm4_Member"):
                    opp_val = getattr(item, "mm4_Member", None)
                    
                    setattr(item, "mm4_Member", self)
                    

    @property
    def mm4_Library2(self):
        return self.__mm4_Library2

    @mm4_Library2.setter
    def mm4_Library2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm4_Library__mm4_Library2", None)
        self.__mm4_Library2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mm4_Medium"):
                    opp_val = getattr(item, "mm4_Medium", None)
                    
                    if opp_val == self:
                        setattr(item, "mm4_Medium", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mm4_Medium"):
                    opp_val = getattr(item, "mm4_Medium", None)
                    
                    setattr(item, "mm4_Medium", self)
                    
