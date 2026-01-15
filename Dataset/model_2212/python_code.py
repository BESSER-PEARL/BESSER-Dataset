from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class SeasonEnum(Enum):
    Vår = "Vår"
    Høst = "Høst"


############################################
# Definition of Classes
############################################

class studyPlan_Semester:

    def __init__(self, season: str, codename: str, year: int):
        self.season = season
        self.codename = codename
        self.year = year
        
    @property
    def season(self) -> str:
        return self.__season

    @season.setter
    def season(self, season: str):
        self.__season = season

    @property
    def codename(self) -> str:
        return self.__codename

    @codename.setter
    def codename(self, codename: str):
        self.__codename = codename

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year

class studyPlan_StudyPlan:

    pass
class studyPlan_Specialization:

    def __init__(self, name: str, year: int, Specialization: "studyPlan_SemesterProgramme" = None, specializations: "studyPlan_StudyProgramme" = None, Specialization24: "studyPlan_StudyProgramme" = None, studyPlan_Specialization: "studyPlan_Specialization" = None, studyPlan_Specialization27: set["studyPlan_Specialization"] = None, specialization: set["studyPlan_SemesterProgramme"] = None):
        self.name = name
        self.year = year
        self.Specialization = Specialization
        self.specializations = specializations
        self.Specialization24 = Specialization24
        self.studyPlan_Specialization = studyPlan_Specialization
        self.studyPlan_Specialization27 = studyPlan_Specialization27 if studyPlan_Specialization27 is not None else set()
        self.specialization = specialization if specialization is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def specializations(self):
        return self.__specializations

    @specializations.setter
    def specializations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyPlan_Specialization__specializations", None)
        self.__specializations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StudyProgramme26"):
                opp_val = getattr(old_value, "StudyProgramme26", None)
                if opp_val == self:
                    setattr(old_value, "StudyProgramme26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StudyProgramme26"):
                opp_val = getattr(value, "StudyProgramme26", None)
                setattr(value, "StudyProgramme26", self)

    @property
    def studyPlan_Specialization27(self):
        return self.__studyPlan_Specialization27

    @studyPlan_Specialization27.setter
    def studyPlan_Specialization27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyPlan_Specialization__studyPlan_Specialization27", None)
        self.__studyPlan_Specialization27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "studyPlan_Specialization"):
                    opp_val = getattr(item, "studyPlan_Specialization", None)
                    
                    if opp_val == self:
                        setattr(item, "studyPlan_Specialization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "studyPlan_Specialization"):
                    opp_val = getattr(item, "studyPlan_Specialization", None)
                    
                    setattr(item, "studyPlan_Specialization", self)
                    

    @property
    def Specialization24(self):
        return self.__Specialization24

    @Specialization24.setter
    def Specialization24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyPlan_Specialization__Specialization24", None)
        self.__Specialization24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyProgramme"):
                opp_val = getattr(old_value, "studyProgramme", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyProgramme"):
                opp_val = getattr(value, "studyProgramme", None)
                if opp_val is None:
                    setattr(value, "studyProgramme", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Specialization(self):
        return self.__Specialization

    @Specialization.setter
    def Specialization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyPlan_Specialization__Specialization", None)
        self.__Specialization = value
        
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
    def studyPlan_Specialization(self):
        return self.__studyPlan_Specialization

    @studyPlan_Specialization.setter
    def studyPlan_Specialization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyPlan_Specialization__studyPlan_Specialization", None)
        self.__studyPlan_Specialization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyPlan_Specialization27"):
                opp_val = getattr(old_value, "studyPlan_Specialization27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyPlan_Specialization27"):
                opp_val = getattr(value, "studyPlan_Specialization27", None)
                if opp_val is None:
                    setattr(value, "studyPlan_Specialization27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def specialization(self):
        return self.__specialization

    @specialization.setter
    def specialization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyPlan_Specialization__specialization", None)
        self.__specialization = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SemesterProgramme"):
                    opp_val = getattr(item, "SemesterProgramme", None)
                    
                    if opp_val == self:
                        setattr(item, "SemesterProgramme", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SemesterProgramme"):
                    opp_val = getattr(item, "SemesterProgramme", None)
                    
                    setattr(item, "SemesterProgramme", self)
                    

class Semester:

    pass
class studyPlan_SemesterProgramme(Semester):

    pass
class studyPlan_SemesterPlan(Semester):

    pass
class studyPlan_University:

    def __init__(self, name: str, university: set["studyPlan_Student"] = None, university3: set["studyPlan_StudyProgramme"] = None, university5: set["studyPlan_Course"] = None, University: "studyPlan_Course" = None, University22: "studyPlan_StudyProgramme" = None, University18: "studyPlan_Student" = None):
        self.name = name
        self.university = university if university is not None else set()
        self.university3 = university3 if university3 is not None else set()
        self.university5 = university5 if university5 is not None else set()
        self.University = University
        self.University22 = University22
        self.University18 = University18
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def university(self):
        return self.__university

    @university.setter
    def university(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyPlan_University__university", None)
        self.__university = value if value is not None else set()
        
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
    def University22(self):
        return self.__University22

    @University22.setter
    def University22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyPlan_University__University22", None)
        self.__University22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyProgrammes"):
                opp_val = getattr(old_value, "studyProgrammes", None)
                if opp_val == self:
                    setattr(old_value, "studyProgrammes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyProgrammes"):
                opp_val = getattr(value, "studyProgrammes", None)
                setattr(value, "studyProgrammes", self)

    @property
    def university3(self):
        return self.__university3

    @university3.setter
    def university3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyPlan_University__university3", None)
        self.__university3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StudyProgramme"):
                    opp_val = getattr(item, "StudyProgramme", None)
                    
                    if opp_val == self:
                        setattr(item, "StudyProgramme", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StudyProgramme"):
                    opp_val = getattr(item, "StudyProgramme", None)
                    
                    setattr(item, "StudyProgramme", self)
                    

    @property
    def University(self):
        return self.__University

    @University.setter
    def University(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyPlan_University__University", None)
        self.__University = value
        
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
    def university5(self):
        return self.__university5

    @university5.setter
    def university5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyPlan_University__university5", None)
        self.__university5 = value if value is not None else set()
        
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
    def University18(self):
        return self.__University18

    @University18.setter
    def University18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyPlan_University__University18", None)
        self.__University18 = value
        
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

class studyPlan_Course:

    def __init__(self, credits: float, level: int, codename: str, name: str, courses: "studyPlan_University" = None, Course: "studyPlan_University" = None, studyPlan_Course: "studyPlan_SemesterPlan" = None, studyPlan_Course13: "studyPlan_SemesterProgramme" = None, studyPlan_Course16: "studyPlan_SemesterProgramme" = None):
        self.credits = credits
        self.level = level
        self.codename = codename
        self.name = name
        self.courses = courses
        self.Course = Course
        self.studyPlan_Course = studyPlan_Course
        self.studyPlan_Course13 = studyPlan_Course13
        self.studyPlan_Course16 = studyPlan_Course16
        
    @property
    def level(self) -> int:
        return self.__level

    @level.setter
    def level(self, level: int):
        self.__level = level

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
    def codename(self) -> str:
        return self.__codename

    @codename.setter
    def codename(self, codename: str):
        self.__codename = codename

    @property
    def studyPlan_Course13(self):
        return self.__studyPlan_Course13

    @studyPlan_Course13.setter
    def studyPlan_Course13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyPlan_Course__studyPlan_Course13", None)
        self.__studyPlan_Course13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyPlan_SemesterProgramme"):
                opp_val = getattr(old_value, "studyPlan_SemesterProgramme", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyPlan_SemesterProgramme"):
                opp_val = getattr(value, "studyPlan_SemesterProgramme", None)
                if opp_val is None:
                    setattr(value, "studyPlan_SemesterProgramme", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyPlan_Course__courses", None)
        self.__courses = value
        
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

    @property
    def studyPlan_Course16(self):
        return self.__studyPlan_Course16

    @studyPlan_Course16.setter
    def studyPlan_Course16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyPlan_Course__studyPlan_Course16", None)
        self.__studyPlan_Course16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyPlan_SemesterProgramme15"):
                opp_val = getattr(old_value, "studyPlan_SemesterProgramme15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyPlan_SemesterProgramme15"):
                opp_val = getattr(value, "studyPlan_SemesterProgramme15", None)
                if opp_val is None:
                    setattr(value, "studyPlan_SemesterProgramme15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Course(self):
        return self.__Course

    @Course.setter
    def Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyPlan_Course__Course", None)
        self.__Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "university5"):
                opp_val = getattr(old_value, "university5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "university5"):
                opp_val = getattr(value, "university5", None)
                if opp_val is None:
                    setattr(value, "university5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def studyPlan_Course(self):
        return self.__studyPlan_Course

    @studyPlan_Course.setter
    def studyPlan_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyPlan_Course__studyPlan_Course", None)
        self.__studyPlan_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyPlan_SemesterPlan"):
                opp_val = getattr(old_value, "studyPlan_SemesterPlan", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyPlan_SemesterPlan"):
                opp_val = getattr(value, "studyPlan_SemesterPlan", None)
                if opp_val is None:
                    setattr(value, "studyPlan_SemesterPlan", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class studyPlan_StudyProgramme:

    def __init__(self, codename: str, name: str, lengthInYears: int, StudyProgramme: "studyPlan_University" = None, studyProgrammes: "studyPlan_University" = None, StudyProgramme26: "studyPlan_Specialization" = None, studyProgramme: set["studyPlan_Specialization"] = None):
        self.codename = codename
        self.name = name
        self.lengthInYears = lengthInYears
        self.StudyProgramme = StudyProgramme
        self.studyProgrammes = studyProgrammes
        self.StudyProgramme26 = StudyProgramme26
        self.studyProgramme = studyProgramme if studyProgramme is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def lengthInYears(self) -> int:
        return self.__lengthInYears

    @lengthInYears.setter
    def lengthInYears(self, lengthInYears: int):
        self.__lengthInYears = lengthInYears

    @property
    def codename(self) -> str:
        return self.__codename

    @codename.setter
    def codename(self, codename: str):
        self.__codename = codename

    @property
    def studyProgrammes(self):
        return self.__studyProgrammes

    @studyProgrammes.setter
    def studyProgrammes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyPlan_StudyProgramme__studyProgrammes", None)
        self.__studyProgrammes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "University22"):
                opp_val = getattr(old_value, "University22", None)
                if opp_val == self:
                    setattr(old_value, "University22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "University22"):
                opp_val = getattr(value, "University22", None)
                setattr(value, "University22", self)

    @property
    def StudyProgramme26(self):
        return self.__StudyProgramme26

    @StudyProgramme26.setter
    def StudyProgramme26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyPlan_StudyProgramme__StudyProgramme26", None)
        self.__StudyProgramme26 = value
        
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
    def studyProgramme(self):
        return self.__studyProgramme

    @studyProgramme.setter
    def studyProgramme(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyPlan_StudyProgramme__studyProgramme", None)
        self.__studyProgramme = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Specialization24"):
                    opp_val = getattr(item, "Specialization24", None)
                    
                    if opp_val == self:
                        setattr(item, "Specialization24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Specialization24"):
                    opp_val = getattr(item, "Specialization24", None)
                    
                    setattr(item, "Specialization24", self)
                    

    @property
    def StudyProgramme(self):
        return self.__StudyProgramme

    @StudyProgramme.setter
    def StudyProgramme(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyPlan_StudyProgramme__StudyProgramme", None)
        self.__StudyProgramme = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "university3"):
                opp_val = getattr(old_value, "university3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "university3"):
                opp_val = getattr(value, "university3", None)
                if opp_val is None:
                    setattr(value, "university3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class studyPlan_Student:

    def __init__(self, name: str, username: str, Student: "studyPlan_University" = None, Student7: "studyPlan_StudyPlan" = None, student: "studyPlan_StudyPlan" = None, students: "studyPlan_University" = None):
        self.name = name
        self.username = username
        self.Student = Student
        self.Student7 = Student7
        self.student = student
        self.students = students
        
    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, username: str):
        self.__username = username

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
        old_value = getattr(self, f"_studyPlan_Student__students", None)
        self.__students = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "University18"):
                opp_val = getattr(old_value, "University18", None)
                if opp_val == self:
                    setattr(old_value, "University18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "University18"):
                opp_val = getattr(value, "University18", None)
                setattr(value, "University18", self)

    @property
    def Student(self):
        return self.__Student

    @Student.setter
    def Student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyPlan_Student__Student", None)
        self.__Student = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "university"):
                opp_val = getattr(old_value, "university", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "university"):
                opp_val = getattr(value, "university", None)
                if opp_val is None:
                    setattr(value, "university", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Student7(self):
        return self.__Student7

    @Student7.setter
    def Student7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyPlan_Student__Student7", None)
        self.__Student7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyplan"):
                opp_val = getattr(old_value, "studyplan", None)
                if opp_val == self:
                    setattr(old_value, "studyplan", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyplan"):
                opp_val = getattr(value, "studyplan", None)
                setattr(value, "studyplan", self)

    @property
    def student(self):
        return self.__student

    @student.setter
    def student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyPlan_Student__student", None)
        self.__student = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StudyPlan20"):
                opp_val = getattr(old_value, "StudyPlan20", None)
                if opp_val == self:
                    setattr(old_value, "StudyPlan20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StudyPlan20"):
                opp_val = getattr(value, "StudyPlan20", None)
                setattr(value, "StudyPlan20", self)
