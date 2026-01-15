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

class University_UniversityManagementSystem:

    pass
class University_Exam:

    def __init__(self, examID: str, University_Exam: "University_Course" = None):
        self.examID = examID
        self.University_Exam = University_Exam
        
    @property
    def examID(self) -> str:
        return self.__examID

    @examID.setter
    def examID(self, examID: str):
        self.__examID = examID

    @property
    def University_Exam(self):
        return self.__University_Exam

    @University_Exam.setter
    def University_Exam(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_University_Exam__University_Exam", None)
        self.__University_Exam = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "University_Course7"):
                opp_val = getattr(old_value, "University_Course7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "University_Course7"):
                opp_val = getattr(value, "University_Course7", None)
                if opp_val is None:
                    setattr(value, "University_Course7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class University_Course:

    def __init__(self, name: str, courseNumber: int, courseType: str, University_Course: "University_Student" = None, University_Course2: "University_Professor" = None, University_Course7: set["University_Exam"] = None, University_Course5: "University_Course" = None, University_Course3: set["University_Course"] = None, University_Course9: "University_UniversityManagementSystem" = None):
        self.name = name
        self.courseNumber = courseNumber
        self.courseType = courseType
        self.University_Course = University_Course
        self.University_Course2 = University_Course2
        self.University_Course7 = University_Course7 if University_Course7 is not None else set()
        self.University_Course5 = University_Course5
        self.University_Course3 = University_Course3 if University_Course3 is not None else set()
        self.University_Course9 = University_Course9
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def courseType(self) -> str:
        return self.__courseType

    @courseType.setter
    def courseType(self, courseType: str):
        self.__courseType = courseType

    @property
    def courseNumber(self) -> int:
        return self.__courseNumber

    @courseNumber.setter
    def courseNumber(self, courseNumber: int):
        self.__courseNumber = courseNumber

    @property
    def University_Course2(self):
        return self.__University_Course2

    @University_Course2.setter
    def University_Course2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_University_Course__University_Course2", None)
        self.__University_Course2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "University_Professor"):
                opp_val = getattr(old_value, "University_Professor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "University_Professor"):
                opp_val = getattr(value, "University_Professor", None)
                if opp_val is None:
                    setattr(value, "University_Professor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def University_Course3(self):
        return self.__University_Course3

    @University_Course3.setter
    def University_Course3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_University_Course__University_Course3", None)
        self.__University_Course3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "University_Course5"):
                    opp_val = getattr(item, "University_Course5", None)
                    
                    if opp_val == self:
                        setattr(item, "University_Course5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "University_Course5"):
                    opp_val = getattr(item, "University_Course5", None)
                    
                    setattr(item, "University_Course5", self)
                    

    @property
    def University_Course(self):
        return self.__University_Course

    @University_Course.setter
    def University_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_University_Course__University_Course", None)
        self.__University_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "University_Student"):
                opp_val = getattr(old_value, "University_Student", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "University_Student"):
                opp_val = getattr(value, "University_Student", None)
                if opp_val is None:
                    setattr(value, "University_Student", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def University_Course9(self):
        return self.__University_Course9

    @University_Course9.setter
    def University_Course9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_University_Course__University_Course9", None)
        self.__University_Course9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "University_UniversityManagementSystem"):
                opp_val = getattr(old_value, "University_UniversityManagementSystem", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "University_UniversityManagementSystem"):
                opp_val = getattr(value, "University_UniversityManagementSystem", None)
                if opp_val is None:
                    setattr(value, "University_UniversityManagementSystem", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def University_Course7(self):
        return self.__University_Course7

    @University_Course7.setter
    def University_Course7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_University_Course__University_Course7", None)
        self.__University_Course7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "University_Exam"):
                    opp_val = getattr(item, "University_Exam", None)
                    
                    if opp_val == self:
                        setattr(item, "University_Exam", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "University_Exam"):
                    opp_val = getattr(item, "University_Exam", None)
                    
                    setattr(item, "University_Exam", self)
                    

    @property
    def University_Course5(self):
        return self.__University_Course5

    @University_Course5.setter
    def University_Course5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_University_Course__University_Course5", None)
        self.__University_Course5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "University_Course3"):
                opp_val = getattr(old_value, "University_Course3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "University_Course3"):
                opp_val = getattr(value, "University_Course3", None)
                if opp_val is None:
                    setattr(value, "University_Course3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Person:

    pass
class University_Professor(Person):

    def __init__(self, employeeNumber: int, University_Professor: set["University_Course"] = None):
        self.employeeNumber = employeeNumber
        self.University_Professor = University_Professor if University_Professor is not None else set()
        
    @property
    def employeeNumber(self) -> int:
        return self.__employeeNumber

    @employeeNumber.setter
    def employeeNumber(self, employeeNumber: int):
        self.__employeeNumber = employeeNumber

    @property
    def University_Professor(self):
        return self.__University_Professor

    @University_Professor.setter
    def University_Professor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_University_Professor__University_Professor", None)
        self.__University_Professor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "University_Course2"):
                    opp_val = getattr(item, "University_Course2", None)
                    
                    if opp_val == self:
                        setattr(item, "University_Course2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "University_Course2"):
                    opp_val = getattr(item, "University_Course2", None)
                    
                    setattr(item, "University_Course2", self)
                    

class University_Student(Person):

    def __init__(self, matriculationNumber: int, University_Student: set["University_Course"] = None):
        self.matriculationNumber = matriculationNumber
        self.University_Student = University_Student if University_Student is not None else set()
        
    @property
    def matriculationNumber(self) -> int:
        return self.__matriculationNumber

    @matriculationNumber.setter
    def matriculationNumber(self, matriculationNumber: int):
        self.__matriculationNumber = matriculationNumber

    @property
    def University_Student(self):
        return self.__University_Student

    @University_Student.setter
    def University_Student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_University_Student__University_Student", None)
        self.__University_Student = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "University_Course"):
                    opp_val = getattr(item, "University_Course", None)
                    
                    if opp_val == self:
                        setattr(item, "University_Course", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "University_Course"):
                    opp_val = getattr(item, "University_Course", None)
                    
                    setattr(item, "University_Course", self)
                    

class University_Person(ABC):

    def __init__(self, name: str, email: str, University_Person: "University_UniversityManagementSystem" = None):
        self.name = name
        self.email = email
        self.University_Person = University_Person
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def University_Person(self):
        return self.__University_Person

    @University_Person.setter
    def University_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_University_Person__University_Person", None)
        self.__University_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "University_UniversityManagementSystem11"):
                opp_val = getattr(old_value, "University_UniversityManagementSystem11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "University_UniversityManagementSystem11"):
                opp_val = getattr(value, "University_UniversityManagementSystem11", None)
                if opp_val is None:
                    setattr(value, "University_UniversityManagementSystem11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
