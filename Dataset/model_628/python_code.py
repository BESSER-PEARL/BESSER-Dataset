from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Color(Enum):
    Red = "Red"
    Green = "Green"
    Blue = "Blue"
class Gender(Enum):
    Male = "Male"
    Female = "Female"
    Both = "Both"


############################################
# Definition of Classes
############################################

class model_Person:

    def __init__(self, firstName: str, gender: str, lastName: str, custom: str, age: str):
        self.firstName = firstName
        self.gender = gender
        self.lastName = lastName
        self.custom = custom
        self.age = age
        
    @property
    def age(self) -> str:
        return self.__age

    @age.setter
    def age(self, age: str):
        self.__age = age

    @property
    def custom(self) -> str:
        return self.__custom

    @custom.setter
    def custom(self, custom: str):
        self.__custom = custom

    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def gender(self) -> str:
        return self.__gender

    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

class model_Referencer:

    pass
class model_TableWithoutMultiplicityConcrete:

    pass
class model_TableWithUnique:

    pass
class model_TableWithoutMultiplicity:

    pass
class model_CrossReferenceContent:

    pass
class model_CrossReferenceContainer:

    pass
class model_TableContent(ABC):

    pass
class model_TableWithMultiplicity:

    pass
class model_Content:

    def __init__(self, uniqueAttribute: str, secondAttribute: str, model_Content: "model_Container" = None):
        self.uniqueAttribute = uniqueAttribute
        self.secondAttribute = secondAttribute
        self.model_Content = model_Content
        
    @property
    def uniqueAttribute(self) -> str:
        return self.__uniqueAttribute

    @uniqueAttribute.setter
    def uniqueAttribute(self, uniqueAttribute: str):
        self.__uniqueAttribute = uniqueAttribute

    @property
    def secondAttribute(self) -> str:
        return self.__secondAttribute

    @secondAttribute.setter
    def secondAttribute(self, secondAttribute: str):
        self.__secondAttribute = secondAttribute

    @property
    def model_Content(self):
        return self.__model_Content

    @model_Content.setter
    def model_Content(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Content__model_Content", None)
        self.__model_Content = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Container"):
                opp_val = getattr(old_value, "model_Container", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Container"):
                opp_val = getattr(value, "model_Container", None)
                if opp_val is None:
                    setattr(value, "model_Container", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_Container:

    pass
class model_PowerBlock:

    def __init__(self, name: str, model_PowerBlock: "model_Computer" = None):
        self.name = name
        self.model_PowerBlock = model_PowerBlock
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_PowerBlock(self):
        return self.__model_PowerBlock

    @model_PowerBlock.setter
    def model_PowerBlock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_PowerBlock__model_PowerBlock", None)
        self.__model_PowerBlock = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Computer11"):
                opp_val = getattr(old_value, "model_Computer11", None)
                if opp_val == self:
                    setattr(old_value, "model_Computer11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Computer11"):
                opp_val = getattr(value, "model_Computer11", None)
                setattr(value, "model_Computer11", self)

class TableContent:

    pass
class model_TableContentWithInnerChild(TableContent):

    def __init__(self, stuff: str, model_TableContentWithInnerChild: "model_TableContent" = None, model_TableContentWithInnerChild23: "model_TableWithoutMultiplicityConcrete" = None):
        self.stuff = stuff
        self.model_TableContentWithInnerChild = model_TableContentWithInnerChild
        self.model_TableContentWithInnerChild23 = model_TableContentWithInnerChild23
        
    @property
    def stuff(self) -> str:
        return self.__stuff

    @stuff.setter
    def stuff(self, stuff: str):
        self.__stuff = stuff

    @property
    def model_TableContentWithInnerChild(self):
        return self.__model_TableContentWithInnerChild

    @model_TableContentWithInnerChild.setter
    def model_TableContentWithInnerChild(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TableContentWithInnerChild__model_TableContentWithInnerChild", None)
        self.__model_TableContentWithInnerChild = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_TableContent21"):
                opp_val = getattr(old_value, "model_TableContent21", None)
                if opp_val == self:
                    setattr(old_value, "model_TableContent21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_TableContent21"):
                opp_val = getattr(value, "model_TableContent21", None)
                setattr(value, "model_TableContent21", self)

    @property
    def model_TableContentWithInnerChild23(self):
        return self.__model_TableContentWithInnerChild23

    @model_TableContentWithInnerChild23.setter
    def model_TableContentWithInnerChild23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_TableContentWithInnerChild__model_TableContentWithInnerChild23", None)
        self.__model_TableContentWithInnerChild23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_TableWithoutMultiplicityConcrete"):
                opp_val = getattr(old_value, "model_TableWithoutMultiplicityConcrete", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_TableWithoutMultiplicityConcrete"):
                opp_val = getattr(value, "model_TableWithoutMultiplicityConcrete", None)
                if opp_val is None:
                    setattr(value, "model_TableWithoutMultiplicityConcrete", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_TableContentWithValidation(TableContent):

    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class model_TableContentWithInnerChild2(TableContent):

    pass
class model_TableContentWithoutValidation(TableContent):

    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight
        
    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class model_Mainboard:

    def __init__(self, name: str, model_Mainboard: "model_Computer" = None):
        self.name = name
        self.model_Mainboard = model_Mainboard
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_Mainboard(self):
        return self.__model_Mainboard

    @model_Mainboard.setter
    def model_Mainboard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Mainboard__model_Mainboard", None)
        self.__model_Mainboard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Computer"):
                opp_val = getattr(old_value, "model_Computer", None)
                if opp_val == self:
                    setattr(old_value, "model_Computer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Computer"):
                opp_val = getattr(value, "model_Computer", None)
                setattr(value, "model_Computer", self)

class model_Computer:

    def __init__(self, name: str, colors: str, model_Computer: "model_Mainboard" = None, model_Computer11: "model_PowerBlock" = None, model_Computer25: "model_Referencer" = None):
        self.name = name
        self.colors = colors
        self.model_Computer = model_Computer
        self.model_Computer11 = model_Computer11
        self.model_Computer25 = model_Computer25
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def colors(self) -> str:
        return self.__colors

    @colors.setter
    def colors(self, colors: str):
        self.__colors = colors

    @property
    def model_Computer(self):
        return self.__model_Computer

    @model_Computer.setter
    def model_Computer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Computer__model_Computer", None)
        self.__model_Computer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Mainboard"):
                opp_val = getattr(old_value, "model_Mainboard", None)
                if opp_val == self:
                    setattr(old_value, "model_Mainboard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Mainboard"):
                opp_val = getattr(value, "model_Mainboard", None)
                setattr(value, "model_Mainboard", self)

    @property
    def model_Computer11(self):
        return self.__model_Computer11

    @model_Computer11.setter
    def model_Computer11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Computer__model_Computer11", None)
        self.__model_Computer11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_PowerBlock"):
                opp_val = getattr(old_value, "model_PowerBlock", None)
                if opp_val == self:
                    setattr(old_value, "model_PowerBlock", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_PowerBlock"):
                opp_val = getattr(value, "model_PowerBlock", None)
                setattr(value, "model_PowerBlock", self)

    @property
    def model_Computer25(self):
        return self.__model_Computer25

    @model_Computer25.setter
    def model_Computer25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Computer__model_Computer25", None)
        self.__model_Computer25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Referencer"):
                opp_val = getattr(old_value, "model_Referencer", None)
                if opp_val == self:
                    setattr(old_value, "model_Referencer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Referencer"):
                opp_val = getattr(value, "model_Referencer", None)
                setattr(value, "model_Referencer", self)

class model_Librarian:

    def __init__(self, name: str, model_Librarian: "model_Library" = None):
        self.name = name
        self.model_Librarian = model_Librarian
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_Librarian(self):
        return self.__model_Librarian

    @model_Librarian.setter
    def model_Librarian(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Librarian__model_Librarian", None)
        self.__model_Librarian = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Library3"):
                opp_val = getattr(old_value, "model_Library3", None)
                if opp_val == self:
                    setattr(old_value, "model_Library3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Library3"):
                opp_val = getattr(value, "model_Library3", None)
                setattr(value, "model_Library3", self)

    def validate(self, context: str, diagnostic: str) -> bool:
        # TODO: Implement validate method
        pass

class model_Book:

    def __init__(self, title: str, pages: int, Book: "model_Writer" = None, model_Book: "model_Library" = None, books: "model_Writer" = None):
        self.title = title
        self.pages = pages
        self.Book = Book
        self.model_Book = model_Book
        self.books = books
        
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
    def model_Book(self):
        return self.__model_Book

    @model_Book.setter
    def model_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Book__model_Book", None)
        self.__model_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Library"):
                opp_val = getattr(old_value, "model_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Library"):
                opp_val = getattr(value, "model_Library", None)
                if opp_val is None:
                    setattr(value, "model_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def books(self):
        return self.__books

    @books.setter
    def books(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Book__books", None)
        self.__books = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Writer8"):
                opp_val = getattr(old_value, "Writer8", None)
                if opp_val == self:
                    setattr(old_value, "Writer8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Writer8"):
                opp_val = getattr(value, "Writer8", None)
                setattr(value, "Writer8", self)

    @property
    def Book(self):
        return self.__Book

    @Book.setter
    def Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Book__Book", None)
        self.__Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "writers"):
                opp_val = getattr(old_value, "writers", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "writers"):
                opp_val = getattr(value, "writers", None)
                if opp_val is None:
                    setattr(value, "writers", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def validate(self, diagnostic: str, context: str) -> bool:
        # TODO: Implement validate method
        pass

class model_Writer:

    def __init__(self, firstName: str, lastName: str, EMail: str, BirthDate: date, Pseudonym: bool, initials: str, title: str, writers: set["model_Book"] = None, Writer: "model_Library" = None, writers6: "model_Library" = None, Writer8: "model_Book" = None):
        self.firstName = firstName
        self.lastName = lastName
        self.EMail = EMail
        self.BirthDate = BirthDate
        self.Pseudonym = Pseudonym
        self.initials = initials
        self.title = title
        self.writers = writers if writers is not None else set()
        self.Writer = Writer
        self.writers6 = writers6
        self.Writer8 = Writer8
        
    @property
    def initials(self) -> str:
        return self.__initials

    @initials.setter
    def initials(self, initials: str):
        self.__initials = initials

    @property
    def EMail(self) -> str:
        return self.__EMail

    @EMail.setter
    def EMail(self, EMail: str):
        self.__EMail = EMail

    @property
    def BirthDate(self) -> date:
        return self.__BirthDate

    @BirthDate.setter
    def BirthDate(self, BirthDate: date):
        self.__BirthDate = BirthDate

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def Pseudonym(self) -> bool:
        return self.__Pseudonym

    @Pseudonym.setter
    def Pseudonym(self, Pseudonym: bool):
        self.__Pseudonym = Pseudonym

    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def Writer8(self):
        return self.__Writer8

    @Writer8.setter
    def Writer8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Writer__Writer8", None)
        self.__Writer8 = value
        
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
    def Writer(self):
        return self.__Writer

    @Writer.setter
    def Writer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Writer__Writer", None)
        self.__Writer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library"):
                opp_val = getattr(old_value, "library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library"):
                opp_val = getattr(value, "library", None)
                if opp_val is None:
                    setattr(value, "library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def writers6(self):
        return self.__writers6

    @writers6.setter
    def writers6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Writer__writers6", None)
        self.__writers6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Library"):
                opp_val = getattr(old_value, "Library", None)
                if opp_val == self:
                    setattr(old_value, "Library", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Library"):
                opp_val = getattr(value, "Library", None)
                setattr(value, "Library", self)

    @property
    def writers(self):
        return self.__writers

    @writers.setter
    def writers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Writer__writers", None)
        self.__writers = value if value is not None else set()
        
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
                    

    def validate(self, diagnostic: str, context: str) -> bool:
        # TODO: Implement validate method
        pass

class model_Library:

    def __init__(self, name: str, phoneNumber: str, library: set["model_Writer"] = None, model_Library: set["model_Book"] = None, model_Library3: "model_Librarian" = None, Library: "model_Writer" = None):
        self.name = name
        self.phoneNumber = phoneNumber
        self.library = library if library is not None else set()
        self.model_Library = model_Library if model_Library is not None else set()
        self.model_Library3 = model_Library3
        self.Library = Library
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def phoneNumber(self) -> str:
        return self.__phoneNumber

    @phoneNumber.setter
    def phoneNumber(self, phoneNumber: str):
        self.__phoneNumber = phoneNumber

    @property
    def model_Library3(self):
        return self.__model_Library3

    @model_Library3.setter
    def model_Library3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Library__model_Library3", None)
        self.__model_Library3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Librarian"):
                opp_val = getattr(old_value, "model_Librarian", None)
                if opp_val == self:
                    setattr(old_value, "model_Librarian", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Librarian"):
                opp_val = getattr(value, "model_Librarian", None)
                setattr(value, "model_Librarian", self)

    @property
    def library(self):
        return self.__library

    @library.setter
    def library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Library__library", None)
        self.__library = value if value is not None else set()
        
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
    def Library(self):
        return self.__Library

    @Library.setter
    def Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Library__Library", None)
        self.__Library = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "writers6"):
                opp_val = getattr(old_value, "writers6", None)
                if opp_val == self:
                    setattr(old_value, "writers6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "writers6"):
                opp_val = getattr(value, "writers6", None)
                setattr(value, "writers6", self)

    @property
    def model_Library(self):
        return self.__model_Library

    @model_Library.setter
    def model_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Library__model_Library", None)
        self.__model_Library = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Book"):
                    opp_val = getattr(item, "model_Book", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Book", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Book"):
                    opp_val = getattr(item, "model_Book", None)
                    
                    setattr(item, "model_Book", self)
                    

    def validate(self, diagnostic: str, context: str) -> bool:
        # TODO: Implement validate method
        pass
