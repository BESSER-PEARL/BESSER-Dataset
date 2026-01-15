from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class grades(Enum):
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"
    A = "A"


############################################
# Definition of Classes
############################################

class study_courseAllocation:

    def __init__(self, grade: str, study_courseAllocation: "study_StudyPlan" = None, study_courseAllocation41: "study_StudyPlan" = None, study_courseAllocation44: "study_Course" = None):
        self.grade = grade
        self.study_courseAllocation = study_courseAllocation
        self.study_courseAllocation41 = study_courseAllocation41
        self.study_courseAllocation44 = study_courseAllocation44
        
    @property
    def grade(self) -> str:
        return self.__grade

    @grade.setter
    def grade(self, grade: str):
        self.__grade = grade

    @property
    def study_courseAllocation(self):
        return self.__study_courseAllocation

    @study_courseAllocation.setter
    def study_courseAllocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_courseAllocation__study_courseAllocation", None)
        self.__study_courseAllocation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "study_StudyPlan37"):
                opp_val = getattr(old_value, "study_StudyPlan37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "study_StudyPlan37"):
                opp_val = getattr(value, "study_StudyPlan37", None)
                if opp_val is None:
                    setattr(value, "study_StudyPlan37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def study_courseAllocation44(self):
        return self.__study_courseAllocation44

    @study_courseAllocation44.setter
    def study_courseAllocation44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_courseAllocation__study_courseAllocation44", None)
        self.__study_courseAllocation44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "study_Course45"):
                opp_val = getattr(old_value, "study_Course45", None)
                if opp_val == self:
                    setattr(old_value, "study_Course45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "study_Course45"):
                opp_val = getattr(value, "study_Course45", None)
                setattr(value, "study_Course45", self)

    @property
    def study_courseAllocation41(self):
        return self.__study_courseAllocation41

    @study_courseAllocation41.setter
    def study_courseAllocation41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_courseAllocation__study_courseAllocation41", None)
        self.__study_courseAllocation41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "study_StudyPlan42"):
                opp_val = getattr(old_value, "study_StudyPlan42", None)
                if opp_val == self:
                    setattr(old_value, "study_StudyPlan42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "study_StudyPlan42"):
                opp_val = getattr(value, "study_StudyPlan42", None)
                setattr(value, "study_StudyPlan42", self)

class study_StudyPlan:

    def __init__(self, StudyPlan: "study_Student" = None, study_StudyPlan: "study_Semester" = None, study_StudyPlan37: set["study_courseAllocation"] = None, studyPlan: "study_Student" = None, study_StudyPlan42: "study_courseAllocation" = None):
        self.StudyPlan = StudyPlan
        self.study_StudyPlan = study_StudyPlan
        self.study_StudyPlan37 = study_StudyPlan37 if study_StudyPlan37 is not None else set()
        self.studyPlan = studyPlan
        self.study_StudyPlan42 = study_StudyPlan42
        
    @property
    def study_StudyPlan(self):
        return self.__study_StudyPlan

    @study_StudyPlan.setter
    def study_StudyPlan(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_StudyPlan__study_StudyPlan", None)
        self.__study_StudyPlan = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "study_Semester35"):
                opp_val = getattr(old_value, "study_Semester35", None)
                if opp_val == self:
                    setattr(old_value, "study_Semester35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "study_Semester35"):
                opp_val = getattr(value, "study_Semester35", None)
                setattr(value, "study_Semester35", self)

    @property
    def study_StudyPlan42(self):
        return self.__study_StudyPlan42

    @study_StudyPlan42.setter
    def study_StudyPlan42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_StudyPlan__study_StudyPlan42", None)
        self.__study_StudyPlan42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "study_courseAllocation41"):
                opp_val = getattr(old_value, "study_courseAllocation41", None)
                if opp_val == self:
                    setattr(old_value, "study_courseAllocation41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "study_courseAllocation41"):
                opp_val = getattr(value, "study_courseAllocation41", None)
                setattr(value, "study_courseAllocation41", self)

    @property
    def studyPlan(self):
        return self.__studyPlan

    @studyPlan.setter
    def studyPlan(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_StudyPlan__studyPlan", None)
        self.__studyPlan = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Student39"):
                opp_val = getattr(old_value, "Student39", None)
                if opp_val == self:
                    setattr(old_value, "Student39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Student39"):
                opp_val = getattr(value, "Student39", None)
                setattr(value, "Student39", self)

    @property
    def StudyPlan(self):
        return self.__StudyPlan

    @StudyPlan.setter
    def StudyPlan(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_StudyPlan__StudyPlan", None)
        self.__StudyPlan = value
        
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
    def study_StudyPlan37(self):
        return self.__study_StudyPlan37

    @study_StudyPlan37.setter
    def study_StudyPlan37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_StudyPlan__study_StudyPlan37", None)
        self.__study_StudyPlan37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "study_courseAllocation"):
                    opp_val = getattr(item, "study_courseAllocation", None)
                    
                    if opp_val == self:
                        setattr(item, "study_courseAllocation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "study_courseAllocation"):
                    opp_val = getattr(item, "study_courseAllocation", None)
                    
                    setattr(item, "study_courseAllocation", self)
                    

    def chooseCourse(self, course: str, studyplan: str):
        # TODO: Implement chooseCourse method
        pass

class study_Semester:

    def __init__(self, season: str, year: int, Semester: "study_Department" = None, Semester24: "study_Specialisation" = None, semesters: "study_Specialisation" = None, semesters32: "study_Department" = None, study_Semester35: "study_StudyPlan" = None, study_Semester: set["study_Course"] = None):
        self.season = season
        self.year = year
        self.Semester = Semester
        self.Semester24 = Semester24
        self.semesters = semesters
        self.semesters32 = semesters32
        self.study_Semester35 = study_Semester35
        self.study_Semester = study_Semester if study_Semester is not None else set()
        
    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def season(self) -> str:
        return self.__season

    @season.setter
    def season(self, season: str):
        self.__season = season

    @property
    def Semester24(self):
        return self.__Semester24

    @Semester24.setter
    def Semester24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Semester__Semester24", None)
        self.__Semester24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "specialisation"):
                opp_val = getattr(old_value, "specialisation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "specialisation"):
                opp_val = getattr(value, "specialisation", None)
                if opp_val is None:
                    setattr(value, "specialisation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def study_Semester35(self):
        return self.__study_Semester35

    @study_Semester35.setter
    def study_Semester35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Semester__study_Semester35", None)
        self.__study_Semester35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "study_StudyPlan"):
                opp_val = getattr(old_value, "study_StudyPlan", None)
                if opp_val == self:
                    setattr(old_value, "study_StudyPlan", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "study_StudyPlan"):
                opp_val = getattr(value, "study_StudyPlan", None)
                setattr(value, "study_StudyPlan", self)

    @property
    def semesters32(self):
        return self.__semesters32

    @semesters32.setter
    def semesters32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Semester__semesters32", None)
        self.__semesters32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Department33"):
                opp_val = getattr(old_value, "Department33", None)
                if opp_val == self:
                    setattr(old_value, "Department33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Department33"):
                opp_val = getattr(value, "Department33", None)
                setattr(value, "Department33", self)

    @property
    def semesters(self):
        return self.__semesters

    @semesters.setter
    def semesters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Semester__semesters", None)
        self.__semesters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Specialisation29"):
                opp_val = getattr(old_value, "Specialisation29", None)
                if opp_val == self:
                    setattr(old_value, "Specialisation29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Specialisation29"):
                opp_val = getattr(value, "Specialisation29", None)
                setattr(value, "Specialisation29", self)

    @property
    def Semester(self):
        return self.__Semester

    @Semester.setter
    def Semester(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Semester__Semester", None)
        self.__Semester = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "department8"):
                opp_val = getattr(old_value, "department8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "department8"):
                opp_val = getattr(value, "department8", None)
                if opp_val is None:
                    setattr(value, "department8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def study_Semester(self):
        return self.__study_Semester

    @study_Semester.setter
    def study_Semester(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Semester__study_Semester", None)
        self.__study_Semester = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "study_Course"):
                    opp_val = getattr(item, "study_Course", None)
                    
                    if opp_val == self:
                        setattr(item, "study_Course", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "study_Course"):
                    opp_val = getattr(item, "study_Course", None)
                    
                    setattr(item, "study_Course", self)
                    

class study_Specialisation:

    def __init__(self, name: str, requirement: str, Specialisation: "study_Department" = None, Specialisation11: "study_Program" = None, study_Specialisation: "study_Student" = None, specialisations: "study_Program" = None, study_Specialisation21: "study_Student" = None, specialisation: set["study_Semester"] = None, specialisations26: "study_Department" = None, Specialisation29: "study_Semester" = None):
        self.name = name
        self.requirement = requirement
        self.Specialisation = Specialisation
        self.Specialisation11 = Specialisation11
        self.study_Specialisation = study_Specialisation
        self.specialisations = specialisations
        self.study_Specialisation21 = study_Specialisation21
        self.specialisation = specialisation if specialisation is not None else set()
        self.specialisations26 = specialisations26
        self.Specialisation29 = Specialisation29
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def requirement(self) -> str:
        return self.__requirement

    @requirement.setter
    def requirement(self, requirement: str):
        self.__requirement = requirement

    @property
    def specialisation(self):
        return self.__specialisation

    @specialisation.setter
    def specialisation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Specialisation__specialisation", None)
        self.__specialisation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Semester24"):
                    opp_val = getattr(item, "Semester24", None)
                    
                    if opp_val == self:
                        setattr(item, "Semester24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Semester24"):
                    opp_val = getattr(item, "Semester24", None)
                    
                    setattr(item, "Semester24", self)
                    

    @property
    def Specialisation11(self):
        return self.__Specialisation11

    @Specialisation11.setter
    def Specialisation11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Specialisation__Specialisation11", None)
        self.__Specialisation11 = value
        
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
    def Specialisation29(self):
        return self.__Specialisation29

    @Specialisation29.setter
    def Specialisation29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Specialisation__Specialisation29", None)
        self.__Specialisation29 = value
        
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
    def study_Specialisation21(self):
        return self.__study_Specialisation21

    @study_Specialisation21.setter
    def study_Specialisation21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Specialisation__study_Specialisation21", None)
        self.__study_Specialisation21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "study_Student22"):
                opp_val = getattr(old_value, "study_Student22", None)
                if opp_val == self:
                    setattr(old_value, "study_Student22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "study_Student22"):
                opp_val = getattr(value, "study_Student22", None)
                setattr(value, "study_Student22", self)

    @property
    def specialisations26(self):
        return self.__specialisations26

    @specialisations26.setter
    def specialisations26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Specialisation__specialisations26", None)
        self.__specialisations26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Department27"):
                opp_val = getattr(old_value, "Department27", None)
                if opp_val == self:
                    setattr(old_value, "Department27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Department27"):
                opp_val = getattr(value, "Department27", None)
                setattr(value, "Department27", self)

    @property
    def study_Specialisation(self):
        return self.__study_Specialisation

    @study_Specialisation.setter
    def study_Specialisation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Specialisation__study_Specialisation", None)
        self.__study_Specialisation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "study_Student"):
                opp_val = getattr(old_value, "study_Student", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "study_Student"):
                opp_val = getattr(value, "study_Student", None)
                if opp_val is None:
                    setattr(value, "study_Student", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Specialisation(self):
        return self.__Specialisation

    @Specialisation.setter
    def Specialisation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Specialisation__Specialisation", None)
        self.__Specialisation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "department6"):
                opp_val = getattr(old_value, "department6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "department6"):
                opp_val = getattr(value, "department6", None)
                if opp_val is None:
                    setattr(value, "department6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def specialisations(self):
        return self.__specialisations

    @specialisations.setter
    def specialisations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Specialisation__specialisations", None)
        self.__specialisations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Program19"):
                opp_val = getattr(old_value, "Program19", None)
                if opp_val == self:
                    setattr(old_value, "Program19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Program19"):
                opp_val = getattr(value, "Program19", None)
                setattr(value, "Program19", self)

class study_Student:

    def __init__(self, name: str, Student: "study_Department" = None, students: "study_Department" = None, student: "study_StudyPlan" = None, study_Student: set["study_Specialisation"] = None, study_Student22: "study_Specialisation" = None, Student39: "study_StudyPlan" = None):
        self.name = name
        self.Student = Student
        self.students = students
        self.student = student
        self.study_Student = study_Student if study_Student is not None else set()
        self.study_Student22 = study_Student22
        self.Student39 = Student39
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Student39(self):
        return self.__Student39

    @Student39.setter
    def Student39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Student__Student39", None)
        self.__Student39 = value
        
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
    def students(self):
        return self.__students

    @students.setter
    def students(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Student__students", None)
        self.__students = value
        
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
    def study_Student(self):
        return self.__study_Student

    @study_Student.setter
    def study_Student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Student__study_Student", None)
        self.__study_Student = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "study_Specialisation"):
                    opp_val = getattr(item, "study_Specialisation", None)
                    
                    if opp_val == self:
                        setattr(item, "study_Specialisation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "study_Specialisation"):
                    opp_val = getattr(item, "study_Specialisation", None)
                    
                    setattr(item, "study_Specialisation", self)
                    

    @property
    def student(self):
        return self.__student

    @student.setter
    def student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Student__student", None)
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
        old_value = getattr(self, f"_study_Student__Student", None)
        self.__Student = value
        
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
    def study_Student22(self):
        return self.__study_Student22

    @study_Student22.setter
    def study_Student22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Student__study_Student22", None)
        self.__study_Student22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "study_Specialisation21"):
                opp_val = getattr(old_value, "study_Specialisation21", None)
                if opp_val == self:
                    setattr(old_value, "study_Specialisation21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "study_Specialisation21"):
                opp_val = getattr(value, "study_Specialisation21", None)
                setattr(value, "study_Specialisation21", self)

class study_Program:

    def __init__(self, name: str, code: str, numYears: int, Program: "study_Department" = None, programs: "study_Department" = None, program: set["study_Specialisation"] = None, Program19: "study_Specialisation" = None):
        self.name = name
        self.code = code
        self.numYears = numYears
        self.Program = Program
        self.programs = programs
        self.program = program if program is not None else set()
        self.Program19 = Program19
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def numYears(self) -> int:
        return self.__numYears

    @numYears.setter
    def numYears(self, numYears: int):
        self.__numYears = numYears

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def program(self):
        return self.__program

    @program.setter
    def program(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Program__program", None)
        self.__program = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Specialisation11"):
                    opp_val = getattr(item, "Specialisation11", None)
                    
                    if opp_val == self:
                        setattr(item, "Specialisation11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Specialisation11"):
                    opp_val = getattr(item, "Specialisation11", None)
                    
                    setattr(item, "Specialisation11", self)
                    

    @property
    def Program(self):
        return self.__Program

    @Program.setter
    def Program(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Program__Program", None)
        self.__Program = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "department2"):
                opp_val = getattr(old_value, "department2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "department2"):
                opp_val = getattr(value, "department2", None)
                if opp_val is None:
                    setattr(value, "department2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def programs(self):
        return self.__programs

    @programs.setter
    def programs(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Program__programs", None)
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
    def Program19(self):
        return self.__Program19

    @Program19.setter
    def Program19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Program__Program19", None)
        self.__Program19 = value
        
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

class study_Course:

    def __init__(self, season: str, year: int, name: str, code: str, credits: float, Course: "study_Department" = None, courses: "study_Department" = None, study_Course: "study_Semester" = None, study_Course45: "study_courseAllocation" = None):
        self.season = season
        self.year = year
        self.name = name
        self.code = code
        self.credits = credits
        self.Course = Course
        self.courses = courses
        self.study_Course = study_Course
        self.study_Course45 = study_Course45
        
    @property
    def season(self) -> str:
        return self.__season

    @season.setter
    def season(self, season: str):
        self.__season = season

    @property
    def credits(self) -> float:
        return self.__credits

    @credits.setter
    def credits(self, credits: float):
        self.__credits = credits

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
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def Course(self):
        return self.__Course

    @Course.setter
    def Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Course__Course", None)
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
    def study_Course45(self):
        return self.__study_Course45

    @study_Course45.setter
    def study_Course45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Course__study_Course45", None)
        self.__study_Course45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "study_courseAllocation44"):
                opp_val = getattr(old_value, "study_courseAllocation44", None)
                if opp_val == self:
                    setattr(old_value, "study_courseAllocation44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "study_courseAllocation44"):
                opp_val = getattr(value, "study_courseAllocation44", None)
                setattr(value, "study_courseAllocation44", self)

    @property
    def study_Course(self):
        return self.__study_Course

    @study_Course.setter
    def study_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Course__study_Course", None)
        self.__study_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "study_Semester"):
                opp_val = getattr(old_value, "study_Semester", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "study_Semester"):
                opp_val = getattr(value, "study_Semester", None)
                if opp_val is None:
                    setattr(value, "study_Semester", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Course__courses", None)
        self.__courses = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Department17"):
                opp_val = getattr(old_value, "Department17", None)
                if opp_val == self:
                    setattr(old_value, "Department17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Department17"):
                opp_val = getattr(value, "Department17", None)
                setattr(value, "Department17", self)

class study_Department:

    def __init__(self, name: str, code: str, department: set["study_Course"] = None, department2: set["study_Program"] = None, department4: set["study_Student"] = None, department6: set["study_Specialisation"] = None, department8: set["study_Semester"] = None, Department: "study_Program" = None, Department13: "study_Student" = None, Department27: "study_Specialisation" = None, Department17: "study_Course" = None, Department33: "study_Semester" = None):
        self.name = name
        self.code = code
        self.department = department if department is not None else set()
        self.department2 = department2 if department2 is not None else set()
        self.department4 = department4 if department4 is not None else set()
        self.department6 = department6 if department6 is not None else set()
        self.department8 = department8 if department8 is not None else set()
        self.Department = Department
        self.Department13 = Department13
        self.Department27 = Department27
        self.Department17 = Department17
        self.Department33 = Department33
        
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
    def department6(self):
        return self.__department6

    @department6.setter
    def department6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Department__department6", None)
        self.__department6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Specialisation"):
                    opp_val = getattr(item, "Specialisation", None)
                    
                    if opp_val == self:
                        setattr(item, "Specialisation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Specialisation"):
                    opp_val = getattr(item, "Specialisation", None)
                    
                    setattr(item, "Specialisation", self)
                    

    @property
    def department4(self):
        return self.__department4

    @department4.setter
    def department4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Department__department4", None)
        self.__department4 = value if value is not None else set()
        
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
    def department(self):
        return self.__department

    @department.setter
    def department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Department__department", None)
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
    def department2(self):
        return self.__department2

    @department2.setter
    def department2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Department__department2", None)
        self.__department2 = value if value is not None else set()
        
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
    def Department27(self):
        return self.__Department27

    @Department27.setter
    def Department27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Department__Department27", None)
        self.__Department27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "specialisations26"):
                opp_val = getattr(old_value, "specialisations26", None)
                if opp_val == self:
                    setattr(old_value, "specialisations26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "specialisations26"):
                opp_val = getattr(value, "specialisations26", None)
                setattr(value, "specialisations26", self)

    @property
    def Department(self):
        return self.__Department

    @Department.setter
    def Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Department__Department", None)
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
    def Department13(self):
        return self.__Department13

    @Department13.setter
    def Department13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Department__Department13", None)
        self.__Department13 = value
        
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
    def Department33(self):
        return self.__Department33

    @Department33.setter
    def Department33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Department__Department33", None)
        self.__Department33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "semesters32"):
                opp_val = getattr(old_value, "semesters32", None)
                if opp_val == self:
                    setattr(old_value, "semesters32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "semesters32"):
                opp_val = getattr(value, "semesters32", None)
                setattr(value, "semesters32", self)

    @property
    def department8(self):
        return self.__department8

    @department8.setter
    def department8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Department__department8", None)
        self.__department8 = value if value is not None else set()
        
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
    def Department17(self):
        return self.__Department17

    @Department17.setter
    def Department17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Department__Department17", None)
        self.__Department17 = value
        
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
