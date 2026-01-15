from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class FallOrSpring(Enum):
    Fall = "Fall"
    Spring = "Spring"
class programmeCode(Enum):
    Datateknologi5 = "Datateknologi5"
    Informatikk = "Informatikk"
    Datateknologi2 = "Datateknologi2"


############################################
# Definition of Classes
############################################

class study_Semester:

    def __init__(self, fallOrSpring: str, semesterNumber: int, study_Semester13: set["study_CourseSlot"] = None, study_Semester: "study_StudyPlan" = None, study_Semester11: "study_Specialization" = None):
        self.fallOrSpring = fallOrSpring
        self.semesterNumber = semesterNumber
        self.study_Semester13 = study_Semester13 if study_Semester13 is not None else set()
        self.study_Semester = study_Semester
        self.study_Semester11 = study_Semester11
        
    @property
    def semesterNumber(self) -> int:
        return self.__semesterNumber

    @semesterNumber.setter
    def semesterNumber(self, semesterNumber: int):
        self.__semesterNumber = semesterNumber

    @property
    def fallOrSpring(self) -> str:
        return self.__fallOrSpring

    @fallOrSpring.setter
    def fallOrSpring(self, fallOrSpring: str):
        self.__fallOrSpring = fallOrSpring

    @property
    def study_Semester13(self):
        return self.__study_Semester13

    @study_Semester13.setter
    def study_Semester13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Semester__study_Semester13", None)
        self.__study_Semester13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "study_CourseSlot"):
                    opp_val = getattr(item, "study_CourseSlot", None)
                    
                    if opp_val == self:
                        setattr(item, "study_CourseSlot", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "study_CourseSlot"):
                    opp_val = getattr(item, "study_CourseSlot", None)
                    
                    setattr(item, "study_CourseSlot", self)
                    

    @property
    def study_Semester(self):
        return self.__study_Semester

    @study_Semester.setter
    def study_Semester(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Semester__study_Semester", None)
        self.__study_Semester = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "study_StudyPlan8"):
                opp_val = getattr(old_value, "study_StudyPlan8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "study_StudyPlan8"):
                opp_val = getattr(value, "study_StudyPlan8", None)
                if opp_val is None:
                    setattr(value, "study_StudyPlan8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def study_Semester11(self):
        return self.__study_Semester11

    @study_Semester11.setter
    def study_Semester11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Semester__study_Semester11", None)
        self.__study_Semester11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "study_Specialization10"):
                opp_val = getattr(old_value, "study_Specialization10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "study_Specialization10"):
                opp_val = getattr(value, "study_Specialization10", None)
                if opp_val is None:
                    setattr(value, "study_Specialization10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class study_CourseSlot:

    def __init__(self, elective: bool, study_CourseSlot: "study_Semester" = None, study_CourseSlot15: "study_Course" = None, study_CourseSlot18: set["study_Course"] = None):
        self.elective = elective
        self.study_CourseSlot = study_CourseSlot
        self.study_CourseSlot15 = study_CourseSlot15
        self.study_CourseSlot18 = study_CourseSlot18 if study_CourseSlot18 is not None else set()
        
    @property
    def elective(self) -> bool:
        return self.__elective

    @elective.setter
    def elective(self, elective: bool):
        self.__elective = elective

    @property
    def study_CourseSlot15(self):
        return self.__study_CourseSlot15

    @study_CourseSlot15.setter
    def study_CourseSlot15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_CourseSlot__study_CourseSlot15", None)
        self.__study_CourseSlot15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "study_Course16"):
                opp_val = getattr(old_value, "study_Course16", None)
                if opp_val == self:
                    setattr(old_value, "study_Course16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "study_Course16"):
                opp_val = getattr(value, "study_Course16", None)
                setattr(value, "study_Course16", self)

    @property
    def study_CourseSlot18(self):
        return self.__study_CourseSlot18

    @study_CourseSlot18.setter
    def study_CourseSlot18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_CourseSlot__study_CourseSlot18", None)
        self.__study_CourseSlot18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "study_Course19"):
                    opp_val = getattr(item, "study_Course19", None)
                    
                    if opp_val == self:
                        setattr(item, "study_Course19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "study_Course19"):
                    opp_val = getattr(item, "study_Course19", None)
                    
                    setattr(item, "study_Course19", self)
                    

    @property
    def study_CourseSlot(self):
        return self.__study_CourseSlot

    @study_CourseSlot.setter
    def study_CourseSlot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_CourseSlot__study_CourseSlot", None)
        self.__study_CourseSlot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "study_Semester13"):
                opp_val = getattr(old_value, "study_Semester13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "study_Semester13"):
                opp_val = getattr(value, "study_Semester13", None)
                if opp_val is None:
                    setattr(value, "study_Semester13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class study_Course:

    def __init__(self, name: str, code: str, points: float, study_Course: "study_Department" = None, study_Course16: "study_CourseSlot" = None, study_Course19: "study_CourseSlot" = None):
        self.name = name
        self.code = code
        self.points = points
        self.study_Course = study_Course
        self.study_Course16 = study_Course16
        self.study_Course19 = study_Course19
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def points(self) -> float:
        return self.__points

    @points.setter
    def points(self, points: float):
        self.__points = points

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def study_Course16(self):
        return self.__study_Course16

    @study_Course16.setter
    def study_Course16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Course__study_Course16", None)
        self.__study_Course16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "study_CourseSlot15"):
                opp_val = getattr(old_value, "study_CourseSlot15", None)
                if opp_val == self:
                    setattr(old_value, "study_CourseSlot15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "study_CourseSlot15"):
                opp_val = getattr(value, "study_CourseSlot15", None)
                setattr(value, "study_CourseSlot15", self)

    @property
    def study_Course19(self):
        return self.__study_Course19

    @study_Course19.setter
    def study_Course19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Course__study_Course19", None)
        self.__study_Course19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "study_CourseSlot18"):
                opp_val = getattr(old_value, "study_CourseSlot18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "study_CourseSlot18"):
                opp_val = getattr(value, "study_CourseSlot18", None)
                if opp_val is None:
                    setattr(value, "study_CourseSlot18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "study_Department2"):
                opp_val = getattr(old_value, "study_Department2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "study_Department2"):
                opp_val = getattr(value, "study_Department2", None)
                if opp_val is None:
                    setattr(value, "study_Department2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class study_Programme:

    def __init__(self, name: str, programmeCode: str, study_Programme4: set["study_StudyPlan"] = None, study_Programme: "study_Department" = None):
        self.name = name
        self.programmeCode = programmeCode
        self.study_Programme4 = study_Programme4 if study_Programme4 is not None else set()
        self.study_Programme = study_Programme
        
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
    def study_Programme4(self):
        return self.__study_Programme4

    @study_Programme4.setter
    def study_Programme4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Programme__study_Programme4", None)
        self.__study_Programme4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "study_StudyPlan"):
                    opp_val = getattr(item, "study_StudyPlan", None)
                    
                    if opp_val == self:
                        setattr(item, "study_StudyPlan", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "study_StudyPlan"):
                    opp_val = getattr(item, "study_StudyPlan", None)
                    
                    setattr(item, "study_StudyPlan", self)
                    

    @property
    def study_Programme(self):
        return self.__study_Programme

    @study_Programme.setter
    def study_Programme(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Programme__study_Programme", None)
        self.__study_Programme = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "study_Department"):
                opp_val = getattr(old_value, "study_Department", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "study_Department"):
                opp_val = getattr(value, "study_Department", None)
                if opp_val is None:
                    setattr(value, "study_Department", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class study_Department:

    pass
class study_Specialization:

    def __init__(self, name: str, study_Specialization: "study_StudyPlan" = None, study_Specialization10: set["study_Semester"] = None):
        self.name = name
        self.study_Specialization = study_Specialization
        self.study_Specialization10 = study_Specialization10 if study_Specialization10 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "study_StudyPlan6"):
                opp_val = getattr(old_value, "study_StudyPlan6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "study_StudyPlan6"):
                opp_val = getattr(value, "study_StudyPlan6", None)
                if opp_val is None:
                    setattr(value, "study_StudyPlan6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def study_Specialization10(self):
        return self.__study_Specialization10

    @study_Specialization10.setter
    def study_Specialization10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_study_Specialization__study_Specialization10", None)
        self.__study_Specialization10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "study_Semester11"):
                    opp_val = getattr(item, "study_Semester11", None)
                    
                    if opp_val == self:
                        setattr(item, "study_Semester11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "study_Semester11"):
                    opp_val = getattr(item, "study_Semester11", None)
                    
                    setattr(item, "study_Semester11", self)
                    

class study_StudyPlan:

    pass