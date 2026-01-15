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
class extlibrary_VideoCassette(AudioVisualItem):

    pass
class extlibrary_BookOnTape(AudioVisualItem):

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

class Person:

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

    def __init__(self, copies: int, 23: set["extlibrary_Borrower"] = None, 33: "extlibrary_Borrower" = None):
        self.copies = copies
        self.23 = 23 if 23 is not None else set()
        self.33 = 33
        
    @property
    def copies(self) -> int:
        return self.__copies

    @copies.setter
    def copies(self, copies: int):
        self.__copies = copies

    @property
    def 23(self):
        return self.__23

    @23.setter
    def 23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_Lendable__23", None)
        self.__23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "24"):
                    opp_val = getattr(item, "24", None)
                    
                    if opp_val == self:
                        setattr(item, "24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "24"):
                    opp_val = getattr(item, "24", None)
                    
                    setattr(item, "24", self)
                    

    @property
    def 33(self):
        return self.__33

    @33.setter
    def 33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_Lendable__33", None)
        self.__33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "32"):
                opp_val = getattr(old_value, "32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "32"):
                opp_val = getattr(value, "32", None)
                if opp_val is None:
                    setattr(value, "32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Addressable:

    pass
class extlibrary_Person(Addressable):

    def __init__(self, lastName: str, firstName: str, extlibrary_Person: "extlibrary_BookOnTape" = None, extlibrary_Person30: "extlibrary_VideoCassette" = None):
        self.lastName = lastName
        self.firstName = firstName
        self.extlibrary_Person = extlibrary_Person
        self.extlibrary_Person30 = extlibrary_Person30
        
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
    def extlibrary_Person30(self):
        return self.__extlibrary_Person30

    @extlibrary_Person30.setter
    def extlibrary_Person30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_Person__extlibrary_Person30", None)
        self.__extlibrary_Person30 = value
        
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

    def __init__(self, name: str, people: str, extlibrary_Library: set["extlibrary_Writer"] = None, extlibrary_Library4: set["extlibrary_Employee"] = None, extlibrary_Library6: set["extlibrary_Borrower"] = None, extlibrary_Library8: set["extlibrary_Item"] = None, extlibrary_Library10: set["extlibrary_Book"] = None, 14: "extlibrary_Library" = None, 13: set["extlibrary_Library"] = None, 18: "extlibrary_Library" = None, 17: "extlibrary_Library" = None):
        self.name = name
        self.people = people
        self.extlibrary_Library = extlibrary_Library if extlibrary_Library is not None else set()
        self.extlibrary_Library4 = extlibrary_Library4 if extlibrary_Library4 is not None else set()
        self.extlibrary_Library6 = extlibrary_Library6 if extlibrary_Library6 is not None else set()
        self.extlibrary_Library8 = extlibrary_Library8 if extlibrary_Library8 is not None else set()
        self.extlibrary_Library10 = extlibrary_Library10 if extlibrary_Library10 is not None else set()
        self.14 = 14
        self.13 = 13 if 13 is not None else set()
        self.18 = 18
        self.17 = 17
        
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
    def 17(self):
        return self.__17

    @17.setter
    def 17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_Library__17", None)
        self.__17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "18"):
                opp_val = getattr(old_value, "18", None)
                if opp_val == self:
                    setattr(old_value, "18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "18"):
                opp_val = getattr(value, "18", None)
                setattr(value, "18", self)

    @property
    def extlibrary_Library6(self):
        return self.__extlibrary_Library6

    @extlibrary_Library6.setter
    def extlibrary_Library6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_Library__extlibrary_Library6", None)
        self.__extlibrary_Library6 = value if value is not None else set()
        
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
    def extlibrary_Library10(self):
        return self.__extlibrary_Library10

    @extlibrary_Library10.setter
    def extlibrary_Library10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_Library__extlibrary_Library10", None)
        self.__extlibrary_Library10 = value if value is not None else set()
        
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
    def 13(self):
        return self.__13

    @13.setter
    def 13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_Library__13", None)
        self.__13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "14"):
                    opp_val = getattr(item, "14", None)
                    
                    if opp_val == self:
                        setattr(item, "14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "14"):
                    opp_val = getattr(item, "14", None)
                    
                    setattr(item, "14", self)
                    

    @property
    def extlibrary_Library8(self):
        return self.__extlibrary_Library8

    @extlibrary_Library8.setter
    def extlibrary_Library8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_Library__extlibrary_Library8", None)
        self.__extlibrary_Library8 = value if value is not None else set()
        
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
    def extlibrary_Library4(self):
        return self.__extlibrary_Library4

    @extlibrary_Library4.setter
    def extlibrary_Library4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_Library__extlibrary_Library4", None)
        self.__extlibrary_Library4 = value if value is not None else set()
        
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
    def 18(self):
        return self.__18

    @18.setter
    def 18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_Library__18", None)
        self.__18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "17"):
                opp_val = getattr(old_value, "17", None)
                if opp_val == self:
                    setattr(old_value, "17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "17"):
                opp_val = getattr(value, "17", None)
                setattr(value, "17", self)

    @property
    def 14(self):
        return self.__14

    @14.setter
    def 14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_Library__14", None)
        self.__14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "13"):
                opp_val = getattr(old_value, "13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "13"):
                opp_val = getattr(value, "13", None)
                if opp_val is None:
                    setattr(value, "13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class extlibrary_Writer(Person):

    def __init__(self, name: str, extlibrary_Writer: "extlibrary_Library" = None, 1: "extlibrary_Book" = None, 20: set["extlibrary_Book"] = None, extlibrary_Writer28: "extlibrary_BookOnTape" = None):
        self.name = name
        self.extlibrary_Writer = extlibrary_Writer
        self.1 = 1
        self.20 = 20 if 20 is not None else set()
        self.extlibrary_Writer28 = extlibrary_Writer28
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def 20(self):
        return self.__20

    @20.setter
    def 20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_Writer__20", None)
        self.__20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "21"):
                    opp_val = getattr(item, "21", None)
                    
                    if opp_val == self:
                        setattr(item, "21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "21"):
                    opp_val = getattr(item, "21", None)
                    
                    setattr(item, "21", self)
                    

    @property
    def extlibrary_Writer28(self):
        return self.__extlibrary_Writer28

    @extlibrary_Writer28.setter
    def extlibrary_Writer28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_Writer__extlibrary_Writer28", None)
        self.__extlibrary_Writer28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extlibrary_BookOnTape27"):
                opp_val = getattr(old_value, "extlibrary_BookOnTape27", None)
                if opp_val == self:
                    setattr(old_value, "extlibrary_BookOnTape27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extlibrary_BookOnTape27"):
                opp_val = getattr(value, "extlibrary_BookOnTape27", None)
                setattr(value, "extlibrary_BookOnTape27", self)

    @property
    def 1(self):
        return self.__1

    @1.setter
    def 1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_Writer__1", None)
        self.__1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, ""):
                opp_val = getattr(old_value, "", None)
                if opp_val == self:
                    setattr(old_value, "", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, ""):
                opp_val = getattr(value, "", None)
                setattr(value, "", self)

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
            if hasattr(old_value, "extlibrary_Library8"):
                opp_val = getattr(old_value, "extlibrary_Library8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extlibrary_Library8"):
                opp_val = getattr(value, "extlibrary_Library8", None)
                if opp_val is None:
                    setattr(value, "extlibrary_Library8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class extlibrary_Borrower(Person):

    pass
class extlibrary_Employee(Person):

    pass
class CirculatingItem:

    pass
class extlibrary_AudioVisualItem(CirculatingItem):

    def __init__(self, title: str, minutesLength: int, damaged: bool):
        self.title = title
        self.minutesLength = minutesLength
        self.damaged = damaged
        
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

    @property
    def minutesLength(self) -> int:
        return self.__minutesLength

    @minutesLength.setter
    def minutesLength(self, minutesLength: int):
        self.__minutesLength = minutesLength

class extlibrary_Book(CirculatingItem):

    def __init__(self, title: str, pages: int, category: str, extlibrary_Book: "extlibrary_Library" = None, : "extlibrary_Writer" = None, 21: "extlibrary_Writer" = None):
        self.title = title
        self.pages = pages
        self.category = category
        self.extlibrary_Book = extlibrary_Book
        self. = 
        self.21 = 21
        
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
    def (self):
        return self.__

    @.setter
    def (self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_Book__", None)
        self.__ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "1"):
                opp_val = getattr(old_value, "1", None)
                if opp_val == self:
                    setattr(old_value, "1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "1"):
                opp_val = getattr(value, "1", None)
                setattr(value, "1", self)

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
            if hasattr(old_value, "extlibrary_Library10"):
                opp_val = getattr(old_value, "extlibrary_Library10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extlibrary_Library10"):
                opp_val = getattr(value, "extlibrary_Library10", None)
                if opp_val is None:
                    setattr(value, "extlibrary_Library10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 21(self):
        return self.__21

    @21.setter
    def 21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_Book__21", None)
        self.__21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "20"):
                opp_val = getattr(old_value, "20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "20"):
                opp_val = getattr(value, "20", None)
                if opp_val is None:
                    setattr(value, "20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
