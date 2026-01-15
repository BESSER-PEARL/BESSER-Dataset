from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Book_Chapter:

    def __init__(self, title: str, nbPages: int, author: str, Chapter: "Book_Book" = None, chapters: "Book_Book" = None):
        self.title = title
        self.nbPages = nbPages
        self.author = author
        self.Chapter = Chapter
        self.chapters = chapters
        
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
    def Chapter(self):
        return self.__Chapter

    @Chapter.setter
    def Chapter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Book_Chapter__Chapter", None)
        self.__Chapter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "book"):
                opp_val = getattr(old_value, "book", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "book"):
                opp_val = getattr(value, "book", None)
                if opp_val is None:
                    setattr(value, "book", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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

class Book_Book:

    def __init__(self, title: str, book: set["Book_Chapter"] = None, Book: "Book_Chapter" = None):
        self.title = title
        self.book = book if book is not None else set()
        self.Book = Book
        
    @property
    def title(self) -> str:
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
                    

    @property
    def Book(self):
        return self.__Book

    @Book.setter
    def Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Book_Book__Book", None)
        self.__Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "chapters"):
                opp_val = getattr(old_value, "chapters", None)
                if opp_val == self:
                    setattr(old_value, "chapters", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "chapters"):
                opp_val = getattr(value, "chapters", None)
                setattr(value, "chapters", self)
