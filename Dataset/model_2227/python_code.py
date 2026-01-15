from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ProgrammeCode(Enum):
    MIDT = "MIDT"
    BIT = "BIT"
    MIT = "MIT"
    MTIOT = "MTIOT"
    MTPROD = "MTPROD"
    MTDT = "MTDT"
class ProgrammeType(Enum):
    Bachelors = "Bachelors"
    Masters = "Masters"
    IntegratedMaster = "IntegratedMaster"


############################################
# Definition of Classes
############################################

class CourseSlot:

    pass
class studyprogramme_CompulsoryCourseSlot(CourseSlot):

    pass
class studyprogramme_University:

    def __init__(self, name: str, studyprogramme_University18: set["studyprogramme_Course"] = None, studyprogramme_University21: set["studyprogramme_Semester"] = None, studyprogramme_University24: set["studyprogramme_Specialization"] = None, studyprogramme_University: set["studyprogramme_Programme"] = None):
        self.name = name
        self.studyprogramme_University18 = studyprogramme_University18 if studyprogramme_University18 is not None else set()
        self.studyprogramme_University21 = studyprogramme_University21 if studyprogramme_University21 is not None else set()
        self.studyprogramme_University24 = studyprogramme_University24 if studyprogramme_University24 is not None else set()
        self.studyprogramme_University = studyprogramme_University if studyprogramme_University is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def studyprogramme_University(self):
        return self.__studyprogramme_University

    @studyprogramme_University.setter
    def studyprogramme_University(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogramme_University__studyprogramme_University", None)
        self.__studyprogramme_University = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "studyprogramme_Programme"):
                    opp_val = getattr(item, "studyprogramme_Programme", None)
                    
                    if opp_val == self:
                        setattr(item, "studyprogramme_Programme", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "studyprogramme_Programme"):
                    opp_val = getattr(item, "studyprogramme_Programme", None)
                    
                    setattr(item, "studyprogramme_Programme", self)
                    

    @property
    def studyprogramme_University24(self):
        return self.__studyprogramme_University24

    @studyprogramme_University24.setter
    def studyprogramme_University24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogramme_University__studyprogramme_University24", None)
        self.__studyprogramme_University24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "studyprogramme_Specialization"):
                    opp_val = getattr(item, "studyprogramme_Specialization", None)
                    
                    if opp_val == self:
                        setattr(item, "studyprogramme_Specialization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "studyprogramme_Specialization"):
                    opp_val = getattr(item, "studyprogramme_Specialization", None)
                    
                    setattr(item, "studyprogramme_Specialization", self)
                    

    @property
    def studyprogramme_University21(self):
        return self.__studyprogramme_University21

    @studyprogramme_University21.setter
    def studyprogramme_University21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogramme_University__studyprogramme_University21", None)
        self.__studyprogramme_University21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "studyprogramme_Semester22"):
                    opp_val = getattr(item, "studyprogramme_Semester22", None)
                    
                    if opp_val == self:
                        setattr(item, "studyprogramme_Semester22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "studyprogramme_Semester22"):
                    opp_val = getattr(item, "studyprogramme_Semester22", None)
                    
                    setattr(item, "studyprogramme_Semester22", self)
                    

    @property
    def studyprogramme_University18(self):
        return self.__studyprogramme_University18

    @studyprogramme_University18.setter
    def studyprogramme_University18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogramme_University__studyprogramme_University18", None)
        self.__studyprogramme_University18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "studyprogramme_Course19"):
                    opp_val = getattr(item, "studyprogramme_Course19", None)
                    
                    if opp_val == self:
                        setattr(item, "studyprogramme_Course19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "studyprogramme_Course19"):
                    opp_val = getattr(item, "studyprogramme_Course19", None)
                    
                    setattr(item, "studyprogramme_Course19", self)
                    

class studyprogramme_ElectiveCourseSlot(CourseSlot):

    pass
class studyprogramme_CourseSlot:

    pass
class studyprogramme_Semester:

    def __init__(self, semesterNumber: int, studyprogramme_Semester12: "studyprogramme_SemesterContainer" = None, studyprogramme_Semester: set["studyprogramme_CourseSlot"] = None, studyprogramme_Semester22: "studyprogramme_University" = None):
        self.semesterNumber = semesterNumber
        self.studyprogramme_Semester12 = studyprogramme_Semester12
        self.studyprogramme_Semester = studyprogramme_Semester if studyprogramme_Semester is not None else set()
        self.studyprogramme_Semester22 = studyprogramme_Semester22
        
    @property
    def semesterNumber(self) -> int:
        return self.__semesterNumber

    @semesterNumber.setter
    def semesterNumber(self, semesterNumber: int):
        self.__semesterNumber = semesterNumber

    @property
    def studyprogramme_Semester(self):
        return self.__studyprogramme_Semester

    @studyprogramme_Semester.setter
    def studyprogramme_Semester(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogramme_Semester__studyprogramme_Semester", None)
        self.__studyprogramme_Semester = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "studyprogramme_CourseSlot"):
                    opp_val = getattr(item, "studyprogramme_CourseSlot", None)
                    
                    if opp_val == self:
                        setattr(item, "studyprogramme_CourseSlot", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "studyprogramme_CourseSlot"):
                    opp_val = getattr(item, "studyprogramme_CourseSlot", None)
                    
                    setattr(item, "studyprogramme_CourseSlot", self)
                    

    @property
    def studyprogramme_Semester22(self):
        return self.__studyprogramme_Semester22

    @studyprogramme_Semester22.setter
    def studyprogramme_Semester22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogramme_Semester__studyprogramme_Semester22", None)
        self.__studyprogramme_Semester22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyprogramme_University21"):
                opp_val = getattr(old_value, "studyprogramme_University21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyprogramme_University21"):
                opp_val = getattr(value, "studyprogramme_University21", None)
                if opp_val is None:
                    setattr(value, "studyprogramme_University21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def studyprogramme_Semester12(self):
        return self.__studyprogramme_Semester12

    @studyprogramme_Semester12.setter
    def studyprogramme_Semester12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogramme_Semester__studyprogramme_Semester12", None)
        self.__studyprogramme_Semester12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyprogramme_SemesterContainer"):
                opp_val = getattr(old_value, "studyprogramme_SemesterContainer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyprogramme_SemesterContainer"):
                opp_val = getattr(value, "studyprogramme_SemesterContainer", None)
                if opp_val is None:
                    setattr(value, "studyprogramme_SemesterContainer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class studyprogramme_ElectiveCourseList:

    def __init__(self, name: str, studyprogramme_ElectiveCourseList: set["studyprogramme_Course"] = None, electiveCourseList: "studyprogramme_ElectiveCourseSlot" = None, ElectiveCourseList: "studyprogramme_ElectiveCourseSlot" = None):
        self.name = name
        self.studyprogramme_ElectiveCourseList = studyprogramme_ElectiveCourseList if studyprogramme_ElectiveCourseList is not None else set()
        self.electiveCourseList = electiveCourseList
        self.ElectiveCourseList = ElectiveCourseList
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def studyprogramme_ElectiveCourseList(self):
        return self.__studyprogramme_ElectiveCourseList

    @studyprogramme_ElectiveCourseList.setter
    def studyprogramme_ElectiveCourseList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogramme_ElectiveCourseList__studyprogramme_ElectiveCourseList", None)
        self.__studyprogramme_ElectiveCourseList = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "studyprogramme_Course14"):
                    opp_val = getattr(item, "studyprogramme_Course14", None)
                    
                    if opp_val == self:
                        setattr(item, "studyprogramme_Course14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "studyprogramme_Course14"):
                    opp_val = getattr(item, "studyprogramme_Course14", None)
                    
                    setattr(item, "studyprogramme_Course14", self)
                    

    @property
    def electiveCourseList(self):
        return self.__electiveCourseList

    @electiveCourseList.setter
    def electiveCourseList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogramme_ElectiveCourseList__electiveCourseList", None)
        self.__electiveCourseList = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ElectiveCourseSlot"):
                opp_val = getattr(old_value, "ElectiveCourseSlot", None)
                if opp_val == self:
                    setattr(old_value, "ElectiveCourseSlot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ElectiveCourseSlot"):
                opp_val = getattr(value, "ElectiveCourseSlot", None)
                setattr(value, "ElectiveCourseSlot", self)

    @property
    def ElectiveCourseList(self):
        return self.__ElectiveCourseList

    @ElectiveCourseList.setter
    def ElectiveCourseList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogramme_ElectiveCourseList__ElectiveCourseList", None)
        self.__ElectiveCourseList = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "electiveCourseSlot"):
                opp_val = getattr(old_value, "electiveCourseSlot", None)
                if opp_val == self:
                    setattr(old_value, "electiveCourseSlot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "electiveCourseSlot"):
                opp_val = getattr(value, "electiveCourseSlot", None)
                setattr(value, "electiveCourseSlot", self)

class studyprogramme_SemesterContainer:

    pass
class studyprogramme_Course:

    def __init__(self, level: int, displayedName: str, name: str, courseCode: str, credits: float, studyprogramme_Course: "studyprogramme_CourseSlot" = None, studyprogramme_Course14: "studyprogramme_ElectiveCourseList" = None, studyprogramme_Course19: "studyprogramme_University" = None, studyprogramme_Course27: "studyprogramme_ElectiveCourseSlot" = None):
        self.level = level
        self.displayedName = displayedName
        self.name = name
        self.courseCode = courseCode
        self.credits = credits
        self.studyprogramme_Course = studyprogramme_Course
        self.studyprogramme_Course14 = studyprogramme_Course14
        self.studyprogramme_Course19 = studyprogramme_Course19
        self.studyprogramme_Course27 = studyprogramme_Course27
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def courseCode(self) -> str:
        return self.__courseCode

    @courseCode.setter
    def courseCode(self, courseCode: str):
        self.__courseCode = courseCode

    @property
    def level(self) -> int:
        return self.__level

    @level.setter
    def level(self, level: int):
        self.__level = level

    @property
    def displayedName(self) -> str:
        return self.__displayedName

    @displayedName.setter
    def displayedName(self, displayedName: str):
        self.__displayedName = displayedName

    @property
    def credits(self) -> float:
        return self.__credits

    @credits.setter
    def credits(self, credits: float):
        self.__credits = credits

    @property
    def studyprogramme_Course(self):
        return self.__studyprogramme_Course

    @studyprogramme_Course.setter
    def studyprogramme_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogramme_Course__studyprogramme_Course", None)
        self.__studyprogramme_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyprogramme_CourseSlot10"):
                opp_val = getattr(old_value, "studyprogramme_CourseSlot10", None)
                if opp_val == self:
                    setattr(old_value, "studyprogramme_CourseSlot10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyprogramme_CourseSlot10"):
                opp_val = getattr(value, "studyprogramme_CourseSlot10", None)
                setattr(value, "studyprogramme_CourseSlot10", self)

    @property
    def studyprogramme_Course27(self):
        return self.__studyprogramme_Course27

    @studyprogramme_Course27.setter
    def studyprogramme_Course27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogramme_Course__studyprogramme_Course27", None)
        self.__studyprogramme_Course27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyprogramme_ElectiveCourseSlot"):
                opp_val = getattr(old_value, "studyprogramme_ElectiveCourseSlot", None)
                if opp_val == self:
                    setattr(old_value, "studyprogramme_ElectiveCourseSlot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyprogramme_ElectiveCourseSlot"):
                opp_val = getattr(value, "studyprogramme_ElectiveCourseSlot", None)
                setattr(value, "studyprogramme_ElectiveCourseSlot", self)

    @property
    def studyprogramme_Course14(self):
        return self.__studyprogramme_Course14

    @studyprogramme_Course14.setter
    def studyprogramme_Course14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogramme_Course__studyprogramme_Course14", None)
        self.__studyprogramme_Course14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyprogramme_ElectiveCourseList"):
                opp_val = getattr(old_value, "studyprogramme_ElectiveCourseList", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyprogramme_ElectiveCourseList"):
                opp_val = getattr(value, "studyprogramme_ElectiveCourseList", None)
                if opp_val is None:
                    setattr(value, "studyprogramme_ElectiveCourseList", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def studyprogramme_Course19(self):
        return self.__studyprogramme_Course19

    @studyprogramme_Course19.setter
    def studyprogramme_Course19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogramme_Course__studyprogramme_Course19", None)
        self.__studyprogramme_Course19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyprogramme_University18"):
                opp_val = getattr(old_value, "studyprogramme_University18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyprogramme_University18"):
                opp_val = getattr(value, "studyprogramme_University18", None)
                if opp_val is None:
                    setattr(value, "studyprogramme_University18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SemesterContainer:

    pass
class studyprogramme_Specialization(SemesterContainer):

    def __init__(self, selectionSemester: int, name: str, specializations: "studyprogramme_Programme" = None, Specialization4: "studyprogramme_Specialization" = None, parrentSpecialisation: set["studyprogramme_Specialization"] = None, Specialization: "studyprogramme_Programme" = None, Specialization7: "studyprogramme_Specialization" = None, subSpecialisations: "studyprogramme_Specialization" = None, studyprogramme_Specialization: "studyprogramme_University" = None):
        self.selectionSemester = selectionSemester
        self.name = name
        self.specializations = specializations
        self.Specialization4 = Specialization4
        self.parrentSpecialisation = parrentSpecialisation if parrentSpecialisation is not None else set()
        self.Specialization = Specialization
        self.Specialization7 = Specialization7
        self.subSpecialisations = subSpecialisations
        self.studyprogramme_Specialization = studyprogramme_Specialization
        
    @property
    def selectionSemester(self) -> int:
        return self.__selectionSemester

    @selectionSemester.setter
    def selectionSemester(self, selectionSemester: int):
        self.__selectionSemester = selectionSemester

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def subSpecialisations(self):
        return self.__subSpecialisations

    @subSpecialisations.setter
    def subSpecialisations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogramme_Specialization__subSpecialisations", None)
        self.__subSpecialisations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Specialization7"):
                opp_val = getattr(old_value, "Specialization7", None)
                if opp_val == self:
                    setattr(old_value, "Specialization7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Specialization7"):
                opp_val = getattr(value, "Specialization7", None)
                setattr(value, "Specialization7", self)

    @property
    def parrentSpecialisation(self):
        return self.__parrentSpecialisation

    @parrentSpecialisation.setter
    def parrentSpecialisation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogramme_Specialization__parrentSpecialisation", None)
        self.__parrentSpecialisation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Specialization4"):
                    opp_val = getattr(item, "Specialization4", None)
                    
                    if opp_val == self:
                        setattr(item, "Specialization4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Specialization4"):
                    opp_val = getattr(item, "Specialization4", None)
                    
                    setattr(item, "Specialization4", self)
                    

    @property
    def specializations(self):
        return self.__specializations

    @specializations.setter
    def specializations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogramme_Specialization__specializations", None)
        self.__specializations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Programme"):
                opp_val = getattr(old_value, "Programme", None)
                if opp_val == self:
                    setattr(old_value, "Programme", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Programme"):
                opp_val = getattr(value, "Programme", None)
                setattr(value, "Programme", self)

    @property
    def Specialization(self):
        return self.__Specialization

    @Specialization.setter
    def Specialization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogramme_Specialization__Specialization", None)
        self.__Specialization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "programme"):
                opp_val = getattr(old_value, "programme", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "programme"):
                opp_val = getattr(value, "programme", None)
                if opp_val is None:
                    setattr(value, "programme", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Specialization7(self):
        return self.__Specialization7

    @Specialization7.setter
    def Specialization7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogramme_Specialization__Specialization7", None)
        self.__Specialization7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "subSpecialisations"):
                opp_val = getattr(old_value, "subSpecialisations", None)
                if opp_val == self:
                    setattr(old_value, "subSpecialisations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "subSpecialisations"):
                opp_val = getattr(value, "subSpecialisations", None)
                setattr(value, "subSpecialisations", self)

    @property
    def Specialization4(self):
        return self.__Specialization4

    @Specialization4.setter
    def Specialization4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogramme_Specialization__Specialization4", None)
        self.__Specialization4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "parrentSpecialisation"):
                opp_val = getattr(old_value, "parrentSpecialisation", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "parrentSpecialisation"):
                opp_val = getattr(value, "parrentSpecialisation", None)
                if opp_val is None:
                    setattr(value, "parrentSpecialisation", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def studyprogramme_Specialization(self):
        return self.__studyprogramme_Specialization

    @studyprogramme_Specialization.setter
    def studyprogramme_Specialization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogramme_Specialization__studyprogramme_Specialization", None)
        self.__studyprogramme_Specialization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyprogramme_University24"):
                opp_val = getattr(old_value, "studyprogramme_University24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyprogramme_University24"):
                opp_val = getattr(value, "studyprogramme_University24", None)
                if opp_val is None:
                    setattr(value, "studyprogramme_University24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class studyprogramme_Programme(SemesterContainer):

    def __init__(self, name: str, programmeCode: str, numberOfYears: int, programmeType: str, Programme: "studyprogramme_Specialization" = None, programme: set["studyprogramme_Specialization"] = None, studyprogramme_Programme: "studyprogramme_University" = None):
        self.name = name
        self.programmeCode = programmeCode
        self.numberOfYears = numberOfYears
        self.programmeType = programmeType
        self.Programme = Programme
        self.programme = programme if programme is not None else set()
        self.studyprogramme_Programme = studyprogramme_Programme
        
    @property
    def programmeType(self) -> str:
        return self.__programmeType

    @programmeType.setter
    def programmeType(self, programmeType: str):
        self.__programmeType = programmeType

    @property
    def programmeCode(self) -> str:
        return self.__programmeCode

    @programmeCode.setter
    def programmeCode(self, programmeCode: str):
        self.__programmeCode = programmeCode

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def numberOfYears(self) -> int:
        return self.__numberOfYears

    @numberOfYears.setter
    def numberOfYears(self, numberOfYears: int):
        self.__numberOfYears = numberOfYears

    @property
    def Programme(self):
        return self.__Programme

    @Programme.setter
    def Programme(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogramme_Programme__Programme", None)
        self.__Programme = value
        
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
    def programme(self):
        return self.__programme

    @programme.setter
    def programme(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogramme_Programme__programme", None)
        self.__programme = value if value is not None else set()
        
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
    def studyprogramme_Programme(self):
        return self.__studyprogramme_Programme

    @studyprogramme_Programme.setter
    def studyprogramme_Programme(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogramme_Programme__studyprogramme_Programme", None)
        self.__studyprogramme_Programme = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyprogramme_University"):
                opp_val = getattr(old_value, "studyprogramme_University", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyprogramme_University"):
                opp_val = getattr(value, "studyprogramme_University", None)
                if opp_val is None:
                    setattr(value, "studyprogramme_University", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
