from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class OperatorType(Enum):
    XOR = "XOR"
    AND = "AND"
    OR = "OR"


############################################
# Definition of Classes
############################################

class Univerity_uncertainty_aUniversity(ABC):

    pass
class uUniversity:

    pass
class uncertainty_Univerity_University:

    pass
class Univerity_uncertainty_aPerson(ABC):

    pass
class uPerson:

    pass
class uncertainty_Univerity_Person:

    pass
class Univerity_uncertainty_aCourses(ABC):

    pass
class uCourses:

    pass
class Univerity_uncertainty_UData(ABC):

    def __init__(self, name: str, utype: str):
        self.name = name
        self.utype = utype
        
    @property
    def utype(self) -> str:
        return self.__utype

    @utype.setter
    def utype(self, utype: str):
        self.__utype = utype

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class uncertainty_Univerity_Courses:

    pass
class ModelElement:

    pass
class uncertainty_UData:

    pass
class uncertainty_aUniversity:

    pass
class Univerity_uncertainty_uUniversity(uncertainty_UData, uncertainty_aUniversity):

    pass
class uncertainty_aPerson:

    pass
class Univerity_uncertainty_uPerson(uncertainty_UData, uncertainty_aPerson):

    pass
class Univerity_uncertainty_ModelElement(ABC):

    pass
class aPerson:

    pass
class aCourses:

    pass
class uncertainty_aCourses:

    pass
class Univerity_uncertainty_uCourses(uncertainty_aCourses, uncertainty_UData):

    pass
class uncertainty_ModelElement:

    pass
class Univerity_University(uncertainty_ModelElement, uncertainty_aUniversity):

    pass
class Univerity_Person(uncertainty_ModelElement, uncertainty_aPerson):

    def __init__(self, Name: str, Email: str, Univerity_Person: "aPerson" = None):
        self.Name = Name
        self.Email = Email
        self.Univerity_Person = Univerity_Person
        
    @property
    def Email(self) -> str:
        return self.__Email

    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Univerity_Person(self):
        return self.__Univerity_Person

    @Univerity_Person.setter
    def Univerity_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Univerity_Person__Univerity_Person", None)
        self.__Univerity_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aPerson7"):
                opp_val = getattr(old_value, "aPerson7", None)
                if opp_val == self:
                    setattr(old_value, "aPerson7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aPerson7"):
                opp_val = getattr(value, "aPerson7", None)
                setattr(value, "aPerson7", self)

class Univerity_Courses(uncertainty_ModelElement, uncertainty_aCourses):

    def __init__(self, Name: str, CFU: int, Semester: str, Univerity_Courses2: "aPerson" = None, Univerity_Courses4: set["aPerson"] = None, Univerity_Courses: set["aCourses"] = None):
        self.Name = Name
        self.CFU = CFU
        self.Semester = Semester
        self.Univerity_Courses2 = Univerity_Courses2
        self.Univerity_Courses4 = Univerity_Courses4 if Univerity_Courses4 is not None else set()
        self.Univerity_Courses = Univerity_Courses if Univerity_Courses is not None else set()
        
    @property
    def Semester(self) -> str:
        return self.__Semester

    @Semester.setter
    def Semester(self, Semester: str):
        self.__Semester = Semester

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def CFU(self) -> int:
        return self.__CFU

    @CFU.setter
    def CFU(self, CFU: int):
        self.__CFU = CFU

    @property
    def Univerity_Courses(self):
        return self.__Univerity_Courses

    @Univerity_Courses.setter
    def Univerity_Courses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Univerity_Courses__Univerity_Courses", None)
        self.__Univerity_Courses = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aCourses"):
                    opp_val = getattr(item, "aCourses", None)
                    
                    if opp_val == self:
                        setattr(item, "aCourses", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aCourses"):
                    opp_val = getattr(item, "aCourses", None)
                    
                    setattr(item, "aCourses", self)
                    

    @property
    def Univerity_Courses4(self):
        return self.__Univerity_Courses4

    @Univerity_Courses4.setter
    def Univerity_Courses4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Univerity_Courses__Univerity_Courses4", None)
        self.__Univerity_Courses4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "aPerson5"):
                    opp_val = getattr(item, "aPerson5", None)
                    
                    if opp_val == self:
                        setattr(item, "aPerson5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "aPerson5"):
                    opp_val = getattr(item, "aPerson5", None)
                    
                    setattr(item, "aPerson5", self)
                    

    @property
    def Univerity_Courses2(self):
        return self.__Univerity_Courses2

    @Univerity_Courses2.setter
    def Univerity_Courses2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Univerity_Courses__Univerity_Courses2", None)
        self.__Univerity_Courses2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "aPerson"):
                opp_val = getattr(old_value, "aPerson", None)
                if opp_val == self:
                    setattr(old_value, "aPerson", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "aPerson"):
                opp_val = getattr(value, "aPerson", None)
                setattr(value, "aPerson", self)
