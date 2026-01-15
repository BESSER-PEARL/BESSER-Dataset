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

class bz242995_Author:

    def __init__(self, Name: str, id: str, Author: "bz242995_OneTimeWonder" = None, theAuthor: "bz242995_OneTimeWonder" = None):
        self.Name = Name
        self.id = id
        self.Author = Author
        self.theAuthor = theAuthor
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def theAuthor(self):
        return self.__theAuthor

    @theAuthor.setter
    def theAuthor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bz242995_Author__theAuthor", None)
        self.__theAuthor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "OneTimeWonder"):
                opp_val = getattr(old_value, "OneTimeWonder", None)
                if opp_val == self:
                    setattr(old_value, "OneTimeWonder", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "OneTimeWonder"):
                opp_val = getattr(value, "OneTimeWonder", None)
                setattr(value, "OneTimeWonder", self)

    @property
    def Author(self):
        return self.__Author

    @Author.setter
    def Author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bz242995_Author__Author", None)
        self.__Author = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "theBook"):
                opp_val = getattr(old_value, "theBook", None)
                if opp_val == self:
                    setattr(old_value, "theBook", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "theBook"):
                opp_val = getattr(value, "theBook", None)
                setattr(value, "theBook", self)

class bz242995_OneTimeWonder:

    def __init__(self, id: str, Name: str, theBook: "bz242995_Author" = None, OneTimeWonder: "bz242995_Author" = None):
        self.id = id
        self.Name = Name
        self.theBook = theBook
        self.OneTimeWonder = OneTimeWonder
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def theBook(self):
        return self.__theBook

    @theBook.setter
    def theBook(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bz242995_OneTimeWonder__theBook", None)
        self.__theBook = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Author"):
                opp_val = getattr(old_value, "Author", None)
                if opp_val == self:
                    setattr(old_value, "Author", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Author"):
                opp_val = getattr(value, "Author", None)
                setattr(value, "Author", self)

    @property
    def OneTimeWonder(self):
        return self.__OneTimeWonder

    @OneTimeWonder.setter
    def OneTimeWonder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bz242995_OneTimeWonder__OneTimeWonder", None)
        self.__OneTimeWonder = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "theAuthor"):
                opp_val = getattr(old_value, "theAuthor", None)
                if opp_val == self:
                    setattr(old_value, "theAuthor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "theAuthor"):
                opp_val = getattr(value, "theAuthor", None)
                setattr(value, "theAuthor", self)

class bz242995_Library:

    def __init__(self, name: str, bz242995_Library: set["bz242995_Writer"] = None, bz242995_Library3: set["bz242995_Book"] = None):
        self.name = name
        self.bz242995_Library = bz242995_Library if bz242995_Library is not None else set()
        self.bz242995_Library3 = bz242995_Library3 if bz242995_Library3 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bz242995_Library(self):
        return self.__bz242995_Library

    @bz242995_Library.setter
    def bz242995_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bz242995_Library__bz242995_Library", None)
        self.__bz242995_Library = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bz242995_Writer"):
                    opp_val = getattr(item, "bz242995_Writer", None)
                    
                    if opp_val == self:
                        setattr(item, "bz242995_Writer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bz242995_Writer"):
                    opp_val = getattr(item, "bz242995_Writer", None)
                    
                    setattr(item, "bz242995_Writer", self)
                    

    @property
    def bz242995_Library3(self):
        return self.__bz242995_Library3

    @bz242995_Library3.setter
    def bz242995_Library3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bz242995_Library__bz242995_Library3", None)
        self.__bz242995_Library3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bz242995_Book"):
                    opp_val = getattr(item, "bz242995_Book", None)
                    
                    if opp_val == self:
                        setattr(item, "bz242995_Book", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bz242995_Book"):
                    opp_val = getattr(item, "bz242995_Book", None)
                    
                    setattr(item, "bz242995_Book", self)
                    

class bz242995_Writer:

    def __init__(self, name: str, Writer: "bz242995_Book" = None, bz242995_Writer: "bz242995_Library" = None, author: set["bz242995_Book"] = None):
        self.name = name
        self.Writer = Writer
        self.bz242995_Writer = bz242995_Writer
        self.author = author if author is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def bz242995_Writer(self):
        return self.__bz242995_Writer

    @bz242995_Writer.setter
    def bz242995_Writer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bz242995_Writer__bz242995_Writer", None)
        self.__bz242995_Writer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bz242995_Library"):
                opp_val = getattr(old_value, "bz242995_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bz242995_Library"):
                opp_val = getattr(value, "bz242995_Library", None)
                if opp_val is None:
                    setattr(value, "bz242995_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bz242995_Writer__author", None)
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
        old_value = getattr(self, f"_bz242995_Writer__Writer", None)
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

class bz242995_Book:

    def __init__(self, title: str, pages: int, category: str, books: "bz242995_Writer" = None, bz242995_Book: "bz242995_Library" = None, Book: "bz242995_Writer" = None):
        self.title = title
        self.pages = pages
        self.category = category
        self.books = books
        self.bz242995_Book = bz242995_Book
        self.Book = Book
        
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
    def category(self) -> str:
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category

    @property
    def Book(self):
        return self.__Book

    @Book.setter
    def Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bz242995_Book__Book", None)
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
    def books(self):
        return self.__books

    @books.setter
    def books(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bz242995_Book__books", None)
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
    def bz242995_Book(self):
        return self.__bz242995_Book

    @bz242995_Book.setter
    def bz242995_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bz242995_Book__bz242995_Book", None)
        self.__bz242995_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bz242995_Library3"):
                opp_val = getattr(old_value, "bz242995_Library3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bz242995_Library3"):
                opp_val = getattr(value, "bz242995_Library3", None)
                if opp_val is None:
                    setattr(value, "bz242995_Library3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
