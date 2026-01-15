from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Person:

    pass
class persons_Female(Person):

    pass
class persons_Male(Person):

    pass
class persons_Person(ABC):

    def __init__(self, fullName: str, birthday: date, persons_Person: "persons_PersonRegister" = None):
        self.fullName = fullName
        self.birthday = birthday
        self.persons_Person = persons_Person
        
    @property
    def fullName(self) -> str:
        return self.__fullName

    @fullName.setter
    def fullName(self, fullName: str):
        self.__fullName = fullName

    @property
    def birthday(self) -> date:
        return self.__birthday

    @birthday.setter
    def birthday(self, birthday: date):
        self.__birthday = birthday

    @property
    def persons_Person(self):
        return self.__persons_Person

    @persons_Person.setter
    def persons_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persons_Person__persons_Person", None)
        self.__persons_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persons_PersonRegister"):
                opp_val = getattr(old_value, "persons_PersonRegister", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persons_PersonRegister"):
                opp_val = getattr(value, "persons_PersonRegister", None)
                if opp_val is None:
                    setattr(value, "persons_PersonRegister", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class persons_PersonRegister:

    def __init__(self, id: str, persons_PersonRegister: set["persons_Person"] = None):
        self.id = id
        self.persons_PersonRegister = persons_PersonRegister if persons_PersonRegister is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def persons_PersonRegister(self):
        return self.__persons_PersonRegister

    @persons_PersonRegister.setter
    def persons_PersonRegister(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_persons_PersonRegister__persons_PersonRegister", None)
        self.__persons_PersonRegister = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "persons_Person"):
                    opp_val = getattr(item, "persons_Person", None)
                    
                    if opp_val == self:
                        setattr(item, "persons_Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "persons_Person"):
                    opp_val = getattr(item, "persons_Person", None)
                    
                    setattr(item, "persons_Person", self)
                    
