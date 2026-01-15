from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Person:

    pass
class familyleft2_Father(Person):

    def __init__(self, address: str, father: "familyleft2_Family" = None, Father: "familyleft2_Family" = None):
        self.address = address
        self.father = father
        self.Father = Father
        
    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def Father(self):
        return self.__Father

    @Father.setter
    def Father(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familyleft2_Father__Father", None)
        self.__Father = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family"):
                opp_val = getattr(old_value, "family", None)
                if opp_val == self:
                    setattr(old_value, "family", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family"):
                opp_val = getattr(value, "family", None)
                setattr(value, "family", self)

    @property
    def father(self):
        return self.__father

    @father.setter
    def father(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familyleft2_Father__father", None)
        self.__father = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Family"):
                opp_val = getattr(old_value, "Family", None)
                if opp_val == self:
                    setattr(old_value, "Family", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Family"):
                opp_val = getattr(value, "Family", None)
                setattr(value, "Family", self)

class familyleft2_Person(ABC):

    def __init__(self, name: str, age: int, isMale: bool):
        self.name = name
        self.age = age
        self.isMale = isMale
        
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
    def isMale(self) -> bool:
        return self.__isMale

    @isMale.setter
    def isMale(self, isMale: bool):
        self.__isMale = isMale

class familyleft2_Daughter(Person):

    pass
class familyleft2_Son(Person):

    pass
class familyleft2_Mother(Person):

    def __init__(self, address: str, mother: "familyleft2_Family" = None, Mother: "familyleft2_Family" = None):
        self.address = address
        self.mother = mother
        self.Mother = Mother
        
    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def mother(self):
        return self.__mother

    @mother.setter
    def mother(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familyleft2_Mother__mother", None)
        self.__mother = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Family2"):
                opp_val = getattr(old_value, "Family2", None)
                if opp_val == self:
                    setattr(old_value, "Family2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Family2"):
                opp_val = getattr(value, "Family2", None)
                setattr(value, "Family2", self)

    @property
    def Mother(self):
        return self.__Mother

    @Mother.setter
    def Mother(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_familyleft2_Mother__Mother", None)
        self.__Mother = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family9"):
                opp_val = getattr(old_value, "family9", None)
                if opp_val == self:
                    setattr(old_value, "family9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family9"):
                opp_val = getattr(value, "family9", None)
                setattr(value, "family9", self)

class familyleft2_Family:

    pass