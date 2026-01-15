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

class library_Book:

    def __init__(self, title: str, pages: int, category: str, library_Book: "library_Library" = None, library_Book5: "library_Library" = None, books: set["library_Writer"] = None, Book: "library_Writer" = None, library_Book10: "library_Writer" = None, library_Book13: "library_Writer" = None):
        self.title = title
        self.pages = pages
        self.category = category
        self.library_Book = library_Book
        self.library_Book5 = library_Book5
        self.books = books if books is not None else set()
        self.Book = Book
        self.library_Book10 = library_Book10
        self.library_Book13 = library_Book13
        
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
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def Book(self):
        return self.__Book

    @Book.setter
    def Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__Book", None)
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
    def books(self):
        return self.__books

    @books.setter
    def books(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__books", None)
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
    def library_Book5(self):
        return self.__library_Book5

    @library_Book5.setter
    def library_Book5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__library_Book5", None)
        self.__library_Book5 = value
        
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

    @property
    def library_Book13(self):
        return self.__library_Book13

    @library_Book13.setter
    def library_Book13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__library_Book13", None)
        self.__library_Book13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Writer12"):
                opp_val = getattr(old_value, "library_Writer12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Writer12"):
                opp_val = getattr(value, "library_Writer12", None)
                if opp_val is None:
                    setattr(value, "library_Writer12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "library_Library2"):
                opp_val = getattr(old_value, "library_Library2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library2"):
                opp_val = getattr(value, "library_Library2", None)
                if opp_val is None:
                    setattr(value, "library_Library2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Book10(self):
        return self.__library_Book10

    @library_Book10.setter
    def library_Book10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__library_Book10", None)
        self.__library_Book10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Writer9"):
                opp_val = getattr(old_value, "library_Writer9", None)
                if opp_val == self:
                    setattr(old_value, "library_Writer9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Writer9"):
                opp_val = getattr(value, "library_Writer9", None)
                setattr(value, "library_Writer9", self)

class library_Writer:

    def __init__(self, name: str, library_Writer: "library_Library" = None, Writer: "library_Book" = None, authors: set["library_Book"] = None, library_Writer9: "library_Book" = None, library_Writer12: set["library_Book"] = None):
        self.name = name
        self.library_Writer = library_Writer
        self.Writer = Writer
        self.authors = authors if authors is not None else set()
        self.library_Writer9 = library_Writer9
        self.library_Writer12 = library_Writer12 if library_Writer12 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Writer(self):
        return self.__Writer

    @Writer.setter
    def Writer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Writer__Writer", None)
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
    def library_Writer12(self):
        return self.__library_Writer12

    @library_Writer12.setter
    def library_Writer12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Writer__library_Writer12", None)
        self.__library_Writer12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Book13"):
                    opp_val = getattr(item, "library_Book13", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Book13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Book13"):
                    opp_val = getattr(item, "library_Book13", None)
                    
                    setattr(item, "library_Book13", self)
                    

    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Writer__authors", None)
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
    def library_Writer(self):
        return self.__library_Writer

    @library_Writer.setter
    def library_Writer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Writer__library_Writer", None)
        self.__library_Writer = value
        
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
    def library_Writer9(self):
        return self.__library_Writer9

    @library_Writer9.setter
    def library_Writer9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Writer__library_Writer9", None)
        self.__library_Writer9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Book10"):
                opp_val = getattr(old_value, "library_Book10", None)
                if opp_val == self:
                    setattr(old_value, "library_Book10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Book10"):
                opp_val = getattr(value, "library_Book10", None)
                setattr(value, "library_Book10", self)

class library_Library:

    def __init__(self, address: str, sumOfPages: int, internalRequestCount: int, requestCount: int, library_Library: set["library_Writer"] = None, library_Library2: set["library_Book"] = None, library_Library4: set["library_Book"] = None):
        self.address = address
        self.sumOfPages = sumOfPages
        self.internalRequestCount = internalRequestCount
        self.requestCount = requestCount
        self.library_Library = library_Library if library_Library is not None else set()
        self.library_Library2 = library_Library2 if library_Library2 is not None else set()
        self.library_Library4 = library_Library4 if library_Library4 is not None else set()
        
    @property
    def sumOfPages(self) -> int:
        return self.__sumOfPages

    @sumOfPages.setter
    def sumOfPages(self, sumOfPages: int):
        self.__sumOfPages = sumOfPages

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
    def internalRequestCount(self) -> int:
        return self.__internalRequestCount

    @internalRequestCount.setter
    def internalRequestCount(self, internalRequestCount: int):
        self.__internalRequestCount = internalRequestCount

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
                if hasattr(item, "library_Book5"):
                    opp_val = getattr(item, "library_Book5", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Book5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Book5"):
                    opp_val = getattr(item, "library_Book5", None)
                    
                    setattr(item, "library_Book5", self)
                    

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
                    
