from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class BookCategory(Enum):
    Mystery = "Mystery"
    ScienceFiction = "ScienceFiction"
    Biography = "Biography"


############################################
# Definition of Classes
############################################

class Asset:

    pass
class Book:

    pass
class libraryExample_SchoolBook(Asset, Book):

    pass
class libraryExample_Book:

    def __init__(self, title: str, pages: int, category: str, books: "libraryExample_Writer" = None, Book: "libraryExample_Writer" = None, libraryExample_Book: "libraryExample_Library" = None):
        self.title = title
        self.pages = pages
        self.category = category
        self.books = books
        self.Book = Book
        self.libraryExample_Book = libraryExample_Book
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

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
    def Book(self):
        return self.__Book

    @Book.setter
    def Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryExample_Book__Book", None)
        self.__Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "writer"):
                opp_val = getattr(old_value, "writer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "writer"):
                opp_val = getattr(value, "writer", None)
                if opp_val is None:
                    setattr(value, "writer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def libraryExample_Book(self):
        return self.__libraryExample_Book

    @libraryExample_Book.setter
    def libraryExample_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryExample_Book__libraryExample_Book", None)
        self.__libraryExample_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryExample_Library"):
                opp_val = getattr(old_value, "libraryExample_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryExample_Library"):
                opp_val = getattr(value, "libraryExample_Library", None)
                if opp_val is None:
                    setattr(value, "libraryExample_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def books(self):
        return self.__books

    @books.setter
    def books(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryExample_Book__books", None)
        self.__books = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Writer"):
                opp_val = getattr(old_value, "Writer", None)
                if opp_val == self:
                    setattr(old_value, "Writer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Writer"):
                opp_val = getattr(value, "Writer", None)
                setattr(value, "Writer", self)

class libraryExample_Asset:

    def __init__(self, value: float):
        self.value = value
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

class Library:

    pass
class libraryExample_SchoolLibrary(Library):

    def __init__(self, location: str):
        self.location = location
        
    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

class libraryExample_Library:

    def __init__(self, name: str, libraryExample_Library2: set["libraryExample_Writer"] = None, libraryExample_Library: set["libraryExample_Book"] = None):
        self.name = name
        self.libraryExample_Library2 = libraryExample_Library2 if libraryExample_Library2 is not None else set()
        self.libraryExample_Library = libraryExample_Library if libraryExample_Library is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def libraryExample_Library(self):
        return self.__libraryExample_Library

    @libraryExample_Library.setter
    def libraryExample_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryExample_Library__libraryExample_Library", None)
        self.__libraryExample_Library = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "libraryExample_Book"):
                    opp_val = getattr(item, "libraryExample_Book", None)
                    
                    if opp_val == self:
                        setattr(item, "libraryExample_Book", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "libraryExample_Book"):
                    opp_val = getattr(item, "libraryExample_Book", None)
                    
                    setattr(item, "libraryExample_Book", self)
                    

    @property
    def libraryExample_Library2(self):
        return self.__libraryExample_Library2

    @libraryExample_Library2.setter
    def libraryExample_Library2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryExample_Library__libraryExample_Library2", None)
        self.__libraryExample_Library2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "libraryExample_Writer"):
                    opp_val = getattr(item, "libraryExample_Writer", None)
                    
                    if opp_val == self:
                        setattr(item, "libraryExample_Writer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "libraryExample_Writer"):
                    opp_val = getattr(item, "libraryExample_Writer", None)
                    
                    setattr(item, "libraryExample_Writer", self)
                    

class libraryExample_Writer:

    def __init__(self, name: str, lastname: str, libraryExample_Writer: "libraryExample_Library" = None, Writer: "libraryExample_Book" = None, writer: set["libraryExample_Book"] = None):
        self.name = name
        self.lastname = lastname
        self.libraryExample_Writer = libraryExample_Writer
        self.Writer = Writer
        self.writer = writer if writer is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def lastname(self) -> str:
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname

    @property
    def Writer(self):
        return self.__Writer

    @Writer.setter
    def Writer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryExample_Writer__Writer", None)
        self.__Writer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "books"):
                opp_val = getattr(old_value, "books", None)
                if opp_val == self:
                    setattr(old_value, "books", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "books"):
                opp_val = getattr(value, "books", None)
                setattr(value, "books", self)

    @property
    def libraryExample_Writer(self):
        return self.__libraryExample_Writer

    @libraryExample_Writer.setter
    def libraryExample_Writer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryExample_Writer__libraryExample_Writer", None)
        self.__libraryExample_Writer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryExample_Library2"):
                opp_val = getattr(old_value, "libraryExample_Library2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryExample_Library2"):
                opp_val = getattr(value, "libraryExample_Library2", None)
                if opp_val is None:
                    setattr(value, "libraryExample_Library2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def writer(self):
        return self.__writer

    @writer.setter
    def writer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryExample_Writer__writer", None)
        self.__writer = value if value is not None else set()
        
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
                    
