from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Named:

    pass
class school_School(Named):

    def __init__(self, school_School2: "school_SchoolStatistics" = None, school_School4: set["school_Person"] = None, school_School: "school_SchoolModel" = None):
        self.school_School2 = school_School2
        self.school_School4 = school_School4 if school_School4 is not None else set()
        self.school_School = school_School
        
    @property
    def school_School4(self):
        return self.__school_School4

    @school_School4.setter
    def school_School4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_School__school_School4", None)
        self.__school_School4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "school_Person"):
                    opp_val = getattr(item, "school_Person", None)
                    
                    if opp_val == self:
                        setattr(item, "school_Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "school_Person"):
                    opp_val = getattr(item, "school_Person", None)
                    
                    setattr(item, "school_Person", self)
                    

    @property
    def school_School2(self):
        return self.__school_School2

    @school_School2.setter
    def school_School2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_School__school_School2", None)
        self.__school_School2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_SchoolStatistics"):
                opp_val = getattr(old_value, "school_SchoolStatistics", None)
                if opp_val == self:
                    setattr(old_value, "school_SchoolStatistics", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_SchoolStatistics"):
                opp_val = getattr(value, "school_SchoolStatistics", None)
                setattr(value, "school_SchoolStatistics", self)

    @property
    def school_School(self):
        return self.__school_School

    @school_School.setter
    def school_School(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_School__school_School", None)
        self.__school_School = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_SchoolModel"):
                opp_val = getattr(old_value, "school_SchoolModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_SchoolModel"):
                opp_val = getattr(value, "school_SchoolModel", None)
                if opp_val is None:
                    setattr(value, "school_SchoolModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getTeachers(self):
        # TODO: Implement getTeachers method
        pass

    def getStudents(self):
        # TODO: Implement getStudents method
        pass

class school_SchoolModel:

    pass
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
                    

class school_Named(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class school_Person(Named):

    pass
class school_SchoolStatistics:

    def __init__(self, studentsNumber: int, teachersNumber: int, studentsWithNoTeacher: str, school_SchoolStatistics: "school_School" = None):
        self.studentsNumber = studentsNumber
        self.teachersNumber = teachersNumber
        self.studentsWithNoTeacher = studentsWithNoTeacher
        self.school_SchoolStatistics = school_SchoolStatistics
        
    @property
    def studentsWithNoTeacher(self) -> str:
        return self.__studentsWithNoTeacher

    @studentsWithNoTeacher.setter
    def studentsWithNoTeacher(self, studentsWithNoTeacher: str):
        self.__studentsWithNoTeacher = studentsWithNoTeacher

    @property
    def teachersNumber(self) -> int:
        return self.__teachersNumber

    @teachersNumber.setter
    def teachersNumber(self, teachersNumber: int):
        self.__teachersNumber = teachersNumber

    @property
    def studentsNumber(self) -> int:
        return self.__studentsNumber

    @studentsNumber.setter
    def studentsNumber(self, studentsNumber: int):
        self.__studentsNumber = studentsNumber

    @property
    def school_SchoolStatistics(self):
        return self.__school_SchoolStatistics

    @school_SchoolStatistics.setter
    def school_SchoolStatistics(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_SchoolStatistics__school_SchoolStatistics", None)
        self.__school_SchoolStatistics = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_School2"):
                opp_val = getattr(old_value, "school_School2", None)
                if opp_val == self:
                    setattr(old_value, "school_School2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_School2"):
                opp_val = getattr(value, "school_School2", None)
                setattr(value, "school_School2", self)
