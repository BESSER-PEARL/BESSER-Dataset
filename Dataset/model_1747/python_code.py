from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Book_Chapter:

    def __init__(self, title: str, Book_Chapter: "Book_Book" = None):
        self.title = title
        self.Book_Chapter = Book_Chapter
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def Book_Chapter(self):
        return self.__Book_Chapter

    @Book_Chapter.setter
    def Book_Chapter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Book_Chapter__Book_Chapter", None)
        self.__Book_Chapter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Book_Book7"):
                opp_val = getattr(old_value, "Book_Book7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Book_Book7"):
                opp_val = getattr(value, "Book_Book7", None)
                if opp_val is None:
                    setattr(value, "Book_Book7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Book_Author:

    def __init__(self, name: str, Book_Author: "Book_Library" = None, Book_Author5: "Book_Book" = None):
        self.name = name
        self.Book_Author = Book_Author
        self.Book_Author5 = Book_Author5
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Book_Author5(self):
        return self.__Book_Author5

    @Book_Author5.setter
    def Book_Author5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Book_Author__Book_Author5", None)
        self.__Book_Author5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Book_Book4"):
                opp_val = getattr(old_value, "Book_Book4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Book_Book4"):
                opp_val = getattr(value, "Book_Book4", None)
                if opp_val is None:
                    setattr(value, "Book_Book4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Book_Author(self):
        return self.__Book_Author

    @Book_Author.setter
    def Book_Author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Book_Author__Book_Author", None)
        self.__Book_Author = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Book_Library2"):
                opp_val = getattr(old_value, "Book_Library2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Book_Library2"):
                opp_val = getattr(value, "Book_Library2", None)
                if opp_val is None:
                    setattr(value, "Book_Library2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Book_Book:

    def __init__(self, isbn: str, title: str, nbpages: int, Book_Book: "Book_Library" = None, Book_Book4: set["Book_Author"] = None, Book_Book7: set["Book_Chapter"] = None):
        self.isbn = isbn
        self.title = title
        self.nbpages = nbpages
        self.Book_Book = Book_Book
        self.Book_Book4 = Book_Book4 if Book_Book4 is not None else set()
        self.Book_Book7 = Book_Book7 if Book_Book7 is not None else set()
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def nbpages(self) -> int:
        return self.__nbpages

    @nbpages.setter
    def nbpages(self, nbpages: int):
        self.__nbpages = nbpages

    @property
    def isbn(self) -> str:
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn: str):
        self.__isbn = isbn

    @property
    def Book_Book4(self):
        return self.__Book_Book4

    @Book_Book4.setter
    def Book_Book4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Book_Book__Book_Book4", None)
        self.__Book_Book4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Book_Author5"):
                    opp_val = getattr(item, "Book_Author5", None)
                    
                    if opp_val == self:
                        setattr(item, "Book_Author5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Book_Author5"):
                    opp_val = getattr(item, "Book_Author5", None)
                    
                    setattr(item, "Book_Author5", self)
                    

    @property
    def Book_Book(self):
        return self.__Book_Book

    @Book_Book.setter
    def Book_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Book_Book__Book_Book", None)
        self.__Book_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Book_Library"):
                opp_val = getattr(old_value, "Book_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Book_Library"):
                opp_val = getattr(value, "Book_Library", None)
                if opp_val is None:
                    setattr(value, "Book_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Book_Book7(self):
        return self.__Book_Book7

    @Book_Book7.setter
    def Book_Book7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Book_Book__Book_Book7", None)
        self.__Book_Book7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Book_Chapter"):
                    opp_val = getattr(item, "Book_Chapter", None)
                    
                    if opp_val == self:
                        setattr(item, "Book_Chapter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Book_Chapter"):
                    opp_val = getattr(item, "Book_Chapter", None)
                    
                    setattr(item, "Book_Chapter", self)
                    

class Book_Library:

    pass