from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Category(Enum):
    SF = "SF"
    Polar = "Polar"
    Enfant = "Enfant"


############################################
# Definition of Classes
############################################

class Sample_EString:

    pass
class Sample_Person:

    def __init__(self, firstName: str, lastName: str, Sample_Person: "Sample_Book" = None):
        self.firstName = firstName
        self.lastName = lastName
        self.Sample_Person = Sample_Person
        
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
    def Sample_Person(self):
        return self.__Sample_Person

    @Sample_Person.setter
    def Sample_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Sample_Person__Sample_Person", None)
        self.__Sample_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Sample_Book2"):
                opp_val = getattr(old_value, "Sample_Book2", None)
                if opp_val == self:
                    setattr(old_value, "Sample_Book2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Sample_Book2"):
                opp_val = getattr(value, "Sample_Book2", None)
                setattr(value, "Sample_Book2", self)

class Sample_Book:

    def __init__(self, name: str, category: str, Sample_Book: "Sample_Library" = None, Sample_Book2: "Sample_Person" = None, Sample_Book4: "Sample_EString" = None):
        self.name = name
        self.category = category
        self.Sample_Book = Sample_Book
        self.Sample_Book2 = Sample_Book2
        self.Sample_Book4 = Sample_Book4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def category(self) -> str:
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category

    @property
    def Sample_Book2(self):
        return self.__Sample_Book2

    @Sample_Book2.setter
    def Sample_Book2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Sample_Book__Sample_Book2", None)
        self.__Sample_Book2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Sample_Person"):
                opp_val = getattr(old_value, "Sample_Person", None)
                if opp_val == self:
                    setattr(old_value, "Sample_Person", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Sample_Person"):
                opp_val = getattr(value, "Sample_Person", None)
                setattr(value, "Sample_Person", self)

    @property
    def Sample_Book(self):
        return self.__Sample_Book

    @Sample_Book.setter
    def Sample_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Sample_Book__Sample_Book", None)
        self.__Sample_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Sample_Library"):
                opp_val = getattr(old_value, "Sample_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Sample_Library"):
                opp_val = getattr(value, "Sample_Library", None)
                if opp_val is None:
                    setattr(value, "Sample_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Sample_Book4(self):
        return self.__Sample_Book4

    @Sample_Book4.setter
    def Sample_Book4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Sample_Book__Sample_Book4", None)
        self.__Sample_Book4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Sample_EString"):
                opp_val = getattr(old_value, "Sample_EString", None)
                if opp_val == self:
                    setattr(old_value, "Sample_EString", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Sample_EString"):
                opp_val = getattr(value, "Sample_EString", None)
                setattr(value, "Sample_EString", self)

class Sample_Library:

    def __init__(self, name: str, Sample_Library: set["Sample_Book"] = None):
        self.name = name
        self.Sample_Library = Sample_Library if Sample_Library is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Sample_Library(self):
        return self.__Sample_Library

    @Sample_Library.setter
    def Sample_Library(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Sample_Library__Sample_Library", None)
        self.__Sample_Library = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Sample_Book"):
                    opp_val = getattr(item, "Sample_Book", None)
                    
                    if opp_val == self:
                        setattr(item, "Sample_Book", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Sample_Book"):
                    opp_val = getattr(item, "Sample_Book", None)
                    
                    setattr(item, "Sample_Book", self)
                    
