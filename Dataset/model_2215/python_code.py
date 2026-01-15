from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class SemesterTime(Enum):
    Fall = "Fall"
    Spring = "Spring"
class SlotType(Enum):
    O = "O"
    V = "V"
    V2 = "V2"


############################################
# Definition of Classes
############################################

class university_University:

    def __init__(self, name: str, university_University: set["university_Programmes"] = None, university_University29: set["university_Courses"] = None, university_University31: set["university_Semesters"] = None):
        self.name = name
        self.university_University = university_University if university_University is not None else set()
        self.university_University29 = university_University29 if university_University29 is not None else set()
        self.university_University31 = university_University31 if university_University31 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def university_University31(self):
        return self.__university_University31

    @university_University31.setter
    def university_University31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_University__university_University31", None)
        self.__university_University31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "university_Semesters32"):
                    opp_val = getattr(item, "university_Semesters32", None)
                    
                    if opp_val == self:
                        setattr(item, "university_Semesters32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "university_Semesters32"):
                    opp_val = getattr(item, "university_Semesters32", None)
                    
                    setattr(item, "university_Semesters32", self)
                    

    @property
    def university_University29(self):
        return self.__university_University29

    @university_University29.setter
    def university_University29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_University__university_University29", None)
        self.__university_University29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "university_Courses"):
                    opp_val = getattr(item, "university_Courses", None)
                    
                    if opp_val == self:
                        setattr(item, "university_Courses", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "university_Courses"):
                    opp_val = getattr(item, "university_Courses", None)
                    
                    setattr(item, "university_Courses", self)
                    

    @property
    def university_University(self):
        return self.__university_University

    @university_University.setter
    def university_University(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_University__university_University", None)
        self.__university_University = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "university_Programmes"):
                    opp_val = getattr(item, "university_Programmes", None)
                    
                    if opp_val == self:
                        setattr(item, "university_Programmes", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "university_Programmes"):
                    opp_val = getattr(item, "university_Programmes", None)
                    
                    setattr(item, "university_Programmes", self)
                    

class university_CourseInstances:

    pass
class university_Slot:

    def __init__(self, points: int, slotType: str, name: str, Slot: "university_ProgrammeSemesters" = None, slots: "university_ProgrammeSemesters" = None, university_Slot: set["university_CourseInstances"] = None):
        self.points = points
        self.slotType = slotType
        self.name = name
        self.Slot = Slot
        self.slots = slots
        self.university_Slot = university_Slot if university_Slot is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def points(self) -> int:
        return self.__points

    @points.setter
    def points(self, points: int):
        self.__points = points

    @property
    def slotType(self) -> str:
        return self.__slotType

    @slotType.setter
    def slotType(self, slotType: str):
        self.__slotType = slotType

    @property
    def slots(self):
        return self.__slots

    @slots.setter
    def slots(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Slot__slots", None)
        self.__slots = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProgrammeSemesters18"):
                opp_val = getattr(old_value, "ProgrammeSemesters18", None)
                if opp_val == self:
                    setattr(old_value, "ProgrammeSemesters18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProgrammeSemesters18"):
                opp_val = getattr(value, "ProgrammeSemesters18", None)
                setattr(value, "ProgrammeSemesters18", self)

    @property
    def university_Slot(self):
        return self.__university_Slot

    @university_Slot.setter
    def university_Slot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Slot__university_Slot", None)
        self.__university_Slot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "university_CourseInstances20"):
                    opp_val = getattr(item, "university_CourseInstances20", None)
                    
                    if opp_val == self:
                        setattr(item, "university_CourseInstances20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "university_CourseInstances20"):
                    opp_val = getattr(item, "university_CourseInstances20", None)
                    
                    setattr(item, "university_CourseInstances20", self)
                    

    @property
    def Slot(self):
        return self.__Slot

    @Slot.setter
    def Slot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Slot__Slot", None)
        self.__Slot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "programmeSemester"):
                opp_val = getattr(old_value, "programmeSemester", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "programmeSemester"):
                opp_val = getattr(value, "programmeSemester", None)
                if opp_val is None:
                    setattr(value, "programmeSemester", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class university_Semesters:

    def __init__(self, year: int, semesterTime: str, university_Semesters: "university_CourseInstances" = None, Semesters: "university_ProgrammeSemesters" = None, semester: set["university_ProgrammeSemesters"] = None, university_Semesters32: "university_University" = None):
        self.year = year
        self.semesterTime = semesterTime
        self.university_Semesters = university_Semesters
        self.Semesters = Semesters
        self.semester = semester if semester is not None else set()
        self.university_Semesters32 = university_Semesters32
        
    @property
    def semesterTime(self) -> str:
        return self.__semesterTime

    @semesterTime.setter
    def semesterTime(self, semesterTime: str):
        self.__semesterTime = semesterTime

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def university_Semesters32(self):
        return self.__university_Semesters32

    @university_Semesters32.setter
    def university_Semesters32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Semesters__university_Semesters32", None)
        self.__university_Semesters32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "university_University31"):
                opp_val = getattr(old_value, "university_University31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "university_University31"):
                opp_val = getattr(value, "university_University31", None)
                if opp_val is None:
                    setattr(value, "university_University31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def university_Semesters(self):
        return self.__university_Semesters

    @university_Semesters.setter
    def university_Semesters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Semesters__university_Semesters", None)
        self.__university_Semesters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "university_CourseInstances"):
                opp_val = getattr(old_value, "university_CourseInstances", None)
                if opp_val == self:
                    setattr(old_value, "university_CourseInstances", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "university_CourseInstances"):
                opp_val = getattr(value, "university_CourseInstances", None)
                setattr(value, "university_CourseInstances", self)

    @property
    def Semesters(self):
        return self.__Semesters

    @Semesters.setter
    def Semesters(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Semesters__Semesters", None)
        self.__Semesters = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "programmeSemesters13"):
                opp_val = getattr(old_value, "programmeSemesters13", None)
                if opp_val == self:
                    setattr(old_value, "programmeSemesters13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "programmeSemesters13"):
                opp_val = getattr(value, "programmeSemesters13", None)
                setattr(value, "programmeSemesters13", self)

    @property
    def semester(self):
        return self.__semester

    @semester.setter
    def semester(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Semesters__semester", None)
        self.__semester = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ProgrammeSemesters22"):
                    opp_val = getattr(item, "ProgrammeSemesters22", None)
                    
                    if opp_val == self:
                        setattr(item, "ProgrammeSemesters22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ProgrammeSemesters22"):
                    opp_val = getattr(item, "ProgrammeSemesters22", None)
                    
                    setattr(item, "ProgrammeSemesters22", self)
                    

class university_Courses:

    def __init__(self, code: str, name: str, credits: float, Courses: "university_CourseInstances" = None, course: set["university_CourseInstances"] = None, university_Courses: "university_University" = None):
        self.code = code
        self.name = name
        self.credits = credits
        self.Courses = Courses
        self.course = course if course is not None else set()
        self.university_Courses = university_Courses
        
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
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def Courses(self):
        return self.__Courses

    @Courses.setter
    def Courses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Courses__Courses", None)
        self.__Courses = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "instances7"):
                opp_val = getattr(old_value, "instances7", None)
                if opp_val == self:
                    setattr(old_value, "instances7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "instances7"):
                opp_val = getattr(value, "instances7", None)
                setattr(value, "instances7", self)

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Courses__course", None)
        self.__course = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CourseInstances"):
                    opp_val = getattr(item, "CourseInstances", None)
                    
                    if opp_val == self:
                        setattr(item, "CourseInstances", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CourseInstances"):
                    opp_val = getattr(item, "CourseInstances", None)
                    
                    setattr(item, "CourseInstances", self)
                    

    @property
    def university_Courses(self):
        return self.__university_Courses

    @university_Courses.setter
    def university_Courses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Courses__university_Courses", None)
        self.__university_Courses = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "university_University29"):
                opp_val = getattr(old_value, "university_University29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "university_University29"):
                opp_val = getattr(value, "university_University29", None)
                if opp_val is None:
                    setattr(value, "university_University29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class university_Specializations:

    def __init__(self, name: str, Specializations: "university_ProgrammeInstances" = None, Specializations16: "university_ProgrammeSemesters" = None, specializations: "university_ProgrammeInstances" = None, specialization: set["university_ProgrammeSemesters"] = None):
        self.name = name
        self.Specializations = Specializations
        self.Specializations16 = Specializations16
        self.specializations = specializations
        self.specialization = specialization if specialization is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Specializations(self):
        return self.__Specializations

    @Specializations.setter
    def Specializations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Specializations__Specializations", None)
        self.__Specializations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "programmeInstance4"):
                opp_val = getattr(old_value, "programmeInstance4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "programmeInstance4"):
                opp_val = getattr(value, "programmeInstance4", None)
                if opp_val is None:
                    setattr(value, "programmeInstance4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def specializations(self):
        return self.__specializations

    @specializations.setter
    def specializations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Specializations__specializations", None)
        self.__specializations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ProgrammeInstances24"):
                opp_val = getattr(old_value, "ProgrammeInstances24", None)
                if opp_val == self:
                    setattr(old_value, "ProgrammeInstances24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ProgrammeInstances24"):
                opp_val = getattr(value, "ProgrammeInstances24", None)
                setattr(value, "ProgrammeInstances24", self)

    @property
    def Specializations16(self):
        return self.__Specializations16

    @Specializations16.setter
    def Specializations16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Specializations__Specializations16", None)
        self.__Specializations16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "programmeSemester15"):
                opp_val = getattr(old_value, "programmeSemester15", None)
                if opp_val == self:
                    setattr(old_value, "programmeSemester15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "programmeSemester15"):
                opp_val = getattr(value, "programmeSemester15", None)
                setattr(value, "programmeSemester15", self)

    @property
    def specialization(self):
        return self.__specialization

    @specialization.setter
    def specialization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Specializations__specialization", None)
        self.__specialization = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ProgrammeSemesters26"):
                    opp_val = getattr(item, "ProgrammeSemesters26", None)
                    
                    if opp_val == self:
                        setattr(item, "ProgrammeSemesters26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ProgrammeSemesters26"):
                    opp_val = getattr(item, "ProgrammeSemesters26", None)
                    
                    setattr(item, "ProgrammeSemesters26", self)
                    

class university_ProgrammeSemesters:

    pass
class university_ProgrammeInstances:

    def __init__(self, startYear: int, ProgrammeInstances: "university_Programmes" = None, instances: "university_Programmes" = None, programmeInstance: set["university_ProgrammeSemesters"] = None, programmeInstance4: set["university_Specializations"] = None, ProgrammeInstances10: "university_ProgrammeSemesters" = None, ProgrammeInstances24: "university_Specializations" = None):
        self.startYear = startYear
        self.ProgrammeInstances = ProgrammeInstances
        self.instances = instances
        self.programmeInstance = programmeInstance if programmeInstance is not None else set()
        self.programmeInstance4 = programmeInstance4 if programmeInstance4 is not None else set()
        self.ProgrammeInstances10 = ProgrammeInstances10
        self.ProgrammeInstances24 = ProgrammeInstances24
        
    @property
    def startYear(self) -> int:
        return self.__startYear

    @startYear.setter
    def startYear(self, startYear: int):
        self.__startYear = startYear

    @property
    def ProgrammeInstances24(self):
        return self.__ProgrammeInstances24

    @ProgrammeInstances24.setter
    def ProgrammeInstances24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_ProgrammeInstances__ProgrammeInstances24", None)
        self.__ProgrammeInstances24 = value
        
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
    def ProgrammeInstances10(self):
        return self.__ProgrammeInstances10

    @ProgrammeInstances10.setter
    def ProgrammeInstances10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_ProgrammeInstances__ProgrammeInstances10", None)
        self.__ProgrammeInstances10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "programmeSemesters"):
                opp_val = getattr(old_value, "programmeSemesters", None)
                if opp_val == self:
                    setattr(old_value, "programmeSemesters", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "programmeSemesters"):
                opp_val = getattr(value, "programmeSemesters", None)
                setattr(value, "programmeSemesters", self)

    @property
    def ProgrammeInstances(self):
        return self.__ProgrammeInstances

    @ProgrammeInstances.setter
    def ProgrammeInstances(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_ProgrammeInstances__ProgrammeInstances", None)
        self.__ProgrammeInstances = value
        
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
    def programmeInstance(self):
        return self.__programmeInstance

    @programmeInstance.setter
    def programmeInstance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_ProgrammeInstances__programmeInstance", None)
        self.__programmeInstance = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ProgrammeSemesters"):
                    opp_val = getattr(item, "ProgrammeSemesters", None)
                    
                    if opp_val == self:
                        setattr(item, "ProgrammeSemesters", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ProgrammeSemesters"):
                    opp_val = getattr(item, "ProgrammeSemesters", None)
                    
                    setattr(item, "ProgrammeSemesters", self)
                    

    @property
    def instances(self):
        return self.__instances

    @instances.setter
    def instances(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_ProgrammeInstances__instances", None)
        self.__instances = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Programmes"):
                opp_val = getattr(old_value, "Programmes", None)
                if opp_val == self:
                    setattr(old_value, "Programmes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Programmes"):
                opp_val = getattr(value, "Programmes", None)
                setattr(value, "Programmes", self)

    @property
    def programmeInstance4(self):
        return self.__programmeInstance4

    @programmeInstance4.setter
    def programmeInstance4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_ProgrammeInstances__programmeInstance4", None)
        self.__programmeInstance4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Specializations"):
                    opp_val = getattr(item, "Specializations", None)
                    
                    if opp_val == self:
                        setattr(item, "Specializations", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Specializations"):
                    opp_val = getattr(item, "Specializations", None)
                    
                    setattr(item, "Specializations", self)
                    

class university_Programmes:

    def __init__(self, name: str, code: str, programme: set["university_ProgrammeInstances"] = None, Programmes: "university_ProgrammeInstances" = None, university_Programmes: "university_University" = None):
        self.name = name
        self.code = code
        self.programme = programme if programme is not None else set()
        self.Programmes = Programmes
        self.university_Programmes = university_Programmes
        
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
    def programme(self):
        return self.__programme

    @programme.setter
    def programme(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Programmes__programme", None)
        self.__programme = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ProgrammeInstances"):
                    opp_val = getattr(item, "ProgrammeInstances", None)
                    
                    if opp_val == self:
                        setattr(item, "ProgrammeInstances", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ProgrammeInstances"):
                    opp_val = getattr(item, "ProgrammeInstances", None)
                    
                    setattr(item, "ProgrammeInstances", self)
                    

    @property
    def Programmes(self):
        return self.__Programmes

    @Programmes.setter
    def Programmes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Programmes__Programmes", None)
        self.__Programmes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "instances"):
                opp_val = getattr(old_value, "instances", None)
                if opp_val == self:
                    setattr(old_value, "instances", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "instances"):
                opp_val = getattr(value, "instances", None)
                setattr(value, "instances", self)

    @property
    def university_Programmes(self):
        return self.__university_Programmes

    @university_Programmes.setter
    def university_Programmes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Programmes__university_Programmes", None)
        self.__university_Programmes = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "university_University"):
                opp_val = getattr(old_value, "university_University", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "university_University"):
                opp_val = getattr(value, "university_University", None)
                if opp_val is None:
                    setattr(value, "university_University", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
