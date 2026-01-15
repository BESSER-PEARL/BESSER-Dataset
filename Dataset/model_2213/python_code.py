from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class GradeEnum(Enum):
    NONE = "NONE"
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"


############################################
# Definition of Classes
############################################

class study_CourseRelationship:

    def __init__(self, grade: str, numExamAttempts: int, CourseRelationship: "study_IndividualStudyPlan" = None, courses34: "study_IndividualStudyPlan" = None, study_CourseRelationship: "study_Course" = None):
        self.grade = grade
        self.numExamAttempts = numExamAttempts
        self.CourseRelationship = CourseRelationship
        self.courses34 = courses34
        self.study_CourseRelationship = study_CourseRelationship
        
    @property
    def grade(self) -> str:
        return self.__grade

    @grade.setter
    def grade(self, grade: str):
        self.__grade = grade

    @property
    def numExamAttempts(self) -> int:
        return self.__numExamAttempts

    @numExamAttempts.setter
    def numExamAttempts(self, numExamAttempts: int):
        self.__numExamAttempts = numExamAttempts

    @property
    def courses34(self):
        return self.__courses34

    @courses34.setter
    def courses34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_CourseRelationship__courses34", None)
        self.__courses34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IndividualStudyPlan35"):
                opp_val = getattr(old_value, "IndividualStudyPlan35", None)
                if opp_val == self:
                    setattr(old_value, "IndividualStudyPlan35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IndividualStudyPlan35"):
                opp_val = getattr(value, "IndividualStudyPlan35", None)
                setattr(value, "IndividualStudyPlan35", self)

    @property
    def CourseRelationship(self):
        return self.__CourseRelationship

    @CourseRelationship.setter
    def CourseRelationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_CourseRelationship__CourseRelationship", None)
        self.__CourseRelationship = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyPlan32"):
                opp_val = getattr(old_value, "studyPlan32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyPlan32"):
                opp_val = getattr(value, "studyPlan32", None)
                if opp_val is None:
                    setattr(value, "studyPlan32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def study_CourseRelationship(self):
        return self.__study_CourseRelationship

    @study_CourseRelationship.setter
    def study_CourseRelationship(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_CourseRelationship__study_CourseRelationship", None)
        self.__study_CourseRelationship = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "study_Course37"):
                opp_val = getattr(old_value, "study_Course37", None)
                if opp_val == self:
                    setattr(old_value, "study_Course37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "study_Course37"):
                opp_val = getattr(value, "study_Course37", None)
                setattr(value, "study_Course37", self)

class study_IndividualStudyPlan:

    pass
class study_ElectiveCourseList:

    pass
class study_Semester:

    def __init__(self, ordinal: int, Semester: "study_Specialization" = None, semesters: "study_Specialization" = None, study_Semester: set["study_Course"] = None, semester: "study_ElectiveCourseList" = None, Semester21: "study_ElectiveCourseList" = None, study_Semester30: "study_IndividualStudyPlan" = None):
        self.ordinal = ordinal
        self.Semester = Semester
        self.semesters = semesters
        self.study_Semester = study_Semester if study_Semester is not None else set()
        self.semester = semester
        self.Semester21 = Semester21
        self.study_Semester30 = study_Semester30
        
    @property
    def ordinal(self) -> int:
        return self.__ordinal

    @ordinal.setter
    def ordinal(self, ordinal: int):
        self.__ordinal = ordinal

    @property
    def semester(self):
        return self.__semester

    @semester.setter
    def semester(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Semester__semester", None)
        self.__semester = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ElectiveCourseList"):
                opp_val = getattr(old_value, "ElectiveCourseList", None)
                if opp_val == self:
                    setattr(old_value, "ElectiveCourseList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ElectiveCourseList"):
                opp_val = getattr(value, "ElectiveCourseList", None)
                setattr(value, "ElectiveCourseList", self)

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
    def study_Semester30(self):
        return self.__study_Semester30

    @study_Semester30.setter
    def study_Semester30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Semester__study_Semester30", None)
        self.__study_Semester30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "study_IndividualStudyPlan"):
                opp_val = getattr(old_value, "study_IndividualStudyPlan", None)
                if opp_val == self:
                    setattr(old_value, "study_IndividualStudyPlan", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "study_IndividualStudyPlan"):
                opp_val = getattr(value, "study_IndividualStudyPlan", None)
                setattr(value, "study_IndividualStudyPlan", self)

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
            if hasattr(old_value, "Specialization15"):
                opp_val = getattr(old_value, "Specialization15", None)
                if opp_val == self:
                    setattr(old_value, "Specialization15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Specialization15"):
                opp_val = getattr(value, "Specialization15", None)
                setattr(value, "Specialization15", self)

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
                    

    @property
    def Semester21(self):
        return self.__Semester21

    @Semester21.setter
    def Semester21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Semester__Semester21", None)
        self.__Semester21 = value
        
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

class study_StudyProgramme:

    def __init__(self, code: str, name: str, numYears: int, studyProgrammes: "study_University" = None, studyProgramme: set["study_Specialization"] = None, study_StudyProgramme: set["study_Specialization"] = None, StudyProgramme: "study_University" = None, StudyProgramme9: "study_Specialization" = None):
        self.code = code
        self.name = name
        self.numYears = numYears
        self.studyProgrammes = studyProgrammes
        self.studyProgramme = studyProgramme if studyProgramme is not None else set()
        self.study_StudyProgramme = study_StudyProgramme if study_StudyProgramme is not None else set()
        self.StudyProgramme = StudyProgramme
        self.StudyProgramme9 = StudyProgramme9
        
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
    def numYears(self) -> int:
        return self.__numYears

    @numYears.setter
    def numYears(self, numYears: int):
        self.__numYears = numYears

    @property
    def StudyProgramme9(self):
        return self.__StudyProgramme9

    @StudyProgramme9.setter
    def StudyProgramme9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_StudyProgramme__StudyProgramme9", None)
        self.__StudyProgramme9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "allSpecializations"):
                opp_val = getattr(old_value, "allSpecializations", None)
                if opp_val == self:
                    setattr(old_value, "allSpecializations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "allSpecializations"):
                opp_val = getattr(value, "allSpecializations", None)
                setattr(value, "allSpecializations", self)

    @property
    def studyProgrammes(self):
        return self.__studyProgrammes

    @studyProgrammes.setter
    def studyProgrammes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_StudyProgramme__studyProgrammes", None)
        self.__studyProgrammes = value
        
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
    def StudyProgramme(self):
        return self.__StudyProgramme

    @StudyProgramme.setter
    def StudyProgramme(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_StudyProgramme__StudyProgramme", None)
        self.__StudyProgramme = value
        
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
    def study_StudyProgramme(self):
        return self.__study_StudyProgramme

    @study_StudyProgramme.setter
    def study_StudyProgramme(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_StudyProgramme__study_StudyProgramme", None)
        self.__study_StudyProgramme = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "study_Specialization"):
                    opp_val = getattr(item, "study_Specialization", None)
                    
                    if opp_val == self:
                        setattr(item, "study_Specialization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "study_Specialization"):
                    opp_val = getattr(item, "study_Specialization", None)
                    
                    setattr(item, "study_Specialization", self)
                    

    @property
    def studyProgramme(self):
        return self.__studyProgramme

    @studyProgramme.setter
    def studyProgramme(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_StudyProgramme__studyProgramme", None)
        self.__studyProgramme = value if value is not None else set()
        
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
                    

class study_University:

    def __init__(self, name: str, university2: set["study_Course"] = None, university4: set["study_Student"] = None, University: "study_StudyProgramme" = None, university: set["study_StudyProgramme"] = None, University25: "study_Student" = None, University19: "study_Course" = None):
        self.name = name
        self.university2 = university2 if university2 is not None else set()
        self.university4 = university4 if university4 is not None else set()
        self.University = University
        self.university = university if university is not None else set()
        self.University25 = University25
        self.University19 = University19
        
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
        old_value = getattr(self, f"_study_University__University", None)
        self.__University = value
        
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
    def university(self):
        return self.__university

    @university.setter
    def university(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_University__university", None)
        self.__university = value if value is not None else set()
        
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
    def university4(self):
        return self.__university4

    @university4.setter
    def university4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_University__university4", None)
        self.__university4 = value if value is not None else set()
        
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
    def university2(self):
        return self.__university2

    @university2.setter
    def university2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_University__university2", None)
        self.__university2 = value if value is not None else set()
        
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
    def University19(self):
        return self.__University19

    @University19.setter
    def University19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_University__University19", None)
        self.__University19 = value
        
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
    def University25(self):
        return self.__University25

    @University25.setter
    def University25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_University__University25", None)
        self.__University25 = value
        
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

class study_Specialization:

    def __init__(self, numYears: int, name: str, Specialization: "study_StudyProgramme" = None, study_Specialization: "study_StudyProgramme" = None, specialization: set["study_Semester"] = None, study_Specialization13: "study_Specialization" = None, study_Specialization11: set["study_Specialization"] = None, Specialization15: "study_Semester" = None, allSpecializations: "study_StudyProgramme" = None):
        self.numYears = numYears
        self.name = name
        self.Specialization = Specialization
        self.study_Specialization = study_Specialization
        self.specialization = specialization if specialization is not None else set()
        self.study_Specialization13 = study_Specialization13
        self.study_Specialization11 = study_Specialization11 if study_Specialization11 is not None else set()
        self.Specialization15 = Specialization15
        self.allSpecializations = allSpecializations
        
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
    def study_Specialization(self):
        return self.__study_Specialization

    @study_Specialization.setter
    def study_Specialization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Specialization__study_Specialization", None)
        self.__study_Specialization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "study_StudyProgramme"):
                opp_val = getattr(old_value, "study_StudyProgramme", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "study_StudyProgramme"):
                opp_val = getattr(value, "study_StudyProgramme", None)
                if opp_val is None:
                    setattr(value, "study_StudyProgramme", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Specialization15(self):
        return self.__Specialization15

    @Specialization15.setter
    def Specialization15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Specialization__Specialization15", None)
        self.__Specialization15 = value
        
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
    def study_Specialization11(self):
        return self.__study_Specialization11

    @study_Specialization11.setter
    def study_Specialization11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Specialization__study_Specialization11", None)
        self.__study_Specialization11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "study_Specialization13"):
                    opp_val = getattr(item, "study_Specialization13", None)
                    
                    if opp_val == self:
                        setattr(item, "study_Specialization13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "study_Specialization13"):
                    opp_val = getattr(item, "study_Specialization13", None)
                    
                    setattr(item, "study_Specialization13", self)
                    

    @property
    def specialization(self):
        return self.__specialization

    @specialization.setter
    def specialization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Specialization__specialization", None)
        self.__specialization = value if value is not None else set()
        
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
    def Specialization(self):
        return self.__Specialization

    @Specialization.setter
    def Specialization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Specialization__Specialization", None)
        self.__Specialization = value
        
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
    def study_Specialization13(self):
        return self.__study_Specialization13

    @study_Specialization13.setter
    def study_Specialization13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Specialization__study_Specialization13", None)
        self.__study_Specialization13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "study_Specialization11"):
                opp_val = getattr(old_value, "study_Specialization11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "study_Specialization11"):
                opp_val = getattr(value, "study_Specialization11", None)
                if opp_val is None:
                    setattr(value, "study_Specialization11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def allSpecializations(self):
        return self.__allSpecializations

    @allSpecializations.setter
    def allSpecializations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Specialization__allSpecializations", None)
        self.__allSpecializations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StudyProgramme9"):
                opp_val = getattr(old_value, "StudyProgramme9", None)
                if opp_val == self:
                    setattr(old_value, "StudyProgramme9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StudyProgramme9"):
                opp_val = getattr(value, "StudyProgramme9", None)
                setattr(value, "StudyProgramme9", self)

class study_Student:

    def __init__(self, username: str, name: str, Student: "study_University" = None, students: "study_University" = None, student: "study_IndividualStudyPlan" = None, Student28: "study_IndividualStudyPlan" = None):
        self.username = username
        self.name = name
        self.Student = Student
        self.students = students
        self.student = student
        self.Student28 = Student28
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, username: str):
        self.__username = username

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
            if hasattr(old_value, "University25"):
                opp_val = getattr(old_value, "University25", None)
                if opp_val == self:
                    setattr(old_value, "University25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "University25"):
                opp_val = getattr(value, "University25", None)
                setattr(value, "University25", self)

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
            if hasattr(old_value, "IndividualStudyPlan"):
                opp_val = getattr(old_value, "IndividualStudyPlan", None)
                if opp_val == self:
                    setattr(old_value, "IndividualStudyPlan", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IndividualStudyPlan"):
                opp_val = getattr(value, "IndividualStudyPlan", None)
                setattr(value, "IndividualStudyPlan", self)

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
            if hasattr(old_value, "university4"):
                opp_val = getattr(old_value, "university4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "university4"):
                opp_val = getattr(value, "university4", None)
                if opp_val is None:
                    setattr(value, "university4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Student28(self):
        return self.__Student28

    @Student28.setter
    def Student28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Student__Student28", None)
        self.__Student28 = value
        
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

class study_Course:

    def __init__(self, code: str, name: str, credits: float, level: int, Course: "study_University" = None, study_Course: "study_Semester" = None, study_Course23: "study_ElectiveCourseList" = None, courses: "study_University" = None, study_Course37: "study_CourseRelationship" = None):
        self.code = code
        self.name = name
        self.credits = credits
        self.level = level
        self.Course = Course
        self.study_Course = study_Course
        self.study_Course23 = study_Course23
        self.courses = courses
        self.study_Course37 = study_Course37
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

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
    def study_Course37(self):
        return self.__study_Course37

    @study_Course37.setter
    def study_Course37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Course__study_Course37", None)
        self.__study_Course37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "study_CourseRelationship"):
                opp_val = getattr(old_value, "study_CourseRelationship", None)
                if opp_val == self:
                    setattr(old_value, "study_CourseRelationship", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "study_CourseRelationship"):
                opp_val = getattr(value, "study_CourseRelationship", None)
                setattr(value, "study_CourseRelationship", self)

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
            if hasattr(old_value, "university2"):
                opp_val = getattr(old_value, "university2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "university2"):
                opp_val = getattr(value, "university2", None)
                if opp_val is None:
                    setattr(value, "university2", set([self]))
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
            if hasattr(old_value, "University19"):
                opp_val = getattr(old_value, "University19", None)
                if opp_val == self:
                    setattr(old_value, "University19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "University19"):
                opp_val = getattr(value, "University19", None)
                setattr(value, "University19", self)

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
    def study_Course23(self):
        return self.__study_Course23

    @study_Course23.setter
    def study_Course23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Course__study_Course23", None)
        self.__study_Course23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "study_ElectiveCourseList"):
                opp_val = getattr(old_value, "study_ElectiveCourseList", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "study_ElectiveCourseList"):
                opp_val = getattr(value, "study_ElectiveCourseList", None)
                if opp_val is None:
                    setattr(value, "study_ElectiveCourseList", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
