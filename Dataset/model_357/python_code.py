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

class cascadenotall_Library:

    def __init__(self, name: str, cascadenotall_Library: set["cascadenotall_Writer"] = None, cascadenotall_Library3: set["cascadenotall_Book"] = None):
        self.name = name
        self.cascadenotall_Library = cascadenotall_Library if cascadenotall_Library is not None else set()
        self.cascadenotall_Library3 = cascadenotall_Library3 if cascadenotall_Library3 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cascadenotall_Library3(self):
        return self.__cascadenotall_Library3

    @cascadenotall_Library3.setter
    def cascadenotall_Library3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cascadenotall_Library__cascadenotall_Library3", None)
        self.__cascadenotall_Library3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cascadenotall_Book"):
                    opp_val = getattr(item, "cascadenotall_Book", None)
                    
                    if opp_val == self:
                        setattr(item, "cascadenotall_Book", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cascadenotall_Book"):
                    opp_val = getattr(item, "cascadenotall_Book", None)
                    
                    setattr(item, "cascadenotall_Book", self)
                    

    @property
    def cascadenotall_Library(self):
        return self.__cascadenotall_Library

    @cascadenotall_Library.setter
    def cascadenotall_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cascadenotall_Library__cascadenotall_Library", None)
        self.__cascadenotall_Library = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "cascadenotall_Writer"):
                    opp_val = getattr(item, "cascadenotall_Writer", None)
                    
                    if opp_val == self:
                        setattr(item, "cascadenotall_Writer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "cascadenotall_Writer"):
                    opp_val = getattr(item, "cascadenotall_Writer", None)
                    
                    setattr(item, "cascadenotall_Writer", self)
                    

class cascadenotall_Writer:

    def __init__(self, name: str, Writer: "cascadenotall_Book" = None, cascadenotall_Writer: "cascadenotall_Library" = None, author: set["cascadenotall_Book"] = None):
        self.name = name
        self.Writer = Writer
        self.cascadenotall_Writer = cascadenotall_Writer
        self.author = author if author is not None else set()
        
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
        old_value = getattr(self, f"_cascadenotall_Writer__author", None)
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
        old_value = getattr(self, f"_cascadenotall_Writer__Writer", None)
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
    def cascadenotall_Writer(self):
        return self.__cascadenotall_Writer

    @cascadenotall_Writer.setter
    def cascadenotall_Writer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cascadenotall_Writer__cascadenotall_Writer", None)
        self.__cascadenotall_Writer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cascadenotall_Library"):
                opp_val = getattr(old_value, "cascadenotall_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cascadenotall_Library"):
                opp_val = getattr(value, "cascadenotall_Library", None)
                if opp_val is None:
                    setattr(value, "cascadenotall_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class cascadenotall_Book:

    def __init__(self, title: str, pages: str, category: str, books: "cascadenotall_Writer" = None, cascadenotall_Book: "cascadenotall_Library" = None, Book: "cascadenotall_Writer" = None):
        self.title = title
        self.pages = pages
        self.category = category
        self.books = books
        self.cascadenotall_Book = cascadenotall_Book
        self.Book = Book
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

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
    def cascadenotall_Book(self):
        return self.__cascadenotall_Book

    @cascadenotall_Book.setter
    def cascadenotall_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cascadenotall_Book__cascadenotall_Book", None)
        self.__cascadenotall_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "cascadenotall_Library3"):
                opp_val = getattr(old_value, "cascadenotall_Library3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "cascadenotall_Library3"):
                opp_val = getattr(value, "cascadenotall_Library3", None)
                if opp_val is None:
                    setattr(value, "cascadenotall_Library3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def books(self):
        return self.__books

    @books.setter
    def books(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_cascadenotall_Book__books", None)
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
        old_value = getattr(self, f"_cascadenotall_Book__Book", None)
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
