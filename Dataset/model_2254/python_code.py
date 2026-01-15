from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Course:

    pass
class schoolIncqDerived_SpecialisationCourse(Course):

    def __init__(self, specialisation: str):
        self.specialisation = specialisation
        
    @property
    def specialisation(self) -> str:
        return self.__specialisation

    @specialisation.setter
    def specialisation(self, specialisation: str):
        self.__specialisation = specialisation

class schoolIncqDerived_Student:

    def __init__(self, name: str, Student: "schoolIncqDerived_SchoolClass" = None, students: "schoolIncqDerived_SchoolClass" = None):
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
        old_value = getattr(self, f"_schoolIncqDerived_Student__Student", None)
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
        old_value = getattr(self, f"_schoolIncqDerived_Student__students", None)
        self.__students = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SchoolClass23"):
                opp_val = getattr(old_value, "SchoolClass23", None)
                if opp_val == self:
                    setattr(old_value, "SchoolClass23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SchoolClass23"):
                opp_val = getattr(value, "SchoolClass23", None)
                setattr(value, "SchoolClass23", self)

class schoolIncqDerived_School:

    def __init__(self, name: str, address: str, currentYear: int, numberOfTeachers: int, school: set["schoolIncqDerived_Year"] = None, school7: set["schoolIncqDerived_Teacher"] = None, school10: set["schoolIncqDerived_Course"] = None, School: "schoolIncqDerived_Course" = None, schoolIncqDerived_School: set["schoolIncqDerived_Teacher"] = None, schoolIncqDerived_School13: "schoolIncqDerived_Year" = None, School25: "schoolIncqDerived_Teacher" = None, School32: "schoolIncqDerived_Year" = None):
        self.name = name
        self.address = address
        self.currentYear = currentYear
        self.numberOfTeachers = numberOfTeachers
        self.school = school if school is not None else set()
        self.school7 = school7 if school7 is not None else set()
        self.school10 = school10 if school10 is not None else set()
        self.School = School
        self.schoolIncqDerived_School = schoolIncqDerived_School if schoolIncqDerived_School is not None else set()
        self.schoolIncqDerived_School13 = schoolIncqDerived_School13
        self.School25 = School25
        self.School32 = School32
        
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
    def currentYear(self) -> int:
        return self.__currentYear

    @currentYear.setter
    def currentYear(self, currentYear: int):
        self.__currentYear = currentYear

    @property
    def numberOfTeachers(self) -> int:
        return self.__numberOfTeachers

    @numberOfTeachers.setter
    def numberOfTeachers(self, numberOfTeachers: int):
        self.__numberOfTeachers = numberOfTeachers

    @property
    def School25(self):
        return self.__School25

    @School25.setter
    def School25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schoolIncqDerived_School__School25", None)
        self.__School25 = value
        
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
    def School(self):
        return self.__School

    @School.setter
    def School(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schoolIncqDerived_School__School", None)
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
        old_value = getattr(self, f"_schoolIncqDerived_School__school", None)
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
    def School32(self):
        return self.__School32

    @School32.setter
    def School32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schoolIncqDerived_School__School32", None)
        self.__School32 = value
        
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
    def schoolIncqDerived_School(self):
        return self.__schoolIncqDerived_School

    @schoolIncqDerived_School.setter
    def schoolIncqDerived_School(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schoolIncqDerived_School__schoolIncqDerived_School", None)
        self.__schoolIncqDerived_School = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "schoolIncqDerived_Teacher"):
                    opp_val = getattr(item, "schoolIncqDerived_Teacher", None)
                    
                    if opp_val == self:
                        setattr(item, "schoolIncqDerived_Teacher", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "schoolIncqDerived_Teacher"):
                    opp_val = getattr(item, "schoolIncqDerived_Teacher", None)
                    
                    setattr(item, "schoolIncqDerived_Teacher", self)
                    

    @property
    def school7(self):
        return self.__school7

    @school7.setter
    def school7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schoolIncqDerived_School__school7", None)
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
        old_value = getattr(self, f"_schoolIncqDerived_School__school10", None)
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
    def schoolIncqDerived_School13(self):
        return self.__schoolIncqDerived_School13

    @schoolIncqDerived_School13.setter
    def schoolIncqDerived_School13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schoolIncqDerived_School__schoolIncqDerived_School13", None)
        self.__schoolIncqDerived_School13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schoolIncqDerived_Year"):
                opp_val = getattr(old_value, "schoolIncqDerived_Year", None)
                if opp_val == self:
                    setattr(old_value, "schoolIncqDerived_Year", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schoolIncqDerived_Year"):
                opp_val = getattr(value, "schoolIncqDerived_Year", None)
                setattr(value, "schoolIncqDerived_Year", self)

class schoolIncqDerived_Year:

    def __init__(self, startingDate: int, Year: "schoolIncqDerived_School" = None, Year15: "schoolIncqDerived_SchoolClass" = None, schoolIncqDerived_Year: "schoolIncqDerived_School" = None, years: "schoolIncqDerived_School" = None, year: set["schoolIncqDerived_SchoolClass"] = None):
        self.startingDate = startingDate
        self.Year = Year
        self.Year15 = Year15
        self.schoolIncqDerived_Year = schoolIncqDerived_Year
        self.years = years
        self.year = year if year is not None else set()
        
    @property
    def startingDate(self) -> int:
        return self.__startingDate

    @startingDate.setter
    def startingDate(self, startingDate: int):
        self.__startingDate = startingDate

    @property
    def schoolIncqDerived_Year(self):
        return self.__schoolIncqDerived_Year

    @schoolIncqDerived_Year.setter
    def schoolIncqDerived_Year(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schoolIncqDerived_Year__schoolIncqDerived_Year", None)
        self.__schoolIncqDerived_Year = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schoolIncqDerived_School13"):
                opp_val = getattr(old_value, "schoolIncqDerived_School13", None)
                if opp_val == self:
                    setattr(old_value, "schoolIncqDerived_School13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schoolIncqDerived_School13"):
                opp_val = getattr(value, "schoolIncqDerived_School13", None)
                setattr(value, "schoolIncqDerived_School13", self)

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schoolIncqDerived_Year__year", None)
        self.__year = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SchoolClass34"):
                    opp_val = getattr(item, "SchoolClass34", None)
                    
                    if opp_val == self:
                        setattr(item, "SchoolClass34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SchoolClass34"):
                    opp_val = getattr(item, "SchoolClass34", None)
                    
                    setattr(item, "SchoolClass34", self)
                    

    @property
    def years(self):
        return self.__years

    @years.setter
    def years(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schoolIncqDerived_Year__years", None)
        self.__years = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "School32"):
                opp_val = getattr(old_value, "School32", None)
                if opp_val == self:
                    setattr(old_value, "School32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "School32"):
                opp_val = getattr(value, "School32", None)
                setattr(value, "School32", self)

    @property
    def Year15(self):
        return self.__Year15

    @Year15.setter
    def Year15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schoolIncqDerived_Year__Year15", None)
        self.__Year15 = value
        
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
        old_value = getattr(self, f"_schoolIncqDerived_Year__Year", None)
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

class schoolIncqDerived_SchoolClass:

    def __init__(self, code: str, SchoolClass: "schoolIncqDerived_Course" = None, schoolClasses: "schoolIncqDerived_Year" = None, schoolClass: set["schoolIncqDerived_Student"] = None, schoolClass18: set["schoolIncqDerived_Course"] = None, schoolIncqDerived_SchoolClass: "schoolIncqDerived_Teacher" = None, schoolIncqDerived_SchoolClass30: "schoolIncqDerived_Teacher" = None, SchoolClass34: "schoolIncqDerived_Year" = None, SchoolClass23: "schoolIncqDerived_Student" = None):
        self.code = code
        self.SchoolClass = SchoolClass
        self.schoolClasses = schoolClasses
        self.schoolClass = schoolClass if schoolClass is not None else set()
        self.schoolClass18 = schoolClass18 if schoolClass18 is not None else set()
        self.schoolIncqDerived_SchoolClass = schoolIncqDerived_SchoolClass
        self.schoolIncqDerived_SchoolClass30 = schoolIncqDerived_SchoolClass30
        self.SchoolClass34 = SchoolClass34
        self.SchoolClass23 = SchoolClass23
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def SchoolClass23(self):
        return self.__SchoolClass23

    @SchoolClass23.setter
    def SchoolClass23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schoolIncqDerived_SchoolClass__SchoolClass23", None)
        self.__SchoolClass23 = value
        
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
    def schoolClass18(self):
        return self.__schoolClass18

    @schoolClass18.setter
    def schoolClass18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schoolIncqDerived_SchoolClass__schoolClass18", None)
        self.__schoolClass18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Course19"):
                    opp_val = getattr(item, "Course19", None)
                    
                    if opp_val == self:
                        setattr(item, "Course19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Course19"):
                    opp_val = getattr(item, "Course19", None)
                    
                    setattr(item, "Course19", self)
                    

    @property
    def schoolIncqDerived_SchoolClass(self):
        return self.__schoolIncqDerived_SchoolClass

    @schoolIncqDerived_SchoolClass.setter
    def schoolIncqDerived_SchoolClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schoolIncqDerived_SchoolClass__schoolIncqDerived_SchoolClass", None)
        self.__schoolIncqDerived_SchoolClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schoolIncqDerived_Teacher21"):
                opp_val = getattr(old_value, "schoolIncqDerived_Teacher21", None)
                if opp_val == self:
                    setattr(old_value, "schoolIncqDerived_Teacher21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schoolIncqDerived_Teacher21"):
                opp_val = getattr(value, "schoolIncqDerived_Teacher21", None)
                setattr(value, "schoolIncqDerived_Teacher21", self)

    @property
    def schoolIncqDerived_SchoolClass30(self):
        return self.__schoolIncqDerived_SchoolClass30

    @schoolIncqDerived_SchoolClass30.setter
    def schoolIncqDerived_SchoolClass30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schoolIncqDerived_SchoolClass__schoolIncqDerived_SchoolClass30", None)
        self.__schoolIncqDerived_SchoolClass30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schoolIncqDerived_Teacher29"):
                opp_val = getattr(old_value, "schoolIncqDerived_Teacher29", None)
                if opp_val == self:
                    setattr(old_value, "schoolIncqDerived_Teacher29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schoolIncqDerived_Teacher29"):
                opp_val = getattr(value, "schoolIncqDerived_Teacher29", None)
                setattr(value, "schoolIncqDerived_Teacher29", self)

    @property
    def schoolClasses(self):
        return self.__schoolClasses

    @schoolClasses.setter
    def schoolClasses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schoolIncqDerived_SchoolClass__schoolClasses", None)
        self.__schoolClasses = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Year15"):
                opp_val = getattr(old_value, "Year15", None)
                if opp_val == self:
                    setattr(old_value, "Year15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Year15"):
                opp_val = getattr(value, "Year15", None)
                setattr(value, "Year15", self)

    @property
    def SchoolClass34(self):
        return self.__SchoolClass34

    @SchoolClass34.setter
    def SchoolClass34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schoolIncqDerived_SchoolClass__SchoolClass34", None)
        self.__SchoolClass34 = value
        
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
        old_value = getattr(self, f"_schoolIncqDerived_SchoolClass__schoolClass", None)
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
    def SchoolClass(self):
        return self.__SchoolClass

    @SchoolClass.setter
    def SchoolClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schoolIncqDerived_SchoolClass__SchoolClass", None)
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

class schoolIncqDerived_Teacher:

    def __init__(self, name: str, Teacher: "schoolIncqDerived_Course" = None, Teacher8: "schoolIncqDerived_School" = None, schoolIncqDerived_Teacher21: "schoolIncqDerived_SchoolClass" = None, schoolIncqDerived_Teacher: "schoolIncqDerived_School" = None, teachers: "schoolIncqDerived_School" = None, teacher: set["schoolIncqDerived_Course"] = None, schoolIncqDerived_Teacher29: "schoolIncqDerived_SchoolClass" = None):
        self.name = name
        self.Teacher = Teacher
        self.Teacher8 = Teacher8
        self.schoolIncqDerived_Teacher21 = schoolIncqDerived_Teacher21
        self.schoolIncqDerived_Teacher = schoolIncqDerived_Teacher
        self.teachers = teachers
        self.teacher = teacher if teacher is not None else set()
        self.schoolIncqDerived_Teacher29 = schoolIncqDerived_Teacher29
        
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
        old_value = getattr(self, f"_schoolIncqDerived_Teacher__Teacher", None)
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
        old_value = getattr(self, f"_schoolIncqDerived_Teacher__Teacher8", None)
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
    def schoolIncqDerived_Teacher21(self):
        return self.__schoolIncqDerived_Teacher21

    @schoolIncqDerived_Teacher21.setter
    def schoolIncqDerived_Teacher21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schoolIncqDerived_Teacher__schoolIncqDerived_Teacher21", None)
        self.__schoolIncqDerived_Teacher21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schoolIncqDerived_SchoolClass"):
                opp_val = getattr(old_value, "schoolIncqDerived_SchoolClass", None)
                if opp_val == self:
                    setattr(old_value, "schoolIncqDerived_SchoolClass", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schoolIncqDerived_SchoolClass"):
                opp_val = getattr(value, "schoolIncqDerived_SchoolClass", None)
                setattr(value, "schoolIncqDerived_SchoolClass", self)

    @property
    def teachers(self):
        return self.__teachers

    @teachers.setter
    def teachers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schoolIncqDerived_Teacher__teachers", None)
        self.__teachers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "School25"):
                opp_val = getattr(old_value, "School25", None)
                if opp_val == self:
                    setattr(old_value, "School25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "School25"):
                opp_val = getattr(value, "School25", None)
                setattr(value, "School25", self)

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schoolIncqDerived_Teacher__teacher", None)
        self.__teacher = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Course27"):
                    opp_val = getattr(item, "Course27", None)
                    
                    if opp_val == self:
                        setattr(item, "Course27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Course27"):
                    opp_val = getattr(item, "Course27", None)
                    
                    setattr(item, "Course27", self)
                    

    @property
    def schoolIncqDerived_Teacher29(self):
        return self.__schoolIncqDerived_Teacher29

    @schoolIncqDerived_Teacher29.setter
    def schoolIncqDerived_Teacher29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schoolIncqDerived_Teacher__schoolIncqDerived_Teacher29", None)
        self.__schoolIncqDerived_Teacher29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schoolIncqDerived_SchoolClass30"):
                opp_val = getattr(old_value, "schoolIncqDerived_SchoolClass30", None)
                if opp_val == self:
                    setattr(old_value, "schoolIncqDerived_SchoolClass30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schoolIncqDerived_SchoolClass30"):
                opp_val = getattr(value, "schoolIncqDerived_SchoolClass30", None)
                setattr(value, "schoolIncqDerived_SchoolClass30", self)

    @property
    def schoolIncqDerived_Teacher(self):
        return self.__schoolIncqDerived_Teacher

    @schoolIncqDerived_Teacher.setter
    def schoolIncqDerived_Teacher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schoolIncqDerived_Teacher__schoolIncqDerived_Teacher", None)
        self.__schoolIncqDerived_Teacher = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schoolIncqDerived_School"):
                opp_val = getattr(old_value, "schoolIncqDerived_School", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schoolIncqDerived_School"):
                opp_val = getattr(value, "schoolIncqDerived_School", None)
                if opp_val is None:
                    setattr(value, "schoolIncqDerived_School", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class schoolIncqDerived_Course:

    def __init__(self, subject: str, weight: int, courses2: "schoolIncqDerived_Teacher" = None, courses4: "schoolIncqDerived_SchoolClass" = None, Course: "schoolIncqDerived_School" = None, courses: "schoolIncqDerived_School" = None, Course19: "schoolIncqDerived_SchoolClass" = None, Course27: "schoolIncqDerived_Teacher" = None):
        self.subject = subject
        self.weight = weight
        self.courses2 = courses2
        self.courses4 = courses4
        self.Course = Course
        self.courses = courses
        self.Course19 = Course19
        self.Course27 = Course27
        
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
        old_value = getattr(self, f"_schoolIncqDerived_Course__Course", None)
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
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schoolIncqDerived_Course__courses", None)
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
        old_value = getattr(self, f"_schoolIncqDerived_Course__courses2", None)
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
    def Course19(self):
        return self.__Course19

    @Course19.setter
    def Course19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schoolIncqDerived_Course__Course19", None)
        self.__Course19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "schoolClass18"):
                opp_val = getattr(old_value, "schoolClass18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "schoolClass18"):
                opp_val = getattr(value, "schoolClass18", None)
                if opp_val is None:
                    setattr(value, "schoolClass18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def courses4(self):
        return self.__courses4

    @courses4.setter
    def courses4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schoolIncqDerived_Course__courses4", None)
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
    def Course27(self):
        return self.__Course27

    @Course27.setter
    def Course27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_schoolIncqDerived_Course__Course27", None)
        self.__Course27 = value
        
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
