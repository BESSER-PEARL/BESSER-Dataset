from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class library_Member:

    def __init__(self, name: str, id: int, library_Member8: set["library_Book"] = None, library_Member: "library_Library" = None):
        self.name = name
        self.id = id
        self.library_Member8 = library_Member8 if library_Member8 is not None else set()
        self.library_Member = library_Member
        
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
    def library_Member(self):
        return self.__library_Member

    @library_Member.setter
    def library_Member(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Member__library_Member", None)
        self.__library_Member = value
        
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
    def library_Member8(self):
        return self.__library_Member8

    @library_Member8.setter
    def library_Member8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Member__library_Member8", None)
        self.__library_Member8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Book9"):
                    opp_val = getattr(item, "library_Book9", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Book9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Book9"):
                    opp_val = getattr(item, "library_Book9", None)
                    
                    setattr(item, "library_Book9", self)
                    

class library_Writer:

    def __init__(self, name: str, Writer: "library_Book" = None, author: set["library_Book"] = None, library_Writer: "library_Library" = None):
        self.name = name
        self.Writer = Writer
        self.author = author if author is not None else set()
        self.library_Writer = library_Writer
        
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

class library_Book:

    def __init__(self, title: str, pages: int, books: "library_Writer" = None, Book: "library_Writer" = None, library_Book9: "library_Member" = None, library_Book: "library_Library" = None):
        self.title = title
        self.pages = pages
        self.books = books
        self.Book = Book
        self.library_Book9 = library_Book9
        self.library_Book = library_Book
        
    @property
    def pages(self) -> int:
        return self.__pages

    @pages.setter
    def pages(self, pages: int):
        self.__pages = pages

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def library_Book9(self):
        return self.__library_Book9

    @library_Book9.setter
    def library_Book9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__library_Book9", None)
        self.__library_Book9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Member8"):
                opp_val = getattr(old_value, "library_Member8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Member8"):
                opp_val = getattr(value, "library_Member8", None)
                if opp_val is None:
                    setattr(value, "library_Member8", set([self]))
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

class library_Library:

    def __init__(self, name: str, library_Library: set["library_Book"] = None, library_Library2: set["library_Writer"] = None, library_Library4: set["library_Member"] = None):
        self.name = name
        self.library_Library = library_Library if library_Library is not None else set()
        self.library_Library2 = library_Library2 if library_Library2 is not None else set()
        self.library_Library4 = library_Library4 if library_Library4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
                if hasattr(item, "library_Member"):
                    opp_val = getattr(item, "library_Member", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Member", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Member"):
                    opp_val = getattr(item, "library_Member", None)
                    
                    setattr(item, "library_Member", self)
                    
