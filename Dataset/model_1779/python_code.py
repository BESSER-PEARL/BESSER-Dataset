from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Chapter:

    pass
class Book_Book:

    def __init__(self, title: str, 1: set["Chapter"] = None):
        self.title = title
        self.1 = 1 if 1 is not None else set()
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def 1(self):
        return self.__1

    @1.setter
    def 1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Book_Book__1", None)
        self.__1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "#"):
                    opp_val = getattr(item, "#", None)
                    
                    if opp_val == self:
                        setattr(item, "#", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "#"):
                    opp_val = getattr(item, "#", None)
                    
                    setattr(item, "#", self)
                    

class Book:

    pass
class Book_Chapter:

    def __init__(self, title: str, nbPages: int, author: str, 12: "Book" = None):
        self.title = title
        self.nbPages = nbPages
        self.author = author
        self.12 = 12
        
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
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def 12(self):
        return self.__12

    @12.setter
    def 12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Book_Chapter__12", None)
        self.__12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "#3"):
                opp_val = getattr(old_value, "#3", None)
                if opp_val == self:
                    setattr(old_value, "#3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "#3"):
                opp_val = getattr(value, "#3", None)
                setattr(value, "#3", self)
