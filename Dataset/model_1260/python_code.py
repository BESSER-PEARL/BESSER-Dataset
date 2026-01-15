from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Sexe(Enum):
    FEMALE = "FEMALE"
    MALE = "MALE"


############################################
# Definition of Classes
############################################

class family_Car:

    def __init__(self, numberOfSeats: str, family_Car: "family_Person" = None):
        self.numberOfSeats = numberOfSeats
        self.family_Car = family_Car
        
    @property
    def numberOfSeats(self) -> str:
        return self.__numberOfSeats

    @numberOfSeats.setter
    def numberOfSeats(self, numberOfSeats: str):
        self.__numberOfSeats = numberOfSeats

    @property
    def family_Car(self):
        return self.__family_Car

    @family_Car.setter
    def family_Car(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Car__family_Car", None)
        self.__family_Car = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_Person4"):
                opp_val = getattr(old_value, "family_Person4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_Person4"):
                opp_val = getattr(value, "family_Person4", None)
                if opp_val is None:
                    setattr(value, "family_Person4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class family_Address:

    def __init__(self, street: str, family_Address: "family_Family" = None):
        self.street = street
        self.family_Address = family_Address
        
    @property
    def street(self) -> str:
        return self.__street

    @street.setter
    def street(self, street: str):
        self.__street = street

    @property
    def family_Address(self):
        return self.__family_Address

    @family_Address.setter
    def family_Address(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Address__family_Address", None)
        self.__family_Address = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_Family2"):
                opp_val = getattr(old_value, "family_Family2", None)
                if opp_val == self:
                    setattr(old_value, "family_Family2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_Family2"):
                opp_val = getattr(value, "family_Family2", None)
                setattr(value, "family_Family2", self)

class family_Person:

    def __init__(self, firstName: str, sexe: str, family_Person: "family_Family" = None, family_Person4: set["family_Car"] = None):
        self.firstName = firstName
        self.sexe = sexe
        self.family_Person = family_Person
        self.family_Person4 = family_Person4 if family_Person4 is not None else set()
        
    @property
    def sexe(self) -> str:
        return self.__sexe

    @sexe.setter
    def sexe(self, sexe: str):
        self.__sexe = sexe

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

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
    def family_Person4(self):
        return self.__family_Person4

    @family_Person4.setter
    def family_Person4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Person__family_Person4", None)
        self.__family_Person4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "family_Car"):
                    opp_val = getattr(item, "family_Car", None)
                    
                    if opp_val == self:
                        setattr(item, "family_Car", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "family_Car"):
                    opp_val = getattr(item, "family_Car", None)
                    
                    setattr(item, "family_Car", self)
                    

class family_Family:

    def __init__(self, surname: str, numberOfPets: int, hasASwimmingPool: bool, favoriteHolidayDestinations: str, family_Family: set["family_Person"] = None, family_Family2: "family_Address" = None):
        self.surname = surname
        self.numberOfPets = numberOfPets
        self.hasASwimmingPool = hasASwimmingPool
        self.favoriteHolidayDestinations = favoriteHolidayDestinations
        self.family_Family = family_Family if family_Family is not None else set()
        self.family_Family2 = family_Family2
        
    @property
    def favoriteHolidayDestinations(self) -> str:
        return self.__favoriteHolidayDestinations

    @favoriteHolidayDestinations.setter
    def favoriteHolidayDestinations(self, favoriteHolidayDestinations: str):
        self.__favoriteHolidayDestinations = favoriteHolidayDestinations

    @property
    def numberOfPets(self) -> int:
        return self.__numberOfPets

    @numberOfPets.setter
    def numberOfPets(self, numberOfPets: int):
        self.__numberOfPets = numberOfPets

    @property
    def surname(self) -> str:
        return self.__surname

    @surname.setter
    def surname(self, surname: str):
        self.__surname = surname

    @property
    def hasASwimmingPool(self) -> bool:
        return self.__hasASwimmingPool

    @hasASwimmingPool.setter
    def hasASwimmingPool(self, hasASwimmingPool: bool):
        self.__hasASwimmingPool = hasASwimmingPool

    @property
    def family_Family2(self):
        return self.__family_Family2

    @family_Family2.setter
    def family_Family2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Family__family_Family2", None)
        self.__family_Family2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_Address"):
                opp_val = getattr(old_value, "family_Address", None)
                if opp_val == self:
                    setattr(old_value, "family_Address", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_Address"):
                opp_val = getattr(value, "family_Address", None)
                setattr(value, "family_Address", self)

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
                if hasattr(item, "family_Person"):
                    opp_val = getattr(item, "family_Person", None)
                    
                    if opp_val == self:
                        setattr(item, "family_Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "family_Person"):
                    opp_val = getattr(item, "family_Person", None)
                    
                    setattr(item, "family_Person", self)
                    

class Family:

    pass
class family_WealthyFamily(Family):

    def __init__(self, forbesRanking: int):
        self.forbesRanking = forbesRanking
        
    @property
    def forbesRanking(self) -> int:
        return self.__forbesRanking

    @forbesRanking.setter
    def forbesRanking(self, forbesRanking: int):
        self.__forbesRanking = forbesRanking
