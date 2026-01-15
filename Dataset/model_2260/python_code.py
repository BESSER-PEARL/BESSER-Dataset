from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Course:

    pass
class school_LimitedCapacityCourse(Course):

    def __init__(self, capacity: int):
        self.capacity = capacity
        
    @property
    def capacity(self) -> int:
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: int):
        self.__capacity = capacity

class school_SpecialisationCourse(Course):

    def __init__(self, specialisation: str):
        self.specialisation = specialisation
        
    @property
    def specialisation(self) -> str:
        return self.__specialisation

    @specialisation.setter
    def specialisation(self, specialisation: str):
        self.__specialisation = specialisation

class school_Student:

    def __init__(self, name: str, Student: "school_SchoolClass" = None, students: "school_SchoolClass" = None, school_Student: "school_Student" = None, school_Student21: set["school_Student"] = None):
        self.name = name
        self.Student = Student
        self.students = students
        self.school_Student = school_Student
        self.school_Student21 = school_Student21 if school_Student21 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def students(self):
        return self.__students

    @students.setter
    def students(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Student__students", None)
        self.__students = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SchoolClass20"):
                opp_val = getattr(old_value, "SchoolClass20", None)
                if opp_val == self:
                    setattr(old_value, "SchoolClass20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SchoolClass20"):
                opp_val = getattr(value, "SchoolClass20", None)
                setattr(value, "SchoolClass20", self)

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
            if hasattr(old_value, "schoolClass"):
                opp_val = getattr(old_value, "schoolClass", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schoolClass"):
                opp_val = getattr(value, "schoolClass", None)
                if opp_val is None:
                    setattr(value, "schoolClass", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "school_Student21"):
                opp_val = getattr(old_value, "school_Student21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_Student21"):
                opp_val = getattr(value, "school_Student21", None)
                if opp_val is None:
                    setattr(value, "school_Student21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def school_Student21(self):
        return self.__school_Student21

    @school_Student21.setter
    def school_Student21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Student__school_Student21", None)
        self.__school_Student21 = value if value is not None else set()
        
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
                    

class school_SchoolClass:

    def __init__(self, code: str, SchoolClass: "school_Course" = None, schoolClasses: "school_Year" = None, schoolClass: set["school_Student"] = None, schoolClass15: set["school_Course"] = None, homeroomedClass: "school_Teacher" = None, SchoolClass20: "school_Student" = None, SchoolClass32: "school_Year" = None, SchoolClass28: "school_Teacher" = None):
        self.code = code
        self.SchoolClass = SchoolClass
        self.schoolClasses = schoolClasses
        self.schoolClass = schoolClass if schoolClass is not None else set()
        self.schoolClass15 = schoolClass15 if schoolClass15 is not None else set()
        self.homeroomedClass = homeroomedClass
        self.SchoolClass20 = SchoolClass20
        self.SchoolClass32 = SchoolClass32
        self.SchoolClass28 = SchoolClass28
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def SchoolClass32(self):
        return self.__SchoolClass32

    @SchoolClass32.setter
    def SchoolClass32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_SchoolClass__SchoolClass32", None)
        self.__SchoolClass32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "year"):
                opp_val = getattr(old_value, "year", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "year"):
                opp_val = getattr(value, "year", None)
                if opp_val is None:
                    setattr(value, "year", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def schoolClass(self):
        return self.__schoolClass

    @schoolClass.setter
    def schoolClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_SchoolClass__schoolClass", None)
        self.__schoolClass = value if value is not None else set()
        
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
    def schoolClasses(self):
        return self.__schoolClasses

    @schoolClasses.setter
    def schoolClasses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_SchoolClass__schoolClasses", None)
        self.__schoolClasses = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Year12"):
                opp_val = getattr(old_value, "Year12", None)
                if opp_val == self:
                    setattr(old_value, "Year12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Year12"):
                opp_val = getattr(value, "Year12", None)
                setattr(value, "Year12", self)

    @property
    def SchoolClass28(self):
        return self.__SchoolClass28

    @SchoolClass28.setter
    def SchoolClass28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_SchoolClass__SchoolClass28", None)
        self.__SchoolClass28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "homeroomTeacher"):
                opp_val = getattr(old_value, "homeroomTeacher", None)
                if opp_val == self:
                    setattr(old_value, "homeroomTeacher", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "homeroomTeacher"):
                opp_val = getattr(value, "homeroomTeacher", None)
                setattr(value, "homeroomTeacher", self)

    @property
    def SchoolClass20(self):
        return self.__SchoolClass20

    @SchoolClass20.setter
    def SchoolClass20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_SchoolClass__SchoolClass20", None)
        self.__SchoolClass20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "students"):
                opp_val = getattr(old_value, "students", None)
                if opp_val == self:
                    setattr(old_value, "students", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "students"):
                opp_val = getattr(value, "students", None)
                setattr(value, "students", self)

    @property
    def SchoolClass(self):
        return self.__SchoolClass

    @SchoolClass.setter
    def SchoolClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_SchoolClass__SchoolClass", None)
        self.__SchoolClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courses4"):
                opp_val = getattr(old_value, "courses4", None)
                if opp_val == self:
                    setattr(old_value, "courses4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courses4"):
                opp_val = getattr(value, "courses4", None)
                setattr(value, "courses4", self)

    @property
    def homeroomedClass(self):
        return self.__homeroomedClass

    @homeroomedClass.setter
    def homeroomedClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_SchoolClass__homeroomedClass", None)
        self.__homeroomedClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Teacher18"):
                opp_val = getattr(old_value, "Teacher18", None)
                if opp_val == self:
                    setattr(old_value, "Teacher18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Teacher18"):
                opp_val = getattr(value, "Teacher18", None)
                setattr(value, "Teacher18", self)

    @property
    def schoolClass15(self):
        return self.__schoolClass15

    @schoolClass15.setter
    def schoolClass15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_SchoolClass__schoolClass15", None)
        self.__schoolClass15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Course16"):
                    opp_val = getattr(item, "Course16", None)
                    
                    if opp_val == self:
                        setattr(item, "Course16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Course16"):
                    opp_val = getattr(item, "Course16", None)
                    
                    setattr(item, "Course16", self)
                    

class school_Year:

    def __init__(self, startingDate: int, Year: "school_School" = None, Year12: "school_SchoolClass" = None, years: "school_School" = None, year: set["school_SchoolClass"] = None):
        self.startingDate = startingDate
        self.Year = Year
        self.Year12 = Year12
        self.years = years
        self.year = year if year is not None else set()
        
    @property
    def startingDate(self) -> int:
        return self.__startingDate

    @startingDate.setter
    def startingDate(self, startingDate: int):
        self.__startingDate = startingDate

    @property
    def Year12(self):
        return self.__Year12

    @Year12.setter
    def Year12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Year__Year12", None)
        self.__Year12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schoolClasses"):
                opp_val = getattr(old_value, "schoolClasses", None)
                if opp_val == self:
                    setattr(old_value, "schoolClasses", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schoolClasses"):
                opp_val = getattr(value, "schoolClasses", None)
                setattr(value, "schoolClasses", self)

    @property
    def Year(self):
        return self.__Year

    @Year.setter
    def Year(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Year__Year", None)
        self.__Year = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school"):
                opp_val = getattr(old_value, "school", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school"):
                opp_val = getattr(value, "school", None)
                if opp_val is None:
                    setattr(value, "school", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Year__year", None)
        self.__year = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SchoolClass32"):
                    opp_val = getattr(item, "SchoolClass32", None)
                    
                    if opp_val == self:
                        setattr(item, "SchoolClass32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SchoolClass32"):
                    opp_val = getattr(item, "SchoolClass32", None)
                    
                    setattr(item, "SchoolClass32", self)
                    

    @property
    def years(self):
        return self.__years

    @years.setter
    def years(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Year__years", None)
        self.__years = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "School30"):
                opp_val = getattr(old_value, "School30", None)
                if opp_val == self:
                    setattr(old_value, "School30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "School30"):
                opp_val = getattr(value, "School30", None)
                setattr(value, "School30", self)

class school_Teacher:

    def __init__(self, name: str, Teacher: "school_Course" = None, Teacher8: "school_School" = None, Teacher18: "school_SchoolClass" = None, teachers: "school_School" = None, teacher: set["school_Course"] = None, homeroomTeacher: "school_SchoolClass" = None):
        self.name = name
        self.Teacher = Teacher
        self.Teacher8 = Teacher8
        self.Teacher18 = Teacher18
        self.teachers = teachers
        self.teacher = teacher if teacher is not None else set()
        self.homeroomTeacher = homeroomTeacher
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Teacher8(self):
        return self.__Teacher8

    @Teacher8.setter
    def Teacher8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Teacher__Teacher8", None)
        self.__Teacher8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school7"):
                opp_val = getattr(old_value, "school7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school7"):
                opp_val = getattr(value, "school7", None)
                if opp_val is None:
                    setattr(value, "school7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Teacher18(self):
        return self.__Teacher18

    @Teacher18.setter
    def Teacher18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Teacher__Teacher18", None)
        self.__Teacher18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "homeroomedClass"):
                opp_val = getattr(old_value, "homeroomedClass", None)
                if opp_val == self:
                    setattr(old_value, "homeroomedClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "homeroomedClass"):
                opp_val = getattr(value, "homeroomedClass", None)
                setattr(value, "homeroomedClass", self)

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Teacher__teacher", None)
        self.__teacher = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Course26"):
                    opp_val = getattr(item, "Course26", None)
                    
                    if opp_val == self:
                        setattr(item, "Course26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Course26"):
                    opp_val = getattr(item, "Course26", None)
                    
                    setattr(item, "Course26", self)
                    

    @property
    def homeroomTeacher(self):
        return self.__homeroomTeacher

    @homeroomTeacher.setter
    def homeroomTeacher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Teacher__homeroomTeacher", None)
        self.__homeroomTeacher = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SchoolClass28"):
                opp_val = getattr(old_value, "SchoolClass28", None)
                if opp_val == self:
                    setattr(old_value, "SchoolClass28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SchoolClass28"):
                opp_val = getattr(value, "SchoolClass28", None)
                setattr(value, "SchoolClass28", self)

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
            if hasattr(old_value, "courses2"):
                opp_val = getattr(old_value, "courses2", None)
                if opp_val == self:
                    setattr(old_value, "courses2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courses2"):
                opp_val = getattr(value, "courses2", None)
                setattr(value, "courses2", self)

    @property
    def teachers(self):
        return self.__teachers

    @teachers.setter
    def teachers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Teacher__teachers", None)
        self.__teachers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "School24"):
                opp_val = getattr(old_value, "School24", None)
                if opp_val == self:
                    setattr(old_value, "School24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "School24"):
                opp_val = getattr(value, "School24", None)
                setattr(value, "School24", self)

class school_School:

    def __init__(self, name: str, address: str, School: "school_Course" = None, school: set["school_Year"] = None, school7: set["school_Teacher"] = None, school10: set["school_Course"] = None, School24: "school_Teacher" = None, School30: "school_Year" = None):
        self.name = name
        self.address = address
        self.School = School
        self.school = school if school is not None else set()
        self.school7 = school7 if school7 is not None else set()
        self.school10 = school10 if school10 is not None else set()
        self.School24 = School24
        self.School30 = School30
        
    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def School30(self):
        return self.__School30

    @School30.setter
    def School30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_School__School30", None)
        self.__School30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "years"):
                opp_val = getattr(old_value, "years", None)
                if opp_val == self:
                    setattr(old_value, "years", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "years"):
                opp_val = getattr(value, "years", None)
                setattr(value, "years", self)

    @property
    def School24(self):
        return self.__School24

    @School24.setter
    def School24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_School__School24", None)
        self.__School24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "teachers"):
                opp_val = getattr(old_value, "teachers", None)
                if opp_val == self:
                    setattr(old_value, "teachers", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "teachers"):
                opp_val = getattr(value, "teachers", None)
                setattr(value, "teachers", self)

    @property
    def school7(self):
        return self.__school7

    @school7.setter
    def school7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_School__school7", None)
        self.__school7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Teacher8"):
                    opp_val = getattr(item, "Teacher8", None)
                    
                    if opp_val == self:
                        setattr(item, "Teacher8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Teacher8"):
                    opp_val = getattr(item, "Teacher8", None)
                    
                    setattr(item, "Teacher8", self)
                    

    @property
    def school10(self):
        return self.__school10

    @school10.setter
    def school10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_School__school10", None)
        self.__school10 = value if value is not None else set()
        
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
    def School(self):
        return self.__School

    @School.setter
    def School(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_School__School", None)
        self.__School = value
        
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
    def school(self):
        return self.__school

    @school.setter
    def school(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_School__school", None)
        self.__school = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Year"):
                    opp_val = getattr(item, "Year", None)
                    
                    if opp_val == self:
                        setattr(item, "Year", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Year"):
                    opp_val = getattr(item, "Year", None)
                    
                    setattr(item, "Year", self)
                    

class school_Course:

    def __init__(self, subject: str, weight: int, courses: "school_School" = None, courses2: "school_Teacher" = None, courses4: "school_SchoolClass" = None, Course: "school_School" = None, Course16: "school_SchoolClass" = None, Course26: "school_Teacher" = None):
        self.subject = subject
        self.weight = weight
        self.courses = courses
        self.courses2 = courses2
        self.courses4 = courses4
        self.Course = Course
        self.Course16 = Course16
        self.Course26 = Course26
        
    @property
    def subject(self) -> str:
        return self.__subject

    @subject.setter
    def subject(self, subject: str):
        self.__subject = subject

    @property
    def weight(self) -> int:
        return self.__weight

    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

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
            if hasattr(old_value, "school10"):
                opp_val = getattr(old_value, "school10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school10"):
                opp_val = getattr(value, "school10", None)
                if opp_val is None:
                    setattr(value, "school10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Course26(self):
        return self.__Course26

    @Course26.setter
    def Course26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Course__Course26", None)
        self.__Course26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "teacher"):
                opp_val = getattr(old_value, "teacher", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "teacher"):
                opp_val = getattr(value, "teacher", None)
                if opp_val is None:
                    setattr(value, "teacher", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Course16(self):
        return self.__Course16

    @Course16.setter
    def Course16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Course__Course16", None)
        self.__Course16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schoolClass15"):
                opp_val = getattr(old_value, "schoolClass15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schoolClass15"):
                opp_val = getattr(value, "schoolClass15", None)
                if opp_val is None:
                    setattr(value, "schoolClass15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Course__courses", None)
        self.__courses = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "School"):
                opp_val = getattr(old_value, "School", None)
                if opp_val == self:
                    setattr(old_value, "School", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "School"):
                opp_val = getattr(value, "School", None)
                setattr(value, "School", self)

    @property
    def courses2(self):
        return self.__courses2

    @courses2.setter
    def courses2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Course__courses2", None)
        self.__courses2 = value
        
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
    def courses4(self):
        return self.__courses4

    @courses4.setter
    def courses4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Course__courses4", None)
        self.__courses4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SchoolClass"):
                opp_val = getattr(old_value, "SchoolClass", None)
                if opp_val == self:
                    setattr(old_value, "SchoolClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SchoolClass"):
                opp_val = getattr(value, "SchoolClass", None)
                setattr(value, "SchoolClass", self)
