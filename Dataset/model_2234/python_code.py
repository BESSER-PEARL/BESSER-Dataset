from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class SemesterType(Enum):
    SPRING = "SPRING"
    FALL = "FALL"
class CourseStatus(Enum):
    MANDATORY = "MANDATORY"
    ELECTIVE = "ELECTIVE"


############################################
# Definition of Classes
############################################

class studyplan_CourseGroup:

    def __init__(self, group: str, courseStatus: str, studyplan_CourseGroup: "studyplan_Specialization" = None, CourseGroup: "studyplan_Course" = None, courseGroup: "studyplan_Course" = None, studyplan_CourseGroup23: "studyplan_Semester" = None):
        self.group = group
        self.courseStatus = courseStatus
        self.studyplan_CourseGroup = studyplan_CourseGroup
        self.CourseGroup = CourseGroup
        self.courseGroup = courseGroup
        self.studyplan_CourseGroup23 = studyplan_CourseGroup23
        
    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def courseStatus(self) -> str:
        return self.__courseStatus

    @courseStatus.setter
    def courseStatus(self, courseStatus: str):
        self.__courseStatus = courseStatus

    @property
    def courseGroup(self):
        return self.__courseGroup

    @courseGroup.setter
    def courseGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyplan_CourseGroup__courseGroup", None)
        self.__courseGroup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Course"):
                opp_val = getattr(old_value, "Course", None)
                if opp_val == self:
                    setattr(old_value, "Course", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Course"):
                opp_val = getattr(value, "Course", None)
                setattr(value, "Course", self)

    @property
    def studyplan_CourseGroup23(self):
        return self.__studyplan_CourseGroup23

    @studyplan_CourseGroup23.setter
    def studyplan_CourseGroup23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyplan_CourseGroup__studyplan_CourseGroup23", None)
        self.__studyplan_CourseGroup23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyplan_Semester24"):
                opp_val = getattr(old_value, "studyplan_Semester24", None)
                if opp_val == self:
                    setattr(old_value, "studyplan_Semester24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyplan_Semester24"):
                opp_val = getattr(value, "studyplan_Semester24", None)
                setattr(value, "studyplan_Semester24", self)

    @property
    def studyplan_CourseGroup(self):
        return self.__studyplan_CourseGroup

    @studyplan_CourseGroup.setter
    def studyplan_CourseGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyplan_CourseGroup__studyplan_CourseGroup", None)
        self.__studyplan_CourseGroup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyplan_Specialization15"):
                opp_val = getattr(old_value, "studyplan_Specialization15", None)
                if opp_val == self:
                    setattr(old_value, "studyplan_Specialization15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyplan_Specialization15"):
                opp_val = getattr(value, "studyplan_Specialization15", None)
                setattr(value, "studyplan_Specialization15", self)

    @property
    def CourseGroup(self):
        return self.__CourseGroup

    @CourseGroup.setter
    def CourseGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyplan_CourseGroup__CourseGroup", None)
        self.__CourseGroup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course"):
                opp_val = getattr(old_value, "course", None)
                if opp_val == self:
                    setattr(old_value, "course", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course"):
                opp_val = getattr(value, "course", None)
                setattr(value, "course", self)

class studyplan_Specialization:

    def __init__(self, specName: str, studyplan_Specialization: set["studyplan_Semester"] = None, studyplan_Specialization13: "studyplan_Specialization" = None, studyplan_Specialization11: set["studyplan_Specialization"] = None, studyplan_Specialization15: "studyplan_CourseGroup" = None, studyplan_Specialization18: "studyplan_FieldOfStudy" = None):
        self.specName = specName
        self.studyplan_Specialization = studyplan_Specialization if studyplan_Specialization is not None else set()
        self.studyplan_Specialization13 = studyplan_Specialization13
        self.studyplan_Specialization11 = studyplan_Specialization11 if studyplan_Specialization11 is not None else set()
        self.studyplan_Specialization15 = studyplan_Specialization15
        self.studyplan_Specialization18 = studyplan_Specialization18
        
    @property
    def specName(self) -> str:
        return self.__specName

    @specName.setter
    def specName(self, specName: str):
        self.__specName = specName

    @property
    def studyplan_Specialization18(self):
        return self.__studyplan_Specialization18

    @studyplan_Specialization18.setter
    def studyplan_Specialization18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyplan_Specialization__studyplan_Specialization18", None)
        self.__studyplan_Specialization18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyplan_FieldOfStudy17"):
                opp_val = getattr(old_value, "studyplan_FieldOfStudy17", None)
                if opp_val == self:
                    setattr(old_value, "studyplan_FieldOfStudy17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyplan_FieldOfStudy17"):
                opp_val = getattr(value, "studyplan_FieldOfStudy17", None)
                setattr(value, "studyplan_FieldOfStudy17", self)

    @property
    def studyplan_Specialization11(self):
        return self.__studyplan_Specialization11

    @studyplan_Specialization11.setter
    def studyplan_Specialization11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyplan_Specialization__studyplan_Specialization11", None)
        self.__studyplan_Specialization11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "studyplan_Specialization13"):
                    opp_val = getattr(item, "studyplan_Specialization13", None)
                    
                    if opp_val == self:
                        setattr(item, "studyplan_Specialization13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "studyplan_Specialization13"):
                    opp_val = getattr(item, "studyplan_Specialization13", None)
                    
                    setattr(item, "studyplan_Specialization13", self)
                    

    @property
    def studyplan_Specialization15(self):
        return self.__studyplan_Specialization15

    @studyplan_Specialization15.setter
    def studyplan_Specialization15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyplan_Specialization__studyplan_Specialization15", None)
        self.__studyplan_Specialization15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyplan_CourseGroup"):
                opp_val = getattr(old_value, "studyplan_CourseGroup", None)
                if opp_val == self:
                    setattr(old_value, "studyplan_CourseGroup", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyplan_CourseGroup"):
                opp_val = getattr(value, "studyplan_CourseGroup", None)
                setattr(value, "studyplan_CourseGroup", self)

    @property
    def studyplan_Specialization13(self):
        return self.__studyplan_Specialization13

    @studyplan_Specialization13.setter
    def studyplan_Specialization13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyplan_Specialization__studyplan_Specialization13", None)
        self.__studyplan_Specialization13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyplan_Specialization11"):
                opp_val = getattr(old_value, "studyplan_Specialization11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyplan_Specialization11"):
                opp_val = getattr(value, "studyplan_Specialization11", None)
                if opp_val is None:
                    setattr(value, "studyplan_Specialization11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def studyplan_Specialization(self):
        return self.__studyplan_Specialization

    @studyplan_Specialization.setter
    def studyplan_Specialization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyplan_Specialization__studyplan_Specialization", None)
        self.__studyplan_Specialization = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "studyplan_Semester10"):
                    opp_val = getattr(item, "studyplan_Semester10", None)
                    
                    if opp_val == self:
                        setattr(item, "studyplan_Semester10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "studyplan_Semester10"):
                    opp_val = getattr(item, "studyplan_Semester10", None)
                    
                    setattr(item, "studyplan_Semester10", self)
                    

class studyplan_StudyPlan:

    def __init__(self, planName: str, studyplan_StudyPlan: "studyplan_FieldOfStudy" = None, studyplan_StudyPlan2: "studyplan_Course" = None, studyplan_StudyPlan4: "studyplan_Semester" = None):
        self.planName = planName
        self.studyplan_StudyPlan = studyplan_StudyPlan
        self.studyplan_StudyPlan2 = studyplan_StudyPlan2
        self.studyplan_StudyPlan4 = studyplan_StudyPlan4
        
    @property
    def planName(self) -> str:
        return self.__planName

    @planName.setter
    def planName(self, planName: str):
        self.__planName = planName

    @property
    def studyplan_StudyPlan(self):
        return self.__studyplan_StudyPlan

    @studyplan_StudyPlan.setter
    def studyplan_StudyPlan(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyplan_StudyPlan__studyplan_StudyPlan", None)
        self.__studyplan_StudyPlan = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyplan_FieldOfStudy"):
                opp_val = getattr(old_value, "studyplan_FieldOfStudy", None)
                if opp_val == self:
                    setattr(old_value, "studyplan_FieldOfStudy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyplan_FieldOfStudy"):
                opp_val = getattr(value, "studyplan_FieldOfStudy", None)
                setattr(value, "studyplan_FieldOfStudy", self)

    @property
    def studyplan_StudyPlan4(self):
        return self.__studyplan_StudyPlan4

    @studyplan_StudyPlan4.setter
    def studyplan_StudyPlan4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyplan_StudyPlan__studyplan_StudyPlan4", None)
        self.__studyplan_StudyPlan4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyplan_Semester"):
                opp_val = getattr(old_value, "studyplan_Semester", None)
                if opp_val == self:
                    setattr(old_value, "studyplan_Semester", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyplan_Semester"):
                opp_val = getattr(value, "studyplan_Semester", None)
                setattr(value, "studyplan_Semester", self)

    @property
    def studyplan_StudyPlan2(self):
        return self.__studyplan_StudyPlan2

    @studyplan_StudyPlan2.setter
    def studyplan_StudyPlan2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyplan_StudyPlan__studyplan_StudyPlan2", None)
        self.__studyplan_StudyPlan2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyplan_Course"):
                opp_val = getattr(old_value, "studyplan_Course", None)
                if opp_val == self:
                    setattr(old_value, "studyplan_Course", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyplan_Course"):
                opp_val = getattr(value, "studyplan_Course", None)
                setattr(value, "studyplan_Course", self)

class studyplan_Semester:

    def __init__(self, year: int, semesterType: str, studyplan_Semester: "studyplan_StudyPlan" = None, studyplan_Semester6: set["studyplan_Course"] = None, studyplan_Semester10: "studyplan_Specialization" = None, studyplan_Semester21: "studyplan_FieldOfStudy" = None, studyplan_Semester24: "studyplan_CourseGroup" = None):
        self.year = year
        self.semesterType = semesterType
        self.studyplan_Semester = studyplan_Semester
        self.studyplan_Semester6 = studyplan_Semester6 if studyplan_Semester6 is not None else set()
        self.studyplan_Semester10 = studyplan_Semester10
        self.studyplan_Semester21 = studyplan_Semester21
        self.studyplan_Semester24 = studyplan_Semester24
        
    @property
    def semesterType(self) -> str:
        return self.__semesterType

    @semesterType.setter
    def semesterType(self, semesterType: str):
        self.__semesterType = semesterType

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def studyplan_Semester21(self):
        return self.__studyplan_Semester21

    @studyplan_Semester21.setter
    def studyplan_Semester21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyplan_Semester__studyplan_Semester21", None)
        self.__studyplan_Semester21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyplan_FieldOfStudy20"):
                opp_val = getattr(old_value, "studyplan_FieldOfStudy20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyplan_FieldOfStudy20"):
                opp_val = getattr(value, "studyplan_FieldOfStudy20", None)
                if opp_val is None:
                    setattr(value, "studyplan_FieldOfStudy20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def studyplan_Semester6(self):
        return self.__studyplan_Semester6

    @studyplan_Semester6.setter
    def studyplan_Semester6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyplan_Semester__studyplan_Semester6", None)
        self.__studyplan_Semester6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "studyplan_Course7"):
                    opp_val = getattr(item, "studyplan_Course7", None)
                    
                    if opp_val == self:
                        setattr(item, "studyplan_Course7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "studyplan_Course7"):
                    opp_val = getattr(item, "studyplan_Course7", None)
                    
                    setattr(item, "studyplan_Course7", self)
                    

    @property
    def studyplan_Semester10(self):
        return self.__studyplan_Semester10

    @studyplan_Semester10.setter
    def studyplan_Semester10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyplan_Semester__studyplan_Semester10", None)
        self.__studyplan_Semester10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyplan_Specialization"):
                opp_val = getattr(old_value, "studyplan_Specialization", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyplan_Specialization"):
                opp_val = getattr(value, "studyplan_Specialization", None)
                if opp_val is None:
                    setattr(value, "studyplan_Specialization", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def studyplan_Semester(self):
        return self.__studyplan_Semester

    @studyplan_Semester.setter
    def studyplan_Semester(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyplan_Semester__studyplan_Semester", None)
        self.__studyplan_Semester = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyplan_StudyPlan4"):
                opp_val = getattr(old_value, "studyplan_StudyPlan4", None)
                if opp_val == self:
                    setattr(old_value, "studyplan_StudyPlan4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyplan_StudyPlan4"):
                opp_val = getattr(value, "studyplan_StudyPlan4", None)
                setattr(value, "studyplan_StudyPlan4", self)

    @property
    def studyplan_Semester24(self):
        return self.__studyplan_Semester24

    @studyplan_Semester24.setter
    def studyplan_Semester24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyplan_Semester__studyplan_Semester24", None)
        self.__studyplan_Semester24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyplan_CourseGroup23"):
                opp_val = getattr(old_value, "studyplan_CourseGroup23", None)
                if opp_val == self:
                    setattr(old_value, "studyplan_CourseGroup23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyplan_CourseGroup23"):
                opp_val = getattr(value, "studyplan_CourseGroup23", None)
                setattr(value, "studyplan_CourseGroup23", self)

class studyplan_Course:

    def __init__(self, courseName: str, courseCode: int, credit: float, status: str, studyplan_Course: "studyplan_StudyPlan" = None, studyplan_Course7: "studyplan_Semester" = None, course: "studyplan_CourseGroup" = None, Course: "studyplan_CourseGroup" = None):
        self.courseName = courseName
        self.courseCode = courseCode
        self.credit = credit
        self.status = status
        self.studyplan_Course = studyplan_Course
        self.studyplan_Course7 = studyplan_Course7
        self.course = course
        self.Course = Course
        
    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def courseCode(self) -> int:
        return self.__courseCode

    @courseCode.setter
    def courseCode(self, courseCode: int):
        self.__courseCode = courseCode

    @property
    def courseName(self) -> str:
        return self.__courseName

    @courseName.setter
    def courseName(self, courseName: str):
        self.__courseName = courseName

    @property
    def credit(self) -> float:
        return self.__credit

    @credit.setter
    def credit(self, credit: float):
        self.__credit = credit

    @property
    def studyplan_Course(self):
        return self.__studyplan_Course

    @studyplan_Course.setter
    def studyplan_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyplan_Course__studyplan_Course", None)
        self.__studyplan_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyplan_StudyPlan2"):
                opp_val = getattr(old_value, "studyplan_StudyPlan2", None)
                if opp_val == self:
                    setattr(old_value, "studyplan_StudyPlan2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyplan_StudyPlan2"):
                opp_val = getattr(value, "studyplan_StudyPlan2", None)
                setattr(value, "studyplan_StudyPlan2", self)

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyplan_Course__course", None)
        self.__course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CourseGroup"):
                opp_val = getattr(old_value, "CourseGroup", None)
                if opp_val == self:
                    setattr(old_value, "CourseGroup", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CourseGroup"):
                opp_val = getattr(value, "CourseGroup", None)
                setattr(value, "CourseGroup", self)

    @property
    def Course(self):
        return self.__Course

    @Course.setter
    def Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyplan_Course__Course", None)
        self.__Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courseGroup"):
                opp_val = getattr(old_value, "courseGroup", None)
                if opp_val == self:
                    setattr(old_value, "courseGroup", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courseGroup"):
                opp_val = getattr(value, "courseGroup", None)
                setattr(value, "courseGroup", self)

    @property
    def studyplan_Course7(self):
        return self.__studyplan_Course7

    @studyplan_Course7.setter
    def studyplan_Course7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyplan_Course__studyplan_Course7", None)
        self.__studyplan_Course7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyplan_Semester6"):
                opp_val = getattr(old_value, "studyplan_Semester6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyplan_Semester6"):
                opp_val = getattr(value, "studyplan_Semester6", None)
                if opp_val is None:
                    setattr(value, "studyplan_Semester6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class studyplan_FieldOfStudy:

    def __init__(self, fieldName: str, studyplan_FieldOfStudy: "studyplan_StudyPlan" = None, studyplan_FieldOfStudy17: "studyplan_Specialization" = None, studyplan_FieldOfStudy20: set["studyplan_Semester"] = None):
        self.fieldName = fieldName
        self.studyplan_FieldOfStudy = studyplan_FieldOfStudy
        self.studyplan_FieldOfStudy17 = studyplan_FieldOfStudy17
        self.studyplan_FieldOfStudy20 = studyplan_FieldOfStudy20 if studyplan_FieldOfStudy20 is not None else set()
        
    @property
    def fieldName(self) -> str:
        return self.__fieldName

    @fieldName.setter
    def fieldName(self, fieldName: str):
        self.__fieldName = fieldName

    @property
    def studyplan_FieldOfStudy17(self):
        return self.__studyplan_FieldOfStudy17

    @studyplan_FieldOfStudy17.setter
    def studyplan_FieldOfStudy17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyplan_FieldOfStudy__studyplan_FieldOfStudy17", None)
        self.__studyplan_FieldOfStudy17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyplan_Specialization18"):
                opp_val = getattr(old_value, "studyplan_Specialization18", None)
                if opp_val == self:
                    setattr(old_value, "studyplan_Specialization18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyplan_Specialization18"):
                opp_val = getattr(value, "studyplan_Specialization18", None)
                setattr(value, "studyplan_Specialization18", self)

    @property
    def studyplan_FieldOfStudy20(self):
        return self.__studyplan_FieldOfStudy20

    @studyplan_FieldOfStudy20.setter
    def studyplan_FieldOfStudy20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyplan_FieldOfStudy__studyplan_FieldOfStudy20", None)
        self.__studyplan_FieldOfStudy20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "studyplan_Semester21"):
                    opp_val = getattr(item, "studyplan_Semester21", None)
                    
                    if opp_val == self:
                        setattr(item, "studyplan_Semester21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "studyplan_Semester21"):
                    opp_val = getattr(item, "studyplan_Semester21", None)
                    
                    setattr(item, "studyplan_Semester21", self)
                    

    @property
    def studyplan_FieldOfStudy(self):
        return self.__studyplan_FieldOfStudy

    @studyplan_FieldOfStudy.setter
    def studyplan_FieldOfStudy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyplan_FieldOfStudy__studyplan_FieldOfStudy", None)
        self.__studyplan_FieldOfStudy = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyplan_StudyPlan"):
                opp_val = getattr(old_value, "studyplan_StudyPlan", None)
                if opp_val == self:
                    setattr(old_value, "studyplan_StudyPlan", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyplan_StudyPlan"):
                opp_val = getattr(value, "studyplan_StudyPlan", None)
                setattr(value, "studyplan_StudyPlan", self)
