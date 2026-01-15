from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class SemesterSeason(Enum):
    Spring = "Spring"
    Fall = "Fall"
class Access(Enum):
    O = "O"
    M2A = "M2A"
    M1A = "M1A"
    VA = "VA"
    NA = "NA"


############################################
# Definition of Classes
############################################

class StudyProgrammes_Specialization:

    def __init__(self, name: str, startSemester: int, lengthInSemesters: int, StudyProgrammes_Specialization8: set["StudyProgrammes_Semester"] = None, StudyProgrammes_Specialization: "StudyProgrammes_Programme" = None):
        self.name = name
        self.startSemester = startSemester
        self.lengthInSemesters = lengthInSemesters
        self.StudyProgrammes_Specialization8 = StudyProgrammes_Specialization8 if StudyProgrammes_Specialization8 is not None else set()
        self.StudyProgrammes_Specialization = StudyProgrammes_Specialization
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def lengthInSemesters(self) -> int:
        return self.__lengthInSemesters

    @lengthInSemesters.setter
    def lengthInSemesters(self, lengthInSemesters: int):
        self.__lengthInSemesters = lengthInSemesters

    @property
    def startSemester(self) -> int:
        return self.__startSemester

    @startSemester.setter
    def startSemester(self, startSemester: int):
        self.__startSemester = startSemester

    @property
    def StudyProgrammes_Specialization8(self):
        return self.__StudyProgrammes_Specialization8

    @StudyProgrammes_Specialization8.setter
    def StudyProgrammes_Specialization8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StudyProgrammes_Specialization__StudyProgrammes_Specialization8", None)
        self.__StudyProgrammes_Specialization8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StudyProgrammes_Semester9"):
                    opp_val = getattr(item, "StudyProgrammes_Semester9", None)
                    
                    if opp_val == self:
                        setattr(item, "StudyProgrammes_Semester9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StudyProgrammes_Semester9"):
                    opp_val = getattr(item, "StudyProgrammes_Semester9", None)
                    
                    setattr(item, "StudyProgrammes_Semester9", self)
                    

    @property
    def StudyProgrammes_Specialization(self):
        return self.__StudyProgrammes_Specialization

    @StudyProgrammes_Specialization.setter
    def StudyProgrammes_Specialization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StudyProgrammes_Specialization__StudyProgrammes_Specialization", None)
        self.__StudyProgrammes_Specialization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StudyProgrammes_Programme4"):
                opp_val = getattr(old_value, "StudyProgrammes_Programme4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StudyProgrammes_Programme4"):
                opp_val = getattr(value, "StudyProgrammes_Programme4", None)
                if opp_val is None:
                    setattr(value, "StudyProgrammes_Programme4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class StudyProgrammes_Course:

    def __init__(self, name: str, code: str, credits: float, availableSemesters: str, StudyProgrammes_Course: "StudyProgrammes_Department" = None, StudyProgrammes_Course14: "StudyProgrammes_CourseAccess" = None):
        self.name = name
        self.code = code
        self.credits = credits
        self.availableSemesters = availableSemesters
        self.StudyProgrammes_Course = StudyProgrammes_Course
        self.StudyProgrammes_Course14 = StudyProgrammes_Course14
        
    @property
    def credits(self) -> float:
        return self.__credits

    @credits.setter
    def credits(self, credits: float):
        self.__credits = credits

    @property
    def availableSemesters(self) -> str:
        return self.__availableSemesters

    @availableSemesters.setter
    def availableSemesters(self, availableSemesters: str):
        self.__availableSemesters = availableSemesters

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
    def StudyProgrammes_Course14(self):
        return self.__StudyProgrammes_Course14

    @StudyProgrammes_Course14.setter
    def StudyProgrammes_Course14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StudyProgrammes_Course__StudyProgrammes_Course14", None)
        self.__StudyProgrammes_Course14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StudyProgrammes_CourseAccess13"):
                opp_val = getattr(old_value, "StudyProgrammes_CourseAccess13", None)
                if opp_val == self:
                    setattr(old_value, "StudyProgrammes_CourseAccess13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StudyProgrammes_CourseAccess13"):
                opp_val = getattr(value, "StudyProgrammes_CourseAccess13", None)
                setattr(value, "StudyProgrammes_CourseAccess13", self)

    @property
    def StudyProgrammes_Course(self):
        return self.__StudyProgrammes_Course

    @StudyProgrammes_Course.setter
    def StudyProgrammes_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StudyProgrammes_Course__StudyProgrammes_Course", None)
        self.__StudyProgrammes_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StudyProgrammes_Department2"):
                opp_val = getattr(old_value, "StudyProgrammes_Department2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StudyProgrammes_Department2"):
                opp_val = getattr(value, "StudyProgrammes_Department2", None)
                if opp_val is None:
                    setattr(value, "StudyProgrammes_Department2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class StudyProgrammes_Programme:

    def __init__(self, name: str, code: str, startYear: int, totalNumberOfSemesters: int, semestersBeforeSpecialization: int, StudyProgrammes_Programme6: set["StudyProgrammes_Semester"] = None, StudyProgrammes_Programme: "StudyProgrammes_Department" = None, StudyProgrammes_Programme4: set["StudyProgrammes_Specialization"] = None):
        self.name = name
        self.code = code
        self.startYear = startYear
        self.totalNumberOfSemesters = totalNumberOfSemesters
        self.semestersBeforeSpecialization = semestersBeforeSpecialization
        self.StudyProgrammes_Programme6 = StudyProgrammes_Programme6 if StudyProgrammes_Programme6 is not None else set()
        self.StudyProgrammes_Programme = StudyProgrammes_Programme
        self.StudyProgrammes_Programme4 = StudyProgrammes_Programme4 if StudyProgrammes_Programme4 is not None else set()
        
    @property
    def semestersBeforeSpecialization(self) -> int:
        return self.__semestersBeforeSpecialization

    @semestersBeforeSpecialization.setter
    def semestersBeforeSpecialization(self, semestersBeforeSpecialization: int):
        self.__semestersBeforeSpecialization = semestersBeforeSpecialization

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def startYear(self) -> int:
        return self.__startYear

    @startYear.setter
    def startYear(self, startYear: int):
        self.__startYear = startYear

    @property
    def totalNumberOfSemesters(self) -> int:
        return self.__totalNumberOfSemesters

    @totalNumberOfSemesters.setter
    def totalNumberOfSemesters(self, totalNumberOfSemesters: int):
        self.__totalNumberOfSemesters = totalNumberOfSemesters

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def StudyProgrammes_Programme4(self):
        return self.__StudyProgrammes_Programme4

    @StudyProgrammes_Programme4.setter
    def StudyProgrammes_Programme4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StudyProgrammes_Programme__StudyProgrammes_Programme4", None)
        self.__StudyProgrammes_Programme4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StudyProgrammes_Specialization"):
                    opp_val = getattr(item, "StudyProgrammes_Specialization", None)
                    
                    if opp_val == self:
                        setattr(item, "StudyProgrammes_Specialization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StudyProgrammes_Specialization"):
                    opp_val = getattr(item, "StudyProgrammes_Specialization", None)
                    
                    setattr(item, "StudyProgrammes_Specialization", self)
                    

    @property
    def StudyProgrammes_Programme6(self):
        return self.__StudyProgrammes_Programme6

    @StudyProgrammes_Programme6.setter
    def StudyProgrammes_Programme6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StudyProgrammes_Programme__StudyProgrammes_Programme6", None)
        self.__StudyProgrammes_Programme6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StudyProgrammes_Semester"):
                    opp_val = getattr(item, "StudyProgrammes_Semester", None)
                    
                    if opp_val == self:
                        setattr(item, "StudyProgrammes_Semester", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StudyProgrammes_Semester"):
                    opp_val = getattr(item, "StudyProgrammes_Semester", None)
                    
                    setattr(item, "StudyProgrammes_Semester", self)
                    

    @property
    def StudyProgrammes_Programme(self):
        return self.__StudyProgrammes_Programme

    @StudyProgrammes_Programme.setter
    def StudyProgrammes_Programme(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StudyProgrammes_Programme__StudyProgrammes_Programme", None)
        self.__StudyProgrammes_Programme = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StudyProgrammes_Department"):
                opp_val = getattr(old_value, "StudyProgrammes_Department", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StudyProgrammes_Department"):
                opp_val = getattr(value, "StudyProgrammes_Department", None)
                if opp_val is None:
                    setattr(value, "StudyProgrammes_Department", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class StudyProgrammes_CourseAccess:

    def __init__(self, access: str, StudyProgrammes_CourseAccess: "StudyProgrammes_Semester" = None, StudyProgrammes_CourseAccess13: "StudyProgrammes_Course" = None):
        self.access = access
        self.StudyProgrammes_CourseAccess = StudyProgrammes_CourseAccess
        self.StudyProgrammes_CourseAccess13 = StudyProgrammes_CourseAccess13
        
    @property
    def access(self) -> str:
        return self.__access

    @access.setter
    def access(self, access: str):
        self.__access = access

    @property
    def StudyProgrammes_CourseAccess13(self):
        return self.__StudyProgrammes_CourseAccess13

    @StudyProgrammes_CourseAccess13.setter
    def StudyProgrammes_CourseAccess13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StudyProgrammes_CourseAccess__StudyProgrammes_CourseAccess13", None)
        self.__StudyProgrammes_CourseAccess13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StudyProgrammes_Course14"):
                opp_val = getattr(old_value, "StudyProgrammes_Course14", None)
                if opp_val == self:
                    setattr(old_value, "StudyProgrammes_Course14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StudyProgrammes_Course14"):
                opp_val = getattr(value, "StudyProgrammes_Course14", None)
                setattr(value, "StudyProgrammes_Course14", self)

    @property
    def StudyProgrammes_CourseAccess(self):
        return self.__StudyProgrammes_CourseAccess

    @StudyProgrammes_CourseAccess.setter
    def StudyProgrammes_CourseAccess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StudyProgrammes_CourseAccess__StudyProgrammes_CourseAccess", None)
        self.__StudyProgrammes_CourseAccess = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StudyProgrammes_Semester11"):
                opp_val = getattr(old_value, "StudyProgrammes_Semester11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StudyProgrammes_Semester11"):
                opp_val = getattr(value, "StudyProgrammes_Semester11", None)
                if opp_val is None:
                    setattr(value, "StudyProgrammes_Semester11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class StudyProgrammes_Semester:

    def __init__(self, code: str, year: int, semesterSeason: str, StudyProgrammes_Semester: "StudyProgrammes_Programme" = None, StudyProgrammes_Semester9: "StudyProgrammes_Specialization" = None, StudyProgrammes_Semester11: set["StudyProgrammes_CourseAccess"] = None):
        self.code = code
        self.year = year
        self.semesterSeason = semesterSeason
        self.StudyProgrammes_Semester = StudyProgrammes_Semester
        self.StudyProgrammes_Semester9 = StudyProgrammes_Semester9
        self.StudyProgrammes_Semester11 = StudyProgrammes_Semester11 if StudyProgrammes_Semester11 is not None else set()
        
    @property
    def semesterSeason(self) -> str:
        return self.__semesterSeason

    @semesterSeason.setter
    def semesterSeason(self, semesterSeason: str):
        self.__semesterSeason = semesterSeason

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def StudyProgrammes_Semester(self):
        return self.__StudyProgrammes_Semester

    @StudyProgrammes_Semester.setter
    def StudyProgrammes_Semester(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StudyProgrammes_Semester__StudyProgrammes_Semester", None)
        self.__StudyProgrammes_Semester = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StudyProgrammes_Programme6"):
                opp_val = getattr(old_value, "StudyProgrammes_Programme6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StudyProgrammes_Programme6"):
                opp_val = getattr(value, "StudyProgrammes_Programme6", None)
                if opp_val is None:
                    setattr(value, "StudyProgrammes_Programme6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def StudyProgrammes_Semester11(self):
        return self.__StudyProgrammes_Semester11

    @StudyProgrammes_Semester11.setter
    def StudyProgrammes_Semester11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StudyProgrammes_Semester__StudyProgrammes_Semester11", None)
        self.__StudyProgrammes_Semester11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StudyProgrammes_CourseAccess"):
                    opp_val = getattr(item, "StudyProgrammes_CourseAccess", None)
                    
                    if opp_val == self:
                        setattr(item, "StudyProgrammes_CourseAccess", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StudyProgrammes_CourseAccess"):
                    opp_val = getattr(item, "StudyProgrammes_CourseAccess", None)
                    
                    setattr(item, "StudyProgrammes_CourseAccess", self)
                    

    @property
    def StudyProgrammes_Semester9(self):
        return self.__StudyProgrammes_Semester9

    @StudyProgrammes_Semester9.setter
    def StudyProgrammes_Semester9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StudyProgrammes_Semester__StudyProgrammes_Semester9", None)
        self.__StudyProgrammes_Semester9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StudyProgrammes_Specialization8"):
                opp_val = getattr(old_value, "StudyProgrammes_Specialization8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StudyProgrammes_Specialization8"):
                opp_val = getattr(value, "StudyProgrammes_Specialization8", None)
                if opp_val is None:
                    setattr(value, "StudyProgrammes_Specialization8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class StudyProgrammes_Department:

    def __init__(self, name: str, StudyProgrammes_Department: set["StudyProgrammes_Programme"] = None, StudyProgrammes_Department2: set["StudyProgrammes_Course"] = None):
        self.name = name
        self.StudyProgrammes_Department = StudyProgrammes_Department if StudyProgrammes_Department is not None else set()
        self.StudyProgrammes_Department2 = StudyProgrammes_Department2 if StudyProgrammes_Department2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def StudyProgrammes_Department(self):
        return self.__StudyProgrammes_Department

    @StudyProgrammes_Department.setter
    def StudyProgrammes_Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StudyProgrammes_Department__StudyProgrammes_Department", None)
        self.__StudyProgrammes_Department = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StudyProgrammes_Programme"):
                    opp_val = getattr(item, "StudyProgrammes_Programme", None)
                    
                    if opp_val == self:
                        setattr(item, "StudyProgrammes_Programme", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StudyProgrammes_Programme"):
                    opp_val = getattr(item, "StudyProgrammes_Programme", None)
                    
                    setattr(item, "StudyProgrammes_Programme", self)
                    

    @property
    def StudyProgrammes_Department2(self):
        return self.__StudyProgrammes_Department2

    @StudyProgrammes_Department2.setter
    def StudyProgrammes_Department2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StudyProgrammes_Department__StudyProgrammes_Department2", None)
        self.__StudyProgrammes_Department2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StudyProgrammes_Course"):
                    opp_val = getattr(item, "StudyProgrammes_Course", None)
                    
                    if opp_val == self:
                        setattr(item, "StudyProgrammes_Course", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StudyProgrammes_Course"):
                    opp_val = getattr(item, "StudyProgrammes_Course", None)
                    
                    setattr(item, "StudyProgrammes_Course", self)
                    
