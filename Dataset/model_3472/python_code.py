from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Operator(Enum):
    select = "select"
    add = "add"
    remove = "remove"
    multiply = "multiply"
    divide = "divide"
class ComparisonOperator(Enum):
    equal = "equal"
    geq = "geq"
    gt = "gt"
    leq = "leq"
    lt = "lt"
class LogicalOperator(Enum):
    void = "void"
    and = "and"
    or = "or"


############################################
# Definition of Classes
############################################

class EFM_NodeFeatureElement(ABC):

    pass
class NodeFeatureElement:

    pass
class EFM_IntValue:

    pass
class Operation:

    pass
class EFM_ValueOperation(Operation):

    pass
class EFM_RangeOperation(Operation):

    def __init__(self, min: int, max: int, EFM_RangeOperation: "EFM_Attribute" = None):
        self.min = min
        self.max = max
        self.EFM_RangeOperation = EFM_RangeOperation
        
    @property
    def min(self) -> int:
        return self.__min

    @min.setter
    def min(self, min: int):
        self.__min = min

    @property
    def max(self) -> int:
        return self.__max

    @max.setter
    def max(self, max: int):
        self.__max = max

    @property
    def EFM_RangeOperation(self):
        return self.__EFM_RangeOperation

    @EFM_RangeOperation.setter
    def EFM_RangeOperation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EFM_RangeOperation__EFM_RangeOperation", None)
        self.__EFM_RangeOperation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EFM_Attribute38"):
                opp_val = getattr(old_value, "EFM_Attribute38", None)
                if opp_val == self:
                    setattr(old_value, "EFM_Attribute38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EFM_Attribute38"):
                opp_val = getattr(value, "EFM_Attribute38", None)
                setattr(value, "EFM_Attribute38", self)

class FMElement:

    pass
class EFM_Attribute(FMElement):

    def __init__(self, name: str, EFM_Attribute15: "EFM_Value" = None, EFM_Attribute: "EFM_Feature" = None, EFM_Attribute38: "EFM_RangeOperation" = None, EFM_Attribute40: "EFM_ValueOperation" = None, EFM_Attribute50: "EFM_NodeFeature" = None, EFM_Attribute70: "EFM_ResourceVerification" = None, EFM_Attribute73: "EFM_ResourceVerification" = None):
        self.name = name
        self.EFM_Attribute15 = EFM_Attribute15
        self.EFM_Attribute = EFM_Attribute
        self.EFM_Attribute38 = EFM_Attribute38
        self.EFM_Attribute40 = EFM_Attribute40
        self.EFM_Attribute50 = EFM_Attribute50
        self.EFM_Attribute70 = EFM_Attribute70
        self.EFM_Attribute73 = EFM_Attribute73
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def EFM_Attribute73(self):
        return self.__EFM_Attribute73

    @EFM_Attribute73.setter
    def EFM_Attribute73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EFM_Attribute__EFM_Attribute73", None)
        self.__EFM_Attribute73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EFM_ResourceVerification72"):
                opp_val = getattr(old_value, "EFM_ResourceVerification72", None)
                if opp_val == self:
                    setattr(old_value, "EFM_ResourceVerification72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EFM_ResourceVerification72"):
                opp_val = getattr(value, "EFM_ResourceVerification72", None)
                setattr(value, "EFM_ResourceVerification72", self)

    @property
    def EFM_Attribute40(self):
        return self.__EFM_Attribute40

    @EFM_Attribute40.setter
    def EFM_Attribute40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EFM_Attribute__EFM_Attribute40", None)
        self.__EFM_Attribute40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EFM_ValueOperation"):
                opp_val = getattr(old_value, "EFM_ValueOperation", None)
                if opp_val == self:
                    setattr(old_value, "EFM_ValueOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EFM_ValueOperation"):
                opp_val = getattr(value, "EFM_ValueOperation", None)
                setattr(value, "EFM_ValueOperation", self)

    @property
    def EFM_Attribute15(self):
        return self.__EFM_Attribute15

    @EFM_Attribute15.setter
    def EFM_Attribute15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EFM_Attribute__EFM_Attribute15", None)
        self.__EFM_Attribute15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EFM_Value"):
                opp_val = getattr(old_value, "EFM_Value", None)
                if opp_val == self:
                    setattr(old_value, "EFM_Value", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EFM_Value"):
                opp_val = getattr(value, "EFM_Value", None)
                setattr(value, "EFM_Value", self)

    @property
    def EFM_Attribute50(self):
        return self.__EFM_Attribute50

    @EFM_Attribute50.setter
    def EFM_Attribute50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EFM_Attribute__EFM_Attribute50", None)
        self.__EFM_Attribute50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EFM_NodeFeature49"):
                opp_val = getattr(old_value, "EFM_NodeFeature49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EFM_NodeFeature49"):
                opp_val = getattr(value, "EFM_NodeFeature49", None)
                if opp_val is None:
                    setattr(value, "EFM_NodeFeature49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def EFM_Attribute(self):
        return self.__EFM_Attribute

    @EFM_Attribute.setter
    def EFM_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EFM_Attribute__EFM_Attribute", None)
        self.__EFM_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EFM_Feature4"):
                opp_val = getattr(old_value, "EFM_Feature4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EFM_Feature4"):
                opp_val = getattr(value, "EFM_Feature4", None)
                if opp_val is None:
                    setattr(value, "EFM_Feature4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def EFM_Attribute70(self):
        return self.__EFM_Attribute70

    @EFM_Attribute70.setter
    def EFM_Attribute70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EFM_Attribute__EFM_Attribute70", None)
        self.__EFM_Attribute70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EFM_ResourceVerification"):
                opp_val = getattr(old_value, "EFM_ResourceVerification", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EFM_ResourceVerification"):
                opp_val = getattr(value, "EFM_ResourceVerification", None)
                if opp_val is None:
                    setattr(value, "EFM_ResourceVerification", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def EFM_Attribute38(self):
        return self.__EFM_Attribute38

    @EFM_Attribute38.setter
    def EFM_Attribute38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EFM_Attribute__EFM_Attribute38", None)
        self.__EFM_Attribute38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EFM_RangeOperation"):
                opp_val = getattr(old_value, "EFM_RangeOperation", None)
                if opp_val == self:
                    setattr(old_value, "EFM_RangeOperation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EFM_RangeOperation"):
                opp_val = getattr(value, "EFM_RangeOperation", None)
                setattr(value, "EFM_RangeOperation", self)

class EFM_FMElement:

    pass
class EFM_Feature(FMElement):

    def __init__(self, name: str, EFM_Feature9: "EFM_FeatCardinality" = None, EFM_Feature11: set["EFM_NodeFeature"] = None, EFM_Feature13: "EFM_Alternative" = None, EFM_Feature17: "EFM_BooleanConstraint" = None, EFM_Feature20: "EFM_BooleanConstraint" = None, EFM_Feature: "EFM_FeatureModel" = None, EFM_Feature4: set["EFM_Attribute"] = None, EFM_Feature7: "EFM_Feature" = None, EFM_Feature5: set["EFM_Feature"] = None, EFM_Feature26: "EFM_Functional" = None, EFM_Feature29: "EFM_Functional" = None, EFM_Feature36: "EFM_Operation" = None, EFM_Feature60: "EFM_HostedBy" = None, EFM_Feature44: "EFM_Colocated" = None, EFM_Feature47: "EFM_Colocated" = None, EFM_Feature79: "EFM_NotHostedBy" = None, EFM_Feature65: "EFM_Separated" = None, EFM_Feature68: "EFM_Separated" = None):
        self.name = name
        self.EFM_Feature9 = EFM_Feature9
        self.EFM_Feature11 = EFM_Feature11 if EFM_Feature11 is not None else set()
        self.EFM_Feature13 = EFM_Feature13
        self.EFM_Feature17 = EFM_Feature17
        self.EFM_Feature20 = EFM_Feature20
        self.EFM_Feature = EFM_Feature
        self.EFM_Feature4 = EFM_Feature4 if EFM_Feature4 is not None else set()
        self.EFM_Feature7 = EFM_Feature7
        self.EFM_Feature5 = EFM_Feature5 if EFM_Feature5 is not None else set()
        self.EFM_Feature26 = EFM_Feature26
        self.EFM_Feature29 = EFM_Feature29
        self.EFM_Feature36 = EFM_Feature36
        self.EFM_Feature60 = EFM_Feature60
        self.EFM_Feature44 = EFM_Feature44
        self.EFM_Feature47 = EFM_Feature47
        self.EFM_Feature79 = EFM_Feature79
        self.EFM_Feature65 = EFM_Feature65
        self.EFM_Feature68 = EFM_Feature68
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def EFM_Feature4(self):
        return self.__EFM_Feature4

    @EFM_Feature4.setter
    def EFM_Feature4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EFM_Feature__EFM_Feature4", None)
        self.__EFM_Feature4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EFM_Attribute"):
                    opp_val = getattr(item, "EFM_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "EFM_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EFM_Attribute"):
                    opp_val = getattr(item, "EFM_Attribute", None)
                    
                    setattr(item, "EFM_Attribute", self)
                    

    @property
    def EFM_Feature13(self):
        return self.__EFM_Feature13

    @EFM_Feature13.setter
    def EFM_Feature13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EFM_Feature__EFM_Feature13", None)
        self.__EFM_Feature13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EFM_Alternative"):
                opp_val = getattr(old_value, "EFM_Alternative", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EFM_Alternative"):
                opp_val = getattr(value, "EFM_Alternative", None)
                if opp_val is None:
                    setattr(value, "EFM_Alternative", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def EFM_Feature44(self):
        return self.__EFM_Feature44

    @EFM_Feature44.setter
    def EFM_Feature44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EFM_Feature__EFM_Feature44", None)
        self.__EFM_Feature44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EFM_Colocated"):
                opp_val = getattr(old_value, "EFM_Colocated", None)
                if opp_val == self:
                    setattr(old_value, "EFM_Colocated", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EFM_Colocated"):
                opp_val = getattr(value, "EFM_Colocated", None)
                setattr(value, "EFM_Colocated", self)

    @property
    def EFM_Feature7(self):
        return self.__EFM_Feature7

    @EFM_Feature7.setter
    def EFM_Feature7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EFM_Feature__EFM_Feature7", None)
        self.__EFM_Feature7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EFM_Feature5"):
                opp_val = getattr(old_value, "EFM_Feature5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EFM_Feature5"):
                opp_val = getattr(value, "EFM_Feature5", None)
                if opp_val is None:
                    setattr(value, "EFM_Feature5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def EFM_Feature29(self):
        return self.__EFM_Feature29

    @EFM_Feature29.setter
    def EFM_Feature29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EFM_Feature__EFM_Feature29", None)
        self.__EFM_Feature29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EFM_Functional28"):
                opp_val = getattr(old_value, "EFM_Functional28", None)
                if opp_val == self:
                    setattr(old_value, "EFM_Functional28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EFM_Functional28"):
                opp_val = getattr(value, "EFM_Functional28", None)
                setattr(value, "EFM_Functional28", self)

    @property
    def EFM_Feature60(self):
        return self.__EFM_Feature60

    @EFM_Feature60.setter
    def EFM_Feature60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EFM_Feature__EFM_Feature60", None)
        self.__EFM_Feature60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EFM_HostedBy59"):
                opp_val = getattr(old_value, "EFM_HostedBy59", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EFM_HostedBy59"):
                opp_val = getattr(value, "EFM_HostedBy59", None)
                if opp_val is None:
                    setattr(value, "EFM_HostedBy59", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def EFM_Feature79(self):
        return self.__EFM_Feature79

    @EFM_Feature79.setter
    def EFM_Feature79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EFM_Feature__EFM_Feature79", None)
        self.__EFM_Feature79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EFM_NotHostedBy78"):
                opp_val = getattr(old_value, "EFM_NotHostedBy78", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EFM_NotHostedBy78"):
                opp_val = getattr(value, "EFM_NotHostedBy78", None)
                if opp_val is None:
                    setattr(value, "EFM_NotHostedBy78", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def EFM_Feature(self):
        return self.__EFM_Feature

    @EFM_Feature.setter
    def EFM_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EFM_Feature__EFM_Feature", None)
        self.__EFM_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EFM_FeatureModel2"):
                opp_val = getattr(old_value, "EFM_FeatureModel2", None)
                if opp_val == self:
                    setattr(old_value, "EFM_FeatureModel2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EFM_FeatureModel2"):
                opp_val = getattr(value, "EFM_FeatureModel2", None)
                setattr(value, "EFM_FeatureModel2", self)

    @property
    def EFM_Feature36(self):
        return self.__EFM_Feature36

    @EFM_Feature36.setter
    def EFM_Feature36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EFM_Feature__EFM_Feature36", None)
        self.__EFM_Feature36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EFM_Operation35"):
                opp_val = getattr(old_value, "EFM_Operation35", None)
                if opp_val == self:
                    setattr(old_value, "EFM_Operation35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EFM_Operation35"):
                opp_val = getattr(value, "EFM_Operation35", None)
                setattr(value, "EFM_Operation35", self)

    @property
    def EFM_Feature9(self):
        return self.__EFM_Feature9

    @EFM_Feature9.setter
    def EFM_Feature9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EFM_Feature__EFM_Feature9", None)
        self.__EFM_Feature9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EFM_FeatCardinality"):
                opp_val = getattr(old_value, "EFM_FeatCardinality", None)
                if opp_val == self:
                    setattr(old_value, "EFM_FeatCardinality", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EFM_FeatCardinality"):
                opp_val = getattr(value, "EFM_FeatCardinality", None)
                setattr(value, "EFM_FeatCardinality", self)

    @property
    def EFM_Feature65(self):
        return self.__EFM_Feature65

    @EFM_Feature65.setter
    def EFM_Feature65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EFM_Feature__EFM_Feature65", None)
        self.__EFM_Feature65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EFM_Separated"):
                opp_val = getattr(old_value, "EFM_Separated", None)
                if opp_val == self:
                    setattr(old_value, "EFM_Separated", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EFM_Separated"):
                opp_val = getattr(value, "EFM_Separated", None)
                setattr(value, "EFM_Separated", self)

    @property
    def EFM_Feature11(self):
        return self.__EFM_Feature11

    @EFM_Feature11.setter
    def EFM_Feature11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EFM_Feature__EFM_Feature11", None)
        self.__EFM_Feature11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EFM_NodeFeature"):
                    opp_val = getattr(item, "EFM_NodeFeature", None)
                    
                    if opp_val == self:
                        setattr(item, "EFM_NodeFeature", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EFM_NodeFeature"):
                    opp_val = getattr(item, "EFM_NodeFeature", None)
                    
                    setattr(item, "EFM_NodeFeature", self)
                    

    @property
    def EFM_Feature47(self):
        return self.__EFM_Feature47

    @EFM_Feature47.setter
    def EFM_Feature47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EFM_Feature__EFM_Feature47", None)
        self.__EFM_Feature47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EFM_Colocated46"):
                opp_val = getattr(old_value, "EFM_Colocated46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EFM_Colocated46"):
                opp_val = getattr(value, "EFM_Colocated46", None)
                if opp_val is None:
                    setattr(value, "EFM_Colocated46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def EFM_Feature68(self):
        return self.__EFM_Feature68

    @EFM_Feature68.setter
    def EFM_Feature68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EFM_Feature__EFM_Feature68", None)
        self.__EFM_Feature68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EFM_Separated67"):
                opp_val = getattr(old_value, "EFM_Separated67", None)
                if opp_val == self:
                    setattr(old_value, "EFM_Separated67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EFM_Separated67"):
                opp_val = getattr(value, "EFM_Separated67", None)
                setattr(value, "EFM_Separated67", self)

    @property
    def EFM_Feature5(self):
        return self.__EFM_Feature5

    @EFM_Feature5.setter
    def EFM_Feature5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EFM_Feature__EFM_Feature5", None)
        self.__EFM_Feature5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EFM_Feature7"):
                    opp_val = getattr(item, "EFM_Feature7", None)
                    
                    if opp_val == self:
                        setattr(item, "EFM_Feature7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EFM_Feature7"):
                    opp_val = getattr(item, "EFM_Feature7", None)
                    
                    setattr(item, "EFM_Feature7", self)
                    

    @property
    def EFM_Feature17(self):
        return self.__EFM_Feature17

    @EFM_Feature17.setter
    def EFM_Feature17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EFM_Feature__EFM_Feature17", None)
        self.__EFM_Feature17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EFM_BooleanConstraint"):
                opp_val = getattr(old_value, "EFM_BooleanConstraint", None)
                if opp_val == self:
                    setattr(old_value, "EFM_BooleanConstraint", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EFM_BooleanConstraint"):
                opp_val = getattr(value, "EFM_BooleanConstraint", None)
                setattr(value, "EFM_BooleanConstraint", self)

    @property
    def EFM_Feature26(self):
        return self.__EFM_Feature26

    @EFM_Feature26.setter
    def EFM_Feature26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EFM_Feature__EFM_Feature26", None)
        self.__EFM_Feature26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EFM_Functional"):
                opp_val = getattr(old_value, "EFM_Functional", None)
                if opp_val == self:
                    setattr(old_value, "EFM_Functional", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EFM_Functional"):
                opp_val = getattr(value, "EFM_Functional", None)
                setattr(value, "EFM_Functional", self)

    @property
    def EFM_Feature20(self):
        return self.__EFM_Feature20

    @EFM_Feature20.setter
    def EFM_Feature20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EFM_Feature__EFM_Feature20", None)
        self.__EFM_Feature20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EFM_BooleanConstraint19"):
                opp_val = getattr(old_value, "EFM_BooleanConstraint19", None)
                if opp_val == self:
                    setattr(old_value, "EFM_BooleanConstraint19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EFM_BooleanConstraint19"):
                opp_val = getattr(value, "EFM_BooleanConstraint19", None)
                setattr(value, "EFM_BooleanConstraint19", self)

class EFM_FMConstraint(ABC):

    pass
class EFM_FeatureModel:

    pass
class EFM_Operation:

    pass
class BooleanConstraint:

    pass
class EFM_Excludes(BooleanConstraint):

    pass
class EFM_Implies(BooleanConstraint):

    pass
class Cardinality:

    pass
class FMConstraint:

    pass
class EFM_Separated(FMConstraint):

    pass
class EFM_HostedBy(FMConstraint):

    pass
class EFM_Functional(FMConstraint):

    def __init__(self, type: str, value: int, EFM_Functional: "EFM_Feature" = None, EFM_Functional28: "EFM_Feature" = None):
        self.type = type
        self.value = value
        self.EFM_Functional = EFM_Functional
        self.EFM_Functional28 = EFM_Functional28
        
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
    def EFM_Functional(self):
        return self.__EFM_Functional

    @EFM_Functional.setter
    def EFM_Functional(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EFM_Functional__EFM_Functional", None)
        self.__EFM_Functional = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EFM_Feature26"):
                opp_val = getattr(old_value, "EFM_Feature26", None)
                if opp_val == self:
                    setattr(old_value, "EFM_Feature26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EFM_Feature26"):
                opp_val = getattr(value, "EFM_Feature26", None)
                setattr(value, "EFM_Feature26", self)

    @property
    def EFM_Functional28(self):
        return self.__EFM_Functional28

    @EFM_Functional28.setter
    def EFM_Functional28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EFM_Functional__EFM_Functional28", None)
        self.__EFM_Functional28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EFM_Feature29"):
                opp_val = getattr(old_value, "EFM_Feature29", None)
                if opp_val == self:
                    setattr(old_value, "EFM_Feature29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EFM_Feature29"):
                opp_val = getattr(value, "EFM_Feature29", None)
                setattr(value, "EFM_Feature29", self)

class EFM_Comparison(FMConstraint):

    def __init__(self, type: str, EFM_Comparison: "EFM_FMElement" = None, EFM_Comparison32: "EFM_FMElement" = None):
        self.type = type
        self.EFM_Comparison = EFM_Comparison
        self.EFM_Comparison32 = EFM_Comparison32
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def EFM_Comparison32(self):
        return self.__EFM_Comparison32

    @EFM_Comparison32.setter
    def EFM_Comparison32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EFM_Comparison__EFM_Comparison32", None)
        self.__EFM_Comparison32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EFM_FMElement33"):
                opp_val = getattr(old_value, "EFM_FMElement33", None)
                if opp_val == self:
                    setattr(old_value, "EFM_FMElement33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EFM_FMElement33"):
                opp_val = getattr(value, "EFM_FMElement33", None)
                setattr(value, "EFM_FMElement33", self)

    @property
    def EFM_Comparison(self):
        return self.__EFM_Comparison

    @EFM_Comparison.setter
    def EFM_Comparison(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EFM_Comparison__EFM_Comparison", None)
        self.__EFM_Comparison = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EFM_FMElement"):
                opp_val = getattr(old_value, "EFM_FMElement", None)
                if opp_val == self:
                    setattr(old_value, "EFM_FMElement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EFM_FMElement"):
                opp_val = getattr(value, "EFM_FMElement", None)
                setattr(value, "EFM_FMElement", self)

class EFM_Requires(FMConstraint):

    def __init__(self, operator: str, EFM_Requires: set["EFM_Operation"] = None, EFM_Requires23: "EFM_Operation" = None):
        self.operator = operator
        self.EFM_Requires = EFM_Requires if EFM_Requires is not None else set()
        self.EFM_Requires23 = EFM_Requires23
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def EFM_Requires(self):
        return self.__EFM_Requires

    @EFM_Requires.setter
    def EFM_Requires(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EFM_Requires__EFM_Requires", None)
        self.__EFM_Requires = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EFM_Operation"):
                    opp_val = getattr(item, "EFM_Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "EFM_Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EFM_Operation"):
                    opp_val = getattr(item, "EFM_Operation", None)
                    
                    setattr(item, "EFM_Operation", self)
                    

    @property
    def EFM_Requires23(self):
        return self.__EFM_Requires23

    @EFM_Requires23.setter
    def EFM_Requires23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EFM_Requires__EFM_Requires23", None)
        self.__EFM_Requires23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EFM_Operation24"):
                opp_val = getattr(old_value, "EFM_Operation24", None)
                if opp_val == self:
                    setattr(old_value, "EFM_Operation24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EFM_Operation24"):
                opp_val = getattr(value, "EFM_Operation24", None)
                setattr(value, "EFM_Operation24", self)

class EFM_ResourceVerification(FMConstraint):

    pass
class EFM_Colocated(FMConstraint):

    pass
class EFM_NotHostedBy(FMConstraint):

    pass
class EFM_BooleanConstraint(FMConstraint):

    pass
class EFM_Value:

    pass
class EFM_Cardinality(ABC):

    def __init__(self, cardinalityMin: int, cardinalityMax: int, configValue: int):
        self.cardinalityMin = cardinalityMin
        self.cardinalityMax = cardinalityMax
        self.configValue = configValue
        
    @property
    def cardinalityMin(self) -> int:
        return self.__cardinalityMin

    @cardinalityMin.setter
    def cardinalityMin(self, cardinalityMin: int):
        self.__cardinalityMin = cardinalityMin

    @property
    def cardinalityMax(self) -> int:
        return self.__cardinalityMax

    @cardinalityMax.setter
    def cardinalityMax(self, cardinalityMax: int):
        self.__cardinalityMax = cardinalityMax

    @property
    def configValue(self) -> int:
        return self.__configValue

    @configValue.setter
    def configValue(self, configValue: int):
        self.__configValue = configValue

class Feature:

    pass
class EFM_Alternative(Feature):

    pass
class Alternative:

    pass
class EFM_Exclusive(Alternative):

    pass
class EFM_NodeFeature(NodeFeatureElement):

    def __init__(self, name: str, EFM_NodeFeature: "EFM_Feature" = None, EFM_NodeFeature49: set["EFM_Attribute"] = None, EFM_NodeFeature52: "EFM_FeatCardinality" = None, EFM_NodeFeature55: "EFM_HostedBy" = None, EFM_NodeFeature57: "EFM_NotHostedBy" = None, EFM_NodeFeature63: "EFM_HostedBy" = None, EFM_NodeFeature76: "EFM_NotHostedBy" = None):
        self.name = name
        self.EFM_NodeFeature = EFM_NodeFeature
        self.EFM_NodeFeature49 = EFM_NodeFeature49 if EFM_NodeFeature49 is not None else set()
        self.EFM_NodeFeature52 = EFM_NodeFeature52
        self.EFM_NodeFeature55 = EFM_NodeFeature55
        self.EFM_NodeFeature57 = EFM_NodeFeature57
        self.EFM_NodeFeature63 = EFM_NodeFeature63
        self.EFM_NodeFeature76 = EFM_NodeFeature76
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def EFM_NodeFeature63(self):
        return self.__EFM_NodeFeature63

    @EFM_NodeFeature63.setter
    def EFM_NodeFeature63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EFM_NodeFeature__EFM_NodeFeature63", None)
        self.__EFM_NodeFeature63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EFM_HostedBy62"):
                opp_val = getattr(old_value, "EFM_HostedBy62", None)
                if opp_val == self:
                    setattr(old_value, "EFM_HostedBy62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EFM_HostedBy62"):
                opp_val = getattr(value, "EFM_HostedBy62", None)
                setattr(value, "EFM_HostedBy62", self)

    @property
    def EFM_NodeFeature52(self):
        return self.__EFM_NodeFeature52

    @EFM_NodeFeature52.setter
    def EFM_NodeFeature52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EFM_NodeFeature__EFM_NodeFeature52", None)
        self.__EFM_NodeFeature52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EFM_FeatCardinality53"):
                opp_val = getattr(old_value, "EFM_FeatCardinality53", None)
                if opp_val == self:
                    setattr(old_value, "EFM_FeatCardinality53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EFM_FeatCardinality53"):
                opp_val = getattr(value, "EFM_FeatCardinality53", None)
                setattr(value, "EFM_FeatCardinality53", self)

    @property
    def EFM_NodeFeature76(self):
        return self.__EFM_NodeFeature76

    @EFM_NodeFeature76.setter
    def EFM_NodeFeature76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EFM_NodeFeature__EFM_NodeFeature76", None)
        self.__EFM_NodeFeature76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EFM_NotHostedBy75"):
                opp_val = getattr(old_value, "EFM_NotHostedBy75", None)
                if opp_val == self:
                    setattr(old_value, "EFM_NotHostedBy75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EFM_NotHostedBy75"):
                opp_val = getattr(value, "EFM_NotHostedBy75", None)
                setattr(value, "EFM_NotHostedBy75", self)

    @property
    def EFM_NodeFeature49(self):
        return self.__EFM_NodeFeature49

    @EFM_NodeFeature49.setter
    def EFM_NodeFeature49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EFM_NodeFeature__EFM_NodeFeature49", None)
        self.__EFM_NodeFeature49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "EFM_Attribute50"):
                    opp_val = getattr(item, "EFM_Attribute50", None)
                    
                    if opp_val == self:
                        setattr(item, "EFM_Attribute50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "EFM_Attribute50"):
                    opp_val = getattr(item, "EFM_Attribute50", None)
                    
                    setattr(item, "EFM_Attribute50", self)
                    

    @property
    def EFM_NodeFeature(self):
        return self.__EFM_NodeFeature

    @EFM_NodeFeature.setter
    def EFM_NodeFeature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EFM_NodeFeature__EFM_NodeFeature", None)
        self.__EFM_NodeFeature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EFM_Feature11"):
                opp_val = getattr(old_value, "EFM_Feature11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EFM_Feature11"):
                opp_val = getattr(value, "EFM_Feature11", None)
                if opp_val is None:
                    setattr(value, "EFM_Feature11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def EFM_NodeFeature55(self):
        return self.__EFM_NodeFeature55

    @EFM_NodeFeature55.setter
    def EFM_NodeFeature55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EFM_NodeFeature__EFM_NodeFeature55", None)
        self.__EFM_NodeFeature55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EFM_HostedBy"):
                opp_val = getattr(old_value, "EFM_HostedBy", None)
                if opp_val == self:
                    setattr(old_value, "EFM_HostedBy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EFM_HostedBy"):
                opp_val = getattr(value, "EFM_HostedBy", None)
                setattr(value, "EFM_HostedBy", self)

    @property
    def EFM_NodeFeature57(self):
        return self.__EFM_NodeFeature57

    @EFM_NodeFeature57.setter
    def EFM_NodeFeature57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_EFM_NodeFeature__EFM_NodeFeature57", None)
        self.__EFM_NodeFeature57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "EFM_NotHostedBy"):
                opp_val = getattr(old_value, "EFM_NotHostedBy", None)
                if opp_val == self:
                    setattr(old_value, "EFM_NotHostedBy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "EFM_NotHostedBy"):
                opp_val = getattr(value, "EFM_NotHostedBy", None)
                setattr(value, "EFM_NotHostedBy", self)

class EFM_FeatCardinality(Cardinality):

    pass