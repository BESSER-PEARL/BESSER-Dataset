from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class SemesterCode(Enum):
    Spring = "Spring"
    Autumn = "Autumn"


############################################
# Definition of Classes
############################################

class studies_StudyCourse:

    def __init__(self, mandatory: bool, studies_StudyCourse: "studies_CourseInstance" = None):
        self.mandatory = mandatory
        self.studies_StudyCourse = studies_StudyCourse
        
    @property
    def mandatory(self) -> bool:
        return self.__mandatory

    @mandatory.setter
    def mandatory(self, mandatory: bool):
        self.__mandatory = mandatory

    @property
    def studies_StudyCourse(self):
        return self.__studies_StudyCourse

    @studies_StudyCourse.setter
    def studies_StudyCourse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studies_StudyCourse__studies_StudyCourse", None)
        self.__studies_StudyCourse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studies_CourseInstance"):
                opp_val = getattr(old_value, "studies_CourseInstance", None)
                if opp_val == self:
                    setattr(old_value, "studies_CourseInstance", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studies_CourseInstance"):
                opp_val = getattr(value, "studies_CourseInstance", None)
                setattr(value, "studies_CourseInstance", self)

class studies_Semester:

    def __init__(self, studyYearSemester: str, studies_Semester: "studies_StudyYear" = None, studies_Semester15: "studies_StudyYear" = None, studies_Semester18: set["studies_CourseInstance"] = None):
        self.studyYearSemester = studyYearSemester
        self.studies_Semester = studies_Semester
        self.studies_Semester15 = studies_Semester15
        self.studies_Semester18 = studies_Semester18 if studies_Semester18 is not None else set()
        
    @property
    def studyYearSemester(self) -> str:
        return self.__studyYearSemester

    @studyYearSemester.setter
    def studyYearSemester(self, studyYearSemester: str):
        self.__studyYearSemester = studyYearSemester

    @property
    def studies_Semester18(self):
        return self.__studies_Semester18

    @studies_Semester18.setter
    def studies_Semester18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studies_Semester__studies_Semester18", None)
        self.__studies_Semester18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "studies_CourseInstance19"):
                    opp_val = getattr(item, "studies_CourseInstance19", None)
                    
                    if opp_val == self:
                        setattr(item, "studies_CourseInstance19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "studies_CourseInstance19"):
                    opp_val = getattr(item, "studies_CourseInstance19", None)
                    
                    setattr(item, "studies_CourseInstance19", self)
                    

    @property
    def studies_Semester(self):
        return self.__studies_Semester

    @studies_Semester.setter
    def studies_Semester(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studies_Semester__studies_Semester", None)
        self.__studies_Semester = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studies_StudyYear12"):
                opp_val = getattr(old_value, "studies_StudyYear12", None)
                if opp_val == self:
                    setattr(old_value, "studies_StudyYear12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studies_StudyYear12"):
                opp_val = getattr(value, "studies_StudyYear12", None)
                setattr(value, "studies_StudyYear12", self)

    @property
    def studies_Semester15(self):
        return self.__studies_Semester15

    @studies_Semester15.setter
    def studies_Semester15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studies_Semester__studies_Semester15", None)
        self.__studies_Semester15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studies_StudyYear14"):
                opp_val = getattr(old_value, "studies_StudyYear14", None)
                if opp_val == self:
                    setattr(old_value, "studies_StudyYear14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studies_StudyYear14"):
                opp_val = getattr(value, "studies_StudyYear14", None)
                setattr(value, "studies_StudyYear14", self)

class studies_StudyYear:

    def __init__(self, programName: str, studies_StudyYear: "studies_StudyInstance" = None, studies_StudyYear12: "studies_Semester" = None, studies_StudyYear10: "studies_StudyYear" = None, studies_StudyYear8: set["studies_StudyYear"] = None, studies_StudyYear14: "studies_Semester" = None):
        self.programName = programName
        self.studies_StudyYear = studies_StudyYear
        self.studies_StudyYear12 = studies_StudyYear12
        self.studies_StudyYear10 = studies_StudyYear10
        self.studies_StudyYear8 = studies_StudyYear8 if studies_StudyYear8 is not None else set()
        self.studies_StudyYear14 = studies_StudyYear14
        
    @property
    def programName(self) -> str:
        return self.__programName

    @programName.setter
    def programName(self, programName: str):
        self.__programName = programName

    @property
    def studies_StudyYear14(self):
        return self.__studies_StudyYear14

    @studies_StudyYear14.setter
    def studies_StudyYear14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studies_StudyYear__studies_StudyYear14", None)
        self.__studies_StudyYear14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studies_Semester15"):
                opp_val = getattr(old_value, "studies_Semester15", None)
                if opp_val == self:
                    setattr(old_value, "studies_Semester15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studies_Semester15"):
                opp_val = getattr(value, "studies_Semester15", None)
                setattr(value, "studies_Semester15", self)

    @property
    def studies_StudyYear(self):
        return self.__studies_StudyYear

    @studies_StudyYear.setter
    def studies_StudyYear(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studies_StudyYear__studies_StudyYear", None)
        self.__studies_StudyYear = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studies_StudyInstance"):
                opp_val = getattr(old_value, "studies_StudyInstance", None)
                if opp_val == self:
                    setattr(old_value, "studies_StudyInstance", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studies_StudyInstance"):
                opp_val = getattr(value, "studies_StudyInstance", None)
                setattr(value, "studies_StudyInstance", self)

    @property
    def studies_StudyYear8(self):
        return self.__studies_StudyYear8

    @studies_StudyYear8.setter
    def studies_StudyYear8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studies_StudyYear__studies_StudyYear8", None)
        self.__studies_StudyYear8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "studies_StudyYear10"):
                    opp_val = getattr(item, "studies_StudyYear10", None)
                    
                    if opp_val == self:
                        setattr(item, "studies_StudyYear10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "studies_StudyYear10"):
                    opp_val = getattr(item, "studies_StudyYear10", None)
                    
                    setattr(item, "studies_StudyYear10", self)
                    

    @property
    def studies_StudyYear12(self):
        return self.__studies_StudyYear12

    @studies_StudyYear12.setter
    def studies_StudyYear12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studies_StudyYear__studies_StudyYear12", None)
        self.__studies_StudyYear12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studies_Semester"):
                opp_val = getattr(old_value, "studies_Semester", None)
                if opp_val == self:
                    setattr(old_value, "studies_Semester", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studies_Semester"):
                opp_val = getattr(value, "studies_Semester", None)
                setattr(value, "studies_Semester", self)

    @property
    def studies_StudyYear10(self):
        return self.__studies_StudyYear10

    @studies_StudyYear10.setter
    def studies_StudyYear10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studies_StudyYear__studies_StudyYear10", None)
        self.__studies_StudyYear10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studies_StudyYear8"):
                opp_val = getattr(old_value, "studies_StudyYear8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studies_StudyYear8"):
                opp_val = getattr(value, "studies_StudyYear8", None)
                if opp_val is None:
                    setattr(value, "studies_StudyYear8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class studies_CourseInstance:

    def __init__(self, year: int, semester: str, instanceName: str, CourseInstance: "studies_Course" = None, courseInstances: "studies_Course" = None, studies_CourseInstance: "studies_StudyCourse" = None, studies_CourseInstance19: "studies_Semester" = None):
        self.year = year
        self.semester = semester
        self.instanceName = instanceName
        self.CourseInstance = CourseInstance
        self.courseInstances = courseInstances
        self.studies_CourseInstance = studies_CourseInstance
        self.studies_CourseInstance19 = studies_CourseInstance19
        
    @property
    def instanceName(self) -> str:
        return self.__instanceName

    @instanceName.setter
    def instanceName(self, instanceName: str):
        self.__instanceName = instanceName

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def semester(self) -> str:
        return self.__semester

    @semester.setter
    def semester(self, semester: str):
        self.__semester = semester

    @property
    def studies_CourseInstance(self):
        return self.__studies_CourseInstance

    @studies_CourseInstance.setter
    def studies_CourseInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studies_CourseInstance__studies_CourseInstance", None)
        self.__studies_CourseInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studies_StudyCourse"):
                opp_val = getattr(old_value, "studies_StudyCourse", None)
                if opp_val == self:
                    setattr(old_value, "studies_StudyCourse", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studies_StudyCourse"):
                opp_val = getattr(value, "studies_StudyCourse", None)
                setattr(value, "studies_StudyCourse", self)

    @property
    def studies_CourseInstance19(self):
        return self.__studies_CourseInstance19

    @studies_CourseInstance19.setter
    def studies_CourseInstance19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studies_CourseInstance__studies_CourseInstance19", None)
        self.__studies_CourseInstance19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studies_Semester18"):
                opp_val = getattr(old_value, "studies_Semester18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studies_Semester18"):
                opp_val = getattr(value, "studies_Semester18", None)
                if opp_val is None:
                    setattr(value, "studies_Semester18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def courseInstances(self):
        return self.__courseInstances

    @courseInstances.setter
    def courseInstances(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studies_CourseInstance__courseInstances", None)
        self.__courseInstances = value
        
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
    def CourseInstance(self):
        return self.__CourseInstance

    @CourseInstance.setter
    def CourseInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studies_CourseInstance__CourseInstance", None)
        self.__CourseInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course"):
                opp_val = getattr(old_value, "course", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course"):
                opp_val = getattr(value, "course", None)
                if opp_val is None:
                    setattr(value, "course", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class studies_Study:

    def __init__(self, name: str, code: str, study: set["studies_StudyInstance"] = None, studies_Study: "studies_University" = None, Study: "studies_StudyInstance" = None):
        self.name = name
        self.code = code
        self.study = study if study is not None else set()
        self.studies_Study = studies_Study
        self.Study = Study
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def studies_Study(self):
        return self.__studies_Study

    @studies_Study.setter
    def studies_Study(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studies_Study__studies_Study", None)
        self.__studies_Study = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studies_University2"):
                opp_val = getattr(old_value, "studies_University2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studies_University2"):
                opp_val = getattr(value, "studies_University2", None)
                if opp_val is None:
                    setattr(value, "studies_University2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Study(self):
        return self.__Study

    @Study.setter
    def Study(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studies_Study__Study", None)
        self.__Study = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyInstances"):
                opp_val = getattr(old_value, "studyInstances", None)
                if opp_val == self:
                    setattr(old_value, "studyInstances", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyInstances"):
                opp_val = getattr(value, "studyInstances", None)
                setattr(value, "studyInstances", self)

    @property
    def study(self):
        return self.__study

    @study.setter
    def study(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studies_Study__study", None)
        self.__study = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StudyInstance"):
                    opp_val = getattr(item, "StudyInstance", None)
                    
                    if opp_val == self:
                        setattr(item, "StudyInstance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StudyInstance"):
                    opp_val = getattr(item, "StudyInstance", None)
                    
                    setattr(item, "StudyInstance", self)
                    

class studies_StudyInstance:

    def __init__(self, year: int, StudyInstance: "studies_Study" = None, studyInstances: "studies_Study" = None, studies_StudyInstance: "studies_StudyYear" = None):
        self.year = year
        self.StudyInstance = StudyInstance
        self.studyInstances = studyInstances
        self.studies_StudyInstance = studies_StudyInstance
        
    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def StudyInstance(self):
        return self.__StudyInstance

    @StudyInstance.setter
    def StudyInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studies_StudyInstance__StudyInstance", None)
        self.__StudyInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "study"):
                opp_val = getattr(old_value, "study", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "study"):
                opp_val = getattr(value, "study", None)
                if opp_val is None:
                    setattr(value, "study", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def studies_StudyInstance(self):
        return self.__studies_StudyInstance

    @studies_StudyInstance.setter
    def studies_StudyInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studies_StudyInstance__studies_StudyInstance", None)
        self.__studies_StudyInstance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studies_StudyYear"):
                opp_val = getattr(old_value, "studies_StudyYear", None)
                if opp_val == self:
                    setattr(old_value, "studies_StudyYear", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studies_StudyYear"):
                opp_val = getattr(value, "studies_StudyYear", None)
                setattr(value, "studies_StudyYear", self)

    @property
    def studyInstances(self):
        return self.__studyInstances

    @studyInstances.setter
    def studyInstances(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studies_StudyInstance__studyInstances", None)
        self.__studyInstances = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Study"):
                opp_val = getattr(old_value, "Study", None)
                if opp_val == self:
                    setattr(old_value, "Study", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Study"):
                opp_val = getattr(value, "Study", None)
                setattr(value, "Study", self)

class studies_Course:

    def __init__(self, name: str, code: str, studyPoints: float, studies_Course: "studies_University" = None, course: set["studies_CourseInstance"] = None, Course: "studies_CourseInstance" = None):
        self.name = name
        self.code = code
        self.studyPoints = studyPoints
        self.studies_Course = studies_Course
        self.course = course if course is not None else set()
        self.Course = Course
        
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
    def studyPoints(self) -> float:
        return self.__studyPoints

    @studyPoints.setter
    def studyPoints(self, studyPoints: float):
        self.__studyPoints = studyPoints

    @property
    def Course(self):
        return self.__Course

    @Course.setter
    def Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studies_Course__Course", None)
        self.__Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courseInstances"):
                opp_val = getattr(old_value, "courseInstances", None)
                if opp_val == self:
                    setattr(old_value, "courseInstances", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courseInstances"):
                opp_val = getattr(value, "courseInstances", None)
                setattr(value, "courseInstances", self)

    @property
    def studies_Course(self):
        return self.__studies_Course

    @studies_Course.setter
    def studies_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studies_Course__studies_Course", None)
        self.__studies_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studies_University"):
                opp_val = getattr(old_value, "studies_University", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studies_University"):
                opp_val = getattr(value, "studies_University", None)
                if opp_val is None:
                    setattr(value, "studies_University", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studies_Course__course", None)
        self.__course = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CourseInstance"):
                    opp_val = getattr(item, "CourseInstance", None)
                    
                    if opp_val == self:
                        setattr(item, "CourseInstance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CourseInstance"):
                    opp_val = getattr(item, "CourseInstance", None)
                    
                    setattr(item, "CourseInstance", self)
                    

class studies_University:

    def __init__(self, name: str, studies_University: set["studies_Course"] = None, studies_University2: set["studies_Study"] = None):
        self.name = name
        self.studies_University = studies_University if studies_University is not None else set()
        self.studies_University2 = studies_University2 if studies_University2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def studies_University(self):
        return self.__studies_University

    @studies_University.setter
    def studies_University(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studies_University__studies_University", None)
        self.__studies_University = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "studies_Course"):
                    opp_val = getattr(item, "studies_Course", None)
                    
                    if opp_val == self:
                        setattr(item, "studies_Course", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "studies_Course"):
                    opp_val = getattr(item, "studies_Course", None)
                    
                    setattr(item, "studies_Course", self)
                    

    @property
    def studies_University2(self):
        return self.__studies_University2

    @studies_University2.setter
    def studies_University2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studies_University__studies_University2", None)
        self.__studies_University2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "studies_Study"):
                    opp_val = getattr(item, "studies_Study", None)
                    
                    if opp_val == self:
                        setattr(item, "studies_Study", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "studies_Study"):
                    opp_val = getattr(item, "studies_Study", None)
                    
                    setattr(item, "studies_Study", self)
                    
