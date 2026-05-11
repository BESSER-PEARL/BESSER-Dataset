from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Level(Enum):
    Bachelor = "Bachelor"
    Master = "Master"
class SemesterType(Enum):
    Fall = "Fall"
    Spring = "Spring"
class AvailableSemesters(Enum):
    Fall = "Fall"
    Spring = "Spring"
    Both = "Both"
class Access(Enum):
    O = "O"
    VA = "VA"
    VB = "VB"
    M1A = "M1A"
    M2A = "M2A"
    NoAccess = "NoAccess"


############################################
# Definition of Classes
############################################

class studyprograms_Department:

    def __init__(self, code: str, name: str, studyprograms_Department: set["studyprograms_Programme"] = None, studyprograms_Department15: set["studyprograms_Course"] = None):
        self.code = code
        self.name = name
        self.studyprograms_Department = studyprograms_Department if studyprograms_Department is not None else set()
        self.studyprograms_Department15 = studyprograms_Department15 if studyprograms_Department15 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code


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
                if hasattr(item, "studyprograms_Programme13"):
                    opp_val = getattr(item, "studyprograms_Programme13", None)
                    
                    if opp_val == self:
                        setattr(item, "studyprograms_Programme13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "studyprograms_Programme13"):
                    opp_val = getattr(item, "studyprograms_Programme13", None)
                    
                    setattr(item, "studyprograms_Programme13", self)
                    

    @property
    def studyprograms_Department15(self):
        return self.__studyprograms_Department15

    @studyprograms_Department15.setter
    def studyprograms_Department15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprograms_Department__studyprograms_Department15", None)
        self.__studyprograms_Department15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "studyprograms_Course16"):
                    opp_val = getattr(item, "studyprograms_Course16", None)
                    
                    if opp_val == self:
                        setattr(item, "studyprograms_Course16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "studyprograms_Course16"):
                    opp_val = getattr(item, "studyprograms_Course16", None)
                    
                    setattr(item, "studyprograms_Course16", self)
                    

class studyprograms_CourseAccess:

    def __init__(self, Access: str, studyprograms_CourseAccess: "studyprograms_Semester" = None, studyprograms_CourseAccess11: set["studyprograms_Course"] = None):
        self.Access = Access
        self.studyprograms_CourseAccess = studyprograms_CourseAccess
        self.studyprograms_CourseAccess11 = studyprograms_CourseAccess11 if studyprograms_CourseAccess11 is not None else set()
        
        pass
    @property
    def Access(self):
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
            if hasattr(old_value, "studyprograms_Semester9"):
                opp_val = getattr(old_value, "studyprograms_Semester9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyprograms_Semester9"):
                opp_val = getattr(value, "studyprograms_Semester9", None)
                if opp_val is None:
                    setattr(value, "studyprograms_Semester9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def studyprograms_CourseAccess11(self):
        return self.__studyprograms_CourseAccess11

    @studyprograms_CourseAccess11.setter
    def studyprograms_CourseAccess11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprograms_CourseAccess__studyprograms_CourseAccess11", None)
        self.__studyprograms_CourseAccess11 = value if value is not None else set()
        
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
                    

class studyprograms_IndividualStudyPlan:

    def __init__(self, studentNo: str, studyprograms_IndividualStudyPlan: set["studyprograms_Semester"] = None):
        self.studentNo = studentNo
        self.studyprograms_IndividualStudyPlan = studyprograms_IndividualStudyPlan if studyprograms_IndividualStudyPlan is not None else set()
        
        pass
    @property
    def studentNo(self):
        return self.__studentNo

    @studentNo.setter
    def studentNo(self, studentNo: str):
        self.__studentNo = studentNo


    @property
    def studyprograms_IndividualStudyPlan(self):
        return self.__studyprograms_IndividualStudyPlan

    @studyprograms_IndividualStudyPlan.setter
    def studyprograms_IndividualStudyPlan(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprograms_IndividualStudyPlan__studyprograms_IndividualStudyPlan", None)
        self.__studyprograms_IndividualStudyPlan = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "studyprograms_Semester7"):
                    opp_val = getattr(item, "studyprograms_Semester7", None)
                    
                    if opp_val == self:
                        setattr(item, "studyprograms_Semester7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "studyprograms_Semester7"):
                    opp_val = getattr(item, "studyprograms_Semester7", None)
                    
                    setattr(item, "studyprograms_Semester7", self)
                    

class studyprograms_Semester:

    def __init__(self, semesterCode: str, year: int, semesterType: str, studyprograms_Semester: "studyprograms_Programme" = None, studyprograms_Semester5: "studyprograms_Specialisation" = None, studyprograms_Semester7: "studyprograms_IndividualStudyPlan" = None, studyprograms_Semester9: set["studyprograms_CourseAccess"] = None):
        self.semesterCode = semesterCode
        self.year = year
        self.semesterType = semesterType
        self.studyprograms_Semester = studyprograms_Semester
        self.studyprograms_Semester5 = studyprograms_Semester5
        self.studyprograms_Semester7 = studyprograms_Semester7
        self.studyprograms_Semester9 = studyprograms_Semester9 if studyprograms_Semester9 is not None else set()
        
        pass
    @property
    def semesterType(self):
        return self.__semesterType

    @semesterType.setter
    def semesterType(self, semesterType: str):
        self.__semesterType = semesterType


    @property
    def semesterCode(self):
        return self.__semesterCode

    @semesterCode.setter
    def semesterCode(self, semesterCode: str):
        self.__semesterCode = semesterCode


    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year


    @property
    def studyprograms_Semester7(self):
        return self.__studyprograms_Semester7

    @studyprograms_Semester7.setter
    def studyprograms_Semester7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprograms_Semester__studyprograms_Semester7", None)
        self.__studyprograms_Semester7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyprograms_IndividualStudyPlan"):
                opp_val = getattr(old_value, "studyprograms_IndividualStudyPlan", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyprograms_IndividualStudyPlan"):
                opp_val = getattr(value, "studyprograms_IndividualStudyPlan", None)
                if opp_val is None:
                    setattr(value, "studyprograms_IndividualStudyPlan", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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

    @property
    def studyprograms_Semester9(self):
        return self.__studyprograms_Semester9

    @studyprograms_Semester9.setter
    def studyprograms_Semester9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprograms_Semester__studyprograms_Semester9", None)
        self.__studyprograms_Semester9 = value if value is not None else set()
        
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
                    

class studyprograms_Specialisation:

    def __init__(self, name: str, startSemester: int, studyprograms_Specialisation: "studyprograms_Programme" = None, studyprograms_Specialisation4: set["studyprograms_Semester"] = None):
        self.name = name
        self.startSemester = startSemester
        self.studyprograms_Specialisation = studyprograms_Specialisation
        self.studyprograms_Specialisation4 = studyprograms_Specialisation4 if studyprograms_Specialisation4 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def startSemester(self):
        return self.__startSemester

    @startSemester.setter
    def startSemester(self, startSemester: int):
        self.__startSemester = startSemester


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
                    

class studyprograms_Programme:

    def __init__(self, name: str, code: str, startYear: int, duration: int, studyprograms_Programme2: set["studyprograms_Semester"] = None, studyprograms_Programme: set["studyprograms_Specialisation"] = None, studyprograms_Programme13: "studyprograms_Department" = None):
        self.name = name
        self.code = code
        self.startYear = startYear
        self.duration = duration
        self.studyprograms_Programme2 = studyprograms_Programme2 if studyprograms_Programme2 is not None else set()
        self.studyprograms_Programme = studyprograms_Programme if studyprograms_Programme is not None else set()
        self.studyprograms_Programme13 = studyprograms_Programme13
        
        pass
    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def startYear(self):
        return self.__startYear

    @startYear.setter
    def startYear(self, startYear: int):
        self.__startYear = startYear


    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration: int):
        self.__duration = duration


    @property
    def studyprograms_Programme13(self):
        return self.__studyprograms_Programme13

    @studyprograms_Programme13.setter
    def studyprograms_Programme13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprograms_Programme__studyprograms_Programme13", None)
        self.__studyprograms_Programme13 = value
        
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

    def __init__(self, code: str, name: str, ects: float, level: str, availableSemester: str, studyprograms_Course: "studyprograms_CourseAccess" = None, studyprograms_Course16: "studyprograms_Department" = None):
        self.code = code
        self.name = name
        self.ects = ects
        self.level = level
        self.availableSemester = availableSemester
        self.studyprograms_Course = studyprograms_Course
        self.studyprograms_Course16 = studyprograms_Course16
        
        pass
    @property
    def ects(self):
        return self.__ects

    @ects.setter
    def ects(self, ects: float):
        self.__ects = ects


    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code


    @property
    def availableSemester(self):
        return self.__availableSemester

    @availableSemester.setter
    def availableSemester(self, availableSemester: str):
        self.__availableSemester = availableSemester


    @property
    def studyprograms_Course16(self):
        return self.__studyprograms_Course16

    @studyprograms_Course16.setter
    def studyprograms_Course16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprograms_Course__studyprograms_Course16", None)
        self.__studyprograms_Course16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyprograms_Department15"):
                opp_val = getattr(old_value, "studyprograms_Department15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyprograms_Department15"):
                opp_val = getattr(value, "studyprograms_Department15", None)
                if opp_val is None:
                    setattr(value, "studyprograms_Department15", set([self]))
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
            if hasattr(old_value, "studyprograms_CourseAccess11"):
                opp_val = getattr(old_value, "studyprograms_CourseAccess11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyprograms_CourseAccess11"):
                opp_val = getattr(value, "studyprograms_CourseAccess11", None)
                if opp_val is None:
                    setattr(value, "studyprograms_CourseAccess11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
