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

class aUniversity:

    pass
class UniverityU_uncertainty_aPerson(ABC):

    pass
class uPerson:

    pass
class UniverityU_uncertainty_aUniversity(ABC):

    pass
class uUniversity:

    pass
class uncertainty_UData:

    pass
class UniverityU_uncertainty_UData(ABC):

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

class UniverityU_uncertainty_aCourses(ABC):

    pass
class uCourses:

    pass
class uncertainty_aPerson:

    pass
class UniverityU_uncertainty_uPerson(uncertainty_UData, uncertainty_aPerson):

    pass
class aPerson:

    pass
class ModelElement:

    pass
class UniverityU_uncertainty_ModelElement(ABC):

    pass
class uncertainty_aUniversity:

    pass
class UniverityU_uncertainty_uUniversity(uncertainty_UData, uncertainty_aUniversity):

    pass
class aCourses:

    pass
class uncertainty_aCourses:

    pass
class UniverityU_uncertainty_uCourses(uncertainty_UData, uncertainty_aCourses):

    pass
class uncertainty_ModelElement:

    pass
class UniverityU_Person(uncertainty_ModelElement, uncertainty_aPerson):

    def __init__(self, Email: str, Name: str, UniverityU_Person: "aPerson" = None):
        self.Email = Email
        self.Name = Name
        self.UniverityU_Person = UniverityU_Person
        
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
    def UniverityU_Person(self):
        return self.__UniverityU_Person

    @UniverityU_Person.setter
    def UniverityU_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UniverityU_Person__UniverityU_Person", None)
        self.__UniverityU_Person = value
        
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

class UniverityU_University(uncertainty_ModelElement, uncertainty_aUniversity):

    pass
class UniverityU_Courses(uncertainty_ModelElement, uncertainty_aCourses):

    def __init__(self, Name: str, CFU: int, Semester: str, UniverityU_Courses: set["aCourses"] = None, UniverityU_Courses2: "aPerson" = None, UniverityU_Courses4: set["aPerson"] = None):
        self.Name = Name
        self.CFU = CFU
        self.Semester = Semester
        self.UniverityU_Courses = UniverityU_Courses if UniverityU_Courses is not None else set()
        self.UniverityU_Courses2 = UniverityU_Courses2
        self.UniverityU_Courses4 = UniverityU_Courses4 if UniverityU_Courses4 is not None else set()
        
    @property
    def Semester(self) -> str:
        return self.__Semester

    @Semester.setter
    def Semester(self, Semester: str):
        self.__Semester = Semester

    @property
    def CFU(self) -> int:
        return self.__CFU

    @CFU.setter
    def CFU(self, CFU: int):
        self.__CFU = CFU

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def UniverityU_Courses4(self):
        return self.__UniverityU_Courses4

    @UniverityU_Courses4.setter
    def UniverityU_Courses4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UniverityU_Courses__UniverityU_Courses4", None)
        self.__UniverityU_Courses4 = value if value is not None else set()
        
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
    def UniverityU_Courses2(self):
        return self.__UniverityU_Courses2

    @UniverityU_Courses2.setter
    def UniverityU_Courses2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UniverityU_Courses__UniverityU_Courses2", None)
        self.__UniverityU_Courses2 = value
        
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

    @property
    def UniverityU_Courses(self):
        return self.__UniverityU_Courses

    @UniverityU_Courses.setter
    def UniverityU_Courses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UniverityU_Courses__UniverityU_Courses", None)
        self.__UniverityU_Courses = value if value is not None else set()
        
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
                    
