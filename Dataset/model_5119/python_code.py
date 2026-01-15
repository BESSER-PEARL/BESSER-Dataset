from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Verdict(Enum):
    none = "none"
    pass = "pass"
    fail = "fail"


############################################
# Definition of Classes
############################################

class VariableValue:

    pass
class diva_EnumVariableValue(VariableValue):

    pass
class diva_BoolVariableValue(VariableValue):

    def __init__(self, bool: bool):
        self.bool = bool
        
    @property
    def bool(self) -> bool:
        return self.__bool

    @bool.setter
    def bool(self, bool: bool):
        self.__bool = bool

class diva_DiVAModelElement(ABC):

    pass
class ScoredElement:

    pass
class diva_ConfigVariant(ScoredElement):

    pass
class diva_Configuration(ScoredElement):

    def __init__(self, verdict: str, diva_Configuration: "diva_Context" = None, diva_Configuration75: set["diva_ConfigVariant"] = None):
        self.verdict = verdict
        self.diva_Configuration = diva_Configuration
        self.diva_Configuration75 = diva_Configuration75 if diva_Configuration75 is not None else set()
        
    @property
    def verdict(self) -> str:
        return self.__verdict

    @verdict.setter
    def verdict(self, verdict: str):
        self.__verdict = verdict

    @property
    def diva_Configuration(self):
        return self.__diva_Configuration

    @diva_Configuration.setter
    def diva_Configuration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Configuration__diva_Configuration", None)
        self.__diva_Configuration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Context68"):
                opp_val = getattr(old_value, "diva_Context68", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Context68"):
                opp_val = getattr(value, "diva_Context68", None)
                if opp_val is None:
                    setattr(value, "diva_Context68", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def diva_Configuration75(self):
        return self.__diva_Configuration75

    @diva_Configuration75.setter
    def diva_Configuration75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Configuration__diva_Configuration75", None)
        self.__diva_Configuration75 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diva_ConfigVariant"):
                    opp_val = getattr(item, "diva_ConfigVariant", None)
                    
                    if opp_val == self:
                        setattr(item, "diva_ConfigVariant", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diva_ConfigVariant"):
                    opp_val = getattr(item, "diva_ConfigVariant", None)
                    
                    setattr(item, "diva_ConfigVariant", self)
                    

class diva_Annotation:

    def __init__(self, key: str, value: str, diva_Annotation: "diva_DiVAModelElement" = None):
        self.key = key
        self.value = value
        self.diva_Annotation = diva_Annotation
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def diva_Annotation(self):
        return self.__diva_Annotation

    @diva_Annotation.setter
    def diva_Annotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Annotation__diva_Annotation", None)
        self.__diva_Annotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_DiVAModelElement"):
                opp_val = getattr(old_value, "diva_DiVAModelElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_DiVAModelElement"):
                opp_val = getattr(value, "diva_DiVAModelElement", None)
                if opp_val is None:
                    setattr(value, "diva_DiVAModelElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Rule:

    pass
class diva_PriorityRule(Rule):

    pass
class Expression:

    pass
class Term:

    pass
class diva_NaryTerm(Term):

    pass
class diva_NotTerm(Term):

    pass
class NaryTerm:

    pass
class diva_OrTerm(NaryTerm):

    pass
class diva_AndTerm(NaryTerm):

    pass
class diva_ContextExpression(Expression):

    pass
class diva_VariantExpression(Expression):

    pass
class VariableTerm:

    pass
class diva_BooleanTerm(VariableTerm):

    pass
class diva_EnumTerm(VariableTerm):

    pass
class diva_VariableTerm(Term):

    pass
class diva_VariantTerm(Term):

    pass
class Variable:

    pass
class diva_BooleanVariable(Variable):

    pass
class diva_EnumVariable(Variable):

    pass
class Model:

    pass
class diva_AspectModel(Model):

    pass
class NamedElement:

    pass
class diva_Context(NamedElement):

    def __init__(self, verdict: str, diva_Context: set["diva_VariableValue"] = None, diva_Context68: set["diva_Configuration"] = None, diva_Context70: "diva_VariantExpression" = None, diva_Context73: set["diva_Priority"] = None, diva_Context81: "diva_Scenario" = None):
        self.verdict = verdict
        self.diva_Context = diva_Context if diva_Context is not None else set()
        self.diva_Context68 = diva_Context68 if diva_Context68 is not None else set()
        self.diva_Context70 = diva_Context70
        self.diva_Context73 = diva_Context73 if diva_Context73 is not None else set()
        self.diva_Context81 = diva_Context81
        
    @property
    def verdict(self) -> str:
        return self.__verdict

    @verdict.setter
    def verdict(self, verdict: str):
        self.__verdict = verdict

    @property
    def diva_Context(self):
        return self.__diva_Context

    @diva_Context.setter
    def diva_Context(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Context__diva_Context", None)
        self.__diva_Context = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diva_VariableValue"):
                    opp_val = getattr(item, "diva_VariableValue", None)
                    
                    if opp_val == self:
                        setattr(item, "diva_VariableValue", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diva_VariableValue"):
                    opp_val = getattr(item, "diva_VariableValue", None)
                    
                    setattr(item, "diva_VariableValue", self)
                    

    @property
    def diva_Context73(self):
        return self.__diva_Context73

    @diva_Context73.setter
    def diva_Context73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Context__diva_Context73", None)
        self.__diva_Context73 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diva_Priority"):
                    opp_val = getattr(item, "diva_Priority", None)
                    
                    if opp_val == self:
                        setattr(item, "diva_Priority", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diva_Priority"):
                    opp_val = getattr(item, "diva_Priority", None)
                    
                    setattr(item, "diva_Priority", self)
                    

    @property
    def diva_Context70(self):
        return self.__diva_Context70

    @diva_Context70.setter
    def diva_Context70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Context__diva_Context70", None)
        self.__diva_Context70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_VariantExpression71"):
                opp_val = getattr(old_value, "diva_VariantExpression71", None)
                if opp_val == self:
                    setattr(old_value, "diva_VariantExpression71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_VariantExpression71"):
                opp_val = getattr(value, "diva_VariantExpression71", None)
                setattr(value, "diva_VariantExpression71", self)

    @property
    def diva_Context68(self):
        return self.__diva_Context68

    @diva_Context68.setter
    def diva_Context68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Context__diva_Context68", None)
        self.__diva_Context68 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diva_Configuration"):
                    opp_val = getattr(item, "diva_Configuration", None)
                    
                    if opp_val == self:
                        setattr(item, "diva_Configuration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diva_Configuration"):
                    opp_val = getattr(item, "diva_Configuration", None)
                    
                    setattr(item, "diva_Configuration", self)
                    

    @property
    def diva_Context81(self):
        return self.__diva_Context81

    @diva_Context81.setter
    def diva_Context81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Context__diva_Context81", None)
        self.__diva_Context81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Scenario80"):
                opp_val = getattr(old_value, "diva_Scenario80", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Scenario80"):
                opp_val = getattr(value, "diva_Scenario80", None)
                if opp_val is None:
                    setattr(value, "diva_Scenario80", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class diva_Scenario(NamedElement):

    pass
class diva_Variant(NamedElement):

    pass
class diva_EnumLiteral(NamedElement):

    pass
class Constraint:

    pass
class diva_MultiplicityConstraint(Constraint):

    def __init__(self, upper: str, lower: str, diva_MultiplicityConstraint59: "diva_ContextExpression" = None, diva_MultiplicityConstraint: "diva_Dimension" = None):
        self.upper = upper
        self.lower = lower
        self.diva_MultiplicityConstraint59 = diva_MultiplicityConstraint59
        self.diva_MultiplicityConstraint = diva_MultiplicityConstraint
        
    @property
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

    @property
    def lower(self) -> str:
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower

    @property
    def diva_MultiplicityConstraint59(self):
        return self.__diva_MultiplicityConstraint59

    @diva_MultiplicityConstraint59.setter
    def diva_MultiplicityConstraint59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_MultiplicityConstraint__diva_MultiplicityConstraint59", None)
        self.__diva_MultiplicityConstraint59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_ContextExpression60"):
                opp_val = getattr(old_value, "diva_ContextExpression60", None)
                if opp_val == self:
                    setattr(old_value, "diva_ContextExpression60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_ContextExpression60"):
                opp_val = getattr(value, "diva_ContextExpression60", None)
                setattr(value, "diva_ContextExpression60", self)

    @property
    def diva_MultiplicityConstraint(self):
        return self.__diva_MultiplicityConstraint

    @diva_MultiplicityConstraint.setter
    def diva_MultiplicityConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_MultiplicityConstraint__diva_MultiplicityConstraint", None)
        self.__diva_MultiplicityConstraint = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Dimension44"):
                opp_val = getattr(old_value, "diva_Dimension44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Dimension44"):
                opp_val = getattr(value, "diva_Dimension44", None)
                if opp_val is None:
                    setattr(value, "diva_Dimension44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class diva_Invariant(Constraint):

    pass
class diva_Constraint(NamedElement):

    pass
class diva_Rule(NamedElement):

    pass
class diva_Dimension(NamedElement):

    def __init__(self, upper: str, lower: str, diva_Dimension: "diva_VariabilityModel" = None, 27: "diva_Variant" = None, 38: set["diva_Variant"] = None, diva_Dimension41: set["diva_Property"] = None, diva_Dimension44: set["diva_MultiplicityConstraint"] = None):
        self.upper = upper
        self.lower = lower
        self.diva_Dimension = diva_Dimension
        self.27 = 27
        self.38 = 38 if 38 is not None else set()
        self.diva_Dimension41 = diva_Dimension41 if diva_Dimension41 is not None else set()
        self.diva_Dimension44 = diva_Dimension44 if diva_Dimension44 is not None else set()
        
    @property
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

    @property
    def lower(self) -> str:
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower

    @property
    def diva_Dimension41(self):
        return self.__diva_Dimension41

    @diva_Dimension41.setter
    def diva_Dimension41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Dimension__diva_Dimension41", None)
        self.__diva_Dimension41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diva_Property42"):
                    opp_val = getattr(item, "diva_Property42", None)
                    
                    if opp_val == self:
                        setattr(item, "diva_Property42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diva_Property42"):
                    opp_val = getattr(item, "diva_Property42", None)
                    
                    setattr(item, "diva_Property42", self)
                    

    @property
    def 27(self):
        return self.__27

    @27.setter
    def 27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Dimension__27", None)
        self.__27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "26"):
                opp_val = getattr(old_value, "26", None)
                if opp_val == self:
                    setattr(old_value, "26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "26"):
                opp_val = getattr(value, "26", None)
                setattr(value, "26", self)

    @property
    def diva_Dimension44(self):
        return self.__diva_Dimension44

    @diva_Dimension44.setter
    def diva_Dimension44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Dimension__diva_Dimension44", None)
        self.__diva_Dimension44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diva_MultiplicityConstraint"):
                    opp_val = getattr(item, "diva_MultiplicityConstraint", None)
                    
                    if opp_val == self:
                        setattr(item, "diva_MultiplicityConstraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diva_MultiplicityConstraint"):
                    opp_val = getattr(item, "diva_MultiplicityConstraint", None)
                    
                    setattr(item, "diva_MultiplicityConstraint", self)
                    

    @property
    def diva_Dimension(self):
        return self.__diva_Dimension

    @diva_Dimension.setter
    def diva_Dimension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Dimension__diva_Dimension", None)
        self.__diva_Dimension = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_VariabilityModel6"):
                opp_val = getattr(old_value, "diva_VariabilityModel6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_VariabilityModel6"):
                opp_val = getattr(value, "diva_VariabilityModel6", None)
                if opp_val is None:
                    setattr(value, "diva_VariabilityModel6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def 38(self):
        return self.__38

    @38.setter
    def 38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Dimension__38", None)
        self.__38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "39"):
                    opp_val = getattr(item, "39", None)
                    
                    if opp_val == self:
                        setattr(item, "39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "39"):
                    opp_val = getattr(item, "39", None)
                    
                    setattr(item, "39", self)
                    

class diva_Property(NamedElement):

    def __init__(self, direction: str, diva_Property: "diva_VariabilityModel" = None, diva_Property54: "diva_PropertyValue" = None, diva_Property57: "diva_PropertyPriority" = None, diva_Property42: "diva_Dimension" = None, diva_Property85: "diva_Score" = None, diva_Property88: "diva_Priority" = None):
        self.direction = direction
        self.diva_Property = diva_Property
        self.diva_Property54 = diva_Property54
        self.diva_Property57 = diva_Property57
        self.diva_Property42 = diva_Property42
        self.diva_Property85 = diva_Property85
        self.diva_Property88 = diva_Property88
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def diva_Property57(self):
        return self.__diva_Property57

    @diva_Property57.setter
    def diva_Property57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Property__diva_Property57", None)
        self.__diva_Property57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_PropertyPriority56"):
                opp_val = getattr(old_value, "diva_PropertyPriority56", None)
                if opp_val == self:
                    setattr(old_value, "diva_PropertyPriority56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_PropertyPriority56"):
                opp_val = getattr(value, "diva_PropertyPriority56", None)
                setattr(value, "diva_PropertyPriority56", self)

    @property
    def diva_Property85(self):
        return self.__diva_Property85

    @diva_Property85.setter
    def diva_Property85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Property__diva_Property85", None)
        self.__diva_Property85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Score84"):
                opp_val = getattr(old_value, "diva_Score84", None)
                if opp_val == self:
                    setattr(old_value, "diva_Score84", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Score84"):
                opp_val = getattr(value, "diva_Score84", None)
                setattr(value, "diva_Score84", self)

    @property
    def diva_Property(self):
        return self.__diva_Property

    @diva_Property.setter
    def diva_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Property__diva_Property", None)
        self.__diva_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_VariabilityModel4"):
                opp_val = getattr(old_value, "diva_VariabilityModel4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_VariabilityModel4"):
                opp_val = getattr(value, "diva_VariabilityModel4", None)
                if opp_val is None:
                    setattr(value, "diva_VariabilityModel4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def diva_Property54(self):
        return self.__diva_Property54

    @diva_Property54.setter
    def diva_Property54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Property__diva_Property54", None)
        self.__diva_Property54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_PropertyValue53"):
                opp_val = getattr(old_value, "diva_PropertyValue53", None)
                if opp_val == self:
                    setattr(old_value, "diva_PropertyValue53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_PropertyValue53"):
                opp_val = getattr(value, "diva_PropertyValue53", None)
                setattr(value, "diva_PropertyValue53", self)

    @property
    def diva_Property42(self):
        return self.__diva_Property42

    @diva_Property42.setter
    def diva_Property42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Property__diva_Property42", None)
        self.__diva_Property42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Dimension41"):
                opp_val = getattr(old_value, "diva_Dimension41", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Dimension41"):
                opp_val = getattr(value, "diva_Dimension41", None)
                if opp_val is None:
                    setattr(value, "diva_Dimension41", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def diva_Property88(self):
        return self.__diva_Property88

    @diva_Property88.setter
    def diva_Property88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Property__diva_Property88", None)
        self.__diva_Property88 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Priority87"):
                opp_val = getattr(old_value, "diva_Priority87", None)
                if opp_val == self:
                    setattr(old_value, "diva_Priority87", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Priority87"):
                opp_val = getattr(value, "diva_Priority87", None)
                setattr(value, "diva_Priority87", self)

class diva_Variable(NamedElement):

    pass
class diva_BaseModel(Model):

    def __init__(self, diva_BaseModel: "diva_VariabilityModel" = None):
        self.diva_BaseModel = diva_BaseModel
        
    @property
    def diva_BaseModel(self):
        return self.__diva_BaseModel

    @diva_BaseModel.setter
    def diva_BaseModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_BaseModel__diva_BaseModel", None)
        self.__diva_BaseModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_VariabilityModel"):
                opp_val = getattr(old_value, "diva_VariabilityModel", None)
                if opp_val == self:
                    setattr(old_value, "diva_VariabilityModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_VariabilityModel"):
                opp_val = getattr(value, "diva_VariabilityModel", None)
                setattr(value, "diva_VariabilityModel", self)

    def weave(self):
        # TODO: Implement weave method
        pass

class DiVAModelElement:

    pass
class diva_SimulationModel(DiVAModelElement):

    pass
class diva_Priority(DiVAModelElement):

    def __init__(self, priority: int, diva_Priority: "diva_Context" = None, diva_Priority87: "diva_Property" = None):
        self.priority = priority
        self.diva_Priority = diva_Priority
        self.diva_Priority87 = diva_Priority87
        
    @property
    def priority(self) -> int:
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority

    @property
    def diva_Priority87(self):
        return self.__diva_Priority87

    @diva_Priority87.setter
    def diva_Priority87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Priority__diva_Priority87", None)
        self.__diva_Priority87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Property88"):
                opp_val = getattr(old_value, "diva_Property88", None)
                if opp_val == self:
                    setattr(old_value, "diva_Property88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Property88"):
                opp_val = getattr(value, "diva_Property88", None)
                setattr(value, "diva_Property88", self)

    @property
    def diva_Priority(self):
        return self.__diva_Priority

    @diva_Priority.setter
    def diva_Priority(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Priority__diva_Priority", None)
        self.__diva_Priority = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Context73"):
                opp_val = getattr(old_value, "diva_Context73", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Context73"):
                opp_val = getattr(value, "diva_Context73", None)
                if opp_val is None:
                    setattr(value, "diva_Context73", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class diva_VariabilityModel(DiVAModelElement):

    pass
class diva_ScoredElement(DiVAModelElement):

    def __init__(self, totalScore: int, diva_ScoredElement: set["diva_Score"] = None):
        self.totalScore = totalScore
        self.diva_ScoredElement = diva_ScoredElement if diva_ScoredElement is not None else set()
        
    @property
    def totalScore(self) -> int:
        return self.__totalScore

    @totalScore.setter
    def totalScore(self, totalScore: int):
        self.__totalScore = totalScore

    @property
    def diva_ScoredElement(self):
        return self.__diva_ScoredElement

    @diva_ScoredElement.setter
    def diva_ScoredElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_ScoredElement__diva_ScoredElement", None)
        self.__diva_ScoredElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diva_Score"):
                    opp_val = getattr(item, "diva_Score", None)
                    
                    if opp_val == self:
                        setattr(item, "diva_Score", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diva_Score"):
                    opp_val = getattr(item, "diva_Score", None)
                    
                    setattr(item, "diva_Score", self)
                    

class diva_PropertyPriority(DiVAModelElement):

    def __init__(self, priority: str, diva_PropertyPriority: "diva_PriorityRule" = None, diva_PropertyPriority56: "diva_Property" = None):
        self.priority = priority
        self.diva_PropertyPriority = diva_PropertyPriority
        self.diva_PropertyPriority56 = diva_PropertyPriority56
        
    @property
    def priority(self) -> str:
        return self.__priority

    @priority.setter
    def priority(self, priority: str):
        self.__priority = priority

    @property
    def diva_PropertyPriority56(self):
        return self.__diva_PropertyPriority56

    @diva_PropertyPriority56.setter
    def diva_PropertyPriority56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_PropertyPriority__diva_PropertyPriority56", None)
        self.__diva_PropertyPriority56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Property57"):
                opp_val = getattr(old_value, "diva_Property57", None)
                if opp_val == self:
                    setattr(old_value, "diva_Property57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Property57"):
                opp_val = getattr(value, "diva_Property57", None)
                setattr(value, "diva_Property57", self)

    @property
    def diva_PropertyPriority(self):
        return self.__diva_PropertyPriority

    @diva_PropertyPriority.setter
    def diva_PropertyPriority(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_PropertyPriority__diva_PropertyPriority", None)
        self.__diva_PropertyPriority = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_PriorityRule51"):
                opp_val = getattr(old_value, "diva_PriorityRule51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_PriorityRule51"):
                opp_val = getattr(value, "diva_PriorityRule51", None)
                if opp_val is None:
                    setattr(value, "diva_PriorityRule51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class diva_Expression(DiVAModelElement):

    def __init__(self, text: str, diva_Expression: "diva_Invariant" = None, diva_Expression46: "diva_Term" = None):
        self.text = text
        self.diva_Expression = diva_Expression
        self.diva_Expression46 = diva_Expression46
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    @property
    def diva_Expression46(self):
        return self.__diva_Expression46

    @diva_Expression46.setter
    def diva_Expression46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Expression__diva_Expression46", None)
        self.__diva_Expression46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Term47"):
                opp_val = getattr(old_value, "diva_Term47", None)
                if opp_val == self:
                    setattr(old_value, "diva_Term47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Term47"):
                opp_val = getattr(value, "diva_Term47", None)
                setattr(value, "diva_Term47", self)

    @property
    def diva_Expression(self):
        return self.__diva_Expression

    @diva_Expression.setter
    def diva_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Expression__diva_Expression", None)
        self.__diva_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Invariant"):
                opp_val = getattr(old_value, "diva_Invariant", None)
                if opp_val == self:
                    setattr(old_value, "diva_Invariant", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Invariant"):
                opp_val = getattr(value, "diva_Invariant", None)
                setattr(value, "diva_Invariant", self)

class diva_Term(DiVAModelElement):

    pass
class diva_NamedElement(DiVAModelElement):

    def __init__(self, name: str, id: str):
        self.name = name
        self.id = id
        
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

class diva_VariableValue(DiVAModelElement):

    pass
class diva_Score(DiVAModelElement):

    def __init__(self, score: int, diva_Score: "diva_ScoredElement" = None, diva_Score84: "diva_Property" = None):
        self.score = score
        self.diva_Score = diva_Score
        self.diva_Score84 = diva_Score84
        
    @property
    def score(self) -> int:
        return self.__score

    @score.setter
    def score(self, score: int):
        self.__score = score

    @property
    def diva_Score84(self):
        return self.__diva_Score84

    @diva_Score84.setter
    def diva_Score84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Score__diva_Score84", None)
        self.__diva_Score84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Property85"):
                opp_val = getattr(old_value, "diva_Property85", None)
                if opp_val == self:
                    setattr(old_value, "diva_Property85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Property85"):
                opp_val = getattr(value, "diva_Property85", None)
                setattr(value, "diva_Property85", self)

    @property
    def diva_Score(self):
        return self.__diva_Score

    @diva_Score.setter
    def diva_Score(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Score__diva_Score", None)
        self.__diva_Score = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_ScoredElement"):
                opp_val = getattr(old_value, "diva_ScoredElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_ScoredElement"):
                opp_val = getattr(value, "diva_ScoredElement", None)
                if opp_val is None:
                    setattr(value, "diva_ScoredElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class diva_PropertyValue(DiVAModelElement):

    def __init__(self, value: str, diva_PropertyValue: "diva_Variant" = None, diva_PropertyValue53: "diva_Property" = None):
        self.value = value
        self.diva_PropertyValue = diva_PropertyValue
        self.diva_PropertyValue53 = diva_PropertyValue53
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def diva_PropertyValue(self):
        return self.__diva_PropertyValue

    @diva_PropertyValue.setter
    def diva_PropertyValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_PropertyValue__diva_PropertyValue", None)
        self.__diva_PropertyValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Variant29"):
                opp_val = getattr(old_value, "diva_Variant29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Variant29"):
                opp_val = getattr(value, "diva_Variant29", None)
                if opp_val is None:
                    setattr(value, "diva_Variant29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def diva_PropertyValue53(self):
        return self.__diva_PropertyValue53

    @diva_PropertyValue53.setter
    def diva_PropertyValue53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_PropertyValue__diva_PropertyValue53", None)
        self.__diva_PropertyValue53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Property54"):
                opp_val = getattr(old_value, "diva_Property54", None)
                if opp_val == self:
                    setattr(old_value, "diva_Property54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Property54"):
                opp_val = getattr(value, "diva_Property54", None)
                setattr(value, "diva_Property54", self)

class diva_Model(DiVAModelElement):

    pass