from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Dog:

    pass
class Example_HuntingDog(Dog):

    pass
class Example_RaceDog(Dog):

    pass
class Pet:

    pass
class Example_Cat(Pet):

    pass
class Example_Dog(Pet):

    pass
class Example_Pet(ABC):

    def __init__(self, name: str, breed: str, Example_Pet: "Example_Family" = None):
        self.name = name
        self.breed = breed
        self.Example_Pet = Example_Pet
        
    @property
    def breed(self) -> str:
        return self.__breed

    @breed.setter
    def breed(self, breed: str):
        self.__breed = breed

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Example_Pet(self):
        return self.__Example_Pet

    @Example_Pet.setter
    def Example_Pet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Example_Pet__Example_Pet", None)
        self.__Example_Pet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Example_Family"):
                opp_val = getattr(old_value, "Example_Family", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Example_Family"):
                opp_val = getattr(value, "Example_Family", None)
                if opp_val is None:
                    setattr(value, "Example_Family", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Member:

    pass
class Example_Daughter(Member):

    pass
class Example_Son(Member):

    pass
class Example_Parent(Member):

    pass
class Example_Member(ABC):

    def __init__(self, firstName: str, lastName: str):
        self.firstName = firstName
        self.lastName = lastName
        
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

class Example_Family:

    def __init__(self, address: str, family: set["Example_Parent"] = None, family2: set["Example_Son"] = None, Family: "Example_Parent" = None, family4: set["Example_Daughter"] = None, Example_Family: set["Example_Pet"] = None, Family8: "Example_Son" = None, Family10: "Example_Daughter" = None):
        self.address = address
        self.family = family if family is not None else set()
        self.family2 = family2 if family2 is not None else set()
        self.Family = Family
        self.family4 = family4 if family4 is not None else set()
        self.Example_Family = Example_Family if Example_Family is not None else set()
        self.Family8 = Family8
        self.Family10 = Family10
        
    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def Example_Family(self):
        return self.__Example_Family

    @Example_Family.setter
    def Example_Family(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Example_Family__Example_Family", None)
        self.__Example_Family = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Example_Pet"):
                    opp_val = getattr(item, "Example_Pet", None)
                    
                    if opp_val == self:
                        setattr(item, "Example_Pet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Example_Pet"):
                    opp_val = getattr(item, "Example_Pet", None)
                    
                    setattr(item, "Example_Pet", self)
                    

    @property
    def family(self):
        return self.__family

    @family.setter
    def family(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Example_Family__family", None)
        self.__family = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Parent"):
                    opp_val = getattr(item, "Parent", None)
                    
                    if opp_val == self:
                        setattr(item, "Parent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Parent"):
                    opp_val = getattr(item, "Parent", None)
                    
                    setattr(item, "Parent", self)
                    

    @property
    def family2(self):
        return self.__family2

    @family2.setter
    def family2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Example_Family__family2", None)
        self.__family2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Son"):
                    opp_val = getattr(item, "Son", None)
                    
                    if opp_val == self:
                        setattr(item, "Son", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Son"):
                    opp_val = getattr(item, "Son", None)
                    
                    setattr(item, "Son", self)
                    

    @property
    def family4(self):
        return self.__family4

    @family4.setter
    def family4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Example_Family__family4", None)
        self.__family4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Daughter"):
                    opp_val = getattr(item, "Daughter", None)
                    
                    if opp_val == self:
                        setattr(item, "Daughter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Daughter"):
                    opp_val = getattr(item, "Daughter", None)
                    
                    setattr(item, "Daughter", self)
                    

    @property
    def Family10(self):
        return self.__Family10

    @Family10.setter
    def Family10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Example_Family__Family10", None)
        self.__Family10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "daughters"):
                opp_val = getattr(old_value, "daughters", None)
                if opp_val == self:
                    setattr(old_value, "daughters", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "daughters"):
                opp_val = getattr(value, "daughters", None)
                setattr(value, "daughters", self)

    @property
    def Family(self):
        return self.__Family

    @Family.setter
    def Family(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Example_Family__Family", None)
        self.__Family = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parents"):
                opp_val = getattr(old_value, "parents", None)
                if opp_val == self:
                    setattr(old_value, "parents", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parents"):
                opp_val = getattr(value, "parents", None)
                setattr(value, "parents", self)

    @property
    def Family8(self):
        return self.__Family8

    @Family8.setter
    def Family8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Example_Family__Family8", None)
        self.__Family8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sons"):
                opp_val = getattr(old_value, "sons", None)
                if opp_val == self:
                    setattr(old_value, "sons", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sons"):
                opp_val = getattr(value, "sons", None)
                setattr(value, "sons", self)
