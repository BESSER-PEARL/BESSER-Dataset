from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

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
            if hasattr(old_value, "SchoolClass24"):
                opp_val = getattr(old_value, "SchoolClass24", None)
                if opp_val == self:
                    setattr(old_value, "SchoolClass24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SchoolClass24"):
                opp_val = getattr(value, "SchoolClass24", None)
                setattr(value, "SchoolClass24", self)

class school_SchoolClass:

    def __init__(self, code: str, SchoolClass: "school_Course" = None, schoolClasses: "school_Year" = None, schoolClass: set["school_Student"] = None, schoolClass18: set["school_Course"] = None, homeroomedClass: "school_Teacher" = None, school_SchoolClass: set["school_Course"] = None, SchoolClass24: "school_Student" = None, SchoolClass30: "school_Teacher" = None, SchoolClass34: "school_Year" = None):
        self.code = code
        self.SchoolClass = SchoolClass
        self.schoolClasses = schoolClasses
        self.schoolClass = schoolClass if schoolClass is not None else set()
        self.schoolClass18 = schoolClass18 if schoolClass18 is not None else set()
        self.homeroomedClass = homeroomedClass
        self.school_SchoolClass = school_SchoolClass if school_SchoolClass is not None else set()
        self.SchoolClass24 = SchoolClass24
        self.SchoolClass30 = SchoolClass30
        self.SchoolClass34 = SchoolClass34
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def school_SchoolClass(self):
        return self.__school_SchoolClass

    @school_SchoolClass.setter
    def school_SchoolClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_SchoolClass__school_SchoolClass", None)
        self.__school_SchoolClass = value if value is not None else set()
        
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
    def SchoolClass30(self):
        return self.__SchoolClass30

    @SchoolClass30.setter
    def SchoolClass30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_SchoolClass__SchoolClass30", None)
        self.__SchoolClass30 = value
        
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
    def schoolClass18(self):
        return self.__schoolClass18

    @schoolClass18.setter
    def schoolClass18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_SchoolClass__schoolClass18", None)
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
    def schoolClasses(self):
        return self.__schoolClasses

    @schoolClasses.setter
    def schoolClasses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_SchoolClass__schoolClasses", None)
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
        old_value = getattr(self, f"_school_SchoolClass__SchoolClass34", None)
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
    def homeroomedClass(self):
        return self.__homeroomedClass

    @homeroomedClass.setter
    def homeroomedClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_SchoolClass__homeroomedClass", None)
        self.__homeroomedClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Teacher21"):
                opp_val = getattr(old_value, "Teacher21", None)
                if opp_val == self:
                    setattr(old_value, "Teacher21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Teacher21"):
                opp_val = getattr(value, "Teacher21", None)
                setattr(value, "Teacher21", self)

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
    def SchoolClass24(self):
        return self.__SchoolClass24

    @SchoolClass24.setter
    def SchoolClass24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_SchoolClass__SchoolClass24", None)
        self.__SchoolClass24 = value
        
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

class school_Year:

    def __init__(self, startingDate: int, weightOfRegularCourses: int, Year: "school_School" = None, school_Year: "school_School" = None, Year15: "school_SchoolClass" = None, years: "school_School" = None, year: set["school_SchoolClass"] = None):
        self.startingDate = startingDate
        self.weightOfRegularCourses = weightOfRegularCourses
        self.Year = Year
        self.school_Year = school_Year
        self.Year15 = Year15
        self.years = years
        self.year = year if year is not None else set()
        
    @property
    def weightOfRegularCourses(self) -> int:
        return self.__weightOfRegularCourses

    @weightOfRegularCourses.setter
    def weightOfRegularCourses(self, weightOfRegularCourses: int):
        self.__weightOfRegularCourses = weightOfRegularCourses

    @property
    def startingDate(self) -> int:
        return self.__startingDate

    @startingDate.setter
    def startingDate(self, startingDate: int):
        self.__startingDate = startingDate

    @property
    def school_Year(self):
        return self.__school_Year

    @school_Year.setter
    def school_Year(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Year__school_Year", None)
        self.__school_Year = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_School13"):
                opp_val = getattr(old_value, "school_School13", None)
                if opp_val == self:
                    setattr(old_value, "school_School13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_School13"):
                opp_val = getattr(value, "school_School13", None)
                setattr(value, "school_School13", self)

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
        old_value = getattr(self, f"_school_Year__Year15", None)
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

class school_Teacher:

    def __init__(self, name: str, Teacher8: "school_School" = None, school_Teacher: "school_School" = None, Teacher: "school_Course" = None, Teacher21: "school_SchoolClass" = None, teacher: set["school_Course"] = None, homeroomTeacher: "school_SchoolClass" = None, teachers: "school_School" = None):
        self.name = name
        self.Teacher8 = Teacher8
        self.school_Teacher = school_Teacher
        self.Teacher = Teacher
        self.Teacher21 = Teacher21
        self.teacher = teacher if teacher is not None else set()
        self.homeroomTeacher = homeroomTeacher
        self.teachers = teachers
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "SchoolClass30"):
                opp_val = getattr(old_value, "SchoolClass30", None)
                if opp_val == self:
                    setattr(old_value, "SchoolClass30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SchoolClass30"):
                opp_val = getattr(value, "SchoolClass30", None)
                setattr(value, "SchoolClass30", self)

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
    def teachers(self):
        return self.__teachers

    @teachers.setter
    def teachers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Teacher__teachers", None)
        self.__teachers = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "School26"):
                opp_val = getattr(old_value, "School26", None)
                if opp_val == self:
                    setattr(old_value, "School26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "School26"):
                opp_val = getattr(value, "School26", None)
                setattr(value, "School26", self)

    @property
    def Teacher21(self):
        return self.__Teacher21

    @Teacher21.setter
    def Teacher21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Teacher__Teacher21", None)
        self.__Teacher21 = value
        
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
                if hasattr(item, "Course28"):
                    opp_val = getattr(item, "Course28", None)
                    
                    if opp_val == self:
                        setattr(item, "Course28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Course28"):
                    opp_val = getattr(item, "Course28", None)
                    
                    setattr(item, "Course28", self)
                    

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

class school_School:

    def __init__(self, name: str, address: str, numberOfTeachers: int, currentYear: int, School: "school_Course" = None, school: set["school_Year"] = None, school7: set["school_Teacher"] = None, school10: set["school_Course"] = None, school_School: set["school_Teacher"] = None, school_School13: "school_Year" = None, School32: "school_Year" = None, School26: "school_Teacher" = None):
        self.name = name
        self.address = address
        self.numberOfTeachers = numberOfTeachers
        self.currentYear = currentYear
        self.School = School
        self.school = school if school is not None else set()
        self.school7 = school7 if school7 is not None else set()
        self.school10 = school10 if school10 is not None else set()
        self.school_School = school_School if school_School is not None else set()
        self.school_School13 = school_School13
        self.School32 = School32
        self.School26 = School26
        
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
    def School32(self):
        return self.__School32

    @School32.setter
    def School32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_School__School32", None)
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
    def School26(self):
        return self.__School26

    @School26.setter
    def School26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_School__School26", None)
        self.__School26 = value
        
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
    def school_School13(self):
        return self.__school_School13

    @school_School13.setter
    def school_School13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_School__school_School13", None)
        self.__school_School13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_Year"):
                opp_val = getattr(old_value, "school_Year", None)
                if opp_val == self:
                    setattr(old_value, "school_Year", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_Year"):
                opp_val = getattr(value, "school_Year", None)
                setattr(value, "school_Year", self)

class school_Course:

    def __init__(self, subject: str, weight: int, courses: "school_School" = None, courses4: "school_SchoolClass" = None, Course: "school_School" = None, courses2: "school_Teacher" = None, Course19: "school_SchoolClass" = None, school_Course: "school_SchoolClass" = None, Course28: "school_Teacher" = None):
        self.subject = subject
        self.weight = weight
        self.courses = courses
        self.courses4 = courses4
        self.Course = Course
        self.courses2 = courses2
        self.Course19 = Course19
        self.school_Course = school_Course
        self.Course28 = Course28
        
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
    def school_Course(self):
        return self.__school_Course

    @school_Course.setter
    def school_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Course__school_Course", None)
        self.__school_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_SchoolClass"):
                opp_val = getattr(old_value, "school_SchoolClass", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_SchoolClass"):
                opp_val = getattr(value, "school_SchoolClass", None)
                if opp_val is None:
                    setattr(value, "school_SchoolClass", set([self]))
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
    def Course19(self):
        return self.__Course19

    @Course19.setter
    def Course19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Course__Course19", None)
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
    def Course28(self):
        return self.__Course28

    @Course28.setter
    def Course28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Course__Course28", None)
        self.__Course28 = value
        
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
