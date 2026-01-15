from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class CourseType(Enum):
    Obligatory = "Obligatory"
    Elective = "Elective"
    M2A = "M2A"
    M1A = "M1A"
class ProgrammeType(Enum):
    YEAR_STUDY = "YEAR_STUDY"
    BACHELOR = "BACHELOR"
    MASTER_2_YEARS = "MASTER_2_YEARS"
    INTEGRATED_MASTER = "INTEGRATED_MASTER"
class SemesterType(Enum):
    FALL = "FALL"
    SPRING = "SPRING"
class CourseLevel(Enum):
    HIGHER = "HIGHER"
    PHD = "PHD"
    THIRD_YEAR = "THIRD_YEAR"


############################################
# Definition of Classes
############################################

class programme_SemesterCourse:

    def __init__(self, courseType: str, programme_SemesterCourse18: "programme_Course" = None, programme_SemesterCourse: "programme_Semester" = None):
        self.courseType = courseType
        self.programme_SemesterCourse18 = programme_SemesterCourse18
        self.programme_SemesterCourse = programme_SemesterCourse
        
    @property
    def courseType(self) -> str:
        return self.__courseType

    @courseType.setter
    def courseType(self, courseType: str):
        self.__courseType = courseType

    @property
    def programme_SemesterCourse18(self):
        return self.__programme_SemesterCourse18

    @programme_SemesterCourse18.setter
    def programme_SemesterCourse18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_programme_SemesterCourse__programme_SemesterCourse18", None)
        self.__programme_SemesterCourse18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "programme_Course19"):
                opp_val = getattr(old_value, "programme_Course19", None)
                if opp_val == self:
                    setattr(old_value, "programme_Course19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "programme_Course19"):
                opp_val = getattr(value, "programme_Course19", None)
                setattr(value, "programme_Course19", self)

    @property
    def programme_SemesterCourse(self):
        return self.__programme_SemesterCourse

    @programme_SemesterCourse.setter
    def programme_SemesterCourse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_programme_SemesterCourse__programme_SemesterCourse", None)
        self.__programme_SemesterCourse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "programme_Semester16"):
                opp_val = getattr(old_value, "programme_Semester16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "programme_Semester16"):
                opp_val = getattr(value, "programme_Semester16", None)
                if opp_val is None:
                    setattr(value, "programme_Semester16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class programme_Semester:

    def __init__(self, semesterType: str, programme_Semester: "programme_StudyYear" = None, programme_Semester16: set["programme_SemesterCourse"] = None):
        self.semesterType = semesterType
        self.programme_Semester = programme_Semester
        self.programme_Semester16 = programme_Semester16 if programme_Semester16 is not None else set()
        
    @property
    def semesterType(self) -> str:
        return self.__semesterType

    @semesterType.setter
    def semesterType(self, semesterType: str):
        self.__semesterType = semesterType

    @property
    def programme_Semester16(self):
        return self.__programme_Semester16

    @programme_Semester16.setter
    def programme_Semester16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_programme_Semester__programme_Semester16", None)
        self.__programme_Semester16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "programme_SemesterCourse"):
                    opp_val = getattr(item, "programme_SemesterCourse", None)
                    
                    if opp_val == self:
                        setattr(item, "programme_SemesterCourse", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "programme_SemesterCourse"):
                    opp_val = getattr(item, "programme_SemesterCourse", None)
                    
                    setattr(item, "programme_SemesterCourse", self)
                    

    @property
    def programme_Semester(self):
        return self.__programme_Semester

    @programme_Semester.setter
    def programme_Semester(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_programme_Semester__programme_Semester", None)
        self.__programme_Semester = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "programme_StudyYear14"):
                opp_val = getattr(old_value, "programme_StudyYear14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "programme_StudyYear14"):
                opp_val = getattr(value, "programme_StudyYear14", None)
                if opp_val is None:
                    setattr(value, "programme_StudyYear14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class programme_StudyYear:

    def __init__(self, year: int, programme_StudyYear: "programme_Programme" = None, programme_StudyYear12: "programme_Specialization" = None, programme_StudyYear14: set["programme_Semester"] = None):
        self.year = year
        self.programme_StudyYear = programme_StudyYear
        self.programme_StudyYear12 = programme_StudyYear12
        self.programme_StudyYear14 = programme_StudyYear14 if programme_StudyYear14 is not None else set()
        
    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def programme_StudyYear14(self):
        return self.__programme_StudyYear14

    @programme_StudyYear14.setter
    def programme_StudyYear14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_programme_StudyYear__programme_StudyYear14", None)
        self.__programme_StudyYear14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "programme_Semester"):
                    opp_val = getattr(item, "programme_Semester", None)
                    
                    if opp_val == self:
                        setattr(item, "programme_Semester", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "programme_Semester"):
                    opp_val = getattr(item, "programme_Semester", None)
                    
                    setattr(item, "programme_Semester", self)
                    

    @property
    def programme_StudyYear(self):
        return self.__programme_StudyYear

    @programme_StudyYear.setter
    def programme_StudyYear(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_programme_StudyYear__programme_StudyYear", None)
        self.__programme_StudyYear = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "programme_Programme6"):
                opp_val = getattr(old_value, "programme_Programme6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "programme_Programme6"):
                opp_val = getattr(value, "programme_Programme6", None)
                if opp_val is None:
                    setattr(value, "programme_Programme6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def programme_StudyYear12(self):
        return self.__programme_StudyYear12

    @programme_StudyYear12.setter
    def programme_StudyYear12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_programme_StudyYear__programme_StudyYear12", None)
        self.__programme_StudyYear12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "programme_Specialization11"):
                opp_val = getattr(old_value, "programme_Specialization11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "programme_Specialization11"):
                opp_val = getattr(value, "programme_Specialization11", None)
                if opp_val is None:
                    setattr(value, "programme_Specialization11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class programme_Programme:

    def __init__(self, name: str, programmeType: str, code: str, programme_Programme4: set["programme_Specialization"] = None, programme_Programme: "programme_Department" = None, programme_Programme6: set["programme_StudyYear"] = None):
        self.name = name
        self.programmeType = programmeType
        self.code = code
        self.programme_Programme4 = programme_Programme4 if programme_Programme4 is not None else set()
        self.programme_Programme = programme_Programme
        self.programme_Programme6 = programme_Programme6 if programme_Programme6 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def programmeType(self) -> str:
        return self.__programmeType

    @programmeType.setter
    def programmeType(self, programmeType: str):
        self.__programmeType = programmeType

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def programme_Programme4(self):
        return self.__programme_Programme4

    @programme_Programme4.setter
    def programme_Programme4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_programme_Programme__programme_Programme4", None)
        self.__programme_Programme4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "programme_Specialization"):
                    opp_val = getattr(item, "programme_Specialization", None)
                    
                    if opp_val == self:
                        setattr(item, "programme_Specialization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "programme_Specialization"):
                    opp_val = getattr(item, "programme_Specialization", None)
                    
                    setattr(item, "programme_Specialization", self)
                    

    @property
    def programme_Programme(self):
        return self.__programme_Programme

    @programme_Programme.setter
    def programme_Programme(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_programme_Programme__programme_Programme", None)
        self.__programme_Programme = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "programme_Department"):
                opp_val = getattr(old_value, "programme_Department", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "programme_Department"):
                opp_val = getattr(value, "programme_Department", None)
                if opp_val is None:
                    setattr(value, "programme_Department", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def programme_Programme6(self):
        return self.__programme_Programme6

    @programme_Programme6.setter
    def programme_Programme6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_programme_Programme__programme_Programme6", None)
        self.__programme_Programme6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "programme_StudyYear"):
                    opp_val = getattr(item, "programme_StudyYear", None)
                    
                    if opp_val == self:
                        setattr(item, "programme_StudyYear", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "programme_StudyYear"):
                    opp_val = getattr(item, "programme_StudyYear", None)
                    
                    setattr(item, "programme_StudyYear", self)
                    

class programme_Department:

    def __init__(self, name: str, programme_Department2: set["programme_Course"] = None, programme_Department: set["programme_Programme"] = None):
        self.name = name
        self.programme_Department2 = programme_Department2 if programme_Department2 is not None else set()
        self.programme_Department = programme_Department if programme_Department is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def programme_Department(self):
        return self.__programme_Department

    @programme_Department.setter
    def programme_Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_programme_Department__programme_Department", None)
        self.__programme_Department = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "programme_Programme"):
                    opp_val = getattr(item, "programme_Programme", None)
                    
                    if opp_val == self:
                        setattr(item, "programme_Programme", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "programme_Programme"):
                    opp_val = getattr(item, "programme_Programme", None)
                    
                    setattr(item, "programme_Programme", self)
                    

    @property
    def programme_Department2(self):
        return self.__programme_Department2

    @programme_Department2.setter
    def programme_Department2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_programme_Department__programme_Department2", None)
        self.__programme_Department2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "programme_Course"):
                    opp_val = getattr(item, "programme_Course", None)
                    
                    if opp_val == self:
                        setattr(item, "programme_Course", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "programme_Course"):
                    opp_val = getattr(item, "programme_Course", None)
                    
                    setattr(item, "programme_Course", self)
                    

class programme_Specialization:

    def __init__(self, name: str, programme_Specialization: "programme_Programme" = None, programme_Specialization9: "programme_Specialization" = None, programme_Specialization7: set["programme_Specialization"] = None, programme_Specialization11: set["programme_StudyYear"] = None):
        self.name = name
        self.programme_Specialization = programme_Specialization
        self.programme_Specialization9 = programme_Specialization9
        self.programme_Specialization7 = programme_Specialization7 if programme_Specialization7 is not None else set()
        self.programme_Specialization11 = programme_Specialization11 if programme_Specialization11 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def programme_Specialization(self):
        return self.__programme_Specialization

    @programme_Specialization.setter
    def programme_Specialization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_programme_Specialization__programme_Specialization", None)
        self.__programme_Specialization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "programme_Programme4"):
                opp_val = getattr(old_value, "programme_Programme4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "programme_Programme4"):
                opp_val = getattr(value, "programme_Programme4", None)
                if opp_val is None:
                    setattr(value, "programme_Programme4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def programme_Specialization9(self):
        return self.__programme_Specialization9

    @programme_Specialization9.setter
    def programme_Specialization9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_programme_Specialization__programme_Specialization9", None)
        self.__programme_Specialization9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "programme_Specialization7"):
                opp_val = getattr(old_value, "programme_Specialization7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "programme_Specialization7"):
                opp_val = getattr(value, "programme_Specialization7", None)
                if opp_val is None:
                    setattr(value, "programme_Specialization7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def programme_Specialization7(self):
        return self.__programme_Specialization7

    @programme_Specialization7.setter
    def programme_Specialization7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_programme_Specialization__programme_Specialization7", None)
        self.__programme_Specialization7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "programme_Specialization9"):
                    opp_val = getattr(item, "programme_Specialization9", None)
                    
                    if opp_val == self:
                        setattr(item, "programme_Specialization9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "programme_Specialization9"):
                    opp_val = getattr(item, "programme_Specialization9", None)
                    
                    setattr(item, "programme_Specialization9", self)
                    

    @property
    def programme_Specialization11(self):
        return self.__programme_Specialization11

    @programme_Specialization11.setter
    def programme_Specialization11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_programme_Specialization__programme_Specialization11", None)
        self.__programme_Specialization11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "programme_StudyYear12"):
                    opp_val = getattr(item, "programme_StudyYear12", None)
                    
                    if opp_val == self:
                        setattr(item, "programme_StudyYear12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "programme_StudyYear12"):
                    opp_val = getattr(item, "programme_StudyYear12", None)
                    
                    setattr(item, "programme_StudyYear12", self)
                    

class programme_Course:

    def __init__(self, code: str, taugtIn: str, level: str, credits: float, name: str, programme_Course: "programme_Department" = None, programme_Course19: "programme_SemesterCourse" = None):
        self.code = code
        self.taugtIn = taugtIn
        self.level = level
        self.credits = credits
        self.name = name
        self.programme_Course = programme_Course
        self.programme_Course19 = programme_Course19
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def credits(self) -> float:
        return self.__credits

    @credits.setter
    def credits(self, credits: float):
        self.__credits = credits

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def level(self) -> str:
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level

    @property
    def taugtIn(self) -> str:
        return self.__taugtIn

    @taugtIn.setter
    def taugtIn(self, taugtIn: str):
        self.__taugtIn = taugtIn

    @property
    def programme_Course19(self):
        return self.__programme_Course19

    @programme_Course19.setter
    def programme_Course19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_programme_Course__programme_Course19", None)
        self.__programme_Course19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "programme_SemesterCourse18"):
                opp_val = getattr(old_value, "programme_SemesterCourse18", None)
                if opp_val == self:
                    setattr(old_value, "programme_SemesterCourse18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "programme_SemesterCourse18"):
                opp_val = getattr(value, "programme_SemesterCourse18", None)
                setattr(value, "programme_SemesterCourse18", self)

    @property
    def programme_Course(self):
        return self.__programme_Course

    @programme_Course.setter
    def programme_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_programme_Course__programme_Course", None)
        self.__programme_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "programme_Department2"):
                opp_val = getattr(old_value, "programme_Department2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "programme_Department2"):
                opp_val = getattr(value, "programme_Department2", None)
                if opp_val is None:
                    setattr(value, "programme_Department2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
