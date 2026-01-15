from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class MinRequirementType(Enum):
    Absolute = "Absolute"
    Relative = "Relative"


############################################
# Definition of Classes
############################################

class gsml_GradingSystem:

    pass
class Task:

    pass
class gsml_TaskGroup(Task):

    pass
class gsml_ConcreteTask(Task):

    def __init__(self, MaxPoints: float):
        self.MaxPoints = MaxPoints
        
    @property
    def MaxPoints(self) -> float:
        return self.__MaxPoints

    @MaxPoints.setter
    def MaxPoints(self, MaxPoints: float):
        self.__MaxPoints = MaxPoints

class gsml_Grade:

    def __init__(self, Name: str, RequiredPoints: float, gsml_Grade: "gsml_GradingScheme" = None, gsml_Grade14: "gsml_GradingScheme" = None):
        self.Name = Name
        self.RequiredPoints = RequiredPoints
        self.gsml_Grade = gsml_Grade
        self.gsml_Grade14 = gsml_Grade14
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def RequiredPoints(self) -> float:
        return self.__RequiredPoints

    @RequiredPoints.setter
    def RequiredPoints(self, RequiredPoints: float):
        self.__RequiredPoints = RequiredPoints

    @property
    def gsml_Grade(self):
        return self.__gsml_Grade

    @gsml_Grade.setter
    def gsml_Grade(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gsml_Grade__gsml_Grade", None)
        self.__gsml_Grade = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gsml_GradingScheme11"):
                opp_val = getattr(old_value, "gsml_GradingScheme11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gsml_GradingScheme11"):
                opp_val = getattr(value, "gsml_GradingScheme11", None)
                if opp_val is None:
                    setattr(value, "gsml_GradingScheme11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gsml_Grade14(self):
        return self.__gsml_Grade14

    @gsml_Grade14.setter
    def gsml_Grade14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gsml_Grade__gsml_Grade14", None)
        self.__gsml_Grade14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gsml_GradingScheme13"):
                opp_val = getattr(old_value, "gsml_GradingScheme13", None)
                if opp_val == self:
                    setattr(old_value, "gsml_GradingScheme13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gsml_GradingScheme13"):
                opp_val = getattr(value, "gsml_GradingScheme13", None)
                setattr(value, "gsml_GradingScheme13", self)

class gsml_GradingScheme:

    pass
class gsml_Grading:

    def __init__(self, Semester: str, gsml_Grading: "gsml_Course" = None, gsml_Grading18: "gsml_GradingScheme" = None, gsml_Grading21: set["gsml_Task"] = None, gsml_Grading24: set["gsml_Task"] = None):
        self.Semester = Semester
        self.gsml_Grading = gsml_Grading
        self.gsml_Grading18 = gsml_Grading18
        self.gsml_Grading21 = gsml_Grading21 if gsml_Grading21 is not None else set()
        self.gsml_Grading24 = gsml_Grading24 if gsml_Grading24 is not None else set()
        
    @property
    def Semester(self) -> str:
        return self.__Semester

    @Semester.setter
    def Semester(self, Semester: str):
        self.__Semester = Semester

    @property
    def gsml_Grading21(self):
        return self.__gsml_Grading21

    @gsml_Grading21.setter
    def gsml_Grading21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gsml_Grading__gsml_Grading21", None)
        self.__gsml_Grading21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gsml_Task22"):
                    opp_val = getattr(item, "gsml_Task22", None)
                    
                    if opp_val == self:
                        setattr(item, "gsml_Task22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gsml_Task22"):
                    opp_val = getattr(item, "gsml_Task22", None)
                    
                    setattr(item, "gsml_Task22", self)
                    

    @property
    def gsml_Grading24(self):
        return self.__gsml_Grading24

    @gsml_Grading24.setter
    def gsml_Grading24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gsml_Grading__gsml_Grading24", None)
        self.__gsml_Grading24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gsml_Task25"):
                    opp_val = getattr(item, "gsml_Task25", None)
                    
                    if opp_val == self:
                        setattr(item, "gsml_Task25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gsml_Task25"):
                    opp_val = getattr(item, "gsml_Task25", None)
                    
                    setattr(item, "gsml_Task25", self)
                    

    @property
    def gsml_Grading18(self):
        return self.__gsml_Grading18

    @gsml_Grading18.setter
    def gsml_Grading18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gsml_Grading__gsml_Grading18", None)
        self.__gsml_Grading18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gsml_GradingScheme19"):
                opp_val = getattr(old_value, "gsml_GradingScheme19", None)
                if opp_val == self:
                    setattr(old_value, "gsml_GradingScheme19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gsml_GradingScheme19"):
                opp_val = getattr(value, "gsml_GradingScheme19", None)
                setattr(value, "gsml_GradingScheme19", self)

    @property
    def gsml_Grading(self):
        return self.__gsml_Grading

    @gsml_Grading.setter
    def gsml_Grading(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gsml_Grading__gsml_Grading", None)
        self.__gsml_Grading = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gsml_Course"):
                opp_val = getattr(old_value, "gsml_Course", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gsml_Course"):
                opp_val = getattr(value, "gsml_Course", None)
                if opp_val is None:
                    setattr(value, "gsml_Course", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class gsml_Task(ABC):

    def __init__(self, Name: str, MinRequirement: float, MinRequirementType: str, gsml_Task: "gsml_TaskGroup" = None, gsml_Task22: "gsml_Grading" = None, gsml_Task25: "gsml_Grading" = None):
        self.Name = Name
        self.MinRequirement = MinRequirement
        self.MinRequirementType = MinRequirementType
        self.gsml_Task = gsml_Task
        self.gsml_Task22 = gsml_Task22
        self.gsml_Task25 = gsml_Task25
        
    @property
    def MinRequirement(self) -> float:
        return self.__MinRequirement

    @MinRequirement.setter
    def MinRequirement(self, MinRequirement: float):
        self.__MinRequirement = MinRequirement

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def MinRequirementType(self) -> str:
        return self.__MinRequirementType

    @MinRequirementType.setter
    def MinRequirementType(self, MinRequirementType: str):
        self.__MinRequirementType = MinRequirementType

    @property
    def gsml_Task22(self):
        return self.__gsml_Task22

    @gsml_Task22.setter
    def gsml_Task22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gsml_Task__gsml_Task22", None)
        self.__gsml_Task22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gsml_Grading21"):
                opp_val = getattr(old_value, "gsml_Grading21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gsml_Grading21"):
                opp_val = getattr(value, "gsml_Grading21", None)
                if opp_val is None:
                    setattr(value, "gsml_Grading21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gsml_Task25(self):
        return self.__gsml_Task25

    @gsml_Task25.setter
    def gsml_Task25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gsml_Task__gsml_Task25", None)
        self.__gsml_Task25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gsml_Grading24"):
                opp_val = getattr(old_value, "gsml_Grading24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gsml_Grading24"):
                opp_val = getattr(value, "gsml_Grading24", None)
                if opp_val is None:
                    setattr(value, "gsml_Grading24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gsml_Task(self):
        return self.__gsml_Task

    @gsml_Task.setter
    def gsml_Task(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gsml_Task__gsml_Task", None)
        self.__gsml_Task = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gsml_TaskGroup"):
                opp_val = getattr(old_value, "gsml_TaskGroup", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gsml_TaskGroup"):
                opp_val = getattr(value, "gsml_TaskGroup", None)
                if opp_val is None:
                    setattr(value, "gsml_TaskGroup", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class gsml_Course:

    def __init__(self, Name: str, gsml_Course7: "gsml_GradingScheme" = None, gsml_Course: set["gsml_Grading"] = None, gsml_Course2: set["gsml_GradingScheme"] = None, gsml_Course4: "gsml_GradingScheme" = None, gsml_Course16: "gsml_GradingSystem" = None):
        self.Name = Name
        self.gsml_Course7 = gsml_Course7
        self.gsml_Course = gsml_Course if gsml_Course is not None else set()
        self.gsml_Course2 = gsml_Course2 if gsml_Course2 is not None else set()
        self.gsml_Course4 = gsml_Course4
        self.gsml_Course16 = gsml_Course16
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def gsml_Course7(self):
        return self.__gsml_Course7

    @gsml_Course7.setter
    def gsml_Course7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gsml_Course__gsml_Course7", None)
        self.__gsml_Course7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gsml_GradingScheme8"):
                opp_val = getattr(old_value, "gsml_GradingScheme8", None)
                if opp_val == self:
                    setattr(old_value, "gsml_GradingScheme8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gsml_GradingScheme8"):
                opp_val = getattr(value, "gsml_GradingScheme8", None)
                setattr(value, "gsml_GradingScheme8", self)

    @property
    def gsml_Course4(self):
        return self.__gsml_Course4

    @gsml_Course4.setter
    def gsml_Course4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gsml_Course__gsml_Course4", None)
        self.__gsml_Course4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gsml_GradingScheme5"):
                opp_val = getattr(old_value, "gsml_GradingScheme5", None)
                if opp_val == self:
                    setattr(old_value, "gsml_GradingScheme5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gsml_GradingScheme5"):
                opp_val = getattr(value, "gsml_GradingScheme5", None)
                setattr(value, "gsml_GradingScheme5", self)

    @property
    def gsml_Course(self):
        return self.__gsml_Course

    @gsml_Course.setter
    def gsml_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gsml_Course__gsml_Course", None)
        self.__gsml_Course = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gsml_Grading"):
                    opp_val = getattr(item, "gsml_Grading", None)
                    
                    if opp_val == self:
                        setattr(item, "gsml_Grading", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gsml_Grading"):
                    opp_val = getattr(item, "gsml_Grading", None)
                    
                    setattr(item, "gsml_Grading", self)
                    

    @property
    def gsml_Course2(self):
        return self.__gsml_Course2

    @gsml_Course2.setter
    def gsml_Course2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gsml_Course__gsml_Course2", None)
        self.__gsml_Course2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gsml_GradingScheme"):
                    opp_val = getattr(item, "gsml_GradingScheme", None)
                    
                    if opp_val == self:
                        setattr(item, "gsml_GradingScheme", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gsml_GradingScheme"):
                    opp_val = getattr(item, "gsml_GradingScheme", None)
                    
                    setattr(item, "gsml_GradingScheme", self)
                    

    @property
    def gsml_Course16(self):
        return self.__gsml_Course16

    @gsml_Course16.setter
    def gsml_Course16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gsml_Course__gsml_Course16", None)
        self.__gsml_Course16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gsml_GradingSystem"):
                opp_val = getattr(old_value, "gsml_GradingSystem", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gsml_GradingSystem"):
                opp_val = getattr(value, "gsml_GradingSystem", None)
                if opp_val is None:
                    setattr(value, "gsml_GradingSystem", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
