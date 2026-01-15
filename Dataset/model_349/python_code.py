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

class eavlibrary_Pen:

    def __init__(self, name: str, eavlibrary_Pen: "eavlibrary_Writer" = None):
        self.name = name
        self.eavlibrary_Pen = eavlibrary_Pen
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def eavlibrary_Pen(self):
        return self.__eavlibrary_Pen

    @eavlibrary_Pen.setter
    def eavlibrary_Pen(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eavlibrary_Pen__eavlibrary_Pen", None)
        self.__eavlibrary_Pen = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eavlibrary_Writer8"):
                opp_val = getattr(old_value, "eavlibrary_Writer8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eavlibrary_Writer8"):
                opp_val = getattr(value, "eavlibrary_Writer8", None)
                if opp_val is None:
                    setattr(value, "eavlibrary_Writer8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eavlibrary_Writer:

    def __init__(self, name: str, image: str, abstract: str, eavlibrary_Writer: "eavlibrary_Library" = None, Writer: "eavlibrary_Book" = None, author: set["eavlibrary_Book"] = None, eavlibrary_Writer6: "eavlibrary_City" = None, eavlibrary_Writer8: set["eavlibrary_Pen"] = None):
        self.name = name
        self.image = image
        self.abstract = abstract
        self.eavlibrary_Writer = eavlibrary_Writer
        self.Writer = Writer
        self.author = author if author is not None else set()
        self.eavlibrary_Writer6 = eavlibrary_Writer6
        self.eavlibrary_Writer8 = eavlibrary_Writer8 if eavlibrary_Writer8 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def image(self) -> str:
        return self.__image

    @image.setter
    def image(self, image: str):
        self.__image = image

    @property
    def abstract(self) -> str:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: str):
        self.__abstract = abstract

    @property
    def eavlibrary_Writer6(self):
        return self.__eavlibrary_Writer6

    @eavlibrary_Writer6.setter
    def eavlibrary_Writer6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eavlibrary_Writer__eavlibrary_Writer6", None)
        self.__eavlibrary_Writer6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eavlibrary_City"):
                opp_val = getattr(old_value, "eavlibrary_City", None)
                if opp_val == self:
                    setattr(old_value, "eavlibrary_City", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eavlibrary_City"):
                opp_val = getattr(value, "eavlibrary_City", None)
                setattr(value, "eavlibrary_City", self)

    @property
    def eavlibrary_Writer8(self):
        return self.__eavlibrary_Writer8

    @eavlibrary_Writer8.setter
    def eavlibrary_Writer8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eavlibrary_Writer__eavlibrary_Writer8", None)
        self.__eavlibrary_Writer8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eavlibrary_Pen"):
                    opp_val = getattr(item, "eavlibrary_Pen", None)
                    
                    if opp_val == self:
                        setattr(item, "eavlibrary_Pen", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eavlibrary_Pen"):
                    opp_val = getattr(item, "eavlibrary_Pen", None)
                    
                    setattr(item, "eavlibrary_Pen", self)
                    

    @property
    def eavlibrary_Writer(self):
        return self.__eavlibrary_Writer

    @eavlibrary_Writer.setter
    def eavlibrary_Writer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eavlibrary_Writer__eavlibrary_Writer", None)
        self.__eavlibrary_Writer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eavlibrary_Library"):
                opp_val = getattr(old_value, "eavlibrary_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eavlibrary_Library"):
                opp_val = getattr(value, "eavlibrary_Library", None)
                if opp_val is None:
                    setattr(value, "eavlibrary_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eavlibrary_Writer__author", None)
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
        old_value = getattr(self, f"_eavlibrary_Writer__Writer", None)
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

class eavlibrary_Library:

    def __init__(self, name: str, eavlibrary_Library: set["eavlibrary_Writer"] = None, eavlibrary_Library3: set["eavlibrary_Book"] = None):
        self.name = name
        self.eavlibrary_Library = eavlibrary_Library if eavlibrary_Library is not None else set()
        self.eavlibrary_Library3 = eavlibrary_Library3 if eavlibrary_Library3 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def eavlibrary_Library3(self):
        return self.__eavlibrary_Library3

    @eavlibrary_Library3.setter
    def eavlibrary_Library3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eavlibrary_Library__eavlibrary_Library3", None)
        self.__eavlibrary_Library3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eavlibrary_Book"):
                    opp_val = getattr(item, "eavlibrary_Book", None)
                    
                    if opp_val == self:
                        setattr(item, "eavlibrary_Book", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eavlibrary_Book"):
                    opp_val = getattr(item, "eavlibrary_Book", None)
                    
                    setattr(item, "eavlibrary_Book", self)
                    

    @property
    def eavlibrary_Library(self):
        return self.__eavlibrary_Library

    @eavlibrary_Library.setter
    def eavlibrary_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eavlibrary_Library__eavlibrary_Library", None)
        self.__eavlibrary_Library = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eavlibrary_Writer"):
                    opp_val = getattr(item, "eavlibrary_Writer", None)
                    
                    if opp_val == self:
                        setattr(item, "eavlibrary_Writer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eavlibrary_Writer"):
                    opp_val = getattr(item, "eavlibrary_Writer", None)
                    
                    setattr(item, "eavlibrary_Writer", self)
                    

class eavlibrary_City:

    def __init__(self, name: str, eavlibrary_City: "eavlibrary_Writer" = None):
        self.name = name
        self.eavlibrary_City = eavlibrary_City
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def eavlibrary_City(self):
        return self.__eavlibrary_City

    @eavlibrary_City.setter
    def eavlibrary_City(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eavlibrary_City__eavlibrary_City", None)
        self.__eavlibrary_City = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eavlibrary_Writer6"):
                opp_val = getattr(old_value, "eavlibrary_Writer6", None)
                if opp_val == self:
                    setattr(old_value, "eavlibrary_Writer6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eavlibrary_Writer6"):
                opp_val = getattr(value, "eavlibrary_Writer6", None)
                setattr(value, "eavlibrary_Writer6", self)

class eavlibrary_Book:

    def __init__(self, title: str, pages: str, category: str, test: str, eavlibrary_Book: "eavlibrary_Library" = None, books: "eavlibrary_Writer" = None, Book: "eavlibrary_Writer" = None):
        self.title = title
        self.pages = pages
        self.category = category
        self.test = test
        self.eavlibrary_Book = eavlibrary_Book
        self.books = books
        self.Book = Book
        
    @property
    def test(self) -> str:
        return self.__test

    @test.setter
    def test(self, test: str):
        self.__test = test

    @property
    def pages(self) -> str:
        return self.__pages

    @pages.setter
    def pages(self, pages: str):
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
        old_value = getattr(self, f"_eavlibrary_Book__books", None)
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
    def eavlibrary_Book(self):
        return self.__eavlibrary_Book

    @eavlibrary_Book.setter
    def eavlibrary_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eavlibrary_Book__eavlibrary_Book", None)
        self.__eavlibrary_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eavlibrary_Library3"):
                opp_val = getattr(old_value, "eavlibrary_Library3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eavlibrary_Library3"):
                opp_val = getattr(value, "eavlibrary_Library3", None)
                if opp_val is None:
                    setattr(value, "eavlibrary_Library3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Book(self):
        return self.__Book

    @Book.setter
    def Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eavlibrary_Book__Book", None)
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
