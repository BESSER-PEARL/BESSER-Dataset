from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class mm2_Category:

    def __init__(self, name: str, mm2_Category: "mm2_Library" = None, mm2_Category7: "mm2_Category" = None, mm2_Category5: set["mm2_Category"] = None, mm2_Category9: set["mm2_Medium"] = None):
        self.name = name
        self.mm2_Category = mm2_Category
        self.mm2_Category7 = mm2_Category7
        self.mm2_Category5 = mm2_Category5 if mm2_Category5 is not None else set()
        self.mm2_Category9 = mm2_Category9 if mm2_Category9 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mm2_Category9(self):
        return self.__mm2_Category9

    @mm2_Category9.setter
    def mm2_Category9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm2_Category__mm2_Category9", None)
        self.__mm2_Category9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mm2_Medium10"):
                    opp_val = getattr(item, "mm2_Medium10", None)
                    
                    if opp_val == self:
                        setattr(item, "mm2_Medium10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mm2_Medium10"):
                    opp_val = getattr(item, "mm2_Medium10", None)
                    
                    setattr(item, "mm2_Medium10", self)
                    

    @property
    def mm2_Category(self):
        return self.__mm2_Category

    @mm2_Category.setter
    def mm2_Category(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm2_Category__mm2_Category", None)
        self.__mm2_Category = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mm2_Library4"):
                opp_val = getattr(old_value, "mm2_Library4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mm2_Library4"):
                opp_val = getattr(value, "mm2_Library4", None)
                if opp_val is None:
                    setattr(value, "mm2_Library4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mm2_Category7(self):
        return self.__mm2_Category7

    @mm2_Category7.setter
    def mm2_Category7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm2_Category__mm2_Category7", None)
        self.__mm2_Category7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mm2_Category5"):
                opp_val = getattr(old_value, "mm2_Category5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mm2_Category5"):
                opp_val = getattr(value, "mm2_Category5", None)
                if opp_val is None:
                    setattr(value, "mm2_Category5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mm2_Category5(self):
        return self.__mm2_Category5

    @mm2_Category5.setter
    def mm2_Category5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm2_Category__mm2_Category5", None)
        self.__mm2_Category5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mm2_Category7"):
                    opp_val = getattr(item, "mm2_Category7", None)
                    
                    if opp_val == self:
                        setattr(item, "mm2_Category7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mm2_Category7"):
                    opp_val = getattr(item, "mm2_Category7", None)
                    
                    setattr(item, "mm2_Category7", self)
                    

class mm2_Library:

    def __init__(self, name: str, mm2_Library: set["mm2_Member"] = None, mm2_Library2: set["mm2_Medium"] = None, mm2_Library4: set["mm2_Category"] = None):
        self.name = name
        self.mm2_Library = mm2_Library if mm2_Library is not None else set()
        self.mm2_Library2 = mm2_Library2 if mm2_Library2 is not None else set()
        self.mm2_Library4 = mm2_Library4 if mm2_Library4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mm2_Library2(self):
        return self.__mm2_Library2

    @mm2_Library2.setter
    def mm2_Library2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm2_Library__mm2_Library2", None)
        self.__mm2_Library2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mm2_Medium"):
                    opp_val = getattr(item, "mm2_Medium", None)
                    
                    if opp_val == self:
                        setattr(item, "mm2_Medium", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mm2_Medium"):
                    opp_val = getattr(item, "mm2_Medium", None)
                    
                    setattr(item, "mm2_Medium", self)
                    

    @property
    def mm2_Library(self):
        return self.__mm2_Library

    @mm2_Library.setter
    def mm2_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm2_Library__mm2_Library", None)
        self.__mm2_Library = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mm2_Member"):
                    opp_val = getattr(item, "mm2_Member", None)
                    
                    if opp_val == self:
                        setattr(item, "mm2_Member", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mm2_Member"):
                    opp_val = getattr(item, "mm2_Member", None)
                    
                    setattr(item, "mm2_Member", self)
                    

    @property
    def mm2_Library4(self):
        return self.__mm2_Library4

    @mm2_Library4.setter
    def mm2_Library4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm2_Library__mm2_Library4", None)
        self.__mm2_Library4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mm2_Category"):
                    opp_val = getattr(item, "mm2_Category", None)
                    
                    if opp_val == self:
                        setattr(item, "mm2_Category", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mm2_Category"):
                    opp_val = getattr(item, "mm2_Category", None)
                    
                    setattr(item, "mm2_Category", self)
                    

class mm2_Medium:

    def __init__(self, name: str, type: str, mm2_Medium: "mm2_Library" = None, mm2_Medium10: "mm2_Category" = None, mm2_Medium13: "mm2_Member" = None):
        self.name = name
        self.type = type
        self.mm2_Medium = mm2_Medium
        self.mm2_Medium10 = mm2_Medium10
        self.mm2_Medium13 = mm2_Medium13
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mm2_Medium(self):
        return self.__mm2_Medium

    @mm2_Medium.setter
    def mm2_Medium(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm2_Medium__mm2_Medium", None)
        self.__mm2_Medium = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mm2_Library2"):
                opp_val = getattr(old_value, "mm2_Library2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mm2_Library2"):
                opp_val = getattr(value, "mm2_Library2", None)
                if opp_val is None:
                    setattr(value, "mm2_Library2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mm2_Medium13(self):
        return self.__mm2_Medium13

    @mm2_Medium13.setter
    def mm2_Medium13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm2_Medium__mm2_Medium13", None)
        self.__mm2_Medium13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mm2_Member12"):
                opp_val = getattr(old_value, "mm2_Member12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mm2_Member12"):
                opp_val = getattr(value, "mm2_Member12", None)
                if opp_val is None:
                    setattr(value, "mm2_Member12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mm2_Medium10(self):
        return self.__mm2_Medium10

    @mm2_Medium10.setter
    def mm2_Medium10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm2_Medium__mm2_Medium10", None)
        self.__mm2_Medium10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mm2_Category9"):
                opp_val = getattr(old_value, "mm2_Category9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mm2_Category9"):
                opp_val = getattr(value, "mm2_Category9", None)
                if opp_val is None:
                    setattr(value, "mm2_Category9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mm2_Member:

    def __init__(self, name: str, mm2_Member: "mm2_Library" = None, mm2_Member12: set["mm2_Medium"] = None):
        self.name = name
        self.mm2_Member = mm2_Member
        self.mm2_Member12 = mm2_Member12 if mm2_Member12 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mm2_Member(self):
        return self.__mm2_Member

    @mm2_Member.setter
    def mm2_Member(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm2_Member__mm2_Member", None)
        self.__mm2_Member = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mm2_Library"):
                opp_val = getattr(old_value, "mm2_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mm2_Library"):
                opp_val = getattr(value, "mm2_Library", None)
                if opp_val is None:
                    setattr(value, "mm2_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mm2_Member12(self):
        return self.__mm2_Member12

    @mm2_Member12.setter
    def mm2_Member12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm2_Member__mm2_Member12", None)
        self.__mm2_Member12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mm2_Medium13"):
                    opp_val = getattr(item, "mm2_Medium13", None)
                    
                    if opp_val == self:
                        setattr(item, "mm2_Medium13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mm2_Medium13"):
                    opp_val = getattr(item, "mm2_Medium13", None)
                    
                    setattr(item, "mm2_Medium13", self)
                    
