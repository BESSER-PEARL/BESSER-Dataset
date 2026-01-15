from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class MinRequirementsType(Enum):
    Percentage = "Percentage"
    Absolute = "Absolute"


############################################
# Definition of Classes
############################################

class gradingsystem_Task(ABC):

    def __init__(self, name: str, gradingsystem_Task: "gradingsystem_MinRequirement" = None, gradingsystem_Task5: "gradingsystem_TaskGroup" = None, gradingsystem_Task12: "gradingsystem_Grading" = None):
        self.name = name
        self.gradingsystem_Task = gradingsystem_Task
        self.gradingsystem_Task5 = gradingsystem_Task5
        self.gradingsystem_Task12 = gradingsystem_Task12
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def gradingsystem_Task12(self):
        return self.__gradingsystem_Task12

    @gradingsystem_Task12.setter
    def gradingsystem_Task12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gradingsystem_Task__gradingsystem_Task12", None)
        self.__gradingsystem_Task12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gradingsystem_Grading11"):
                opp_val = getattr(old_value, "gradingsystem_Grading11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gradingsystem_Grading11"):
                opp_val = getattr(value, "gradingsystem_Grading11", None)
                if opp_val is None:
                    setattr(value, "gradingsystem_Grading11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gradingsystem_Task(self):
        return self.__gradingsystem_Task

    @gradingsystem_Task.setter
    def gradingsystem_Task(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gradingsystem_Task__gradingsystem_Task", None)
        self.__gradingsystem_Task = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gradingsystem_MinRequirement"):
                opp_val = getattr(old_value, "gradingsystem_MinRequirement", None)
                if opp_val == self:
                    setattr(old_value, "gradingsystem_MinRequirement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gradingsystem_MinRequirement"):
                opp_val = getattr(value, "gradingsystem_MinRequirement", None)
                setattr(value, "gradingsystem_MinRequirement", self)

    @property
    def gradingsystem_Task5(self):
        return self.__gradingsystem_Task5

    @gradingsystem_Task5.setter
    def gradingsystem_Task5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gradingsystem_Task__gradingsystem_Task5", None)
        self.__gradingsystem_Task5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gradingsystem_TaskGroup"):
                opp_val = getattr(old_value, "gradingsystem_TaskGroup", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gradingsystem_TaskGroup"):
                opp_val = getattr(value, "gradingsystem_TaskGroup", None)
                if opp_val is None:
                    setattr(value, "gradingsystem_TaskGroup", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class gradingsystem_Grade:

    def __init__(self, name: str, requiredPoints: int, gradingsystem_Grade: "gradingsystem_GradingScheme" = None, gradingsystem_Grade9: "gradingsystem_GradingScheme" = None):
        self.name = name
        self.requiredPoints = requiredPoints
        self.gradingsystem_Grade = gradingsystem_Grade
        self.gradingsystem_Grade9 = gradingsystem_Grade9
        
    @property
    def requiredPoints(self) -> int:
        return self.__requiredPoints

    @requiredPoints.setter
    def requiredPoints(self, requiredPoints: int):
        self.__requiredPoints = requiredPoints

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def gradingsystem_Grade9(self):
        return self.__gradingsystem_Grade9

    @gradingsystem_Grade9.setter
    def gradingsystem_Grade9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gradingsystem_Grade__gradingsystem_Grade9", None)
        self.__gradingsystem_Grade9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gradingsystem_GradingScheme8"):
                opp_val = getattr(old_value, "gradingsystem_GradingScheme8", None)
                if opp_val == self:
                    setattr(old_value, "gradingsystem_GradingScheme8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gradingsystem_GradingScheme8"):
                opp_val = getattr(value, "gradingsystem_GradingScheme8", None)
                setattr(value, "gradingsystem_GradingScheme8", self)

    @property
    def gradingsystem_Grade(self):
        return self.__gradingsystem_Grade

    @gradingsystem_Grade.setter
    def gradingsystem_Grade(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gradingsystem_Grade__gradingsystem_Grade", None)
        self.__gradingsystem_Grade = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gradingsystem_GradingScheme"):
                opp_val = getattr(old_value, "gradingsystem_GradingScheme", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gradingsystem_GradingScheme"):
                opp_val = getattr(value, "gradingsystem_GradingScheme", None)
                if opp_val is None:
                    setattr(value, "gradingsystem_GradingScheme", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class gradingsystem_GradingScheme:

    pass
class Task:

    pass
class gradingsystem_TaskGroup(Task):

    pass
class gradingsystem_ConcreteTask(Task):

    def __init__(self, maxPoints: int):
        self.maxPoints = maxPoints
        
    @property
    def maxPoints(self) -> int:
        return self.__maxPoints

    @maxPoints.setter
    def maxPoints(self, maxPoints: int):
        self.__maxPoints = maxPoints

class gradingsystem_MinRequirement:

    def __init__(self, value: int, type: str, gradingsystem_MinRequirement: "gradingsystem_Task" = None):
        self.value = value
        self.type = type
        self.gradingsystem_MinRequirement = gradingsystem_MinRequirement
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def gradingsystem_MinRequirement(self):
        return self.__gradingsystem_MinRequirement

    @gradingsystem_MinRequirement.setter
    def gradingsystem_MinRequirement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gradingsystem_MinRequirement__gradingsystem_MinRequirement", None)
        self.__gradingsystem_MinRequirement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gradingsystem_Task"):
                opp_val = getattr(old_value, "gradingsystem_Task", None)
                if opp_val == self:
                    setattr(old_value, "gradingsystem_Task", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gradingsystem_Task"):
                opp_val = getattr(value, "gradingsystem_Task", None)
                setattr(value, "gradingsystem_Task", self)

class gradingsystem_Grading:

    def __init__(self, semester: str, gradingsystem_Grading: "gradingsystem_Course" = None, gradingsystem_Grading11: set["gradingsystem_Task"] = None, gradingsystem_Grading14: "gradingsystem_GradingScheme" = None):
        self.semester = semester
        self.gradingsystem_Grading = gradingsystem_Grading
        self.gradingsystem_Grading11 = gradingsystem_Grading11 if gradingsystem_Grading11 is not None else set()
        self.gradingsystem_Grading14 = gradingsystem_Grading14
        
    @property
    def semester(self) -> str:
        return self.__semester

    @semester.setter
    def semester(self, semester: str):
        self.__semester = semester

    @property
    def gradingsystem_Grading(self):
        return self.__gradingsystem_Grading

    @gradingsystem_Grading.setter
    def gradingsystem_Grading(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gradingsystem_Grading__gradingsystem_Grading", None)
        self.__gradingsystem_Grading = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gradingsystem_Course2"):
                opp_val = getattr(old_value, "gradingsystem_Course2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gradingsystem_Course2"):
                opp_val = getattr(value, "gradingsystem_Course2", None)
                if opp_val is None:
                    setattr(value, "gradingsystem_Course2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def gradingsystem_Grading11(self):
        return self.__gradingsystem_Grading11

    @gradingsystem_Grading11.setter
    def gradingsystem_Grading11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gradingsystem_Grading__gradingsystem_Grading11", None)
        self.__gradingsystem_Grading11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gradingsystem_Task12"):
                    opp_val = getattr(item, "gradingsystem_Task12", None)
                    
                    if opp_val == self:
                        setattr(item, "gradingsystem_Task12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gradingsystem_Task12"):
                    opp_val = getattr(item, "gradingsystem_Task12", None)
                    
                    setattr(item, "gradingsystem_Task12", self)
                    

    @property
    def gradingsystem_Grading14(self):
        return self.__gradingsystem_Grading14

    @gradingsystem_Grading14.setter
    def gradingsystem_Grading14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gradingsystem_Grading__gradingsystem_Grading14", None)
        self.__gradingsystem_Grading14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gradingsystem_GradingScheme15"):
                opp_val = getattr(old_value, "gradingsystem_GradingScheme15", None)
                if opp_val == self:
                    setattr(old_value, "gradingsystem_GradingScheme15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gradingsystem_GradingScheme15"):
                opp_val = getattr(value, "gradingsystem_GradingScheme15", None)
                setattr(value, "gradingsystem_GradingScheme15", self)

class gradingsystem_Course:

    def __init__(self, name: str, gradingsystem_Course: "gradingsystem_GradingSystem" = None, gradingsystem_Course2: set["gradingsystem_Grading"] = None):
        self.name = name
        self.gradingsystem_Course = gradingsystem_Course
        self.gradingsystem_Course2 = gradingsystem_Course2 if gradingsystem_Course2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def gradingsystem_Course2(self):
        return self.__gradingsystem_Course2

    @gradingsystem_Course2.setter
    def gradingsystem_Course2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gradingsystem_Course__gradingsystem_Course2", None)
        self.__gradingsystem_Course2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "gradingsystem_Grading"):
                    opp_val = getattr(item, "gradingsystem_Grading", None)
                    
                    if opp_val == self:
                        setattr(item, "gradingsystem_Grading", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "gradingsystem_Grading"):
                    opp_val = getattr(item, "gradingsystem_Grading", None)
                    
                    setattr(item, "gradingsystem_Grading", self)
                    

    @property
    def gradingsystem_Course(self):
        return self.__gradingsystem_Course

    @gradingsystem_Course.setter
    def gradingsystem_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_gradingsystem_Course__gradingsystem_Course", None)
        self.__gradingsystem_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gradingsystem_GradingSystem"):
                opp_val = getattr(old_value, "gradingsystem_GradingSystem", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gradingsystem_GradingSystem"):
                opp_val = getattr(value, "gradingsystem_GradingSystem", None)
                if opp_val is None:
                    setattr(value, "gradingsystem_GradingSystem", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class gradingsystem_GradingSystem:

    pass