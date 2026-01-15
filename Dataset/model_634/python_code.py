from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class mm1_Book:

    def __init__(self, name: str, mm1_Book: "mm1_Library" = None, mm1_Book5: "mm1_Member" = None):
        self.name = name
        self.mm1_Book = mm1_Book
        self.mm1_Book5 = mm1_Book5
        
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
    def mm1_Book5(self):
        return self.__mm1_Book5

    @mm1_Book5.setter
    def mm1_Book5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm1_Book__mm1_Book5", None)
        self.__mm1_Book5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mm1_Member4"):
                opp_val = getattr(old_value, "mm1_Member4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mm1_Member4"):
                opp_val = getattr(value, "mm1_Member4", None)
                if opp_val is None:
                    setattr(value, "mm1_Member4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mm1_Member:

    def __init__(self, name: str, mm1_Member: "mm1_Library" = None, mm1_Member4: set["mm1_Book"] = None):
        self.name = name
        self.mm1_Member = mm1_Member
        self.mm1_Member4 = mm1_Member4 if mm1_Member4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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

    @property
    def mm1_Member4(self):
        return self.__mm1_Member4

    @mm1_Member4.setter
    def mm1_Member4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm1_Member__mm1_Member4", None)
        self.__mm1_Member4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "mm1_Book5"):
                    opp_val = getattr(item, "mm1_Book5", None)
                    
                    if opp_val == self:
                        setattr(item, "mm1_Book5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mm1_Book5"):
                    opp_val = getattr(item, "mm1_Book5", None)
                    
                    setattr(item, "mm1_Book5", self)
                    

class mm1_Library:

    def __init__(self, name: str, mm1_Library: set["mm1_Member"] = None, mm1_Library2: set["mm1_Book"] = None):
        self.name = name
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
                    
