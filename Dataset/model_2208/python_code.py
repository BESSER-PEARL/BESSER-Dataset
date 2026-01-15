from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class IsMandatory(Enum):
    MANDATORY = "MANDATORY"
    ELECTIVE = "ELECTIVE"
class Season(Enum):
    FALL = "FALL"
    SPRING = "SPRING"


############################################
# Definition of Classes
############################################

class study_Course:

    def __init__(self, credits: float, code: str, name: str, level: int, study_Course: "study_SemesterCourse" = None, courses17: "study_Department" = None, Course: "study_Department" = None):
        self.credits = credits
        self.code = code
        self.name = name
        self.level = level
        self.study_Course = study_Course
        self.courses17 = courses17
        self.Course = Course
        
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
    def level(self) -> int:
        return self.__level

    @level.setter
    def level(self, level: int):
        self.__level = level

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def study_Course(self):
        return self.__study_Course

    @study_Course.setter
    def study_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Course__study_Course", None)
        self.__study_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "study_SemesterCourse"):
                opp_val = getattr(old_value, "study_SemesterCourse", None)
                if opp_val == self:
                    setattr(old_value, "study_SemesterCourse", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "study_SemesterCourse"):
                opp_val = getattr(value, "study_SemesterCourse", None)
                setattr(value, "study_SemesterCourse", self)

    @property
    def Course(self):
        return self.__Course

    @Course.setter
    def Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Course__Course", None)
        self.__Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "department"):
                opp_val = getattr(old_value, "department", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "department"):
                opp_val = getattr(value, "department", None)
                if opp_val is None:
                    setattr(value, "department", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def courses17(self):
        return self.__courses17

    @courses17.setter
    def courses17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Course__courses17", None)
        self.__courses17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Department18"):
                opp_val = getattr(old_value, "Department18", None)
                if opp_val == self:
                    setattr(old_value, "Department18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Department18"):
                opp_val = getattr(value, "Department18", None)
                setattr(value, "Department18", self)

class study_Department:

    def __init__(self, name: str, Department: "study_Programme" = None, Department18: "study_Course" = None, department: set["study_Course"] = None, department21: set["study_Programme"] = None):
        self.name = name
        self.Department = Department
        self.Department18 = Department18
        self.department = department if department is not None else set()
        self.department21 = department21 if department21 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Department(self):
        return self.__Department

    @Department.setter
    def Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Department__Department", None)
        self.__Department = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "programs"):
                opp_val = getattr(old_value, "programs", None)
                if opp_val == self:
                    setattr(old_value, "programs", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "programs"):
                opp_val = getattr(value, "programs", None)
                setattr(value, "programs", self)

    @property
    def Department18(self):
        return self.__Department18

    @Department18.setter
    def Department18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Department__Department18", None)
        self.__Department18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courses17"):
                opp_val = getattr(old_value, "courses17", None)
                if opp_val == self:
                    setattr(old_value, "courses17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courses17"):
                opp_val = getattr(value, "courses17", None)
                setattr(value, "courses17", self)

    @property
    def department21(self):
        return self.__department21

    @department21.setter
    def department21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Department__department21", None)
        self.__department21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Programme22"):
                    opp_val = getattr(item, "Programme22", None)
                    
                    if opp_val == self:
                        setattr(item, "Programme22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Programme22"):
                    opp_val = getattr(item, "Programme22", None)
                    
                    setattr(item, "Programme22", self)
                    

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Department__department", None)
        self.__department = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Course"):
                    opp_val = getattr(item, "Course", None)
                    
                    if opp_val == self:
                        setattr(item, "Course", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Course"):
                    opp_val = getattr(item, "Course", None)
                    
                    setattr(item, "Course", self)
                    

class study_Specialization:

    def __init__(self, name: str, Specialization: "study_Programme" = None, Specialization8: "study_Semester" = None, specialization: set["study_Semester"] = None, specializations: "study_Programme" = None):
        self.name = name
        self.Specialization = Specialization
        self.Specialization8 = Specialization8
        self.specialization = specialization if specialization is not None else set()
        self.specializations = specializations
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def specializations(self):
        return self.__specializations

    @specializations.setter
    def specializations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Specialization__specializations", None)
        self.__specializations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Programme12"):
                opp_val = getattr(old_value, "Programme12", None)
                if opp_val == self:
                    setattr(old_value, "Programme12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Programme12"):
                opp_val = getattr(value, "Programme12", None)
                setattr(value, "Programme12", self)

    @property
    def Specialization8(self):
        return self.__Specialization8

    @Specialization8.setter
    def Specialization8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Specialization__Specialization8", None)
        self.__Specialization8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "semesters7"):
                opp_val = getattr(old_value, "semesters7", None)
                if opp_val == self:
                    setattr(old_value, "semesters7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "semesters7"):
                opp_val = getattr(value, "semesters7", None)
                setattr(value, "semesters7", self)

    @property
    def specialization(self):
        return self.__specialization

    @specialization.setter
    def specialization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Specialization__specialization", None)
        self.__specialization = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Semester10"):
                    opp_val = getattr(item, "Semester10", None)
                    
                    if opp_val == self:
                        setattr(item, "Semester10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Semester10"):
                    opp_val = getattr(item, "Semester10", None)
                    
                    setattr(item, "Semester10", self)
                    

    @property
    def Specialization(self):
        return self.__Specialization

    @Specialization.setter
    def Specialization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Specialization__Specialization", None)
        self.__Specialization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "programme2"):
                opp_val = getattr(old_value, "programme2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "programme2"):
                opp_val = getattr(value, "programme2", None)
                if opp_val is None:
                    setattr(value, "programme2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class study_Semester:

    def __init__(self, year: int, Season: str, semester: set["study_SemesterCourse"] = None, Semester: "study_Programme" = None, semesters: "study_Programme" = None, semesters7: "study_Specialization" = None, Semester10: "study_Specialization" = None, Semester15: "study_SemesterCourse" = None):
        self.year = year
        self.Season = Season
        self.semester = semester if semester is not None else set()
        self.Semester = Semester
        self.semesters = semesters
        self.semesters7 = semesters7
        self.Semester10 = Semester10
        self.Semester15 = Semester15
        
    @property
    def Season(self) -> str:
        return self.__Season

    @Season.setter
    def Season(self, Season: str):
        self.__Season = Season

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def semesters(self):
        return self.__semesters

    @semesters.setter
    def semesters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Semester__semesters", None)
        self.__semesters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Programme"):
                opp_val = getattr(old_value, "Programme", None)
                if opp_val == self:
                    setattr(old_value, "Programme", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Programme"):
                opp_val = getattr(value, "Programme", None)
                setattr(value, "Programme", self)

    @property
    def Semester(self):
        return self.__Semester

    @Semester.setter
    def Semester(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Semester__Semester", None)
        self.__Semester = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "programme"):
                opp_val = getattr(old_value, "programme", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "programme"):
                opp_val = getattr(value, "programme", None)
                if opp_val is None:
                    setattr(value, "programme", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Semester10(self):
        return self.__Semester10

    @Semester10.setter
    def Semester10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Semester__Semester10", None)
        self.__Semester10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "specialization"):
                opp_val = getattr(old_value, "specialization", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "specialization"):
                opp_val = getattr(value, "specialization", None)
                if opp_val is None:
                    setattr(value, "specialization", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def semesters7(self):
        return self.__semesters7

    @semesters7.setter
    def semesters7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Semester__semesters7", None)
        self.__semesters7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Specialization8"):
                opp_val = getattr(old_value, "Specialization8", None)
                if opp_val == self:
                    setattr(old_value, "Specialization8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Specialization8"):
                opp_val = getattr(value, "Specialization8", None)
                setattr(value, "Specialization8", self)

    @property
    def Semester15(self):
        return self.__Semester15

    @Semester15.setter
    def Semester15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Semester__Semester15", None)
        self.__Semester15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courses"):
                opp_val = getattr(old_value, "courses", None)
                if opp_val == self:
                    setattr(old_value, "courses", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courses"):
                opp_val = getattr(value, "courses", None)
                setattr(value, "courses", self)

    @property
    def semester(self):
        return self.__semester

    @semester.setter
    def semester(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Semester__semester", None)
        self.__semester = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SemesterCourse"):
                    opp_val = getattr(item, "SemesterCourse", None)
                    
                    if opp_val == self:
                        setattr(item, "SemesterCourse", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SemesterCourse"):
                    opp_val = getattr(item, "SemesterCourse", None)
                    
                    setattr(item, "SemesterCourse", self)
                    

class study_Programme:

    def __init__(self, name: str, code: str, duration: int, programme: set["study_Semester"] = None, programme2: set["study_Specialization"] = None, programs: "study_Department" = None, Programme: "study_Semester" = None, Programme12: "study_Specialization" = None, Programme22: "study_Department" = None):
        self.name = name
        self.code = code
        self.duration = duration
        self.programme = programme if programme is not None else set()
        self.programme2 = programme2 if programme2 is not None else set()
        self.programs = programs
        self.Programme = Programme
        self.Programme12 = Programme12
        self.Programme22 = Programme22
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def duration(self) -> int:
        return self.__duration

    @duration.setter
    def duration(self, duration: int):
        self.__duration = duration

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def programme(self):
        return self.__programme

    @programme.setter
    def programme(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Programme__programme", None)
        self.__programme = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Semester"):
                    opp_val = getattr(item, "Semester", None)
                    
                    if opp_val == self:
                        setattr(item, "Semester", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Semester"):
                    opp_val = getattr(item, "Semester", None)
                    
                    setattr(item, "Semester", self)
                    

    @property
    def Programme12(self):
        return self.__Programme12

    @Programme12.setter
    def Programme12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Programme__Programme12", None)
        self.__Programme12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "specializations"):
                opp_val = getattr(old_value, "specializations", None)
                if opp_val == self:
                    setattr(old_value, "specializations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "specializations"):
                opp_val = getattr(value, "specializations", None)
                setattr(value, "specializations", self)

    @property
    def programme2(self):
        return self.__programme2

    @programme2.setter
    def programme2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Programme__programme2", None)
        self.__programme2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Specialization"):
                    opp_val = getattr(item, "Specialization", None)
                    
                    if opp_val == self:
                        setattr(item, "Specialization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Specialization"):
                    opp_val = getattr(item, "Specialization", None)
                    
                    setattr(item, "Specialization", self)
                    

    @property
    def Programme(self):
        return self.__Programme

    @Programme.setter
    def Programme(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Programme__Programme", None)
        self.__Programme = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "semesters"):
                opp_val = getattr(old_value, "semesters", None)
                if opp_val == self:
                    setattr(old_value, "semesters", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "semesters"):
                opp_val = getattr(value, "semesters", None)
                setattr(value, "semesters", self)

    @property
    def programs(self):
        return self.__programs

    @programs.setter
    def programs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Programme__programs", None)
        self.__programs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Department"):
                opp_val = getattr(old_value, "Department", None)
                if opp_val == self:
                    setattr(old_value, "Department", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Department"):
                opp_val = getattr(value, "Department", None)
                setattr(value, "Department", self)

    @property
    def Programme22(self):
        return self.__Programme22

    @Programme22.setter
    def Programme22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Programme__Programme22", None)
        self.__Programme22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "department21"):
                opp_val = getattr(old_value, "department21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "department21"):
                opp_val = getattr(value, "department21", None)
                if opp_val is None:
                    setattr(value, "department21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class study_SemesterCourse:

    def __init__(self, mandatory: str, SemesterCourse: "study_Semester" = None, study_SemesterCourse: "study_Course" = None, courses: "study_Semester" = None):
        self.mandatory = mandatory
        self.SemesterCourse = SemesterCourse
        self.study_SemesterCourse = study_SemesterCourse
        self.courses = courses
        
    @property
    def mandatory(self) -> str:
        return self.__mandatory

    @mandatory.setter
    def mandatory(self, mandatory: str):
        self.__mandatory = mandatory

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_SemesterCourse__courses", None)
        self.__courses = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Semester15"):
                opp_val = getattr(old_value, "Semester15", None)
                if opp_val == self:
                    setattr(old_value, "Semester15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Semester15"):
                opp_val = getattr(value, "Semester15", None)
                setattr(value, "Semester15", self)

    @property
    def study_SemesterCourse(self):
        return self.__study_SemesterCourse

    @study_SemesterCourse.setter
    def study_SemesterCourse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_SemesterCourse__study_SemesterCourse", None)
        self.__study_SemesterCourse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "study_Course"):
                opp_val = getattr(old_value, "study_Course", None)
                if opp_val == self:
                    setattr(old_value, "study_Course", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "study_Course"):
                opp_val = getattr(value, "study_Course", None)
                setattr(value, "study_Course", self)

    @property
    def SemesterCourse(self):
        return self.__SemesterCourse

    @SemesterCourse.setter
    def SemesterCourse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_SemesterCourse__SemesterCourse", None)
        self.__SemesterCourse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "semester"):
                opp_val = getattr(old_value, "semester", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "semester"):
                opp_val = getattr(value, "semester", None)
                if opp_val is None:
                    setattr(value, "semester", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
