from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class mm1_Book:

    def __init__(self, name: str, mm1_Book7: "mm1_Member" = None, mm1_Book: "mm1_Library" = None):
        self.name = name
        self.mm1_Book7 = mm1_Book7
        self.mm1_Book = mm1_Book
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mm1_Book(self):
        return self.__mm1_Book

    @mm1_Book.setter
    def mm1_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm1_Book__mm1_Book", None)
        self.__mm1_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mm1_Library2"):
                opp_val = getattr(old_value, "mm1_Library2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mm1_Library2"):
                opp_val = getattr(value, "mm1_Library2", None)
                if opp_val is None:
                    setattr(value, "mm1_Library2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mm1_Book7(self):
        return self.__mm1_Book7

    @mm1_Book7.setter
    def mm1_Book7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm1_Book__mm1_Book7", None)
        self.__mm1_Book7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mm1_Member6"):
                opp_val = getattr(old_value, "mm1_Member6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mm1_Member6"):
                opp_val = getattr(value, "mm1_Member6", None)
                if opp_val is None:
                    setattr(value, "mm1_Member6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mm1_Member:

    def __init__(self, name: str, mm1_Member6: set["mm1_Book"] = None, mm1_Member: "mm1_Library" = None, mm1_Member9: set["mm1_Film"] = None):
        self.name = name
        self.mm1_Member6 = mm1_Member6 if mm1_Member6 is not None else set()
        self.mm1_Member = mm1_Member
        self.mm1_Member9 = mm1_Member9 if mm1_Member9 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mm1_Member9(self):
        return self.__mm1_Member9

    @mm1_Member9.setter
    def mm1_Member9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm1_Member__mm1_Member9", None)
        self.__mm1_Member9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mm1_Film10"):
                    opp_val = getattr(item, "mm1_Film10", None)
                    
                    if opp_val == self:
                        setattr(item, "mm1_Film10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mm1_Film10"):
                    opp_val = getattr(item, "mm1_Film10", None)
                    
                    setattr(item, "mm1_Film10", self)
                    

    @property
    def mm1_Member6(self):
        return self.__mm1_Member6

    @mm1_Member6.setter
    def mm1_Member6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm1_Member__mm1_Member6", None)
        self.__mm1_Member6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mm1_Book7"):
                    opp_val = getattr(item, "mm1_Book7", None)
                    
                    if opp_val == self:
                        setattr(item, "mm1_Book7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mm1_Book7"):
                    opp_val = getattr(item, "mm1_Book7", None)
                    
                    setattr(item, "mm1_Book7", self)
                    

    @property
    def mm1_Member(self):
        return self.__mm1_Member

    @mm1_Member.setter
    def mm1_Member(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm1_Member__mm1_Member", None)
        self.__mm1_Member = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mm1_Library"):
                opp_val = getattr(old_value, "mm1_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mm1_Library"):
                opp_val = getattr(value, "mm1_Library", None)
                if opp_val is None:
                    setattr(value, "mm1_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mm1_Film:

    def __init__(self, name: str, mm1_Film: "mm1_Library" = None, mm1_Film10: "mm1_Member" = None):
        self.name = name
        self.mm1_Film = mm1_Film
        self.mm1_Film10 = mm1_Film10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mm1_Film(self):
        return self.__mm1_Film

    @mm1_Film.setter
    def mm1_Film(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm1_Film__mm1_Film", None)
        self.__mm1_Film = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mm1_Library4"):
                opp_val = getattr(old_value, "mm1_Library4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mm1_Library4"):
                opp_val = getattr(value, "mm1_Library4", None)
                if opp_val is None:
                    setattr(value, "mm1_Library4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mm1_Film10(self):
        return self.__mm1_Film10

    @mm1_Film10.setter
    def mm1_Film10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm1_Film__mm1_Film10", None)
        self.__mm1_Film10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mm1_Member9"):
                opp_val = getattr(old_value, "mm1_Member9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mm1_Member9"):
                opp_val = getattr(value, "mm1_Member9", None)
                if opp_val is None:
                    setattr(value, "mm1_Member9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mm1_Library:

    def __init__(self, name: str, mm1_Library4: set["mm1_Film"] = None, mm1_Library: set["mm1_Member"] = None, mm1_Library2: set["mm1_Book"] = None):
        self.name = name
        self.mm1_Library4 = mm1_Library4 if mm1_Library4 is not None else set()
        self.mm1_Library = mm1_Library if mm1_Library is not None else set()
        self.mm1_Library2 = mm1_Library2 if mm1_Library2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mm1_Library(self):
        return self.__mm1_Library

    @mm1_Library.setter
    def mm1_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm1_Library__mm1_Library", None)
        self.__mm1_Library = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mm1_Member"):
                    opp_val = getattr(item, "mm1_Member", None)
                    
                    if opp_val == self:
                        setattr(item, "mm1_Member", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mm1_Member"):
                    opp_val = getattr(item, "mm1_Member", None)
                    
                    setattr(item, "mm1_Member", self)
                    

    @property
    def mm1_Library4(self):
        return self.__mm1_Library4

    @mm1_Library4.setter
    def mm1_Library4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm1_Library__mm1_Library4", None)
        self.__mm1_Library4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mm1_Film"):
                    opp_val = getattr(item, "mm1_Film", None)
                    
                    if opp_val == self:
                        setattr(item, "mm1_Film", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mm1_Film"):
                    opp_val = getattr(item, "mm1_Film", None)
                    
                    setattr(item, "mm1_Film", self)
                    

    @property
    def mm1_Library2(self):
        return self.__mm1_Library2

    @mm1_Library2.setter
    def mm1_Library2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm1_Library__mm1_Library2", None)
        self.__mm1_Library2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mm1_Book"):
                    opp_val = getattr(item, "mm1_Book", None)
                    
                    if opp_val == self:
                        setattr(item, "mm1_Book", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mm1_Book"):
                    opp_val = getattr(item, "mm1_Book", None)
                    
                    setattr(item, "mm1_Book", self)
                    
