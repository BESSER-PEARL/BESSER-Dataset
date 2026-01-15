from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class library_Book:

    pass
class library_BookCopy:

    def __init__(self, copies: int, library_BookCopy: "library_Library" = None, library_BookCopy2: "library_Book" = None):
        self.copies = copies
        self.library_BookCopy = library_BookCopy
        self.library_BookCopy2 = library_BookCopy2
        
    @property
    def copies(self) -> int:
        return self.__copies

    @copies.setter
    def copies(self, copies: int):
        self.__copies = copies

    @property
    def library_BookCopy(self):
        return self.__library_BookCopy

    @library_BookCopy.setter
    def library_BookCopy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_BookCopy__library_BookCopy", None)
        self.__library_BookCopy = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Library"):
                opp_val = getattr(old_value, "library_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library"):
                opp_val = getattr(value, "library_Library", None)
                if opp_val is None:
                    setattr(value, "library_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_BookCopy2(self):
        return self.__library_BookCopy2

    @library_BookCopy2.setter
    def library_BookCopy2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_BookCopy__library_BookCopy2", None)
        self.__library_BookCopy2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Book"):
                opp_val = getattr(old_value, "library_Book", None)
                if opp_val == self:
                    setattr(old_value, "library_Book", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Book"):
                opp_val = getattr(value, "library_Book", None)
                setattr(value, "library_Book", self)

class library_Library:

    def __init__(self, name: str, library_Library: set["library_BookCopy"] = None):
        self.name = name
        self.library_Library = library_Library if library_Library is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def library_Library(self):
        return self.__library_Library

    @library_Library.setter
    def library_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library", None)
        self.__library_Library = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_BookCopy"):
                    opp_val = getattr(item, "library_BookCopy", None)
                    
                    if opp_val == self:
                        setattr(item, "library_BookCopy", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_BookCopy"):
                    opp_val = getattr(item, "library_BookCopy", None)
                    
                    setattr(item, "library_BookCopy", self)
                    
