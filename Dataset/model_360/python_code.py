from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class BookCategory(Enum):
    Mystery = "Mystery"
    ScienceFiction = "ScienceFiction"
    Biography = "Biography"
    Computing = "Computing"


############################################
# Definition of Classes
############################################

class Person:

    pass
class tinylibrary_Person(ABC):

    def __init__(self, firstName: str, lastName: str, name: str):
        self.firstName = firstName
        self.lastName = lastName
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

class tinylibrary_Writer(Person):

    pass
class tinylibrary_Employee(Person):

    pass
class tinylibrary_Book:

    def __init__(self, isbn: str, title: str, category: str, pages: str, published: date, damaged: str, tinylibrary_Book: "tinylibrary_Library" = None, Book: "tinylibrary_Writer" = None, books: set["tinylibrary_Writer"] = None):
        self.isbn = isbn
        self.title = title
        self.category = category
        self.pages = pages
        self.published = published
        self.damaged = damaged
        self.tinylibrary_Book = tinylibrary_Book
        self.Book = Book
        self.books = books if books is not None else set()
        
    @property
    def damaged(self) -> str:
        return self.__damaged

    @damaged.setter
    def damaged(self, damaged: str):
        self.__damaged = damaged

    @property
    def isbn(self) -> str:
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn: str):
        self.__isbn = isbn

    @property
    def category(self) -> str:
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category

    @property
    def pages(self) -> str:
        return self.__pages

    @pages.setter
    def pages(self, pages: str):
        self.__pages = pages

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def published(self) -> date:
        return self.__published

    @published.setter
    def published(self, published: date):
        self.__published = published

    @property
    def books(self):
        return self.__books

    @books.setter
    def books(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tinylibrary_Book__books", None)
        self.__books = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Writer"):
                    opp_val = getattr(item, "Writer", None)
                    
                    if opp_val == self:
                        setattr(item, "Writer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Writer"):
                    opp_val = getattr(item, "Writer", None)
                    
                    setattr(item, "Writer", self)
                    

    @property
    def tinylibrary_Book(self):
        return self.__tinylibrary_Book

    @tinylibrary_Book.setter
    def tinylibrary_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tinylibrary_Book__tinylibrary_Book", None)
        self.__tinylibrary_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tinylibrary_Library"):
                opp_val = getattr(old_value, "tinylibrary_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tinylibrary_Library"):
                opp_val = getattr(value, "tinylibrary_Library", None)
                if opp_val is None:
                    setattr(value, "tinylibrary_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Book(self):
        return self.__Book

    @Book.setter
    def Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tinylibrary_Book__Book", None)
        self.__Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "authors"):
                opp_val = getattr(old_value, "authors", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "authors"):
                opp_val = getattr(value, "authors", None)
                if opp_val is None:
                    setattr(value, "authors", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class tinylibrary_Library:

    pass