from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Book_Book:

    def __init__(self, title: str, authorName: str, Book_Book: set["Book_Chapter"] = None):
        self.title = title
        self.authorName = authorName
        self.Book_Book = Book_Book if Book_Book is not None else set()
        
    @property
    def authorName(self) -> str:
        return self.__authorName

    @authorName.setter
    def authorName(self, authorName: str):
        self.__authorName = authorName

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def Book_Book(self):
        return self.__Book_Book

    @Book_Book.setter
    def Book_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Book_Book__Book_Book", None)
        self.__Book_Book = value if value is not None else set()
        
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
                    

class Book_Chapter:

    def __init__(self, title: str, nbPages: int, Book_Chapter: "Book_Book" = None):
        self.title = title
        self.nbPages = nbPages
        self.Book_Chapter = Book_Chapter
        
    @property
    def nbPages(self) -> int:
        return self.__nbPages

    @nbPages.setter
    def nbPages(self, nbPages: int):
        self.__nbPages = nbPages

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
            if hasattr(old_value, "Book_Book"):
                opp_val = getattr(old_value, "Book_Book", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Book_Book"):
                opp_val = getattr(value, "Book_Book", None)
                if opp_val is None:
                    setattr(value, "Book_Book", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
