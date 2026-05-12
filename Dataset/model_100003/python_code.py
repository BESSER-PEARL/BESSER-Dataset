from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Book:

    pass
class Book_Chapter:

    def __init__(self, title: str, nbPages: str, author: str, chapters: "Book" = None):
        self.title = title
        self.nbPages = nbPages
        self.author = author
        self.chapters = chapters
        
        pass
    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def nbPages(self):
        return self.__nbPages

    @nbPages.setter
    def nbPages(self, nbPages: str):
        self.__nbPages = nbPages


    @property
    def chapters(self):
        return self.__chapters

    @chapters.setter
    def chapters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Book_Chapter__chapters", None)
        self.__chapters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Book"):
                opp_val = getattr(old_value, "Book", None)
                if opp_val == self:
                    setattr(old_value, "Book", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Book"):
                opp_val = getattr(value, "Book", None)
                setattr(value, "Book", self)

class Chapter:

    pass
class Book_Book:

    def __init__(self, title: str, book: set["Chapter"] = None):
        self.title = title
        self.book = book if book is not None else set()
        
        pass
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def book(self):
        return self.__book

    @book.setter
    def book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Book_Book__book", None)
        self.__book = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Chapter"):
                    opp_val = getattr(item, "Chapter", None)
                    
                    if opp_val == self:
                        setattr(item, "Chapter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Chapter"):
                    opp_val = getattr(item, "Chapter", None)
                    
                    setattr(item, "Chapter", self)
                    
