from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class SchoolElement(Enum):
    Student = "Student"
    Teacher = "Teacher"
    Faculty = "Faculty"
    CourseOfStudy = "CourseOfStudy"
    Course = "Course"
    School = "School"


############################################
# Definition of Classes
############################################

class school_Query:

    def __init__(self, type: str, school_Query32: "school_Where" = None, school_Query: "school_Student" = None, school_Query45: "school_SchoolDatabase" = None):
        self.type = type
        self.school_Query32 = school_Query32
        self.school_Query = school_Query
        self.school_Query45 = school_Query45
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def school_Query32(self):
        return self.__school_Query32

    @school_Query32.setter
    def school_Query32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Query__school_Query32", None)
        self.__school_Query32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_Where"):
                opp_val = getattr(old_value, "school_Where", None)
                if opp_val == self:
                    setattr(old_value, "school_Where", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_Where"):
                opp_val = getattr(value, "school_Where", None)
                setattr(value, "school_Where", self)

    @property
    def school_Query45(self):
        return self.__school_Query45

    @school_Query45.setter
    def school_Query45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Query__school_Query45", None)
        self.__school_Query45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_SchoolDatabase44"):
                opp_val = getattr(old_value, "school_SchoolDatabase44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_SchoolDatabase44"):
                opp_val = getattr(value, "school_SchoolDatabase44", None)
                if opp_val is None:
                    setattr(value, "school_SchoolDatabase44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def school_Query(self):
        return self.__school_Query

    @school_Query.setter
    def school_Query(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Query__school_Query", None)
        self.__school_Query = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_Student30"):
                opp_val = getattr(old_value, "school_Student30", None)
                if opp_val == self:
                    setattr(old_value, "school_Student30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_Student30"):
                opp_val = getattr(value, "school_Student30", None)
                setattr(value, "school_Student30", self)

class school_SchoolDatabase:

    pass
class school_BooleanExpr:

    def __init__(self, lhs: str, rhs: str, operator: str, school_BooleanExpr: "school_Where" = None, school_BooleanExpr37: "school_BooleanExpr" = None, school_BooleanExpr35: "school_BooleanExpr" = None, school_BooleanExpr40: "school_BooleanExpr" = None, school_BooleanExpr38: "school_BooleanExpr" = None):
        self.lhs = lhs
        self.rhs = rhs
        self.operator = operator
        self.school_BooleanExpr = school_BooleanExpr
        self.school_BooleanExpr37 = school_BooleanExpr37
        self.school_BooleanExpr35 = school_BooleanExpr35
        self.school_BooleanExpr40 = school_BooleanExpr40
        self.school_BooleanExpr38 = school_BooleanExpr38
        
    @property
    def rhs(self) -> str:
        return self.__rhs

    @rhs.setter
    def rhs(self, rhs: str):
        self.__rhs = rhs

    @property
    def lhs(self) -> str:
        return self.__lhs

    @lhs.setter
    def lhs(self, lhs: str):
        self.__lhs = lhs

    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def school_BooleanExpr35(self):
        return self.__school_BooleanExpr35

    @school_BooleanExpr35.setter
    def school_BooleanExpr35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_BooleanExpr__school_BooleanExpr35", None)
        self.__school_BooleanExpr35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_BooleanExpr37"):
                opp_val = getattr(old_value, "school_BooleanExpr37", None)
                if opp_val == self:
                    setattr(old_value, "school_BooleanExpr37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_BooleanExpr37"):
                opp_val = getattr(value, "school_BooleanExpr37", None)
                setattr(value, "school_BooleanExpr37", self)

    @property
    def school_BooleanExpr37(self):
        return self.__school_BooleanExpr37

    @school_BooleanExpr37.setter
    def school_BooleanExpr37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_BooleanExpr__school_BooleanExpr37", None)
        self.__school_BooleanExpr37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_BooleanExpr35"):
                opp_val = getattr(old_value, "school_BooleanExpr35", None)
                if opp_val == self:
                    setattr(old_value, "school_BooleanExpr35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_BooleanExpr35"):
                opp_val = getattr(value, "school_BooleanExpr35", None)
                setattr(value, "school_BooleanExpr35", self)

    @property
    def school_BooleanExpr38(self):
        return self.__school_BooleanExpr38

    @school_BooleanExpr38.setter
    def school_BooleanExpr38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_BooleanExpr__school_BooleanExpr38", None)
        self.__school_BooleanExpr38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_BooleanExpr40"):
                opp_val = getattr(old_value, "school_BooleanExpr40", None)
                if opp_val == self:
                    setattr(old_value, "school_BooleanExpr40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_BooleanExpr40"):
                opp_val = getattr(value, "school_BooleanExpr40", None)
                setattr(value, "school_BooleanExpr40", self)

    @property
    def school_BooleanExpr40(self):
        return self.__school_BooleanExpr40

    @school_BooleanExpr40.setter
    def school_BooleanExpr40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_BooleanExpr__school_BooleanExpr40", None)
        self.__school_BooleanExpr40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_BooleanExpr38"):
                opp_val = getattr(old_value, "school_BooleanExpr38", None)
                if opp_val == self:
                    setattr(old_value, "school_BooleanExpr38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_BooleanExpr38"):
                opp_val = getattr(value, "school_BooleanExpr38", None)
                setattr(value, "school_BooleanExpr38", self)

    @property
    def school_BooleanExpr(self):
        return self.__school_BooleanExpr

    @school_BooleanExpr.setter
    def school_BooleanExpr(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_BooleanExpr__school_BooleanExpr", None)
        self.__school_BooleanExpr = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_Where34"):
                opp_val = getattr(old_value, "school_Where34", None)
                if opp_val == self:
                    setattr(old_value, "school_Where34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_Where34"):
                opp_val = getattr(value, "school_Where34", None)
                setattr(value, "school_Where34", self)

class school_Where:

    pass
class school_CourseResult:

    def __init__(self, grade: str, CourseResult: "school_Course" = None, school_CourseResult: "school_Student" = None, courseresult: "school_Course" = None):
        self.grade = grade
        self.CourseResult = CourseResult
        self.school_CourseResult = school_CourseResult
        self.courseresult = courseresult
        
    @property
    def grade(self) -> str:
        return self.__grade

    @grade.setter
    def grade(self, grade: str):
        self.__grade = grade

    @property
    def CourseResult(self):
        return self.__CourseResult

    @CourseResult.setter
    def CourseResult(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_CourseResult__CourseResult", None)
        self.__CourseResult = value
        
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

    @property
    def school_CourseResult(self):
        return self.__school_CourseResult

    @school_CourseResult.setter
    def school_CourseResult(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_CourseResult__school_CourseResult", None)
        self.__school_CourseResult = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_Student26"):
                opp_val = getattr(old_value, "school_Student26", None)
                if opp_val == self:
                    setattr(old_value, "school_Student26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_Student26"):
                opp_val = getattr(value, "school_Student26", None)
                setattr(value, "school_Student26", self)

    @property
    def courseresult(self):
        return self.__courseresult

    @courseresult.setter
    def courseresult(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_CourseResult__courseresult", None)
        self.__courseresult = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Course28"):
                opp_val = getattr(old_value, "Course28", None)
                if opp_val == self:
                    setattr(old_value, "Course28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Course28"):
                opp_val = getattr(value, "Course28", None)
                setattr(value, "Course28", self)

class school_Teacher:

    def __init__(self, name: str, school_Teacher: "school_School" = None, Teacher: "school_Course" = None, taughtBy: set["school_Course"] = None):
        self.name = name
        self.school_Teacher = school_Teacher
        self.Teacher = Teacher
        self.taughtBy = taughtBy if taughtBy is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Teacher(self):
        return self.__Teacher

    @Teacher.setter
    def Teacher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Teacher__Teacher", None)
        self.__Teacher = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "teaches"):
                opp_val = getattr(old_value, "teaches", None)
                if opp_val == self:
                    setattr(old_value, "teaches", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "teaches"):
                opp_val = getattr(value, "teaches", None)
                setattr(value, "teaches", self)

    @property
    def school_Teacher(self):
        return self.__school_Teacher

    @school_Teacher.setter
    def school_Teacher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Teacher__school_Teacher", None)
        self.__school_Teacher = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_School8"):
                opp_val = getattr(old_value, "school_School8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_School8"):
                opp_val = getattr(value, "school_School8", None)
                if opp_val is None:
                    setattr(value, "school_School8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def taughtBy(self):
        return self.__taughtBy

    @taughtBy.setter
    def taughtBy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Teacher__taughtBy", None)
        self.__taughtBy = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Course24"):
                    opp_val = getattr(item, "Course24", None)
                    
                    if opp_val == self:
                        setattr(item, "Course24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Course24"):
                    opp_val = getattr(item, "Course24", None)
                    
                    setattr(item, "Course24", self)
                    

class school_Student:

    def __init__(self, name: str, studentNumber: str, school_Student: "school_School" = None, Student: "school_CourseOfStudy" = None, Student17: "school_Course" = None, enrolledStudent: set["school_Course"] = None, student: "school_CourseOfStudy" = None, school_Student26: "school_CourseResult" = None, school_Student30: "school_Query" = None):
        self.name = name
        self.studentNumber = studentNumber
        self.school_Student = school_Student
        self.Student = Student
        self.Student17 = Student17
        self.enrolledStudent = enrolledStudent if enrolledStudent is not None else set()
        self.student = student
        self.school_Student26 = school_Student26
        self.school_Student30 = school_Student30
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def studentNumber(self) -> str:
        return self.__studentNumber

    @studentNumber.setter
    def studentNumber(self, studentNumber: str):
        self.__studentNumber = studentNumber

    @property
    def school_Student30(self):
        return self.__school_Student30

    @school_Student30.setter
    def school_Student30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Student__school_Student30", None)
        self.__school_Student30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_Query"):
                opp_val = getattr(old_value, "school_Query", None)
                if opp_val == self:
                    setattr(old_value, "school_Query", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_Query"):
                opp_val = getattr(value, "school_Query", None)
                setattr(value, "school_Query", self)

    @property
    def student(self):
        return self.__student

    @student.setter
    def student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Student__student", None)
        self.__student = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CourseOfStudy22"):
                opp_val = getattr(old_value, "CourseOfStudy22", None)
                if opp_val == self:
                    setattr(old_value, "CourseOfStudy22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CourseOfStudy22"):
                opp_val = getattr(value, "CourseOfStudy22", None)
                setattr(value, "CourseOfStudy22", self)

    @property
    def Student17(self):
        return self.__Student17

    @Student17.setter
    def Student17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Student__Student17", None)
        self.__Student17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "enrolledIn"):
                opp_val = getattr(old_value, "enrolledIn", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "enrolledIn"):
                opp_val = getattr(value, "enrolledIn", None)
                if opp_val is None:
                    setattr(value, "enrolledIn", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def school_Student26(self):
        return self.__school_Student26

    @school_Student26.setter
    def school_Student26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Student__school_Student26", None)
        self.__school_Student26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_CourseResult"):
                opp_val = getattr(old_value, "school_CourseResult", None)
                if opp_val == self:
                    setattr(old_value, "school_CourseResult", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_CourseResult"):
                opp_val = getattr(value, "school_CourseResult", None)
                setattr(value, "school_CourseResult", self)

    @property
    def enrolledStudent(self):
        return self.__enrolledStudent

    @enrolledStudent.setter
    def enrolledStudent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Student__enrolledStudent", None)
        self.__enrolledStudent = value if value is not None else set()
        
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
    def school_Student(self):
        return self.__school_Student

    @school_Student.setter
    def school_Student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Student__school_Student", None)
        self.__school_Student = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_School6"):
                opp_val = getattr(old_value, "school_School6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_School6"):
                opp_val = getattr(value, "school_School6", None)
                if opp_val is None:
                    setattr(value, "school_School6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Student(self):
        return self.__Student

    @Student.setter
    def Student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Student__Student", None)
        self.__Student = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courseofstudy15"):
                opp_val = getattr(old_value, "courseofstudy15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courseofstudy15"):
                opp_val = getattr(value, "courseofstudy15", None)
                if opp_val is None:
                    setattr(value, "courseofstudy15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class school_Course:

    def __init__(self, name: str, courseNumber: str, school_Course: "school_School" = None, school_Course12: "school_CourseOfStudy" = None, enrolledIn: set["school_Student"] = None, teaches: "school_Teacher" = None, course: set["school_CourseResult"] = None, Course: "school_Student" = None, Course24: "school_Teacher" = None, Course28: "school_CourseResult" = None):
        self.name = name
        self.courseNumber = courseNumber
        self.school_Course = school_Course
        self.school_Course12 = school_Course12
        self.enrolledIn = enrolledIn if enrolledIn is not None else set()
        self.teaches = teaches
        self.course = course if course is not None else set()
        self.Course = Course
        self.Course24 = Course24
        self.Course28 = Course28
        
    @property
    def courseNumber(self) -> str:
        return self.__courseNumber

    @courseNumber.setter
    def courseNumber(self, courseNumber: str):
        self.__courseNumber = courseNumber

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def teaches(self):
        return self.__teaches

    @teaches.setter
    def teaches(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Course__teaches", None)
        self.__teaches = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Teacher"):
                opp_val = getattr(old_value, "Teacher", None)
                if opp_val == self:
                    setattr(old_value, "Teacher", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Teacher"):
                opp_val = getattr(value, "Teacher", None)
                setattr(value, "Teacher", self)

    @property
    def Course28(self):
        return self.__Course28

    @Course28.setter
    def Course28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Course__Course28", None)
        self.__Course28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courseresult"):
                opp_val = getattr(old_value, "courseresult", None)
                if opp_val == self:
                    setattr(old_value, "courseresult", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courseresult"):
                opp_val = getattr(value, "courseresult", None)
                setattr(value, "courseresult", self)

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Course__course", None)
        self.__course = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CourseResult"):
                    opp_val = getattr(item, "CourseResult", None)
                    
                    if opp_val == self:
                        setattr(item, "CourseResult", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CourseResult"):
                    opp_val = getattr(item, "CourseResult", None)
                    
                    setattr(item, "CourseResult", self)
                    

    @property
    def Course24(self):
        return self.__Course24

    @Course24.setter
    def Course24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Course__Course24", None)
        self.__Course24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "taughtBy"):
                opp_val = getattr(old_value, "taughtBy", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "taughtBy"):
                opp_val = getattr(value, "taughtBy", None)
                if opp_val is None:
                    setattr(value, "taughtBy", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def enrolledIn(self):
        return self.__enrolledIn

    @enrolledIn.setter
    def enrolledIn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Course__enrolledIn", None)
        self.__enrolledIn = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Student17"):
                    opp_val = getattr(item, "Student17", None)
                    
                    if opp_val == self:
                        setattr(item, "Student17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Student17"):
                    opp_val = getattr(item, "Student17", None)
                    
                    setattr(item, "Student17", self)
                    

    @property
    def Course(self):
        return self.__Course

    @Course.setter
    def Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Course__Course", None)
        self.__Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "enrolledStudent"):
                opp_val = getattr(old_value, "enrolledStudent", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "enrolledStudent"):
                opp_val = getattr(value, "enrolledStudent", None)
                if opp_val is None:
                    setattr(value, "enrolledStudent", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def school_Course12(self):
        return self.__school_Course12

    @school_Course12.setter
    def school_Course12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Course__school_Course12", None)
        self.__school_Course12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_CourseOfStudy11"):
                opp_val = getattr(old_value, "school_CourseOfStudy11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_CourseOfStudy11"):
                opp_val = getattr(value, "school_CourseOfStudy11", None)
                if opp_val is None:
                    setattr(value, "school_CourseOfStudy11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def school_Course(self):
        return self.__school_Course

    @school_Course.setter
    def school_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Course__school_Course", None)
        self.__school_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_School4"):
                opp_val = getattr(old_value, "school_School4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_School4"):
                opp_val = getattr(value, "school_School4", None)
                if opp_val is None:
                    setattr(value, "school_School4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class school_CourseOfStudy:

    def __init__(self, name: str, school_CourseOfStudy: "school_School" = None, CourseOfStudy: "school_Faculty" = None, school_CourseOfStudy11: set["school_Course"] = None, courseofstudy: "school_Faculty" = None, courseofstudy15: set["school_Student"] = None, CourseOfStudy22: "school_Student" = None):
        self.name = name
        self.school_CourseOfStudy = school_CourseOfStudy
        self.CourseOfStudy = CourseOfStudy
        self.school_CourseOfStudy11 = school_CourseOfStudy11 if school_CourseOfStudy11 is not None else set()
        self.courseofstudy = courseofstudy
        self.courseofstudy15 = courseofstudy15 if courseofstudy15 is not None else set()
        self.CourseOfStudy22 = CourseOfStudy22
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def CourseOfStudy(self):
        return self.__CourseOfStudy

    @CourseOfStudy.setter
    def CourseOfStudy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_CourseOfStudy__CourseOfStudy", None)
        self.__CourseOfStudy = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "faculty"):
                opp_val = getattr(old_value, "faculty", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "faculty"):
                opp_val = getattr(value, "faculty", None)
                if opp_val is None:
                    setattr(value, "faculty", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CourseOfStudy22(self):
        return self.__CourseOfStudy22

    @CourseOfStudy22.setter
    def CourseOfStudy22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_CourseOfStudy__CourseOfStudy22", None)
        self.__CourseOfStudy22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "student"):
                opp_val = getattr(old_value, "student", None)
                if opp_val == self:
                    setattr(old_value, "student", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "student"):
                opp_val = getattr(value, "student", None)
                setattr(value, "student", self)

    @property
    def school_CourseOfStudy(self):
        return self.__school_CourseOfStudy

    @school_CourseOfStudy.setter
    def school_CourseOfStudy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_CourseOfStudy__school_CourseOfStudy", None)
        self.__school_CourseOfStudy = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_School2"):
                opp_val = getattr(old_value, "school_School2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_School2"):
                opp_val = getattr(value, "school_School2", None)
                if opp_val is None:
                    setattr(value, "school_School2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def courseofstudy15(self):
        return self.__courseofstudy15

    @courseofstudy15.setter
    def courseofstudy15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_CourseOfStudy__courseofstudy15", None)
        self.__courseofstudy15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Student"):
                    opp_val = getattr(item, "Student", None)
                    
                    if opp_val == self:
                        setattr(item, "Student", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Student"):
                    opp_val = getattr(item, "Student", None)
                    
                    setattr(item, "Student", self)
                    

    @property
    def school_CourseOfStudy11(self):
        return self.__school_CourseOfStudy11

    @school_CourseOfStudy11.setter
    def school_CourseOfStudy11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_CourseOfStudy__school_CourseOfStudy11", None)
        self.__school_CourseOfStudy11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "school_Course12"):
                    opp_val = getattr(item, "school_Course12", None)
                    
                    if opp_val == self:
                        setattr(item, "school_Course12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "school_Course12"):
                    opp_val = getattr(item, "school_Course12", None)
                    
                    setattr(item, "school_Course12", self)
                    

    @property
    def courseofstudy(self):
        return self.__courseofstudy

    @courseofstudy.setter
    def courseofstudy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_CourseOfStudy__courseofstudy", None)
        self.__courseofstudy = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Faculty"):
                opp_val = getattr(old_value, "Faculty", None)
                if opp_val == self:
                    setattr(old_value, "Faculty", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Faculty"):
                opp_val = getattr(value, "Faculty", None)
                setattr(value, "Faculty", self)

class school_Faculty:

    def __init__(self, name: str, school_Faculty: "school_School" = None, faculty: set["school_CourseOfStudy"] = None, Faculty: "school_CourseOfStudy" = None):
        self.name = name
        self.school_Faculty = school_Faculty
        self.faculty = faculty if faculty is not None else set()
        self.Faculty = Faculty
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def school_Faculty(self):
        return self.__school_Faculty

    @school_Faculty.setter
    def school_Faculty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Faculty__school_Faculty", None)
        self.__school_Faculty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_School"):
                opp_val = getattr(old_value, "school_School", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_School"):
                opp_val = getattr(value, "school_School", None)
                if opp_val is None:
                    setattr(value, "school_School", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Faculty(self):
        return self.__Faculty

    @Faculty.setter
    def Faculty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Faculty__Faculty", None)
        self.__Faculty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courseofstudy"):
                opp_val = getattr(old_value, "courseofstudy", None)
                if opp_val == self:
                    setattr(old_value, "courseofstudy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courseofstudy"):
                opp_val = getattr(value, "courseofstudy", None)
                setattr(value, "courseofstudy", self)

    @property
    def faculty(self):
        return self.__faculty

    @faculty.setter
    def faculty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Faculty__faculty", None)
        self.__faculty = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CourseOfStudy"):
                    opp_val = getattr(item, "CourseOfStudy", None)
                    
                    if opp_val == self:
                        setattr(item, "CourseOfStudy", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CourseOfStudy"):
                    opp_val = getattr(item, "CourseOfStudy", None)
                    
                    setattr(item, "CourseOfStudy", self)
                    

class school_School:

    def __init__(self, name: str, school_School: set["school_Faculty"] = None, school_School2: set["school_CourseOfStudy"] = None, school_School4: set["school_Course"] = None, school_School6: set["school_Student"] = None, school_School8: set["school_Teacher"] = None, school_School42: "school_SchoolDatabase" = None):
        self.name = name
        self.school_School = school_School if school_School is not None else set()
        self.school_School2 = school_School2 if school_School2 is not None else set()
        self.school_School4 = school_School4 if school_School4 is not None else set()
        self.school_School6 = school_School6 if school_School6 is not None else set()
        self.school_School8 = school_School8 if school_School8 is not None else set()
        self.school_School42 = school_School42
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def school_School42(self):
        return self.__school_School42

    @school_School42.setter
    def school_School42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_School__school_School42", None)
        self.__school_School42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_SchoolDatabase"):
                opp_val = getattr(old_value, "school_SchoolDatabase", None)
                if opp_val == self:
                    setattr(old_value, "school_SchoolDatabase", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_SchoolDatabase"):
                opp_val = getattr(value, "school_SchoolDatabase", None)
                setattr(value, "school_SchoolDatabase", self)

    @property
    def school_School6(self):
        return self.__school_School6

    @school_School6.setter
    def school_School6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_School__school_School6", None)
        self.__school_School6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "school_Student"):
                    opp_val = getattr(item, "school_Student", None)
                    
                    if opp_val == self:
                        setattr(item, "school_Student", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "school_Student"):
                    opp_val = getattr(item, "school_Student", None)
                    
                    setattr(item, "school_Student", self)
                    

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
                if hasattr(item, "school_Course"):
                    opp_val = getattr(item, "school_Course", None)
                    
                    if opp_val == self:
                        setattr(item, "school_Course", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "school_Course"):
                    opp_val = getattr(item, "school_Course", None)
                    
                    setattr(item, "school_Course", self)
                    

    @property
    def school_School8(self):
        return self.__school_School8

    @school_School8.setter
    def school_School8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_School__school_School8", None)
        self.__school_School8 = value if value is not None else set()
        
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
                    

    @property
    def school_School2(self):
        return self.__school_School2

    @school_School2.setter
    def school_School2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_School__school_School2", None)
        self.__school_School2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "school_CourseOfStudy"):
                    opp_val = getattr(item, "school_CourseOfStudy", None)
                    
                    if opp_val == self:
                        setattr(item, "school_CourseOfStudy", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "school_CourseOfStudy"):
                    opp_val = getattr(item, "school_CourseOfStudy", None)
                    
                    setattr(item, "school_CourseOfStudy", self)
                    

    @property
    def school_School(self):
        return self.__school_School

    @school_School.setter
    def school_School(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_School__school_School", None)
        self.__school_School = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "school_Faculty"):
                    opp_val = getattr(item, "school_Faculty", None)
                    
                    if opp_val == self:
                        setattr(item, "school_Faculty", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "school_Faculty"):
                    opp_val = getattr(item, "school_Faculty", None)
                    
                    setattr(item, "school_Faculty", self)
                    
