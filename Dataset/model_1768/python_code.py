from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Book_Chapter:

    def __init__(self, title: str, nbPages: int, author: str, Book_Chapter: "Book_Book" = None, Book_Chapter4: "Book_Book" = None):
        self.title = title
        self.nbPages = nbPages
        self.author = author
        self.Book_Chapter = Book_Chapter
        self.Book_Chapter4 = Book_Chapter4
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def nbPages(self) -> int:
        return self.__nbPages

    @nbPages.setter
    def nbPages(self, nbPages: int):
        self.__nbPages = nbPages

    @property
    def author(self) -> str:
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

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
            if hasattr(old_value, "Book_Book2"):
                opp_val = getattr(old_value, "Book_Book2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Book_Book2"):
                opp_val = getattr(value, "Book_Book2", None)
                if opp_val is None:
                    setattr(value, "Book_Book2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Book_Chapter4(self):
        return self.__Book_Chapter4

    @Book_Chapter4.setter
    def Book_Chapter4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Book_Chapter__Book_Chapter4", None)
        self.__Book_Chapter4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Book_Book5"):
                opp_val = getattr(old_value, "Book_Book5", None)
                if opp_val == self:
                    setattr(old_value, "Book_Book5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Book_Book5"):
                opp_val = getattr(value, "Book_Book5", None)
                setattr(value, "Book_Book5", self)

class Book_Book:

    def __init__(self, title: str, Book_Book2: set["Book_Chapter"] = None, Book_Book5: "Book_Chapter" = None, Book_Book: "Book_Books" = None):
        self.title = title
        self.Book_Book2 = Book_Book2 if Book_Book2 is not None else set()
        self.Book_Book5 = Book_Book5
        self.Book_Book = Book_Book
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def Book_Book2(self):
        return self.__Book_Book2

    @Book_Book2.setter
    def Book_Book2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Book_Book__Book_Book2", None)
        self.__Book_Book2 = value if value is not None else set()
        
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
                    

    @property
    def Book_Book5(self):
        return self.__Book_Book5

    @Book_Book5.setter
    def Book_Book5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Book_Book__Book_Book5", None)
        self.__Book_Book5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Book_Chapter4"):
                opp_val = getattr(old_value, "Book_Chapter4", None)
                if opp_val == self:
                    setattr(old_value, "Book_Chapter4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Book_Chapter4"):
                opp_val = getattr(value, "Book_Chapter4", None)
                setattr(value, "Book_Chapter4", self)

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
            if hasattr(old_value, "Book_Books"):
                opp_val = getattr(old_value, "Book_Books", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Book_Books"):
                opp_val = getattr(value, "Book_Books", None)
                if opp_val is None:
                    setattr(value, "Book_Books", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Book_Books:

    pass