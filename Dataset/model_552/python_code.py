from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class family_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class NamedElement:

    pass
class family_Person(NamedElement):

    def __init__(self, surname: str, age: int, gender: str, family_Person: "family_Members" = None):
        self.surname = surname
        self.age = age
        self.gender = gender
        self.family_Person = family_Person
        
    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age

    @property
    def surname(self) -> str:
        return self.__surname

    @surname.setter
    def surname(self, surname: str):
        self.__surname = surname

    @property
    def gender(self) -> str:
        return self.__gender

    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

    @property
    def family_Person(self):
        return self.__family_Person

    @family_Person.setter
    def family_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Person__family_Person", None)
        self.__family_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_Members"):
                opp_val = getattr(old_value, "family_Members", None)
                if opp_val == self:
                    setattr(old_value, "family_Members", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_Members"):
                opp_val = getattr(value, "family_Members", None)
                setattr(value, "family_Members", self)

class family_Family(NamedElement):

    def __init__(self, numberOfComponents: int, familyIncome: float, family_Family: set["family_Members"] = None):
        self.numberOfComponents = numberOfComponents
        self.familyIncome = familyIncome
        self.family_Family = family_Family if family_Family is not None else set()
        
    @property
    def familyIncome(self) -> float:
        return self.__familyIncome

    @familyIncome.setter
    def familyIncome(self, familyIncome: float):
        self.__familyIncome = familyIncome

    @property
    def numberOfComponents(self) -> int:
        return self.__numberOfComponents

    @numberOfComponents.setter
    def numberOfComponents(self, numberOfComponents: int):
        self.__numberOfComponents = numberOfComponents

    @property
    def family_Family(self):
        return self.__family_Family

    @family_Family.setter
    def family_Family(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Family__family_Family", None)
        self.__family_Family = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "family_Members2"):
                    opp_val = getattr(item, "family_Members2", None)
                    
                    if opp_val == self:
                        setattr(item, "family_Members2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "family_Members2"):
                    opp_val = getattr(item, "family_Members2", None)
                    
                    setattr(item, "family_Members2", self)
                    

class family_Members(NamedElement):

    def __init__(self, hasChild: bool, family_Members: "family_Person" = None, family_Members2: "family_Family" = None):
        self.hasChild = hasChild
        self.family_Members = family_Members
        self.family_Members2 = family_Members2
        
    @property
    def hasChild(self) -> bool:
        return self.__hasChild

    @hasChild.setter
    def hasChild(self, hasChild: bool):
        self.__hasChild = hasChild

    @property
    def family_Members2(self):
        return self.__family_Members2

    @family_Members2.setter
    def family_Members2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Members__family_Members2", None)
        self.__family_Members2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_Family"):
                opp_val = getattr(old_value, "family_Family", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_Family"):
                opp_val = getattr(value, "family_Family", None)
                if opp_val is None:
                    setattr(value, "family_Family", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def family_Members(self):
        return self.__family_Members

    @family_Members.setter
    def family_Members(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Members__family_Members", None)
        self.__family_Members = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_Person"):
                opp_val = getattr(old_value, "family_Person", None)
                if opp_val == self:
                    setattr(old_value, "family_Person", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_Person"):
                opp_val = getattr(value, "family_Person", None)
                setattr(value, "family_Person", self)
