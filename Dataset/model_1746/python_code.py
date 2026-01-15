from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class mytry_Book:

    def __init__(self, title: str, books: set["mytry_Author"] = None, Book: "mytry_Author" = None, mytry_Book: "mytry_Library" = None):
        self.title = title
        self.books = books if books is not None else set()
        self.Book = Book
        self.mytry_Book = mytry_Book
        
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
        old_value = getattr(self, f"_mytry_Book__books", None)
        self.__books = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Author"):
                    opp_val = getattr(item, "Author", None)
                    
                    if opp_val == self:
                        setattr(item, "Author", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Author"):
                    opp_val = getattr(item, "Author", None)
                    
                    setattr(item, "Author", self)
                    

    @property
    def Book(self):
        return self.__Book

    @Book.setter
    def Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mytry_Book__Book", None)
        self.__Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "authors"):
                opp_val = getattr(old_value, "authors", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "authors"):
                opp_val = getattr(value, "authors", None)
                if opp_val is None:
                    setattr(value, "authors", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mytry_Book(self):
        return self.__mytry_Book

    @mytry_Book.setter
    def mytry_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mytry_Book__mytry_Book", None)
        self.__mytry_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mytry_Library"):
                opp_val = getattr(old_value, "mytry_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mytry_Library"):
                opp_val = getattr(value, "mytry_Library", None)
                if opp_val is None:
                    setattr(value, "mytry_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class mytry_Library:

    pass
class mytry_Author:

    def __init__(self, name: str, mytry_Author: "mytry_Library" = None, Author: "mytry_Book" = None, authors: set["mytry_Book"] = None):
        self.name = name
        self.mytry_Author = mytry_Author
        self.Author = Author
        self.authors = authors if authors is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mytry_Author__authors", None)
        self.__authors = value if value is not None else set()
        
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
    def Author(self):
        return self.__Author

    @Author.setter
    def Author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mytry_Author__Author", None)
        self.__Author = value
        
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
    def mytry_Author(self):
        return self.__mytry_Author

    @mytry_Author.setter
    def mytry_Author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mytry_Author__mytry_Author", None)
        self.__mytry_Author = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mytry_Library2"):
                opp_val = getattr(old_value, "mytry_Library2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mytry_Library2"):
                opp_val = getattr(value, "mytry_Library2", None)
                if opp_val is None:
                    setattr(value, "mytry_Library2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
