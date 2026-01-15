from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class school_Student:

    def __init__(self, name: str, Student: "school_SchoolClass" = None, students: "school_SchoolClass" = None):
        self.name = name
        self.Student = Student
        self.students = students
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
    def students(self):
        return self.__students

    @students.setter
    def students(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Student__students", None)
        self.__students = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SchoolClass19"):
                opp_val = getattr(old_value, "SchoolClass19", None)
                if opp_val == self:
                    setattr(old_value, "SchoolClass19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SchoolClass19"):
                opp_val = getattr(value, "SchoolClass19", None)
                setattr(value, "SchoolClass19", self)

class Course:

    pass
class school_SpecialisationCourse(Course):

    def __init__(self, specialisation: str):
        self.specialisation = specialisation
        
    @property
    def specialisation(self) -> str:
        return self.__specialisation

    @specialisation.setter
    def specialisation(self, specialisation: str):
        self.__specialisation = specialisation

class school_Teacher:

    def __init__(self, name: str, Teacher: "school_Course" = None, Teacher8: "school_School" = None, school_Teacher: "school_SchoolClass" = None, school_Teacher25: "school_SchoolClass" = None, teachers: "school_School" = None, teacher: set["school_Course"] = None):
        self.name = name
        self.Teacher = Teacher
        self.Teacher8 = Teacher8
        self.school_Teacher = school_Teacher
        self.school_Teacher25 = school_Teacher25
        self.teachers = teachers
        self.teacher = teacher if teacher is not None else set()
        
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
    def teachers(self):
        return self.__teachers

    @teachers.setter
    def teachers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Teacher__teachers", None)
        self.__teachers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "School21"):
                opp_val = getattr(old_value, "School21", None)
                if opp_val == self:
                    setattr(old_value, "School21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "School21"):
                opp_val = getattr(value, "School21", None)
                setattr(value, "School21", self)

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
            if hasattr(old_value, "school_SchoolClass"):
                opp_val = getattr(old_value, "school_SchoolClass", None)
                if opp_val == self:
                    setattr(old_value, "school_SchoolClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_SchoolClass"):
                opp_val = getattr(value, "school_SchoolClass", None)
                setattr(value, "school_SchoolClass", self)

    @property
    def school_Teacher25(self):
        return self.__school_Teacher25

    @school_Teacher25.setter
    def school_Teacher25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Teacher__school_Teacher25", None)
        self.__school_Teacher25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_SchoolClass26"):
                opp_val = getattr(old_value, "school_SchoolClass26", None)
                if opp_val == self:
                    setattr(old_value, "school_SchoolClass26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_SchoolClass26"):
                opp_val = getattr(value, "school_SchoolClass26", None)
                setattr(value, "school_SchoolClass26", self)

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
                if hasattr(item, "Course23"):
                    opp_val = getattr(item, "Course23", None)
                    
                    if opp_val == self:
                        setattr(item, "Course23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Course23"):
                    opp_val = getattr(item, "Course23", None)
                    
                    setattr(item, "Course23", self)
                    

class school_School:

    def __init__(self, name: str, address: str, school: set["school_Year"] = None, school7: set["school_Teacher"] = None, school10: set["school_Course"] = None, School: "school_Course" = None, School28: "school_Year" = None, School21: "school_Teacher" = None):
        self.name = name
        self.address = address
        self.school = school if school is not None else set()
        self.school7 = school7 if school7 is not None else set()
        self.school10 = school10 if school10 is not None else set()
        self.School = School
        self.School28 = School28
        self.School21 = School21
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address: str):
        self.__address = address

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
    def School21(self):
        return self.__School21

    @School21.setter
    def School21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_School__School21", None)
        self.__School21 = value
        
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
    def School28(self):
        return self.__School28

    @School28.setter
    def School28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_School__School28", None)
        self.__School28 = value
        
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
                if hasattr(item, "SchoolClass30"):
                    opp_val = getattr(item, "SchoolClass30", None)
                    
                    if opp_val == self:
                        setattr(item, "SchoolClass30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SchoolClass30"):
                    opp_val = getattr(item, "SchoolClass30", None)
                    
                    setattr(item, "SchoolClass30", self)
                    

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
    def years(self):
        return self.__years

    @years.setter
    def years(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Year__years", None)
        self.__years = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "School28"):
                opp_val = getattr(old_value, "School28", None)
                if opp_val == self:
                    setattr(old_value, "School28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "School28"):
                opp_val = getattr(value, "School28", None)
                setattr(value, "School28", self)

class school_SchoolClass:

    def __init__(self, code: str, SchoolClass: "school_Course" = None, schoolClass: set["school_Student"] = None, schoolClass15: set["school_Course"] = None, school_SchoolClass: "school_Teacher" = None, SchoolClass19: "school_Student" = None, schoolClasses: "school_Year" = None, school_SchoolClass26: "school_Teacher" = None, SchoolClass30: "school_Year" = None):
        self.code = code
        self.SchoolClass = SchoolClass
        self.schoolClass = schoolClass if schoolClass is not None else set()
        self.schoolClass15 = schoolClass15 if schoolClass15 is not None else set()
        self.school_SchoolClass = school_SchoolClass
        self.SchoolClass19 = SchoolClass19
        self.schoolClasses = schoolClasses
        self.school_SchoolClass26 = school_SchoolClass26
        self.SchoolClass30 = SchoolClass30
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

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
    def SchoolClass19(self):
        return self.__SchoolClass19

    @SchoolClass19.setter
    def SchoolClass19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_SchoolClass__SchoolClass19", None)
        self.__SchoolClass19 = value
        
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
    def SchoolClass30(self):
        return self.__SchoolClass30

    @SchoolClass30.setter
    def SchoolClass30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_SchoolClass__SchoolClass30", None)
        self.__SchoolClass30 = value
        
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
    def school_SchoolClass(self):
        return self.__school_SchoolClass

    @school_SchoolClass.setter
    def school_SchoolClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_SchoolClass__school_SchoolClass", None)
        self.__school_SchoolClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_Teacher"):
                opp_val = getattr(old_value, "school_Teacher", None)
                if opp_val == self:
                    setattr(old_value, "school_Teacher", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_Teacher"):
                opp_val = getattr(value, "school_Teacher", None)
                setattr(value, "school_Teacher", self)

    @property
    def school_SchoolClass26(self):
        return self.__school_SchoolClass26

    @school_SchoolClass26.setter
    def school_SchoolClass26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_SchoolClass__school_SchoolClass26", None)
        self.__school_SchoolClass26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_Teacher25"):
                opp_val = getattr(old_value, "school_Teacher25", None)
                if opp_val == self:
                    setattr(old_value, "school_Teacher25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_Teacher25"):
                opp_val = getattr(value, "school_Teacher25", None)
                setattr(value, "school_Teacher25", self)

class school_Course:

    def __init__(self, subject: str, weight: int, courses2: "school_Teacher" = None, courses4: "school_SchoolClass" = None, Course: "school_School" = None, courses: "school_School" = None, Course16: "school_SchoolClass" = None, Course23: "school_Teacher" = None):
        self.subject = subject
        self.weight = weight
        self.courses2 = courses2
        self.courses4 = courses4
        self.Course = Course
        self.courses = courses
        self.Course16 = Course16
        self.Course23 = Course23
        
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

    @property
    def Course23(self):
        return self.__Course23

    @Course23.setter
    def Course23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Course__Course23", None)
        self.__Course23 = value
        
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
