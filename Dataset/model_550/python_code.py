from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Person:

    pass
class family_Woman(Person):

    pass
class family_Person(ABC):

    def __init__(self, name: str, eCivil: str, provincia: str, fechaNacimiento: str, family_Person2: "family_Man" = None, family_Person: "family_Family" = None, family_Person4: "family_Woman" = None):
        self.name = name
        self.eCivil = eCivil
        self.provincia = provincia
        self.fechaNacimiento = fechaNacimiento
        self.family_Person2 = family_Person2
        self.family_Person = family_Person
        self.family_Person4 = family_Person4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def provincia(self) -> str:
        return self.__provincia

    @provincia.setter
    def provincia(self, provincia: str):
        self.__provincia = provincia

    @property
    def eCivil(self) -> str:
        return self.__eCivil

    @eCivil.setter
    def eCivil(self, eCivil: str):
        self.__eCivil = eCivil

    @property
    def fechaNacimiento(self) -> str:
        return self.__fechaNacimiento

    @fechaNacimiento.setter
    def fechaNacimiento(self, fechaNacimiento: str):
        self.__fechaNacimiento = fechaNacimiento

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
        self.__family_Person4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "family_Woman"):
                opp_val = getattr(old_value, "family_Woman", None)
                if opp_val == self:
                    setattr(old_value, "family_Woman", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_Woman"):
                opp_val = getattr(value, "family_Woman", None)
                setattr(value, "family_Woman", self)

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
            if hasattr(old_value, "family_Man"):
                opp_val = getattr(old_value, "family_Man", None)
                if opp_val == self:
                    setattr(old_value, "family_Man", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "family_Man"):
                opp_val = getattr(value, "family_Man", None)
                setattr(value, "family_Man", self)

class family_Family:

    def __init__(self, name: str, family_Family: set["family_Person"] = None):
        self.name = name
        self.family_Family = family_Family if family_Family is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
                    

class family_Man(Person):

    pass