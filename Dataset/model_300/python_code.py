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
class library_VideoCassette(AudioVisualItem):

    pass
class library_BookOnTape(AudioVisualItem):

    pass
class Lendable:

    pass
class Item:

    pass
class library_Periodical(Item):

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

class library_CirculatingItem(Lendable, Item):

    pass
class library_Lendable(ABC):

    def __init__(self, copies: int, borrowed: set["library_Borrower"] = None, Lendable: "library_Borrower" = None):
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
        old_value = getattr(self, f"_library_Lendable__borrowed", None)
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
        old_value = getattr(self, f"_library_Lendable__Lendable", None)
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

class library_Addressable(ABC):

    def __init__(self, address: str):
        self.address = address
        
    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

class Person:

    pass
class library_Item(ABC):

    def __init__(self, publicationDate: date, library_Item: "library_Library" = None):
        self.publicationDate = publicationDate
        self.library_Item = library_Item
        
    @property
    def publicationDate(self) -> date:
        return self.__publicationDate

    @publicationDate.setter
    def publicationDate(self, publicationDate: date):
        self.__publicationDate = publicationDate

    @property
    def library_Item(self):
        return self.__library_Item

    @library_Item.setter
    def library_Item(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Item__library_Item", None)
        self.__library_Item = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Library7"):
                opp_val = getattr(old_value, "library_Library7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library7"):
                opp_val = getattr(value, "library_Library7", None)
                if opp_val is None:
                    setattr(value, "library_Library7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class library_Borrower(Person):

    pass
class library_Employee(Person):

    pass
class Addressable:

    pass
class library_Person(Addressable):

    def __init__(self, firstName: str, lastName: str, library_Person: "library_BookOnTape" = None, library_Person22: "library_VideoCassette" = None):
        self.firstName = firstName
        self.lastName = lastName
        self.library_Person = library_Person
        self.library_Person22 = library_Person22
        
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
    def library_Person22(self):
        return self.__library_Person22

    @library_Person22.setter
    def library_Person22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Person__library_Person22", None)
        self.__library_Person22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_VideoCassette"):
                opp_val = getattr(old_value, "library_VideoCassette", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_VideoCassette"):
                opp_val = getattr(value, "library_VideoCassette", None)
                if opp_val is None:
                    setattr(value, "library_VideoCassette", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def library_Person(self):
        return self.__library_Person

    @library_Person.setter
    def library_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Person__library_Person", None)
        self.__library_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_BookOnTape"):
                opp_val = getattr(old_value, "library_BookOnTape", None)
                if opp_val == self:
                    setattr(old_value, "library_BookOnTape", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_BookOnTape"):
                opp_val = getattr(value, "library_BookOnTape", None)
                setattr(value, "library_BookOnTape", self)

class library_Library(Addressable):

    def __init__(self, name: str, people: str, library_Library: set["library_Writer"] = None, library_Library3: set["library_Employee"] = None, library_Library5: set["library_Borrower"] = None, library_Library7: set["library_Item"] = None, library_Library9: set["library_Book"] = None, Library: "library_Library" = None, parentBranch: set["library_Library"] = None, Library14: "library_Library" = None, branches: "library_Library" = None):
        self.name = name
        self.people = people
        self.library_Library = library_Library if library_Library is not None else set()
        self.library_Library3 = library_Library3 if library_Library3 is not None else set()
        self.library_Library5 = library_Library5 if library_Library5 is not None else set()
        self.library_Library7 = library_Library7 if library_Library7 is not None else set()
        self.library_Library9 = library_Library9 if library_Library9 is not None else set()
        self.Library = Library
        self.parentBranch = parentBranch if parentBranch is not None else set()
        self.Library14 = Library14
        self.branches = branches
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def people(self) -> str:
        return self.__people

    @people.setter
    def people(self, people: str):
        self.__people = people

    @property
    def parentBranch(self):
        return self.__parentBranch

    @parentBranch.setter
    def parentBranch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__parentBranch", None)
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
    def library_Library(self):
        return self.__library_Library

    @library_Library.setter
    def library_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library", None)
        self.__library_Library = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Writer"):
                    opp_val = getattr(item, "library_Writer", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Writer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Writer"):
                    opp_val = getattr(item, "library_Writer", None)
                    
                    setattr(item, "library_Writer", self)
                    

    @property
    def library_Library9(self):
        return self.__library_Library9

    @library_Library9.setter
    def library_Library9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library9", None)
        self.__library_Library9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Book"):
                    opp_val = getattr(item, "library_Book", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Book", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Book"):
                    opp_val = getattr(item, "library_Book", None)
                    
                    setattr(item, "library_Book", self)
                    

    @property
    def library_Library3(self):
        return self.__library_Library3

    @library_Library3.setter
    def library_Library3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library3", None)
        self.__library_Library3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Employee"):
                    opp_val = getattr(item, "library_Employee", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Employee", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Employee"):
                    opp_val = getattr(item, "library_Employee", None)
                    
                    setattr(item, "library_Employee", self)
                    

    @property
    def library_Library7(self):
        return self.__library_Library7

    @library_Library7.setter
    def library_Library7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library7", None)
        self.__library_Library7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Item"):
                    opp_val = getattr(item, "library_Item", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Item", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Item"):
                    opp_val = getattr(item, "library_Item", None)
                    
                    setattr(item, "library_Item", self)
                    

    @property
    def Library(self):
        return self.__Library

    @Library.setter
    def Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__Library", None)
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
    def Library14(self):
        return self.__Library14

    @Library14.setter
    def Library14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__Library14", None)
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
    def library_Library5(self):
        return self.__library_Library5

    @library_Library5.setter
    def library_Library5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library5", None)
        self.__library_Library5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Borrower"):
                    opp_val = getattr(item, "library_Borrower", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Borrower", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Borrower"):
                    opp_val = getattr(item, "library_Borrower", None)
                    
                    setattr(item, "library_Borrower", self)
                    

    @property
    def branches(self):
        return self.__branches

    @branches.setter
    def branches(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__branches", None)
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

class library_Writer(Person):

    def __init__(self, name: str, Writer: "library_Book" = None, library_Writer: "library_Library" = None, author: set["library_Book"] = None, library_Writer20: "library_BookOnTape" = None):
        self.name = name
        self.Writer = Writer
        self.library_Writer = library_Writer
        self.author = author if author is not None else set()
        self.library_Writer20 = library_Writer20
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def library_Writer(self):
        return self.__library_Writer

    @library_Writer.setter
    def library_Writer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Writer__library_Writer", None)
        self.__library_Writer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Library"):
                opp_val = getattr(old_value, "library_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library"):
                opp_val = getattr(value, "library_Library", None)
                if opp_val is None:
                    setattr(value, "library_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Writer(self):
        return self.__Writer

    @Writer.setter
    def Writer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Writer__Writer", None)
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
        old_value = getattr(self, f"_library_Writer__author", None)
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
    def library_Writer20(self):
        return self.__library_Writer20

    @library_Writer20.setter
    def library_Writer20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Writer__library_Writer20", None)
        self.__library_Writer20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_BookOnTape19"):
                opp_val = getattr(old_value, "library_BookOnTape19", None)
                if opp_val == self:
                    setattr(old_value, "library_BookOnTape19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_BookOnTape19"):
                opp_val = getattr(value, "library_BookOnTape19", None)
                setattr(value, "library_BookOnTape19", self)

class CirculatingItem:

    pass
class library_AudioVisualItem(CirculatingItem):

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

class library_Book(CirculatingItem):

    def __init__(self, pages: int, category: str, title: str, books: "library_Writer" = None, library_Book: "library_Library" = None, Book: "library_Writer" = None):
        self.pages = pages
        self.category = category
        self.title = title
        self.books = books
        self.library_Book = library_Book
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
    def books(self):
        return self.__books

    @books.setter
    def books(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__books", None)
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
        old_value = getattr(self, f"_library_Book__Book", None)
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
    def library_Book(self):
        return self.__library_Book

    @library_Book.setter
    def library_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__library_Book", None)
        self.__library_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Library9"):
                opp_val = getattr(old_value, "library_Library9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library9"):
                opp_val = getattr(value, "library_Library9", None)
                if opp_val is None:
                    setattr(value, "library_Library9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
