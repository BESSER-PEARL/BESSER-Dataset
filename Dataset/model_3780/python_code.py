from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class BinaryOperator(Enum):
    AND = "AND"
    OR = "OR"
class GroupType(Enum):
    OR = "OR"
    XOR = "XOR"


############################################
# Definition of Classes
############################################

class UnaryDependency:

    pass
class assignment6_model_IntegerValueDependency(UnaryDependency):

    def __init__(self, value: int, assignment6_model_IntegerValueDependency: "assignment6_model_IntegerFeature" = None):
        self.value = value
        self.assignment6_model_IntegerValueDependency = assignment6_model_IntegerValueDependency
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def assignment6_model_IntegerValueDependency(self):
        return self.__assignment6_model_IntegerValueDependency

    @assignment6_model_IntegerValueDependency.setter
    def assignment6_model_IntegerValueDependency(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assignment6_model_IntegerValueDependency__assignment6_model_IntegerValueDependency", None)
        self.__assignment6_model_IntegerValueDependency = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assignment6_model_IntegerFeature"):
                opp_val = getattr(old_value, "assignment6_model_IntegerFeature", None)
                if opp_val == self:
                    setattr(old_value, "assignment6_model_IntegerFeature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assignment6_model_IntegerFeature"):
                opp_val = getattr(value, "assignment6_model_IntegerFeature", None)
                setattr(value, "assignment6_model_IntegerFeature", self)

class assignment6_model_IsSelectedDependency(UnaryDependency):

    pass
class Dependency:

    pass
class assignment6_model_BinaryDependency(Dependency):

    def __init__(self, operator: str, assignment6_model_BinaryDependency: "assignment6_model_Dependency" = None, assignment6_model_BinaryDependency16: "assignment6_model_Dependency" = None):
        self.operator = operator
        self.assignment6_model_BinaryDependency = assignment6_model_BinaryDependency
        self.assignment6_model_BinaryDependency16 = assignment6_model_BinaryDependency16
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def assignment6_model_BinaryDependency16(self):
        return self.__assignment6_model_BinaryDependency16

    @assignment6_model_BinaryDependency16.setter
    def assignment6_model_BinaryDependency16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assignment6_model_BinaryDependency__assignment6_model_BinaryDependency16", None)
        self.__assignment6_model_BinaryDependency16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assignment6_model_Dependency17"):
                opp_val = getattr(old_value, "assignment6_model_Dependency17", None)
                if opp_val == self:
                    setattr(old_value, "assignment6_model_Dependency17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assignment6_model_Dependency17"):
                opp_val = getattr(value, "assignment6_model_Dependency17", None)
                setattr(value, "assignment6_model_Dependency17", self)

    @property
    def assignment6_model_BinaryDependency(self):
        return self.__assignment6_model_BinaryDependency

    @assignment6_model_BinaryDependency.setter
    def assignment6_model_BinaryDependency(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assignment6_model_BinaryDependency__assignment6_model_BinaryDependency", None)
        self.__assignment6_model_BinaryDependency = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assignment6_model_Dependency14"):
                opp_val = getattr(old_value, "assignment6_model_Dependency14", None)
                if opp_val == self:
                    setattr(old_value, "assignment6_model_Dependency14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assignment6_model_Dependency14"):
                opp_val = getattr(value, "assignment6_model_Dependency14", None)
                setattr(value, "assignment6_model_Dependency14", self)

class assignment6_model_UnaryDependency(Dependency):

    pass
class Feature:

    pass
class assignment6_model_SimpleFeature(Feature):

    pass
class assignment6_model_Dependency(ABC):

    def __init__(self, not: bool, assignment6_model_Dependency: "assignment6_model_Feature" = None, assignment6_model_Dependency14: "assignment6_model_BinaryDependency" = None, assignment6_model_Dependency17: "assignment6_model_BinaryDependency" = None):
        self.not = not
        self.assignment6_model_Dependency = assignment6_model_Dependency
        self.assignment6_model_Dependency14 = assignment6_model_Dependency14
        self.assignment6_model_Dependency17 = assignment6_model_Dependency17
        
    @property
    def not(self) -> bool:
        return self.__not

    @not.setter
    def not(self, not: bool):
        self.__not = not

    @property
    def assignment6_model_Dependency(self):
        return self.__assignment6_model_Dependency

    @assignment6_model_Dependency.setter
    def assignment6_model_Dependency(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assignment6_model_Dependency__assignment6_model_Dependency", None)
        self.__assignment6_model_Dependency = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assignment6_model_Feature10"):
                opp_val = getattr(old_value, "assignment6_model_Feature10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assignment6_model_Feature10"):
                opp_val = getattr(value, "assignment6_model_Feature10", None)
                if opp_val is None:
                    setattr(value, "assignment6_model_Feature10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def assignment6_model_Dependency14(self):
        return self.__assignment6_model_Dependency14

    @assignment6_model_Dependency14.setter
    def assignment6_model_Dependency14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assignment6_model_Dependency__assignment6_model_Dependency14", None)
        self.__assignment6_model_Dependency14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assignment6_model_BinaryDependency"):
                opp_val = getattr(old_value, "assignment6_model_BinaryDependency", None)
                if opp_val == self:
                    setattr(old_value, "assignment6_model_BinaryDependency", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assignment6_model_BinaryDependency"):
                opp_val = getattr(value, "assignment6_model_BinaryDependency", None)
                setattr(value, "assignment6_model_BinaryDependency", self)

    @property
    def assignment6_model_Dependency17(self):
        return self.__assignment6_model_Dependency17

    @assignment6_model_Dependency17.setter
    def assignment6_model_Dependency17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assignment6_model_Dependency__assignment6_model_Dependency17", None)
        self.__assignment6_model_Dependency17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assignment6_model_BinaryDependency16"):
                opp_val = getattr(old_value, "assignment6_model_BinaryDependency16", None)
                if opp_val == self:
                    setattr(old_value, "assignment6_model_BinaryDependency16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assignment6_model_BinaryDependency16"):
                opp_val = getattr(value, "assignment6_model_BinaryDependency16", None)
                setattr(value, "assignment6_model_BinaryDependency16", self)

class assignment6_model_Group:

    def __init__(self, name: str, groupType: str, assignment6_model_Group12: set["assignment6_model_SimpleFeature"] = None, assignment6_model_Group: "assignment6_model_Configurator" = None, assignment6_model_Group8: "assignment6_model_Feature" = None):
        self.name = name
        self.groupType = groupType
        self.assignment6_model_Group12 = assignment6_model_Group12 if assignment6_model_Group12 is not None else set()
        self.assignment6_model_Group = assignment6_model_Group
        self.assignment6_model_Group8 = assignment6_model_Group8
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def groupType(self) -> str:
        return self.__groupType

    @groupType.setter
    def groupType(self, groupType: str):
        self.__groupType = groupType

    @property
    def assignment6_model_Group8(self):
        return self.__assignment6_model_Group8

    @assignment6_model_Group8.setter
    def assignment6_model_Group8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assignment6_model_Group__assignment6_model_Group8", None)
        self.__assignment6_model_Group8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assignment6_model_Feature7"):
                opp_val = getattr(old_value, "assignment6_model_Feature7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assignment6_model_Feature7"):
                opp_val = getattr(value, "assignment6_model_Feature7", None)
                if opp_val is None:
                    setattr(value, "assignment6_model_Feature7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def assignment6_model_Group(self):
        return self.__assignment6_model_Group

    @assignment6_model_Group.setter
    def assignment6_model_Group(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assignment6_model_Group__assignment6_model_Group", None)
        self.__assignment6_model_Group = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assignment6_model_Configurator2"):
                opp_val = getattr(old_value, "assignment6_model_Configurator2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assignment6_model_Configurator2"):
                opp_val = getattr(value, "assignment6_model_Configurator2", None)
                if opp_val is None:
                    setattr(value, "assignment6_model_Configurator2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def assignment6_model_Group12(self):
        return self.__assignment6_model_Group12

    @assignment6_model_Group12.setter
    def assignment6_model_Group12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assignment6_model_Group__assignment6_model_Group12", None)
        self.__assignment6_model_Group12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "assignment6_model_SimpleFeature"):
                    opp_val = getattr(item, "assignment6_model_SimpleFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "assignment6_model_SimpleFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "assignment6_model_SimpleFeature"):
                    opp_val = getattr(item, "assignment6_model_SimpleFeature", None)
                    
                    setattr(item, "assignment6_model_SimpleFeature", self)
                    

class assignment6_model_IntegerFeature(Feature):

    def __init__(self, minValue: int, maxValue: int, step: int, value: int, assignment6_model_IntegerFeature: "assignment6_model_IntegerValueDependency" = None):
        self.minValue = minValue
        self.maxValue = maxValue
        self.step = step
        self.value = value
        self.assignment6_model_IntegerFeature = assignment6_model_IntegerFeature
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

    @property
    def minValue(self) -> int:
        return self.__minValue

    @minValue.setter
    def minValue(self, minValue: int):
        self.__minValue = minValue

    @property
    def step(self) -> int:
        return self.__step

    @step.setter
    def step(self, step: int):
        self.__step = step

    @property
    def maxValue(self) -> int:
        return self.__maxValue

    @maxValue.setter
    def maxValue(self, maxValue: int):
        self.__maxValue = maxValue

    @property
    def assignment6_model_IntegerFeature(self):
        return self.__assignment6_model_IntegerFeature

    @assignment6_model_IntegerFeature.setter
    def assignment6_model_IntegerFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assignment6_model_IntegerFeature__assignment6_model_IntegerFeature", None)
        self.__assignment6_model_IntegerFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assignment6_model_IntegerValueDependency"):
                opp_val = getattr(old_value, "assignment6_model_IntegerValueDependency", None)
                if opp_val == self:
                    setattr(old_value, "assignment6_model_IntegerValueDependency", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assignment6_model_IntegerValueDependency"):
                opp_val = getattr(value, "assignment6_model_IntegerValueDependency", None)
                setattr(value, "assignment6_model_IntegerValueDependency", self)

class assignment6_model_Feature(ABC):

    def __init__(self, name: str, mandatory: bool, selected: bool, assignment6_model_Feature: "assignment6_model_Configurator" = None, assignment6_model_Feature5: "assignment6_model_Feature" = None, assignment6_model_Feature3: set["assignment6_model_Feature"] = None, assignment6_model_Feature7: set["assignment6_model_Group"] = None, assignment6_model_Feature10: set["assignment6_model_Dependency"] = None, assignment6_model_Feature19: "assignment6_model_IsSelectedDependency" = None):
        self.name = name
        self.mandatory = mandatory
        self.selected = selected
        self.assignment6_model_Feature = assignment6_model_Feature
        self.assignment6_model_Feature5 = assignment6_model_Feature5
        self.assignment6_model_Feature3 = assignment6_model_Feature3 if assignment6_model_Feature3 is not None else set()
        self.assignment6_model_Feature7 = assignment6_model_Feature7 if assignment6_model_Feature7 is not None else set()
        self.assignment6_model_Feature10 = assignment6_model_Feature10 if assignment6_model_Feature10 is not None else set()
        self.assignment6_model_Feature19 = assignment6_model_Feature19
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mandatory(self) -> bool:
        return self.__mandatory

    @mandatory.setter
    def mandatory(self, mandatory: bool):
        self.__mandatory = mandatory

    @property
    def selected(self) -> bool:
        return self.__selected

    @selected.setter
    def selected(self, selected: bool):
        self.__selected = selected

    @property
    def assignment6_model_Feature10(self):
        return self.__assignment6_model_Feature10

    @assignment6_model_Feature10.setter
    def assignment6_model_Feature10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assignment6_model_Feature__assignment6_model_Feature10", None)
        self.__assignment6_model_Feature10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "assignment6_model_Dependency"):
                    opp_val = getattr(item, "assignment6_model_Dependency", None)
                    
                    if opp_val == self:
                        setattr(item, "assignment6_model_Dependency", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "assignment6_model_Dependency"):
                    opp_val = getattr(item, "assignment6_model_Dependency", None)
                    
                    setattr(item, "assignment6_model_Dependency", self)
                    

    @property
    def assignment6_model_Feature(self):
        return self.__assignment6_model_Feature

    @assignment6_model_Feature.setter
    def assignment6_model_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assignment6_model_Feature__assignment6_model_Feature", None)
        self.__assignment6_model_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assignment6_model_Configurator"):
                opp_val = getattr(old_value, "assignment6_model_Configurator", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assignment6_model_Configurator"):
                opp_val = getattr(value, "assignment6_model_Configurator", None)
                if opp_val is None:
                    setattr(value, "assignment6_model_Configurator", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def assignment6_model_Feature19(self):
        return self.__assignment6_model_Feature19

    @assignment6_model_Feature19.setter
    def assignment6_model_Feature19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assignment6_model_Feature__assignment6_model_Feature19", None)
        self.__assignment6_model_Feature19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assignment6_model_IsSelectedDependency"):
                opp_val = getattr(old_value, "assignment6_model_IsSelectedDependency", None)
                if opp_val == self:
                    setattr(old_value, "assignment6_model_IsSelectedDependency", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assignment6_model_IsSelectedDependency"):
                opp_val = getattr(value, "assignment6_model_IsSelectedDependency", None)
                setattr(value, "assignment6_model_IsSelectedDependency", self)

    @property
    def assignment6_model_Feature5(self):
        return self.__assignment6_model_Feature5

    @assignment6_model_Feature5.setter
    def assignment6_model_Feature5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assignment6_model_Feature__assignment6_model_Feature5", None)
        self.__assignment6_model_Feature5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assignment6_model_Feature3"):
                opp_val = getattr(old_value, "assignment6_model_Feature3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assignment6_model_Feature3"):
                opp_val = getattr(value, "assignment6_model_Feature3", None)
                if opp_val is None:
                    setattr(value, "assignment6_model_Feature3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def assignment6_model_Feature3(self):
        return self.__assignment6_model_Feature3

    @assignment6_model_Feature3.setter
    def assignment6_model_Feature3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assignment6_model_Feature__assignment6_model_Feature3", None)
        self.__assignment6_model_Feature3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "assignment6_model_Feature5"):
                    opp_val = getattr(item, "assignment6_model_Feature5", None)
                    
                    if opp_val == self:
                        setattr(item, "assignment6_model_Feature5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "assignment6_model_Feature5"):
                    opp_val = getattr(item, "assignment6_model_Feature5", None)
                    
                    setattr(item, "assignment6_model_Feature5", self)
                    

    @property
    def assignment6_model_Feature7(self):
        return self.__assignment6_model_Feature7

    @assignment6_model_Feature7.setter
    def assignment6_model_Feature7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assignment6_model_Feature__assignment6_model_Feature7", None)
        self.__assignment6_model_Feature7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "assignment6_model_Group8"):
                    opp_val = getattr(item, "assignment6_model_Group8", None)
                    
                    if opp_val == self:
                        setattr(item, "assignment6_model_Group8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "assignment6_model_Group8"):
                    opp_val = getattr(item, "assignment6_model_Group8", None)
                    
                    setattr(item, "assignment6_model_Group8", self)
                    

class assignment6_model_Configurator:

    def __init__(self, name: str, assignment6_model_Configurator: set["assignment6_model_Feature"] = None, assignment6_model_Configurator2: set["assignment6_model_Group"] = None):
        self.name = name
        self.assignment6_model_Configurator = assignment6_model_Configurator if assignment6_model_Configurator is not None else set()
        self.assignment6_model_Configurator2 = assignment6_model_Configurator2 if assignment6_model_Configurator2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def assignment6_model_Configurator(self):
        return self.__assignment6_model_Configurator

    @assignment6_model_Configurator.setter
    def assignment6_model_Configurator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assignment6_model_Configurator__assignment6_model_Configurator", None)
        self.__assignment6_model_Configurator = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "assignment6_model_Feature"):
                    opp_val = getattr(item, "assignment6_model_Feature", None)
                    
                    if opp_val == self:
                        setattr(item, "assignment6_model_Feature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "assignment6_model_Feature"):
                    opp_val = getattr(item, "assignment6_model_Feature", None)
                    
                    setattr(item, "assignment6_model_Feature", self)
                    

    @property
    def assignment6_model_Configurator2(self):
        return self.__assignment6_model_Configurator2

    @assignment6_model_Configurator2.setter
    def assignment6_model_Configurator2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_assignment6_model_Configurator__assignment6_model_Configurator2", None)
        self.__assignment6_model_Configurator2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "assignment6_model_Group"):
                    opp_val = getattr(item, "assignment6_model_Group", None)
                    
                    if opp_val == self:
                        setattr(item, "assignment6_model_Group", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "assignment6_model_Group"):
                    opp_val = getattr(item, "assignment6_model_Group", None)
                    
                    setattr(item, "assignment6_model_Group", self)
                    
