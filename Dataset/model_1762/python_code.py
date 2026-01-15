from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class BookType(Enum):
    Child = "Child"
    Parent = "Parent"


############################################
# Definition of Classes
############################################

class emftest_Library:

    pass
class Book:

    pass
class emftest_ChildBook(Book):

    pass
class emftest_Author:

    def __init__(self, name: str, emftest_Author: "emftest_Book" = None, emftest_Author6: set["emftest_Book"] = None):
        self.name = name
        self.emftest_Author = emftest_Author
        self.emftest_Author6 = emftest_Author6 if emftest_Author6 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def emftest_Author6(self):
        return self.__emftest_Author6

    @emftest_Author6.setter
    def emftest_Author6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emftest_Author__emftest_Author6", None)
        self.__emftest_Author6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "emftest_Book7"):
                    opp_val = getattr(item, "emftest_Book7", None)
                    
                    if opp_val == self:
                        setattr(item, "emftest_Book7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "emftest_Book7"):
                    opp_val = getattr(item, "emftest_Book7", None)
                    
                    setattr(item, "emftest_Book7", self)
                    

    @property
    def emftest_Author(self):
        return self.__emftest_Author

    @emftest_Author.setter
    def emftest_Author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emftest_Author__emftest_Author", None)
        self.__emftest_Author = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emftest_Book"):
                opp_val = getattr(old_value, "emftest_Book", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emftest_Book"):
                opp_val = getattr(value, "emftest_Book", None)
                if opp_val is None:
                    setattr(value, "emftest_Book", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def writeBook(self, pages: int, title: str, type: str) -> Book:
        # TODO: Implement writeBook method
        pass

class emftest_Book(ABC):

    def __init__(self, title: str, pages: int, emftest_Book2: "emftest_BookCollection" = None, emftest_Book: set["emftest_Author"] = None, emftest_Book7: "emftest_Author" = None):
        self.title = title
        self.pages = pages
        self.emftest_Book2 = emftest_Book2
        self.emftest_Book = emftest_Book if emftest_Book is not None else set()
        self.emftest_Book7 = emftest_Book7
        
    @property
    def pages(self) -> int:
        return self.__pages

    @pages.setter
    def pages(self, pages: int):
        self.__pages = pages

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def emftest_Book7(self):
        return self.__emftest_Book7

    @emftest_Book7.setter
    def emftest_Book7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emftest_Book__emftest_Book7", None)
        self.__emftest_Book7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emftest_Author6"):
                opp_val = getattr(old_value, "emftest_Author6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emftest_Author6"):
                opp_val = getattr(value, "emftest_Author6", None)
                if opp_val is None:
                    setattr(value, "emftest_Author6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def emftest_Book(self):
        return self.__emftest_Book

    @emftest_Book.setter
    def emftest_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emftest_Book__emftest_Book", None)
        self.__emftest_Book = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "emftest_Author"):
                    opp_val = getattr(item, "emftest_Author", None)
                    
                    if opp_val == self:
                        setattr(item, "emftest_Author", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "emftest_Author"):
                    opp_val = getattr(item, "emftest_Author", None)
                    
                    setattr(item, "emftest_Author", self)
                    

    @property
    def emftest_Book2(self):
        return self.__emftest_Book2

    @emftest_Book2.setter
    def emftest_Book2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_emftest_Book__emftest_Book2", None)
        self.__emftest_Book2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "emftest_BookCollection"):
                opp_val = getattr(old_value, "emftest_BookCollection", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "emftest_BookCollection"):
                opp_val = getattr(value, "emftest_BookCollection", None)
                if opp_val is None:
                    setattr(value, "emftest_BookCollection", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class emftest_BookCollection:

    pass
class emftest_ParentBook(Book):

    pass