from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Book_Chapter:

    def __init__(self, author: str, title: str, nbPages: int, 02: "Book" = None):
        self.author = author
        self.title = title
        self.nbPages = nbPages
        self.02 = 02
        
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
    def nbPages(self) -> int:
        return self.__nbPages

    @nbPages.setter
    def nbPages(self, nbPages: int):
        self.__nbPages = nbPages

    @property
    def 02(self):
        return self.__02

    @02.setter
    def 02(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Book_Chapter__02", None)
        self.__02 = value
        
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

class Chapter:

    pass
class Book_Book:

    def __init__(self, title: str, 0: set["Chapter"] = None):
        self.title = title
        self.0 = 0 if 0 is not None else set()
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def 0(self):
        return self.__0

    @0.setter
    def 0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Book_Book__0", None)
        self.__0 = value if value is not None else set()
        
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