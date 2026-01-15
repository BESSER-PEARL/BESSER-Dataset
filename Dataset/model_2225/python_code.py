from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class SemesterStatus(Enum):
    FALL = "FALL"
    SPRING = "SPRING"
class CourseStatus(Enum):
    MANDATORY = "MANDATORY"
    ELECTIVE = "ELECTIVE"


############################################
# Definition of Classes
############################################

class Program_Department:

    def __init__(self, name: str, Department: "Program_Course" = None, Program_Department: set["Program_Program"] = None, department: set["Program_Course"] = None):
        self.name = name
        self.Department = Department
        self.Program_Department = Program_Department if Program_Department is not None else set()
        self.department = department if department is not None else set()
        
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
        old_value = getattr(self, f"_Program_Department__Department", None)
        self.__Department = value
        
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
    def department(self):
        return self.__department

    @department.setter
    def department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Program_Department__department", None)
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
    def Program_Department(self):
        return self.__Program_Department

    @Program_Department.setter
    def Program_Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Program_Department__Program_Department", None)
        self.__Program_Department = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Program_Program14"):
                    opp_val = getattr(item, "Program_Program14", None)
                    
                    if opp_val == self:
                        setattr(item, "Program_Program14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Program_Program14"):
                    opp_val = getattr(item, "Program_Program14", None)
                    
                    setattr(item, "Program_Program14", self)
                    

class Program_SemesterCourse:

    def __init__(self, status: str, Program_SemesterCourse: "Program_Course" = None, semesterCourses: "Program_Semester" = None, SemesterCourse: "Program_Semester" = None):
        self.status = status
        self.Program_SemesterCourse = Program_SemesterCourse
        self.semesterCourses = semesterCourses
        self.SemesterCourse = SemesterCourse
        
    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def Program_SemesterCourse(self):
        return self.__Program_SemesterCourse

    @Program_SemesterCourse.setter
    def Program_SemesterCourse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Program_SemesterCourse__Program_SemesterCourse", None)
        self.__Program_SemesterCourse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Program_Course"):
                opp_val = getattr(old_value, "Program_Course", None)
                if opp_val == self:
                    setattr(old_value, "Program_Course", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Program_Course"):
                opp_val = getattr(value, "Program_Course", None)
                setattr(value, "Program_Course", self)

    @property
    def semesterCourses(self):
        return self.__semesterCourses

    @semesterCourses.setter
    def semesterCourses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Program_SemesterCourse__semesterCourses", None)
        self.__semesterCourses = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Semester"):
                opp_val = getattr(old_value, "Semester", None)
                if opp_val == self:
                    setattr(old_value, "Semester", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Semester"):
                opp_val = getattr(value, "Semester", None)
                setattr(value, "Semester", self)

    @property
    def SemesterCourse(self):
        return self.__SemesterCourse

    @SemesterCourse.setter
    def SemesterCourse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Program_SemesterCourse__SemesterCourse", None)
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

class Program_Course:

    def __init__(self, name: str, code: str, credit: float, Program_Course: "Program_SemesterCourse" = None, courses: "Program_Department" = None, Course: "Program_Department" = None):
        self.name = name
        self.code = code
        self.credit = credit
        self.Program_Course = Program_Course
        self.courses = courses
        self.Course = Course
        
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
    def credit(self) -> float:
        return self.__credit

    @credit.setter
    def credit(self, credit: float):
        self.__credit = credit

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Program_Course__courses", None)
        self.__courses = value
        
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
    def Course(self):
        return self.__Course

    @Course.setter
    def Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Program_Course__Course", None)
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
    def Program_Course(self):
        return self.__Program_Course

    @Program_Course.setter
    def Program_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Program_Course__Program_Course", None)
        self.__Program_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Program_SemesterCourse"):
                opp_val = getattr(old_value, "Program_SemesterCourse", None)
                if opp_val == self:
                    setattr(old_value, "Program_SemesterCourse", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Program_SemesterCourse"):
                opp_val = getattr(value, "Program_SemesterCourse", None)
                setattr(value, "Program_SemesterCourse", self)

class Program_Specialization:

    def __init__(self, name: str, Program_Specialization: "Program_Program" = None, Program_Specialization4: set["Program_Semester"] = None, Program_Specialization8: "Program_Specialization" = None, Program_Specialization6: set["Program_Specialization"] = None):
        self.name = name
        self.Program_Specialization = Program_Specialization
        self.Program_Specialization4 = Program_Specialization4 if Program_Specialization4 is not None else set()
        self.Program_Specialization8 = Program_Specialization8
        self.Program_Specialization6 = Program_Specialization6 if Program_Specialization6 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Program_Specialization(self):
        return self.__Program_Specialization

    @Program_Specialization.setter
    def Program_Specialization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Program_Specialization__Program_Specialization", None)
        self.__Program_Specialization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Program_Program2"):
                opp_val = getattr(old_value, "Program_Program2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Program_Program2"):
                opp_val = getattr(value, "Program_Program2", None)
                if opp_val is None:
                    setattr(value, "Program_Program2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Program_Specialization6(self):
        return self.__Program_Specialization6

    @Program_Specialization6.setter
    def Program_Specialization6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Program_Specialization__Program_Specialization6", None)
        self.__Program_Specialization6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Program_Specialization8"):
                    opp_val = getattr(item, "Program_Specialization8", None)
                    
                    if opp_val == self:
                        setattr(item, "Program_Specialization8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Program_Specialization8"):
                    opp_val = getattr(item, "Program_Specialization8", None)
                    
                    setattr(item, "Program_Specialization8", self)
                    

    @property
    def Program_Specialization8(self):
        return self.__Program_Specialization8

    @Program_Specialization8.setter
    def Program_Specialization8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Program_Specialization__Program_Specialization8", None)
        self.__Program_Specialization8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Program_Specialization6"):
                opp_val = getattr(old_value, "Program_Specialization6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Program_Specialization6"):
                opp_val = getattr(value, "Program_Specialization6", None)
                if opp_val is None:
                    setattr(value, "Program_Specialization6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Program_Specialization4(self):
        return self.__Program_Specialization4

    @Program_Specialization4.setter
    def Program_Specialization4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Program_Specialization__Program_Specialization4", None)
        self.__Program_Specialization4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Program_Semester5"):
                    opp_val = getattr(item, "Program_Semester5", None)
                    
                    if opp_val == self:
                        setattr(item, "Program_Semester5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Program_Semester5"):
                    opp_val = getattr(item, "Program_Semester5", None)
                    
                    setattr(item, "Program_Semester5", self)
                    

class Program_Semester:

    def __init__(self, status: str, name: str, code: str, Program_Semester: "Program_Program" = None, Program_Semester5: "Program_Specialization" = None, Semester: "Program_SemesterCourse" = None, semester: set["Program_SemesterCourse"] = None):
        self.status = status
        self.name = name
        self.code = code
        self.Program_Semester = Program_Semester
        self.Program_Semester5 = Program_Semester5
        self.Semester = Semester
        self.semester = semester if semester is not None else set()
        
    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

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
    def semester(self):
        return self.__semester

    @semester.setter
    def semester(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Program_Semester__semester", None)
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
                    

    @property
    def Program_Semester(self):
        return self.__Program_Semester

    @Program_Semester.setter
    def Program_Semester(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Program_Semester__Program_Semester", None)
        self.__Program_Semester = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Program_Program"):
                opp_val = getattr(old_value, "Program_Program", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Program_Program"):
                opp_val = getattr(value, "Program_Program", None)
                if opp_val is None:
                    setattr(value, "Program_Program", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Semester(self):
        return self.__Semester

    @Semester.setter
    def Semester(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Program_Semester__Semester", None)
        self.__Semester = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "semesterCourses"):
                opp_val = getattr(old_value, "semesterCourses", None)
                if opp_val == self:
                    setattr(old_value, "semesterCourses", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "semesterCourses"):
                opp_val = getattr(value, "semesterCourses", None)
                setattr(value, "semesterCourses", self)

    @property
    def Program_Semester5(self):
        return self.__Program_Semester5

    @Program_Semester5.setter
    def Program_Semester5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Program_Semester__Program_Semester5", None)
        self.__Program_Semester5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Program_Specialization4"):
                opp_val = getattr(old_value, "Program_Specialization4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Program_Specialization4"):
                opp_val = getattr(value, "Program_Specialization4", None)
                if opp_val is None:
                    setattr(value, "Program_Specialization4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Program_Program:

    def __init__(self, name: str, year: float, Program_Program: set["Program_Semester"] = None, Program_Program2: set["Program_Specialization"] = None, Program_Program14: "Program_Department" = None):
        self.name = name
        self.year = year
        self.Program_Program = Program_Program if Program_Program is not None else set()
        self.Program_Program2 = Program_Program2 if Program_Program2 is not None else set()
        self.Program_Program14 = Program_Program14
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def year(self) -> float:
        return self.__year

    @year.setter
    def year(self, year: float):
        self.__year = year

    @property
    def Program_Program(self):
        return self.__Program_Program

    @Program_Program.setter
    def Program_Program(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Program_Program__Program_Program", None)
        self.__Program_Program = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Program_Semester"):
                    opp_val = getattr(item, "Program_Semester", None)
                    
                    if opp_val == self:
                        setattr(item, "Program_Semester", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Program_Semester"):
                    opp_val = getattr(item, "Program_Semester", None)
                    
                    setattr(item, "Program_Semester", self)
                    

    @property
    def Program_Program14(self):
        return self.__Program_Program14

    @Program_Program14.setter
    def Program_Program14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Program_Program__Program_Program14", None)
        self.__Program_Program14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Program_Department"):
                opp_val = getattr(old_value, "Program_Department", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Program_Department"):
                opp_val = getattr(value, "Program_Department", None)
                if opp_val is None:
                    setattr(value, "Program_Department", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Program_Program2(self):
        return self.__Program_Program2

    @Program_Program2.setter
    def Program_Program2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Program_Program__Program_Program2", None)
        self.__Program_Program2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Program_Specialization"):
                    opp_val = getattr(item, "Program_Specialization", None)
                    
                    if opp_val == self:
                        setattr(item, "Program_Specialization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Program_Specialization"):
                    opp_val = getattr(item, "Program_Specialization", None)
                    
                    setattr(item, "Program_Specialization", self)
                    
