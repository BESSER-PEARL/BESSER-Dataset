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

class Lendable:

    pass
class extlibrary_Addressable(ABC):

    def __init__(self, address: str):
        self.address = address
        
    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

class extlibrary_Item(ABC):

    def __init__(self, publicationDate: date, extlibrary_Item: "extlibrary_Library" = None):
        self.publicationDate = publicationDate
        self.extlibrary_Item = extlibrary_Item
        
    @property
    def publicationDate(self) -> date:
        return self.__publicationDate

    @publicationDate.setter
    def publicationDate(self, publicationDate: date):
        self.__publicationDate = publicationDate

    @property
    def extlibrary_Item(self):
        return self.__extlibrary_Item

    @extlibrary_Item.setter
    def extlibrary_Item(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_Item__extlibrary_Item", None)
        self.__extlibrary_Item = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extlibrary_Library7"):
                opp_val = getattr(old_value, "extlibrary_Library7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extlibrary_Library7"):
                opp_val = getattr(value, "extlibrary_Library7", None)
                if opp_val is None:
                    setattr(value, "extlibrary_Library7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class AudioVisualItem:

    pass
class extlibrary_VideoCassette(AudioVisualItem):

    pass
class extlibrary_BookOnTape(AudioVisualItem):

    pass
class Item:

    pass
class extlibrary_Periodical(Item):

    def __init__(self, title: str, issuesPerYear: int):
        self.title = title
        self.issuesPerYear = issuesPerYear
        
    @property
    def issuesPerYear(self) -> int:
        return self.__issuesPerYear

    @issuesPerYear.setter
    def issuesPerYear(self, issuesPerYear: int):
        self.__issuesPerYear = issuesPerYear

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

class extlibrary_CirculatingItem(Lendable, Item):

    pass
class extlibrary_Lendable(ABC):

    def __init__(self, copies: int, borrowed: set["extlibrary_Borrower"] = None, Lendable: "extlibrary_Borrower" = None):
        self.copies = copies
        self.borrowed = borrowed if borrowed is not None else set()
        self.Lendable = Lendable
        
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

class Person:

    pass
class extlibrary_Employee(Person):

    pass
class extlibrary_Borrower(Person):

    pass
class Addressable:

    pass
class extlibrary_Person(Addressable):

    def __init__(self, firstName: str, lastName: str, extlibrary_Person: "extlibrary_BookOnTape" = None, extlibrary_Person22: "extlibrary_VideoCassette" = None):
        self.firstName = firstName
        self.lastName = lastName
        self.extlibrary_Person = extlibrary_Person
        self.extlibrary_Person22 = extlibrary_Person22
        
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
    def extlibrary_Person22(self):
        return self.__extlibrary_Person22

    @extlibrary_Person22.setter
    def extlibrary_Person22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_Person__extlibrary_Person22", None)
        self.__extlibrary_Person22 = value
        
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

class extlibrary_Library(Addressable):

    def __init__(self, name: str, people: str, extlibrary_Library: set["extlibrary_Writer"] = None, extlibrary_Library7: set["extlibrary_Item"] = None, extlibrary_Library9: set["extlibrary_Book"] = None, Library: "extlibrary_Library" = None, parentBranch: set["extlibrary_Library"] = None, Library14: "extlibrary_Library" = None, branches: "extlibrary_Library" = None, extlibrary_Library3: set["extlibrary_Employee"] = None, extlibrary_Library5: set["extlibrary_Borrower"] = None):
        self.name = name
        self.people = people
        self.extlibrary_Library = extlibrary_Library if extlibrary_Library is not None else set()
        self.extlibrary_Library7 = extlibrary_Library7 if extlibrary_Library7 is not None else set()
        self.extlibrary_Library9 = extlibrary_Library9 if extlibrary_Library9 is not None else set()
        self.Library = Library
        self.parentBranch = parentBranch if parentBranch is not None else set()
        self.Library14 = Library14
        self.branches = branches
        self.extlibrary_Library3 = extlibrary_Library3 if extlibrary_Library3 is not None else set()
        self.extlibrary_Library5 = extlibrary_Library5 if extlibrary_Library5 is not None else set()
        
    @property
    def people(self) -> str:
        return self.__people

    @people.setter
    def people(self, people: str):
        self.__people = people

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Library(self):
        return self.__Library

    @Library.setter
    def Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_Library__Library", None)
        self.__Library = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parentBranch"):
                opp_val = getattr(old_value, "parentBranch", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parentBranch"):
                opp_val = getattr(value, "parentBranch", None)
                if opp_val is None:
                    setattr(value, "parentBranch", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def extlibrary_Library7(self):
        return self.__extlibrary_Library7

    @extlibrary_Library7.setter
    def extlibrary_Library7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_Library__extlibrary_Library7", None)
        self.__extlibrary_Library7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "extlibrary_Item"):
                    opp_val = getattr(item, "extlibrary_Item", None)
                    
                    if opp_val == self:
                        setattr(item, "extlibrary_Item", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "extlibrary_Item"):
                    opp_val = getattr(item, "extlibrary_Item", None)
                    
                    setattr(item, "extlibrary_Item", self)
                    

    @property
    def extlibrary_Library5(self):
        return self.__extlibrary_Library5

    @extlibrary_Library5.setter
    def extlibrary_Library5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_Library__extlibrary_Library5", None)
        self.__extlibrary_Library5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "extlibrary_Borrower"):
                    opp_val = getattr(item, "extlibrary_Borrower", None)
                    
                    if opp_val == self:
                        setattr(item, "extlibrary_Borrower", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "extlibrary_Borrower"):
                    opp_val = getattr(item, "extlibrary_Borrower", None)
                    
                    setattr(item, "extlibrary_Borrower", self)
                    

    @property
    def extlibrary_Library3(self):
        return self.__extlibrary_Library3

    @extlibrary_Library3.setter
    def extlibrary_Library3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_Library__extlibrary_Library3", None)
        self.__extlibrary_Library3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "extlibrary_Employee"):
                    opp_val = getattr(item, "extlibrary_Employee", None)
                    
                    if opp_val == self:
                        setattr(item, "extlibrary_Employee", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "extlibrary_Employee"):
                    opp_val = getattr(item, "extlibrary_Employee", None)
                    
                    setattr(item, "extlibrary_Employee", self)
                    

    @property
    def extlibrary_Library9(self):
        return self.__extlibrary_Library9

    @extlibrary_Library9.setter
    def extlibrary_Library9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_Library__extlibrary_Library9", None)
        self.__extlibrary_Library9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "extlibrary_Book"):
                    opp_val = getattr(item, "extlibrary_Book", None)
                    
                    if opp_val == self:
                        setattr(item, "extlibrary_Book", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "extlibrary_Book"):
                    opp_val = getattr(item, "extlibrary_Book", None)
                    
                    setattr(item, "extlibrary_Book", self)
                    

    @property
    def parentBranch(self):
        return self.__parentBranch

    @parentBranch.setter
    def parentBranch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_Library__parentBranch", None)
        self.__parentBranch = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Library"):
                    opp_val = getattr(item, "Library", None)
                    
                    if opp_val == self:
                        setattr(item, "Library", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Library"):
                    opp_val = getattr(item, "Library", None)
                    
                    setattr(item, "Library", self)
                    

    @property
    def extlibrary_Library(self):
        return self.__extlibrary_Library

    @extlibrary_Library.setter
    def extlibrary_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_Library__extlibrary_Library", None)
        self.__extlibrary_Library = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "extlibrary_Writer"):
                    opp_val = getattr(item, "extlibrary_Writer", None)
                    
                    if opp_val == self:
                        setattr(item, "extlibrary_Writer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "extlibrary_Writer"):
                    opp_val = getattr(item, "extlibrary_Writer", None)
                    
                    setattr(item, "extlibrary_Writer", self)
                    

    @property
    def Library14(self):
        return self.__Library14

    @Library14.setter
    def Library14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_Library__Library14", None)
        self.__Library14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "branches"):
                opp_val = getattr(old_value, "branches", None)
                if opp_val == self:
                    setattr(old_value, "branches", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "branches"):
                opp_val = getattr(value, "branches", None)
                setattr(value, "branches", self)

    @property
    def branches(self):
        return self.__branches

    @branches.setter
    def branches(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_Library__branches", None)
        self.__branches = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Library14"):
                opp_val = getattr(old_value, "Library14", None)
                if opp_val == self:
                    setattr(old_value, "Library14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Library14"):
                opp_val = getattr(value, "Library14", None)
                setattr(value, "Library14", self)

class extlibrary_Writer(Person):

    def __init__(self, name: str, Writer: "extlibrary_Book" = None, extlibrary_Writer: "extlibrary_Library" = None, author: set["extlibrary_Book"] = None, extlibrary_Writer20: "extlibrary_BookOnTape" = None):
        self.name = name
        self.Writer = Writer
        self.extlibrary_Writer = extlibrary_Writer
        self.author = author if author is not None else set()
        self.extlibrary_Writer20 = extlibrary_Writer20
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def extlibrary_Writer20(self):
        return self.__extlibrary_Writer20

    @extlibrary_Writer20.setter
    def extlibrary_Writer20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_Writer__extlibrary_Writer20", None)
        self.__extlibrary_Writer20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extlibrary_BookOnTape19"):
                opp_val = getattr(old_value, "extlibrary_BookOnTape19", None)
                if opp_val == self:
                    setattr(old_value, "extlibrary_BookOnTape19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extlibrary_BookOnTape19"):
                opp_val = getattr(value, "extlibrary_BookOnTape19", None)
                setattr(value, "extlibrary_BookOnTape19", self)

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
    def extlibrary_Writer(self):
        return self.__extlibrary_Writer

    @extlibrary_Writer.setter
    def extlibrary_Writer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_Writer__extlibrary_Writer", None)
        self.__extlibrary_Writer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extlibrary_Library"):
                opp_val = getattr(old_value, "extlibrary_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extlibrary_Library"):
                opp_val = getattr(value, "extlibrary_Library", None)
                if opp_val is None:
                    setattr(value, "extlibrary_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
                    

class CirculatingItem:

    pass
class extlibrary_AudioVisualItem(CirculatingItem):

    def __init__(self, title: str, minutesLength: int, damaged: bool):
        self.title = title
        self.minutesLength = minutesLength
        self.damaged = damaged
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def damaged(self) -> bool:
        return self.__damaged

    @damaged.setter
    def damaged(self, damaged: bool):
        self.__damaged = damaged

    @property
    def minutesLength(self) -> int:
        return self.__minutesLength

    @minutesLength.setter
    def minutesLength(self, minutesLength: int):
        self.__minutesLength = minutesLength

class extlibrary_Book(CirculatingItem):

    def __init__(self, title: str, pages: int, category: str, books: "extlibrary_Writer" = None, extlibrary_Book: "extlibrary_Library" = None, Book: "extlibrary_Writer" = None):
        self.title = title
        self.pages = pages
        self.category = category
        self.books = books
        self.extlibrary_Book = extlibrary_Book
        self.Book = Book
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def category(self) -> str:
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category

    @property
    def pages(self) -> int:
        return self.__pages

    @pages.setter
    def pages(self, pages: int):
        self.__pages = pages

    @property
    def extlibrary_Book(self):
        return self.__extlibrary_Book

    @extlibrary_Book.setter
    def extlibrary_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_Book__extlibrary_Book", None)
        self.__extlibrary_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extlibrary_Library9"):
                opp_val = getattr(old_value, "extlibrary_Library9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extlibrary_Library9"):
                opp_val = getattr(value, "extlibrary_Library9", None)
                if opp_val is None:
                    setattr(value, "extlibrary_Library9", set([self]))
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
