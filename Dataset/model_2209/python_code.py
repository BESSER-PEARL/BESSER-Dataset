from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Credits(Enum):
    Double = "Double"
    Full = "Full"
    Minor = "Minor"
    Basic = "Basic"
class Seasons(Enum):
    Fall = "Fall"
    Spring = "Spring"
class ProgrammeType(Enum):
    Bachelor = "Bachelor"
    Master = "Master"
    IntegrertMaster = "IntegrertMaster"
    Årsstudie = "Årsstudie"


############################################
# Definition of Classes
############################################

class universityStudies_CourseSlot(ABC):

    pass
class CourseSlot:

    pass
class universityStudies_ElectiveCourseSlot(CourseSlot):

    pass
class universityStudies_MandatoryCourseSlot(CourseSlot):

    pass
class universityStudies_Specialization:

    def __init__(self, name: str, universityStudies_Specialization8: "universityStudies_Specialization" = None, universityStudies_Specialization6: set["universityStudies_Specialization"] = None, universityStudies_Specialization10: set["universityStudies_Semester"] = None, universityStudies_Specialization: "universityStudies_Programme" = None):
        self.name = name
        self.universityStudies_Specialization8 = universityStudies_Specialization8
        self.universityStudies_Specialization6 = universityStudies_Specialization6 if universityStudies_Specialization6 is not None else set()
        self.universityStudies_Specialization10 = universityStudies_Specialization10 if universityStudies_Specialization10 is not None else set()
        self.universityStudies_Specialization = universityStudies_Specialization
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def universityStudies_Specialization6(self):
        return self.__universityStudies_Specialization6

    @universityStudies_Specialization6.setter
    def universityStudies_Specialization6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_universityStudies_Specialization__universityStudies_Specialization6", None)
        self.__universityStudies_Specialization6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "universityStudies_Specialization8"):
                    opp_val = getattr(item, "universityStudies_Specialization8", None)
                    
                    if opp_val == self:
                        setattr(item, "universityStudies_Specialization8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "universityStudies_Specialization8"):
                    opp_val = getattr(item, "universityStudies_Specialization8", None)
                    
                    setattr(item, "universityStudies_Specialization8", self)
                    

    @property
    def universityStudies_Specialization(self):
        return self.__universityStudies_Specialization

    @universityStudies_Specialization.setter
    def universityStudies_Specialization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_universityStudies_Specialization__universityStudies_Specialization", None)
        self.__universityStudies_Specialization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "universityStudies_Programme2"):
                opp_val = getattr(old_value, "universityStudies_Programme2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "universityStudies_Programme2"):
                opp_val = getattr(value, "universityStudies_Programme2", None)
                if opp_val is None:
                    setattr(value, "universityStudies_Programme2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def universityStudies_Specialization10(self):
        return self.__universityStudies_Specialization10

    @universityStudies_Specialization10.setter
    def universityStudies_Specialization10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_universityStudies_Specialization__universityStudies_Specialization10", None)
        self.__universityStudies_Specialization10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "universityStudies_Semester11"):
                    opp_val = getattr(item, "universityStudies_Semester11", None)
                    
                    if opp_val == self:
                        setattr(item, "universityStudies_Semester11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "universityStudies_Semester11"):
                    opp_val = getattr(item, "universityStudies_Semester11", None)
                    
                    setattr(item, "universityStudies_Semester11", self)
                    

    @property
    def universityStudies_Specialization8(self):
        return self.__universityStudies_Specialization8

    @universityStudies_Specialization8.setter
    def universityStudies_Specialization8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_universityStudies_Specialization__universityStudies_Specialization8", None)
        self.__universityStudies_Specialization8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "universityStudies_Specialization6"):
                opp_val = getattr(old_value, "universityStudies_Specialization6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "universityStudies_Specialization6"):
                opp_val = getattr(value, "universityStudies_Specialization6", None)
                if opp_val is None:
                    setattr(value, "universityStudies_Specialization6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class universityStudies_Department:

    pass
class universityStudies_Semester:

    def __init__(self, season: str, semesterNumber: int, name: str, universityStudies_Semester: "universityStudies_Programme" = None, universityStudies_Semester11: "universityStudies_Specialization" = None, universityStudies_Semester13: set["universityStudies_CourseSlot"] = None):
        self.season = season
        self.semesterNumber = semesterNumber
        self.name = name
        self.universityStudies_Semester = universityStudies_Semester
        self.universityStudies_Semester11 = universityStudies_Semester11
        self.universityStudies_Semester13 = universityStudies_Semester13 if universityStudies_Semester13 is not None else set()
        
    @property
    def season(self) -> str:
        return self.__season

    @season.setter
    def season(self, season: str):
        self.__season = season

    @property
    def semesterNumber(self) -> int:
        return self.__semesterNumber

    @semesterNumber.setter
    def semesterNumber(self, semesterNumber: int):
        self.__semesterNumber = semesterNumber

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def universityStudies_Semester13(self):
        return self.__universityStudies_Semester13

    @universityStudies_Semester13.setter
    def universityStudies_Semester13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_universityStudies_Semester__universityStudies_Semester13", None)
        self.__universityStudies_Semester13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "universityStudies_CourseSlot"):
                    opp_val = getattr(item, "universityStudies_CourseSlot", None)
                    
                    if opp_val == self:
                        setattr(item, "universityStudies_CourseSlot", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "universityStudies_CourseSlot"):
                    opp_val = getattr(item, "universityStudies_CourseSlot", None)
                    
                    setattr(item, "universityStudies_CourseSlot", self)
                    

    @property
    def universityStudies_Semester11(self):
        return self.__universityStudies_Semester11

    @universityStudies_Semester11.setter
    def universityStudies_Semester11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_universityStudies_Semester__universityStudies_Semester11", None)
        self.__universityStudies_Semester11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "universityStudies_Specialization10"):
                opp_val = getattr(old_value, "universityStudies_Specialization10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "universityStudies_Specialization10"):
                opp_val = getattr(value, "universityStudies_Specialization10", None)
                if opp_val is None:
                    setattr(value, "universityStudies_Specialization10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def universityStudies_Semester(self):
        return self.__universityStudies_Semester

    @universityStudies_Semester.setter
    def universityStudies_Semester(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_universityStudies_Semester__universityStudies_Semester", None)
        self.__universityStudies_Semester = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "universityStudies_Programme4"):
                opp_val = getattr(old_value, "universityStudies_Programme4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "universityStudies_Programme4"):
                opp_val = getattr(value, "universityStudies_Programme4", None)
                if opp_val is None:
                    setattr(value, "universityStudies_Programme4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class universityStudies_Programme:

    def __init__(self, programmeType: str, numberOfSemesters: int, name: str, universityStudies_Programme: "universityStudies_Course" = None, universityStudies_Programme4: set["universityStudies_Semester"] = None, Programmes: "universityStudies_Department" = None, universityStudies_Programme2: set["universityStudies_Specialization"] = None, Programme: "universityStudies_Department" = None):
        self.programmeType = programmeType
        self.numberOfSemesters = numberOfSemesters
        self.name = name
        self.universityStudies_Programme = universityStudies_Programme
        self.universityStudies_Programme4 = universityStudies_Programme4 if universityStudies_Programme4 is not None else set()
        self.Programmes = Programmes
        self.universityStudies_Programme2 = universityStudies_Programme2 if universityStudies_Programme2 is not None else set()
        self.Programme = Programme
        
    @property
    def programmeType(self) -> str:
        return self.__programmeType

    @programmeType.setter
    def programmeType(self, programmeType: str):
        self.__programmeType = programmeType

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def numberOfSemesters(self) -> int:
        return self.__numberOfSemesters

    @numberOfSemesters.setter
    def numberOfSemesters(self, numberOfSemesters: int):
        self.__numberOfSemesters = numberOfSemesters

    @property
    def universityStudies_Programme(self):
        return self.__universityStudies_Programme

    @universityStudies_Programme.setter
    def universityStudies_Programme(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_universityStudies_Programme__universityStudies_Programme", None)
        self.__universityStudies_Programme = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "universityStudies_Course"):
                opp_val = getattr(old_value, "universityStudies_Course", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "universityStudies_Course"):
                opp_val = getattr(value, "universityStudies_Course", None)
                if opp_val is None:
                    setattr(value, "universityStudies_Course", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def universityStudies_Programme4(self):
        return self.__universityStudies_Programme4

    @universityStudies_Programme4.setter
    def universityStudies_Programme4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_universityStudies_Programme__universityStudies_Programme4", None)
        self.__universityStudies_Programme4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "universityStudies_Semester"):
                    opp_val = getattr(item, "universityStudies_Semester", None)
                    
                    if opp_val == self:
                        setattr(item, "universityStudies_Semester", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "universityStudies_Semester"):
                    opp_val = getattr(item, "universityStudies_Semester", None)
                    
                    setattr(item, "universityStudies_Semester", self)
                    

    @property
    def Programmes(self):
        return self.__Programmes

    @Programmes.setter
    def Programmes(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_universityStudies_Programme__Programmes", None)
        self.__Programmes = value
        
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
    def universityStudies_Programme2(self):
        return self.__universityStudies_Programme2

    @universityStudies_Programme2.setter
    def universityStudies_Programme2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_universityStudies_Programme__universityStudies_Programme2", None)
        self.__universityStudies_Programme2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "universityStudies_Specialization"):
                    opp_val = getattr(item, "universityStudies_Specialization", None)
                    
                    if opp_val == self:
                        setattr(item, "universityStudies_Specialization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "universityStudies_Specialization"):
                    opp_val = getattr(item, "universityStudies_Specialization", None)
                    
                    setattr(item, "universityStudies_Specialization", self)
                    

    @property
    def Programme(self):
        return self.__Programme

    @Programme.setter
    def Programme(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_universityStudies_Programme__Programme", None)
        self.__Programme = value
        
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

class universityStudies_Course:

    def __init__(self, name: str, code: str, credits: str, level: int, universityStudies_Course: set["universityStudies_Programme"] = None, universityStudies_Course15: "universityStudies_Department" = None, universityStudies_Course20: "universityStudies_CourseSlot" = None, universityStudies_Course22: "universityStudies_ElectiveCourseSlot" = None):
        self.name = name
        self.code = code
        self.credits = credits
        self.level = level
        self.universityStudies_Course = universityStudies_Course if universityStudies_Course is not None else set()
        self.universityStudies_Course15 = universityStudies_Course15
        self.universityStudies_Course20 = universityStudies_Course20
        self.universityStudies_Course22 = universityStudies_Course22
        
    @property
    def level(self) -> int:
        return self.__level

    @level.setter
    def level(self, level: int):
        self.__level = level

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
    def universityStudies_Course22(self):
        return self.__universityStudies_Course22

    @universityStudies_Course22.setter
    def universityStudies_Course22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_universityStudies_Course__universityStudies_Course22", None)
        self.__universityStudies_Course22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "universityStudies_ElectiveCourseSlot"):
                opp_val = getattr(old_value, "universityStudies_ElectiveCourseSlot", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "universityStudies_ElectiveCourseSlot"):
                opp_val = getattr(value, "universityStudies_ElectiveCourseSlot", None)
                if opp_val is None:
                    setattr(value, "universityStudies_ElectiveCourseSlot", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def universityStudies_Course(self):
        return self.__universityStudies_Course

    @universityStudies_Course.setter
    def universityStudies_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_universityStudies_Course__universityStudies_Course", None)
        self.__universityStudies_Course = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "universityStudies_Programme"):
                    opp_val = getattr(item, "universityStudies_Programme", None)
                    
                    if opp_val == self:
                        setattr(item, "universityStudies_Programme", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "universityStudies_Programme"):
                    opp_val = getattr(item, "universityStudies_Programme", None)
                    
                    setattr(item, "universityStudies_Programme", self)
                    

    @property
    def universityStudies_Course15(self):
        return self.__universityStudies_Course15

    @universityStudies_Course15.setter
    def universityStudies_Course15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_universityStudies_Course__universityStudies_Course15", None)
        self.__universityStudies_Course15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "universityStudies_Department"):
                opp_val = getattr(old_value, "universityStudies_Department", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "universityStudies_Department"):
                opp_val = getattr(value, "universityStudies_Department", None)
                if opp_val is None:
                    setattr(value, "universityStudies_Department", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def universityStudies_Course20(self):
        return self.__universityStudies_Course20

    @universityStudies_Course20.setter
    def universityStudies_Course20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_universityStudies_Course__universityStudies_Course20", None)
        self.__universityStudies_Course20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "universityStudies_CourseSlot19"):
                opp_val = getattr(old_value, "universityStudies_CourseSlot19", None)
                if opp_val == self:
                    setattr(old_value, "universityStudies_CourseSlot19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "universityStudies_CourseSlot19"):
                opp_val = getattr(value, "universityStudies_CourseSlot19", None)
                setattr(value, "universityStudies_CourseSlot19", self)
