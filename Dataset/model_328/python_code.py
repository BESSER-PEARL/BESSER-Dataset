from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Category(Enum):
    ALL = "ALL"
    POETRY = "POETRY"
    SCIENCE = "SCIENCE"
    FICTION = "FICTION"


############################################
# Definition of Classes
############################################

class Library_Library:

    def __init__(self, name: str, id: int, Library: "Library_Book" = None, library: set["Library_Book"] = None, library5: set["Library_Writer"] = None, Library10: "Library_Writer" = None):
        self.name = name
        self.id = id
        self.Library = Library
        self.library = library if library is not None else set()
        self.library5 = library5 if library5 is not None else set()
        self.Library10 = Library10
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def library(self):
        return self.__library

    @library.setter
    def library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Library__library", None)
        self.__library = value if value is not None else set()
        
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
    def Library(self):
        return self.__Library

    @Library.setter
    def Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Library__Library", None)
        self.__Library = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "books2"):
                opp_val = getattr(old_value, "books2", None)
                if opp_val == self:
                    setattr(old_value, "books2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "books2"):
                opp_val = getattr(value, "books2", None)
                setattr(value, "books2", self)

    @property
    def Library10(self):
        return self.__Library10

    @Library10.setter
    def Library10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Library__Library10", None)
        self.__Library10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "writers"):
                opp_val = getattr(old_value, "writers", None)
                if opp_val == self:
                    setattr(old_value, "writers", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "writers"):
                opp_val = getattr(value, "writers", None)
                setattr(value, "writers", self)

    @property
    def library5(self):
        return self.__library5

    @library5.setter
    def library5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Library__library5", None)
        self.__library5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Writer6"):
                    opp_val = getattr(item, "Writer6", None)
                    
                    if opp_val == self:
                        setattr(item, "Writer6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Writer6"):
                    opp_val = getattr(item, "Writer6", None)
                    
                    setattr(item, "Writer6", self)
                    

class Library_Writer:

    def __init__(self, id: int, name: str, Writer: "Library_Book" = None, Writer6: "Library_Library" = None, writers: "Library_Library" = None, writer: set["Library_Book"] = None):
        self.id = id
        self.name = name
        self.Writer = Writer
        self.Writer6 = Writer6
        self.writers = writers
        self.writer = writer if writer is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def Writer6(self):
        return self.__Writer6

    @Writer6.setter
    def Writer6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Writer__Writer6", None)
        self.__Writer6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library5"):
                opp_val = getattr(old_value, "library5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library5"):
                opp_val = getattr(value, "library5", None)
                if opp_val is None:
                    setattr(value, "library5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def writers(self):
        return self.__writers

    @writers.setter
    def writers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Writer__writers", None)
        self.__writers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Library10"):
                opp_val = getattr(old_value, "Library10", None)
                if opp_val == self:
                    setattr(old_value, "Library10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Library10"):
                opp_val = getattr(value, "Library10", None)
                setattr(value, "Library10", self)

    @property
    def Writer(self):
        return self.__Writer

    @Writer.setter
    def Writer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Writer__Writer", None)
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
    def writer(self):
        return self.__writer

    @writer.setter
    def writer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Writer__writer", None)
        self.__writer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Book8"):
                    opp_val = getattr(item, "Book8", None)
                    
                    if opp_val == self:
                        setattr(item, "Book8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Book8"):
                    opp_val = getattr(item, "Book8", None)
                    
                    setattr(item, "Book8", self)
                    

class Library_Book:

    def __init__(self, category: str, blurb: str, title: str, pages: int, books: "Library_Writer" = None, books2: "Library_Library" = None, Book: "Library_Library" = None, Book8: "Library_Writer" = None):
        self.category = category
        self.blurb = blurb
        self.title = title
        self.pages = pages
        self.books = books
        self.books2 = books2
        self.Book = Book
        self.Book8 = Book8
        
    @property
    def blurb(self) -> str:
        return self.__blurb

    @blurb.setter
    def blurb(self, blurb: str):
        self.__blurb = blurb

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
    def books(self):
        return self.__books

    @books.setter
    def books(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Book__books", None)
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

    @property
    def Book8(self):
        return self.__Book8

    @Book8.setter
    def Book8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Book__Book8", None)
        self.__Book8 = value
        
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
    def Book(self):
        return self.__Book

    @Book.setter
    def Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Book__Book", None)
        self.__Book = value
        
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
    def books2(self):
        return self.__books2

    @books2.setter
    def books2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Book__books2", None)
        self.__books2 = value
        
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
