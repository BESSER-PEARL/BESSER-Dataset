from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Verdict(Enum):
    none = "none"
    pass_ = "pass_"
    fail = "fail"


############################################
# Definition of Classes
############################################

class ScoredElement:

    pass
class diva_ConfigVariant(ScoredElement):

    pass
class VariableValue:

    pass
class diva_EnumVariableValue(VariableValue):

    pass
class diva_BoolVariableValue(VariableValue):

    def __init__(self, bool: bool):
        self.bool = bool
        
        pass
    @property
    def bool(self):
        return self.__bool

    @bool.setter
    def bool(self, bool: bool):
        self.__bool = bool


class diva_DiVAModelElement(ABC):

    pass
class diva_Annotation:

    def __init__(self, key: str, value: str, diva_Annotation: "diva_DiVAModelElement" = None):
        self.key = key
        self.value = value
        self.diva_Annotation = diva_Annotation
        
        pass
    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key


    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


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
class diva_Configuration(ScoredElement):

    def __init__(self, verdict: str, diva_Configuration: "diva_Context" = None, diva_Configuration68: set["diva_ConfigVariant"] = None):
        self.verdict = verdict
        self.diva_Configuration = diva_Configuration
        self.diva_Configuration68 = diva_Configuration68 if diva_Configuration68 is not None else set()
        
        pass
    @property
    def verdict(self):
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
            if hasattr(old_value, "diva_Context61"):
                opp_val = getattr(old_value, "diva_Context61", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Context61"):
                opp_val = getattr(value, "diva_Context61", None)
                if opp_val is None:
                    setattr(value, "diva_Context61", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def diva_Configuration68(self):
        return self.__diva_Configuration68

    @diva_Configuration68.setter
    def diva_Configuration68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Configuration__diva_Configuration68", None)
        self.__diva_Configuration68 = value if value is not None else set()
        
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
                    

class VariableTerm:

    pass
class diva_BooleanTerm(VariableTerm):

    pass
class diva_EnumTerm(VariableTerm):

    pass
class Expression:

    pass
class diva_VariantExpression(Expression):

    pass
class diva_ContextExpression(Expression):

    pass
class Term:

    pass
class diva_NaryTerm(Term):

    pass
class diva_VariableTerm(Term):

    pass
class diva_VariantTerm(Term):

    pass
class Model:

    pass
class NamedElement:

    pass
class diva_Context(NamedElement):

    def __init__(self, verdict: str, diva_Context: set["diva_VariableValue"] = None, diva_Context61: set["diva_Configuration"] = None, diva_Context63: "diva_VariantExpression" = None, diva_Context66: set["diva_Priority"] = None, diva_Context74: "diva_Scenario" = None):
        self.verdict = verdict
        self.diva_Context = diva_Context if diva_Context is not None else set()
        self.diva_Context61 = diva_Context61 if diva_Context61 is not None else set()
        self.diva_Context63 = diva_Context63
        self.diva_Context66 = diva_Context66 if diva_Context66 is not None else set()
        self.diva_Context74 = diva_Context74
        
        pass
    @property
    def verdict(self):
        return self.__verdict

    @verdict.setter
    def verdict(self, verdict: str):
        self.__verdict = verdict


    @property
    def diva_Context63(self):
        return self.__diva_Context63

    @diva_Context63.setter
    def diva_Context63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Context__diva_Context63", None)
        self.__diva_Context63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_VariantExpression64"):
                opp_val = getattr(old_value, "diva_VariantExpression64", None)
                if opp_val == self:
                    setattr(old_value, "diva_VariantExpression64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_VariantExpression64"):
                opp_val = getattr(value, "diva_VariantExpression64", None)
                setattr(value, "diva_VariantExpression64", self)

    @property
    def diva_Context74(self):
        return self.__diva_Context74

    @diva_Context74.setter
    def diva_Context74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Context__diva_Context74", None)
        self.__diva_Context74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Scenario73"):
                opp_val = getattr(old_value, "diva_Scenario73", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Scenario73"):
                opp_val = getattr(value, "diva_Scenario73", None)
                if opp_val is None:
                    setattr(value, "diva_Scenario73", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def diva_Context66(self):
        return self.__diva_Context66

    @diva_Context66.setter
    def diva_Context66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Context__diva_Context66", None)
        self.__diva_Context66 = value if value is not None else set()
        
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
    def diva_Context61(self):
        return self.__diva_Context61

    @diva_Context61.setter
    def diva_Context61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Context__diva_Context61", None)
        self.__diva_Context61 = value if value is not None else set()
        
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
                    

class diva_Variant(NamedElement):

    pass
class diva_Scenario(NamedElement):

    pass
class Constraint:

    pass
class diva_MultiplicityConstraint(Constraint):

    def __init__(self, upper: str, lower: str, diva_MultiplicityConstraint: "diva_Dimension" = None, diva_MultiplicityConstraint54: "diva_ContextExpression" = None):
        self.upper = upper
        self.lower = lower
        self.diva_MultiplicityConstraint = diva_MultiplicityConstraint
        self.diva_MultiplicityConstraint54 = diva_MultiplicityConstraint54
        
        pass
    @property
    def lower(self):
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower


    @property
    def upper(self):
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper


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
            if hasattr(old_value, "diva_Dimension39"):
                opp_val = getattr(old_value, "diva_Dimension39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Dimension39"):
                opp_val = getattr(value, "diva_Dimension39", None)
                if opp_val is None:
                    setattr(value, "diva_Dimension39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def diva_MultiplicityConstraint54(self):
        return self.__diva_MultiplicityConstraint54

    @diva_MultiplicityConstraint54.setter
    def diva_MultiplicityConstraint54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_MultiplicityConstraint__diva_MultiplicityConstraint54", None)
        self.__diva_MultiplicityConstraint54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_ContextExpression55"):
                opp_val = getattr(old_value, "diva_ContextExpression55", None)
                if opp_val == self:
                    setattr(old_value, "diva_ContextExpression55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_ContextExpression55"):
                opp_val = getattr(value, "diva_ContextExpression55", None)
                setattr(value, "diva_ContextExpression55", self)

class diva_Invariant(Constraint):

    pass
class diva_Constraint(NamedElement):

    pass
class diva_Rule(NamedElement):

    pass
class diva_Dimension(NamedElement):

    def __init__(self, upper: str, lower: str, diva_Dimension36: set["diva_Property"] = None, diva_Dimension39: set["diva_MultiplicityConstraint"] = None, Dimension: "diva_Variant" = None, type: set["diva_Variant"] = None, diva_Dimension: "diva_VariabilityModel" = None):
        self.upper = upper
        self.lower = lower
        self.diva_Dimension36 = diva_Dimension36 if diva_Dimension36 is not None else set()
        self.diva_Dimension39 = diva_Dimension39 if diva_Dimension39 is not None else set()
        self.Dimension = Dimension
        self.type = type if type is not None else set()
        self.diva_Dimension = diva_Dimension
        
        pass
    @property
    def upper(self):
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper


    @property
    def lower(self):
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower


    @property
    def Dimension(self):
        return self.__Dimension

    @Dimension.setter
    def Dimension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Dimension__Dimension", None)
        self.__Dimension = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "variant"):
                opp_val = getattr(old_value, "variant", None)
                if opp_val == self:
                    setattr(old_value, "variant", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "variant"):
                opp_val = getattr(value, "variant", None)
                setattr(value, "variant", self)

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Dimension__type", None)
        self.__type = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Variant"):
                    opp_val = getattr(item, "Variant", None)
                    
                    if opp_val == self:
                        setattr(item, "Variant", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Variant"):
                    opp_val = getattr(item, "Variant", None)
                    
                    setattr(item, "Variant", self)
                    

    @property
    def diva_Dimension39(self):
        return self.__diva_Dimension39

    @diva_Dimension39.setter
    def diva_Dimension39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Dimension__diva_Dimension39", None)
        self.__diva_Dimension39 = value if value is not None else set()
        
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
    def diva_Dimension36(self):
        return self.__diva_Dimension36

    @diva_Dimension36.setter
    def diva_Dimension36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Dimension__diva_Dimension36", None)
        self.__diva_Dimension36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diva_Property37"):
                    opp_val = getattr(item, "diva_Property37", None)
                    
                    if opp_val == self:
                        setattr(item, "diva_Property37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diva_Property37"):
                    opp_val = getattr(item, "diva_Property37", None)
                    
                    setattr(item, "diva_Property37", self)
                    

class diva_Property(NamedElement):

    def __init__(self, direction: str, diva_Property37: "diva_Dimension" = None, diva_Property49: "diva_PropertyValue" = None, diva_Property52: "diva_PropertyPriority" = None, diva_Property: "diva_VariabilityModel" = None, diva_Property78: "diva_Score" = None, diva_Property81: "diva_Priority" = None):
        self.direction = direction
        self.diva_Property37 = diva_Property37
        self.diva_Property49 = diva_Property49
        self.diva_Property52 = diva_Property52
        self.diva_Property = diva_Property
        self.diva_Property78 = diva_Property78
        self.diva_Property81 = diva_Property81
        
        pass
    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction


    @property
    def diva_Property49(self):
        return self.__diva_Property49

    @diva_Property49.setter
    def diva_Property49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Property__diva_Property49", None)
        self.__diva_Property49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_PropertyValue48"):
                opp_val = getattr(old_value, "diva_PropertyValue48", None)
                if opp_val == self:
                    setattr(old_value, "diva_PropertyValue48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_PropertyValue48"):
                opp_val = getattr(value, "diva_PropertyValue48", None)
                setattr(value, "diva_PropertyValue48", self)

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
    def diva_Property52(self):
        return self.__diva_Property52

    @diva_Property52.setter
    def diva_Property52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Property__diva_Property52", None)
        self.__diva_Property52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_PropertyPriority51"):
                opp_val = getattr(old_value, "diva_PropertyPriority51", None)
                if opp_val == self:
                    setattr(old_value, "diva_PropertyPriority51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_PropertyPriority51"):
                opp_val = getattr(value, "diva_PropertyPriority51", None)
                setattr(value, "diva_PropertyPriority51", self)

    @property
    def diva_Property78(self):
        return self.__diva_Property78

    @diva_Property78.setter
    def diva_Property78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Property__diva_Property78", None)
        self.__diva_Property78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Score77"):
                opp_val = getattr(old_value, "diva_Score77", None)
                if opp_val == self:
                    setattr(old_value, "diva_Score77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Score77"):
                opp_val = getattr(value, "diva_Score77", None)
                setattr(value, "diva_Score77", self)

    @property
    def diva_Property81(self):
        return self.__diva_Property81

    @diva_Property81.setter
    def diva_Property81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Property__diva_Property81", None)
        self.__diva_Property81 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Priority80"):
                opp_val = getattr(old_value, "diva_Priority80", None)
                if opp_val == self:
                    setattr(old_value, "diva_Priority80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Priority80"):
                opp_val = getattr(value, "diva_Priority80", None)
                setattr(value, "diva_Priority80", self)

    @property
    def diva_Property37(self):
        return self.__diva_Property37

    @diva_Property37.setter
    def diva_Property37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Property__diva_Property37", None)
        self.__diva_Property37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Dimension36"):
                opp_val = getattr(old_value, "diva_Dimension36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Dimension36"):
                opp_val = getattr(value, "diva_Dimension36", None)
                if opp_val is None:
                    setattr(value, "diva_Dimension36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class diva_Variable(NamedElement):

    pass
class diva_BaseModel(Model):

    def __init__(self, diva_BaseModel: "diva_VariabilityModel" = None):
        self.diva_BaseModel = diva_BaseModel
        
        pass
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
class diva_Model(DiVAModelElement):

    pass
class diva_SimulationModel(DiVAModelElement):

    pass
class diva_NamedElement(DiVAModelElement):

    def __init__(self, name: str, id: str):
        self.name = name
        self.id = id
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class diva_Expression(DiVAModelElement):

    def __init__(self, text: str, diva_Expression41: "diva_Term" = None, diva_Expression: "diva_Invariant" = None):
        self.text = text
        self.diva_Expression41 = diva_Expression41
        self.diva_Expression = diva_Expression
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def diva_Expression41(self):
        return self.__diva_Expression41

    @diva_Expression41.setter
    def diva_Expression41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Expression__diva_Expression41", None)
        self.__diva_Expression41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Term42"):
                opp_val = getattr(old_value, "diva_Term42", None)
                if opp_val == self:
                    setattr(old_value, "diva_Term42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Term42"):
                opp_val = getattr(value, "diva_Term42", None)
                setattr(value, "diva_Term42", self)

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

class diva_VariableValue(DiVAModelElement):

    pass
class diva_Priority(DiVAModelElement):

    def __init__(self, priority: int, diva_Priority: "diva_Context" = None, diva_Priority80: "diva_Property" = None):
        self.priority = priority
        self.diva_Priority = diva_Priority
        self.diva_Priority80 = diva_Priority80
        
        pass
    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority


    @property
    def diva_Priority80(self):
        return self.__diva_Priority80

    @diva_Priority80.setter
    def diva_Priority80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Priority__diva_Priority80", None)
        self.__diva_Priority80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Property81"):
                opp_val = getattr(old_value, "diva_Property81", None)
                if opp_val == self:
                    setattr(old_value, "diva_Property81", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Property81"):
                opp_val = getattr(value, "diva_Property81", None)
                setattr(value, "diva_Property81", self)

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
            if hasattr(old_value, "diva_Context66"):
                opp_val = getattr(old_value, "diva_Context66", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Context66"):
                opp_val = getattr(value, "diva_Context66", None)
                if opp_val is None:
                    setattr(value, "diva_Context66", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class diva_PropertyPriority(DiVAModelElement):

    def __init__(self, priority: str, diva_PropertyPriority: "diva_PriorityRule" = None, diva_PropertyPriority51: "diva_Property" = None):
        self.priority = priority
        self.diva_PropertyPriority = diva_PropertyPriority
        self.diva_PropertyPriority51 = diva_PropertyPriority51
        
        pass
    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, priority: str):
        self.__priority = priority


    @property
    def diva_PropertyPriority51(self):
        return self.__diva_PropertyPriority51

    @diva_PropertyPriority51.setter
    def diva_PropertyPriority51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_PropertyPriority__diva_PropertyPriority51", None)
        self.__diva_PropertyPriority51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Property52"):
                opp_val = getattr(old_value, "diva_Property52", None)
                if opp_val == self:
                    setattr(old_value, "diva_Property52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Property52"):
                opp_val = getattr(value, "diva_Property52", None)
                setattr(value, "diva_Property52", self)

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
            if hasattr(old_value, "diva_PriorityRule46"):
                opp_val = getattr(old_value, "diva_PriorityRule46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_PriorityRule46"):
                opp_val = getattr(value, "diva_PriorityRule46", None)
                if opp_val is None:
                    setattr(value, "diva_PriorityRule46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class diva_PropertyValue(DiVAModelElement):

    def __init__(self, value: str, diva_PropertyValue: "diva_Variant" = None, diva_PropertyValue48: "diva_Property" = None):
        self.value = value
        self.diva_PropertyValue = diva_PropertyValue
        self.diva_PropertyValue48 = diva_PropertyValue48
        
        pass
    @property
    def value(self):
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
            if hasattr(old_value, "diva_Variant26"):
                opp_val = getattr(old_value, "diva_Variant26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Variant26"):
                opp_val = getattr(value, "diva_Variant26", None)
                if opp_val is None:
                    setattr(value, "diva_Variant26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def diva_PropertyValue48(self):
        return self.__diva_PropertyValue48

    @diva_PropertyValue48.setter
    def diva_PropertyValue48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_PropertyValue__diva_PropertyValue48", None)
        self.__diva_PropertyValue48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Property49"):
                opp_val = getattr(old_value, "diva_Property49", None)
                if opp_val == self:
                    setattr(old_value, "diva_Property49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Property49"):
                opp_val = getattr(value, "diva_Property49", None)
                setattr(value, "diva_Property49", self)

class diva_Score(DiVAModelElement):

    def __init__(self, score: int, diva_Score: "diva_ScoredElement" = None, diva_Score77: "diva_Property" = None):
        self.score = score
        self.diva_Score = diva_Score
        self.diva_Score77 = diva_Score77
        
        pass
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score: int):
        self.__score = score


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

    @property
    def diva_Score77(self):
        return self.__diva_Score77

    @diva_Score77.setter
    def diva_Score77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Score__diva_Score77", None)
        self.__diva_Score77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Property78"):
                opp_val = getattr(old_value, "diva_Property78", None)
                if opp_val == self:
                    setattr(old_value, "diva_Property78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Property78"):
                opp_val = getattr(value, "diva_Property78", None)
                setattr(value, "diva_Property78", self)

class diva_ScoredElement(DiVAModelElement):

    def __init__(self, totalScore: int, diva_ScoredElement: set["diva_Score"] = None):
        self.totalScore = totalScore
        self.diva_ScoredElement = diva_ScoredElement if diva_ScoredElement is not None else set()
        
        pass
    @property
    def totalScore(self):
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
                    

class diva_VariabilityModel(DiVAModelElement):

    pass
class diva_NotTerm(Term):

    pass
class NaryTerm:

    pass
class diva_OrTerm(NaryTerm):

    pass
class diva_AndTerm(NaryTerm):

    pass
class diva_Term(DiVAModelElement):

    pass
class diva_EnumLiteral(NamedElement):

    pass
class Variable:

    pass
class diva_BooleanVariable(Variable):

    pass
class diva_EnumVariable(Variable):

    pass
class diva_AspectModel(Model):

    pass