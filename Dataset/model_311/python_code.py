from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class BookCategory(Enum):
    MYSTERY = "MYSTERY"
    ScienceFiction = "ScienceFiction"
    Biography = "Biography"


############################################
# Definition of Classes
############################################

class library_MapOfDataTypes:

    def __init__(self, key: str, value: str, library_MapOfDataTypes: "library_Library" = None):
        self.key = key
        self.value = value
        self.library_MapOfDataTypes = library_MapOfDataTypes
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def library_MapOfDataTypes(self):
        return self.__library_MapOfDataTypes

    @library_MapOfDataTypes.setter
    def library_MapOfDataTypes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_MapOfDataTypes__library_MapOfDataTypes", None)
        self.__library_MapOfDataTypes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Library10"):
                opp_val = getattr(old_value, "library_Library10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library10"):
                opp_val = getattr(value, "library_Library10", None)
                if opp_val is None:
                    setattr(value, "library_Library10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class library_WriterNameMap:

    def __init__(self, key: str, library_WriterNameMap: "library_Library" = None, library_WriterNameMap13: "library_Writer" = None):
        self.key = key
        self.library_WriterNameMap = library_WriterNameMap
        self.library_WriterNameMap13 = library_WriterNameMap13
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def library_WriterNameMap(self):
        return self.__library_WriterNameMap

    @library_WriterNameMap.setter
    def library_WriterNameMap(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_WriterNameMap__library_WriterNameMap", None)
        self.__library_WriterNameMap = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Library8"):
                opp_val = getattr(old_value, "library_Library8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library8"):
                opp_val = getattr(value, "library_Library8", None)
                if opp_val is None:
                    setattr(value, "library_Library8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_WriterNameMap13(self):
        return self.__library_WriterNameMap13

    @library_WriterNameMap13.setter
    def library_WriterNameMap13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_WriterNameMap__library_WriterNameMap13", None)
        self.__library_WriterNameMap13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Writer14"):
                opp_val = getattr(old_value, "library_Writer14", None)
                if opp_val == self:
                    setattr(old_value, "library_Writer14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Writer14"):
                opp_val = getattr(value, "library_Writer14", None)
                setattr(value, "library_Writer14", self)

class library_Library:

    def __init__(self, name: str, bookByTitleMap: str, options: str, uRIs_1: str, map1: str, library_Library: set["library_Writer"] = None, library_Library3: set["library_Book"] = None, library_Library5: set["library_Book"] = None, library_Library8: set["library_WriterNameMap"] = None, library_Library10: set["library_MapOfDataTypes"] = None):
        self.name = name
        self.bookByTitleMap = bookByTitleMap
        self.options = options
        self.uRIs_1 = uRIs_1
        self.map1 = map1
        self.library_Library = library_Library if library_Library is not None else set()
        self.library_Library3 = library_Library3 if library_Library3 is not None else set()
        self.library_Library5 = library_Library5 if library_Library5 is not None else set()
        self.library_Library8 = library_Library8 if library_Library8 is not None else set()
        self.library_Library10 = library_Library10 if library_Library10 is not None else set()
        
    @property
    def bookByTitleMap(self) -> str:
        return self.__bookByTitleMap

    @bookByTitleMap.setter
    def bookByTitleMap(self, bookByTitleMap: str):
        self.__bookByTitleMap = bookByTitleMap

    @property
    def options(self) -> str:
        return self.__options

    @options.setter
    def options(self, options: str):
        self.__options = options

    @property
    def map1(self) -> str:
        return self.__map1

    @map1.setter
    def map1(self, map1: str):
        self.__map1 = map1

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uRIs_1(self) -> str:
        return self.__uRIs_1

    @uRIs_1.setter
    def uRIs_1(self, uRIs_1: str):
        self.__uRIs_1 = uRIs_1

    @property
    def library_Library10(self):
        return self.__library_Library10

    @library_Library10.setter
    def library_Library10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library10", None)
        self.__library_Library10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_MapOfDataTypes"):
                    opp_val = getattr(item, "library_MapOfDataTypes", None)
                    
                    if opp_val == self:
                        setattr(item, "library_MapOfDataTypes", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_MapOfDataTypes"):
                    opp_val = getattr(item, "library_MapOfDataTypes", None)
                    
                    setattr(item, "library_MapOfDataTypes", self)
                    

    @property
    def library_Library5(self):
        return self.__library_Library5

    @library_Library5.setter
    def library_Library5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library5", None)
        self.__library_Library5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Book6"):
                    opp_val = getattr(item, "library_Book6", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Book6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Book6"):
                    opp_val = getattr(item, "library_Book6", None)
                    
                    setattr(item, "library_Book6", self)
                    

    @property
    def library_Library8(self):
        return self.__library_Library8

    @library_Library8.setter
    def library_Library8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library8", None)
        self.__library_Library8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_WriterNameMap"):
                    opp_val = getattr(item, "library_WriterNameMap", None)
                    
                    if opp_val == self:
                        setattr(item, "library_WriterNameMap", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_WriterNameMap"):
                    opp_val = getattr(item, "library_WriterNameMap", None)
                    
                    setattr(item, "library_WriterNameMap", self)
                    

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
    def library_Library3(self):
        return self.__library_Library3

    @library_Library3.setter
    def library_Library3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library3", None)
        self.__library_Library3 = value if value is not None else set()
        
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
                    

class library_Writer:

    def __init__(self, name: str, Writer: "library_Book" = None, library_Writer: "library_Library" = None, author: set["library_Book"] = None, library_Writer14: "library_WriterNameMap" = None):
        self.name = name
        self.Writer = Writer
        self.library_Writer = library_Writer
        self.author = author if author is not None else set()
        self.library_Writer14 = library_Writer14
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def library_Writer14(self):
        return self.__library_Writer14

    @library_Writer14.setter
    def library_Writer14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Writer__library_Writer14", None)
        self.__library_Writer14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_WriterNameMap13"):
                opp_val = getattr(old_value, "library_WriterNameMap13", None)
                if opp_val == self:
                    setattr(old_value, "library_WriterNameMap13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_WriterNameMap13"):
                opp_val = getattr(value, "library_WriterNameMap13", None)
                setattr(value, "library_WriterNameMap13", self)

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

class library_Book:

    def __init__(self, title: str, pages: int, category: str, books: "library_Writer" = None, library_Book: "library_Library" = None, library_Book6: "library_Library" = None, Book: "library_Writer" = None):
        self.title = title
        self.pages = pages
        self.category = category
        self.books = books
        self.library_Book = library_Book
        self.library_Book6 = library_Book6
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
            if hasattr(old_value, "library_Library3"):
                opp_val = getattr(old_value, "library_Library3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library3"):
                opp_val = getattr(value, "library_Library3", None)
                if opp_val is None:
                    setattr(value, "library_Library3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Book6(self):
        return self.__library_Book6

    @library_Book6.setter
    def library_Book6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__library_Book6", None)
        self.__library_Book6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Library5"):
                opp_val = getattr(old_value, "library_Library5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library5"):
                opp_val = getattr(value, "library_Library5", None)
                if opp_val is None:
                    setattr(value, "library_Library5", set([self]))
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
