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


############################################
# Definition of Classes
############################################

class AudioVisualItem:

    pass
class extlibrary_BookOnTape(AudioVisualItem):

    pass
class Lendable:

    pass
class Item:

    pass
class extlibrary_Periodical(Item):

    def __init__(self, title: str, issuesPerYear: int):
        self.title = title
        self.issuesPerYear = issuesPerYear
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def issuesPerYear(self) -> int:
        return self.__issuesPerYear

    @issuesPerYear.setter
    def issuesPerYear(self, issuesPerYear: int):
        self.__issuesPerYear = issuesPerYear

class extlibrary_CirculatingItem(Lendable, Item):

    pass
class extlibrary_Lendable(ABC):

    def __init__(self, copies: int, Lendable: "extlibrary_Borrower" = None, borrowed: set["extlibrary_Borrower"] = None):
        self.copies = copies
        self.Lendable = Lendable
        self.borrowed = borrowed if borrowed is not None else set()
        
    @property
    def copies(self) -> int:
        return self.__copies

    @copies.setter
    def copies(self, copies: int):
        self.__copies = copies

    @property
    def borrowed(self):
        return self.__borrowed

    @borrowed.setter
    def borrowed(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_Lendable__borrowed", None)
        self.__borrowed = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Borrower"):
                    opp_val = getattr(item, "Borrower", None)
                    
                    if opp_val == self:
                        setattr(item, "Borrower", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Borrower"):
                    opp_val = getattr(item, "Borrower", None)
                    
                    setattr(item, "Borrower", self)
                    

    @property
    def Lendable(self):
        return self.__Lendable

    @Lendable.setter
    def Lendable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_Lendable__Lendable", None)
        self.__Lendable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "borrowers"):
                opp_val = getattr(old_value, "borrowers", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "borrowers"):
                opp_val = getattr(value, "borrowers", None)
                if opp_val is None:
                    setattr(value, "borrowers", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class extlibrary_Item(ABC):

    def __init__(self, publicationDate: date):
        self.publicationDate = publicationDate
        
    @property
    def publicationDate(self) -> date:
        return self.__publicationDate

    @publicationDate.setter
    def publicationDate(self, publicationDate: date):
        self.__publicationDate = publicationDate

class extlibrary_Addressable(ABC):

    def __init__(self, address: str):
        self.address = address
        
    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

class Addressable:

    pass
class extlibrary_Person(Addressable):

    def __init__(self, firstName: str, lastName: str, extlibrary_Person7: "extlibrary_VideoCassette" = None, extlibrary_Person: "extlibrary_BookOnTape" = None):
        self.firstName = firstName
        self.lastName = lastName
        self.extlibrary_Person7 = extlibrary_Person7
        self.extlibrary_Person = extlibrary_Person
        
    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def extlibrary_Person(self):
        return self.__extlibrary_Person

    @extlibrary_Person.setter
    def extlibrary_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_Person__extlibrary_Person", None)
        self.__extlibrary_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extlibrary_BookOnTape"):
                opp_val = getattr(old_value, "extlibrary_BookOnTape", None)
                if opp_val == self:
                    setattr(old_value, "extlibrary_BookOnTape", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extlibrary_BookOnTape"):
                opp_val = getattr(value, "extlibrary_BookOnTape", None)
                setattr(value, "extlibrary_BookOnTape", self)

    @property
    def extlibrary_Person7(self):
        return self.__extlibrary_Person7

    @extlibrary_Person7.setter
    def extlibrary_Person7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_Person__extlibrary_Person7", None)
        self.__extlibrary_Person7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extlibrary_VideoCassette"):
                opp_val = getattr(old_value, "extlibrary_VideoCassette", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extlibrary_VideoCassette"):
                opp_val = getattr(value, "extlibrary_VideoCassette", None)
                if opp_val is None:
                    setattr(value, "extlibrary_VideoCassette", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class extlibrary_VideoCassette(AudioVisualItem):

    pass
class Person:

    pass
class extlibrary_Borrower(Person):

    pass
class extlibrary_Employee(Person):

    pass
class extlibrary_Writer(Person):

    def __init__(self, name: str, Writer: "extlibrary_Book" = None, extlibrary_Writer: "extlibrary_BookOnTape" = None, author: set["extlibrary_Book"] = None):
        self.name = name
        self.Writer = Writer
        self.extlibrary_Writer = extlibrary_Writer
        self.author = author if author is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Writer(self):
        return self.__Writer

    @Writer.setter
    def Writer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_Writer__Writer", None)
        self.__Writer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "books"):
                opp_val = getattr(old_value, "books", None)
                if opp_val == self:
                    setattr(old_value, "books", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "books"):
                opp_val = getattr(value, "books", None)
                setattr(value, "books", self)

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_Writer__author", None)
        self.__author = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Book"):
                    opp_val = getattr(item, "Book", None)
                    
                    if opp_val == self:
                        setattr(item, "Book", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Book"):
                    opp_val = getattr(item, "Book", None)
                    
                    setattr(item, "Book", self)
                    

    @property
    def extlibrary_Writer(self):
        return self.__extlibrary_Writer

    @extlibrary_Writer.setter
    def extlibrary_Writer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_Writer__extlibrary_Writer", None)
        self.__extlibrary_Writer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extlibrary_BookOnTape5"):
                opp_val = getattr(old_value, "extlibrary_BookOnTape5", None)
                if opp_val == self:
                    setattr(old_value, "extlibrary_BookOnTape5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extlibrary_BookOnTape5"):
                opp_val = getattr(value, "extlibrary_BookOnTape5", None)
                setattr(value, "extlibrary_BookOnTape5", self)

class CirculatingItem:

    pass
class extlibrary_AudioVisualItem(CirculatingItem):

    def __init__(self, title: str, minutesLength: int, damaged: bool):
        self.title = title
        self.minutesLength = minutesLength
        self.damaged = damaged
        
    @property
    def minutesLength(self) -> int:
        return self.__minutesLength

    @minutesLength.setter
    def minutesLength(self, minutesLength: int):
        self.__minutesLength = minutesLength

    @property
    def damaged(self) -> bool:
        return self.__damaged

    @damaged.setter
    def damaged(self, damaged: bool):
        self.__damaged = damaged

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

class extlibrary_Book(CirculatingItem):

    def __init__(self, title: str, pages: int, category: str, books: "extlibrary_Writer" = None, Book: "extlibrary_Writer" = None):
        self.title = title
        self.pages = pages
        self.category = category
        self.books = books
        self.Book = Book
        
    @property
    def pages(self) -> int:
        return self.__pages

    @pages.setter
    def pages(self, pages: int):
        self.__pages = pages

    @property
    def category(self) -> str:
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def Book(self):
        return self.__Book

    @Book.setter
    def Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_Book__Book", None)
        self.__Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "author"):
                opp_val = getattr(old_value, "author", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "author"):
                opp_val = getattr(value, "author", None)
                if opp_val is None:
                    setattr(value, "author", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def books(self):
        return self.__books

    @books.setter
    def books(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_Book__books", None)
        self.__books = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Writer"):
                opp_val = getattr(old_value, "Writer", None)
                if opp_val == self:
                    setattr(old_value, "Writer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Writer"):
                opp_val = getattr(value, "Writer", None)
                setattr(value, "Writer", self)
