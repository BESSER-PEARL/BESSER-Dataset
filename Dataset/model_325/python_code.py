from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class BookCategory(Enum):
    ScienceFiction = "ScienceFiction"
    Biographie = "Biographie"
    Mistery = "Mistery"


############################################
# Definition of Classes
############################################

class library_Book:

    def __init__(self, category: str, title: str, pages: int, library_Book: set["library__cPfTBB9KEeeOINGRvT6ccg"] = None):
        self.category = category
        self.title = title
        self.pages = pages
        self.library_Book = library_Book if library_Book is not None else set()
        
    @property
    def category(self) -> str:
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category

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
    def library_Book(self):
        return self.__library_Book

    @library_Book.setter
    def library_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__library_Book", None)
        self.__library_Book = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library__cPfTBB9KEeeOINGRvT6ccg11"):
                    opp_val = getattr(item, "library__cPfTBB9KEeeOINGRvT6ccg11", None)
                    
                    if opp_val == self:
                        setattr(item, "library__cPfTBB9KEeeOINGRvT6ccg11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library__cPfTBB9KEeeOINGRvT6ccg11"):
                    opp_val = getattr(item, "library__cPfTBB9KEeeOINGRvT6ccg11", None)
                    
                    setattr(item, "library__cPfTBB9KEeeOINGRvT6ccg11", self)
                    

class library_Writer:

    def __init__(self, name: str, library_Writer: set["library__cPfTDx9KEeeOINGRvT6ccg"] = None):
        self.name = name
        self.library_Writer = library_Writer if library_Writer is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def library_Writer(self):
        return self.__library_Writer

    @library_Writer.setter
    def library_Writer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Writer__library_Writer", None)
        self.__library_Writer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library__cPfTDx9KEeeOINGRvT6ccg9"):
                    opp_val = getattr(item, "library__cPfTDx9KEeeOINGRvT6ccg9", None)
                    
                    if opp_val == self:
                        setattr(item, "library__cPfTDx9KEeeOINGRvT6ccg9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library__cPfTDx9KEeeOINGRvT6ccg9"):
                    opp_val = getattr(item, "library__cPfTDx9KEeeOINGRvT6ccg9", None)
                    
                    setattr(item, "library__cPfTDx9KEeeOINGRvT6ccg9", self)
                    

class library__cPfTDx9KEeeOINGRvT6ccg:

    pass
class library__cPfTBB9KEeeOINGRvT6ccg:

    pass
class library_Library:

    def __init__(self, name: str, address: str, ages: int, library_Library: set["library__cPfS4h9KEeeOINGRvT6ccg"] = None, library_Library2: set["library__cPfTBB9KEeeOINGRvT6ccg"] = None, library_Library4: set["library__cPfTDx9KEeeOINGRvT6ccg"] = None, library_Library6: set["library__cPfS4h9KEeeOINGRvT6ccg"] = None):
        self.name = name
        self.address = address
        self.ages = ages
        self.library_Library = library_Library if library_Library is not None else set()
        self.library_Library2 = library_Library2 if library_Library2 is not None else set()
        self.library_Library4 = library_Library4 if library_Library4 is not None else set()
        self.library_Library6 = library_Library6 if library_Library6 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ages(self) -> int:
        return self.__ages

    @ages.setter
    def ages(self, ages: int):
        self.__ages = ages

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def library_Library6(self):
        return self.__library_Library6

    @library_Library6.setter
    def library_Library6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library6", None)
        self.__library_Library6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library__cPfS4h9KEeeOINGRvT6ccg7"):
                    opp_val = getattr(item, "library__cPfS4h9KEeeOINGRvT6ccg7", None)
                    
                    if opp_val == self:
                        setattr(item, "library__cPfS4h9KEeeOINGRvT6ccg7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library__cPfS4h9KEeeOINGRvT6ccg7"):
                    opp_val = getattr(item, "library__cPfS4h9KEeeOINGRvT6ccg7", None)
                    
                    setattr(item, "library__cPfS4h9KEeeOINGRvT6ccg7", self)
                    

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
                if hasattr(item, "library__cPfTBB9KEeeOINGRvT6ccg"):
                    opp_val = getattr(item, "library__cPfTBB9KEeeOINGRvT6ccg", None)
                    
                    if opp_val == self:
                        setattr(item, "library__cPfTBB9KEeeOINGRvT6ccg", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library__cPfTBB9KEeeOINGRvT6ccg"):
                    opp_val = getattr(item, "library__cPfTBB9KEeeOINGRvT6ccg", None)
                    
                    setattr(item, "library__cPfTBB9KEeeOINGRvT6ccg", self)
                    

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
                if hasattr(item, "library__cPfS4h9KEeeOINGRvT6ccg"):
                    opp_val = getattr(item, "library__cPfS4h9KEeeOINGRvT6ccg", None)
                    
                    if opp_val == self:
                        setattr(item, "library__cPfS4h9KEeeOINGRvT6ccg", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library__cPfS4h9KEeeOINGRvT6ccg"):
                    opp_val = getattr(item, "library__cPfS4h9KEeeOINGRvT6ccg", None)
                    
                    setattr(item, "library__cPfS4h9KEeeOINGRvT6ccg", self)
                    

    @property
    def library_Library4(self):
        return self.__library_Library4

    @library_Library4.setter
    def library_Library4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library4", None)
        self.__library_Library4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library__cPfTDx9KEeeOINGRvT6ccg"):
                    opp_val = getattr(item, "library__cPfTDx9KEeeOINGRvT6ccg", None)
                    
                    if opp_val == self:
                        setattr(item, "library__cPfTDx9KEeeOINGRvT6ccg", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library__cPfTDx9KEeeOINGRvT6ccg"):
                    opp_val = getattr(item, "library__cPfTDx9KEeeOINGRvT6ccg", None)
                    
                    setattr(item, "library__cPfTDx9KEeeOINGRvT6ccg", self)
                    

class library_Employee:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age

class library__cPfS4h9KEeeOINGRvT6ccg:

    pass