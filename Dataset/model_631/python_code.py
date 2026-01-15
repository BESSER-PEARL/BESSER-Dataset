from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class AbstractPerson:

    pass
class library_Loan:

    pass
class library_AbstractPerson(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    def getFirstName(self) -> str:
        # TODO: Implement getFirstName method
        pass

    def getLastName(self) -> str:
        # TODO: Implement getLastName method
        pass

class library_Book:

    def __init__(self, isbn: str, title: str, library_Book: "library_Author" = None, library_Book9: "library_Library" = None, library_Book17: "library_Loan" = None):
        self.isbn = isbn
        self.title = title
        self.library_Book = library_Book
        self.library_Book9 = library_Book9
        self.library_Book17 = library_Book17
        
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
    def library_Book17(self):
        return self.__library_Book17

    @library_Book17.setter
    def library_Book17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__library_Book17", None)
        self.__library_Book17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Loan16"):
                opp_val = getattr(old_value, "library_Loan16", None)
                if opp_val == self:
                    setattr(old_value, "library_Loan16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Loan16"):
                opp_val = getattr(value, "library_Loan16", None)
                setattr(value, "library_Loan16", self)

    @property
    def library_Book9(self):
        return self.__library_Book9

    @library_Book9.setter
    def library_Book9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Book__library_Book9", None)
        self.__library_Book9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_Library8"):
                opp_val = getattr(old_value, "library_Library8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Library8"):
                opp_val = getattr(value, "library_Library8", None)
                if opp_val is None:
                    setattr(value, "library_Library8", set([self]))
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
            if hasattr(old_value, "library_Author6"):
                opp_val = getattr(old_value, "library_Author6", None)
                if opp_val == self:
                    setattr(old_value, "library_Author6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_Author6"):
                opp_val = getattr(value, "library_Author6", None)
                setattr(value, "library_Author6", self)

class library_Author(AbstractPerson):

    pass
class library_Person(AbstractPerson):

    pass
class library_Library:

    def __init__(self, name: str, library_Library: "library_UoD" = None, library_Library8: set["library_Book"] = None, library_Library11: set["library_Loan"] = None):
        self.name = name
        self.library_Library = library_Library
        self.library_Library8 = library_Library8 if library_Library8 is not None else set()
        self.library_Library11 = library_Library11 if library_Library11 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def library_Library11(self):
        return self.__library_Library11

    @library_Library11.setter
    def library_Library11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library11", None)
        self.__library_Library11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Loan"):
                    opp_val = getattr(item, "library_Loan", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Loan", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Loan"):
                    opp_val = getattr(item, "library_Loan", None)
                    
                    setattr(item, "library_Loan", self)
                    

    @property
    def library_Library8(self):
        return self.__library_Library8

    @library_Library8.setter
    def library_Library8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library8", None)
        self.__library_Library8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "library_Book9"):
                    opp_val = getattr(item, "library_Book9", None)
                    
                    if opp_val == self:
                        setattr(item, "library_Book9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "library_Book9"):
                    opp_val = getattr(item, "library_Book9", None)
                    
                    setattr(item, "library_Book9", self)
                    

    @property
    def library_Library(self):
        return self.__library_Library

    @library_Library.setter
    def library_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_library_Library__library_Library", None)
        self.__library_Library = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "library_UoD"):
                opp_val = getattr(old_value, "library_UoD", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "library_UoD"):
                opp_val = getattr(value, "library_UoD", None)
                if opp_val is None:
                    setattr(value, "library_UoD", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class library_UoD:

    pass