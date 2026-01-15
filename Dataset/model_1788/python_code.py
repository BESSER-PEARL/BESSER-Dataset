from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class BOOKS_Book:

    def __init__(self, title: str, BOOKS_Book: set["BOOKS_Chapter"] = None):
        self.title = title
        self.BOOKS_Book = BOOKS_Book if BOOKS_Book is not None else set()
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def BOOKS_Book(self):
        return self.__BOOKS_Book

    @BOOKS_Book.setter
    def BOOKS_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BOOKS_Book__BOOKS_Book", None)
        self.__BOOKS_Book = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BOOKS_Chapter"):
                    opp_val = getattr(item, "BOOKS_Chapter", None)
                    
                    if opp_val == self:
                        setattr(item, "BOOKS_Chapter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BOOKS_Chapter"):
                    opp_val = getattr(item, "BOOKS_Chapter", None)
                    
                    setattr(item, "BOOKS_Chapter", self)
                    

class BOOKS_Chapter:

    def __init__(self, title: str, nbPages: int, BOOKS_Chapter: "BOOKS_Book" = None):
        self.title = title
        self.nbPages = nbPages
        self.BOOKS_Chapter = BOOKS_Chapter
        
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
    def BOOKS_Chapter(self):
        return self.__BOOKS_Chapter

    @BOOKS_Chapter.setter
    def BOOKS_Chapter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BOOKS_Chapter__BOOKS_Chapter", None)
        self.__BOOKS_Chapter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BOOKS_Book"):
                opp_val = getattr(old_value, "BOOKS_Book", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BOOKS_Book"):
                opp_val = getattr(value, "BOOKS_Book", None)
                if opp_val is None:
                    setattr(value, "BOOKS_Book", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
