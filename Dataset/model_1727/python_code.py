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

class extlibraryprofile_Dependency:

    pass
class extlibraryprofile_Borrows:

    pass
class AudioVisualItem:

    pass
class extlibraryprofile_VideoCassete(AudioVisualItem):

    pass
class extlibraryprofile_Class:

    pass
class extlibraryprofile_BookOnTape(AudioVisualItem):

    pass
class Person:

    pass
class extlibraryprofile_Employee(Person):

    pass
class extlibraryprofile_Borrower(Person):

    pass
class extlibraryprofile_Writer(Person):

    def __init__(self, name: str, extlibraryprofile_Writer: "extlibraryprofile_BookOnTape" = None):
        self.name = name
        self.extlibraryprofile_Writer = extlibraryprofile_Writer
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def extlibraryprofile_Writer(self):
        return self.__extlibraryprofile_Writer

    @extlibraryprofile_Writer.setter
    def extlibraryprofile_Writer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibraryprofile_Writer__extlibraryprofile_Writer", None)
        self.__extlibraryprofile_Writer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extlibraryprofile_BookOnTape"):
                opp_val = getattr(old_value, "extlibraryprofile_BookOnTape", None)
                if opp_val == self:
                    setattr(old_value, "extlibraryprofile_BookOnTape", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extlibraryprofile_BookOnTape"):
                opp_val = getattr(value, "extlibraryprofile_BookOnTape", None)
                setattr(value, "extlibraryprofile_BookOnTape", self)

class extlibraryprofile_Addressable(ABC):

    def __init__(self, address: str):
        self.address = address
        
    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

class extlibraryprofile_Package:

    pass
class Addressable:

    pass
class extlibraryprofile_Person(Addressable):

    def __init__(self, firstName: str, lastName: str, extlibraryprofile_Person: set["extlibraryprofile_VideoCassete"] = None, extlibraryprofile_Person5: "extlibraryprofile_BookOnTape" = None, extlibraryprofile_Person8: "extlibraryprofile_Class" = None):
        self.firstName = firstName
        self.lastName = lastName
        self.extlibraryprofile_Person = extlibraryprofile_Person if extlibraryprofile_Person is not None else set()
        self.extlibraryprofile_Person5 = extlibraryprofile_Person5
        self.extlibraryprofile_Person8 = extlibraryprofile_Person8
        
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
    def extlibraryprofile_Person8(self):
        return self.__extlibraryprofile_Person8

    @extlibraryprofile_Person8.setter
    def extlibraryprofile_Person8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibraryprofile_Person__extlibraryprofile_Person8", None)
        self.__extlibraryprofile_Person8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extlibraryprofile_Class9"):
                opp_val = getattr(old_value, "extlibraryprofile_Class9", None)
                if opp_val == self:
                    setattr(old_value, "extlibraryprofile_Class9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extlibraryprofile_Class9"):
                opp_val = getattr(value, "extlibraryprofile_Class9", None)
                setattr(value, "extlibraryprofile_Class9", self)

    @property
    def extlibraryprofile_Person(self):
        return self.__extlibraryprofile_Person

    @extlibraryprofile_Person.setter
    def extlibraryprofile_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibraryprofile_Person__extlibraryprofile_Person", None)
        self.__extlibraryprofile_Person = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "extlibraryprofile_VideoCassete"):
                    opp_val = getattr(item, "extlibraryprofile_VideoCassete", None)
                    
                    if opp_val == self:
                        setattr(item, "extlibraryprofile_VideoCassete", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "extlibraryprofile_VideoCassete"):
                    opp_val = getattr(item, "extlibraryprofile_VideoCassete", None)
                    
                    setattr(item, "extlibraryprofile_VideoCassete", self)
                    

    @property
    def extlibraryprofile_Person5(self):
        return self.__extlibraryprofile_Person5

    @extlibraryprofile_Person5.setter
    def extlibraryprofile_Person5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibraryprofile_Person__extlibraryprofile_Person5", None)
        self.__extlibraryprofile_Person5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extlibraryprofile_BookOnTape6"):
                opp_val = getattr(old_value, "extlibraryprofile_BookOnTape6", None)
                if opp_val == self:
                    setattr(old_value, "extlibraryprofile_BookOnTape6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extlibraryprofile_BookOnTape6"):
                opp_val = getattr(value, "extlibraryprofile_BookOnTape6", None)
                setattr(value, "extlibraryprofile_BookOnTape6", self)

class extlibraryprofile_Library(Addressable):

    def __init__(self, name: str, extlibraryprofile_Library: "extlibraryprofile_Package" = None):
        self.name = name
        self.extlibraryprofile_Library = extlibraryprofile_Library
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def extlibraryprofile_Library(self):
        return self.__extlibraryprofile_Library

    @extlibraryprofile_Library.setter
    def extlibraryprofile_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibraryprofile_Library__extlibraryprofile_Library", None)
        self.__extlibraryprofile_Library = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extlibraryprofile_Package"):
                opp_val = getattr(old_value, "extlibraryprofile_Package", None)
                if opp_val == self:
                    setattr(old_value, "extlibraryprofile_Package", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extlibraryprofile_Package"):
                opp_val = getattr(value, "extlibraryprofile_Package", None)
                setattr(value, "extlibraryprofile_Package", self)

class extlibraryprofile_Lendable(ABC):

    def __init__(self, copies: str):
        self.copies = copies
        
    @property
    def copies(self) -> str:
        return self.__copies

    @copies.setter
    def copies(self, copies: str):
        self.__copies = copies

class extlibraryprofile_Item(ABC):

    def __init__(self, title: str, publicationDate: str, extlibraryprofile_Item: "extlibraryprofile_Class" = None):
        self.title = title
        self.publicationDate = publicationDate
        self.extlibraryprofile_Item = extlibraryprofile_Item
        
    @property
    def publicationDate(self) -> str:
        return self.__publicationDate

    @publicationDate.setter
    def publicationDate(self, publicationDate: str):
        self.__publicationDate = publicationDate

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def extlibraryprofile_Item(self):
        return self.__extlibraryprofile_Item

    @extlibraryprofile_Item.setter
    def extlibraryprofile_Item(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibraryprofile_Item__extlibraryprofile_Item", None)
        self.__extlibraryprofile_Item = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extlibraryprofile_Class"):
                opp_val = getattr(old_value, "extlibraryprofile_Class", None)
                if opp_val == self:
                    setattr(old_value, "extlibraryprofile_Class", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extlibraryprofile_Class"):
                opp_val = getattr(value, "extlibraryprofile_Class", None)
                setattr(value, "extlibraryprofile_Class", self)

class Lendable:

    pass
class Item:

    pass
class extlibraryprofile_Periodical(Item):

    def __init__(self, issuesPerYear: str):
        self.issuesPerYear = issuesPerYear
        
    @property
    def issuesPerYear(self) -> str:
        return self.__issuesPerYear

    @issuesPerYear.setter
    def issuesPerYear(self, issuesPerYear: str):
        self.__issuesPerYear = issuesPerYear

class extlibraryprofile_CirculatingItem(Item, Lendable):

    pass
class CirculatingItem:

    pass
class extlibraryprofile_AudioVisualItem(CirculatingItem):

    def __init__(self, minutesLength: str, damaged: str):
        self.minutesLength = minutesLength
        self.damaged = damaged
        
    @property
    def minutesLength(self) -> str:
        return self.__minutesLength

    @minutesLength.setter
    def minutesLength(self, minutesLength: str):
        self.__minutesLength = minutesLength

    @property
    def damaged(self) -> str:
        return self.__damaged

    @damaged.setter
    def damaged(self, damaged: str):
        self.__damaged = damaged

class extlibraryprofile_Book(CirculatingItem):

    def __init__(self, pages: str, category: str):
        self.pages = pages
        self.category = category
        
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
