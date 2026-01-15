from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class family_FamilyTree:

    pass
class Person:

    pass
class family_Female(Person):

    pass
class family_Male(Person):

    pass
class family_Person(ABC):

    def __init__(self, name: str, age: int, size: int, weight: int, family_Person: "family_Male" = None, family_Person2: "family_Female" = None, family_Person5: "family_Person" = None, family_Person3: set["family_Person"] = None, family_Person8: "family_Person" = None, family_Person6: "family_Person" = None, family_Person10: "family_FamilyTree" = None):
        self.name = name
        self.age = age
        self.size = size
        self.weight = weight
        self.family_Person = family_Person
        self.family_Person2 = family_Person2
        self.family_Person5 = family_Person5
        self.family_Person3 = family_Person3 if family_Person3 is not None else set()
        self.family_Person8 = family_Person8
        self.family_Person6 = family_Person6
        self.family_Person10 = family_Person10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age

    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

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
            if hasattr(old_value, "family_Male"):
                opp_val = getattr(old_value, "family_Male", None)
                if opp_val == self:
                    setattr(old_value, "family_Male", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_Male"):
                opp_val = getattr(value, "family_Male", None)
                setattr(value, "family_Male", self)

    @property
    def family_Person10(self):
        return self.__family_Person10

    @family_Person10.setter
    def family_Person10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Person__family_Person10", None)
        self.__family_Person10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_FamilyTree"):
                opp_val = getattr(old_value, "family_FamilyTree", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_FamilyTree"):
                opp_val = getattr(value, "family_FamilyTree", None)
                if opp_val is None:
                    setattr(value, "family_FamilyTree", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def family_Person3(self):
        return self.__family_Person3

    @family_Person3.setter
    def family_Person3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Person__family_Person3", None)
        self.__family_Person3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "family_Person5"):
                    opp_val = getattr(item, "family_Person5", None)
                    
                    if opp_val == self:
                        setattr(item, "family_Person5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "family_Person5"):
                    opp_val = getattr(item, "family_Person5", None)
                    
                    setattr(item, "family_Person5", self)
                    

    @property
    def family_Person2(self):
        return self.__family_Person2

    @family_Person2.setter
    def family_Person2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Person__family_Person2", None)
        self.__family_Person2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_Female"):
                opp_val = getattr(old_value, "family_Female", None)
                if opp_val == self:
                    setattr(old_value, "family_Female", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_Female"):
                opp_val = getattr(value, "family_Female", None)
                setattr(value, "family_Female", self)

    @property
    def family_Person8(self):
        return self.__family_Person8

    @family_Person8.setter
    def family_Person8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Person__family_Person8", None)
        self.__family_Person8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_Person6"):
                opp_val = getattr(old_value, "family_Person6", None)
                if opp_val == self:
                    setattr(old_value, "family_Person6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_Person6"):
                opp_val = getattr(value, "family_Person6", None)
                setattr(value, "family_Person6", self)

    @property
    def family_Person6(self):
        return self.__family_Person6

    @family_Person6.setter
    def family_Person6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Person__family_Person6", None)
        self.__family_Person6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_Person8"):
                opp_val = getattr(old_value, "family_Person8", None)
                if opp_val == self:
                    setattr(old_value, "family_Person8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_Person8"):
                opp_val = getattr(value, "family_Person8", None)
                setattr(value, "family_Person8", self)

    @property
    def family_Person5(self):
        return self.__family_Person5

    @family_Person5.setter
    def family_Person5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Person__family_Person5", None)
        self.__family_Person5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_Person3"):
                opp_val = getattr(old_value, "family_Person3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_Person3"):
                opp_val = getattr(value, "family_Person3", None)
                if opp_val is None:
                    setattr(value, "family_Person3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
