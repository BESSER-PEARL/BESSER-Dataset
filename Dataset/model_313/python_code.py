from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class BookCategory(Enum):
    Biography = "Biography"
    Mystery = "Mystery"
    ScienceFiction = "ScienceFiction"


############################################
# Definition of Classes
############################################

class people_library_Car:

    pass
class people_library_Book:

    pass
class library_people_Writer:

    def __init__(self, name: str, author: set["people_library_Book"] = None, library_people_Writer: "people_library_Car" = None):
        self.name = name
        self.author = author if author is not None else set()
        self.library_people_Writer = library_people_Writer
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_people_Writer__author", None)
        self.__author = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Book"):
                    opp_val = getattr(item, "Book", None)
                    
                    if opp_val == self:
                        setattr(item, "Book", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Book"):
                    opp_val = getattr(item, "Book", None)
                    
                    setattr(item, "Book", self)
                    

    @property
    def library_people_Writer(self):
        return self.__library_people_Writer

    @library_people_Writer.setter
    def library_people_Writer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_people_Writer__library_people_Writer", None)
        self.__library_people_Writer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "people_library_Car"):
                opp_val = getattr(old_value, "people_library_Car", None)
                if opp_val == self:
                    setattr(old_value, "people_library_Car", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "people_library_Car"):
                opp_val = getattr(value, "people_library_Car", None)
                setattr(value, "people_library_Car", self)

class Writer:

    pass
class library_Book:

    def __init__(self, title: str, pages: int, category: str, Writer: "Writer" = None, library_Book: "library_Library" = None):
        self.title = title
        self.pages = pages
        self.category = category
        self.Writer = Writer
        self.library_Book = library_Book
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def pages(self) -> int:
        return self.__pages

    @pages.setter
    def pages(self, pages: int):
        self.__pages = pages

    @property
    def category(self) -> str:
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category

    @property
    def Writer(self):
        return self.__Writer

    @Writer.setter
    def Writer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__Writer", None)
        self.__Writer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "people"):
                opp_val = getattr(old_value, "people", None)
                if opp_val == self:
                    setattr(old_value, "people", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "people"):
                opp_val = getattr(value, "people", None)
                setattr(value, "people", self)

    @property
    def library_Book(self):
        return self.__library_Book

    @library_Book.setter
    def library_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__library_Book", None)
        self.__library_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Library4"):
                opp_val = getattr(old_value, "library_Library4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library4"):
                opp_val = getattr(value, "library_Library4", None)
                if opp_val is None:
                    setattr(value, "library_Library4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class library_Library:

    def __init__(self, name: str, library_Library: set["Writer"] = None, library_Library4: set["library_Book"] = None):
        self.name = name
        self.library_Library = library_Library if library_Library is not None else set()
        self.library_Library4 = library_Library4 if library_Library4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
                if hasattr(item, "Writer2"):
                    opp_val = getattr(item, "Writer2", None)
                    
                    if opp_val == self:
                        setattr(item, "Writer2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Writer2"):
                    opp_val = getattr(item, "Writer2", None)
                    
                    setattr(item, "Writer2", self)
                    

    def reserve(self, books: str):
        # TODO: Implement reserve method
        pass
