from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ConfigScenarioType(Enum):
    fmSearch = "fmSearch"
    fmPreferences = "fmPreferences"
    fmConflicts = "fmConflicts"
    fsgSearch = "fsgSearch"
    fsgPreferences = "fsgPreferences"
    fsgConflicts = "fsgConflicts"
class DataType(Enum):
    string = "string"
    int = "int"
    double = "double"
    boolean = "boolean"
class CMConstraintType(Enum):
    not = "not"
    and = "and"
    or = "or"
    implies = "implies"
class SCType(Enum):
    hardLimit = "hardLimit"
    optimization = "optimization"
    finiteDomain = "finiteDomain"
    selectionState = "selectionState"
class SelectionStateSCType(Enum):
    mandatory = "mandatory"
    preferred = "preferred"
    forbidden = "forbidden"
class TreeConstraintType(Enum):
    Alternative = "Alternative"
    Or = "Or"
    And = "And"
class OptimizationSCFunct(Enum):
    maximize = "maximize"
    minimize = "minimize"
class CTConstraintType(Enum):
    not = "not"
    and = "and"
    or = "or"
    implies = "implies"
class ConfigType(Enum):
    input = "input"
    output = "output"
class HardLimitSCOp(Enum):
    gt = "gt"
    eq = "eq"
    leq = "leq"
    lt = "lt"
    geq = "geq"


############################################
# Definition of Classes
############################################

class coCoMM_FiniteDomainSCValue:

    def __init__(self, value: str, coCoMM_FiniteDomainSCValue: "coCoMM_FiniteDomainSC" = None):
        self.value = value
        self.coCoMM_FiniteDomainSCValue = coCoMM_FiniteDomainSCValue
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def coCoMM_FiniteDomainSCValue(self):
        return self.__coCoMM_FiniteDomainSCValue

    @coCoMM_FiniteDomainSCValue.setter
    def coCoMM_FiniteDomainSCValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_FiniteDomainSCValue__coCoMM_FiniteDomainSCValue", None)
        self.__coCoMM_FiniteDomainSCValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_FiniteDomainSC82"):
                opp_val = getattr(old_value, "coCoMM_FiniteDomainSC82", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_FiniteDomainSC82"):
                opp_val = getattr(value, "coCoMM_FiniteDomainSC82", None)
                if opp_val is None:
                    setattr(value, "coCoMM_FiniteDomainSC82", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class coCoMM_Config:

    def __init__(self, selected: bool, type: str, coCoMM_Config: "coCoMM_Project" = None, coCoMM_Config59: "coCoMM_Stakeholder" = None, coCoMM_Config62: set["coCoMM_Feature"] = None):
        self.selected = selected
        self.type = type
        self.coCoMM_Config = coCoMM_Config
        self.coCoMM_Config59 = coCoMM_Config59
        self.coCoMM_Config62 = coCoMM_Config62 if coCoMM_Config62 is not None else set()
        
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
    def coCoMM_Config59(self):
        return self.__coCoMM_Config59

    @coCoMM_Config59.setter
    def coCoMM_Config59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_Config__coCoMM_Config59", None)
        self.__coCoMM_Config59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_Stakeholder60"):
                opp_val = getattr(old_value, "coCoMM_Stakeholder60", None)
                if opp_val == self:
                    setattr(old_value, "coCoMM_Stakeholder60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_Stakeholder60"):
                opp_val = getattr(value, "coCoMM_Stakeholder60", None)
                setattr(value, "coCoMM_Stakeholder60", self)

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
            if hasattr(old_value, "coCoMM_Project57"):
                opp_val = getattr(old_value, "coCoMM_Project57", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_Project57"):
                opp_val = getattr(value, "coCoMM_Project57", None)
                if opp_val is None:
                    setattr(value, "coCoMM_Project57", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def coCoMM_Config62(self):
        return self.__coCoMM_Config62

    @coCoMM_Config62.setter
    def coCoMM_Config62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_Config__coCoMM_Config62", None)
        self.__coCoMM_Config62 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "coCoMM_Feature63"):
                    opp_val = getattr(item, "coCoMM_Feature63", None)
                    
                    if opp_val == self:
                        setattr(item, "coCoMM_Feature63", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "coCoMM_Feature63"):
                    opp_val = getattr(item, "coCoMM_Feature63", None)
                    
                    setattr(item, "coCoMM_Feature63", self)
                    

class coCoMM_HardLimitDRExpression:

    def __init__(self, op: str, value: str, coCoMM_HardLimitDRExpression: "coCoMM_HardLimitSC" = None):
        self.op = op
        self.value = value
        self.coCoMM_HardLimitDRExpression = coCoMM_HardLimitDRExpression
        
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
    def coCoMM_HardLimitDRExpression(self):
        return self.__coCoMM_HardLimitDRExpression

    @coCoMM_HardLimitDRExpression.setter
    def coCoMM_HardLimitDRExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_HardLimitDRExpression__coCoMM_HardLimitDRExpression", None)
        self.__coCoMM_HardLimitDRExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_HardLimitSC"):
                opp_val = getattr(old_value, "coCoMM_HardLimitSC", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_HardLimitSC"):
                opp_val = getattr(value, "coCoMM_HardLimitSC", None)
                if opp_val is None:
                    setattr(value, "coCoMM_HardLimitSC", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class coCoMM_CMConstraintExpression:

    def __init__(self, op: str, coCoMM_CMConstraintExpression: "coCoMM_CrossModelConstraint" = None, coCoMM_CMConstraintExpression75: "coCoMM_CMConstraintExpression" = None, coCoMM_CMConstraintExpression73: set["coCoMM_CMConstraintExpression"] = None, coCoMM_CMConstraintExpression71: set["coCoMM_Feature"] = None):
        self.op = op
        self.coCoMM_CMConstraintExpression = coCoMM_CMConstraintExpression
        self.coCoMM_CMConstraintExpression75 = coCoMM_CMConstraintExpression75
        self.coCoMM_CMConstraintExpression73 = coCoMM_CMConstraintExpression73 if coCoMM_CMConstraintExpression73 is not None else set()
        self.coCoMM_CMConstraintExpression71 = coCoMM_CMConstraintExpression71 if coCoMM_CMConstraintExpression71 is not None else set()
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def coCoMM_CMConstraintExpression73(self):
        return self.__coCoMM_CMConstraintExpression73

    @coCoMM_CMConstraintExpression73.setter
    def coCoMM_CMConstraintExpression73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_CMConstraintExpression__coCoMM_CMConstraintExpression73", None)
        self.__coCoMM_CMConstraintExpression73 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "coCoMM_CMConstraintExpression75"):
                    opp_val = getattr(item, "coCoMM_CMConstraintExpression75", None)
                    
                    if opp_val == self:
                        setattr(item, "coCoMM_CMConstraintExpression75", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "coCoMM_CMConstraintExpression75"):
                    opp_val = getattr(item, "coCoMM_CMConstraintExpression75", None)
                    
                    setattr(item, "coCoMM_CMConstraintExpression75", self)
                    

    @property
    def coCoMM_CMConstraintExpression71(self):
        return self.__coCoMM_CMConstraintExpression71

    @coCoMM_CMConstraintExpression71.setter
    def coCoMM_CMConstraintExpression71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_CMConstraintExpression__coCoMM_CMConstraintExpression71", None)
        self.__coCoMM_CMConstraintExpression71 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "coCoMM_Feature72"):
                    opp_val = getattr(item, "coCoMM_Feature72", None)
                    
                    if opp_val == self:
                        setattr(item, "coCoMM_Feature72", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "coCoMM_Feature72"):
                    opp_val = getattr(item, "coCoMM_Feature72", None)
                    
                    setattr(item, "coCoMM_Feature72", self)
                    

    @property
    def coCoMM_CMConstraintExpression75(self):
        return self.__coCoMM_CMConstraintExpression75

    @coCoMM_CMConstraintExpression75.setter
    def coCoMM_CMConstraintExpression75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_CMConstraintExpression__coCoMM_CMConstraintExpression75", None)
        self.__coCoMM_CMConstraintExpression75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_CMConstraintExpression73"):
                opp_val = getattr(old_value, "coCoMM_CMConstraintExpression73", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_CMConstraintExpression73"):
                opp_val = getattr(value, "coCoMM_CMConstraintExpression73", None)
                if opp_val is None:
                    setattr(value, "coCoMM_CMConstraintExpression73", set([self]))
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
            if hasattr(old_value, "coCoMM_CrossModelConstraint41"):
                opp_val = getattr(old_value, "coCoMM_CrossModelConstraint41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_CrossModelConstraint41"):
                opp_val = getattr(value, "coCoMM_CrossModelConstraint41", None)
                if opp_val is None:
                    setattr(value, "coCoMM_CrossModelConstraint41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class coCoMM_Stakeholder:

    def __init__(self, name: str, job: str, coCoMM_Stakeholder: "coCoMM_CoCo" = None, coCoMM_Stakeholder60: "coCoMM_Config" = None):
        self.name = name
        self.job = job
        self.coCoMM_Stakeholder = coCoMM_Stakeholder
        self.coCoMM_Stakeholder60 = coCoMM_Stakeholder60
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def job(self) -> str:
        return self.__job

    @job.setter
    def job(self, job: str):
        self.__job = job

    @property
    def coCoMM_Stakeholder60(self):
        return self.__coCoMM_Stakeholder60

    @coCoMM_Stakeholder60.setter
    def coCoMM_Stakeholder60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_Stakeholder__coCoMM_Stakeholder60", None)
        self.__coCoMM_Stakeholder60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_Config59"):
                opp_val = getattr(old_value, "coCoMM_Config59", None)
                if opp_val == self:
                    setattr(old_value, "coCoMM_Config59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_Config59"):
                opp_val = getattr(value, "coCoMM_Config59", None)
                setattr(value, "coCoMM_Config59", self)

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
            if hasattr(old_value, "coCoMM_CoCo39"):
                opp_val = getattr(old_value, "coCoMM_CoCo39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_CoCo39"):
                opp_val = getattr(value, "coCoMM_CoCo39", None)
                if opp_val is None:
                    setattr(value, "coCoMM_CoCo39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SolutionConstraint:

    pass
class coCoMM_HardLimitSC(SolutionConstraint):

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
            if hasattr(old_value, "coCoMM_AttributeType52"):
                opp_val = getattr(old_value, "coCoMM_AttributeType52", None)
                if opp_val == self:
                    setattr(old_value, "coCoMM_AttributeType52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_AttributeType52"):
                opp_val = getattr(value, "coCoMM_AttributeType52", None)
                setattr(value, "coCoMM_AttributeType52", self)

class coCoMM_FiniteDomainSC(SolutionConstraint):

    pass
class coCoMM_SelectionStateSC(SolutionConstraint):

    def __init__(self, state: str, coCoMM_SelectionStateSC: "coCoMM_FeatureModel" = None, coCoMM_SelectionStateSC45: "coCoMM_Feature" = None):
        self.state = state
        self.coCoMM_SelectionStateSC = coCoMM_SelectionStateSC
        self.coCoMM_SelectionStateSC45 = coCoMM_SelectionStateSC45
        
    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, state: str):
        self.__state = state

    @property
    def coCoMM_SelectionStateSC45(self):
        return self.__coCoMM_SelectionStateSC45

    @coCoMM_SelectionStateSC45.setter
    def coCoMM_SelectionStateSC45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_SelectionStateSC__coCoMM_SelectionStateSC45", None)
        self.__coCoMM_SelectionStateSC45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_Feature46"):
                opp_val = getattr(old_value, "coCoMM_Feature46", None)
                if opp_val == self:
                    setattr(old_value, "coCoMM_Feature46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_Feature46"):
                opp_val = getattr(value, "coCoMM_Feature46", None)
                setattr(value, "coCoMM_Feature46", self)

    @property
    def coCoMM_SelectionStateSC(self):
        return self.__coCoMM_SelectionStateSC

    @coCoMM_SelectionStateSC.setter
    def coCoMM_SelectionStateSC(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_SelectionStateSC__coCoMM_SelectionStateSC", None)
        self.__coCoMM_SelectionStateSC = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_FeatureModel43"):
                opp_val = getattr(old_value, "coCoMM_FeatureModel43", None)
                if opp_val == self:
                    setattr(old_value, "coCoMM_FeatureModel43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_FeatureModel43"):
                opp_val = getattr(value, "coCoMM_FeatureModel43", None)
                setattr(value, "coCoMM_FeatureModel43", self)

class coCoMM_CoCo:

    def __init__(self, configScenario: str, coCoMM_CoCo: set["coCoMM_FeatureModel"] = None, coCoMM_CoCo30: set["coCoMM_CrossModelConstraint"] = None, coCoMM_CoCo32: set["coCoMM_SolutionConstraint"] = None, coCoMM_CoCo34: set["coCoMM_AttributeType"] = None, coCoMM_CoCo37: set["coCoMM_Project"] = None, coCoMM_CoCo39: set["coCoMM_Stakeholder"] = None):
        self.configScenario = configScenario
        self.coCoMM_CoCo = coCoMM_CoCo if coCoMM_CoCo is not None else set()
        self.coCoMM_CoCo30 = coCoMM_CoCo30 if coCoMM_CoCo30 is not None else set()
        self.coCoMM_CoCo32 = coCoMM_CoCo32 if coCoMM_CoCo32 is not None else set()
        self.coCoMM_CoCo34 = coCoMM_CoCo34 if coCoMM_CoCo34 is not None else set()
        self.coCoMM_CoCo37 = coCoMM_CoCo37 if coCoMM_CoCo37 is not None else set()
        self.coCoMM_CoCo39 = coCoMM_CoCo39 if coCoMM_CoCo39 is not None else set()
        
    @property
    def configScenario(self) -> str:
        return self.__configScenario

    @configScenario.setter
    def configScenario(self, configScenario: str):
        self.__configScenario = configScenario

    @property
    def coCoMM_CoCo32(self):
        return self.__coCoMM_CoCo32

    @coCoMM_CoCo32.setter
    def coCoMM_CoCo32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_CoCo__coCoMM_CoCo32", None)
        self.__coCoMM_CoCo32 = value if value is not None else set()
        
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
    def coCoMM_CoCo34(self):
        return self.__coCoMM_CoCo34

    @coCoMM_CoCo34.setter
    def coCoMM_CoCo34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_CoCo__coCoMM_CoCo34", None)
        self.__coCoMM_CoCo34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "coCoMM_AttributeType35"):
                    opp_val = getattr(item, "coCoMM_AttributeType35", None)
                    
                    if opp_val == self:
                        setattr(item, "coCoMM_AttributeType35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "coCoMM_AttributeType35"):
                    opp_val = getattr(item, "coCoMM_AttributeType35", None)
                    
                    setattr(item, "coCoMM_AttributeType35", self)
                    

    @property
    def coCoMM_CoCo30(self):
        return self.__coCoMM_CoCo30

    @coCoMM_CoCo30.setter
    def coCoMM_CoCo30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_CoCo__coCoMM_CoCo30", None)
        self.__coCoMM_CoCo30 = value if value is not None else set()
        
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
                if hasattr(item, "coCoMM_FeatureModel28"):
                    opp_val = getattr(item, "coCoMM_FeatureModel28", None)
                    
                    if opp_val == self:
                        setattr(item, "coCoMM_FeatureModel28", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "coCoMM_FeatureModel28"):
                    opp_val = getattr(item, "coCoMM_FeatureModel28", None)
                    
                    setattr(item, "coCoMM_FeatureModel28", self)
                    

    @property
    def coCoMM_CoCo39(self):
        return self.__coCoMM_CoCo39

    @coCoMM_CoCo39.setter
    def coCoMM_CoCo39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_CoCo__coCoMM_CoCo39", None)
        self.__coCoMM_CoCo39 = value if value is not None else set()
        
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
    def coCoMM_CoCo37(self):
        return self.__coCoMM_CoCo37

    @coCoMM_CoCo37.setter
    def coCoMM_CoCo37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_CoCo__coCoMM_CoCo37", None)
        self.__coCoMM_CoCo37 = value if value is not None else set()
        
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
                    

class coCoMM_CTConstraintExpression:

    def __init__(self, op: str, coCoMM_CTConstraintExpression: "coCoMM_CrossTreeConstraint" = None, coCoMM_CTConstraintExpression65: set["coCoMM_Feature"] = None, coCoMM_CTConstraintExpression69: "coCoMM_CTConstraintExpression" = None, coCoMM_CTConstraintExpression67: set["coCoMM_CTConstraintExpression"] = None):
        self.op = op
        self.coCoMM_CTConstraintExpression = coCoMM_CTConstraintExpression
        self.coCoMM_CTConstraintExpression65 = coCoMM_CTConstraintExpression65 if coCoMM_CTConstraintExpression65 is not None else set()
        self.coCoMM_CTConstraintExpression69 = coCoMM_CTConstraintExpression69
        self.coCoMM_CTConstraintExpression67 = coCoMM_CTConstraintExpression67 if coCoMM_CTConstraintExpression67 is not None else set()
        
    @property
    def op(self) -> str:
        return self.__op

    @op.setter
    def op(self, op: str):
        self.__op = op

    @property
    def coCoMM_CTConstraintExpression69(self):
        return self.__coCoMM_CTConstraintExpression69

    @coCoMM_CTConstraintExpression69.setter
    def coCoMM_CTConstraintExpression69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_CTConstraintExpression__coCoMM_CTConstraintExpression69", None)
        self.__coCoMM_CTConstraintExpression69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_CTConstraintExpression67"):
                opp_val = getattr(old_value, "coCoMM_CTConstraintExpression67", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_CTConstraintExpression67"):
                opp_val = getattr(value, "coCoMM_CTConstraintExpression67", None)
                if opp_val is None:
                    setattr(value, "coCoMM_CTConstraintExpression67", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def coCoMM_CTConstraintExpression65(self):
        return self.__coCoMM_CTConstraintExpression65

    @coCoMM_CTConstraintExpression65.setter
    def coCoMM_CTConstraintExpression65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_CTConstraintExpression__coCoMM_CTConstraintExpression65", None)
        self.__coCoMM_CTConstraintExpression65 = value if value is not None else set()
        
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
                    

    @property
    def coCoMM_CTConstraintExpression67(self):
        return self.__coCoMM_CTConstraintExpression67

    @coCoMM_CTConstraintExpression67.setter
    def coCoMM_CTConstraintExpression67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_CTConstraintExpression__coCoMM_CTConstraintExpression67", None)
        self.__coCoMM_CTConstraintExpression67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "coCoMM_CTConstraintExpression69"):
                    opp_val = getattr(item, "coCoMM_CTConstraintExpression69", None)
                    
                    if opp_val == self:
                        setattr(item, "coCoMM_CTConstraintExpression69", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "coCoMM_CTConstraintExpression69"):
                    opp_val = getattr(item, "coCoMM_CTConstraintExpression69", None)
                    
                    setattr(item, "coCoMM_CTConstraintExpression69", self)
                    

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
            if hasattr(old_value, "coCoMM_CrossTreeConstraint26"):
                opp_val = getattr(old_value, "coCoMM_CrossTreeConstraint26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_CrossTreeConstraint26"):
                opp_val = getattr(value, "coCoMM_CrossTreeConstraint26", None)
                if opp_val is None:
                    setattr(value, "coCoMM_CrossTreeConstraint26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class coCoMM_FeatureAttributeElement:

    def __init__(self, value: str, coCoMM_FeatureAttributeElement: "coCoMM_FeatureAttribute" = None):
        self.value = value
        self.coCoMM_FeatureAttributeElement = coCoMM_FeatureAttributeElement
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def coCoMM_FeatureAttributeElement(self):
        return self.__coCoMM_FeatureAttributeElement

    @coCoMM_FeatureAttributeElement.setter
    def coCoMM_FeatureAttributeElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_FeatureAttributeElement__coCoMM_FeatureAttributeElement", None)
        self.__coCoMM_FeatureAttributeElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_FeatureAttribute24"):
                opp_val = getattr(old_value, "coCoMM_FeatureAttribute24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_FeatureAttribute24"):
                opp_val = getattr(value, "coCoMM_FeatureAttribute24", None)
                if opp_val is None:
                    setattr(value, "coCoMM_FeatureAttribute24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class coCoMM_Project:

    def __init__(self, name: str, date: date, target: bool, coCoMM_Project: "coCoMM_CoCo" = None, coCoMM_Project54: set["coCoMM_SolutionConstraint"] = None, coCoMM_Project57: set["coCoMM_Config"] = None):
        self.name = name
        self.date = date
        self.target = target
        self.coCoMM_Project = coCoMM_Project
        self.coCoMM_Project54 = coCoMM_Project54 if coCoMM_Project54 is not None else set()
        self.coCoMM_Project57 = coCoMM_Project57 if coCoMM_Project57 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def date(self) -> date:
        return self.__date

    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def target(self) -> bool:
        return self.__target

    @target.setter
    def target(self, target: bool):
        self.__target = target

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
            if hasattr(old_value, "coCoMM_CoCo37"):
                opp_val = getattr(old_value, "coCoMM_CoCo37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_CoCo37"):
                opp_val = getattr(value, "coCoMM_CoCo37", None)
                if opp_val is None:
                    setattr(value, "coCoMM_CoCo37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def coCoMM_Project54(self):
        return self.__coCoMM_Project54

    @coCoMM_Project54.setter
    def coCoMM_Project54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_Project__coCoMM_Project54", None)
        self.__coCoMM_Project54 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "coCoMM_SolutionConstraint55"):
                    opp_val = getattr(item, "coCoMM_SolutionConstraint55", None)
                    
                    if opp_val == self:
                        setattr(item, "coCoMM_SolutionConstraint55", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "coCoMM_SolutionConstraint55"):
                    opp_val = getattr(item, "coCoMM_SolutionConstraint55", None)
                    
                    setattr(item, "coCoMM_SolutionConstraint55", self)
                    

    @property
    def coCoMM_Project57(self):
        return self.__coCoMM_Project57

    @coCoMM_Project57.setter
    def coCoMM_Project57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_Project__coCoMM_Project57", None)
        self.__coCoMM_Project57 = value if value is not None else set()
        
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
                    

class coCoMM_SolutionConstraint:

    def __init__(self, type: str, coCoMM_SolutionConstraint: "coCoMM_CoCo" = None, coCoMM_SolutionConstraint55: "coCoMM_Project" = None):
        self.type = type
        self.coCoMM_SolutionConstraint = coCoMM_SolutionConstraint
        self.coCoMM_SolutionConstraint55 = coCoMM_SolutionConstraint55
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def coCoMM_SolutionConstraint55(self):
        return self.__coCoMM_SolutionConstraint55

    @coCoMM_SolutionConstraint55.setter
    def coCoMM_SolutionConstraint55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_SolutionConstraint__coCoMM_SolutionConstraint55", None)
        self.__coCoMM_SolutionConstraint55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_Project54"):
                opp_val = getattr(old_value, "coCoMM_Project54", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_Project54"):
                opp_val = getattr(value, "coCoMM_Project54", None)
                if opp_val is None:
                    setattr(value, "coCoMM_Project54", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "coCoMM_CoCo32"):
                opp_val = getattr(old_value, "coCoMM_CoCo32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_CoCo32"):
                opp_val = getattr(value, "coCoMM_CoCo32", None)
                if opp_val is None:
                    setattr(value, "coCoMM_CoCo32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class coCoMM_CrossModelConstraint:

    pass
class coCoMM_AttributeTypeElement:

    def __init__(self, name: str, dataType: str, coCoMM_AttributeTypeElement: "coCoMM_AttributeType" = None):
        self.name = name
        self.dataType = dataType
        self.coCoMM_AttributeTypeElement = coCoMM_AttributeTypeElement
        
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
    def coCoMM_AttributeTypeElement(self):
        return self.__coCoMM_AttributeTypeElement

    @coCoMM_AttributeTypeElement.setter
    def coCoMM_AttributeTypeElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_AttributeTypeElement__coCoMM_AttributeTypeElement", None)
        self.__coCoMM_AttributeTypeElement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_AttributeType16"):
                opp_val = getattr(old_value, "coCoMM_AttributeType16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_AttributeType16"):
                opp_val = getattr(value, "coCoMM_AttributeType16", None)
                if opp_val is None:
                    setattr(value, "coCoMM_AttributeType16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class coCoMM_AttributeType:

    def __init__(self, id: str, name: str, coCoMM_AttributeType16: set["coCoMM_AttributeTypeElement"] = None, coCoMM_AttributeType18: set["coCoMM_FeatureAttribute"] = None, coCoMM_AttributeType22: "coCoMM_FeatureAttribute" = None, coCoMM_AttributeType: "coCoMM_AttributeType" = None, coCoMM_AttributeType13: "coCoMM_AttributeType" = None, coCoMM_AttributeType35: "coCoMM_CoCo" = None, coCoMM_AttributeType50: "coCoMM_HardLimitSC" = None, coCoMM_AttributeType52: "coCoMM_OptimizationSC" = None):
        self.id = id
        self.name = name
        self.coCoMM_AttributeType16 = coCoMM_AttributeType16 if coCoMM_AttributeType16 is not None else set()
        self.coCoMM_AttributeType18 = coCoMM_AttributeType18 if coCoMM_AttributeType18 is not None else set()
        self.coCoMM_AttributeType22 = coCoMM_AttributeType22
        self.coCoMM_AttributeType = coCoMM_AttributeType
        self.coCoMM_AttributeType13 = coCoMM_AttributeType13
        self.coCoMM_AttributeType35 = coCoMM_AttributeType35
        self.coCoMM_AttributeType50 = coCoMM_AttributeType50
        self.coCoMM_AttributeType52 = coCoMM_AttributeType52
        
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
    def coCoMM_AttributeType18(self):
        return self.__coCoMM_AttributeType18

    @coCoMM_AttributeType18.setter
    def coCoMM_AttributeType18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_AttributeType__coCoMM_AttributeType18", None)
        self.__coCoMM_AttributeType18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "coCoMM_FeatureAttribute19"):
                    opp_val = getattr(item, "coCoMM_FeatureAttribute19", None)
                    
                    if opp_val == self:
                        setattr(item, "coCoMM_FeatureAttribute19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "coCoMM_FeatureAttribute19"):
                    opp_val = getattr(item, "coCoMM_FeatureAttribute19", None)
                    
                    setattr(item, "coCoMM_FeatureAttribute19", self)
                    

    @property
    def coCoMM_AttributeType52(self):
        return self.__coCoMM_AttributeType52

    @coCoMM_AttributeType52.setter
    def coCoMM_AttributeType52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_AttributeType__coCoMM_AttributeType52", None)
        self.__coCoMM_AttributeType52 = value
        
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
    def coCoMM_AttributeType16(self):
        return self.__coCoMM_AttributeType16

    @coCoMM_AttributeType16.setter
    def coCoMM_AttributeType16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_AttributeType__coCoMM_AttributeType16", None)
        self.__coCoMM_AttributeType16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "coCoMM_AttributeTypeElement"):
                    opp_val = getattr(item, "coCoMM_AttributeTypeElement", None)
                    
                    if opp_val == self:
                        setattr(item, "coCoMM_AttributeTypeElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "coCoMM_AttributeTypeElement"):
                    opp_val = getattr(item, "coCoMM_AttributeTypeElement", None)
                    
                    setattr(item, "coCoMM_AttributeTypeElement", self)
                    

    @property
    def coCoMM_AttributeType50(self):
        return self.__coCoMM_AttributeType50

    @coCoMM_AttributeType50.setter
    def coCoMM_AttributeType50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_AttributeType__coCoMM_AttributeType50", None)
        self.__coCoMM_AttributeType50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_HardLimitSC49"):
                opp_val = getattr(old_value, "coCoMM_HardLimitSC49", None)
                if opp_val == self:
                    setattr(old_value, "coCoMM_HardLimitSC49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_HardLimitSC49"):
                opp_val = getattr(value, "coCoMM_HardLimitSC49", None)
                setattr(value, "coCoMM_HardLimitSC49", self)

    @property
    def coCoMM_AttributeType13(self):
        return self.__coCoMM_AttributeType13

    @coCoMM_AttributeType13.setter
    def coCoMM_AttributeType13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_AttributeType__coCoMM_AttributeType13", None)
        self.__coCoMM_AttributeType13 = value
        
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
    def coCoMM_AttributeType35(self):
        return self.__coCoMM_AttributeType35

    @coCoMM_AttributeType35.setter
    def coCoMM_AttributeType35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_AttributeType__coCoMM_AttributeType35", None)
        self.__coCoMM_AttributeType35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_CoCo34"):
                opp_val = getattr(old_value, "coCoMM_CoCo34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_CoCo34"):
                opp_val = getattr(value, "coCoMM_CoCo34", None)
                if opp_val is None:
                    setattr(value, "coCoMM_CoCo34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "coCoMM_AttributeType13"):
                opp_val = getattr(old_value, "coCoMM_AttributeType13", None)
                if opp_val == self:
                    setattr(old_value, "coCoMM_AttributeType13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_AttributeType13"):
                opp_val = getattr(value, "coCoMM_AttributeType13", None)
                setattr(value, "coCoMM_AttributeType13", self)

    @property
    def coCoMM_AttributeType22(self):
        return self.__coCoMM_AttributeType22

    @coCoMM_AttributeType22.setter
    def coCoMM_AttributeType22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_AttributeType__coCoMM_AttributeType22", None)
        self.__coCoMM_AttributeType22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_FeatureAttribute21"):
                opp_val = getattr(old_value, "coCoMM_FeatureAttribute21", None)
                if opp_val == self:
                    setattr(old_value, "coCoMM_FeatureAttribute21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_FeatureAttribute21"):
                opp_val = getattr(value, "coCoMM_FeatureAttribute21", None)
                setattr(value, "coCoMM_FeatureAttribute21", self)

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

class coCoMM_CrossTreeConstraint:

    pass
class coCoMM_FeatureAttribute:

    def __init__(self, name: str, coCoMM_FeatureAttribute: "coCoMM_Feature" = None, coCoMM_FeatureAttribute19: "coCoMM_AttributeType" = None, coCoMM_FeatureAttribute21: "coCoMM_AttributeType" = None, coCoMM_FeatureAttribute24: set["coCoMM_FeatureAttributeElement"] = None, coCoMM_FeatureAttribute77: "coCoMM_FiniteDomainSC" = None):
        self.name = name
        self.coCoMM_FeatureAttribute = coCoMM_FeatureAttribute
        self.coCoMM_FeatureAttribute19 = coCoMM_FeatureAttribute19
        self.coCoMM_FeatureAttribute21 = coCoMM_FeatureAttribute21
        self.coCoMM_FeatureAttribute24 = coCoMM_FeatureAttribute24 if coCoMM_FeatureAttribute24 is not None else set()
        self.coCoMM_FeatureAttribute77 = coCoMM_FeatureAttribute77
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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

    @property
    def coCoMM_FeatureAttribute77(self):
        return self.__coCoMM_FeatureAttribute77

    @coCoMM_FeatureAttribute77.setter
    def coCoMM_FeatureAttribute77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_FeatureAttribute__coCoMM_FeatureAttribute77", None)
        self.__coCoMM_FeatureAttribute77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_FiniteDomainSC"):
                opp_val = getattr(old_value, "coCoMM_FiniteDomainSC", None)
                if opp_val == self:
                    setattr(old_value, "coCoMM_FiniteDomainSC", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_FiniteDomainSC"):
                opp_val = getattr(value, "coCoMM_FiniteDomainSC", None)
                setattr(value, "coCoMM_FiniteDomainSC", self)

    @property
    def coCoMM_FeatureAttribute24(self):
        return self.__coCoMM_FeatureAttribute24

    @coCoMM_FeatureAttribute24.setter
    def coCoMM_FeatureAttribute24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_FeatureAttribute__coCoMM_FeatureAttribute24", None)
        self.__coCoMM_FeatureAttribute24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "coCoMM_FeatureAttributeElement"):
                    opp_val = getattr(item, "coCoMM_FeatureAttributeElement", None)
                    
                    if opp_val == self:
                        setattr(item, "coCoMM_FeatureAttributeElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "coCoMM_FeatureAttributeElement"):
                    opp_val = getattr(item, "coCoMM_FeatureAttributeElement", None)
                    
                    setattr(item, "coCoMM_FeatureAttributeElement", self)
                    

    @property
    def coCoMM_FeatureAttribute19(self):
        return self.__coCoMM_FeatureAttribute19

    @coCoMM_FeatureAttribute19.setter
    def coCoMM_FeatureAttribute19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_FeatureAttribute__coCoMM_FeatureAttribute19", None)
        self.__coCoMM_FeatureAttribute19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_AttributeType18"):
                opp_val = getattr(old_value, "coCoMM_AttributeType18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_AttributeType18"):
                opp_val = getattr(value, "coCoMM_AttributeType18", None)
                if opp_val is None:
                    setattr(value, "coCoMM_AttributeType18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def coCoMM_FeatureAttribute21(self):
        return self.__coCoMM_FeatureAttribute21

    @coCoMM_FeatureAttribute21.setter
    def coCoMM_FeatureAttribute21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_FeatureAttribute__coCoMM_FeatureAttribute21", None)
        self.__coCoMM_FeatureAttribute21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_AttributeType22"):
                opp_val = getattr(old_value, "coCoMM_AttributeType22", None)
                if opp_val == self:
                    setattr(old_value, "coCoMM_AttributeType22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_AttributeType22"):
                opp_val = getattr(value, "coCoMM_AttributeType22", None)
                setattr(value, "coCoMM_AttributeType22", self)

class coCoMM_Feature:

    def __init__(self, mandatory: bool, id: str, name: str, abstract: bool, coCoMM_Feature6: "coCoMM_FeatureModel" = None, coCoMM_Feature9: set["coCoMM_FeatureAttribute"] = None, coCoMM_Feature12: "coCoMM_TreeConstraint" = None, coCoMM_Feature: "coCoMM_FeatureModel" = None, coCoMM_Feature4: set["coCoMM_TreeConstraint"] = None, coCoMM_Feature46: "coCoMM_SelectionStateSC" = None, coCoMM_Feature63: "coCoMM_Config" = None, coCoMM_Feature66: "coCoMM_CTConstraintExpression" = None, coCoMM_Feature72: "coCoMM_CMConstraintExpression" = None, coCoMM_Feature80: "coCoMM_FiniteDomainSC" = None):
        self.mandatory = mandatory
        self.id = id
        self.name = name
        self.abstract = abstract
        self.coCoMM_Feature6 = coCoMM_Feature6
        self.coCoMM_Feature9 = coCoMM_Feature9 if coCoMM_Feature9 is not None else set()
        self.coCoMM_Feature12 = coCoMM_Feature12
        self.coCoMM_Feature = coCoMM_Feature
        self.coCoMM_Feature4 = coCoMM_Feature4 if coCoMM_Feature4 is not None else set()
        self.coCoMM_Feature46 = coCoMM_Feature46
        self.coCoMM_Feature63 = coCoMM_Feature63
        self.coCoMM_Feature66 = coCoMM_Feature66
        self.coCoMM_Feature72 = coCoMM_Feature72
        self.coCoMM_Feature80 = coCoMM_Feature80
        
    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

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
    def mandatory(self) -> bool:
        return self.__mandatory

    @mandatory.setter
    def mandatory(self, mandatory: bool):
        self.__mandatory = mandatory

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
            if hasattr(old_value, "coCoMM_CTConstraintExpression65"):
                opp_val = getattr(old_value, "coCoMM_CTConstraintExpression65", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_CTConstraintExpression65"):
                opp_val = getattr(value, "coCoMM_CTConstraintExpression65", None)
                if opp_val is None:
                    setattr(value, "coCoMM_CTConstraintExpression65", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def coCoMM_Feature80(self):
        return self.__coCoMM_Feature80

    @coCoMM_Feature80.setter
    def coCoMM_Feature80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_Feature__coCoMM_Feature80", None)
        self.__coCoMM_Feature80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_FiniteDomainSC79"):
                opp_val = getattr(old_value, "coCoMM_FiniteDomainSC79", None)
                if opp_val == self:
                    setattr(old_value, "coCoMM_FiniteDomainSC79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_FiniteDomainSC79"):
                opp_val = getattr(value, "coCoMM_FiniteDomainSC79", None)
                setattr(value, "coCoMM_FiniteDomainSC79", self)

    @property
    def coCoMM_Feature72(self):
        return self.__coCoMM_Feature72

    @coCoMM_Feature72.setter
    def coCoMM_Feature72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_Feature__coCoMM_Feature72", None)
        self.__coCoMM_Feature72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_CMConstraintExpression71"):
                opp_val = getattr(old_value, "coCoMM_CMConstraintExpression71", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_CMConstraintExpression71"):
                opp_val = getattr(value, "coCoMM_CMConstraintExpression71", None)
                if opp_val is None:
                    setattr(value, "coCoMM_CMConstraintExpression71", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def coCoMM_Feature63(self):
        return self.__coCoMM_Feature63

    @coCoMM_Feature63.setter
    def coCoMM_Feature63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_Feature__coCoMM_Feature63", None)
        self.__coCoMM_Feature63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_Config62"):
                opp_val = getattr(old_value, "coCoMM_Config62", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_Config62"):
                opp_val = getattr(value, "coCoMM_Config62", None)
                if opp_val is None:
                    setattr(value, "coCoMM_Config62", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def coCoMM_Feature46(self):
        return self.__coCoMM_Feature46

    @coCoMM_Feature46.setter
    def coCoMM_Feature46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_Feature__coCoMM_Feature46", None)
        self.__coCoMM_Feature46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_SelectionStateSC45"):
                opp_val = getattr(old_value, "coCoMM_SelectionStateSC45", None)
                if opp_val == self:
                    setattr(old_value, "coCoMM_SelectionStateSC45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_SelectionStateSC45"):
                opp_val = getattr(value, "coCoMM_SelectionStateSC45", None)
                setattr(value, "coCoMM_SelectionStateSC45", self)

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

class coCoMM_FeatureModel:

    def __init__(self, name: str, isDomain: bool, coCoMM_FeatureModel7: "coCoMM_Feature" = None, coCoMM_FeatureModel: "coCoMM_Feature" = None, coCoMM_FeatureModel2: set["coCoMM_CrossTreeConstraint"] = None, coCoMM_FeatureModel28: "coCoMM_CoCo" = None, coCoMM_FeatureModel43: "coCoMM_SelectionStateSC" = None):
        self.name = name
        self.isDomain = isDomain
        self.coCoMM_FeatureModel7 = coCoMM_FeatureModel7
        self.coCoMM_FeatureModel = coCoMM_FeatureModel
        self.coCoMM_FeatureModel2 = coCoMM_FeatureModel2 if coCoMM_FeatureModel2 is not None else set()
        self.coCoMM_FeatureModel28 = coCoMM_FeatureModel28
        self.coCoMM_FeatureModel43 = coCoMM_FeatureModel43
        
    @property
    def isDomain(self) -> bool:
        return self.__isDomain

    @isDomain.setter
    def isDomain(self, isDomain: bool):
        self.__isDomain = isDomain

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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

    @property
    def coCoMM_FeatureModel43(self):
        return self.__coCoMM_FeatureModel43

    @coCoMM_FeatureModel43.setter
    def coCoMM_FeatureModel43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_FeatureModel__coCoMM_FeatureModel43", None)
        self.__coCoMM_FeatureModel43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coCoMM_SelectionStateSC"):
                opp_val = getattr(old_value, "coCoMM_SelectionStateSC", None)
                if opp_val == self:
                    setattr(old_value, "coCoMM_SelectionStateSC", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coCoMM_SelectionStateSC"):
                opp_val = getattr(value, "coCoMM_SelectionStateSC", None)
                setattr(value, "coCoMM_SelectionStateSC", self)

    @property
    def coCoMM_FeatureModel28(self):
        return self.__coCoMM_FeatureModel28

    @coCoMM_FeatureModel28.setter
    def coCoMM_FeatureModel28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_coCoMM_FeatureModel__coCoMM_FeatureModel28", None)
        self.__coCoMM_FeatureModel28 = value
        
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
