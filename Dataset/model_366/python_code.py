from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class BookCategory(Enum):
    SciFi = "SciFi"
    Biography = "Biography"
    GeneralFiction = "GeneralFiction"
    NonFiction = "NonFiction"


############################################
# Definition of Classes
############################################

class lib_LibSys:

    pass
class lib_Book:

    def __init__(self, title: str, pages: int, category: str, lib_Book: "lib_Library" = None, lib_Book4: "lib_Writer" = None):
        self.title = title
        self.pages = pages
        self.category = category
        self.lib_Book = lib_Book
        self.lib_Book4 = lib_Book4
        
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
    def lib_Book4(self):
        return self.__lib_Book4

    @lib_Book4.setter
    def lib_Book4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lib_Book__lib_Book4", None)
        self.__lib_Book4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lib_Writer5"):
                opp_val = getattr(old_value, "lib_Writer5", None)
                if opp_val == self:
                    setattr(old_value, "lib_Writer5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lib_Writer5"):
                opp_val = getattr(value, "lib_Writer5", None)
                setattr(value, "lib_Writer5", self)

    @property
    def lib_Book(self):
        return self.__lib_Book

    @lib_Book.setter
    def lib_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lib_Book__lib_Book", None)
        self.__lib_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lib_Library2"):
                opp_val = getattr(old_value, "lib_Library2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lib_Library2"):
                opp_val = getattr(value, "lib_Library2", None)
                if opp_val is None:
                    setattr(value, "lib_Library2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class lib_Writer:

    def __init__(self, name: str, lib_Writer: "lib_Library" = None, lib_Writer5: "lib_Book" = None):
        self.name = name
        self.lib_Writer = lib_Writer
        self.lib_Writer5 = lib_Writer5
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def lib_Writer5(self):
        return self.__lib_Writer5

    @lib_Writer5.setter
    def lib_Writer5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lib_Writer__lib_Writer5", None)
        self.__lib_Writer5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lib_Book4"):
                opp_val = getattr(old_value, "lib_Book4", None)
                if opp_val == self:
                    setattr(old_value, "lib_Book4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lib_Book4"):
                opp_val = getattr(value, "lib_Book4", None)
                setattr(value, "lib_Book4", self)

    @property
    def lib_Writer(self):
        return self.__lib_Writer

    @lib_Writer.setter
    def lib_Writer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lib_Writer__lib_Writer", None)
        self.__lib_Writer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lib_Library"):
                opp_val = getattr(old_value, "lib_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lib_Library"):
                opp_val = getattr(value, "lib_Library", None)
                if opp_val is None:
                    setattr(value, "lib_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class lib_Library:

    def __init__(self, name: str, location: str, lib_Library2: set["lib_Book"] = None, lib_Library: set["lib_Writer"] = None, lib_Library7: "lib_LibSys" = None):
        self.name = name
        self.location = location
        self.lib_Library2 = lib_Library2 if lib_Library2 is not None else set()
        self.lib_Library = lib_Library if lib_Library is not None else set()
        self.lib_Library7 = lib_Library7
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def lib_Library7(self):
        return self.__lib_Library7

    @lib_Library7.setter
    def lib_Library7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lib_Library__lib_Library7", None)
        self.__lib_Library7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lib_LibSys"):
                opp_val = getattr(old_value, "lib_LibSys", None)
                if opp_val == self:
                    setattr(old_value, "lib_LibSys", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lib_LibSys"):
                opp_val = getattr(value, "lib_LibSys", None)
                setattr(value, "lib_LibSys", self)

    @property
    def lib_Library2(self):
        return self.__lib_Library2

    @lib_Library2.setter
    def lib_Library2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lib_Library__lib_Library2", None)
        self.__lib_Library2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lib_Book"):
                    opp_val = getattr(item, "lib_Book", None)
                    
                    if opp_val == self:
                        setattr(item, "lib_Book", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lib_Book"):
                    opp_val = getattr(item, "lib_Book", None)
                    
                    setattr(item, "lib_Book", self)
                    

    @property
    def lib_Library(self):
        return self.__lib_Library

    @lib_Library.setter
    def lib_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lib_Library__lib_Library", None)
        self.__lib_Library = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lib_Writer"):
                    opp_val = getattr(item, "lib_Writer", None)
                    
                    if opp_val == self:
                        setattr(item, "lib_Writer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lib_Writer"):
                    opp_val = getattr(item, "lib_Writer", None)
                    
                    setattr(item, "lib_Writer", self)
                    
