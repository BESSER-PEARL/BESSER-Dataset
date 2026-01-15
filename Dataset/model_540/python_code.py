from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class DogBreed(Enum):
    poodle = "poodle"
    labrador = "labrador"


############################################
# Definition of Classes
############################################

class families_Band:

    pass
class families_Bike:

    pass
class District:

    pass
class families_Suburb(District):

    pass
class Pet:

    pass
class families_District:

    pass
class families_Dog(Pet):

    def __init__(self, loud: bool, breed: str, families_Dog: "families_Family" = None, Dog: "families_District" = None, dogs: "families_District" = None):
        self.loud = loud
        self.breed = breed
        self.families_Dog = families_Dog
        self.Dog = Dog
        self.dogs = dogs
        
    @property
    def loud(self) -> bool:
        return self.__loud

    @loud.setter
    def loud(self, loud: bool):
        self.__loud = loud

    @property
    def breed(self) -> str:
        return self.__breed

    @breed.setter
    def breed(self, breed: str):
        self.__breed = breed

    @property
    def families_Dog(self):
        return self.__families_Dog

    @families_Dog.setter
    def families_Dog(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Dog__families_Dog", None)
        self.__families_Dog = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "families_Family4"):
                opp_val = getattr(old_value, "families_Family4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "families_Family4"):
                opp_val = getattr(value, "families_Family4", None)
                if opp_val is None:
                    setattr(value, "families_Family4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Dog(self):
        return self.__Dog

    @Dog.setter
    def Dog(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Dog__Dog", None)
        self.__Dog = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "district24"):
                opp_val = getattr(old_value, "district24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "district24"):
                opp_val = getattr(value, "district24", None)
                if opp_val is None:
                    setattr(value, "district24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dogs(self):
        return self.__dogs

    @dogs.setter
    def dogs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Dog__dogs", None)
        self.__dogs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "District21"):
                opp_val = getattr(old_value, "District21", None)
                if opp_val == self:
                    setattr(old_value, "District21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "District21"):
                opp_val = getattr(value, "District21", None)
                setattr(value, "District21", self)

class families_Account:

    pass
class families_NamedElement(ABC):

    def __init__(self, name: str, families_NamedElement: "families_Model" = None, families_NamedElement28: "families_Model" = None):
        self.name = name
        self.families_NamedElement = families_NamedElement
        self.families_NamedElement28 = families_NamedElement28
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def families_NamedElement(self):
        return self.__families_NamedElement

    @families_NamedElement.setter
    def families_NamedElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_NamedElement__families_NamedElement", None)
        self.__families_NamedElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "families_Model"):
                opp_val = getattr(old_value, "families_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "families_Model"):
                opp_val = getattr(value, "families_Model", None)
                if opp_val is None:
                    setattr(value, "families_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def families_NamedElement28(self):
        return self.__families_NamedElement28

    @families_NamedElement28.setter
    def families_NamedElement28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_NamedElement__families_NamedElement28", None)
        self.__families_NamedElement28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "families_Model27"):
                opp_val = getattr(old_value, "families_Model27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "families_Model27"):
                opp_val = getattr(value, "families_Model27", None)
                if opp_val is None:
                    setattr(value, "families_Model27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class NamedElement:

    pass
class families_Person(NamedElement):

    pass
class families_Pet(NamedElement):

    def __init__(self, male: bool, families_Pet: "families_Family" = None):
        self.male = male
        self.families_Pet = families_Pet
        
    @property
    def male(self) -> bool:
        return self.__male

    @male.setter
    def male(self, male: bool):
        self.__male = male

    @property
    def families_Pet(self):
        return self.__families_Pet

    @families_Pet.setter
    def families_Pet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Pet__families_Pet", None)
        self.__families_Pet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "families_Family"):
                opp_val = getattr(old_value, "families_Family", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "families_Family"):
                opp_val = getattr(value, "families_Family", None)
                if opp_val is None:
                    setattr(value, "families_Family", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class families_Model(NamedElement):

    pass
class families_Family(NamedElement):

    def __init__(self, address: str, numberOfChildren: int, id: str, nuclear: bool, averageAge: float, lotteryNumbers: int, averageAgePrecise: float, families_Family: set["families_Pet"] = None, families_Family2: set["families_Person"] = None, families_Family4: set["families_Dog"] = None, families: "families_District" = None, Family: "families_District" = None, families_Family33: "families_Bike" = None):
        self.address = address
        self.numberOfChildren = numberOfChildren
        self.id = id
        self.nuclear = nuclear
        self.averageAge = averageAge
        self.lotteryNumbers = lotteryNumbers
        self.averageAgePrecise = averageAgePrecise
        self.families_Family = families_Family if families_Family is not None else set()
        self.families_Family2 = families_Family2 if families_Family2 is not None else set()
        self.families_Family4 = families_Family4 if families_Family4 is not None else set()
        self.families = families
        self.Family = Family
        self.families_Family33 = families_Family33
        
    @property
    def averageAge(self) -> float:
        return self.__averageAge

    @averageAge.setter
    def averageAge(self, averageAge: float):
        self.__averageAge = averageAge

    @property
    def numberOfChildren(self) -> int:
        return self.__numberOfChildren

    @numberOfChildren.setter
    def numberOfChildren(self, numberOfChildren: int):
        self.__numberOfChildren = numberOfChildren

    @property
    def lotteryNumbers(self) -> int:
        return self.__lotteryNumbers

    @lotteryNumbers.setter
    def lotteryNumbers(self, lotteryNumbers: int):
        self.__lotteryNumbers = lotteryNumbers

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def nuclear(self) -> bool:
        return self.__nuclear

    @nuclear.setter
    def nuclear(self, nuclear: bool):
        self.__nuclear = nuclear

    @property
    def averageAgePrecise(self) -> float:
        return self.__averageAgePrecise

    @averageAgePrecise.setter
    def averageAgePrecise(self, averageAgePrecise: float):
        self.__averageAgePrecise = averageAgePrecise

    @property
    def families_Family(self):
        return self.__families_Family

    @families_Family.setter
    def families_Family(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Family__families_Family", None)
        self.__families_Family = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "families_Pet"):
                    opp_val = getattr(item, "families_Pet", None)
                    
                    if opp_val == self:
                        setattr(item, "families_Pet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "families_Pet"):
                    opp_val = getattr(item, "families_Pet", None)
                    
                    setattr(item, "families_Pet", self)
                    

    @property
    def families(self):
        return self.__families

    @families.setter
    def families(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Family__families", None)
        self.__families = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "District"):
                opp_val = getattr(old_value, "District", None)
                if opp_val == self:
                    setattr(old_value, "District", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "District"):
                opp_val = getattr(value, "District", None)
                setattr(value, "District", self)

    @property
    def families_Family2(self):
        return self.__families_Family2

    @families_Family2.setter
    def families_Family2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Family__families_Family2", None)
        self.__families_Family2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "families_Person"):
                    opp_val = getattr(item, "families_Person", None)
                    
                    if opp_val == self:
                        setattr(item, "families_Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "families_Person"):
                    opp_val = getattr(item, "families_Person", None)
                    
                    setattr(item, "families_Person", self)
                    

    @property
    def families_Family33(self):
        return self.__families_Family33

    @families_Family33.setter
    def families_Family33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Family__families_Family33", None)
        self.__families_Family33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "families_Bike32"):
                opp_val = getattr(old_value, "families_Bike32", None)
                if opp_val == self:
                    setattr(old_value, "families_Bike32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "families_Bike32"):
                opp_val = getattr(value, "families_Bike32", None)
                setattr(value, "families_Bike32", self)

    @property
    def families_Family4(self):
        return self.__families_Family4

    @families_Family4.setter
    def families_Family4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Family__families_Family4", None)
        self.__families_Family4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "families_Dog"):
                    opp_val = getattr(item, "families_Dog", None)
                    
                    if opp_val == self:
                        setattr(item, "families_Dog", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "families_Dog"):
                    opp_val = getattr(item, "families_Dog", None)
                    
                    setattr(item, "families_Dog", self)
                    

    @property
    def Family(self):
        return self.__Family

    @Family.setter
    def Family(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_families_Family__Family", None)
        self.__Family = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "district"):
                opp_val = getattr(old_value, "district", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "district"):
                opp_val = getattr(value, "district", None)
                if opp_val is None:
                    setattr(value, "district", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
