from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Borrowable:

    pass
class library_CD(Borrowable):

    pass
class library_Magazine(Borrowable):

    pass
class library_Book(Borrowable):

    def __init__(self, author: str):
        self.author = author
        
    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

class library_Customer:

    def __init__(self, name: str, library_Customer: "library_Library" = None, library_Customer3: set["library_Borrowable"] = None):
        self.name = name
        self.library_Customer = library_Customer
        self.library_Customer3 = library_Customer3 if library_Customer3 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def library_Customer(self):
        return self.__library_Customer

    @library_Customer.setter
    def library_Customer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Customer__library_Customer", None)
        self.__library_Customer = value
        
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
    def library_Customer3(self):
        return self.__library_Customer3

    @library_Customer3.setter
    def library_Customer3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Customer__library_Customer3", None)
        self.__library_Customer3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Borrowable"):
                    opp_val = getattr(item, "library_Borrowable", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Borrowable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Borrowable"):
                    opp_val = getattr(item, "library_Borrowable", None)
                    
                    setattr(item, "library_Borrowable", self)
                    

class library_Borrowable(ABC):

    def __init__(self, title: str, copiesAvailable: int, Borrowable: "library_Library" = None, borrowables: "library_Library" = None, library_Borrowable: "library_Customer" = None):
        self.title = title
        self.copiesAvailable = copiesAvailable
        self.Borrowable = Borrowable
        self.borrowables = borrowables
        self.library_Borrowable = library_Borrowable
        
    @property
    def copiesAvailable(self) -> int:
        return self.__copiesAvailable

    @copiesAvailable.setter
    def copiesAvailable(self, copiesAvailable: int):
        self.__copiesAvailable = copiesAvailable

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def library_Borrowable(self):
        return self.__library_Borrowable

    @library_Borrowable.setter
    def library_Borrowable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Borrowable__library_Borrowable", None)
        self.__library_Borrowable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Customer3"):
                opp_val = getattr(old_value, "library_Customer3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Customer3"):
                opp_val = getattr(value, "library_Customer3", None)
                if opp_val is None:
                    setattr(value, "library_Customer3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Borrowable(self):
        return self.__Borrowable

    @Borrowable.setter
    def Borrowable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Borrowable__Borrowable", None)
        self.__Borrowable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library"):
                opp_val = getattr(old_value, "library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library"):
                opp_val = getattr(value, "library", None)
                if opp_val is None:
                    setattr(value, "library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def borrowables(self):
        return self.__borrowables

    @borrowables.setter
    def borrowables(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Borrowable__borrowables", None)
        self.__borrowables = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Library"):
                opp_val = getattr(old_value, "Library", None)
                if opp_val == self:
                    setattr(old_value, "Library", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Library"):
                opp_val = getattr(value, "Library", None)
                setattr(value, "Library", self)

class library_Library:

    def __init__(self, address: str, library: set["library_Borrowable"] = None, Library: "library_Borrowable" = None, library_Library: set["library_Customer"] = None):
        self.address = address
        self.library = library if library is not None else set()
        self.Library = Library
        self.library_Library = library_Library if library_Library is not None else set()
        
    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def library(self):
        return self.__library

    @library.setter
    def library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library", None)
        self.__library = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Borrowable"):
                    opp_val = getattr(item, "Borrowable", None)
                    
                    if opp_val == self:
                        setattr(item, "Borrowable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Borrowable"):
                    opp_val = getattr(item, "Borrowable", None)
                    
                    setattr(item, "Borrowable", self)
                    

    @property
    def Library(self):
        return self.__Library

    @Library.setter
    def Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__Library", None)
        self.__Library = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "borrowables"):
                opp_val = getattr(old_value, "borrowables", None)
                if opp_val == self:
                    setattr(old_value, "borrowables", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "borrowables"):
                opp_val = getattr(value, "borrowables", None)
                setattr(value, "borrowables", self)

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
                if hasattr(item, "library_Customer"):
                    opp_val = getattr(item, "library_Customer", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Customer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Customer"):
                    opp_val = getattr(item, "library_Customer", None)
                    
                    setattr(item, "library_Customer", self)
                    
