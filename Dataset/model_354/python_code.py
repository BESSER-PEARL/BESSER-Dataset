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
    Manga = "Manga"
    Manhwa = "Manhwa"


############################################
# Definition of Classes
############################################

class extlibrary_Addressable(ABC):

    def __init__(self, address: str):
        self.address = address
        
    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

class extlibrary__15IX8G60EeGkd4g88tZXfA:

    pass
class extlibrary__15N3gm60EeGkd4g88tZXfA:

    pass
class extlibrary_TitledItem:

    def __init__(self, title: str):
        self.title = title
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

class _15N3gm60EeGkd4g88tZXfA:

    pass
class extlibrary_Borrower(_15N3gm60EeGkd4g88tZXfA):

    pass
class extlibrary_Employee(_15N3gm60EeGkd4g88tZXfA):

    pass
class extlibrary_Writer(_15N3gm60EeGkd4g88tZXfA):

    def __init__(self, name: str, extlibrary_Writer: set["extlibrary__146VgG60EeGkd4g88tZXfA"] = None):
        self.name = name
        self.extlibrary_Writer = extlibrary_Writer if extlibrary_Writer is not None else set()
        
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
        self.__extlibrary_Writer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "extlibrary__146VgG60EeGkd4g88tZXfA17"):
                    opp_val = getattr(item, "extlibrary__146VgG60EeGkd4g88tZXfA17", None)
                    
                    if opp_val == self:
                        setattr(item, "extlibrary__146VgG60EeGkd4g88tZXfA17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "extlibrary__146VgG60EeGkd4g88tZXfA17"):
                    opp_val = getattr(item, "extlibrary__146VgG60EeGkd4g88tZXfA17", None)
                    
                    setattr(item, "extlibrary__146VgG60EeGkd4g88tZXfA17", self)
                    

class extlibrary__148KsW60EeGkd4g88tZXfA:

    pass
class extlibrary__146VgG60EeGkd4g88tZXfA:

    pass
class extlibrary_Lendable(ABC):

    def __init__(self, copies: int, extlibrary_Lendable: set["extlibrary__15NQcW60EeGkd4g88tZXfA"] = None):
        self.copies = copies
        self.extlibrary_Lendable = extlibrary_Lendable if extlibrary_Lendable is not None else set()
        
    @property
    def copies(self) -> int:
        return self.__copies

    @copies.setter
    def copies(self, copies: int):
        self.__copies = copies

    @property
    def extlibrary_Lendable(self):
        return self.__extlibrary_Lendable

    @extlibrary_Lendable.setter
    def extlibrary_Lendable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_Lendable__extlibrary_Lendable", None)
        self.__extlibrary_Lendable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "extlibrary__15NQcW60EeGkd4g88tZXfA19"):
                    opp_val = getattr(item, "extlibrary__15NQcW60EeGkd4g88tZXfA19", None)
                    
                    if opp_val == self:
                        setattr(item, "extlibrary__15NQcW60EeGkd4g88tZXfA19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "extlibrary__15NQcW60EeGkd4g88tZXfA19"):
                    opp_val = getattr(item, "extlibrary__15NQcW60EeGkd4g88tZXfA19", None)
                    
                    setattr(item, "extlibrary__15NQcW60EeGkd4g88tZXfA19", self)
                    

class extlibrary_Item(ABC):

    def __init__(self, publicationDate: date):
        self.publicationDate = publicationDate
        
    @property
    def publicationDate(self) -> date:
        return self.__publicationDate

    @publicationDate.setter
    def publicationDate(self, publicationDate: date):
        self.__publicationDate = publicationDate

class extlibrary_CirculatingItem(extlibrary_Item, extlibrary_Lendable):

    def __init__(self, publicationDate: date, copies: int, extlibrary_Lendable: set["extlibrary__15NQcW60EeGkd4g88tZXfA"] = None):
        super().__init__(publicationDate, copies, extlibrary_Lendable)
        
class _15OelG60EeGkd4g88tZXfA:

    pass
class extlibrary_Person(_15OelG60EeGkd4g88tZXfA):

    def __init__(self, firstName: str, familyName: str):
        self.firstName = firstName
        self.familyName = familyName
        
    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def familyName(self) -> str:
        return self.__familyName

    @familyName.setter
    def familyName(self, familyName: str):
        self.__familyName = familyName

class extlibrary_Library(_15OelG60EeGkd4g88tZXfA):

    def __init__(self, name: str, people: str, extlibrary_Library: set["extlibrary__15CRUW60EeGkd4g88tZXfA"] = None, extlibrary_Library4: set["extlibrary__15OekG60EeGkd4g88tZXfA"] = None, extlibrary_Library6: set["extlibrary__15NQcW60EeGkd4g88tZXfA"] = None, extlibrary_Library8: set["extlibrary__15Hw4m60EeGkd4g88tZXfA"] = None, extlibrary_Library10: set["extlibrary__146VgG60EeGkd4g88tZXfA"] = None, extlibrary_Library12: set["extlibrary__148KsW60EeGkd4g88tZXfA"] = None, extlibrary_Library14: "extlibrary__148KsW60EeGkd4g88tZXfA" = None):
        self.name = name
        self.people = people
        self.extlibrary_Library = extlibrary_Library if extlibrary_Library is not None else set()
        self.extlibrary_Library4 = extlibrary_Library4 if extlibrary_Library4 is not None else set()
        self.extlibrary_Library6 = extlibrary_Library6 if extlibrary_Library6 is not None else set()
        self.extlibrary_Library8 = extlibrary_Library8 if extlibrary_Library8 is not None else set()
        self.extlibrary_Library10 = extlibrary_Library10 if extlibrary_Library10 is not None else set()
        self.extlibrary_Library12 = extlibrary_Library12 if extlibrary_Library12 is not None else set()
        self.extlibrary_Library14 = extlibrary_Library14
        
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
                if hasattr(item, "extlibrary__15Hw4m60EeGkd4g88tZXfA"):
                    opp_val = getattr(item, "extlibrary__15Hw4m60EeGkd4g88tZXfA", None)
                    
                    if opp_val == self:
                        setattr(item, "extlibrary__15Hw4m60EeGkd4g88tZXfA", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "extlibrary__15Hw4m60EeGkd4g88tZXfA"):
                    opp_val = getattr(item, "extlibrary__15Hw4m60EeGkd4g88tZXfA", None)
                    
                    setattr(item, "extlibrary__15Hw4m60EeGkd4g88tZXfA", self)
                    

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
                if hasattr(item, "extlibrary__146VgG60EeGkd4g88tZXfA"):
                    opp_val = getattr(item, "extlibrary__146VgG60EeGkd4g88tZXfA", None)
                    
                    if opp_val == self:
                        setattr(item, "extlibrary__146VgG60EeGkd4g88tZXfA", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "extlibrary__146VgG60EeGkd4g88tZXfA"):
                    opp_val = getattr(item, "extlibrary__146VgG60EeGkd4g88tZXfA", None)
                    
                    setattr(item, "extlibrary__146VgG60EeGkd4g88tZXfA", self)
                    

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
                if hasattr(item, "extlibrary__15OekG60EeGkd4g88tZXfA"):
                    opp_val = getattr(item, "extlibrary__15OekG60EeGkd4g88tZXfA", None)
                    
                    if opp_val == self:
                        setattr(item, "extlibrary__15OekG60EeGkd4g88tZXfA", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "extlibrary__15OekG60EeGkd4g88tZXfA"):
                    opp_val = getattr(item, "extlibrary__15OekG60EeGkd4g88tZXfA", None)
                    
                    setattr(item, "extlibrary__15OekG60EeGkd4g88tZXfA", self)
                    

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
                if hasattr(item, "extlibrary__15CRUW60EeGkd4g88tZXfA2"):
                    opp_val = getattr(item, "extlibrary__15CRUW60EeGkd4g88tZXfA2", None)
                    
                    if opp_val == self:
                        setattr(item, "extlibrary__15CRUW60EeGkd4g88tZXfA2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "extlibrary__15CRUW60EeGkd4g88tZXfA2"):
                    opp_val = getattr(item, "extlibrary__15CRUW60EeGkd4g88tZXfA2", None)
                    
                    setattr(item, "extlibrary__15CRUW60EeGkd4g88tZXfA2", self)
                    

    @property
    def extlibrary_Library12(self):
        return self.__extlibrary_Library12

    @extlibrary_Library12.setter
    def extlibrary_Library12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_Library__extlibrary_Library12", None)
        self.__extlibrary_Library12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "extlibrary__148KsW60EeGkd4g88tZXfA"):
                    opp_val = getattr(item, "extlibrary__148KsW60EeGkd4g88tZXfA", None)
                    
                    if opp_val == self:
                        setattr(item, "extlibrary__148KsW60EeGkd4g88tZXfA", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "extlibrary__148KsW60EeGkd4g88tZXfA"):
                    opp_val = getattr(item, "extlibrary__148KsW60EeGkd4g88tZXfA", None)
                    
                    setattr(item, "extlibrary__148KsW60EeGkd4g88tZXfA", self)
                    

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
                if hasattr(item, "extlibrary__15NQcW60EeGkd4g88tZXfA"):
                    opp_val = getattr(item, "extlibrary__15NQcW60EeGkd4g88tZXfA", None)
                    
                    if opp_val == self:
                        setattr(item, "extlibrary__15NQcW60EeGkd4g88tZXfA", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "extlibrary__15NQcW60EeGkd4g88tZXfA"):
                    opp_val = getattr(item, "extlibrary__15NQcW60EeGkd4g88tZXfA", None)
                    
                    setattr(item, "extlibrary__15NQcW60EeGkd4g88tZXfA", self)
                    

    @property
    def extlibrary_Library14(self):
        return self.__extlibrary_Library14

    @extlibrary_Library14.setter
    def extlibrary_Library14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_Library__extlibrary_Library14", None)
        self.__extlibrary_Library14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extlibrary__148KsW60EeGkd4g88tZXfA15"):
                opp_val = getattr(old_value, "extlibrary__148KsW60EeGkd4g88tZXfA15", None)
                if opp_val == self:
                    setattr(old_value, "extlibrary__148KsW60EeGkd4g88tZXfA15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extlibrary__148KsW60EeGkd4g88tZXfA15"):
                opp_val = getattr(value, "extlibrary__148KsW60EeGkd4g88tZXfA15", None)
                setattr(value, "extlibrary__148KsW60EeGkd4g88tZXfA15", self)

class extlibrary__15CRUW60EeGkd4g88tZXfA:

    pass
class _9M9ys29IEeGekPcBm25hwQ:

    pass
class extlibrary_Periodical(extlibrary_Item, _9M9ys29IEeGekPcBm25hwQ):

    def __init__(self, publicationDate: date, issuesPerYear: int):
        super().__init__(publicationDate)
        self.issuesPerYear = issuesPerYear
        
    @property
    def issuesPerYear(self) -> int:
        return self.__issuesPerYear

    @issuesPerYear.setter
    def issuesPerYear(self, issuesPerYear: int):
        self.__issuesPerYear = issuesPerYear

class extlibrary_Magazine(extlibrary_Periodical):

    def __init__(self, publicationDate: date, issuesPerYear: int):
        super().__init__(publicationDate, issuesPerYear)
        
class _15LbQG60EeGkd4g88tZXfA:

    pass
class extlibrary_AudioVisualItem(_9M9ys29IEeGekPcBm25hwQ, _15LbQG60EeGkd4g88tZXfA):

    def __init__(self, minutes: int, damaged: bool):
        self.minutes = minutes
        self.damaged = damaged
        
    @property
    def minutes(self) -> int:
        return self.__minutes

    @minutes.setter
    def minutes(self, minutes: int):
        self.__minutes = minutes

    @property
    def damaged(self) -> bool:
        return self.__damaged

    @damaged.setter
    def damaged(self, damaged: bool):
        self.__damaged = damaged

class extlibrary_VideoCassette(extlibrary_AudioVisualItem):

    def __init__(self, minutes: int, damaged: bool, extlibrary_VideoCassette: set["extlibrary__15N3gm60EeGkd4g88tZXfA"] = None):
        super().__init__(minutes, damaged)
        self.extlibrary_VideoCassette = extlibrary_VideoCassette if extlibrary_VideoCassette is not None else set()
        
    @property
    def extlibrary_VideoCassette(self):
        return self.__extlibrary_VideoCassette

    @extlibrary_VideoCassette.setter
    def extlibrary_VideoCassette(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_VideoCassette__extlibrary_VideoCassette", None)
        self.__extlibrary_VideoCassette = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "extlibrary__15N3gm60EeGkd4g88tZXfA"):
                    opp_val = getattr(item, "extlibrary__15N3gm60EeGkd4g88tZXfA", None)
                    
                    if opp_val == self:
                        setattr(item, "extlibrary__15N3gm60EeGkd4g88tZXfA", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "extlibrary__15N3gm60EeGkd4g88tZXfA"):
                    opp_val = getattr(item, "extlibrary__15N3gm60EeGkd4g88tZXfA", None)
                    
                    setattr(item, "extlibrary__15N3gm60EeGkd4g88tZXfA", self)
                    

class extlibrary_BookOnTape(extlibrary_AudioVisualItem):

    def __init__(self, minutes: int, damaged: bool, extlibrary_BookOnTape: "extlibrary__15CRUW60EeGkd4g88tZXfA" = None):
        super().__init__(minutes, damaged)
        self.extlibrary_BookOnTape = extlibrary_BookOnTape
        
    @property
    def extlibrary_BookOnTape(self):
        return self.__extlibrary_BookOnTape

    @extlibrary_BookOnTape.setter
    def extlibrary_BookOnTape(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_BookOnTape__extlibrary_BookOnTape", None)
        self.__extlibrary_BookOnTape = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extlibrary__15CRUW60EeGkd4g88tZXfA21"):
                opp_val = getattr(old_value, "extlibrary__15CRUW60EeGkd4g88tZXfA21", None)
                if opp_val == self:
                    setattr(old_value, "extlibrary__15CRUW60EeGkd4g88tZXfA21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extlibrary__15CRUW60EeGkd4g88tZXfA21"):
                opp_val = getattr(value, "extlibrary__15CRUW60EeGkd4g88tZXfA21", None)
                setattr(value, "extlibrary__15CRUW60EeGkd4g88tZXfA21", self)

class extlibrary_Book(_9M9ys29IEeGekPcBm25hwQ, _15LbQG60EeGkd4g88tZXfA):

    def __init__(self, pages: int, category: str, subtitle: str, extlibrary_Book: "extlibrary__15CRUW60EeGkd4g88tZXfA" = None):
        self.pages = pages
        self.category = category
        self.subtitle = subtitle
        self.extlibrary_Book = extlibrary_Book
        
    @property
    def subtitle(self) -> str:
        return self.__subtitle

    @subtitle.setter
    def subtitle(self, subtitle: str):
        self.__subtitle = subtitle

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
    def extlibrary_Book(self):
        return self.__extlibrary_Book

    @extlibrary_Book.setter
    def extlibrary_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_extlibrary_Book__extlibrary_Book", None)
        self.__extlibrary_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "extlibrary__15CRUW60EeGkd4g88tZXfA"):
                opp_val = getattr(old_value, "extlibrary__15CRUW60EeGkd4g88tZXfA", None)
                if opp_val == self:
                    setattr(old_value, "extlibrary__15CRUW60EeGkd4g88tZXfA", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "extlibrary__15CRUW60EeGkd4g88tZXfA"):
                opp_val = getattr(value, "extlibrary__15CRUW60EeGkd4g88tZXfA", None)
                setattr(value, "extlibrary__15CRUW60EeGkd4g88tZXfA", self)

class extlibrary__15Hw4m60EeGkd4g88tZXfA:

    pass
class extlibrary__15NQcW60EeGkd4g88tZXfA:

    pass
class extlibrary__15OekG60EeGkd4g88tZXfA:

    pass