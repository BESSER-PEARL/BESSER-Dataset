from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Month(Enum):
    January = "January"
    February = "February"
    March = "March"
    April = "April"
    May = "May"
    June = "June"
    July = "July"
    August = "August"
    September = "September"
    October = "October"
    November = "November"
    December = "December"


############################################
# Definition of Classes
############################################

class Person:

    pass
class family_Woman(Person):

    pass
class family_Man(Person):

    pass
class EModelElement:

    pass
class family_Person(EModelElement):

    def __init__(self, firstName: str, lastName: str, birthDay: int, birthMonth: str, birthYear: int, birthCity: str, family_Person: "family_Man" = None, family_Person9: "family_Woman" = None, family_Person11: set["family_Person"] = None, family_Person13: "family_Person" = None):
        self.firstName = firstName
        self.lastName = lastName
        self.birthDay = birthDay
        self.birthMonth = birthMonth
        self.birthYear = birthYear
        self.birthCity = birthCity
        self.family_Person = family_Person
        self.family_Person9 = family_Person9
        self.family_Person11 = family_Person11 if family_Person11 is not None else set()
        self.family_Person13 = family_Person13
        
    @property
    def birthMonth(self) -> str:
        return self.__birthMonth

    @birthMonth.setter
    def birthMonth(self, birthMonth: str):
        self.__birthMonth = birthMonth

    @property
    def birthDay(self) -> int:
        return self.__birthDay

    @birthDay.setter
    def birthDay(self, birthDay: int):
        self.__birthDay = birthDay

    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def birthYear(self) -> int:
        return self.__birthYear

    @birthYear.setter
    def birthYear(self, birthYear: int):
        self.__birthYear = birthYear

    @property
    def birthCity(self) -> str:
        return self.__birthCity

    @birthCity.setter
    def birthCity(self, birthCity: str):
        self.__birthCity = birthCity

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def family_Person11(self):
        return self.__family_Person11

    @family_Person11.setter
    def family_Person11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Person__family_Person11", None)
        self.__family_Person11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "family_Person13"):
                    opp_val = getattr(item, "family_Person13", None)
                    
                    if opp_val == self:
                        setattr(item, "family_Person13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "family_Person13"):
                    opp_val = getattr(item, "family_Person13", None)
                    
                    setattr(item, "family_Person13", self)
                    

    @property
    def family_Person9(self):
        return self.__family_Person9

    @family_Person9.setter
    def family_Person9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Person__family_Person9", None)
        self.__family_Person9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_Woman10"):
                opp_val = getattr(old_value, "family_Woman10", None)
                if opp_val == self:
                    setattr(old_value, "family_Woman10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_Woman10"):
                opp_val = getattr(value, "family_Woman10", None)
                setattr(value, "family_Woman10", self)

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
            if hasattr(old_value, "family_Man7"):
                opp_val = getattr(old_value, "family_Man7", None)
                if opp_val == self:
                    setattr(old_value, "family_Man7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_Man7"):
                opp_val = getattr(value, "family_Man7", None)
                setattr(value, "family_Man7", self)

    @property
    def family_Person13(self):
        return self.__family_Person13

    @family_Person13.setter
    def family_Person13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Person__family_Person13", None)
        self.__family_Person13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_Person11"):
                opp_val = getattr(old_value, "family_Person11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_Person11"):
                opp_val = getattr(value, "family_Person11", None)
                if opp_val is None:
                    setattr(value, "family_Person11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class family_Family(EModelElement):

    def __init__(self, name: str, family_Family: set["family_Man"] = None, family_Family2: set["family_Woman"] = None, family_Family5: "family_Family" = None, family_Family3: set["family_Family"] = None):
        self.name = name
        self.family_Family = family_Family if family_Family is not None else set()
        self.family_Family2 = family_Family2 if family_Family2 is not None else set()
        self.family_Family5 = family_Family5
        self.family_Family3 = family_Family3 if family_Family3 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def family_Family3(self):
        return self.__family_Family3

    @family_Family3.setter
    def family_Family3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Family__family_Family3", None)
        self.__family_Family3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "family_Family5"):
                    opp_val = getattr(item, "family_Family5", None)
                    
                    if opp_val == self:
                        setattr(item, "family_Family5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "family_Family5"):
                    opp_val = getattr(item, "family_Family5", None)
                    
                    setattr(item, "family_Family5", self)
                    

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
                if hasattr(item, "family_Man"):
                    opp_val = getattr(item, "family_Man", None)
                    
                    if opp_val == self:
                        setattr(item, "family_Man", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "family_Man"):
                    opp_val = getattr(item, "family_Man", None)
                    
                    setattr(item, "family_Man", self)
                    

    @property
    def family_Family2(self):
        return self.__family_Family2

    @family_Family2.setter
    def family_Family2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Family__family_Family2", None)
        self.__family_Family2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "family_Woman"):
                    opp_val = getattr(item, "family_Woman", None)
                    
                    if opp_val == self:
                        setattr(item, "family_Woman", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "family_Woman"):
                    opp_val = getattr(item, "family_Woman", None)
                    
                    setattr(item, "family_Woman", self)
                    

    @property
    def family_Family5(self):
        return self.__family_Family5

    @family_Family5.setter
    def family_Family5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_family_Family__family_Family5", None)
        self.__family_Family5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_Family3"):
                opp_val = getattr(old_value, "family_Family3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_Family3"):
                opp_val = getattr(value, "family_Family3", None)
                if opp_val is None:
                    setattr(value, "family_Family3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
