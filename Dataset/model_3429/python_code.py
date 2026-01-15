from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class school_Named(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Person:

    pass
class school_Teacher(Person):

    pass
class school_Student(Person):

    def __init__(self, registrationNum: int, school_Student: set["school_Teacher"] = None):
        self.registrationNum = registrationNum
        self.school_Student = school_Student if school_Student is not None else set()
        
    @property
    def registrationNum(self) -> int:
        return self.__registrationNum

    @registrationNum.setter
    def registrationNum(self, registrationNum: int):
        self.__registrationNum = registrationNum

    @property
    def school_Student(self):
        return self.__school_Student

    @school_Student.setter
    def school_Student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Student__school_Student", None)
        self.__school_Student = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "school_Teacher"):
                    opp_val = getattr(item, "school_Teacher", None)
                    
                    if opp_val == self:
                        setattr(item, "school_Teacher", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "school_Teacher"):
                    opp_val = getattr(item, "school_Teacher", None)
                    
                    setattr(item, "school_Teacher", self)
                    

class Named:

    pass
class school_Person(Named):

    pass
class school_School(Named):

    pass
class school_SchoolModel:

    pass