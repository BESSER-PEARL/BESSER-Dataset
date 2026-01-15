from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class semesterType(Enum):
    fall = "fall"
    spring = "spring"
class courseType(Enum):
    mandatory = "mandatory"
    elective = "elective"
class courseLevel(Enum):
    high = "high"
    basic = "basic"
    medium = "medium"


############################################
# Definition of Classes
############################################

class ntnustudies_Department:

    def __init__(self, name: str, shortName: str, ntnustudies_Department: set["ntnustudies_Course"] = None, ntnustudies_Department30: set["ntnustudies_Programme"] = None):
        self.name = name
        self.shortName = shortName
        self.ntnustudies_Department = ntnustudies_Department if ntnustudies_Department is not None else set()
        self.ntnustudies_Department30 = ntnustudies_Department30 if ntnustudies_Department30 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def shortName(self) -> str:
        return self.__shortName

    @shortName.setter
    def shortName(self, shortName: str):
        self.__shortName = shortName

    @property
    def ntnustudies_Department30(self):
        return self.__ntnustudies_Department30

    @ntnustudies_Department30.setter
    def ntnustudies_Department30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ntnustudies_Department__ntnustudies_Department30", None)
        self.__ntnustudies_Department30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ntnustudies_Programme31"):
                    opp_val = getattr(item, "ntnustudies_Programme31", None)
                    
                    if opp_val == self:
                        setattr(item, "ntnustudies_Programme31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ntnustudies_Programme31"):
                    opp_val = getattr(item, "ntnustudies_Programme31", None)
                    
                    setattr(item, "ntnustudies_Programme31", self)
                    

    @property
    def ntnustudies_Department(self):
        return self.__ntnustudies_Department

    @ntnustudies_Department.setter
    def ntnustudies_Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ntnustudies_Department__ntnustudies_Department", None)
        self.__ntnustudies_Department = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ntnustudies_Course28"):
                    opp_val = getattr(item, "ntnustudies_Course28", None)
                    
                    if opp_val == self:
                        setattr(item, "ntnustudies_Course28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ntnustudies_Course28"):
                    opp_val = getattr(item, "ntnustudies_Course28", None)
                    
                    setattr(item, "ntnustudies_Course28", self)
                    

class ntnustudies_StudyPlan:

    pass
class ntnustudies_ChosenSemester:

    pass
class ntnustudies_Semester:

    def __init__(self, type: str, year: int, Semester: "ntnustudies_Programme" = None, ntnustudies_Semester16: "ntnustudies_ChosenSemester" = None, ntnustudies_Semester: "ntnustudies_Specialization" = None, ntnustudies_Semester11: set["ntnustudies_Course"] = None, semesters: "ntnustudies_Programme" = None):
        self.type = type
        self.year = year
        self.Semester = Semester
        self.ntnustudies_Semester16 = ntnustudies_Semester16
        self.ntnustudies_Semester = ntnustudies_Semester
        self.ntnustudies_Semester11 = ntnustudies_Semester11 if ntnustudies_Semester11 is not None else set()
        self.semesters = semesters
        
    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def ntnustudies_Semester16(self):
        return self.__ntnustudies_Semester16

    @ntnustudies_Semester16.setter
    def ntnustudies_Semester16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ntnustudies_Semester__ntnustudies_Semester16", None)
        self.__ntnustudies_Semester16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ntnustudies_ChosenSemester"):
                opp_val = getattr(old_value, "ntnustudies_ChosenSemester", None)
                if opp_val == self:
                    setattr(old_value, "ntnustudies_ChosenSemester", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ntnustudies_ChosenSemester"):
                opp_val = getattr(value, "ntnustudies_ChosenSemester", None)
                setattr(value, "ntnustudies_ChosenSemester", self)

    @property
    def ntnustudies_Semester11(self):
        return self.__ntnustudies_Semester11

    @ntnustudies_Semester11.setter
    def ntnustudies_Semester11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ntnustudies_Semester__ntnustudies_Semester11", None)
        self.__ntnustudies_Semester11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ntnustudies_Course12"):
                    opp_val = getattr(item, "ntnustudies_Course12", None)
                    
                    if opp_val == self:
                        setattr(item, "ntnustudies_Course12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ntnustudies_Course12"):
                    opp_val = getattr(item, "ntnustudies_Course12", None)
                    
                    setattr(item, "ntnustudies_Course12", self)
                    

    @property
    def semesters(self):
        return self.__semesters

    @semesters.setter
    def semesters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ntnustudies_Semester__semesters", None)
        self.__semesters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Programme14"):
                opp_val = getattr(old_value, "Programme14", None)
                if opp_val == self:
                    setattr(old_value, "Programme14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Programme14"):
                opp_val = getattr(value, "Programme14", None)
                setattr(value, "Programme14", self)

    @property
    def Semester(self):
        return self.__Semester

    @Semester.setter
    def Semester(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ntnustudies_Semester__Semester", None)
        self.__Semester = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "programme2"):
                opp_val = getattr(old_value, "programme2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "programme2"):
                opp_val = getattr(value, "programme2", None)
                if opp_val is None:
                    setattr(value, "programme2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ntnustudies_Semester(self):
        return self.__ntnustudies_Semester

    @ntnustudies_Semester.setter
    def ntnustudies_Semester(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ntnustudies_Semester__ntnustudies_Semester", None)
        self.__ntnustudies_Semester = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ntnustudies_Specialization9"):
                opp_val = getattr(old_value, "ntnustudies_Specialization9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ntnustudies_Specialization9"):
                opp_val = getattr(value, "ntnustudies_Specialization9", None)
                if opp_val is None:
                    setattr(value, "ntnustudies_Specialization9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ntnustudies_Specialization:

    def __init__(self, name: str, specializationChoicePointSemester: int, ntnustudies_Specialization: set["ntnustudies_Course"] = None, ntnustudies_Specialization7: "ntnustudies_Specialization" = None, ntnustudies_Specialization5: "ntnustudies_Specialization" = None, Specialization: "ntnustudies_Programme" = None, specializations: "ntnustudies_Programme" = None, ntnustudies_Specialization9: set["ntnustudies_Semester"] = None, ntnustudies_Specialization23: "ntnustudies_StudyPlan" = None):
        self.name = name
        self.specializationChoicePointSemester = specializationChoicePointSemester
        self.ntnustudies_Specialization = ntnustudies_Specialization if ntnustudies_Specialization is not None else set()
        self.ntnustudies_Specialization7 = ntnustudies_Specialization7
        self.ntnustudies_Specialization5 = ntnustudies_Specialization5
        self.Specialization = Specialization
        self.specializations = specializations
        self.ntnustudies_Specialization9 = ntnustudies_Specialization9 if ntnustudies_Specialization9 is not None else set()
        self.ntnustudies_Specialization23 = ntnustudies_Specialization23
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def specializationChoicePointSemester(self) -> int:
        return self.__specializationChoicePointSemester

    @specializationChoicePointSemester.setter
    def specializationChoicePointSemester(self, specializationChoicePointSemester: int):
        self.__specializationChoicePointSemester = specializationChoicePointSemester

    @property
    def ntnustudies_Specialization23(self):
        return self.__ntnustudies_Specialization23

    @ntnustudies_Specialization23.setter
    def ntnustudies_Specialization23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ntnustudies_Specialization__ntnustudies_Specialization23", None)
        self.__ntnustudies_Specialization23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ntnustudies_StudyPlan22"):
                opp_val = getattr(old_value, "ntnustudies_StudyPlan22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ntnustudies_StudyPlan22"):
                opp_val = getattr(value, "ntnustudies_StudyPlan22", None)
                if opp_val is None:
                    setattr(value, "ntnustudies_StudyPlan22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ntnustudies_Specialization9(self):
        return self.__ntnustudies_Specialization9

    @ntnustudies_Specialization9.setter
    def ntnustudies_Specialization9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ntnustudies_Specialization__ntnustudies_Specialization9", None)
        self.__ntnustudies_Specialization9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ntnustudies_Semester"):
                    opp_val = getattr(item, "ntnustudies_Semester", None)
                    
                    if opp_val == self:
                        setattr(item, "ntnustudies_Semester", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ntnustudies_Semester"):
                    opp_val = getattr(item, "ntnustudies_Semester", None)
                    
                    setattr(item, "ntnustudies_Semester", self)
                    

    @property
    def specializations(self):
        return self.__specializations

    @specializations.setter
    def specializations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ntnustudies_Specialization__specializations", None)
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
        old_value = getattr(self, f"_ntnustudies_Specialization__Specialization", None)
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
    def ntnustudies_Specialization7(self):
        return self.__ntnustudies_Specialization7

    @ntnustudies_Specialization7.setter
    def ntnustudies_Specialization7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ntnustudies_Specialization__ntnustudies_Specialization7", None)
        self.__ntnustudies_Specialization7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ntnustudies_Specialization5"):
                opp_val = getattr(old_value, "ntnustudies_Specialization5", None)
                if opp_val == self:
                    setattr(old_value, "ntnustudies_Specialization5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ntnustudies_Specialization5"):
                opp_val = getattr(value, "ntnustudies_Specialization5", None)
                setattr(value, "ntnustudies_Specialization5", self)

    @property
    def ntnustudies_Specialization5(self):
        return self.__ntnustudies_Specialization5

    @ntnustudies_Specialization5.setter
    def ntnustudies_Specialization5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ntnustudies_Specialization__ntnustudies_Specialization5", None)
        self.__ntnustudies_Specialization5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ntnustudies_Specialization7"):
                opp_val = getattr(old_value, "ntnustudies_Specialization7", None)
                if opp_val == self:
                    setattr(old_value, "ntnustudies_Specialization7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ntnustudies_Specialization7"):
                opp_val = getattr(value, "ntnustudies_Specialization7", None)
                setattr(value, "ntnustudies_Specialization7", self)

    @property
    def ntnustudies_Specialization(self):
        return self.__ntnustudies_Specialization

    @ntnustudies_Specialization.setter
    def ntnustudies_Specialization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ntnustudies_Specialization__ntnustudies_Specialization", None)
        self.__ntnustudies_Specialization = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ntnustudies_Course"):
                    opp_val = getattr(item, "ntnustudies_Course", None)
                    
                    if opp_val == self:
                        setattr(item, "ntnustudies_Course", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ntnustudies_Course"):
                    opp_val = getattr(item, "ntnustudies_Course", None)
                    
                    setattr(item, "ntnustudies_Course", self)
                    

class ntnustudies_Programme:

    def __init__(self, name: str, years: int, programme: set["ntnustudies_Specialization"] = None, programme2: set["ntnustudies_Semester"] = None, Programme: "ntnustudies_Specialization" = None, Programme14: "ntnustudies_Semester" = None, ntnustudies_Programme: "ntnustudies_StudyPlan" = None, ntnustudies_Programme31: "ntnustudies_Department" = None):
        self.name = name
        self.years = years
        self.programme = programme if programme is not None else set()
        self.programme2 = programme2 if programme2 is not None else set()
        self.Programme = Programme
        self.Programme14 = Programme14
        self.ntnustudies_Programme = ntnustudies_Programme
        self.ntnustudies_Programme31 = ntnustudies_Programme31
        
    @property
    def years(self) -> int:
        return self.__years

    @years.setter
    def years(self, years: int):
        self.__years = years

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ntnustudies_Programme31(self):
        return self.__ntnustudies_Programme31

    @ntnustudies_Programme31.setter
    def ntnustudies_Programme31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ntnustudies_Programme__ntnustudies_Programme31", None)
        self.__ntnustudies_Programme31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ntnustudies_Department30"):
                opp_val = getattr(old_value, "ntnustudies_Department30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ntnustudies_Department30"):
                opp_val = getattr(value, "ntnustudies_Department30", None)
                if opp_val is None:
                    setattr(value, "ntnustudies_Department30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def programme2(self):
        return self.__programme2

    @programme2.setter
    def programme2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ntnustudies_Programme__programme2", None)
        self.__programme2 = value if value is not None else set()
        
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
    def Programme(self):
        return self.__Programme

    @Programme.setter
    def Programme(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ntnustudies_Programme__Programme", None)
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
        old_value = getattr(self, f"_ntnustudies_Programme__programme", None)
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
    def ntnustudies_Programme(self):
        return self.__ntnustudies_Programme

    @ntnustudies_Programme.setter
    def ntnustudies_Programme(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ntnustudies_Programme__ntnustudies_Programme", None)
        self.__ntnustudies_Programme = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ntnustudies_StudyPlan"):
                opp_val = getattr(old_value, "ntnustudies_StudyPlan", None)
                if opp_val == self:
                    setattr(old_value, "ntnustudies_StudyPlan", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ntnustudies_StudyPlan"):
                opp_val = getattr(value, "ntnustudies_StudyPlan", None)
                setattr(value, "ntnustudies_StudyPlan", self)

    @property
    def Programme14(self):
        return self.__Programme14

    @Programme14.setter
    def Programme14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ntnustudies_Programme__Programme14", None)
        self.__Programme14 = value
        
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

class ntnustudies_Course:

    def __init__(self, code: str, name: str, credtis: float, semesters: str, level: str, type: str, ntnustudies_Course: "ntnustudies_Specialization" = None, ntnustudies_Course12: "ntnustudies_Semester" = None, ntnustudies_Course19: "ntnustudies_ChosenSemester" = None, ntnustudies_Course28: "ntnustudies_Department" = None):
        self.code = code
        self.name = name
        self.credtis = credtis
        self.semesters = semesters
        self.level = level
        self.type = type
        self.ntnustudies_Course = ntnustudies_Course
        self.ntnustudies_Course12 = ntnustudies_Course12
        self.ntnustudies_Course19 = ntnustudies_Course19
        self.ntnustudies_Course28 = ntnustudies_Course28
        
    @property
    def level(self) -> str:
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def credtis(self) -> float:
        return self.__credtis

    @credtis.setter
    def credtis(self, credtis: float):
        self.__credtis = credtis

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def semesters(self) -> str:
        return self.__semesters

    @semesters.setter
    def semesters(self, semesters: str):
        self.__semesters = semesters

    @property
    def ntnustudies_Course(self):
        return self.__ntnustudies_Course

    @ntnustudies_Course.setter
    def ntnustudies_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ntnustudies_Course__ntnustudies_Course", None)
        self.__ntnustudies_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ntnustudies_Specialization"):
                opp_val = getattr(old_value, "ntnustudies_Specialization", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ntnustudies_Specialization"):
                opp_val = getattr(value, "ntnustudies_Specialization", None)
                if opp_val is None:
                    setattr(value, "ntnustudies_Specialization", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ntnustudies_Course28(self):
        return self.__ntnustudies_Course28

    @ntnustudies_Course28.setter
    def ntnustudies_Course28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ntnustudies_Course__ntnustudies_Course28", None)
        self.__ntnustudies_Course28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ntnustudies_Department"):
                opp_val = getattr(old_value, "ntnustudies_Department", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ntnustudies_Department"):
                opp_val = getattr(value, "ntnustudies_Department", None)
                if opp_val is None:
                    setattr(value, "ntnustudies_Department", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ntnustudies_Course19(self):
        return self.__ntnustudies_Course19

    @ntnustudies_Course19.setter
    def ntnustudies_Course19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ntnustudies_Course__ntnustudies_Course19", None)
        self.__ntnustudies_Course19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ntnustudies_ChosenSemester18"):
                opp_val = getattr(old_value, "ntnustudies_ChosenSemester18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ntnustudies_ChosenSemester18"):
                opp_val = getattr(value, "ntnustudies_ChosenSemester18", None)
                if opp_val is None:
                    setattr(value, "ntnustudies_ChosenSemester18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ntnustudies_Course12(self):
        return self.__ntnustudies_Course12

    @ntnustudies_Course12.setter
    def ntnustudies_Course12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ntnustudies_Course__ntnustudies_Course12", None)
        self.__ntnustudies_Course12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ntnustudies_Semester11"):
                opp_val = getattr(old_value, "ntnustudies_Semester11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ntnustudies_Semester11"):
                opp_val = getattr(value, "ntnustudies_Semester11", None)
                if opp_val is None:
                    setattr(value, "ntnustudies_Semester11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
