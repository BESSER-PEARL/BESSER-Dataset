from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class OptimizationSCFunct(Enum):
    maximize = "maximize"
    minimize = "minimize"
class CMConstraintType(Enum):
    not = "not"
    and = "and"
    or = "or"
    implies = "implies"
class SCType(Enum):
    selectionState = "selectionState"
    hardLimit = "hardLimit"
    optimization = "optimization"
    finiteDomain = "finiteDomain"
class DataType(Enum):
    String = "String"
    int = "int"
    double = "double"
    boolean = "boolean"
class CCType(Enum):
    selectionState = "selectionState"
    hardLimit = "hardLimit"
    optimization = "optimization"
class CCOptimizationOp(Enum):
    maximize = "maximize"
    minimize = "minimize"
class ConfigType(Enum):
    input = "input"
    output = "output"
class AggregationOp(Enum):
    add = "add"
    multiply = "multiply"
    min = "min"
    max = "max"
class CCSelectionStateType(Enum):
    mandatory = "mandatory"
    preferred = "preferred"
    forbidden = "forbidden"
class CTConstraintType(Enum):
    not = "not"
    and = "and"
    or = "or"
    implies = "implies"
class TreeConstraintType(Enum):
    And = "And"
    Alternative = "Alternative"
    Or = "Or"
class CCHardLimitOp(Enum):
    leq = "leq"
    lt = "lt"
    geq = "geq"
    gt = "gt"
    eq = "eq"


############################################
# Definition of Classes
############################################

class SolutionConstraint:

    pass
class coCoMM_OptimizationSC(SolutionConstraint):

    def __init__(self, funct: str, coCoMM_OptimizationSC: "coCoMM_AttributeType" = None):
        self.funct = funct
        self.coCoMM_OptimizationSC = coCoMM_OptimizationSC
        
    @property
    def funct(self) -> str:
        return self.__funct

    @funct.setter
    def funct(self, funct: str):
        self.__funct = funct

    @property
    def coCoMM_OptimizationSC(self):
        return self.__coCoMM_OptimizationSC

    @coCoMM_OptimizationSC.setter
    def coCoMM_OptimizationSC(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_OptimizationSC__coCoMM_OptimizationSC", None)
        self.__coCoMM_OptimizationSC = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_AttributeType74"):
                opp_val = getattr(old_value, "coCoMM_AttributeType74", None)
                if opp_val == self:
                    setattr(old_value, "coCoMM_AttributeType74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_AttributeType74"):
                opp_val = getattr(value, "coCoMM_AttributeType74", None)
                setattr(value, "coCoMM_AttributeType74", self)

class coCoMM_Config:

    def __init__(self, selected: bool, type: str, coCoMM_Config53: "coCoMM_Stakeholder" = None, coCoMM_Config56: set["coCoMM_Feature"] = None, coCoMM_Config: "coCoMM_Project" = None):
        self.selected = selected
        self.type = type
        self.coCoMM_Config53 = coCoMM_Config53
        self.coCoMM_Config56 = coCoMM_Config56 if coCoMM_Config56 is not None else set()
        self.coCoMM_Config = coCoMM_Config
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def selected(self) -> bool:
        return self.__selected

    @selected.setter
    def selected(self, selected: bool):
        self.__selected = selected

    @property
    def coCoMM_Config(self):
        return self.__coCoMM_Config

    @coCoMM_Config.setter
    def coCoMM_Config(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_Config__coCoMM_Config", None)
        self.__coCoMM_Config = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_Project51"):
                opp_val = getattr(old_value, "coCoMM_Project51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_Project51"):
                opp_val = getattr(value, "coCoMM_Project51", None)
                if opp_val is None:
                    setattr(value, "coCoMM_Project51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def coCoMM_Config53(self):
        return self.__coCoMM_Config53

    @coCoMM_Config53.setter
    def coCoMM_Config53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_Config__coCoMM_Config53", None)
        self.__coCoMM_Config53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_Stakeholder54"):
                opp_val = getattr(old_value, "coCoMM_Stakeholder54", None)
                if opp_val == self:
                    setattr(old_value, "coCoMM_Stakeholder54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_Stakeholder54"):
                opp_val = getattr(value, "coCoMM_Stakeholder54", None)
                setattr(value, "coCoMM_Stakeholder54", self)

    @property
    def coCoMM_Config56(self):
        return self.__coCoMM_Config56

    @coCoMM_Config56.setter
    def coCoMM_Config56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_Config__coCoMM_Config56", None)
        self.__coCoMM_Config56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "coCoMM_Feature57"):
                    opp_val = getattr(item, "coCoMM_Feature57", None)
                    
                    if opp_val == self:
                        setattr(item, "coCoMM_Feature57", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "coCoMM_Feature57"):
                    opp_val = getattr(item, "coCoMM_Feature57", None)
                    
                    setattr(item, "coCoMM_Feature57", self)
                    

class ConfigurationConstraint:

    pass
class coCoMM_OptimizationCC(ConfigurationConstraint):

    def __init__(self, funct: str, coCoMM_OptimizationCC: "coCoMM_AggregationFunction" = None):
        self.funct = funct
        self.coCoMM_OptimizationCC = coCoMM_OptimizationCC
        
    @property
    def funct(self) -> str:
        return self.__funct

    @funct.setter
    def funct(self, funct: str):
        self.__funct = funct

    @property
    def coCoMM_OptimizationCC(self):
        return self.__coCoMM_OptimizationCC

    @coCoMM_OptimizationCC.setter
    def coCoMM_OptimizationCC(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_OptimizationCC__coCoMM_OptimizationCC", None)
        self.__coCoMM_OptimizationCC = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_AggregationFunction43"):
                opp_val = getattr(old_value, "coCoMM_AggregationFunction43", None)
                if opp_val == self:
                    setattr(old_value, "coCoMM_AggregationFunction43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_AggregationFunction43"):
                opp_val = getattr(value, "coCoMM_AggregationFunction43", None)
                setattr(value, "coCoMM_AggregationFunction43", self)

class coCoMM_SelectionStateCC(ConfigurationConstraint):

    def __init__(self, state: str, coCoMM_SelectionStateCC: "coCoMM_FeatureModel" = None, coCoMM_SelectionStateCC37: "coCoMM_Feature" = None):
        self.state = state
        self.coCoMM_SelectionStateCC = coCoMM_SelectionStateCC
        self.coCoMM_SelectionStateCC37 = coCoMM_SelectionStateCC37
        
    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def coCoMM_SelectionStateCC(self):
        return self.__coCoMM_SelectionStateCC

    @coCoMM_SelectionStateCC.setter
    def coCoMM_SelectionStateCC(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_SelectionStateCC__coCoMM_SelectionStateCC", None)
        self.__coCoMM_SelectionStateCC = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_FeatureModel35"):
                opp_val = getattr(old_value, "coCoMM_FeatureModel35", None)
                if opp_val == self:
                    setattr(old_value, "coCoMM_FeatureModel35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_FeatureModel35"):
                opp_val = getattr(value, "coCoMM_FeatureModel35", None)
                setattr(value, "coCoMM_FeatureModel35", self)

    @property
    def coCoMM_SelectionStateCC37(self):
        return self.__coCoMM_SelectionStateCC37

    @coCoMM_SelectionStateCC37.setter
    def coCoMM_SelectionStateCC37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_SelectionStateCC__coCoMM_SelectionStateCC37", None)
        self.__coCoMM_SelectionStateCC37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_Feature38"):
                opp_val = getattr(old_value, "coCoMM_Feature38", None)
                if opp_val == self:
                    setattr(old_value, "coCoMM_Feature38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_Feature38"):
                opp_val = getattr(value, "coCoMM_Feature38", None)
                setattr(value, "coCoMM_Feature38", self)

class coCoMM_CMConstraintExpression:

    def __init__(self, op: str, coCoMM_CMConstraintExpression: "coCoMM_CrossModelConstraint" = None, coCoMM_CMConstraintExpression65: set["coCoMM_Feature"] = None, coCoMM_CMConstraintExpression69: "coCoMM_CMConstraintExpression" = None, coCoMM_CMConstraintExpression67: set["coCoMM_CMConstraintExpression"] = None):
        self.op = op
        self.coCoMM_CMConstraintExpression = coCoMM_CMConstraintExpression
        self.coCoMM_CMConstraintExpression65 = coCoMM_CMConstraintExpression65 if coCoMM_CMConstraintExpression65 is not None else set()
        self.coCoMM_CMConstraintExpression69 = coCoMM_CMConstraintExpression69
        self.coCoMM_CMConstraintExpression67 = coCoMM_CMConstraintExpression67 if coCoMM_CMConstraintExpression67 is not None else set()
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def coCoMM_CMConstraintExpression69(self):
        return self.__coCoMM_CMConstraintExpression69

    @coCoMM_CMConstraintExpression69.setter
    def coCoMM_CMConstraintExpression69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_CMConstraintExpression__coCoMM_CMConstraintExpression69", None)
        self.__coCoMM_CMConstraintExpression69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_CMConstraintExpression67"):
                opp_val = getattr(old_value, "coCoMM_CMConstraintExpression67", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_CMConstraintExpression67"):
                opp_val = getattr(value, "coCoMM_CMConstraintExpression67", None)
                if opp_val is None:
                    setattr(value, "coCoMM_CMConstraintExpression67", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def coCoMM_CMConstraintExpression(self):
        return self.__coCoMM_CMConstraintExpression

    @coCoMM_CMConstraintExpression.setter
    def coCoMM_CMConstraintExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_CMConstraintExpression__coCoMM_CMConstraintExpression", None)
        self.__coCoMM_CMConstraintExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_CrossModelConstraint33"):
                opp_val = getattr(old_value, "coCoMM_CrossModelConstraint33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_CrossModelConstraint33"):
                opp_val = getattr(value, "coCoMM_CrossModelConstraint33", None)
                if opp_val is None:
                    setattr(value, "coCoMM_CrossModelConstraint33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def coCoMM_CMConstraintExpression67(self):
        return self.__coCoMM_CMConstraintExpression67

    @coCoMM_CMConstraintExpression67.setter
    def coCoMM_CMConstraintExpression67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_CMConstraintExpression__coCoMM_CMConstraintExpression67", None)
        self.__coCoMM_CMConstraintExpression67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "coCoMM_CMConstraintExpression69"):
                    opp_val = getattr(item, "coCoMM_CMConstraintExpression69", None)
                    
                    if opp_val == self:
                        setattr(item, "coCoMM_CMConstraintExpression69", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "coCoMM_CMConstraintExpression69"):
                    opp_val = getattr(item, "coCoMM_CMConstraintExpression69", None)
                    
                    setattr(item, "coCoMM_CMConstraintExpression69", self)
                    

    @property
    def coCoMM_CMConstraintExpression65(self):
        return self.__coCoMM_CMConstraintExpression65

    @coCoMM_CMConstraintExpression65.setter
    def coCoMM_CMConstraintExpression65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_CMConstraintExpression__coCoMM_CMConstraintExpression65", None)
        self.__coCoMM_CMConstraintExpression65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "coCoMM_Feature66"):
                    opp_val = getattr(item, "coCoMM_Feature66", None)
                    
                    if opp_val == self:
                        setattr(item, "coCoMM_Feature66", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "coCoMM_Feature66"):
                    opp_val = getattr(item, "coCoMM_Feature66", None)
                    
                    setattr(item, "coCoMM_Feature66", self)
                    

class coCoMM_AggregationFunction:

    def __init__(self, operation: str, coCoMM_AggregationFunction: "coCoMM_HardLimitCC" = None, coCoMM_AggregationFunction43: "coCoMM_OptimizationCC" = None, coCoMM_AggregationFunction71: "coCoMM_AttributeType" = None):
        self.operation = operation
        self.coCoMM_AggregationFunction = coCoMM_AggregationFunction
        self.coCoMM_AggregationFunction43 = coCoMM_AggregationFunction43
        self.coCoMM_AggregationFunction71 = coCoMM_AggregationFunction71
        
    @property
    def operation(self) -> str:
        return self.__operation

    @operation.setter
    def operation(self, operation: str):
        self.__operation = operation

    @property
    def coCoMM_AggregationFunction43(self):
        return self.__coCoMM_AggregationFunction43

    @coCoMM_AggregationFunction43.setter
    def coCoMM_AggregationFunction43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_AggregationFunction__coCoMM_AggregationFunction43", None)
        self.__coCoMM_AggregationFunction43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_OptimizationCC"):
                opp_val = getattr(old_value, "coCoMM_OptimizationCC", None)
                if opp_val == self:
                    setattr(old_value, "coCoMM_OptimizationCC", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_OptimizationCC"):
                opp_val = getattr(value, "coCoMM_OptimizationCC", None)
                setattr(value, "coCoMM_OptimizationCC", self)

    @property
    def coCoMM_AggregationFunction71(self):
        return self.__coCoMM_AggregationFunction71

    @coCoMM_AggregationFunction71.setter
    def coCoMM_AggregationFunction71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_AggregationFunction__coCoMM_AggregationFunction71", None)
        self.__coCoMM_AggregationFunction71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_AttributeType72"):
                opp_val = getattr(old_value, "coCoMM_AttributeType72", None)
                if opp_val == self:
                    setattr(old_value, "coCoMM_AttributeType72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_AttributeType72"):
                opp_val = getattr(value, "coCoMM_AttributeType72", None)
                setattr(value, "coCoMM_AttributeType72", self)

    @property
    def coCoMM_AggregationFunction(self):
        return self.__coCoMM_AggregationFunction

    @coCoMM_AggregationFunction.setter
    def coCoMM_AggregationFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_AggregationFunction__coCoMM_AggregationFunction", None)
        self.__coCoMM_AggregationFunction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_HardLimitCC41"):
                opp_val = getattr(old_value, "coCoMM_HardLimitCC41", None)
                if opp_val == self:
                    setattr(old_value, "coCoMM_HardLimitCC41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_HardLimitCC41"):
                opp_val = getattr(value, "coCoMM_HardLimitCC41", None)
                setattr(value, "coCoMM_HardLimitCC41", self)

class coCoMM_HardLimitCCExpression:

    def __init__(self, op: str, value: str, coCoMM_HardLimitCCExpression: "coCoMM_HardLimitCC" = None):
        self.op = op
        self.value = value
        self.coCoMM_HardLimitCCExpression = coCoMM_HardLimitCCExpression
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def coCoMM_HardLimitCCExpression(self):
        return self.__coCoMM_HardLimitCCExpression

    @coCoMM_HardLimitCCExpression.setter
    def coCoMM_HardLimitCCExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_HardLimitCCExpression__coCoMM_HardLimitCCExpression", None)
        self.__coCoMM_HardLimitCCExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_HardLimitCC"):
                opp_val = getattr(old_value, "coCoMM_HardLimitCC", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_HardLimitCC"):
                opp_val = getattr(value, "coCoMM_HardLimitCC", None)
                if opp_val is None:
                    setattr(value, "coCoMM_HardLimitCC", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class coCoMM_HardLimitCC(ConfigurationConstraint):

    pass
class coCoMM_CTConstraintExpression:

    def __init__(self, op: str, coCoMM_CTConstraintExpression: "coCoMM_CrossTreeConstraint" = None, coCoMM_CTConstraintExpression59: set["coCoMM_Feature"] = None, coCoMM_CTConstraintExpression63: "coCoMM_CTConstraintExpression" = None, coCoMM_CTConstraintExpression61: set["coCoMM_CTConstraintExpression"] = None):
        self.op = op
        self.coCoMM_CTConstraintExpression = coCoMM_CTConstraintExpression
        self.coCoMM_CTConstraintExpression59 = coCoMM_CTConstraintExpression59 if coCoMM_CTConstraintExpression59 is not None else set()
        self.coCoMM_CTConstraintExpression63 = coCoMM_CTConstraintExpression63
        self.coCoMM_CTConstraintExpression61 = coCoMM_CTConstraintExpression61 if coCoMM_CTConstraintExpression61 is not None else set()
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def coCoMM_CTConstraintExpression63(self):
        return self.__coCoMM_CTConstraintExpression63

    @coCoMM_CTConstraintExpression63.setter
    def coCoMM_CTConstraintExpression63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_CTConstraintExpression__coCoMM_CTConstraintExpression63", None)
        self.__coCoMM_CTConstraintExpression63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_CTConstraintExpression61"):
                opp_val = getattr(old_value, "coCoMM_CTConstraintExpression61", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_CTConstraintExpression61"):
                opp_val = getattr(value, "coCoMM_CTConstraintExpression61", None)
                if opp_val is None:
                    setattr(value, "coCoMM_CTConstraintExpression61", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def coCoMM_CTConstraintExpression59(self):
        return self.__coCoMM_CTConstraintExpression59

    @coCoMM_CTConstraintExpression59.setter
    def coCoMM_CTConstraintExpression59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_CTConstraintExpression__coCoMM_CTConstraintExpression59", None)
        self.__coCoMM_CTConstraintExpression59 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "coCoMM_Feature60"):
                    opp_val = getattr(item, "coCoMM_Feature60", None)
                    
                    if opp_val == self:
                        setattr(item, "coCoMM_Feature60", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "coCoMM_Feature60"):
                    opp_val = getattr(item, "coCoMM_Feature60", None)
                    
                    setattr(item, "coCoMM_Feature60", self)
                    

    @property
    def coCoMM_CTConstraintExpression(self):
        return self.__coCoMM_CTConstraintExpression

    @coCoMM_CTConstraintExpression.setter
    def coCoMM_CTConstraintExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_CTConstraintExpression__coCoMM_CTConstraintExpression", None)
        self.__coCoMM_CTConstraintExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_CrossTreeConstraint16"):
                opp_val = getattr(old_value, "coCoMM_CrossTreeConstraint16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_CrossTreeConstraint16"):
                opp_val = getattr(value, "coCoMM_CrossTreeConstraint16", None)
                if opp_val is None:
                    setattr(value, "coCoMM_CrossTreeConstraint16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def coCoMM_CTConstraintExpression61(self):
        return self.__coCoMM_CTConstraintExpression61

    @coCoMM_CTConstraintExpression61.setter
    def coCoMM_CTConstraintExpression61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_CTConstraintExpression__coCoMM_CTConstraintExpression61", None)
        self.__coCoMM_CTConstraintExpression61 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "coCoMM_CTConstraintExpression63"):
                    opp_val = getattr(item, "coCoMM_CTConstraintExpression63", None)
                    
                    if opp_val == self:
                        setattr(item, "coCoMM_CTConstraintExpression63", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "coCoMM_CTConstraintExpression63"):
                    opp_val = getattr(item, "coCoMM_CTConstraintExpression63", None)
                    
                    setattr(item, "coCoMM_CTConstraintExpression63", self)
                    

class coCoMM_Stakeholder:

    def __init__(self, name: str, job: str, coCoMM_Stakeholder: "coCoMM_CoCo" = None, coCoMM_Stakeholder54: "coCoMM_Config" = None):
        self.name = name
        self.job = job
        self.coCoMM_Stakeholder = coCoMM_Stakeholder
        self.coCoMM_Stakeholder54 = coCoMM_Stakeholder54
        
    @property
    def job(self) -> str:
        return self.__job

    @job.setter
    def job(self, job: str):
        self.__job = job

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def coCoMM_Stakeholder(self):
        return self.__coCoMM_Stakeholder

    @coCoMM_Stakeholder.setter
    def coCoMM_Stakeholder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_Stakeholder__coCoMM_Stakeholder", None)
        self.__coCoMM_Stakeholder = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_CoCo31"):
                opp_val = getattr(old_value, "coCoMM_CoCo31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_CoCo31"):
                opp_val = getattr(value, "coCoMM_CoCo31", None)
                if opp_val is None:
                    setattr(value, "coCoMM_CoCo31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def coCoMM_Stakeholder54(self):
        return self.__coCoMM_Stakeholder54

    @coCoMM_Stakeholder54.setter
    def coCoMM_Stakeholder54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_Stakeholder__coCoMM_Stakeholder54", None)
        self.__coCoMM_Stakeholder54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_Config53"):
                opp_val = getattr(old_value, "coCoMM_Config53", None)
                if opp_val == self:
                    setattr(old_value, "coCoMM_Config53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_Config53"):
                opp_val = getattr(value, "coCoMM_Config53", None)
                setattr(value, "coCoMM_Config53", self)

class coCoMM_Project:

    def __init__(self, name: str, date: date, target: bool, coCoMM_Project: "coCoMM_CoCo" = None, coCoMM_Project45: set["coCoMM_ConfigurationConstraint"] = None, coCoMM_Project48: set["coCoMM_SolutionConstraint"] = None, coCoMM_Project51: set["coCoMM_Config"] = None):
        self.name = name
        self.date = date
        self.target = target
        self.coCoMM_Project = coCoMM_Project
        self.coCoMM_Project45 = coCoMM_Project45 if coCoMM_Project45 is not None else set()
        self.coCoMM_Project48 = coCoMM_Project48 if coCoMM_Project48 is not None else set()
        self.coCoMM_Project51 = coCoMM_Project51 if coCoMM_Project51 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def target(self) -> bool:
        return self.__target

    @target.setter
    def target(self, target: bool):
        self.__target = target

    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def coCoMM_Project48(self):
        return self.__coCoMM_Project48

    @coCoMM_Project48.setter
    def coCoMM_Project48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_Project__coCoMM_Project48", None)
        self.__coCoMM_Project48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "coCoMM_SolutionConstraint49"):
                    opp_val = getattr(item, "coCoMM_SolutionConstraint49", None)
                    
                    if opp_val == self:
                        setattr(item, "coCoMM_SolutionConstraint49", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "coCoMM_SolutionConstraint49"):
                    opp_val = getattr(item, "coCoMM_SolutionConstraint49", None)
                    
                    setattr(item, "coCoMM_SolutionConstraint49", self)
                    

    @property
    def coCoMM_Project51(self):
        return self.__coCoMM_Project51

    @coCoMM_Project51.setter
    def coCoMM_Project51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_Project__coCoMM_Project51", None)
        self.__coCoMM_Project51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "coCoMM_Config"):
                    opp_val = getattr(item, "coCoMM_Config", None)
                    
                    if opp_val == self:
                        setattr(item, "coCoMM_Config", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "coCoMM_Config"):
                    opp_val = getattr(item, "coCoMM_Config", None)
                    
                    setattr(item, "coCoMM_Config", self)
                    

    @property
    def coCoMM_Project(self):
        return self.__coCoMM_Project

    @coCoMM_Project.setter
    def coCoMM_Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_Project__coCoMM_Project", None)
        self.__coCoMM_Project = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_CoCo29"):
                opp_val = getattr(old_value, "coCoMM_CoCo29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_CoCo29"):
                opp_val = getattr(value, "coCoMM_CoCo29", None)
                if opp_val is None:
                    setattr(value, "coCoMM_CoCo29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def coCoMM_Project45(self):
        return self.__coCoMM_Project45

    @coCoMM_Project45.setter
    def coCoMM_Project45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_Project__coCoMM_Project45", None)
        self.__coCoMM_Project45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "coCoMM_ConfigurationConstraint46"):
                    opp_val = getattr(item, "coCoMM_ConfigurationConstraint46", None)
                    
                    if opp_val == self:
                        setattr(item, "coCoMM_ConfigurationConstraint46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "coCoMM_ConfigurationConstraint46"):
                    opp_val = getattr(item, "coCoMM_ConfigurationConstraint46", None)
                    
                    setattr(item, "coCoMM_ConfigurationConstraint46", self)
                    

class coCoMM_ConfigurationConstraint:

    def __init__(self, type: str, id: str, name: str, coCoMM_ConfigurationConstraint: "coCoMM_CoCo" = None, coCoMM_ConfigurationConstraint46: "coCoMM_Project" = None):
        self.type = type
        self.id = id
        self.name = name
        self.coCoMM_ConfigurationConstraint = coCoMM_ConfigurationConstraint
        self.coCoMM_ConfigurationConstraint46 = coCoMM_ConfigurationConstraint46
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def coCoMM_ConfigurationConstraint46(self):
        return self.__coCoMM_ConfigurationConstraint46

    @coCoMM_ConfigurationConstraint46.setter
    def coCoMM_ConfigurationConstraint46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_ConfigurationConstraint__coCoMM_ConfigurationConstraint46", None)
        self.__coCoMM_ConfigurationConstraint46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_Project45"):
                opp_val = getattr(old_value, "coCoMM_Project45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_Project45"):
                opp_val = getattr(value, "coCoMM_Project45", None)
                if opp_val is None:
                    setattr(value, "coCoMM_Project45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def coCoMM_ConfigurationConstraint(self):
        return self.__coCoMM_ConfigurationConstraint

    @coCoMM_ConfigurationConstraint.setter
    def coCoMM_ConfigurationConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_ConfigurationConstraint__coCoMM_ConfigurationConstraint", None)
        self.__coCoMM_ConfigurationConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_CoCo24"):
                opp_val = getattr(old_value, "coCoMM_CoCo24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_CoCo24"):
                opp_val = getattr(value, "coCoMM_CoCo24", None)
                if opp_val is None:
                    setattr(value, "coCoMM_CoCo24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class coCoMM_SolutionConstraint:

    def __init__(self, type: str, coCoMM_SolutionConstraint: "coCoMM_CoCo" = None, coCoMM_SolutionConstraint49: "coCoMM_Project" = None):
        self.type = type
        self.coCoMM_SolutionConstraint = coCoMM_SolutionConstraint
        self.coCoMM_SolutionConstraint49 = coCoMM_SolutionConstraint49
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def coCoMM_SolutionConstraint(self):
        return self.__coCoMM_SolutionConstraint

    @coCoMM_SolutionConstraint.setter
    def coCoMM_SolutionConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_SolutionConstraint__coCoMM_SolutionConstraint", None)
        self.__coCoMM_SolutionConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_CoCo22"):
                opp_val = getattr(old_value, "coCoMM_CoCo22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_CoCo22"):
                opp_val = getattr(value, "coCoMM_CoCo22", None)
                if opp_val is None:
                    setattr(value, "coCoMM_CoCo22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def coCoMM_SolutionConstraint49(self):
        return self.__coCoMM_SolutionConstraint49

    @coCoMM_SolutionConstraint49.setter
    def coCoMM_SolutionConstraint49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_SolutionConstraint__coCoMM_SolutionConstraint49", None)
        self.__coCoMM_SolutionConstraint49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_Project48"):
                opp_val = getattr(old_value, "coCoMM_Project48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_Project48"):
                opp_val = getattr(value, "coCoMM_Project48", None)
                if opp_val is None:
                    setattr(value, "coCoMM_Project48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class coCoMM_CrossModelConstraint:

    pass
class coCoMM_CoCo:

    def __init__(self, id: str, name: str, configScenario: str, coCoMM_CoCo: set["coCoMM_FeatureModel"] = None, coCoMM_CoCo20: set["coCoMM_CrossModelConstraint"] = None, coCoMM_CoCo22: set["coCoMM_SolutionConstraint"] = None, coCoMM_CoCo24: set["coCoMM_ConfigurationConstraint"] = None, coCoMM_CoCo26: set["coCoMM_AttributeType"] = None, coCoMM_CoCo29: set["coCoMM_Project"] = None, coCoMM_CoCo31: set["coCoMM_Stakeholder"] = None):
        self.id = id
        self.name = name
        self.configScenario = configScenario
        self.coCoMM_CoCo = coCoMM_CoCo if coCoMM_CoCo is not None else set()
        self.coCoMM_CoCo20 = coCoMM_CoCo20 if coCoMM_CoCo20 is not None else set()
        self.coCoMM_CoCo22 = coCoMM_CoCo22 if coCoMM_CoCo22 is not None else set()
        self.coCoMM_CoCo24 = coCoMM_CoCo24 if coCoMM_CoCo24 is not None else set()
        self.coCoMM_CoCo26 = coCoMM_CoCo26 if coCoMM_CoCo26 is not None else set()
        self.coCoMM_CoCo29 = coCoMM_CoCo29 if coCoMM_CoCo29 is not None else set()
        self.coCoMM_CoCo31 = coCoMM_CoCo31 if coCoMM_CoCo31 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def configScenario(self) -> str:
        return self.__configScenario

    @configScenario.setter
    def configScenario(self, configScenario: str):
        self.__configScenario = configScenario

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def coCoMM_CoCo26(self):
        return self.__coCoMM_CoCo26

    @coCoMM_CoCo26.setter
    def coCoMM_CoCo26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_CoCo__coCoMM_CoCo26", None)
        self.__coCoMM_CoCo26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "coCoMM_AttributeType27"):
                    opp_val = getattr(item, "coCoMM_AttributeType27", None)
                    
                    if opp_val == self:
                        setattr(item, "coCoMM_AttributeType27", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "coCoMM_AttributeType27"):
                    opp_val = getattr(item, "coCoMM_AttributeType27", None)
                    
                    setattr(item, "coCoMM_AttributeType27", self)
                    

    @property
    def coCoMM_CoCo22(self):
        return self.__coCoMM_CoCo22

    @coCoMM_CoCo22.setter
    def coCoMM_CoCo22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_CoCo__coCoMM_CoCo22", None)
        self.__coCoMM_CoCo22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "coCoMM_SolutionConstraint"):
                    opp_val = getattr(item, "coCoMM_SolutionConstraint", None)
                    
                    if opp_val == self:
                        setattr(item, "coCoMM_SolutionConstraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "coCoMM_SolutionConstraint"):
                    opp_val = getattr(item, "coCoMM_SolutionConstraint", None)
                    
                    setattr(item, "coCoMM_SolutionConstraint", self)
                    

    @property
    def coCoMM_CoCo20(self):
        return self.__coCoMM_CoCo20

    @coCoMM_CoCo20.setter
    def coCoMM_CoCo20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_CoCo__coCoMM_CoCo20", None)
        self.__coCoMM_CoCo20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "coCoMM_CrossModelConstraint"):
                    opp_val = getattr(item, "coCoMM_CrossModelConstraint", None)
                    
                    if opp_val == self:
                        setattr(item, "coCoMM_CrossModelConstraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "coCoMM_CrossModelConstraint"):
                    opp_val = getattr(item, "coCoMM_CrossModelConstraint", None)
                    
                    setattr(item, "coCoMM_CrossModelConstraint", self)
                    

    @property
    def coCoMM_CoCo(self):
        return self.__coCoMM_CoCo

    @coCoMM_CoCo.setter
    def coCoMM_CoCo(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_CoCo__coCoMM_CoCo", None)
        self.__coCoMM_CoCo = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "coCoMM_FeatureModel18"):
                    opp_val = getattr(item, "coCoMM_FeatureModel18", None)
                    
                    if opp_val == self:
                        setattr(item, "coCoMM_FeatureModel18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "coCoMM_FeatureModel18"):
                    opp_val = getattr(item, "coCoMM_FeatureModel18", None)
                    
                    setattr(item, "coCoMM_FeatureModel18", self)
                    

    @property
    def coCoMM_CoCo31(self):
        return self.__coCoMM_CoCo31

    @coCoMM_CoCo31.setter
    def coCoMM_CoCo31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_CoCo__coCoMM_CoCo31", None)
        self.__coCoMM_CoCo31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "coCoMM_Stakeholder"):
                    opp_val = getattr(item, "coCoMM_Stakeholder", None)
                    
                    if opp_val == self:
                        setattr(item, "coCoMM_Stakeholder", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "coCoMM_Stakeholder"):
                    opp_val = getattr(item, "coCoMM_Stakeholder", None)
                    
                    setattr(item, "coCoMM_Stakeholder", self)
                    

    @property
    def coCoMM_CoCo24(self):
        return self.__coCoMM_CoCo24

    @coCoMM_CoCo24.setter
    def coCoMM_CoCo24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_CoCo__coCoMM_CoCo24", None)
        self.__coCoMM_CoCo24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "coCoMM_ConfigurationConstraint"):
                    opp_val = getattr(item, "coCoMM_ConfigurationConstraint", None)
                    
                    if opp_val == self:
                        setattr(item, "coCoMM_ConfigurationConstraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "coCoMM_ConfigurationConstraint"):
                    opp_val = getattr(item, "coCoMM_ConfigurationConstraint", None)
                    
                    setattr(item, "coCoMM_ConfigurationConstraint", self)
                    

    @property
    def coCoMM_CoCo29(self):
        return self.__coCoMM_CoCo29

    @coCoMM_CoCo29.setter
    def coCoMM_CoCo29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_CoCo__coCoMM_CoCo29", None)
        self.__coCoMM_CoCo29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "coCoMM_Project"):
                    opp_val = getattr(item, "coCoMM_Project", None)
                    
                    if opp_val == self:
                        setattr(item, "coCoMM_Project", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "coCoMM_Project"):
                    opp_val = getattr(item, "coCoMM_Project", None)
                    
                    setattr(item, "coCoMM_Project", self)
                    

class coCoMM_TreeConstraint:

    def __init__(self, type: str, coCoMM_TreeConstraint11: set["coCoMM_Feature"] = None, coCoMM_TreeConstraint: "coCoMM_Feature" = None):
        self.type = type
        self.coCoMM_TreeConstraint11 = coCoMM_TreeConstraint11 if coCoMM_TreeConstraint11 is not None else set()
        self.coCoMM_TreeConstraint = coCoMM_TreeConstraint
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def coCoMM_TreeConstraint(self):
        return self.__coCoMM_TreeConstraint

    @coCoMM_TreeConstraint.setter
    def coCoMM_TreeConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_TreeConstraint__coCoMM_TreeConstraint", None)
        self.__coCoMM_TreeConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_Feature4"):
                opp_val = getattr(old_value, "coCoMM_Feature4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_Feature4"):
                opp_val = getattr(value, "coCoMM_Feature4", None)
                if opp_val is None:
                    setattr(value, "coCoMM_Feature4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def coCoMM_TreeConstraint11(self):
        return self.__coCoMM_TreeConstraint11

    @coCoMM_TreeConstraint11.setter
    def coCoMM_TreeConstraint11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_TreeConstraint__coCoMM_TreeConstraint11", None)
        self.__coCoMM_TreeConstraint11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "coCoMM_Feature12"):
                    opp_val = getattr(item, "coCoMM_Feature12", None)
                    
                    if opp_val == self:
                        setattr(item, "coCoMM_Feature12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "coCoMM_Feature12"):
                    opp_val = getattr(item, "coCoMM_Feature12", None)
                    
                    setattr(item, "coCoMM_Feature12", self)
                    

class coCoMM_CrossTreeConstraint:

    pass
class coCoMM_Feature:

    def __init__(self, mandatory: bool, id: str, name: str, abstract: bool, coCoMM_Feature6: "coCoMM_FeatureModel" = None, coCoMM_Feature9: set["coCoMM_FeatureAttribute"] = None, coCoMM_Feature12: "coCoMM_TreeConstraint" = None, coCoMM_Feature: "coCoMM_FeatureModel" = None, coCoMM_Feature4: set["coCoMM_TreeConstraint"] = None, coCoMM_Feature38: "coCoMM_SelectionStateCC" = None, coCoMM_Feature57: "coCoMM_Config" = None, coCoMM_Feature60: "coCoMM_CTConstraintExpression" = None, coCoMM_Feature66: "coCoMM_CMConstraintExpression" = None):
        self.mandatory = mandatory
        self.id = id
        self.name = name
        self.abstract = abstract
        self.coCoMM_Feature6 = coCoMM_Feature6
        self.coCoMM_Feature9 = coCoMM_Feature9 if coCoMM_Feature9 is not None else set()
        self.coCoMM_Feature12 = coCoMM_Feature12
        self.coCoMM_Feature = coCoMM_Feature
        self.coCoMM_Feature4 = coCoMM_Feature4 if coCoMM_Feature4 is not None else set()
        self.coCoMM_Feature38 = coCoMM_Feature38
        self.coCoMM_Feature57 = coCoMM_Feature57
        self.coCoMM_Feature60 = coCoMM_Feature60
        self.coCoMM_Feature66 = coCoMM_Feature66
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def mandatory(self) -> bool:
        return self.__mandatory

    @mandatory.setter
    def mandatory(self, mandatory: bool):
        self.__mandatory = mandatory

    @property
    def coCoMM_Feature6(self):
        return self.__coCoMM_Feature6

    @coCoMM_Feature6.setter
    def coCoMM_Feature6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_Feature__coCoMM_Feature6", None)
        self.__coCoMM_Feature6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_FeatureModel7"):
                opp_val = getattr(old_value, "coCoMM_FeatureModel7", None)
                if opp_val == self:
                    setattr(old_value, "coCoMM_FeatureModel7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_FeatureModel7"):
                opp_val = getattr(value, "coCoMM_FeatureModel7", None)
                setattr(value, "coCoMM_FeatureModel7", self)

    @property
    def coCoMM_Feature4(self):
        return self.__coCoMM_Feature4

    @coCoMM_Feature4.setter
    def coCoMM_Feature4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_Feature__coCoMM_Feature4", None)
        self.__coCoMM_Feature4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "coCoMM_TreeConstraint"):
                    opp_val = getattr(item, "coCoMM_TreeConstraint", None)
                    
                    if opp_val == self:
                        setattr(item, "coCoMM_TreeConstraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "coCoMM_TreeConstraint"):
                    opp_val = getattr(item, "coCoMM_TreeConstraint", None)
                    
                    setattr(item, "coCoMM_TreeConstraint", self)
                    

    @property
    def coCoMM_Feature57(self):
        return self.__coCoMM_Feature57

    @coCoMM_Feature57.setter
    def coCoMM_Feature57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_Feature__coCoMM_Feature57", None)
        self.__coCoMM_Feature57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_Config56"):
                opp_val = getattr(old_value, "coCoMM_Config56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_Config56"):
                opp_val = getattr(value, "coCoMM_Config56", None)
                if opp_val is None:
                    setattr(value, "coCoMM_Config56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def coCoMM_Feature66(self):
        return self.__coCoMM_Feature66

    @coCoMM_Feature66.setter
    def coCoMM_Feature66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_Feature__coCoMM_Feature66", None)
        self.__coCoMM_Feature66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_CMConstraintExpression65"):
                opp_val = getattr(old_value, "coCoMM_CMConstraintExpression65", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_CMConstraintExpression65"):
                opp_val = getattr(value, "coCoMM_CMConstraintExpression65", None)
                if opp_val is None:
                    setattr(value, "coCoMM_CMConstraintExpression65", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def coCoMM_Feature38(self):
        return self.__coCoMM_Feature38

    @coCoMM_Feature38.setter
    def coCoMM_Feature38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_Feature__coCoMM_Feature38", None)
        self.__coCoMM_Feature38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_SelectionStateCC37"):
                opp_val = getattr(old_value, "coCoMM_SelectionStateCC37", None)
                if opp_val == self:
                    setattr(old_value, "coCoMM_SelectionStateCC37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_SelectionStateCC37"):
                opp_val = getattr(value, "coCoMM_SelectionStateCC37", None)
                setattr(value, "coCoMM_SelectionStateCC37", self)

    @property
    def coCoMM_Feature(self):
        return self.__coCoMM_Feature

    @coCoMM_Feature.setter
    def coCoMM_Feature(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_Feature__coCoMM_Feature", None)
        self.__coCoMM_Feature = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_FeatureModel"):
                opp_val = getattr(old_value, "coCoMM_FeatureModel", None)
                if opp_val == self:
                    setattr(old_value, "coCoMM_FeatureModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_FeatureModel"):
                opp_val = getattr(value, "coCoMM_FeatureModel", None)
                setattr(value, "coCoMM_FeatureModel", self)

    @property
    def coCoMM_Feature9(self):
        return self.__coCoMM_Feature9

    @coCoMM_Feature9.setter
    def coCoMM_Feature9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_Feature__coCoMM_Feature9", None)
        self.__coCoMM_Feature9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "coCoMM_FeatureAttribute"):
                    opp_val = getattr(item, "coCoMM_FeatureAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "coCoMM_FeatureAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "coCoMM_FeatureAttribute"):
                    opp_val = getattr(item, "coCoMM_FeatureAttribute", None)
                    
                    setattr(item, "coCoMM_FeatureAttribute", self)
                    

    @property
    def coCoMM_Feature12(self):
        return self.__coCoMM_Feature12

    @coCoMM_Feature12.setter
    def coCoMM_Feature12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_Feature__coCoMM_Feature12", None)
        self.__coCoMM_Feature12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_TreeConstraint11"):
                opp_val = getattr(old_value, "coCoMM_TreeConstraint11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_TreeConstraint11"):
                opp_val = getattr(value, "coCoMM_TreeConstraint11", None)
                if opp_val is None:
                    setattr(value, "coCoMM_TreeConstraint11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def coCoMM_Feature60(self):
        return self.__coCoMM_Feature60

    @coCoMM_Feature60.setter
    def coCoMM_Feature60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_Feature__coCoMM_Feature60", None)
        self.__coCoMM_Feature60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_CTConstraintExpression59"):
                opp_val = getattr(old_value, "coCoMM_CTConstraintExpression59", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_CTConstraintExpression59"):
                opp_val = getattr(value, "coCoMM_CTConstraintExpression59", None)
                if opp_val is None:
                    setattr(value, "coCoMM_CTConstraintExpression59", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class coCoMM_AttributeType:

    def __init__(self, id: str, name: str, dataType: str, coCoMM_AttributeType27: "coCoMM_CoCo" = None, coCoMM_AttributeType: "coCoMM_FeatureAttribute" = None, coCoMM_AttributeType72: "coCoMM_AggregationFunction" = None, coCoMM_AttributeType74: "coCoMM_OptimizationSC" = None):
        self.id = id
        self.name = name
        self.dataType = dataType
        self.coCoMM_AttributeType27 = coCoMM_AttributeType27
        self.coCoMM_AttributeType = coCoMM_AttributeType
        self.coCoMM_AttributeType72 = coCoMM_AttributeType72
        self.coCoMM_AttributeType74 = coCoMM_AttributeType74
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def dataType(self) -> str:
        return self.__dataType

    @dataType.setter
    def dataType(self, dataType: str):
        self.__dataType = dataType

    @property
    def coCoMM_AttributeType74(self):
        return self.__coCoMM_AttributeType74

    @coCoMM_AttributeType74.setter
    def coCoMM_AttributeType74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_AttributeType__coCoMM_AttributeType74", None)
        self.__coCoMM_AttributeType74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_OptimizationSC"):
                opp_val = getattr(old_value, "coCoMM_OptimizationSC", None)
                if opp_val == self:
                    setattr(old_value, "coCoMM_OptimizationSC", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_OptimizationSC"):
                opp_val = getattr(value, "coCoMM_OptimizationSC", None)
                setattr(value, "coCoMM_OptimizationSC", self)

    @property
    def coCoMM_AttributeType72(self):
        return self.__coCoMM_AttributeType72

    @coCoMM_AttributeType72.setter
    def coCoMM_AttributeType72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_AttributeType__coCoMM_AttributeType72", None)
        self.__coCoMM_AttributeType72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_AggregationFunction71"):
                opp_val = getattr(old_value, "coCoMM_AggregationFunction71", None)
                if opp_val == self:
                    setattr(old_value, "coCoMM_AggregationFunction71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_AggregationFunction71"):
                opp_val = getattr(value, "coCoMM_AggregationFunction71", None)
                setattr(value, "coCoMM_AggregationFunction71", self)

    @property
    def coCoMM_AttributeType(self):
        return self.__coCoMM_AttributeType

    @coCoMM_AttributeType.setter
    def coCoMM_AttributeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_AttributeType__coCoMM_AttributeType", None)
        self.__coCoMM_AttributeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_FeatureAttribute14"):
                opp_val = getattr(old_value, "coCoMM_FeatureAttribute14", None)
                if opp_val == self:
                    setattr(old_value, "coCoMM_FeatureAttribute14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_FeatureAttribute14"):
                opp_val = getattr(value, "coCoMM_FeatureAttribute14", None)
                setattr(value, "coCoMM_FeatureAttribute14", self)

    @property
    def coCoMM_AttributeType27(self):
        return self.__coCoMM_AttributeType27

    @coCoMM_AttributeType27.setter
    def coCoMM_AttributeType27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_AttributeType__coCoMM_AttributeType27", None)
        self.__coCoMM_AttributeType27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_CoCo26"):
                opp_val = getattr(old_value, "coCoMM_CoCo26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_CoCo26"):
                opp_val = getattr(value, "coCoMM_CoCo26", None)
                if opp_val is None:
                    setattr(value, "coCoMM_CoCo26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class coCoMM_FeatureAttribute:

    def __init__(self, defaultValue: str, minValue: str, maxValue: str, coCoMM_FeatureAttribute: "coCoMM_Feature" = None, coCoMM_FeatureAttribute14: "coCoMM_AttributeType" = None):
        self.defaultValue = defaultValue
        self.minValue = minValue
        self.maxValue = maxValue
        self.coCoMM_FeatureAttribute = coCoMM_FeatureAttribute
        self.coCoMM_FeatureAttribute14 = coCoMM_FeatureAttribute14
        
    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def maxValue(self) -> str:
        return self.__maxValue

    @maxValue.setter
    def maxValue(self, maxValue: str):
        self.__maxValue = maxValue

    @property
    def minValue(self) -> str:
        return self.__minValue

    @minValue.setter
    def minValue(self, minValue: str):
        self.__minValue = minValue

    @property
    def coCoMM_FeatureAttribute14(self):
        return self.__coCoMM_FeatureAttribute14

    @coCoMM_FeatureAttribute14.setter
    def coCoMM_FeatureAttribute14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_FeatureAttribute__coCoMM_FeatureAttribute14", None)
        self.__coCoMM_FeatureAttribute14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_AttributeType"):
                opp_val = getattr(old_value, "coCoMM_AttributeType", None)
                if opp_val == self:
                    setattr(old_value, "coCoMM_AttributeType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_AttributeType"):
                opp_val = getattr(value, "coCoMM_AttributeType", None)
                setattr(value, "coCoMM_AttributeType", self)

    @property
    def coCoMM_FeatureAttribute(self):
        return self.__coCoMM_FeatureAttribute

    @coCoMM_FeatureAttribute.setter
    def coCoMM_FeatureAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_FeatureAttribute__coCoMM_FeatureAttribute", None)
        self.__coCoMM_FeatureAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_Feature9"):
                opp_val = getattr(old_value, "coCoMM_Feature9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_Feature9"):
                opp_val = getattr(value, "coCoMM_Feature9", None)
                if opp_val is None:
                    setattr(value, "coCoMM_Feature9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class coCoMM_FeatureModel:

    def __init__(self, name: str, isDomain: bool, id: str, coCoMM_FeatureModel7: "coCoMM_Feature" = None, coCoMM_FeatureModel: "coCoMM_Feature" = None, coCoMM_FeatureModel2: set["coCoMM_CrossTreeConstraint"] = None, coCoMM_FeatureModel18: "coCoMM_CoCo" = None, coCoMM_FeatureModel35: "coCoMM_SelectionStateCC" = None):
        self.name = name
        self.isDomain = isDomain
        self.id = id
        self.coCoMM_FeatureModel7 = coCoMM_FeatureModel7
        self.coCoMM_FeatureModel = coCoMM_FeatureModel
        self.coCoMM_FeatureModel2 = coCoMM_FeatureModel2 if coCoMM_FeatureModel2 is not None else set()
        self.coCoMM_FeatureModel18 = coCoMM_FeatureModel18
        self.coCoMM_FeatureModel35 = coCoMM_FeatureModel35
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def isDomain(self) -> bool:
        return self.__isDomain

    @isDomain.setter
    def isDomain(self, isDomain: bool):
        self.__isDomain = isDomain

    @property
    def coCoMM_FeatureModel7(self):
        return self.__coCoMM_FeatureModel7

    @coCoMM_FeatureModel7.setter
    def coCoMM_FeatureModel7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_FeatureModel__coCoMM_FeatureModel7", None)
        self.__coCoMM_FeatureModel7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_Feature6"):
                opp_val = getattr(old_value, "coCoMM_Feature6", None)
                if opp_val == self:
                    setattr(old_value, "coCoMM_Feature6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_Feature6"):
                opp_val = getattr(value, "coCoMM_Feature6", None)
                setattr(value, "coCoMM_Feature6", self)

    @property
    def coCoMM_FeatureModel35(self):
        return self.__coCoMM_FeatureModel35

    @coCoMM_FeatureModel35.setter
    def coCoMM_FeatureModel35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_FeatureModel__coCoMM_FeatureModel35", None)
        self.__coCoMM_FeatureModel35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_SelectionStateCC"):
                opp_val = getattr(old_value, "coCoMM_SelectionStateCC", None)
                if opp_val == self:
                    setattr(old_value, "coCoMM_SelectionStateCC", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_SelectionStateCC"):
                opp_val = getattr(value, "coCoMM_SelectionStateCC", None)
                setattr(value, "coCoMM_SelectionStateCC", self)

    @property
    def coCoMM_FeatureModel2(self):
        return self.__coCoMM_FeatureModel2

    @coCoMM_FeatureModel2.setter
    def coCoMM_FeatureModel2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_FeatureModel__coCoMM_FeatureModel2", None)
        self.__coCoMM_FeatureModel2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "coCoMM_CrossTreeConstraint"):
                    opp_val = getattr(item, "coCoMM_CrossTreeConstraint", None)
                    
                    if opp_val == self:
                        setattr(item, "coCoMM_CrossTreeConstraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "coCoMM_CrossTreeConstraint"):
                    opp_val = getattr(item, "coCoMM_CrossTreeConstraint", None)
                    
                    setattr(item, "coCoMM_CrossTreeConstraint", self)
                    

    @property
    def coCoMM_FeatureModel18(self):
        return self.__coCoMM_FeatureModel18

    @coCoMM_FeatureModel18.setter
    def coCoMM_FeatureModel18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_FeatureModel__coCoMM_FeatureModel18", None)
        self.__coCoMM_FeatureModel18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_CoCo"):
                opp_val = getattr(old_value, "coCoMM_CoCo", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_CoCo"):
                opp_val = getattr(value, "coCoMM_CoCo", None)
                if opp_val is None:
                    setattr(value, "coCoMM_CoCo", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def coCoMM_FeatureModel(self):
        return self.__coCoMM_FeatureModel

    @coCoMM_FeatureModel.setter
    def coCoMM_FeatureModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_FeatureModel__coCoMM_FeatureModel", None)
        self.__coCoMM_FeatureModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_Feature"):
                opp_val = getattr(old_value, "coCoMM_Feature", None)
                if opp_val == self:
                    setattr(old_value, "coCoMM_Feature", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_Feature"):
                opp_val = getattr(value, "coCoMM_Feature", None)
                setattr(value, "coCoMM_Feature", self)
