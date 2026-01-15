from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class family_Person:

    def __init__(self, age: int, family_Person: "family_Family" = None):
        self.age = age
        self.family_Person = family_Person
        
    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age

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

class family_Family:

    def __init__(self, memberCount: int, averageAge: float, family_Family: set["family_Person"] = None):
        self.memberCount = memberCount
        self.averageAge = averageAge
        self.family_Family = family_Family if family_Family is not None else set()
        
    @property
    def averageAge(self) -> float:
        return self.__averageAge

    @averageAge.setter
    def averageAge(self, averageAge: float):
        self.__averageAge = averageAge

    @property
    def memberCount(self) -> int:
        return self.__memberCount

    @memberCount.setter
    def memberCount(self, memberCount: int):
        self.__memberCount = memberCount

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
                    
