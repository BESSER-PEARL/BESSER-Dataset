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

class lazy_Library:

    def __init__(self, name: str, lazy_Library: set["lazy_Writer"] = None, lazy_Library3: set["lazy_Book"] = None):
        self.name = name
        self.lazy_Library = lazy_Library if lazy_Library is not None else set()
        self.lazy_Library3 = lazy_Library3 if lazy_Library3 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def lazy_Library(self):
        return self.__lazy_Library

    @lazy_Library.setter
    def lazy_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lazy_Library__lazy_Library", None)
        self.__lazy_Library = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lazy_Writer"):
                    opp_val = getattr(item, "lazy_Writer", None)
                    
                    if opp_val == self:
                        setattr(item, "lazy_Writer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lazy_Writer"):
                    opp_val = getattr(item, "lazy_Writer", None)
                    
                    setattr(item, "lazy_Writer", self)
                    

    @property
    def lazy_Library3(self):
        return self.__lazy_Library3

    @lazy_Library3.setter
    def lazy_Library3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lazy_Library__lazy_Library3", None)
        self.__lazy_Library3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "lazy_Book"):
                    opp_val = getattr(item, "lazy_Book", None)
                    
                    if opp_val == self:
                        setattr(item, "lazy_Book", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "lazy_Book"):
                    opp_val = getattr(item, "lazy_Book", None)
                    
                    setattr(item, "lazy_Book", self)
                    

class lazy_Book:

    def __init__(self, pages: str, category: str, title: str, books: "lazy_Writer" = None, Book: "lazy_Writer" = None, lazy_Book: "lazy_Library" = None):
        self.pages = pages
        self.category = category
        self.title = title
        self.books = books
        self.Book = Book
        self.lazy_Book = lazy_Book
        
    @property
    def pages(self) -> str:
        return self.__pages

    @pages.setter
    def pages(self, pages: str):
        self.__pages = pages

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
    def books(self):
        return self.__books

    @books.setter
    def books(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lazy_Book__books", None)
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
    def Book(self):
        return self.__Book

    @Book.setter
    def Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lazy_Book__Book", None)
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

    @property
    def lazy_Book(self):
        return self.__lazy_Book

    @lazy_Book.setter
    def lazy_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lazy_Book__lazy_Book", None)
        self.__lazy_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lazy_Library3"):
                opp_val = getattr(old_value, "lazy_Library3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lazy_Library3"):
                opp_val = getattr(value, "lazy_Library3", None)
                if opp_val is None:
                    setattr(value, "lazy_Library3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class lazy_Writer:

    def __init__(self, name: str, Writer: "lazy_Book" = None, author: set["lazy_Book"] = None, lazy_Writer: "lazy_Library" = None):
        self.name = name
        self.Writer = Writer
        self.author = author if author is not None else set()
        self.lazy_Writer = lazy_Writer
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def lazy_Writer(self):
        return self.__lazy_Writer

    @lazy_Writer.setter
    def lazy_Writer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lazy_Writer__lazy_Writer", None)
        self.__lazy_Writer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lazy_Library"):
                opp_val = getattr(old_value, "lazy_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lazy_Library"):
                opp_val = getattr(value, "lazy_Library", None)
                if opp_val is None:
                    setattr(value, "lazy_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Writer(self):
        return self.__Writer

    @Writer.setter
    def Writer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lazy_Writer__Writer", None)
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
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lazy_Writer__author", None)
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
                    
