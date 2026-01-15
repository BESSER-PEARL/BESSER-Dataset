from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class BookCategory(Enum):
    Drama = "Drama"
    History = "History"
    Art = "Art"
    SciFi = "SciFi"


############################################
# Definition of Classes
############################################

class eiqlibrary_Book:

    def __init__(self, title: str, pages: int, category: str, eiqlibrary_Book13: "eiqlibrary_Writer" = None, eiqlibrary_Book: "eiqlibrary_Library" = None, eiqlibrary_Book5: "eiqlibrary_Library" = None, books: set["eiqlibrary_Writer"] = None, Book: "eiqlibrary_Writer" = None, eiqlibrary_Book10: "eiqlibrary_Writer" = None):
        self.title = title
        self.pages = pages
        self.category = category
        self.eiqlibrary_Book13 = eiqlibrary_Book13
        self.eiqlibrary_Book = eiqlibrary_Book
        self.eiqlibrary_Book5 = eiqlibrary_Book5
        self.books = books if books is not None else set()
        self.Book = Book
        self.eiqlibrary_Book10 = eiqlibrary_Book10
        
    @property
    def category(self) -> str:
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category

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
    def eiqlibrary_Book(self):
        return self.__eiqlibrary_Book

    @eiqlibrary_Book.setter
    def eiqlibrary_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eiqlibrary_Book__eiqlibrary_Book", None)
        self.__eiqlibrary_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eiqlibrary_Library2"):
                opp_val = getattr(old_value, "eiqlibrary_Library2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eiqlibrary_Library2"):
                opp_val = getattr(value, "eiqlibrary_Library2", None)
                if opp_val is None:
                    setattr(value, "eiqlibrary_Library2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eiqlibrary_Book13(self):
        return self.__eiqlibrary_Book13

    @eiqlibrary_Book13.setter
    def eiqlibrary_Book13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eiqlibrary_Book__eiqlibrary_Book13", None)
        self.__eiqlibrary_Book13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eiqlibrary_Writer12"):
                opp_val = getattr(old_value, "eiqlibrary_Writer12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eiqlibrary_Writer12"):
                opp_val = getattr(value, "eiqlibrary_Writer12", None)
                if opp_val is None:
                    setattr(value, "eiqlibrary_Writer12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eiqlibrary_Book5(self):
        return self.__eiqlibrary_Book5

    @eiqlibrary_Book5.setter
    def eiqlibrary_Book5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eiqlibrary_Book__eiqlibrary_Book5", None)
        self.__eiqlibrary_Book5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eiqlibrary_Library4"):
                opp_val = getattr(old_value, "eiqlibrary_Library4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eiqlibrary_Library4"):
                opp_val = getattr(value, "eiqlibrary_Library4", None)
                if opp_val is None:
                    setattr(value, "eiqlibrary_Library4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def books(self):
        return self.__books

    @books.setter
    def books(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eiqlibrary_Book__books", None)
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
                    

    @property
    def Book(self):
        return self.__Book

    @Book.setter
    def Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eiqlibrary_Book__Book", None)
        self.__Book = value
        
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
    def eiqlibrary_Book10(self):
        return self.__eiqlibrary_Book10

    @eiqlibrary_Book10.setter
    def eiqlibrary_Book10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eiqlibrary_Book__eiqlibrary_Book10", None)
        self.__eiqlibrary_Book10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eiqlibrary_Writer9"):
                opp_val = getattr(old_value, "eiqlibrary_Writer9", None)
                if opp_val == self:
                    setattr(old_value, "eiqlibrary_Writer9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eiqlibrary_Writer9"):
                opp_val = getattr(value, "eiqlibrary_Writer9", None)
                setattr(value, "eiqlibrary_Writer9", self)

class eiqlibrary_Writer:

    def __init__(self, name: str, eiqlibrary_Writer: "eiqlibrary_Library" = None, eiqlibrary_Writer12: set["eiqlibrary_Book"] = None, Writer: "eiqlibrary_Book" = None, authors: set["eiqlibrary_Book"] = None, eiqlibrary_Writer9: "eiqlibrary_Book" = None):
        self.name = name
        self.eiqlibrary_Writer = eiqlibrary_Writer
        self.eiqlibrary_Writer12 = eiqlibrary_Writer12 if eiqlibrary_Writer12 is not None else set()
        self.Writer = Writer
        self.authors = authors if authors is not None else set()
        self.eiqlibrary_Writer9 = eiqlibrary_Writer9
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eiqlibrary_Writer__authors", None)
        self.__authors = value if value is not None else set()
        
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
    def Writer(self):
        return self.__Writer

    @Writer.setter
    def Writer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eiqlibrary_Writer__Writer", None)
        self.__Writer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "books"):
                opp_val = getattr(old_value, "books", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "books"):
                opp_val = getattr(value, "books", None)
                if opp_val is None:
                    setattr(value, "books", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eiqlibrary_Writer12(self):
        return self.__eiqlibrary_Writer12

    @eiqlibrary_Writer12.setter
    def eiqlibrary_Writer12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eiqlibrary_Writer__eiqlibrary_Writer12", None)
        self.__eiqlibrary_Writer12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eiqlibrary_Book13"):
                    opp_val = getattr(item, "eiqlibrary_Book13", None)
                    
                    if opp_val == self:
                        setattr(item, "eiqlibrary_Book13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eiqlibrary_Book13"):
                    opp_val = getattr(item, "eiqlibrary_Book13", None)
                    
                    setattr(item, "eiqlibrary_Book13", self)
                    

    @property
    def eiqlibrary_Writer(self):
        return self.__eiqlibrary_Writer

    @eiqlibrary_Writer.setter
    def eiqlibrary_Writer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eiqlibrary_Writer__eiqlibrary_Writer", None)
        self.__eiqlibrary_Writer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eiqlibrary_Library"):
                opp_val = getattr(old_value, "eiqlibrary_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eiqlibrary_Library"):
                opp_val = getattr(value, "eiqlibrary_Library", None)
                if opp_val is None:
                    setattr(value, "eiqlibrary_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eiqlibrary_Writer9(self):
        return self.__eiqlibrary_Writer9

    @eiqlibrary_Writer9.setter
    def eiqlibrary_Writer9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eiqlibrary_Writer__eiqlibrary_Writer9", None)
        self.__eiqlibrary_Writer9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eiqlibrary_Book10"):
                opp_val = getattr(old_value, "eiqlibrary_Book10", None)
                if opp_val == self:
                    setattr(old_value, "eiqlibrary_Book10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eiqlibrary_Book10"):
                opp_val = getattr(value, "eiqlibrary_Book10", None)
                setattr(value, "eiqlibrary_Book10", self)

class eiqlibrary_Library:

    def __init__(self, address: str, sumOfPages: int, internalRequestCount: int, requestCount: int, eiqlibrary_Library: set["eiqlibrary_Writer"] = None, eiqlibrary_Library2: set["eiqlibrary_Book"] = None, eiqlibrary_Library4: set["eiqlibrary_Book"] = None):
        self.address = address
        self.sumOfPages = sumOfPages
        self.internalRequestCount = internalRequestCount
        self.requestCount = requestCount
        self.eiqlibrary_Library = eiqlibrary_Library if eiqlibrary_Library is not None else set()
        self.eiqlibrary_Library2 = eiqlibrary_Library2 if eiqlibrary_Library2 is not None else set()
        self.eiqlibrary_Library4 = eiqlibrary_Library4 if eiqlibrary_Library4 is not None else set()
        
    @property
    def internalRequestCount(self) -> int:
        return self.__internalRequestCount

    @internalRequestCount.setter
    def internalRequestCount(self, internalRequestCount: int):
        self.__internalRequestCount = internalRequestCount

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def requestCount(self) -> int:
        return self.__requestCount

    @requestCount.setter
    def requestCount(self, requestCount: int):
        self.__requestCount = requestCount

    @property
    def sumOfPages(self) -> int:
        return self.__sumOfPages

    @sumOfPages.setter
    def sumOfPages(self, sumOfPages: int):
        self.__sumOfPages = sumOfPages

    @property
    def eiqlibrary_Library4(self):
        return self.__eiqlibrary_Library4

    @eiqlibrary_Library4.setter
    def eiqlibrary_Library4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eiqlibrary_Library__eiqlibrary_Library4", None)
        self.__eiqlibrary_Library4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eiqlibrary_Book5"):
                    opp_val = getattr(item, "eiqlibrary_Book5", None)
                    
                    if opp_val == self:
                        setattr(item, "eiqlibrary_Book5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eiqlibrary_Book5"):
                    opp_val = getattr(item, "eiqlibrary_Book5", None)
                    
                    setattr(item, "eiqlibrary_Book5", self)
                    

    @property
    def eiqlibrary_Library(self):
        return self.__eiqlibrary_Library

    @eiqlibrary_Library.setter
    def eiqlibrary_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eiqlibrary_Library__eiqlibrary_Library", None)
        self.__eiqlibrary_Library = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eiqlibrary_Writer"):
                    opp_val = getattr(item, "eiqlibrary_Writer", None)
                    
                    if opp_val == self:
                        setattr(item, "eiqlibrary_Writer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eiqlibrary_Writer"):
                    opp_val = getattr(item, "eiqlibrary_Writer", None)
                    
                    setattr(item, "eiqlibrary_Writer", self)
                    

    @property
    def eiqlibrary_Library2(self):
        return self.__eiqlibrary_Library2

    @eiqlibrary_Library2.setter
    def eiqlibrary_Library2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eiqlibrary_Library__eiqlibrary_Library2", None)
        self.__eiqlibrary_Library2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eiqlibrary_Book"):
                    opp_val = getattr(item, "eiqlibrary_Book", None)
                    
                    if opp_val == self:
                        setattr(item, "eiqlibrary_Book", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eiqlibrary_Book"):
                    opp_val = getattr(item, "eiqlibrary_Book", None)
                    
                    setattr(item, "eiqlibrary_Book", self)
                    
