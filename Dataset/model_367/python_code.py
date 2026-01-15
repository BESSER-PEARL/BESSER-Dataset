from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Item:

    pass
class CirculatingItem:

    pass
class library_Lendable(ABC):

    def __init__(self, copies: int, borrowing: set["library_Borrower"] = None, Lendable: "library_Borrower" = None):
        self.copies = copies
        self.borrowing = borrowing if borrowing is not None else set()
        self.Lendable = Lendable
        
    @property
    def copies(self) -> int:
        return self.__copies

    @copies.setter
    def copies(self, copies: int):
        self.__copies = copies

    @property
    def Lendable(self):
        return self.__Lendable

    @Lendable.setter
    def Lendable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Lendable__Lendable", None)
        self.__Lendable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "borrowers"):
                opp_val = getattr(old_value, "borrowers", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "borrowers"):
                opp_val = getattr(value, "borrowers", None)
                if opp_val is None:
                    setattr(value, "borrowers", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def borrowing(self):
        return self.__borrowing

    @borrowing.setter
    def borrowing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Lendable__borrowing", None)
        self.__borrowing = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Borrower"):
                    opp_val = getattr(item, "Borrower", None)
                    
                    if opp_val == self:
                        setattr(item, "Borrower", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Borrower"):
                    opp_val = getattr(item, "Borrower", None)
                    
                    setattr(item, "Borrower", self)
                    

class library_IncBook(CirculatingItem):

    def __init__(self, title: str, pages: int, IncBook: "library_Writer" = None, books: set["library_Writer"] = None):
        self.title = title
        self.pages = pages
        self.IncBook = IncBook
        self.books = books if books is not None else set()
        
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
    def IncBook(self):
        return self.__IncBook

    @IncBook.setter
    def IncBook(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_IncBook__IncBook", None)
        self.__IncBook = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "authors"):
                opp_val = getattr(old_value, "authors", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "authors"):
                opp_val = getattr(value, "authors", None)
                if opp_val is None:
                    setattr(value, "authors", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def books(self):
        return self.__books

    @books.setter
    def books(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_IncBook__books", None)
        self.__books = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Writer"):
                    opp_val = getattr(item, "Writer", None)
                    
                    if opp_val == self:
                        setattr(item, "Writer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Writer"):
                    opp_val = getattr(item, "Writer", None)
                    
                    setattr(item, "Writer", self)
                    

class Person:

    pass
class library_Addressable(ABC):

    def __init__(self, address: str):
        self.address = address
        
    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

class Lendable:

    pass
class library_CirculatingItem(Lendable, Item):

    pass
class library_Item(ABC):

    def __init__(self, publicationDate: date, library_Item: "library_Library" = None):
        self.publicationDate = publicationDate
        self.library_Item = library_Item
        
    @property
    def publicationDate(self) -> date:
        return self.__publicationDate

    @publicationDate.setter
    def publicationDate(self, publicationDate: date):
        self.__publicationDate = publicationDate

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
            if hasattr(old_value, "library_Library6"):
                opp_val = getattr(old_value, "library_Library6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library6"):
                opp_val = getattr(value, "library_Library6", None)
                if opp_val is None:
                    setattr(value, "library_Library6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class library_Borrower(Person):

    pass
class library_Employee(Person):

    pass
class library_Writer(Person):

    pass
class Addressable:

    pass
class library_Person(Addressable):

    def __init__(self, firstName: str, lastName: str):
        self.firstName = firstName
        self.lastName = lastName
        
    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

class library_Library(Addressable):

    def __init__(self, name: str, library_Library: set["library_Writer"] = None, library_Library2: set["library_Employee"] = None, library_Library4: set["library_Borrower"] = None, library_Library6: set["library_Item"] = None):
        self.name = name
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
                if hasattr(item, "library_Employee"):
                    opp_val = getattr(item, "library_Employee", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Employee", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Employee"):
                    opp_val = getattr(item, "library_Employee", None)
                    
                    setattr(item, "library_Employee", self)
                    

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
                if hasattr(item, "library_Borrower"):
                    opp_val = getattr(item, "library_Borrower", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Borrower", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Borrower"):
                    opp_val = getattr(item, "library_Borrower", None)
                    
                    setattr(item, "library_Borrower", self)
                    
