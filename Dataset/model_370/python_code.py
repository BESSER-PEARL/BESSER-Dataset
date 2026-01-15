from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class library_Author:

    def __init__(self, name: str, author: set["library_Book"] = None, Author: "library_Book" = None, library_Author: "library_Library" = None):
        self.name = name
        self.author = author if author is not None else set()
        self.Author = Author
        self.library_Author = library_Author
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Author(self):
        return self.__Author

    @Author.setter
    def Author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Author__Author", None)
        self.__Author = value
        
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
        old_value = getattr(self, f"_library_Author__author", None)
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
    def library_Author(self):
        return self.__library_Author

    @library_Author.setter
    def library_Author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Author__library_Author", None)
        self.__library_Author = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Library6"):
                opp_val = getattr(old_value, "library_Library6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library6"):
                opp_val = getattr(value, "library_Library6", None)
                if opp_val is None:
                    setattr(value, "library_Library6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class library_Library:

    def __init__(self, name: str, library_Library: set["library_Shelf"] = None, library_Library6: set["library_Author"] = None, library_Library8: set["library_Employee"] = None):
        self.name = name
        self.library_Library = library_Library if library_Library is not None else set()
        self.library_Library6 = library_Library6 if library_Library6 is not None else set()
        self.library_Library8 = library_Library8 if library_Library8 is not None else set()
        
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
                if hasattr(item, "library_Shelf4"):
                    opp_val = getattr(item, "library_Shelf4", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Shelf4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Shelf4"):
                    opp_val = getattr(item, "library_Shelf4", None)
                    
                    setattr(item, "library_Shelf4", self)
                    

    @property
    def library_Library6(self):
        return self.__library_Library6

    @library_Library6.setter
    def library_Library6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library6", None)
        self.__library_Library6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Author"):
                    opp_val = getattr(item, "library_Author", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Author", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Author"):
                    opp_val = getattr(item, "library_Author", None)
                    
                    setattr(item, "library_Author", self)
                    

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
                if hasattr(item, "library_Employee9"):
                    opp_val = getattr(item, "library_Employee9", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Employee9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Employee9"):
                    opp_val = getattr(item, "library_Employee9", None)
                    
                    setattr(item, "library_Employee9", self)
                    

class library_Shelf:

    def __init__(self, name: str, library_Shelf: "library_Employee" = None, library_Shelf4: "library_Library" = None, library_Shelf11: set["library_Book"] = None):
        self.name = name
        self.library_Shelf = library_Shelf
        self.library_Shelf4 = library_Shelf4
        self.library_Shelf11 = library_Shelf11 if library_Shelf11 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def library_Shelf(self):
        return self.__library_Shelf

    @library_Shelf.setter
    def library_Shelf(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Shelf__library_Shelf", None)
        self.__library_Shelf = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Employee"):
                opp_val = getattr(old_value, "library_Employee", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Employee"):
                opp_val = getattr(value, "library_Employee", None)
                if opp_val is None:
                    setattr(value, "library_Employee", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Shelf4(self):
        return self.__library_Shelf4

    @library_Shelf4.setter
    def library_Shelf4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Shelf__library_Shelf4", None)
        self.__library_Shelf4 = value
        
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
    def library_Shelf11(self):
        return self.__library_Shelf11

    @library_Shelf11.setter
    def library_Shelf11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Shelf__library_Shelf11", None)
        self.__library_Shelf11 = value if value is not None else set()
        
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
                    

class library_Employee:

    def __init__(self, name: str, library_Employee: set["library_Shelf"] = None, library_Employee9: "library_Library" = None):
        self.name = name
        self.library_Employee = library_Employee if library_Employee is not None else set()
        self.library_Employee9 = library_Employee9
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def library_Employee9(self):
        return self.__library_Employee9

    @library_Employee9.setter
    def library_Employee9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Employee__library_Employee9", None)
        self.__library_Employee9 = value
        
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
    def library_Employee(self):
        return self.__library_Employee

    @library_Employee.setter
    def library_Employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Employee__library_Employee", None)
        self.__library_Employee = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Shelf"):
                    opp_val = getattr(item, "library_Shelf", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Shelf", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Shelf"):
                    opp_val = getattr(item, "library_Shelf", None)
                    
                    setattr(item, "library_Shelf", self)
                    

class library_Book:

    def __init__(self, title: str, Book: "library_Author" = None, books: "library_Author" = None, library_Book: "library_Shelf" = None):
        self.title = title
        self.Book = Book
        self.books = books
        self.library_Book = library_Book
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

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
            if hasattr(old_value, "library_Shelf11"):
                opp_val = getattr(old_value, "library_Shelf11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Shelf11"):
                opp_val = getattr(value, "library_Shelf11", None)
                if opp_val is None:
                    setattr(value, "library_Shelf11", set([self]))
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
            if hasattr(old_value, "Author"):
                opp_val = getattr(old_value, "Author", None)
                if opp_val == self:
                    setattr(old_value, "Author", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Author"):
                opp_val = getattr(value, "Author", None)
                setattr(value, "Author", self)
