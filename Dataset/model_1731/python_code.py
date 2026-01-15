from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Item:

    pass
class library_Book(Item):

    def __init__(self, numPages: int):
        self.numPages = numPages
        
    @property
    def numPages(self) -> int:
        return self.__numPages

    @numPages.setter
    def numPages(self, numPages: int):
        self.__numPages = numPages

class library_Item(ABC):

    def __init__(self, title: str, pubDate: date, library_Item: "library_LibraryShelf" = None):
        self.title = title
        self.pubDate = pubDate
        self.library_Item = library_Item
        
    @property
    def pubDate(self) -> date:
        return self.__pubDate

    @pubDate.setter
    def pubDate(self, pubDate: date):
        self.__pubDate = pubDate

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def library_Item(self):
        return self.__library_Item

    @library_Item.setter
    def library_Item(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Item__library_Item", None)
        self.__library_Item = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_LibraryShelf"):
                opp_val = getattr(old_value, "library_LibraryShelf", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_LibraryShelf"):
                opp_val = getattr(value, "library_LibraryShelf", None)
                if opp_val is None:
                    setattr(value, "library_LibraryShelf", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class library_LibraryShelf:

    def __init__(self, name: str, library_LibraryShelf: set["library_Item"] = None):
        self.name = name
        self.library_LibraryShelf = library_LibraryShelf if library_LibraryShelf is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def library_LibraryShelf(self):
        return self.__library_LibraryShelf

    @library_LibraryShelf.setter
    def library_LibraryShelf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_LibraryShelf__library_LibraryShelf", None)
        self.__library_LibraryShelf = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Item"):
                    opp_val = getattr(item, "library_Item", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Item", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Item"):
                    opp_val = getattr(item, "library_Item", None)
                    
                    setattr(item, "library_Item", self)
                    

class MultimediaItem:

    pass
class library_BlueRay(MultimediaItem):

    pass
class library_CD(MultimediaItem):

    pass
class library_DVD(MultimediaItem):

    pass
class library_MultimediaItem(Item):

    def __init__(self, length: float):
        self.length = length
        
    @property
    def length(self) -> float:
        return self.__length

    @length.setter
    def length(self, length: float):
        self.__length = length
