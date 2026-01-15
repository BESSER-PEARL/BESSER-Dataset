from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class books_Writer:

    pass
class books_Book:

    def __init__(self, isbn: str, title: str, pages: int, books_Book: "books_Catalog" = None, books: set["books_Writer"] = None):
        self.isbn = isbn
        self.title = title
        self.pages = pages
        self.books_Book = books_Book
        self.books = books if books is not None else set()
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def isbn(self) -> str:
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn: str):
        self.__isbn = isbn

    @property
    def pages(self) -> int:
        return self.__pages

    @pages.setter
    def pages(self, pages: int):
        self.__pages = pages

    @property
    def books(self):
        return self.__books

    @books.setter
    def books(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_books_Book__books", None)
        self.__books = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "writers.ecoreWriter"):
                    opp_val = getattr(item, "writers.ecoreWriter", None)
                    
                    if opp_val == self:
                        setattr(item, "writers.ecoreWriter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "writers.ecoreWriter"):
                    opp_val = getattr(item, "writers.ecoreWriter", None)
                    
                    setattr(item, "writers.ecoreWriter", self)
                    

    @property
    def books_Book(self):
        return self.__books_Book

    @books_Book.setter
    def books_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_books_Book__books_Book", None)
        self.__books_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "books_Catalog"):
                opp_val = getattr(old_value, "books_Catalog", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "books_Catalog"):
                opp_val = getattr(value, "books_Catalog", None)
                if opp_val is None:
                    setattr(value, "books_Catalog", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class books_Catalog:

    pass