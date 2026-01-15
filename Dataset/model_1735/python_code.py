from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class library_Library:

    def __init__(self, name: str, library_Library: set["library_Writer"] = None, library_Library2: set["library_Book"] = None):
        self.name = name
        self.library_Library = library_Library if library_Library is not None else set()
        self.library_Library2 = library_Library2 if library_Library2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def library_Library2(self):
        return self.__library_Library2

    @library_Library2.setter
    def library_Library2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library2", None)
        self.__library_Library2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Book"):
                    opp_val = getattr(item, "library_Book", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Book", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Book"):
                    opp_val = getattr(item, "library_Book", None)
                    
                    setattr(item, "library_Book", self)
                    

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
                if hasattr(item, "library_Writer"):
                    opp_val = getattr(item, "library_Writer", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Writer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Writer"):
                    opp_val = getattr(item, "library_Writer", None)
                    
                    setattr(item, "library_Writer", self)
                    

class library_Book:

    pass
class library_Writer:

    pass