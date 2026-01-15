from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class CourseStatus(Enum):
    mandatory = "mandatory"
    elective = "elective"
class Grade(Enum):
    E = "E"
    F = "F"
    A = "A"
    B = "B"
    C = "C"
    D = "D"
class Season(Enum):
    fall = "fall"
    spring = "spring"


############################################
# Definition of Classes
############################################

class studyProgramStructure_StudyPlan:

    pass
class studyProgramStructure_Student:

    def __init__(self, name: str, studyProgramStructure_Student29: "studyProgramStructure_Program" = None, studyProgramStructure_Student32: set["studyProgramStructure_Specialization"] = None, Student: "studyProgramStructure_StudyPlan" = None, studyProgramStructure_Student: "studyProgramStructure_University" = None, student: "studyProgramStructure_StudyPlan" = None):
        self.name = name
        self.studyProgramStructure_Student29 = studyProgramStructure_Student29
        self.studyProgramStructure_Student32 = studyProgramStructure_Student32 if studyProgramStructure_Student32 is not None else set()
        self.Student = Student
        self.studyProgramStructure_Student = studyProgramStructure_Student
        self.student = student
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def student(self):
        return self.__student

    @student.setter
    def student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyProgramStructure_Student__student", None)
        self.__student = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StudyPlan"):
                opp_val = getattr(old_value, "StudyPlan", None)
                if opp_val == self:
                    setattr(old_value, "StudyPlan", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StudyPlan"):
                opp_val = getattr(value, "StudyPlan", None)
                setattr(value, "StudyPlan", self)

    @property
    def Student(self):
        return self.__Student

    @Student.setter
    def Student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyProgramStructure_Student__Student", None)
        self.__Student = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyPlan"):
                opp_val = getattr(old_value, "studyPlan", None)
                if opp_val == self:
                    setattr(old_value, "studyPlan", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyPlan"):
                opp_val = getattr(value, "studyPlan", None)
                setattr(value, "studyPlan", self)

    @property
    def studyProgramStructure_Student(self):
        return self.__studyProgramStructure_Student

    @studyProgramStructure_Student.setter
    def studyProgramStructure_Student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyProgramStructure_Student__studyProgramStructure_Student", None)
        self.__studyProgramStructure_Student = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyProgramStructure_University26"):
                opp_val = getattr(old_value, "studyProgramStructure_University26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyProgramStructure_University26"):
                opp_val = getattr(value, "studyProgramStructure_University26", None)
                if opp_val is None:
                    setattr(value, "studyProgramStructure_University26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def studyProgramStructure_Student29(self):
        return self.__studyProgramStructure_Student29

    @studyProgramStructure_Student29.setter
    def studyProgramStructure_Student29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyProgramStructure_Student__studyProgramStructure_Student29", None)
        self.__studyProgramStructure_Student29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyProgramStructure_Program30"):
                opp_val = getattr(old_value, "studyProgramStructure_Program30", None)
                if opp_val == self:
                    setattr(old_value, "studyProgramStructure_Program30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyProgramStructure_Program30"):
                opp_val = getattr(value, "studyProgramStructure_Program30", None)
                setattr(value, "studyProgramStructure_Program30", self)

    @property
    def studyProgramStructure_Student32(self):
        return self.__studyProgramStructure_Student32

    @studyProgramStructure_Student32.setter
    def studyProgramStructure_Student32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyProgramStructure_Student__studyProgramStructure_Student32", None)
        self.__studyProgramStructure_Student32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "studyProgramStructure_Specialization"):
                    opp_val = getattr(item, "studyProgramStructure_Specialization", None)
                    
                    if opp_val == self:
                        setattr(item, "studyProgramStructure_Specialization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "studyProgramStructure_Specialization"):
                    opp_val = getattr(item, "studyProgramStructure_Specialization", None)
                    
                    setattr(item, "studyProgramStructure_Specialization", self)
                    

class studyProgramStructure_CourseAllocation:

    def __init__(self, grade: str, studyProgramStructure_CourseAllocation: "studyProgramStructure_StudyPlan" = None, studyProgramStructure_CourseAllocation38: "studyProgramStructure_Course" = None):
        self.grade = grade
        self.studyProgramStructure_CourseAllocation = studyProgramStructure_CourseAllocation
        self.studyProgramStructure_CourseAllocation38 = studyProgramStructure_CourseAllocation38
        
    @property
    def grade(self) -> str:
        return self.__grade

    @grade.setter
    def grade(self, grade: str):
        self.__grade = grade

    @property
    def studyProgramStructure_CourseAllocation38(self):
        return self.__studyProgramStructure_CourseAllocation38

    @studyProgramStructure_CourseAllocation38.setter
    def studyProgramStructure_CourseAllocation38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyProgramStructure_CourseAllocation__studyProgramStructure_CourseAllocation38", None)
        self.__studyProgramStructure_CourseAllocation38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyProgramStructure_Course39"):
                opp_val = getattr(old_value, "studyProgramStructure_Course39", None)
                if opp_val == self:
                    setattr(old_value, "studyProgramStructure_Course39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyProgramStructure_Course39"):
                opp_val = getattr(value, "studyProgramStructure_Course39", None)
                setattr(value, "studyProgramStructure_Course39", self)

    @property
    def studyProgramStructure_CourseAllocation(self):
        return self.__studyProgramStructure_CourseAllocation

    @studyProgramStructure_CourseAllocation.setter
    def studyProgramStructure_CourseAllocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyProgramStructure_CourseAllocation__studyProgramStructure_CourseAllocation", None)
        self.__studyProgramStructure_CourseAllocation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyProgramStructure_StudyPlan35"):
                opp_val = getattr(old_value, "studyProgramStructure_StudyPlan35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyProgramStructure_StudyPlan35"):
                opp_val = getattr(value, "studyProgramStructure_StudyPlan35", None)
                if opp_val is None:
                    setattr(value, "studyProgramStructure_StudyPlan35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class studyProgramStructure_University:

    def __init__(self, name: str, studyProgramStructure_University: set["studyProgramStructure_Program"] = None, studyProgramStructure_University23: set["studyProgramStructure_Course"] = None, studyProgramStructure_University26: set["studyProgramStructure_Student"] = None):
        self.name = name
        self.studyProgramStructure_University = studyProgramStructure_University if studyProgramStructure_University is not None else set()
        self.studyProgramStructure_University23 = studyProgramStructure_University23 if studyProgramStructure_University23 is not None else set()
        self.studyProgramStructure_University26 = studyProgramStructure_University26 if studyProgramStructure_University26 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def studyProgramStructure_University23(self):
        return self.__studyProgramStructure_University23

    @studyProgramStructure_University23.setter
    def studyProgramStructure_University23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyProgramStructure_University__studyProgramStructure_University23", None)
        self.__studyProgramStructure_University23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "studyProgramStructure_Course24"):
                    opp_val = getattr(item, "studyProgramStructure_Course24", None)
                    
                    if opp_val == self:
                        setattr(item, "studyProgramStructure_Course24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "studyProgramStructure_Course24"):
                    opp_val = getattr(item, "studyProgramStructure_Course24", None)
                    
                    setattr(item, "studyProgramStructure_Course24", self)
                    

    @property
    def studyProgramStructure_University26(self):
        return self.__studyProgramStructure_University26

    @studyProgramStructure_University26.setter
    def studyProgramStructure_University26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyProgramStructure_University__studyProgramStructure_University26", None)
        self.__studyProgramStructure_University26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "studyProgramStructure_Student"):
                    opp_val = getattr(item, "studyProgramStructure_Student", None)
                    
                    if opp_val == self:
                        setattr(item, "studyProgramStructure_Student", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "studyProgramStructure_Student"):
                    opp_val = getattr(item, "studyProgramStructure_Student", None)
                    
                    setattr(item, "studyProgramStructure_Student", self)
                    

    @property
    def studyProgramStructure_University(self):
        return self.__studyProgramStructure_University

    @studyProgramStructure_University.setter
    def studyProgramStructure_University(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyProgramStructure_University__studyProgramStructure_University", None)
        self.__studyProgramStructure_University = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "studyProgramStructure_Program"):
                    opp_val = getattr(item, "studyProgramStructure_Program", None)
                    
                    if opp_val == self:
                        setattr(item, "studyProgramStructure_Program", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "studyProgramStructure_Program"):
                    opp_val = getattr(item, "studyProgramStructure_Program", None)
                    
                    setattr(item, "studyProgramStructure_Program", self)
                    

class studyProgramStructure_CourseGroup:

    def __init__(self, name: str, status: str, CourseGroup: "studyProgramStructure_Semester" = None, courseGroups: "studyProgramStructure_Semester" = None, studyProgramStructure_CourseGroup: set["studyProgramStructure_Course"] = None):
        self.name = name
        self.status = status
        self.CourseGroup = CourseGroup
        self.courseGroups = courseGroups
        self.studyProgramStructure_CourseGroup = studyProgramStructure_CourseGroup if studyProgramStructure_CourseGroup is not None else set()
        
    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def studyProgramStructure_CourseGroup(self):
        return self.__studyProgramStructure_CourseGroup

    @studyProgramStructure_CourseGroup.setter
    def studyProgramStructure_CourseGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyProgramStructure_CourseGroup__studyProgramStructure_CourseGroup", None)
        self.__studyProgramStructure_CourseGroup = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "studyProgramStructure_Course"):
                    opp_val = getattr(item, "studyProgramStructure_Course", None)
                    
                    if opp_val == self:
                        setattr(item, "studyProgramStructure_Course", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "studyProgramStructure_Course"):
                    opp_val = getattr(item, "studyProgramStructure_Course", None)
                    
                    setattr(item, "studyProgramStructure_Course", self)
                    

    @property
    def courseGroups(self):
        return self.__courseGroups

    @courseGroups.setter
    def courseGroups(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyProgramStructure_CourseGroup__courseGroups", None)
        self.__courseGroups = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Semester19"):
                opp_val = getattr(old_value, "Semester19", None)
                if opp_val == self:
                    setattr(old_value, "Semester19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Semester19"):
                opp_val = getattr(value, "Semester19", None)
                setattr(value, "Semester19", self)

    @property
    def CourseGroup(self):
        return self.__CourseGroup

    @CourseGroup.setter
    def CourseGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyProgramStructure_CourseGroup__CourseGroup", None)
        self.__CourseGroup = value
        
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

class studyProgramStructure_Semester:

    def __init__(self, year: int, season: str, Semester: "studyProgramStructure_Program" = None, Semester10: "studyProgramStructure_Specialization" = None, semester: set["studyProgramStructure_CourseGroup"] = None, semesters: "studyProgramStructure_Program" = None, Semester19: "studyProgramStructure_CourseGroup" = None, semesters16: "studyProgramStructure_Specialization" = None, studyProgramStructure_Semester: "studyProgramStructure_StudyPlan" = None):
        self.year = year
        self.season = season
        self.Semester = Semester
        self.Semester10 = Semester10
        self.semester = semester if semester is not None else set()
        self.semesters = semesters
        self.Semester19 = Semester19
        self.semesters16 = semesters16
        self.studyProgramStructure_Semester = studyProgramStructure_Semester
        
    @property
    def season(self) -> str:
        return self.__season

    @season.setter
    def season(self, season: str):
        self.__season = season

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def Semester10(self):
        return self.__Semester10

    @Semester10.setter
    def Semester10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyProgramStructure_Semester__Semester10", None)
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
    def semesters16(self):
        return self.__semesters16

    @semesters16.setter
    def semesters16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyProgramStructure_Semester__semesters16", None)
        self.__semesters16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Specialization17"):
                opp_val = getattr(old_value, "Specialization17", None)
                if opp_val == self:
                    setattr(old_value, "Specialization17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Specialization17"):
                opp_val = getattr(value, "Specialization17", None)
                setattr(value, "Specialization17", self)

    @property
    def semester(self):
        return self.__semester

    @semester.setter
    def semester(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyProgramStructure_Semester__semester", None)
        self.__semester = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CourseGroup"):
                    opp_val = getattr(item, "CourseGroup", None)
                    
                    if opp_val == self:
                        setattr(item, "CourseGroup", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CourseGroup"):
                    opp_val = getattr(item, "CourseGroup", None)
                    
                    setattr(item, "CourseGroup", self)
                    

    @property
    def semesters(self):
        return self.__semesters

    @semesters.setter
    def semesters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyProgramStructure_Semester__semesters", None)
        self.__semesters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Program14"):
                opp_val = getattr(old_value, "Program14", None)
                if opp_val == self:
                    setattr(old_value, "Program14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Program14"):
                opp_val = getattr(value, "Program14", None)
                setattr(value, "Program14", self)

    @property
    def Semester(self):
        return self.__Semester

    @Semester.setter
    def Semester(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyProgramStructure_Semester__Semester", None)
        self.__Semester = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "program2"):
                opp_val = getattr(old_value, "program2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "program2"):
                opp_val = getattr(value, "program2", None)
                if opp_val is None:
                    setattr(value, "program2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def studyProgramStructure_Semester(self):
        return self.__studyProgramStructure_Semester

    @studyProgramStructure_Semester.setter
    def studyProgramStructure_Semester(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyProgramStructure_Semester__studyProgramStructure_Semester", None)
        self.__studyProgramStructure_Semester = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyProgramStructure_StudyPlan"):
                opp_val = getattr(old_value, "studyProgramStructure_StudyPlan", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyProgramStructure_StudyPlan"):
                opp_val = getattr(value, "studyProgramStructure_StudyPlan", None)
                if opp_val is None:
                    setattr(value, "studyProgramStructure_StudyPlan", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Semester19(self):
        return self.__Semester19

    @Semester19.setter
    def Semester19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyProgramStructure_Semester__Semester19", None)
        self.__Semester19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courseGroups"):
                opp_val = getattr(old_value, "courseGroups", None)
                if opp_val == self:
                    setattr(old_value, "courseGroups", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courseGroups"):
                opp_val = getattr(value, "courseGroups", None)
                setattr(value, "courseGroups", self)

class studyProgramStructure_Specialization:

    def __init__(self, name: str, numOfSemesters: int, Specialization: "studyProgramStructure_Program" = None, Specialization5: "studyProgramStructure_Specialization" = None, baseSpecialization: set["studyProgramStructure_Specialization"] = None, Specialization8: "studyProgramStructure_Specialization" = None, furtherSpecializations: "studyProgramStructure_Specialization" = None, specialization: set["studyProgramStructure_Semester"] = None, specializations: "studyProgramStructure_Program" = None, Specialization17: "studyProgramStructure_Semester" = None, studyProgramStructure_Specialization: "studyProgramStructure_Student" = None):
        self.name = name
        self.numOfSemesters = numOfSemesters
        self.Specialization = Specialization
        self.Specialization5 = Specialization5
        self.baseSpecialization = baseSpecialization if baseSpecialization is not None else set()
        self.Specialization8 = Specialization8
        self.furtherSpecializations = furtherSpecializations
        self.specialization = specialization if specialization is not None else set()
        self.specializations = specializations
        self.Specialization17 = Specialization17
        self.studyProgramStructure_Specialization = studyProgramStructure_Specialization
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def numOfSemesters(self) -> int:
        return self.__numOfSemesters

    @numOfSemesters.setter
    def numOfSemesters(self, numOfSemesters: int):
        self.__numOfSemesters = numOfSemesters

    @property
    def studyProgramStructure_Specialization(self):
        return self.__studyProgramStructure_Specialization

    @studyProgramStructure_Specialization.setter
    def studyProgramStructure_Specialization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyProgramStructure_Specialization__studyProgramStructure_Specialization", None)
        self.__studyProgramStructure_Specialization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyProgramStructure_Student32"):
                opp_val = getattr(old_value, "studyProgramStructure_Student32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyProgramStructure_Student32"):
                opp_val = getattr(value, "studyProgramStructure_Student32", None)
                if opp_val is None:
                    setattr(value, "studyProgramStructure_Student32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Specialization5(self):
        return self.__Specialization5

    @Specialization5.setter
    def Specialization5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyProgramStructure_Specialization__Specialization5", None)
        self.__Specialization5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "baseSpecialization"):
                opp_val = getattr(old_value, "baseSpecialization", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "baseSpecialization"):
                opp_val = getattr(value, "baseSpecialization", None)
                if opp_val is None:
                    setattr(value, "baseSpecialization", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Specialization8(self):
        return self.__Specialization8

    @Specialization8.setter
    def Specialization8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyProgramStructure_Specialization__Specialization8", None)
        self.__Specialization8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "furtherSpecializations"):
                opp_val = getattr(old_value, "furtherSpecializations", None)
                if opp_val == self:
                    setattr(old_value, "furtherSpecializations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "furtherSpecializations"):
                opp_val = getattr(value, "furtherSpecializations", None)
                setattr(value, "furtherSpecializations", self)

    @property
    def furtherSpecializations(self):
        return self.__furtherSpecializations

    @furtherSpecializations.setter
    def furtherSpecializations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyProgramStructure_Specialization__furtherSpecializations", None)
        self.__furtherSpecializations = value
        
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
    def specializations(self):
        return self.__specializations

    @specializations.setter
    def specializations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyProgramStructure_Specialization__specializations", None)
        self.__specializations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Program"):
                opp_val = getattr(old_value, "Program", None)
                if opp_val == self:
                    setattr(old_value, "Program", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Program"):
                opp_val = getattr(value, "Program", None)
                setattr(value, "Program", self)

    @property
    def baseSpecialization(self):
        return self.__baseSpecialization

    @baseSpecialization.setter
    def baseSpecialization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyProgramStructure_Specialization__baseSpecialization", None)
        self.__baseSpecialization = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Specialization5"):
                    opp_val = getattr(item, "Specialization5", None)
                    
                    if opp_val == self:
                        setattr(item, "Specialization5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Specialization5"):
                    opp_val = getattr(item, "Specialization5", None)
                    
                    setattr(item, "Specialization5", self)
                    

    @property
    def specialization(self):
        return self.__specialization

    @specialization.setter
    def specialization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyProgramStructure_Specialization__specialization", None)
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
    def Specialization17(self):
        return self.__Specialization17

    @Specialization17.setter
    def Specialization17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyProgramStructure_Specialization__Specialization17", None)
        self.__Specialization17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "semesters16"):
                opp_val = getattr(old_value, "semesters16", None)
                if opp_val == self:
                    setattr(old_value, "semesters16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "semesters16"):
                opp_val = getattr(value, "semesters16", None)
                setattr(value, "semesters16", self)

    @property
    def Specialization(self):
        return self.__Specialization

    @Specialization.setter
    def Specialization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyProgramStructure_Specialization__Specialization", None)
        self.__Specialization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "program"):
                opp_val = getattr(old_value, "program", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "program"):
                opp_val = getattr(value, "program", None)
                if opp_val is None:
                    setattr(value, "program", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class studyProgramStructure_Program:

    def __init__(self, numOfSemestersForBaseSpecialization: int, numOfYears: int, name: str, code: str, program: set["studyProgramStructure_Specialization"] = None, program2: set["studyProgramStructure_Semester"] = None, Program14: "studyProgramStructure_Semester" = None, Program: "studyProgramStructure_Specialization" = None, studyProgramStructure_Program: "studyProgramStructure_University" = None, studyProgramStructure_Program30: "studyProgramStructure_Student" = None):
        self.numOfSemestersForBaseSpecialization = numOfSemestersForBaseSpecialization
        self.numOfYears = numOfYears
        self.name = name
        self.code = code
        self.program = program if program is not None else set()
        self.program2 = program2 if program2 is not None else set()
        self.Program14 = Program14
        self.Program = Program
        self.studyProgramStructure_Program = studyProgramStructure_Program
        self.studyProgramStructure_Program30 = studyProgramStructure_Program30
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def numOfSemestersForBaseSpecialization(self) -> int:
        return self.__numOfSemestersForBaseSpecialization

    @numOfSemestersForBaseSpecialization.setter
    def numOfSemestersForBaseSpecialization(self, numOfSemestersForBaseSpecialization: int):
        self.__numOfSemestersForBaseSpecialization = numOfSemestersForBaseSpecialization

    @property
    def numOfYears(self) -> int:
        return self.__numOfYears

    @numOfYears.setter
    def numOfYears(self, numOfYears: int):
        self.__numOfYears = numOfYears

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def studyProgramStructure_Program(self):
        return self.__studyProgramStructure_Program

    @studyProgramStructure_Program.setter
    def studyProgramStructure_Program(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyProgramStructure_Program__studyProgramStructure_Program", None)
        self.__studyProgramStructure_Program = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyProgramStructure_University"):
                opp_val = getattr(old_value, "studyProgramStructure_University", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyProgramStructure_University"):
                opp_val = getattr(value, "studyProgramStructure_University", None)
                if opp_val is None:
                    setattr(value, "studyProgramStructure_University", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Program(self):
        return self.__Program

    @Program.setter
    def Program(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyProgramStructure_Program__Program", None)
        self.__Program = value
        
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
    def Program14(self):
        return self.__Program14

    @Program14.setter
    def Program14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyProgramStructure_Program__Program14", None)
        self.__Program14 = value
        
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
    def studyProgramStructure_Program30(self):
        return self.__studyProgramStructure_Program30

    @studyProgramStructure_Program30.setter
    def studyProgramStructure_Program30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyProgramStructure_Program__studyProgramStructure_Program30", None)
        self.__studyProgramStructure_Program30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyProgramStructure_Student29"):
                opp_val = getattr(old_value, "studyProgramStructure_Student29", None)
                if opp_val == self:
                    setattr(old_value, "studyProgramStructure_Student29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyProgramStructure_Student29"):
                opp_val = getattr(value, "studyProgramStructure_Student29", None)
                setattr(value, "studyProgramStructure_Student29", self)

    @property
    def program(self):
        return self.__program

    @program.setter
    def program(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyProgramStructure_Program__program", None)
        self.__program = value if value is not None else set()
        
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
    def program2(self):
        return self.__program2

    @program2.setter
    def program2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyProgramStructure_Program__program2", None)
        self.__program2 = value if value is not None else set()
        
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
                    

class studyProgramStructure_Course:

    def __init__(self, name: str, code: str, credits: float, level: int, studyProgramStructure_Course: "studyProgramStructure_CourseGroup" = None, studyProgramStructure_Course24: "studyProgramStructure_University" = None, studyProgramStructure_Course39: "studyProgramStructure_CourseAllocation" = None):
        self.name = name
        self.code = code
        self.credits = credits
        self.level = level
        self.studyProgramStructure_Course = studyProgramStructure_Course
        self.studyProgramStructure_Course24 = studyProgramStructure_Course24
        self.studyProgramStructure_Course39 = studyProgramStructure_Course39
        
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
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def level(self) -> int:
        return self.__level

    @level.setter
    def level(self, level: int):
        self.__level = level

    @property
    def studyProgramStructure_Course(self):
        return self.__studyProgramStructure_Course

    @studyProgramStructure_Course.setter
    def studyProgramStructure_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyProgramStructure_Course__studyProgramStructure_Course", None)
        self.__studyProgramStructure_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyProgramStructure_CourseGroup"):
                opp_val = getattr(old_value, "studyProgramStructure_CourseGroup", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyProgramStructure_CourseGroup"):
                opp_val = getattr(value, "studyProgramStructure_CourseGroup", None)
                if opp_val is None:
                    setattr(value, "studyProgramStructure_CourseGroup", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def studyProgramStructure_Course39(self):
        return self.__studyProgramStructure_Course39

    @studyProgramStructure_Course39.setter
    def studyProgramStructure_Course39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyProgramStructure_Course__studyProgramStructure_Course39", None)
        self.__studyProgramStructure_Course39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyProgramStructure_CourseAllocation38"):
                opp_val = getattr(old_value, "studyProgramStructure_CourseAllocation38", None)
                if opp_val == self:
                    setattr(old_value, "studyProgramStructure_CourseAllocation38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyProgramStructure_CourseAllocation38"):
                opp_val = getattr(value, "studyProgramStructure_CourseAllocation38", None)
                setattr(value, "studyProgramStructure_CourseAllocation38", self)

    @property
    def studyProgramStructure_Course24(self):
        return self.__studyProgramStructure_Course24

    @studyProgramStructure_Course24.setter
    def studyProgramStructure_Course24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyProgramStructure_Course__studyProgramStructure_Course24", None)
        self.__studyProgramStructure_Course24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyProgramStructure_University23"):
                opp_val = getattr(old_value, "studyProgramStructure_University23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyProgramStructure_University23"):
                opp_val = getattr(value, "studyProgramStructure_University23", None)
                if opp_val is None:
                    setattr(value, "studyProgramStructure_University23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
