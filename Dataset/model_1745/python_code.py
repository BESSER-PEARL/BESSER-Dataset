from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class LibraryContent:

    pass
class library_Magazine(LibraryContent):

    pass
class library_Book(LibraryContent):

    pass
class library_LibraryContent(ABC):

    def __init__(self, name: str, author: str, library_LibraryContent: "library_Library" = None):
        self.name = name
        self.author = author
        self.library_LibraryContent = library_LibraryContent
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def library_LibraryContent(self):
        return self.__library_LibraryContent

    @library_LibraryContent.setter
    def library_LibraryContent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_LibraryContent__library_LibraryContent", None)
        self.__library_LibraryContent = value
        
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

class library_Library:

    def __init__(self, name: str, library_Library: set["library_LibraryContent"] = None):
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
                if hasattr(item, "library_LibraryContent"):
                    opp_val = getattr(item, "library_LibraryContent", None)
                    
                    if opp_val == self:
                        setattr(item, "library_LibraryContent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_LibraryContent"):
                    opp_val = getattr(item, "library_LibraryContent", None)
                    
                    setattr(item, "library_LibraryContent", self)
                    
