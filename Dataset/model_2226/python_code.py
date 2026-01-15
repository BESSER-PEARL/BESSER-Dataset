from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class SemesterType(Enum):
    Fall = "Fall"
    Spring = "Spring"
class Access(Enum):
    M1A = "M1A"
    M2A = "M2A"
    NoAccess = "NoAccess"
    O = "O"
    VA = "VA"
    VB = "VB"
class Level(Enum):
    Bachelor = "Bachelor"
    Master = "Master"
class AvailableSemesters(Enum):
    Fall = "Fall"
    Spring = "Spring"
    Both = "Both"


############################################
# Definition of Classes
############################################

class studyprograms_Department:

    def __init__(self, code: str, name: str, studyprograms_Department: set["studyprograms_Programme"] = None, studyprograms_Department16: set["studyprograms_Course"] = None):
        self.code = code
        self.name = name
        self.studyprograms_Department = studyprograms_Department if studyprograms_Department is not None else set()
        self.studyprograms_Department16 = studyprograms_Department16 if studyprograms_Department16 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def studyprograms_Department16(self):
        return self.__studyprograms_Department16

    @studyprograms_Department16.setter
    def studyprograms_Department16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprograms_Department__studyprograms_Department16", None)
        self.__studyprograms_Department16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "studyprograms_Course17"):
                    opp_val = getattr(item, "studyprograms_Course17", None)
                    
                    if opp_val == self:
                        setattr(item, "studyprograms_Course17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "studyprograms_Course17"):
                    opp_val = getattr(item, "studyprograms_Course17", None)
                    
                    setattr(item, "studyprograms_Course17", self)
                    

    @property
    def studyprograms_Department(self):
        return self.__studyprograms_Department

    @studyprograms_Department.setter
    def studyprograms_Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprograms_Department__studyprograms_Department", None)
        self.__studyprograms_Department = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "studyprograms_Programme14"):
                    opp_val = getattr(item, "studyprograms_Programme14", None)
                    
                    if opp_val == self:
                        setattr(item, "studyprograms_Programme14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "studyprograms_Programme14"):
                    opp_val = getattr(item, "studyprograms_Programme14", None)
                    
                    setattr(item, "studyprograms_Programme14", self)
                    

class studyprograms_CourseAccess:

    def __init__(self, Access: str, studyprograms_CourseAccess12: set["studyprograms_Course"] = None, studyprograms_CourseAccess: "studyprograms_Semester" = None):
        self.Access = Access
        self.studyprograms_CourseAccess12 = studyprograms_CourseAccess12 if studyprograms_CourseAccess12 is not None else set()
        self.studyprograms_CourseAccess = studyprograms_CourseAccess
        
    @property
    def Access(self) -> str:
        return self.__Access

    @Access.setter
    def Access(self, Access: str):
        self.__Access = Access

    @property
    def studyprograms_CourseAccess(self):
        return self.__studyprograms_CourseAccess

    @studyprograms_CourseAccess.setter
    def studyprograms_CourseAccess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprograms_CourseAccess__studyprograms_CourseAccess", None)
        self.__studyprograms_CourseAccess = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyprograms_Semester10"):
                opp_val = getattr(old_value, "studyprograms_Semester10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyprograms_Semester10"):
                opp_val = getattr(value, "studyprograms_Semester10", None)
                if opp_val is None:
                    setattr(value, "studyprograms_Semester10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def studyprograms_CourseAccess12(self):
        return self.__studyprograms_CourseAccess12

    @studyprograms_CourseAccess12.setter
    def studyprograms_CourseAccess12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprograms_CourseAccess__studyprograms_CourseAccess12", None)
        self.__studyprograms_CourseAccess12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "studyprograms_Course"):
                    opp_val = getattr(item, "studyprograms_Course", None)
                    
                    if opp_val == self:
                        setattr(item, "studyprograms_Course", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "studyprograms_Course"):
                    opp_val = getattr(item, "studyprograms_Course", None)
                    
                    setattr(item, "studyprograms_Course", self)
                    

class studyprograms_Programme:

    def __init__(self, name: str, code: str, startYear: int, duration: int, studyprograms_Programme: set["studyprograms_Specialisation"] = None, studyprograms_Programme2: set["studyprograms_Semester"] = None, studyprograms_Programme14: "studyprograms_Department" = None):
        self.name = name
        self.code = code
        self.startYear = startYear
        self.duration = duration
        self.studyprograms_Programme = studyprograms_Programme if studyprograms_Programme is not None else set()
        self.studyprograms_Programme2 = studyprograms_Programme2 if studyprograms_Programme2 is not None else set()
        self.studyprograms_Programme14 = studyprograms_Programme14
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def duration(self) -> int:
        return self.__duration

    @duration.setter
    def duration(self, duration: int):
        self.__duration = duration

    @property
    def startYear(self) -> int:
        return self.__startYear

    @startYear.setter
    def startYear(self, startYear: int):
        self.__startYear = startYear

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def studyprograms_Programme14(self):
        return self.__studyprograms_Programme14

    @studyprograms_Programme14.setter
    def studyprograms_Programme14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprograms_Programme__studyprograms_Programme14", None)
        self.__studyprograms_Programme14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyprograms_Department"):
                opp_val = getattr(old_value, "studyprograms_Department", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyprograms_Department"):
                opp_val = getattr(value, "studyprograms_Department", None)
                if opp_val is None:
                    setattr(value, "studyprograms_Department", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def studyprograms_Programme(self):
        return self.__studyprograms_Programme

    @studyprograms_Programme.setter
    def studyprograms_Programme(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprograms_Programme__studyprograms_Programme", None)
        self.__studyprograms_Programme = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "studyprograms_Specialisation"):
                    opp_val = getattr(item, "studyprograms_Specialisation", None)
                    
                    if opp_val == self:
                        setattr(item, "studyprograms_Specialisation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "studyprograms_Specialisation"):
                    opp_val = getattr(item, "studyprograms_Specialisation", None)
                    
                    setattr(item, "studyprograms_Specialisation", self)
                    

    @property
    def studyprograms_Programme2(self):
        return self.__studyprograms_Programme2

    @studyprograms_Programme2.setter
    def studyprograms_Programme2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprograms_Programme__studyprograms_Programme2", None)
        self.__studyprograms_Programme2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "studyprograms_Semester"):
                    opp_val = getattr(item, "studyprograms_Semester", None)
                    
                    if opp_val == self:
                        setattr(item, "studyprograms_Semester", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "studyprograms_Semester"):
                    opp_val = getattr(item, "studyprograms_Semester", None)
                    
                    setattr(item, "studyprograms_Semester", self)
                    

class studyprograms_Course:

    def __init__(self, code: str, name: str, ects: float, level: str, availableSemester: str, studyprograms_Course: "studyprograms_CourseAccess" = None, studyprograms_Course17: "studyprograms_Department" = None):
        self.code = code
        self.name = name
        self.ects = ects
        self.level = level
        self.availableSemester = availableSemester
        self.studyprograms_Course = studyprograms_Course
        self.studyprograms_Course17 = studyprograms_Course17
        
    @property
    def availableSemester(self) -> str:
        return self.__availableSemester

    @availableSemester.setter
    def availableSemester(self, availableSemester: str):
        self.__availableSemester = availableSemester

    @property
    def ects(self) -> float:
        return self.__ects

    @ects.setter
    def ects(self, ects: float):
        self.__ects = ects

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def level(self) -> str:
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level

    @property
    def studyprograms_Course17(self):
        return self.__studyprograms_Course17

    @studyprograms_Course17.setter
    def studyprograms_Course17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprograms_Course__studyprograms_Course17", None)
        self.__studyprograms_Course17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyprograms_Department16"):
                opp_val = getattr(old_value, "studyprograms_Department16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyprograms_Department16"):
                opp_val = getattr(value, "studyprograms_Department16", None)
                if opp_val is None:
                    setattr(value, "studyprograms_Department16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def studyprograms_Course(self):
        return self.__studyprograms_Course

    @studyprograms_Course.setter
    def studyprograms_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprograms_Course__studyprograms_Course", None)
        self.__studyprograms_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyprograms_CourseAccess12"):
                opp_val = getattr(old_value, "studyprograms_CourseAccess12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyprograms_CourseAccess12"):
                opp_val = getattr(value, "studyprograms_CourseAccess12", None)
                if opp_val is None:
                    setattr(value, "studyprograms_CourseAccess12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class studyprograms_Semester:

    def __init__(self, semesterType: str, semesterCode: str, year: int, studyprograms_Semester: "studyprograms_Programme" = None, studyprograms_Semester5: "studyprograms_Specialisation" = None, studyprograms_Semester10: set["studyprograms_CourseAccess"] = None):
        self.semesterType = semesterType
        self.semesterCode = semesterCode
        self.year = year
        self.studyprograms_Semester = studyprograms_Semester
        self.studyprograms_Semester5 = studyprograms_Semester5
        self.studyprograms_Semester10 = studyprograms_Semester10 if studyprograms_Semester10 is not None else set()
        
    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def semesterType(self) -> str:
        return self.__semesterType

    @semesterType.setter
    def semesterType(self, semesterType: str):
        self.__semesterType = semesterType

    @property
    def semesterCode(self) -> str:
        return self.__semesterCode

    @semesterCode.setter
    def semesterCode(self, semesterCode: str):
        self.__semesterCode = semesterCode

    @property
    def studyprograms_Semester10(self):
        return self.__studyprograms_Semester10

    @studyprograms_Semester10.setter
    def studyprograms_Semester10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprograms_Semester__studyprograms_Semester10", None)
        self.__studyprograms_Semester10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "studyprograms_CourseAccess"):
                    opp_val = getattr(item, "studyprograms_CourseAccess", None)
                    
                    if opp_val == self:
                        setattr(item, "studyprograms_CourseAccess", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "studyprograms_CourseAccess"):
                    opp_val = getattr(item, "studyprograms_CourseAccess", None)
                    
                    setattr(item, "studyprograms_CourseAccess", self)
                    

    @property
    def studyprograms_Semester(self):
        return self.__studyprograms_Semester

    @studyprograms_Semester.setter
    def studyprograms_Semester(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprograms_Semester__studyprograms_Semester", None)
        self.__studyprograms_Semester = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyprograms_Programme2"):
                opp_val = getattr(old_value, "studyprograms_Programme2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyprograms_Programme2"):
                opp_val = getattr(value, "studyprograms_Programme2", None)
                if opp_val is None:
                    setattr(value, "studyprograms_Programme2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def studyprograms_Semester5(self):
        return self.__studyprograms_Semester5

    @studyprograms_Semester5.setter
    def studyprograms_Semester5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprograms_Semester__studyprograms_Semester5", None)
        self.__studyprograms_Semester5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyprograms_Specialisation4"):
                opp_val = getattr(old_value, "studyprograms_Specialisation4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyprograms_Specialisation4"):
                opp_val = getattr(value, "studyprograms_Specialisation4", None)
                if opp_val is None:
                    setattr(value, "studyprograms_Specialisation4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class studyprograms_Specialisation:

    def __init__(self, name: str, startSemester: int, studyprograms_Specialisation: "studyprograms_Programme" = None, studyprograms_Specialisation4: set["studyprograms_Semester"] = None, studyprograms_Specialisation8: "studyprograms_Specialisation" = None, studyprograms_Specialisation6: set["studyprograms_Specialisation"] = None):
        self.name = name
        self.startSemester = startSemester
        self.studyprograms_Specialisation = studyprograms_Specialisation
        self.studyprograms_Specialisation4 = studyprograms_Specialisation4 if studyprograms_Specialisation4 is not None else set()
        self.studyprograms_Specialisation8 = studyprograms_Specialisation8
        self.studyprograms_Specialisation6 = studyprograms_Specialisation6 if studyprograms_Specialisation6 is not None else set()
        
    @property
    def startSemester(self) -> int:
        return self.__startSemester

    @startSemester.setter
    def startSemester(self, startSemester: int):
        self.__startSemester = startSemester

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def studyprograms_Specialisation4(self):
        return self.__studyprograms_Specialisation4

    @studyprograms_Specialisation4.setter
    def studyprograms_Specialisation4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprograms_Specialisation__studyprograms_Specialisation4", None)
        self.__studyprograms_Specialisation4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "studyprograms_Semester5"):
                    opp_val = getattr(item, "studyprograms_Semester5", None)
                    
                    if opp_val == self:
                        setattr(item, "studyprograms_Semester5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "studyprograms_Semester5"):
                    opp_val = getattr(item, "studyprograms_Semester5", None)
                    
                    setattr(item, "studyprograms_Semester5", self)
                    

    @property
    def studyprograms_Specialisation6(self):
        return self.__studyprograms_Specialisation6

    @studyprograms_Specialisation6.setter
    def studyprograms_Specialisation6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprograms_Specialisation__studyprograms_Specialisation6", None)
        self.__studyprograms_Specialisation6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "studyprograms_Specialisation8"):
                    opp_val = getattr(item, "studyprograms_Specialisation8", None)
                    
                    if opp_val == self:
                        setattr(item, "studyprograms_Specialisation8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "studyprograms_Specialisation8"):
                    opp_val = getattr(item, "studyprograms_Specialisation8", None)
                    
                    setattr(item, "studyprograms_Specialisation8", self)
                    

    @property
    def studyprograms_Specialisation8(self):
        return self.__studyprograms_Specialisation8

    @studyprograms_Specialisation8.setter
    def studyprograms_Specialisation8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprograms_Specialisation__studyprograms_Specialisation8", None)
        self.__studyprograms_Specialisation8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyprograms_Specialisation6"):
                opp_val = getattr(old_value, "studyprograms_Specialisation6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyprograms_Specialisation6"):
                opp_val = getattr(value, "studyprograms_Specialisation6", None)
                if opp_val is None:
                    setattr(value, "studyprograms_Specialisation6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def studyprograms_Specialisation(self):
        return self.__studyprograms_Specialisation

    @studyprograms_Specialisation.setter
    def studyprograms_Specialisation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprograms_Specialisation__studyprograms_Specialisation", None)
        self.__studyprograms_Specialisation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyprograms_Programme"):
                opp_val = getattr(old_value, "studyprograms_Programme", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyprograms_Programme"):
                opp_val = getattr(value, "studyprograms_Programme", None)
                if opp_val is None:
                    setattr(value, "studyprograms_Programme", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
