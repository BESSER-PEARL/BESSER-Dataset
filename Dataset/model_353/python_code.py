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

class libraryModel_Book:

    def __init__(self, title: str, pages: int, category: str, libraryModel_Book: "libraryModel_Library" = None, Book: "libraryModel_Writer" = None, books: "libraryModel_Writer" = None):
        self.title = title
        self.pages = pages
        self.category = category
        self.libraryModel_Book = libraryModel_Book
        self.Book = Book
        self.books = books
        
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
        old_value = getattr(self, f"_libraryModel_Book__books", None)
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
    def libraryModel_Book(self):
        return self.__libraryModel_Book

    @libraryModel_Book.setter
    def libraryModel_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryModel_Book__libraryModel_Book", None)
        self.__libraryModel_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryModel_Library2"):
                opp_val = getattr(old_value, "libraryModel_Library2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryModel_Library2"):
                opp_val = getattr(value, "libraryModel_Library2", None)
                if opp_val is None:
                    setattr(value, "libraryModel_Library2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Book(self):
        return self.__Book

    @Book.setter
    def Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryModel_Book__Book", None)
        self.__Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "author"):
                opp_val = getattr(old_value, "author", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "author"):
                opp_val = getattr(value, "author", None)
                if opp_val is None:
                    setattr(value, "author", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class libraryModel_Writer:

    def __init__(self, name: str, libraryModel_Writer: "libraryModel_Library" = None, author: set["libraryModel_Book"] = None, Writer: "libraryModel_Book" = None):
        self.name = name
        self.libraryModel_Writer = libraryModel_Writer
        self.author = author if author is not None else set()
        self.Writer = Writer
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryModel_Writer__author", None)
        self.__author = value if value is not None else set()
        
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
        old_value = getattr(self, f"_libraryModel_Writer__Writer", None)
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
    def libraryModel_Writer(self):
        return self.__libraryModel_Writer

    @libraryModel_Writer.setter
    def libraryModel_Writer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryModel_Writer__libraryModel_Writer", None)
        self.__libraryModel_Writer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "libraryModel_Library"):
                opp_val = getattr(old_value, "libraryModel_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "libraryModel_Library"):
                opp_val = getattr(value, "libraryModel_Library", None)
                if opp_val is None:
                    setattr(value, "libraryModel_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class libraryModel_Library:

    def __init__(self, name: str, libraryModel_Library: set["libraryModel_Writer"] = None, libraryModel_Library2: set["libraryModel_Book"] = None):
        self.name = name
        self.libraryModel_Library = libraryModel_Library if libraryModel_Library is not None else set()
        self.libraryModel_Library2 = libraryModel_Library2 if libraryModel_Library2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def libraryModel_Library(self):
        return self.__libraryModel_Library

    @libraryModel_Library.setter
    def libraryModel_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryModel_Library__libraryModel_Library", None)
        self.__libraryModel_Library = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "libraryModel_Writer"):
                    opp_val = getattr(item, "libraryModel_Writer", None)
                    
                    if opp_val == self:
                        setattr(item, "libraryModel_Writer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "libraryModel_Writer"):
                    opp_val = getattr(item, "libraryModel_Writer", None)
                    
                    setattr(item, "libraryModel_Writer", self)
                    

    @property
    def libraryModel_Library2(self):
        return self.__libraryModel_Library2

    @libraryModel_Library2.setter
    def libraryModel_Library2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_libraryModel_Library__libraryModel_Library2", None)
        self.__libraryModel_Library2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "libraryModel_Book"):
                    opp_val = getattr(item, "libraryModel_Book", None)
                    
                    if opp_val == self:
                        setattr(item, "libraryModel_Book", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "libraryModel_Book"):
                    opp_val = getattr(item, "libraryModel_Book", None)
                    
                    setattr(item, "libraryModel_Book", self)
                    
