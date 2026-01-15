from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class CourseStatus(Enum):
    MANDATORY = "MANDATORY"
    ELECTIVE = "ELECTIVE"
class Season(Enum):
    FALL = "FALL"
    SPRING = "SPRING"


############################################
# Definition of Classes
############################################

class studyplan_Course:

    def __init__(self, code: str, name: str, credits: float, courses: "studyplan_Department" = None, studyplan_Course: "studyplan_SemesterCourse" = None, Course: "studyplan_Department" = None):
        self.code = code
        self.name = name
        self.credits = credits
        self.courses = courses
        self.studyplan_Course = studyplan_Course
        self.Course = Course
        
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
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyplan_Course__courses", None)
        self.__courses = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Department13"):
                opp_val = getattr(old_value, "Department13", None)
                if opp_val == self:
                    setattr(old_value, "Department13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Department13"):
                opp_val = getattr(value, "Department13", None)
                setattr(value, "Department13", self)

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
            if hasattr(old_value, "studyplan_SemesterCourse15"):
                opp_val = getattr(old_value, "studyplan_SemesterCourse15", None)
                if opp_val == self:
                    setattr(old_value, "studyplan_SemesterCourse15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyplan_SemesterCourse15"):
                opp_val = getattr(value, "studyplan_SemesterCourse15", None)
                setattr(value, "studyplan_SemesterCourse15", self)

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

class studyplan_SemesterCourse:

    def __init__(self, status: str, studyplan_SemesterCourse: "studyplan_Semester" = None, studyplan_SemesterCourse15: "studyplan_Course" = None):
        self.status = status
        self.studyplan_SemesterCourse = studyplan_SemesterCourse
        self.studyplan_SemesterCourse15 = studyplan_SemesterCourse15
        
    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def studyplan_SemesterCourse(self):
        return self.__studyplan_SemesterCourse

    @studyplan_SemesterCourse.setter
    def studyplan_SemesterCourse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyplan_SemesterCourse__studyplan_SemesterCourse", None)
        self.__studyplan_SemesterCourse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyplan_Semester5"):
                opp_val = getattr(old_value, "studyplan_Semester5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyplan_Semester5"):
                opp_val = getattr(value, "studyplan_Semester5", None)
                if opp_val is None:
                    setattr(value, "studyplan_Semester5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def studyplan_SemesterCourse15(self):
        return self.__studyplan_SemesterCourse15

    @studyplan_SemesterCourse15.setter
    def studyplan_SemesterCourse15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyplan_SemesterCourse__studyplan_SemesterCourse15", None)
        self.__studyplan_SemesterCourse15 = value
        
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

class studyplan_Program:

    def __init__(self, code: str, name: str, studyplan_Program: set["studyplan_Semester"] = None, studyplan_Program2: set["studyplan_Specialization"] = None, programs: "studyplan_Department" = None, Program: "studyplan_Department" = None):
        self.code = code
        self.name = name
        self.studyplan_Program = studyplan_Program if studyplan_Program is not None else set()
        self.studyplan_Program2 = studyplan_Program2 if studyplan_Program2 is not None else set()
        self.programs = programs
        self.Program = Program
        
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
    def studyplan_Program2(self):
        return self.__studyplan_Program2

    @studyplan_Program2.setter
    def studyplan_Program2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyplan_Program__studyplan_Program2", None)
        self.__studyplan_Program2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "studyplan_Specialization"):
                    opp_val = getattr(item, "studyplan_Specialization", None)
                    
                    if opp_val == self:
                        setattr(item, "studyplan_Specialization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "studyplan_Specialization"):
                    opp_val = getattr(item, "studyplan_Specialization", None)
                    
                    setattr(item, "studyplan_Specialization", self)
                    

    @property
    def programs(self):
        return self.__programs

    @programs.setter
    def programs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyplan_Program__programs", None)
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
    def Program(self):
        return self.__Program

    @Program.setter
    def Program(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyplan_Program__Program", None)
        self.__Program = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "department18"):
                opp_val = getattr(old_value, "department18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "department18"):
                opp_val = getattr(value, "department18", None)
                if opp_val is None:
                    setattr(value, "department18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def studyplan_Program(self):
        return self.__studyplan_Program

    @studyplan_Program.setter
    def studyplan_Program(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyplan_Program__studyplan_Program", None)
        self.__studyplan_Program = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "studyplan_Semester"):
                    opp_val = getattr(item, "studyplan_Semester", None)
                    
                    if opp_val == self:
                        setattr(item, "studyplan_Semester", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "studyplan_Semester"):
                    opp_val = getattr(item, "studyplan_Semester", None)
                    
                    setattr(item, "studyplan_Semester", self)
                    

class studyplan_Department:

    def __init__(self, name: str, Department: "studyplan_Program" = None, Department13: "studyplan_Course" = None, department: set["studyplan_Course"] = None, department18: set["studyplan_Program"] = None):
        self.name = name
        self.Department = Department
        self.Department13 = Department13
        self.department = department if department is not None else set()
        self.department18 = department18 if department18 is not None else set()
        
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
        old_value = getattr(self, f"_studyplan_Department__Department", None)
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
    def department(self):
        return self.__department

    @department.setter
    def department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyplan_Department__department", None)
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
                    

    @property
    def Department13(self):
        return self.__Department13

    @Department13.setter
    def Department13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyplan_Department__Department13", None)
        self.__Department13 = value
        
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
    def department18(self):
        return self.__department18

    @department18.setter
    def department18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyplan_Department__department18", None)
        self.__department18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Program"):
                    opp_val = getattr(item, "Program", None)
                    
                    if opp_val == self:
                        setattr(item, "Program", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Program"):
                    opp_val = getattr(item, "Program", None)
                    
                    setattr(item, "Program", self)
                    

class studyplan_Specialization:

    def __init__(self, name: str, studyplan_Specialization: "studyplan_Program" = None, studyplan_Specialization11: "studyplan_Specialization" = None, studyplan_Specialization9: set["studyplan_Specialization"] = None, studyplan_Specialization7: set["studyplan_Semester"] = None):
        self.name = name
        self.studyplan_Specialization = studyplan_Specialization
        self.studyplan_Specialization11 = studyplan_Specialization11
        self.studyplan_Specialization9 = studyplan_Specialization9 if studyplan_Specialization9 is not None else set()
        self.studyplan_Specialization7 = studyplan_Specialization7 if studyplan_Specialization7 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def studyplan_Specialization9(self):
        return self.__studyplan_Specialization9

    @studyplan_Specialization9.setter
    def studyplan_Specialization9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyplan_Specialization__studyplan_Specialization9", None)
        self.__studyplan_Specialization9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "studyplan_Specialization11"):
                    opp_val = getattr(item, "studyplan_Specialization11", None)
                    
                    if opp_val == self:
                        setattr(item, "studyplan_Specialization11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "studyplan_Specialization11"):
                    opp_val = getattr(item, "studyplan_Specialization11", None)
                    
                    setattr(item, "studyplan_Specialization11", self)
                    

    @property
    def studyplan_Specialization(self):
        return self.__studyplan_Specialization

    @studyplan_Specialization.setter
    def studyplan_Specialization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyplan_Specialization__studyplan_Specialization", None)
        self.__studyplan_Specialization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyplan_Program2"):
                opp_val = getattr(old_value, "studyplan_Program2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyplan_Program2"):
                opp_val = getattr(value, "studyplan_Program2", None)
                if opp_val is None:
                    setattr(value, "studyplan_Program2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def studyplan_Specialization7(self):
        return self.__studyplan_Specialization7

    @studyplan_Specialization7.setter
    def studyplan_Specialization7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyplan_Specialization__studyplan_Specialization7", None)
        self.__studyplan_Specialization7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "studyplan_Semester8"):
                    opp_val = getattr(item, "studyplan_Semester8", None)
                    
                    if opp_val == self:
                        setattr(item, "studyplan_Semester8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "studyplan_Semester8"):
                    opp_val = getattr(item, "studyplan_Semester8", None)
                    
                    setattr(item, "studyplan_Semester8", self)
                    

    @property
    def studyplan_Specialization11(self):
        return self.__studyplan_Specialization11

    @studyplan_Specialization11.setter
    def studyplan_Specialization11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyplan_Specialization__studyplan_Specialization11", None)
        self.__studyplan_Specialization11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyplan_Specialization9"):
                opp_val = getattr(old_value, "studyplan_Specialization9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyplan_Specialization9"):
                opp_val = getattr(value, "studyplan_Specialization9", None)
                if opp_val is None:
                    setattr(value, "studyplan_Specialization9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class studyplan_Semester:

    def __init__(self, name: str, season: str, year: int, studyplan_Semester: "studyplan_Program" = None, studyplan_Semester5: set["studyplan_SemesterCourse"] = None, studyplan_Semester8: "studyplan_Specialization" = None):
        self.name = name
        self.season = season
        self.year = year
        self.studyplan_Semester = studyplan_Semester
        self.studyplan_Semester5 = studyplan_Semester5 if studyplan_Semester5 is not None else set()
        self.studyplan_Semester8 = studyplan_Semester8
        
    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def season(self) -> str:
        return self.__season

    @season.setter
    def season(self, season: str):
        self.__season = season

    @property
    def studyplan_Semester8(self):
        return self.__studyplan_Semester8

    @studyplan_Semester8.setter
    def studyplan_Semester8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyplan_Semester__studyplan_Semester8", None)
        self.__studyplan_Semester8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyplan_Specialization7"):
                opp_val = getattr(old_value, "studyplan_Specialization7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyplan_Specialization7"):
                opp_val = getattr(value, "studyplan_Specialization7", None)
                if opp_val is None:
                    setattr(value, "studyplan_Specialization7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def studyplan_Semester5(self):
        return self.__studyplan_Semester5

    @studyplan_Semester5.setter
    def studyplan_Semester5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyplan_Semester__studyplan_Semester5", None)
        self.__studyplan_Semester5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "studyplan_SemesterCourse"):
                    opp_val = getattr(item, "studyplan_SemesterCourse", None)
                    
                    if opp_val == self:
                        setattr(item, "studyplan_SemesterCourse", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "studyplan_SemesterCourse"):
                    opp_val = getattr(item, "studyplan_SemesterCourse", None)
                    
                    setattr(item, "studyplan_SemesterCourse", self)
                    

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
            if hasattr(old_value, "studyplan_Program"):
                opp_val = getattr(old_value, "studyplan_Program", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyplan_Program"):
                opp_val = getattr(value, "studyplan_Program", None)
                if opp_val is None:
                    setattr(value, "studyplan_Program", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
