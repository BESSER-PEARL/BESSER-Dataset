from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class mm3_Book:

    def __init__(self, name: str, mm3_Book: "mm3_Library" = None, mm3_Book7: "mm3_Member" = None):
        self.name = name
        self.mm3_Book = mm3_Book
        self.mm3_Book7 = mm3_Book7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mm3_Book(self):
        return self.__mm3_Book

    @mm3_Book.setter
    def mm3_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm3_Book__mm3_Book", None)
        self.__mm3_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mm3_Library2"):
                opp_val = getattr(old_value, "mm3_Library2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mm3_Library2"):
                opp_val = getattr(value, "mm3_Library2", None)
                if opp_val is None:
                    setattr(value, "mm3_Library2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mm3_Book7(self):
        return self.__mm3_Book7

    @mm3_Book7.setter
    def mm3_Book7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm3_Book__mm3_Book7", None)
        self.__mm3_Book7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mm3_Member6"):
                opp_val = getattr(old_value, "mm3_Member6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mm3_Member6"):
                opp_val = getattr(value, "mm3_Member6", None)
                if opp_val is None:
                    setattr(value, "mm3_Member6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mm3_Film:

    def __init__(self, name: str, mm3_Film: "mm3_Library" = None, mm3_Film10: "mm3_Member" = None):
        self.name = name
        self.mm3_Film = mm3_Film
        self.mm3_Film10 = mm3_Film10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mm3_Film10(self):
        return self.__mm3_Film10

    @mm3_Film10.setter
    def mm3_Film10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm3_Film__mm3_Film10", None)
        self.__mm3_Film10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mm3_Member9"):
                opp_val = getattr(old_value, "mm3_Member9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mm3_Member9"):
                opp_val = getattr(value, "mm3_Member9", None)
                if opp_val is None:
                    setattr(value, "mm3_Member9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mm3_Film(self):
        return self.__mm3_Film

    @mm3_Film.setter
    def mm3_Film(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm3_Film__mm3_Film", None)
        self.__mm3_Film = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mm3_Library4"):
                opp_val = getattr(old_value, "mm3_Library4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mm3_Library4"):
                opp_val = getattr(value, "mm3_Library4", None)
                if opp_val is None:
                    setattr(value, "mm3_Library4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mm3_Member:

    def __init__(self, name: str, mm3_Member: "mm3_Library" = None, mm3_Member6: set["mm3_Book"] = None, mm3_Member9: set["mm3_Film"] = None):
        self.name = name
        self.mm3_Member = mm3_Member
        self.mm3_Member6 = mm3_Member6 if mm3_Member6 is not None else set()
        self.mm3_Member9 = mm3_Member9 if mm3_Member9 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mm3_Member6(self):
        return self.__mm3_Member6

    @mm3_Member6.setter
    def mm3_Member6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm3_Member__mm3_Member6", None)
        self.__mm3_Member6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mm3_Book7"):
                    opp_val = getattr(item, "mm3_Book7", None)
                    
                    if opp_val == self:
                        setattr(item, "mm3_Book7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mm3_Book7"):
                    opp_val = getattr(item, "mm3_Book7", None)
                    
                    setattr(item, "mm3_Book7", self)
                    

    @property
    def mm3_Member(self):
        return self.__mm3_Member

    @mm3_Member.setter
    def mm3_Member(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm3_Member__mm3_Member", None)
        self.__mm3_Member = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mm3_Library"):
                opp_val = getattr(old_value, "mm3_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mm3_Library"):
                opp_val = getattr(value, "mm3_Library", None)
                if opp_val is None:
                    setattr(value, "mm3_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mm3_Member9(self):
        return self.__mm3_Member9

    @mm3_Member9.setter
    def mm3_Member9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm3_Member__mm3_Member9", None)
        self.__mm3_Member9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mm3_Film10"):
                    opp_val = getattr(item, "mm3_Film10", None)
                    
                    if opp_val == self:
                        setattr(item, "mm3_Film10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mm3_Film10"):
                    opp_val = getattr(item, "mm3_Film10", None)
                    
                    setattr(item, "mm3_Film10", self)
                    

class mm3_Library:

    def __init__(self, name: str, mm3_Library2: set["mm3_Book"] = None, mm3_Library4: set["mm3_Film"] = None, mm3_Library: set["mm3_Member"] = None):
        self.name = name
        self.mm3_Library2 = mm3_Library2 if mm3_Library2 is not None else set()
        self.mm3_Library4 = mm3_Library4 if mm3_Library4 is not None else set()
        self.mm3_Library = mm3_Library if mm3_Library is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mm3_Library(self):
        return self.__mm3_Library

    @mm3_Library.setter
    def mm3_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm3_Library__mm3_Library", None)
        self.__mm3_Library = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mm3_Member"):
                    opp_val = getattr(item, "mm3_Member", None)
                    
                    if opp_val == self:
                        setattr(item, "mm3_Member", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mm3_Member"):
                    opp_val = getattr(item, "mm3_Member", None)
                    
                    setattr(item, "mm3_Member", self)
                    

    @property
    def mm3_Library4(self):
        return self.__mm3_Library4

    @mm3_Library4.setter
    def mm3_Library4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm3_Library__mm3_Library4", None)
        self.__mm3_Library4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mm3_Film"):
                    opp_val = getattr(item, "mm3_Film", None)
                    
                    if opp_val == self:
                        setattr(item, "mm3_Film", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mm3_Film"):
                    opp_val = getattr(item, "mm3_Film", None)
                    
                    setattr(item, "mm3_Film", self)
                    

    @property
    def mm3_Library2(self):
        return self.__mm3_Library2

    @mm3_Library2.setter
    def mm3_Library2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm3_Library__mm3_Library2", None)
        self.__mm3_Library2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mm3_Book"):
                    opp_val = getattr(item, "mm3_Book", None)
                    
                    if opp_val == self:
                        setattr(item, "mm3_Book", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mm3_Book"):
                    opp_val = getattr(item, "mm3_Book", None)
                    
                    setattr(item, "mm3_Book", self)
                    
