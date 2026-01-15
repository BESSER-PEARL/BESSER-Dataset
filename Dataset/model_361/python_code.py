from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Library_Book:

    def __init__(self, title: str, Library_Book: "Library_Library" = None, books: set["Library_Writer"] = None, Book: "Library_Writer" = None):
        self.title = title
        self.Library_Book = Library_Book
        self.books = books if books is not None else set()
        self.Book = Book
        
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
        self.__books = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Writer"):
                    opp_val = getattr(item, "Writer", None)
                    
                    if opp_val == self:
                        setattr(item, "Writer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Writer"):
                    opp_val = getattr(item, "Writer", None)
                    
                    setattr(item, "Writer", self)
                    

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
    def Library_Book(self):
        return self.__Library_Book

    @Library_Book.setter
    def Library_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Book__Library_Book", None)
        self.__Library_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Library_Library2"):
                opp_val = getattr(old_value, "Library_Library2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Library_Library2"):
                opp_val = getattr(value, "Library_Library2", None)
                if opp_val is None:
                    setattr(value, "Library_Library2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Library_Writer:

    def __init__(self, name: str, Library_Writer: "Library_Library" = None, Writer: "Library_Book" = None, author: set["Library_Book"] = None):
        self.name = name
        self.Library_Writer = Library_Writer
        self.Writer = Writer
        self.author = author if author is not None else set()
        
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
        old_value = getattr(self, f"_Library_Writer__Writer", None)
        self.__Writer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "books"):
                opp_val = getattr(old_value, "books", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "books"):
                opp_val = getattr(value, "books", None)
                if opp_val is None:
                    setattr(value, "books", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Writer__author", None)
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
    def Library_Writer(self):
        return self.__Library_Writer

    @Library_Writer.setter
    def Library_Writer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Writer__Library_Writer", None)
        self.__Library_Writer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Library_Library"):
                opp_val = getattr(old_value, "Library_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Library_Library"):
                opp_val = getattr(value, "Library_Library", None)
                if opp_val is None:
                    setattr(value, "Library_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Library_Library:

    def __init__(self, name: str, Library_Library: set["Library_Writer"] = None, Library_Library2: set["Library_Book"] = None):
        self.name = name
        self.Library_Library = Library_Library if Library_Library is not None else set()
        self.Library_Library2 = Library_Library2 if Library_Library2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Library_Library(self):
        return self.__Library_Library

    @Library_Library.setter
    def Library_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Library__Library_Library", None)
        self.__Library_Library = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Library_Writer"):
                    opp_val = getattr(item, "Library_Writer", None)
                    
                    if opp_val == self:
                        setattr(item, "Library_Writer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Library_Writer"):
                    opp_val = getattr(item, "Library_Writer", None)
                    
                    setattr(item, "Library_Writer", self)
                    

    @property
    def Library_Library2(self):
        return self.__Library_Library2

    @Library_Library2.setter
    def Library_Library2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Library__Library_Library2", None)
        self.__Library_Library2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Library_Book"):
                    opp_val = getattr(item, "Library_Book", None)
                    
                    if opp_val == self:
                        setattr(item, "Library_Book", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Library_Book"):
                    opp_val = getattr(item, "Library_Book", None)
                    
                    setattr(item, "Library_Book", self)
                    
