from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Book_Library:

    pass
class Book_Summary:

    def __init__(self, content: str, nbWords: int, Book_Summary: "Book_Chapter" = None):
        self.content = content
        self.nbWords = nbWords
        self.Book_Summary = Book_Summary
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def nbWords(self) -> int:
        return self.__nbWords

    @nbWords.setter
    def nbWords(self, nbWords: int):
        self.__nbWords = nbWords

    @property
    def Book_Summary(self):
        return self.__Book_Summary

    @Book_Summary.setter
    def Book_Summary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Book_Summary__Book_Summary", None)
        self.__Book_Summary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Book_Chapter2"):
                opp_val = getattr(old_value, "Book_Chapter2", None)
                if opp_val == self:
                    setattr(old_value, "Book_Chapter2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Book_Chapter2"):
                opp_val = getattr(value, "Book_Chapter2", None)
                setattr(value, "Book_Chapter2", self)

class Book_Chapter:

    def __init__(self, title: str, nbPages: int, author: str, Book_Chapter: "Book_Book" = None, Book_Chapter2: "Book_Summary" = None):
        self.title = title
        self.nbPages = nbPages
        self.author = author
        self.Book_Chapter = Book_Chapter
        self.Book_Chapter2 = Book_Chapter2
        
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
    def Book_Chapter2(self):
        return self.__Book_Chapter2

    @Book_Chapter2.setter
    def Book_Chapter2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Book_Chapter__Book_Chapter2", None)
        self.__Book_Chapter2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Book_Summary"):
                opp_val = getattr(old_value, "Book_Summary", None)
                if opp_val == self:
                    setattr(old_value, "Book_Summary", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Book_Summary"):
                opp_val = getattr(value, "Book_Summary", None)
                setattr(value, "Book_Summary", self)

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

class Book_Book:

    def __init__(self, title: str, Book_Book: set["Book_Chapter"] = None, Book_Book4: "Book_Library" = None):
        self.title = title
        self.Book_Book = Book_Book if Book_Book is not None else set()
        self.Book_Book4 = Book_Book4
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def Book_Book4(self):
        return self.__Book_Book4

    @Book_Book4.setter
    def Book_Book4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Book_Book__Book_Book4", None)
        self.__Book_Book4 = value
        
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
                    
