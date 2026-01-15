from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class CourseType(Enum):
    Obligatory = "Obligatory"
    Elective = "Elective"
class SemesterType(Enum):
    Fall = "Fall"
    Spring = "Spring"


############################################
# Definition of Classes
############################################

class studyprogram_SemesterCourse:

    def __init__(self, type: str, name: str, SemesterCourse: "studyprogram_Semester" = None, semesterCourses: "studyprogram_Semester" = None, studyprogram_SemesterCourse: "studyprogram_Course" = None):
        self.type = type
        self.name = name
        self.SemesterCourse = SemesterCourse
        self.semesterCourses = semesterCourses
        self.studyprogram_SemesterCourse = studyprogram_SemesterCourse
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def studyprogram_SemesterCourse(self):
        return self.__studyprogram_SemesterCourse

    @studyprogram_SemesterCourse.setter
    def studyprogram_SemesterCourse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_SemesterCourse__studyprogram_SemesterCourse", None)
        self.__studyprogram_SemesterCourse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyprogram_Course"):
                opp_val = getattr(old_value, "studyprogram_Course", None)
                if opp_val == self:
                    setattr(old_value, "studyprogram_Course", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyprogram_Course"):
                opp_val = getattr(value, "studyprogram_Course", None)
                setattr(value, "studyprogram_Course", self)

    @property
    def semesterCourses(self):
        return self.__semesterCourses

    @semesterCourses.setter
    def semesterCourses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_SemesterCourse__semesterCourses", None)
        self.__semesterCourses = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Semester29"):
                opp_val = getattr(old_value, "Semester29", None)
                if opp_val == self:
                    setattr(old_value, "Semester29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Semester29"):
                opp_val = getattr(value, "Semester29", None)
                setattr(value, "Semester29", self)

    @property
    def SemesterCourse(self):
        return self.__SemesterCourse

    @SemesterCourse.setter
    def SemesterCourse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_SemesterCourse__SemesterCourse", None)
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

class studyprogram_Semester:

    def __init__(self, type: str, Semester: "studyprogram_Year" = None, semesters: "studyprogram_Year" = None, semester: set["studyprogram_SemesterCourse"] = None, Semester29: "studyprogram_SemesterCourse" = None):
        self.type = type
        self.Semester = Semester
        self.semesters = semesters
        self.semester = semester if semester is not None else set()
        self.Semester29 = Semester29
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def Semester(self):
        return self.__Semester

    @Semester.setter
    def Semester(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_Semester__Semester", None)
        self.__Semester = value
        
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
    def semesters(self):
        return self.__semesters

    @semesters.setter
    def semesters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_Semester__semesters", None)
        self.__semesters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Year26"):
                opp_val = getattr(old_value, "Year26", None)
                if opp_val == self:
                    setattr(old_value, "Year26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Year26"):
                opp_val = getattr(value, "Year26", None)
                setattr(value, "Year26", self)

    @property
    def semester(self):
        return self.__semester

    @semester.setter
    def semester(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_Semester__semester", None)
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
    def Semester29(self):
        return self.__Semester29

    @Semester29.setter
    def Semester29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_Semester__Semester29", None)
        self.__Semester29 = value
        
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

class studyprogram_Year:

    def __init__(self, value: int, Year: "studyprogram_StudyPlan" = None, year: set["studyprogram_Semester"] = None, years: "studyprogram_StudyPlan" = None, Year26: "studyprogram_Semester" = None):
        self.value = value
        self.Year = Year
        self.year = year if year is not None else set()
        self.years = years
        self.Year26 = Year26
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_Year__year", None)
        self.__year = value if value is not None else set()
        
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
    def Year(self):
        return self.__Year

    @Year.setter
    def Year(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_Year__Year", None)
        self.__Year = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyPlan"):
                opp_val = getattr(old_value, "studyPlan", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyPlan"):
                opp_val = getattr(value, "studyPlan", None)
                if opp_val is None:
                    setattr(value, "studyPlan", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def years(self):
        return self.__years

    @years.setter
    def years(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_Year__years", None)
        self.__years = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StudyPlan24"):
                opp_val = getattr(old_value, "StudyPlan24", None)
                if opp_val == self:
                    setattr(old_value, "StudyPlan24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StudyPlan24"):
                opp_val = getattr(value, "StudyPlan24", None)
                setattr(value, "StudyPlan24", self)

    @property
    def Year26(self):
        return self.__Year26

    @Year26.setter
    def Year26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_Year__Year26", None)
        self.__Year26 = value
        
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

class studyprogram_ObligatoryCourses:

    pass
class studyprogram_ElectiveCourses:

    pass
class studyprogram_StudyPlan:

    def __init__(self, name: str, StudyPlan: "studyprogram_Program" = None, studyPlan: set["studyprogram_Year"] = None, studyPlans: "studyprogram_Program" = None, StudyPlan17: "studyprogram_StudyPlan" = None, specialisations: "studyprogram_StudyPlan" = None, StudyPlan21: "studyprogram_StudyPlan" = None, studyPlan20: set["studyprogram_StudyPlan"] = None, StudyPlan24: "studyprogram_Year" = None):
        self.name = name
        self.StudyPlan = StudyPlan
        self.studyPlan = studyPlan if studyPlan is not None else set()
        self.studyPlans = studyPlans
        self.StudyPlan17 = StudyPlan17
        self.specialisations = specialisations
        self.StudyPlan21 = StudyPlan21
        self.studyPlan20 = studyPlan20 if studyPlan20 is not None else set()
        self.StudyPlan24 = StudyPlan24
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def studyPlans(self):
        return self.__studyPlans

    @studyPlans.setter
    def studyPlans(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_StudyPlan__studyPlans", None)
        self.__studyPlans = value
        
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
    def studyPlan20(self):
        return self.__studyPlan20

    @studyPlan20.setter
    def studyPlan20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_StudyPlan__studyPlan20", None)
        self.__studyPlan20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StudyPlan21"):
                    opp_val = getattr(item, "StudyPlan21", None)
                    
                    if opp_val == self:
                        setattr(item, "StudyPlan21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StudyPlan21"):
                    opp_val = getattr(item, "StudyPlan21", None)
                    
                    setattr(item, "StudyPlan21", self)
                    

    @property
    def StudyPlan24(self):
        return self.__StudyPlan24

    @StudyPlan24.setter
    def StudyPlan24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_StudyPlan__StudyPlan24", None)
        self.__StudyPlan24 = value
        
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
    def StudyPlan21(self):
        return self.__StudyPlan21

    @StudyPlan21.setter
    def StudyPlan21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_StudyPlan__StudyPlan21", None)
        self.__StudyPlan21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyPlan20"):
                opp_val = getattr(old_value, "studyPlan20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyPlan20"):
                opp_val = getattr(value, "studyPlan20", None)
                if opp_val is None:
                    setattr(value, "studyPlan20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def StudyPlan17(self):
        return self.__StudyPlan17

    @StudyPlan17.setter
    def StudyPlan17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_StudyPlan__StudyPlan17", None)
        self.__StudyPlan17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "specialisations"):
                opp_val = getattr(old_value, "specialisations", None)
                if opp_val == self:
                    setattr(old_value, "specialisations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "specialisations"):
                opp_val = getattr(value, "specialisations", None)
                setattr(value, "specialisations", self)

    @property
    def specialisations(self):
        return self.__specialisations

    @specialisations.setter
    def specialisations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_StudyPlan__specialisations", None)
        self.__specialisations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StudyPlan17"):
                opp_val = getattr(old_value, "StudyPlan17", None)
                if opp_val == self:
                    setattr(old_value, "StudyPlan17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StudyPlan17"):
                opp_val = getattr(value, "StudyPlan17", None)
                setattr(value, "StudyPlan17", self)

    @property
    def StudyPlan(self):
        return self.__StudyPlan

    @StudyPlan.setter
    def StudyPlan(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_StudyPlan__StudyPlan", None)
        self.__StudyPlan = value
        
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

    @property
    def studyPlan(self):
        return self.__studyPlan

    @studyPlan.setter
    def studyPlan(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_StudyPlan__studyPlan", None)
        self.__studyPlan = value if value is not None else set()
        
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
                    

class studyprogram_Program:

    def __init__(self, name: str, Program: "studyprogram_Department" = None, programs: "studyprogram_Department" = None, program: set["studyprogram_StudyPlan"] = None, program9: "studyprogram_ElectiveCourses" = None, program11: "studyprogram_ObligatoryCourses" = None, Program14: "studyprogram_StudyPlan" = None, Program34: "studyprogram_ElectiveCourses" = None, Program38: "studyprogram_ObligatoryCourses" = None):
        self.name = name
        self.Program = Program
        self.programs = programs
        self.program = program if program is not None else set()
        self.program9 = program9
        self.program11 = program11
        self.Program14 = Program14
        self.Program34 = Program34
        self.Program38 = Program38
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def program(self):
        return self.__program

    @program.setter
    def program(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_Program__program", None)
        self.__program = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StudyPlan"):
                    opp_val = getattr(item, "StudyPlan", None)
                    
                    if opp_val == self:
                        setattr(item, "StudyPlan", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StudyPlan"):
                    opp_val = getattr(item, "StudyPlan", None)
                    
                    setattr(item, "StudyPlan", self)
                    

    @property
    def Program14(self):
        return self.__Program14

    @Program14.setter
    def Program14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_Program__Program14", None)
        self.__Program14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyPlans"):
                opp_val = getattr(old_value, "studyPlans", None)
                if opp_val == self:
                    setattr(old_value, "studyPlans", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyPlans"):
                opp_val = getattr(value, "studyPlans", None)
                setattr(value, "studyPlans", self)

    @property
    def Program(self):
        return self.__Program

    @Program.setter
    def Program(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_Program__Program", None)
        self.__Program = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "department4"):
                opp_val = getattr(old_value, "department4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "department4"):
                opp_val = getattr(value, "department4", None)
                if opp_val is None:
                    setattr(value, "department4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Program34(self):
        return self.__Program34

    @Program34.setter
    def Program34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_Program__Program34", None)
        self.__Program34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "electiveCourses"):
                opp_val = getattr(old_value, "electiveCourses", None)
                if opp_val == self:
                    setattr(old_value, "electiveCourses", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "electiveCourses"):
                opp_val = getattr(value, "electiveCourses", None)
                setattr(value, "electiveCourses", self)

    @property
    def program11(self):
        return self.__program11

    @program11.setter
    def program11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_Program__program11", None)
        self.__program11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ObligatoryCourses"):
                opp_val = getattr(old_value, "ObligatoryCourses", None)
                if opp_val == self:
                    setattr(old_value, "ObligatoryCourses", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ObligatoryCourses"):
                opp_val = getattr(value, "ObligatoryCourses", None)
                setattr(value, "ObligatoryCourses", self)

    @property
    def program9(self):
        return self.__program9

    @program9.setter
    def program9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_Program__program9", None)
        self.__program9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ElectiveCourses"):
                opp_val = getattr(old_value, "ElectiveCourses", None)
                if opp_val == self:
                    setattr(old_value, "ElectiveCourses", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ElectiveCourses"):
                opp_val = getattr(value, "ElectiveCourses", None)
                setattr(value, "ElectiveCourses", self)

    @property
    def programs(self):
        return self.__programs

    @programs.setter
    def programs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_Program__programs", None)
        self.__programs = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Department6"):
                opp_val = getattr(old_value, "Department6", None)
                if opp_val == self:
                    setattr(old_value, "Department6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Department6"):
                opp_val = getattr(value, "Department6", None)
                setattr(value, "Department6", self)

    @property
    def Program38(self):
        return self.__Program38

    @Program38.setter
    def Program38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_Program__Program38", None)
        self.__Program38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "obligatoryCourses"):
                opp_val = getattr(old_value, "obligatoryCourses", None)
                if opp_val == self:
                    setattr(old_value, "obligatoryCourses", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "obligatoryCourses"):
                opp_val = getattr(value, "obligatoryCourses", None)
                setattr(value, "obligatoryCourses", self)

class studyprogram_Course:

    def __init__(self, semester: str, name: str, credits: str, code: str, Course: "studyprogram_Department" = None, studyprogram_Course: "studyprogram_SemesterCourse" = None, courses: "studyprogram_Department" = None, studyprogram_Course36: "studyprogram_ElectiveCourses" = None, studyprogram_Course40: "studyprogram_ObligatoryCourses" = None):
        self.semester = semester
        self.name = name
        self.credits = credits
        self.code = code
        self.Course = Course
        self.studyprogram_Course = studyprogram_Course
        self.courses = courses
        self.studyprogram_Course36 = studyprogram_Course36
        self.studyprogram_Course40 = studyprogram_Course40
        
    @property
    def semester(self) -> str:
        return self.__semester

    @semester.setter
    def semester(self, semester: str):
        self.__semester = semester

    @property
    def credits(self) -> str:
        return self.__credits

    @credits.setter
    def credits(self, credits: str):
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
    def studyprogram_Course40(self):
        return self.__studyprogram_Course40

    @studyprogram_Course40.setter
    def studyprogram_Course40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_Course__studyprogram_Course40", None)
        self.__studyprogram_Course40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyprogram_ObligatoryCourses"):
                opp_val = getattr(old_value, "studyprogram_ObligatoryCourses", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyprogram_ObligatoryCourses"):
                opp_val = getattr(value, "studyprogram_ObligatoryCourses", None)
                if opp_val is None:
                    setattr(value, "studyprogram_ObligatoryCourses", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def studyprogram_Course(self):
        return self.__studyprogram_Course

    @studyprogram_Course.setter
    def studyprogram_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_Course__studyprogram_Course", None)
        self.__studyprogram_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyprogram_SemesterCourse"):
                opp_val = getattr(old_value, "studyprogram_SemesterCourse", None)
                if opp_val == self:
                    setattr(old_value, "studyprogram_SemesterCourse", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyprogram_SemesterCourse"):
                opp_val = getattr(value, "studyprogram_SemesterCourse", None)
                setattr(value, "studyprogram_SemesterCourse", self)

    @property
    def Course(self):
        return self.__Course

    @Course.setter
    def Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_Course__Course", None)
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
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_Course__courses", None)
        self.__courses = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Department32"):
                opp_val = getattr(old_value, "Department32", None)
                if opp_val == self:
                    setattr(old_value, "Department32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Department32"):
                opp_val = getattr(value, "Department32", None)
                setattr(value, "Department32", self)

    @property
    def studyprogram_Course36(self):
        return self.__studyprogram_Course36

    @studyprogram_Course36.setter
    def studyprogram_Course36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_Course__studyprogram_Course36", None)
        self.__studyprogram_Course36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyprogram_ElectiveCourses"):
                opp_val = getattr(old_value, "studyprogram_ElectiveCourses", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyprogram_ElectiveCourses"):
                opp_val = getattr(value, "studyprogram_ElectiveCourses", None)
                if opp_val is None:
                    setattr(value, "studyprogram_ElectiveCourses", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class studyprogram_Department:

    def __init__(self, name: str, department4: set["studyprogram_Program"] = None, Department: "studyprogram_University" = None, departments: "studyprogram_University" = None, department: set["studyprogram_Course"] = None, Department6: "studyprogram_Program" = None, Department32: "studyprogram_Course" = None):
        self.name = name
        self.department4 = department4 if department4 is not None else set()
        self.Department = Department
        self.departments = departments
        self.department = department if department is not None else set()
        self.Department6 = Department6
        self.Department32 = Department32
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Department32(self):
        return self.__Department32

    @Department32.setter
    def Department32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_Department__Department32", None)
        self.__Department32 = value
        
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
    def department4(self):
        return self.__department4

    @department4.setter
    def department4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_Department__department4", None)
        self.__department4 = value if value is not None else set()
        
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
                    

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_Department__department", None)
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
    def Department(self):
        return self.__Department

    @Department.setter
    def Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_Department__Department", None)
        self.__Department = value
        
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
    def Department6(self):
        return self.__Department6

    @Department6.setter
    def Department6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_Department__Department6", None)
        self.__Department6 = value
        
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
    def departments(self):
        return self.__departments

    @departments.setter
    def departments(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_Department__departments", None)
        self.__departments = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "University"):
                opp_val = getattr(old_value, "University", None)
                if opp_val == self:
                    setattr(old_value, "University", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "University"):
                opp_val = getattr(value, "University", None)
                setattr(value, "University", self)

class studyprogram_University:

    def __init__(self, name: str, school: set["studyprogram_Department"] = None, University: "studyprogram_Department" = None):
        self.name = name
        self.school = school if school is not None else set()
        self.University = University
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def University(self):
        return self.__University

    @University.setter
    def University(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_University__University", None)
        self.__University = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "departments"):
                opp_val = getattr(old_value, "departments", None)
                if opp_val == self:
                    setattr(old_value, "departments", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "departments"):
                opp_val = getattr(value, "departments", None)
                setattr(value, "departments", self)

    @property
    def school(self):
        return self.__school

    @school.setter
    def school(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_University__school", None)
        self.__school = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Department"):
                    opp_val = getattr(item, "Department", None)
                    
                    if opp_val == self:
                        setattr(item, "Department", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Department"):
                    opp_val = getattr(item, "Department", None)
                    
                    setattr(item, "Department", self)
                    
