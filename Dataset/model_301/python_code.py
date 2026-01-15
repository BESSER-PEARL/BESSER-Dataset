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

class Library_Addressable(ABC):

    def __init__(self, address: str):
        self.address = address
        
    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

class Lendable:

    pass
class Item:

    pass
class Library_Periodical(Item):

    def __init__(self, issuesPerYear: int, title: str):
        self.issuesPerYear = issuesPerYear
        self.title = title
        
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

class Library_CirculatingItem(Lendable, Item):

    pass
class Library_Lendable(ABC):

    def __init__(self, copies: int, Lendable: "Library_Borrower" = None, borrowed: set["Library_Borrower"] = None):
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
        old_value = getattr(self, f"_Library_Lendable__borrowed", None)
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
        old_value = getattr(self, f"_Library_Lendable__Lendable", None)
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

class AudioVisualItem:

    pass
class Library_VideoCassette(AudioVisualItem):

    pass
class Library_BookOnTape(AudioVisualItem):

    pass
class Addressable:

    pass
class Library_Person(Addressable):

    def __init__(self, firstName: str, lastName: str, Library_Person: "Library_BookOnTape" = None, Library_Person22: "Library_VideoCassette" = None):
        self.firstName = firstName
        self.lastName = lastName
        self.Library_Person = Library_Person
        self.Library_Person22 = Library_Person22
        
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
    def Library_Person(self):
        return self.__Library_Person

    @Library_Person.setter
    def Library_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Person__Library_Person", None)
        self.__Library_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Library_BookOnTape"):
                opp_val = getattr(old_value, "Library_BookOnTape", None)
                if opp_val == self:
                    setattr(old_value, "Library_BookOnTape", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Library_BookOnTape"):
                opp_val = getattr(value, "Library_BookOnTape", None)
                setattr(value, "Library_BookOnTape", self)

    @property
    def Library_Person22(self):
        return self.__Library_Person22

    @Library_Person22.setter
    def Library_Person22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Person__Library_Person22", None)
        self.__Library_Person22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Library_VideoCassette"):
                opp_val = getattr(old_value, "Library_VideoCassette", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Library_VideoCassette"):
                opp_val = getattr(value, "Library_VideoCassette", None)
                if opp_val is None:
                    setattr(value, "Library_VideoCassette", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Library_Library(Addressable):

    def __init__(self, people: str, name: str, Library_Library7: set["Library_Item"] = None, Library_Library9: set["Library_Book"] = None, Library: "Library_Library" = None, parentBranch: set["Library_Library"] = None, Library14: "Library_Library" = None, branches: "Library_Library" = None, Library_Library: set["Library_Writer"] = None, Library_Library3: set["Library_Employee"] = None, Library_Library5: set["Library_Borrower"] = None):
        self.people = people
        self.name = name
        self.Library_Library7 = Library_Library7 if Library_Library7 is not None else set()
        self.Library_Library9 = Library_Library9 if Library_Library9 is not None else set()
        self.Library = Library
        self.parentBranch = parentBranch if parentBranch is not None else set()
        self.Library14 = Library14
        self.branches = branches
        self.Library_Library = Library_Library if Library_Library is not None else set()
        self.Library_Library3 = Library_Library3 if Library_Library3 is not None else set()
        self.Library_Library5 = Library_Library5 if Library_Library5 is not None else set()
        
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
    def Library14(self):
        return self.__Library14

    @Library14.setter
    def Library14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Library__Library14", None)
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
    def Library_Library5(self):
        return self.__Library_Library5

    @Library_Library5.setter
    def Library_Library5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Library__Library_Library5", None)
        self.__Library_Library5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Library_Borrower"):
                    opp_val = getattr(item, "Library_Borrower", None)
                    
                    if opp_val == self:
                        setattr(item, "Library_Borrower", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Library_Borrower"):
                    opp_val = getattr(item, "Library_Borrower", None)
                    
                    setattr(item, "Library_Borrower", self)
                    

    @property
    def parentBranch(self):
        return self.__parentBranch

    @parentBranch.setter
    def parentBranch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Library__parentBranch", None)
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
    def Library(self):
        return self.__Library

    @Library.setter
    def Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Library__Library", None)
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
    def Library_Library7(self):
        return self.__Library_Library7

    @Library_Library7.setter
    def Library_Library7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Library__Library_Library7", None)
        self.__Library_Library7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Library_Item"):
                    opp_val = getattr(item, "Library_Item", None)
                    
                    if opp_val == self:
                        setattr(item, "Library_Item", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Library_Item"):
                    opp_val = getattr(item, "Library_Item", None)
                    
                    setattr(item, "Library_Item", self)
                    

    @property
    def branches(self):
        return self.__branches

    @branches.setter
    def branches(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Library__branches", None)
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

    @property
    def Library_Library9(self):
        return self.__Library_Library9

    @Library_Library9.setter
    def Library_Library9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Library__Library_Library9", None)
        self.__Library_Library9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Library_Book"):
                    opp_val = getattr(item, "Library_Book", None)
                    
                    if opp_val == self:
                        setattr(item, "Library_Book", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Library_Book"):
                    opp_val = getattr(item, "Library_Book", None)
                    
                    setattr(item, "Library_Book", self)
                    

    @property
    def Library_Library(self):
        return self.__Library_Library

    @Library_Library.setter
    def Library_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Library__Library_Library", None)
        self.__Library_Library = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Library_Writer"):
                    opp_val = getattr(item, "Library_Writer", None)
                    
                    if opp_val == self:
                        setattr(item, "Library_Writer", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Library_Writer"):
                    opp_val = getattr(item, "Library_Writer", None)
                    
                    setattr(item, "Library_Writer", self)
                    

    @property
    def Library_Library3(self):
        return self.__Library_Library3

    @Library_Library3.setter
    def Library_Library3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Library__Library_Library3", None)
        self.__Library_Library3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Library_Employee"):
                    opp_val = getattr(item, "Library_Employee", None)
                    
                    if opp_val == self:
                        setattr(item, "Library_Employee", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Library_Employee"):
                    opp_val = getattr(item, "Library_Employee", None)
                    
                    setattr(item, "Library_Employee", self)
                    

class Person:

    pass
class Library_Employee(Person):

    pass
class Library_Borrower(Person):

    pass
class Library_Writer(Person):

    def __init__(self, name: str, author: set["Library_Book"] = None, Writer: "Library_Book" = None, Library_Writer: "Library_Library" = None, Library_Writer20: "Library_BookOnTape" = None):
        self.name = name
        self.author = author if author is not None else set()
        self.Writer = Writer
        self.Library_Writer = Library_Writer
        self.Library_Writer20 = Library_Writer20
        
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
        old_value = getattr(self, f"_Library_Writer__Writer", None)
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
    def Library_Writer20(self):
        return self.__Library_Writer20

    @Library_Writer20.setter
    def Library_Writer20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Writer__Library_Writer20", None)
        self.__Library_Writer20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Library_BookOnTape19"):
                opp_val = getattr(old_value, "Library_BookOnTape19", None)
                if opp_val == self:
                    setattr(old_value, "Library_BookOnTape19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Library_BookOnTape19"):
                opp_val = getattr(value, "Library_BookOnTape19", None)
                setattr(value, "Library_BookOnTape19", self)

    @property
    def Library_Writer(self):
        return self.__Library_Writer

    @Library_Writer.setter
    def Library_Writer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Writer__Library_Writer", None)
        self.__Library_Writer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Library_Library"):
                opp_val = getattr(old_value, "Library_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Library_Library"):
                opp_val = getattr(value, "Library_Library", None)
                if opp_val is None:
                    setattr(value, "Library_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Writer__author", None)
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
                    

class Library_Item(ABC):

    def __init__(self, publicationDate: date, Library_Item: "Library_Library" = None):
        self.publicationDate = publicationDate
        self.Library_Item = Library_Item
        
    @property
    def publicationDate(self) -> date:
        return self.__publicationDate

    @publicationDate.setter
    def publicationDate(self, publicationDate: date):
        self.__publicationDate = publicationDate

    @property
    def Library_Item(self):
        return self.__Library_Item

    @Library_Item.setter
    def Library_Item(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Item__Library_Item", None)
        self.__Library_Item = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Library_Library7"):
                opp_val = getattr(old_value, "Library_Library7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Library_Library7"):
                opp_val = getattr(value, "Library_Library7", None)
                if opp_val is None:
                    setattr(value, "Library_Library7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class CirculatingItem:

    pass
class Library_AudioVisualItem(CirculatingItem):

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

class Library_Book(CirculatingItem):

    def __init__(self, title: str, pages: int, category: str, Library_Book: "Library_Library" = None, Book: "Library_Writer" = None, books: "Library_Writer" = None):
        self.title = title
        self.pages = pages
        self.category = category
        self.Library_Book = Library_Book
        self.Book = Book
        self.books = books
        
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
    def pages(self) -> int:
        return self.__pages

    @pages.setter
    def pages(self, pages: int):
        self.__pages = pages

    @property
    def Library_Book(self):
        return self.__Library_Book

    @Library_Book.setter
    def Library_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Book__Library_Book", None)
        self.__Library_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Library_Library9"):
                opp_val = getattr(old_value, "Library_Library9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Library_Library9"):
                opp_val = getattr(value, "Library_Library9", None)
                if opp_val is None:
                    setattr(value, "Library_Library9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Book(self):
        return self.__Book

    @Book.setter
    def Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Book__Book", None)
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
        old_value = getattr(self, f"_Library_Book__books", None)
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
