from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class BibText_BibTextFile:

    pass
class BibText_LocatedElement(ABC):

    def __init__(self, location: str):
        self.location = location
        
        pass
    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location


class Attribute:

    pass
class BibText_Year(Attribute):

    pass
class BibTextEntry:

    pass
class BibText_Author(BibTextEntry):

    def __init__(self, name: str, Author: "BibText_Article" = None, author: set["BibText_Article"] = None):
        self.name = name
        self.Author = Author
        self.author = author if author is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def Author(self):
        return self.__Author

    @Author.setter
    def Author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BibText_Author__Author", None)
        self.__Author = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "articles"):
                opp_val = getattr(old_value, "articles", None)
                if opp_val == self:
                    setattr(old_value, "articles", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "articles"):
                opp_val = getattr(value, "articles", None)
                setattr(value, "articles", self)

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BibText_Author__author", None)
        self.__author = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Article"):
                    opp_val = getattr(item, "Article", None)
                    
                    if opp_val == self:
                        setattr(item, "Article", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Article"):
                    opp_val = getattr(item, "Article", None)
                    
                    setattr(item, "Article", self)
                    

class BibText_Article(BibTextEntry):

    pass
class LocatedElement:

    pass
class BibText_Attribute(LocatedElement):

    def __init__(self, value: str, BibText_Attribute: "BibText_BibTextEntry" = None):
        self.value = value
        self.BibText_Attribute = BibText_Attribute
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def BibText_Attribute(self):
        return self.__BibText_Attribute

    @BibText_Attribute.setter
    def BibText_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BibText_Attribute__BibText_Attribute", None)
        self.__BibText_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BibText_BibTextEntry2"):
                opp_val = getattr(old_value, "BibText_BibTextEntry2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BibText_BibTextEntry2"):
                opp_val = getattr(value, "BibText_BibTextEntry2", None)
                if opp_val is None:
                    setattr(value, "BibText_BibTextEntry2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class BibText_BibTextEntry(LocatedElement):

    def __init__(self, key: str, BibText_BibTextEntry2: set["BibText_Attribute"] = None, BibText_BibTextEntry: "BibText_BibTextFile" = None):
        self.key = key
        self.BibText_BibTextEntry2 = BibText_BibTextEntry2 if BibText_BibTextEntry2 is not None else set()
        self.BibText_BibTextEntry = BibText_BibTextEntry
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def BibText_BibTextEntry(self):
        return self.__BibText_BibTextEntry

    @BibText_BibTextEntry.setter
    def BibText_BibTextEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BibText_BibTextEntry__BibText_BibTextEntry", None)
        self.__BibText_BibTextEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BibText_BibTextFile"):
                opp_val = getattr(old_value, "BibText_BibTextFile", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BibText_BibTextFile"):
                opp_val = getattr(value, "BibText_BibTextFile", None)
                if opp_val is None:
                    setattr(value, "BibText_BibTextFile", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def BibText_BibTextEntry2(self):
        return self.__BibText_BibTextEntry2

    @BibText_BibTextEntry2.setter
    def BibText_BibTextEntry2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BibText_BibTextEntry__BibText_BibTextEntry2", None)
        self.__BibText_BibTextEntry2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BibText_Attribute"):
                    opp_val = getattr(item, "BibText_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "BibText_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BibText_Attribute"):
                    opp_val = getattr(item, "BibText_Attribute", None)
                    
                    setattr(item, "BibText_Attribute", self)
                    
