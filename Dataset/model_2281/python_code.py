from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class CourseType(Enum):
    VO = "VO"
    UE = "UE"
    SEM = "SEM"
    PR = "PR"


############################################
# Definition of Classes
############################################

class dmm_UniversityManagementSystem:

    pass
class dmm_Exam:

    def __init__(self, examID: str, dmm_Exam: "dmm_Course" = None):
        self.examID = examID
        self.dmm_Exam = dmm_Exam
        
    @property
    def examID(self) -> str:
        return self.__examID

    @examID.setter
    def examID(self, examID: str):
        self.__examID = examID

    @property
    def dmm_Exam(self):
        return self.__dmm_Exam

    @dmm_Exam.setter
    def dmm_Exam(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dmm_Exam__dmm_Exam", None)
        self.__dmm_Exam = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dmm_Course7"):
                opp_val = getattr(old_value, "dmm_Course7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dmm_Course7"):
                opp_val = getattr(value, "dmm_Course7", None)
                if opp_val is None:
                    setattr(value, "dmm_Course7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class dmm_Course:

    def __init__(self, courseType: str, name: str, courseNumber: int, dmm_Course: "dmm_Student" = None, dmm_Course2: "dmm_Professor" = None, dmm_Course5: "dmm_Course" = None, dmm_Course3: set["dmm_Course"] = None, dmm_Course7: set["dmm_Exam"] = None, dmm_Course9: "dmm_UniversityManagementSystem" = None):
        self.courseType = courseType
        self.name = name
        self.courseNumber = courseNumber
        self.dmm_Course = dmm_Course
        self.dmm_Course2 = dmm_Course2
        self.dmm_Course5 = dmm_Course5
        self.dmm_Course3 = dmm_Course3 if dmm_Course3 is not None else set()
        self.dmm_Course7 = dmm_Course7 if dmm_Course7 is not None else set()
        self.dmm_Course9 = dmm_Course9
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def courseNumber(self) -> int:
        return self.__courseNumber

    @courseNumber.setter
    def courseNumber(self, courseNumber: int):
        self.__courseNumber = courseNumber

    @property
    def courseType(self) -> str:
        return self.__courseType

    @courseType.setter
    def courseType(self, courseType: str):
        self.__courseType = courseType

    @property
    def dmm_Course5(self):
        return self.__dmm_Course5

    @dmm_Course5.setter
    def dmm_Course5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dmm_Course__dmm_Course5", None)
        self.__dmm_Course5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dmm_Course3"):
                opp_val = getattr(old_value, "dmm_Course3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dmm_Course3"):
                opp_val = getattr(value, "dmm_Course3", None)
                if opp_val is None:
                    setattr(value, "dmm_Course3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dmm_Course2(self):
        return self.__dmm_Course2

    @dmm_Course2.setter
    def dmm_Course2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dmm_Course__dmm_Course2", None)
        self.__dmm_Course2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dmm_Professor"):
                opp_val = getattr(old_value, "dmm_Professor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dmm_Professor"):
                opp_val = getattr(value, "dmm_Professor", None)
                if opp_val is None:
                    setattr(value, "dmm_Professor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dmm_Course9(self):
        return self.__dmm_Course9

    @dmm_Course9.setter
    def dmm_Course9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dmm_Course__dmm_Course9", None)
        self.__dmm_Course9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dmm_UniversityManagementSystem"):
                opp_val = getattr(old_value, "dmm_UniversityManagementSystem", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dmm_UniversityManagementSystem"):
                opp_val = getattr(value, "dmm_UniversityManagementSystem", None)
                if opp_val is None:
                    setattr(value, "dmm_UniversityManagementSystem", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dmm_Course(self):
        return self.__dmm_Course

    @dmm_Course.setter
    def dmm_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dmm_Course__dmm_Course", None)
        self.__dmm_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dmm_Student"):
                opp_val = getattr(old_value, "dmm_Student", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dmm_Student"):
                opp_val = getattr(value, "dmm_Student", None)
                if opp_val is None:
                    setattr(value, "dmm_Student", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def dmm_Course3(self):
        return self.__dmm_Course3

    @dmm_Course3.setter
    def dmm_Course3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dmm_Course__dmm_Course3", None)
        self.__dmm_Course3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dmm_Course5"):
                    opp_val = getattr(item, "dmm_Course5", None)
                    
                    if opp_val == self:
                        setattr(item, "dmm_Course5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dmm_Course5"):
                    opp_val = getattr(item, "dmm_Course5", None)
                    
                    setattr(item, "dmm_Course5", self)
                    

    @property
    def dmm_Course7(self):
        return self.__dmm_Course7

    @dmm_Course7.setter
    def dmm_Course7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dmm_Course__dmm_Course7", None)
        self.__dmm_Course7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dmm_Exam"):
                    opp_val = getattr(item, "dmm_Exam", None)
                    
                    if opp_val == self:
                        setattr(item, "dmm_Exam", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dmm_Exam"):
                    opp_val = getattr(item, "dmm_Exam", None)
                    
                    setattr(item, "dmm_Exam", self)
                    

class Person:

    pass
class dmm_Professor(Person):

    def __init__(self, employeeNumber: int, dmm_Professor: set["dmm_Course"] = None):
        self.employeeNumber = employeeNumber
        self.dmm_Professor = dmm_Professor if dmm_Professor is not None else set()
        
    @property
    def employeeNumber(self) -> int:
        return self.__employeeNumber

    @employeeNumber.setter
    def employeeNumber(self, employeeNumber: int):
        self.__employeeNumber = employeeNumber

    @property
    def dmm_Professor(self):
        return self.__dmm_Professor

    @dmm_Professor.setter
    def dmm_Professor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dmm_Professor__dmm_Professor", None)
        self.__dmm_Professor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dmm_Course2"):
                    opp_val = getattr(item, "dmm_Course2", None)
                    
                    if opp_val == self:
                        setattr(item, "dmm_Course2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dmm_Course2"):
                    opp_val = getattr(item, "dmm_Course2", None)
                    
                    setattr(item, "dmm_Course2", self)
                    

class dmm_Student(Person):

    def __init__(self, matriculationNumber: int, dmm_Student: set["dmm_Course"] = None):
        self.matriculationNumber = matriculationNumber
        self.dmm_Student = dmm_Student if dmm_Student is not None else set()
        
    @property
    def matriculationNumber(self) -> int:
        return self.__matriculationNumber

    @matriculationNumber.setter
    def matriculationNumber(self, matriculationNumber: int):
        self.__matriculationNumber = matriculationNumber

    @property
    def dmm_Student(self):
        return self.__dmm_Student

    @dmm_Student.setter
    def dmm_Student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dmm_Student__dmm_Student", None)
        self.__dmm_Student = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "dmm_Course"):
                    opp_val = getattr(item, "dmm_Course", None)
                    
                    if opp_val == self:
                        setattr(item, "dmm_Course", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "dmm_Course"):
                    opp_val = getattr(item, "dmm_Course", None)
                    
                    setattr(item, "dmm_Course", self)
                    

class dmm_Person(ABC):

    def __init__(self, name: str, email: str, dmm_Person: "dmm_UniversityManagementSystem" = None):
        self.name = name
        self.email = email
        self.dmm_Person = dmm_Person
        
    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dmm_Person(self):
        return self.__dmm_Person

    @dmm_Person.setter
    def dmm_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_dmm_Person__dmm_Person", None)
        self.__dmm_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dmm_UniversityManagementSystem11"):
                opp_val = getattr(old_value, "dmm_UniversityManagementSystem11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dmm_UniversityManagementSystem11"):
                opp_val = getattr(value, "dmm_UniversityManagementSystem11", None)
                if opp_val is None:
                    setattr(value, "dmm_UniversityManagementSystem11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
