from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class mm2_Loan:

    pass
class mm2_Book:

    def __init__(self, name: str, mm2_Book: "mm2_Library" = None, mm2_Book7: "mm2_Loan" = None):
        self.name = name
        self.mm2_Book = mm2_Book
        self.mm2_Book7 = mm2_Book7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mm2_Book7(self):
        return self.__mm2_Book7

    @mm2_Book7.setter
    def mm2_Book7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm2_Book__mm2_Book7", None)
        self.__mm2_Book7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mm2_Loan6"):
                opp_val = getattr(old_value, "mm2_Loan6", None)
                if opp_val == self:
                    setattr(old_value, "mm2_Loan6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mm2_Loan6"):
                opp_val = getattr(value, "mm2_Loan6", None)
                setattr(value, "mm2_Loan6", self)

    @property
    def mm2_Book(self):
        return self.__mm2_Book

    @mm2_Book.setter
    def mm2_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm2_Book__mm2_Book", None)
        self.__mm2_Book = value
        
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

class mm2_Member:

    def __init__(self, name: str, mm2_Member: "mm2_Library" = None, mm2_Member10: "mm2_Loan" = None):
        self.name = name
        self.mm2_Member = mm2_Member
        self.mm2_Member10 = mm2_Member10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mm2_Member10(self):
        return self.__mm2_Member10

    @mm2_Member10.setter
    def mm2_Member10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mm2_Member__mm2_Member10", None)
        self.__mm2_Member10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mm2_Loan9"):
                opp_val = getattr(old_value, "mm2_Loan9", None)
                if opp_val == self:
                    setattr(old_value, "mm2_Loan9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mm2_Loan9"):
                opp_val = getattr(value, "mm2_Loan9", None)
                setattr(value, "mm2_Loan9", self)

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

class mm2_Library:

    def __init__(self, name: str, mm2_Library: set["mm2_Member"] = None, mm2_Library2: set["mm2_Book"] = None, mm2_Library4: set["mm2_Loan"] = None):
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
                if hasattr(item, "mm2_Book"):
                    opp_val = getattr(item, "mm2_Book", None)
                    
                    if opp_val == self:
                        setattr(item, "mm2_Book", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mm2_Book"):
                    opp_val = getattr(item, "mm2_Book", None)
                    
                    setattr(item, "mm2_Book", self)
                    

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
                if hasattr(item, "mm2_Loan"):
                    opp_val = getattr(item, "mm2_Loan", None)
                    
                    if opp_val == self:
                        setattr(item, "mm2_Loan", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "mm2_Loan"):
                    opp_val = getattr(item, "mm2_Loan", None)
                    
                    setattr(item, "mm2_Loan", self)
                    

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
                    
