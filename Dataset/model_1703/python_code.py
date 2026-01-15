from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class AnnotationColor(Enum):
    Yellow = "Yellow"
    Green = "Green"
    Blue = "Blue"
    Red = "Red"
    Purple = "Purple"
    Underline = "Underline"


############################################
# Definition of Classes
############################################

class Bookmark:

    pass
class library_Metadata:

    def __init__(self, key: str, value: str, library_Metadata: "library_Book" = None):
        self.key = key
        self.value = value
        self.library_Metadata = library_Metadata
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def library_Metadata(self):
        return self.__library_Metadata

    @library_Metadata.setter
    def library_Metadata(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Metadata__library_Metadata", None)
        self.__library_Metadata = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Book4"):
                opp_val = getattr(old_value, "library_Book4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Book4"):
                opp_val = getattr(value, "library_Book4", None)
                if opp_val is None:
                    setattr(value, "library_Book4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class library_TextAnnotation(Bookmark):

    def __init__(self, color: str, comment: str):
        self.color = color
        self.comment = comment
        
    @property
    def comment(self) -> str:
        return self.__comment

    @comment.setter
    def comment(self, comment: str):
        self.__comment = comment

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str):
        self.__color = color

class library_Book:

    def __init__(self, bookURN: str, bookURL: str, collection: str, title: str, author: str, lastHref: str, lastLocation: str, lastOpened: str, library_Book2: set["library_Bookmark"] = None, library_Book: "library_Library" = None, library_Book4: set["library_Metadata"] = None):
        self.bookURN = bookURN
        self.bookURL = bookURL
        self.collection = collection
        self.title = title
        self.author = author
        self.lastHref = lastHref
        self.lastLocation = lastLocation
        self.lastOpened = lastOpened
        self.library_Book2 = library_Book2 if library_Book2 is not None else set()
        self.library_Book = library_Book
        self.library_Book4 = library_Book4 if library_Book4 is not None else set()
        
    @property
    def bookURN(self) -> str:
        return self.__bookURN

    @bookURN.setter
    def bookURN(self, bookURN: str):
        self.__bookURN = bookURN

    @property
    def lastLocation(self) -> str:
        return self.__lastLocation

    @lastLocation.setter
    def lastLocation(self, lastLocation: str):
        self.__lastLocation = lastLocation

    @property
    def lastHref(self) -> str:
        return self.__lastHref

    @lastHref.setter
    def lastHref(self, lastHref: str):
        self.__lastHref = lastHref

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def collection(self) -> str:
        return self.__collection

    @collection.setter
    def collection(self, collection: str):
        self.__collection = collection

    @property
    def bookURL(self) -> str:
        return self.__bookURL

    @bookURL.setter
    def bookURL(self, bookURL: str):
        self.__bookURL = bookURL

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def lastOpened(self) -> str:
        return self.__lastOpened

    @lastOpened.setter
    def lastOpened(self, lastOpened: str):
        self.__lastOpened = lastOpened

    @property
    def library_Book4(self):
        return self.__library_Book4

    @library_Book4.setter
    def library_Book4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__library_Book4", None)
        self.__library_Book4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Metadata"):
                    opp_val = getattr(item, "library_Metadata", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Metadata", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Metadata"):
                    opp_val = getattr(item, "library_Metadata", None)
                    
                    setattr(item, "library_Metadata", self)
                    

    @property
    def library_Book2(self):
        return self.__library_Book2

    @library_Book2.setter
    def library_Book2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__library_Book2", None)
        self.__library_Book2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Bookmark"):
                    opp_val = getattr(item, "library_Bookmark", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Bookmark", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Bookmark"):
                    opp_val = getattr(item, "library_Bookmark", None)
                    
                    setattr(item, "library_Bookmark", self)
                    

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

class library_Bookmark:

    def __init__(self, id: str, location: str, page: int, href: str, timestamp: date, text: str, library_Bookmark: "library_Book" = None):
        self.id = id
        self.location = location
        self.page = page
        self.href = href
        self.timestamp = timestamp
        self.text = text
        self.library_Bookmark = library_Bookmark
        
    @property
    def page(self) -> int:
        return self.__page

    @page.setter
    def page(self, page: int):
        self.__page = page

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def timestamp(self) -> date:
        return self.__timestamp

    @timestamp.setter
    def timestamp(self, timestamp: date):
        self.__timestamp = timestamp

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def href(self) -> str:
        return self.__href

    @href.setter
    def href(self, href: str):
        self.__href = href

    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def library_Bookmark(self):
        return self.__library_Bookmark

    @library_Bookmark.setter
    def library_Bookmark(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Bookmark__library_Bookmark", None)
        self.__library_Bookmark = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Book2"):
                opp_val = getattr(old_value, "library_Book2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Book2"):
                opp_val = getattr(value, "library_Book2", None)
                if opp_val is None:
                    setattr(value, "library_Book2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class library_Library:

    def __init__(self, version: str, library_Library: set["library_Book"] = None):
        self.version = version
        self.library_Library = library_Library if library_Library is not None else set()
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

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
                    
