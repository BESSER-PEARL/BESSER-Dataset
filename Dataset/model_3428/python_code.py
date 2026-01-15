from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class PetKind(Enum):
    FRIENDLY = "FRIENDLY"
    INDEPENDENT = "INDEPENDENT"
    DANGEROUS = "DANGEROUS"


############################################
# Definition of Classes
############################################

class people_Pet:

    def __init__(self, name: str, kind: str, people_Pet: "people_Person" = None):
        self.name = name
        self.kind = kind
        self.people_Pet = people_Pet
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def people_Pet(self):
        return self.__people_Pet

    @people_Pet.setter
    def people_Pet(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_people_Pet__people_Pet", None)
        self.__people_Pet = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "people_Person5"):
                opp_val = getattr(old_value, "people_Person5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "people_Person5"):
                opp_val = getattr(value, "people_Person5", None)
                if opp_val is None:
                    setattr(value, "people_Person5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class people_Model:

    pass
class people_Person:

    def __init__(self, name: str, nicknames: str, age: int, alive: bool, luckyNumbers: int, lotteryChances: str, people_Person: "people_Model" = None, people_Person3: "people_Person" = None, people_Person1: "people_Person" = None, people_Person5: set["people_Pet"] = None):
        self.name = name
        self.nicknames = nicknames
        self.age = age
        self.alive = alive
        self.luckyNumbers = luckyNumbers
        self.lotteryChances = lotteryChances
        self.people_Person = people_Person
        self.people_Person3 = people_Person3
        self.people_Person1 = people_Person1
        self.people_Person5 = people_Person5 if people_Person5 is not None else set()
        
    @property
    def alive(self) -> bool:
        return self.__alive

    @alive.setter
    def alive(self, alive: bool):
        self.__alive = alive

    @property
    def nicknames(self) -> str:
        return self.__nicknames

    @nicknames.setter
    def nicknames(self, nicknames: str):
        self.__nicknames = nicknames

    @property
    def lotteryChances(self) -> str:
        return self.__lotteryChances

    @lotteryChances.setter
    def lotteryChances(self, lotteryChances: str):
        self.__lotteryChances = lotteryChances

    @property
    def luckyNumbers(self) -> int:
        return self.__luckyNumbers

    @luckyNumbers.setter
    def luckyNumbers(self, luckyNumbers: int):
        self.__luckyNumbers = luckyNumbers

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
    def people_Person3(self):
        return self.__people_Person3

    @people_Person3.setter
    def people_Person3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_people_Person__people_Person3", None)
        self.__people_Person3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "people_Person1"):
                opp_val = getattr(old_value, "people_Person1", None)
                if opp_val == self:
                    setattr(old_value, "people_Person1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "people_Person1"):
                opp_val = getattr(value, "people_Person1", None)
                setattr(value, "people_Person1", self)

    @property
    def people_Person1(self):
        return self.__people_Person1

    @people_Person1.setter
    def people_Person1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_people_Person__people_Person1", None)
        self.__people_Person1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "people_Person3"):
                opp_val = getattr(old_value, "people_Person3", None)
                if opp_val == self:
                    setattr(old_value, "people_Person3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "people_Person3"):
                opp_val = getattr(value, "people_Person3", None)
                setattr(value, "people_Person3", self)

    @property
    def people_Person(self):
        return self.__people_Person

    @people_Person.setter
    def people_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_people_Person__people_Person", None)
        self.__people_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "people_Model"):
                opp_val = getattr(old_value, "people_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "people_Model"):
                opp_val = getattr(value, "people_Model", None)
                if opp_val is None:
                    setattr(value, "people_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def people_Person5(self):
        return self.__people_Person5

    @people_Person5.setter
    def people_Person5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_people_Person__people_Person5", None)
        self.__people_Person5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "people_Pet"):
                    opp_val = getattr(item, "people_Pet", None)
                    
                    if opp_val == self:
                        setattr(item, "people_Pet", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "people_Pet"):
                    opp_val = getattr(item, "people_Pet", None)
                    
                    setattr(item, "people_Pet", self)
                    
