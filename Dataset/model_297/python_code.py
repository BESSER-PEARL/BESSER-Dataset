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

class library_Review:

    def __init__(self, title: str, positive: bool, Review: "library_Book" = None, reviews: "library_Book" = None):
        self.title = title
        self.positive = positive
        self.Review = Review
        self.reviews = reviews
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def positive(self) -> bool:
        return self.__positive

    @positive.setter
    def positive(self, positive: bool):
        self.__positive = positive

    @property
    def reviews(self):
        return self.__reviews

    @reviews.setter
    def reviews(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Review__reviews", None)
        self.__reviews = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Book8"):
                opp_val = getattr(old_value, "Book8", None)
                if opp_val == self:
                    setattr(old_value, "Book8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Book8"):
                opp_val = getattr(value, "Book8", None)
                setattr(value, "Book8", self)

    @property
    def Review(self):
        return self.__Review

    @Review.setter
    def Review(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Review__Review", None)
        self.__Review = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book"):
                opp_val = getattr(old_value, "book", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book"):
                opp_val = getattr(value, "book", None)
                if opp_val is None:
                    setattr(value, "book", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class library_Opinion:

    def __init__(self, text: str, context: str, Opinion: "library_Writer" = None, opinions: "library_Writer" = None, library_Opinion: "library_Book" = None):
        self.text = text
        self.context = context
        self.Opinion = Opinion
        self.opinions = opinions
        self.library_Opinion = library_Opinion
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def context(self) -> str:
        return self.__context

    @context.setter
    def context(self, context: str):
        self.__context = context

    @property
    def library_Opinion(self):
        return self.__library_Opinion

    @library_Opinion.setter
    def library_Opinion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Opinion__library_Opinion", None)
        self.__library_Opinion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Book12"):
                opp_val = getattr(old_value, "library_Book12", None)
                if opp_val == self:
                    setattr(old_value, "library_Book12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Book12"):
                opp_val = getattr(value, "library_Book12", None)
                setattr(value, "library_Book12", self)

    @property
    def Opinion(self):
        return self.__Opinion

    @Opinion.setter
    def Opinion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Opinion__Opinion", None)
        self.__Opinion = value
        
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
    def opinions(self):
        return self.__opinions

    @opinions.setter
    def opinions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Opinion__opinions", None)
        self.__opinions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Writer10"):
                opp_val = getattr(old_value, "Writer10", None)
                if opp_val == self:
                    setattr(old_value, "Writer10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Writer10"):
                opp_val = getattr(value, "Writer10", None)
                setattr(value, "Writer10", self)

class library_Book:

    def __init__(self, title: str, pages: int, category: str, library_Book: "library_Library" = None, Book: "library_Writer" = None, books: "library_Writer" = None, book: set["library_Review"] = None, Book8: "library_Review" = None, library_Book12: "library_Opinion" = None):
        self.title = title
        self.pages = pages
        self.category = category
        self.library_Book = library_Book
        self.Book = Book
        self.books = books
        self.book = book if book is not None else set()
        self.Book8 = Book8
        self.library_Book12 = library_Book12
        
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
    def Book8(self):
        return self.__Book8

    @Book8.setter
    def Book8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__Book8", None)
        self.__Book8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reviews"):
                opp_val = getattr(old_value, "reviews", None)
                if opp_val == self:
                    setattr(old_value, "reviews", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reviews"):
                opp_val = getattr(value, "reviews", None)
                setattr(value, "reviews", self)

    @property
    def books(self):
        return self.__books

    @books.setter
    def books(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__books", None)
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
    def Book(self):
        return self.__Book

    @Book.setter
    def Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__Book", None)
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
    def library_Book12(self):
        return self.__library_Book12

    @library_Book12.setter
    def library_Book12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__library_Book12", None)
        self.__library_Book12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Opinion"):
                opp_val = getattr(old_value, "library_Opinion", None)
                if opp_val == self:
                    setattr(old_value, "library_Opinion", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Opinion"):
                opp_val = getattr(value, "library_Opinion", None)
                setattr(value, "library_Opinion", self)

    @property
    def book(self):
        return self.__book

    @book.setter
    def book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__book", None)
        self.__book = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Review"):
                    opp_val = getattr(item, "Review", None)
                    
                    if opp_val == self:
                        setattr(item, "Review", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Review"):
                    opp_val = getattr(item, "Review", None)
                    
                    setattr(item, "Review", self)
                    

class library_Writer:

    def __init__(self, name: str, library_Writer: "library_Library" = None, author: set["library_Book"] = None, writer: set["library_Opinion"] = None, Writer: "library_Book" = None, Writer10: "library_Opinion" = None):
        self.name = name
        self.library_Writer = library_Writer
        self.author = author if author is not None else set()
        self.writer = writer if writer is not None else set()
        self.Writer = Writer
        self.Writer10 = Writer10
        
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
        old_value = getattr(self, f"_library_Writer__writer", None)
        self.__writer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Opinion"):
                    opp_val = getattr(item, "Opinion", None)
                    
                    if opp_val == self:
                        setattr(item, "Opinion", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Opinion"):
                    opp_val = getattr(item, "Opinion", None)
                    
                    setattr(item, "Opinion", self)
                    

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
    def Writer10(self):
        return self.__Writer10

    @Writer10.setter
    def Writer10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Writer__Writer10", None)
        self.__Writer10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "opinions"):
                opp_val = getattr(old_value, "opinions", None)
                if opp_val == self:
                    setattr(old_value, "opinions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "opinions"):
                opp_val = getattr(value, "opinions", None)
                setattr(value, "opinions", self)

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Writer__author", None)
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
                    

class library_Library:

    def __init__(self, name: str, library_Library: set["library_Writer"] = None, library_Library2: set["library_Book"] = None):
        self.name = name
        self.library_Library = library_Library if library_Library is not None else set()
        self.library_Library2 = library_Library2 if library_Library2 is not None else set()
        
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
                    
