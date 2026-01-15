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

class diva_visitors_TopDownVisitor(ABC):

    def __init__(self):
        
    def visitVariabilityModel(self, context: str, node: str):
        # TODO: Implement visitVariabilityModel method
        pass

    def visitPropertyValue(self, context: str, node: str):
        # TODO: Implement visitPropertyValue method
        pass

    def visitBooleanVariable(self, context: str, node: str):
        # TODO: Implement visitBooleanVariable method
        pass

    def visitAnnotation(self, node: str, context: str):
        # TODO: Implement visitAnnotation method
        pass

    def visitBoolVariableValue(self, node: str, context: str):
        # TODO: Implement visitBoolVariableValue method
        pass

    def visitContextExpression(self, context: str, node: str):
        # TODO: Implement visitContextExpression method
        pass

    def visitEnumVariable(self, node: str, context: str):
        # TODO: Implement visitEnumVariable method
        pass

    def visitEnumVariableValue(self, context: str, node: str):
        # TODO: Implement visitEnumVariableValue method
        pass

    def visitBooleanTerm(self, context: str, node: str):
        # TODO: Implement visitBooleanTerm method
        pass

    def visitPriority(self, node: str, context: str):
        # TODO: Implement visitPriority method
        pass

    def visitBaseModel(self, context: str, node: str):
        # TODO: Implement visitBaseModel method
        pass

    def visitInvariant(self, node: str, context: str):
        # TODO: Implement visitInvariant method
        pass

    def visitNotTerm(self, node: str, context: str):
        # TODO: Implement visitNotTerm method
        pass

    def visitVariant(self, context: str, node: str):
        # TODO: Implement visitVariant method
        pass

    def visitConfigVariant(self, node: str, context: str):
        # TODO: Implement visitConfigVariant method
        pass

    def visitOrTerm(self, node: str, context: str):
        # TODO: Implement visitOrTerm method
        pass

    def visitAspectModel(self, node: str, context: str):
        # TODO: Implement visitAspectModel method
        pass

    def visitVariantExpression(self, context: str, node: str):
        # TODO: Implement visitVariantExpression method
        pass

    def visitVariantTerm(self, context: str, node: str):
        # TODO: Implement visitVariantTerm method
        pass

    def visitAndTerm(self, node: str, context: str):
        # TODO: Implement visitAndTerm method
        pass

    def visitSimulationModel(self, context: str, node: str):
        # TODO: Implement visitSimulationModel method
        pass

    def visitDimension(self, context: str, node: str):
        # TODO: Implement visitDimension method
        pass

    def visitExpression(self, node: Expression, context: str):
        # TODO: Implement visitExpression method
        pass

    def visitMultiplicityConstraint(self, context: str, node: str):
        # TODO: Implement visitMultiplicityConstraint method
        pass

    def visitScenario(self, context: str, node: str):
        # TODO: Implement visitScenario method
        pass

    def visitConfiguration(self, node: str, context: str):
        # TODO: Implement visitConfiguration method
        pass

    def visitProperty(self, context: str, node: str):
        # TODO: Implement visitProperty method
        pass

    def visitEnumTerm(self, context: str, node: str):
        # TODO: Implement visitEnumTerm method
        pass

    def visitScore(self, context: str, node: str):
        # TODO: Implement visitScore method
        pass

    def visitEnumLiteral(self, node: str, context: str):
        # TODO: Implement visitEnumLiteral method
        pass

    def visitContext(self, node: str, context: str):
        # TODO: Implement visitContext method
        pass

    def visitPropertyPriority(self, context: str, node: str):
        # TODO: Implement visitPropertyPriority method
        pass

    def visitPriorityRule(self, context: str, node: str):
        # TODO: Implement visitPriorityRule method
        pass

class diva_visitors_Visitor(ABC):

    def __init__(self):
        
    def visitOrTerm(self, node: str, context: str):
        # TODO: Implement visitOrTerm method
        pass

    def visitVariant(self, context: str, node: str):
        # TODO: Implement visitVariant method
        pass

    def visitInvariant(self, context: str, node: str):
        # TODO: Implement visitInvariant method
        pass

    def visitEnumVariable(self, context: str, node: str):
        # TODO: Implement visitEnumVariable method
        pass

    def visitVariabilityModel(self, node: str, context: str):
        # TODO: Implement visitVariabilityModel method
        pass

    def visitConfiguration(self, context: str, node: str):
        # TODO: Implement visitConfiguration method
        pass

    def visitAspectModel(self, context: str, node: str):
        # TODO: Implement visitAspectModel method
        pass

    def visitConfigVariant(self, context: str, node: str):
        # TODO: Implement visitConfigVariant method
        pass

    def visitBooleanVariable(self, node: str, context: str):
        # TODO: Implement visitBooleanVariable method
        pass

    def visitScenario(self, node: str, context: str):
        # TODO: Implement visitScenario method
        pass

    def visitBooleanTerm(self, node: str, context: str):
        # TODO: Implement visitBooleanTerm method
        pass

    def visitPriorityRule(self, context: str, node: str):
        # TODO: Implement visitPriorityRule method
        pass

    def visitExpression(self, node: Expression, context: str):
        # TODO: Implement visitExpression method
        pass

    def visitEnumVariableValue(self, context: str, node: str):
        # TODO: Implement visitEnumVariableValue method
        pass

    def visitContext(self, node: str, context: str):
        # TODO: Implement visitContext method
        pass

    def visitSimulationModel(self, node: str, context: str):
        # TODO: Implement visitSimulationModel method
        pass

    def visitMultiplicityConstraint(self, context: str, node: str):
        # TODO: Implement visitMultiplicityConstraint method
        pass

    def visitPropertyValue(self, node: str, context: str):
        # TODO: Implement visitPropertyValue method
        pass

    def visitPropertyPriority(self, context: str, node: str):
        # TODO: Implement visitPropertyPriority method
        pass

    def visitNotTerm(self, context: str, node: str):
        # TODO: Implement visitNotTerm method
        pass

    def visitContextExpression(self, context: str, node: str):
        # TODO: Implement visitContextExpression method
        pass

    def visitScore(self, node: str, context: str):
        # TODO: Implement visitScore method
        pass

    def visitBaseModel(self, node: str, context: str):
        # TODO: Implement visitBaseModel method
        pass

    def visitAnnotation(self, context: str, node: str):
        # TODO: Implement visitAnnotation method
        pass

    def visitPriority(self, context: str, node: str):
        # TODO: Implement visitPriority method
        pass

    def visitEnumTerm(self, context: str, node: str):
        # TODO: Implement visitEnumTerm method
        pass

    def visitAndTerm(self, context: str, node: str):
        # TODO: Implement visitAndTerm method
        pass

    def visitEnumLiteral(self, node: str, context: str):
        # TODO: Implement visitEnumLiteral method
        pass

    def visitBoolVariableValue(self, node: str, context: str):
        # TODO: Implement visitBoolVariableValue method
        pass

    def visitVariantExpression(self, node: str, context: str):
        # TODO: Implement visitVariantExpression method
        pass

    def visitDimension(self, node: str, context: str):
        # TODO: Implement visitDimension method
        pass

    def visitVariantTerm(self, node: str, context: str):
        # TODO: Implement visitVariantTerm method
        pass

    def visitProperty(self, node: str, context: str):
        # TODO: Implement visitProperty method
        pass

class diva_visitors_Visitable(ABC):

    def __init__(self):
        
    def accept(self, visitor: str, context: str):
        # TODO: Implement accept method
        pass

class VariableValue:

    pass
class diva_EnumVariableValue(VariableValue):

    def __init__(self, diva_EnumVariableValue: "diva_EnumLiteral" = None):
        self.diva_EnumVariableValue = diva_EnumVariableValue
        
    @property
    def diva_EnumVariableValue(self):
        return self.__diva_EnumVariableValue

    @diva_EnumVariableValue.setter
    def diva_EnumVariableValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_EnumVariableValue__diva_EnumVariableValue", None)
        self.__diva_EnumVariableValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_EnumLiteral86"):
                opp_val = getattr(old_value, "diva_EnumLiteral86", None)
                if opp_val == self:
                    setattr(old_value, "diva_EnumLiteral86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_EnumLiteral86"):
                opp_val = getattr(value, "diva_EnumLiteral86", None)
                setattr(value, "diva_EnumLiteral86", self)

    def accept(self, visitor: str, context: str):
        # TODO: Implement accept method
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

    def accept(self, visitor: str, context: str):
        # TODO: Implement accept method
        pass

class ScoredElement:

    pass
class diva_ConfigVariant(ScoredElement):

    def __init__(self, diva_ConfigVariant: "diva_Configuration" = None, diva_ConfigVariant70: "diva_Variant" = None):
        self.diva_ConfigVariant = diva_ConfigVariant
        self.diva_ConfigVariant70 = diva_ConfigVariant70
        
    @property
    def diva_ConfigVariant70(self):
        return self.__diva_ConfigVariant70

    @diva_ConfigVariant70.setter
    def diva_ConfigVariant70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_ConfigVariant__diva_ConfigVariant70", None)
        self.__diva_ConfigVariant70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Variant71"):
                opp_val = getattr(old_value, "diva_Variant71", None)
                if opp_val == self:
                    setattr(old_value, "diva_Variant71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Variant71"):
                opp_val = getattr(value, "diva_Variant71", None)
                setattr(value, "diva_Variant71", self)

    @property
    def diva_ConfigVariant(self):
        return self.__diva_ConfigVariant

    @diva_ConfigVariant.setter
    def diva_ConfigVariant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_ConfigVariant__diva_ConfigVariant", None)
        self.__diva_ConfigVariant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Configuration68"):
                opp_val = getattr(old_value, "diva_Configuration68", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Configuration68"):
                opp_val = getattr(value, "diva_Configuration68", None)
                if opp_val is None:
                    setattr(value, "diva_Configuration68", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def accept(self, visitor: str, context: str):
        # TODO: Implement accept method
        pass

class diva_Configuration(ScoredElement):

    def __init__(self, verdict: str, diva_Configuration: "diva_Context" = None, diva_Configuration68: set["diva_ConfigVariant"] = None):
        self.verdict = verdict
        self.diva_Configuration = diva_Configuration
        self.diva_Configuration68 = diva_Configuration68 if diva_Configuration68 is not None else set()
        
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
                    

    def accept(self, context: str, visitor: str):
        # TODO: Implement accept method
        pass

class Visitable:

    pass
class diva_DiVAModelElement(Visitable):

    pass
class diva_Annotation(Visitable):

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

    def accept(self, context: str, visitor: str):
        # TODO: Implement accept method
        pass

class Expression:

    pass
class Rule:

    pass
class diva_PriorityRule(Rule):

    def __init__(self, diva_PriorityRule: "diva_ContextExpression" = None, diva_PriorityRule46: set["diva_PropertyPriority"] = None):
        self.diva_PriorityRule = diva_PriorityRule
        self.diva_PriorityRule46 = diva_PriorityRule46 if diva_PriorityRule46 is not None else set()
        
    @property
    def diva_PriorityRule46(self):
        return self.__diva_PriorityRule46

    @diva_PriorityRule46.setter
    def diva_PriorityRule46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_PriorityRule__diva_PriorityRule46", None)
        self.__diva_PriorityRule46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diva_PropertyPriority"):
                    opp_val = getattr(item, "diva_PropertyPriority", None)
                    
                    if opp_val == self:
                        setattr(item, "diva_PropertyPriority", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diva_PropertyPriority"):
                    opp_val = getattr(item, "diva_PropertyPriority", None)
                    
                    setattr(item, "diva_PropertyPriority", self)
                    

    @property
    def diva_PriorityRule(self):
        return self.__diva_PriorityRule

    @diva_PriorityRule.setter
    def diva_PriorityRule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_PriorityRule__diva_PriorityRule", None)
        self.__diva_PriorityRule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_ContextExpression44"):
                opp_val = getattr(old_value, "diva_ContextExpression44", None)
                if opp_val == self:
                    setattr(old_value, "diva_ContextExpression44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_ContextExpression44"):
                opp_val = getattr(value, "diva_ContextExpression44", None)
                setattr(value, "diva_ContextExpression44", self)

    def accept(self, context: str, visitor: str):
        # TODO: Implement accept method
        pass

class diva_ContextExpression(Expression):

    def __init__(self, diva_ContextExpression: "diva_Variant" = None, diva_ContextExpression33: "diva_Variant" = None, diva_ContextExpression44: "diva_PriorityRule" = None, diva_ContextExpression55: "diva_MultiplicityConstraint" = None):
        self.diva_ContextExpression = diva_ContextExpression
        self.diva_ContextExpression33 = diva_ContextExpression33
        self.diva_ContextExpression44 = diva_ContextExpression44
        self.diva_ContextExpression55 = diva_ContextExpression55
        
    @property
    def diva_ContextExpression55(self):
        return self.__diva_ContextExpression55

    @diva_ContextExpression55.setter
    def diva_ContextExpression55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_ContextExpression__diva_ContextExpression55", None)
        self.__diva_ContextExpression55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_MultiplicityConstraint54"):
                opp_val = getattr(old_value, "diva_MultiplicityConstraint54", None)
                if opp_val == self:
                    setattr(old_value, "diva_MultiplicityConstraint54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_MultiplicityConstraint54"):
                opp_val = getattr(value, "diva_MultiplicityConstraint54", None)
                setattr(value, "diva_MultiplicityConstraint54", self)

    @property
    def diva_ContextExpression44(self):
        return self.__diva_ContextExpression44

    @diva_ContextExpression44.setter
    def diva_ContextExpression44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_ContextExpression__diva_ContextExpression44", None)
        self.__diva_ContextExpression44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_PriorityRule"):
                opp_val = getattr(old_value, "diva_PriorityRule", None)
                if opp_val == self:
                    setattr(old_value, "diva_PriorityRule", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_PriorityRule"):
                opp_val = getattr(value, "diva_PriorityRule", None)
                setattr(value, "diva_PriorityRule", self)

    @property
    def diva_ContextExpression33(self):
        return self.__diva_ContextExpression33

    @diva_ContextExpression33.setter
    def diva_ContextExpression33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_ContextExpression__diva_ContextExpression33", None)
        self.__diva_ContextExpression33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Variant32"):
                opp_val = getattr(old_value, "diva_Variant32", None)
                if opp_val == self:
                    setattr(old_value, "diva_Variant32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Variant32"):
                opp_val = getattr(value, "diva_Variant32", None)
                setattr(value, "diva_Variant32", self)

    @property
    def diva_ContextExpression(self):
        return self.__diva_ContextExpression

    @diva_ContextExpression.setter
    def diva_ContextExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_ContextExpression__diva_ContextExpression", None)
        self.__diva_ContextExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Variant30"):
                opp_val = getattr(old_value, "diva_Variant30", None)
                if opp_val == self:
                    setattr(old_value, "diva_Variant30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Variant30"):
                opp_val = getattr(value, "diva_Variant30", None)
                setattr(value, "diva_Variant30", self)

    def accept(self, visitor: str, context: str):
        # TODO: Implement accept method
        pass

class diva_VariantExpression(Expression):

    def __init__(self, diva_VariantExpression: "diva_Variant" = None, diva_VariantExpression64: "diva_Context" = None):
        self.diva_VariantExpression = diva_VariantExpression
        self.diva_VariantExpression64 = diva_VariantExpression64
        
    @property
    def diva_VariantExpression(self):
        return self.__diva_VariantExpression

    @diva_VariantExpression.setter
    def diva_VariantExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_VariantExpression__diva_VariantExpression", None)
        self.__diva_VariantExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Variant28"):
                opp_val = getattr(old_value, "diva_Variant28", None)
                if opp_val == self:
                    setattr(old_value, "diva_Variant28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Variant28"):
                opp_val = getattr(value, "diva_Variant28", None)
                setattr(value, "diva_Variant28", self)

    @property
    def diva_VariantExpression64(self):
        return self.__diva_VariantExpression64

    @diva_VariantExpression64.setter
    def diva_VariantExpression64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_VariantExpression__diva_VariantExpression64", None)
        self.__diva_VariantExpression64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Context63"):
                opp_val = getattr(old_value, "diva_Context63", None)
                if opp_val == self:
                    setattr(old_value, "diva_Context63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Context63"):
                opp_val = getattr(value, "diva_Context63", None)
                setattr(value, "diva_Context63", self)

    def accept(self, visitor: str, context: str):
        # TODO: Implement accept method
        pass

class VariableTerm:

    pass
class diva_BooleanTerm(VariableTerm):

    def __init__(self):
        
    def accept(self, context: str, visitor: str):
        # TODO: Implement accept method
        pass

class diva_EnumTerm(VariableTerm):

    def __init__(self, diva_EnumTerm: "diva_EnumLiteral" = None):
        self.diva_EnumTerm = diva_EnumTerm
        
    @property
    def diva_EnumTerm(self):
        return self.__diva_EnumTerm

    @diva_EnumTerm.setter
    def diva_EnumTerm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_EnumTerm__diva_EnumTerm", None)
        self.__diva_EnumTerm = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_EnumLiteral21"):
                opp_val = getattr(old_value, "diva_EnumLiteral21", None)
                if opp_val == self:
                    setattr(old_value, "diva_EnumLiteral21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_EnumLiteral21"):
                opp_val = getattr(value, "diva_EnumLiteral21", None)
                setattr(value, "diva_EnumLiteral21", self)

    def accept(self, visitor: str, context: str):
        # TODO: Implement accept method
        pass

class NaryTerm:

    pass
class diva_AndTerm(NaryTerm):

    def __init__(self):
        
    def accept(self, context: str, visitor: str):
        # TODO: Implement accept method
        pass

class Term:

    pass
class diva_VariantTerm(Term):

    def __init__(self, diva_VariantTerm: "diva_Variant" = None):
        self.diva_VariantTerm = diva_VariantTerm
        
    @property
    def diva_VariantTerm(self):
        return self.__diva_VariantTerm

    @diva_VariantTerm.setter
    def diva_VariantTerm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_VariantTerm__diva_VariantTerm", None)
        self.__diva_VariantTerm = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Variant"):
                opp_val = getattr(old_value, "diva_Variant", None)
                if opp_val == self:
                    setattr(old_value, "diva_Variant", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Variant"):
                opp_val = getattr(value, "diva_Variant", None)
                setattr(value, "diva_Variant", self)

    def accept(self, visitor: str, context: str):
        # TODO: Implement accept method
        pass

class diva_NaryTerm(Term):

    pass
class diva_VariableTerm(Term):

    pass
class diva_NotTerm(Term):

    def __init__(self, diva_NotTerm: "diva_Term" = None):
        self.diva_NotTerm = diva_NotTerm
        
    @property
    def diva_NotTerm(self):
        return self.__diva_NotTerm

    @diva_NotTerm.setter
    def diva_NotTerm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_NotTerm__diva_NotTerm", None)
        self.__diva_NotTerm = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Term"):
                opp_val = getattr(old_value, "diva_Term", None)
                if opp_val == self:
                    setattr(old_value, "diva_Term", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Term"):
                opp_val = getattr(value, "diva_Term", None)
                setattr(value, "diva_Term", self)

    def accept(self, visitor: str, context: str):
        # TODO: Implement accept method
        pass

class diva_OrTerm(NaryTerm):

    def __init__(self):
        
    def accept(self, context: str, visitor: str):
        # TODO: Implement accept method
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

    def accept(self, context: str, visitor: str):
        # TODO: Implement accept method
        pass

class diva_Scenario(NamedElement):

    def __init__(self, diva_Scenario: "diva_SimulationModel" = None, diva_Scenario73: set["diva_Context"] = None):
        self.diva_Scenario = diva_Scenario
        self.diva_Scenario73 = diva_Scenario73 if diva_Scenario73 is not None else set()
        
    @property
    def diva_Scenario73(self):
        return self.__diva_Scenario73

    @diva_Scenario73.setter
    def diva_Scenario73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Scenario__diva_Scenario73", None)
        self.__diva_Scenario73 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diva_Context74"):
                    opp_val = getattr(item, "diva_Context74", None)
                    
                    if opp_val == self:
                        setattr(item, "diva_Context74", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diva_Context74"):
                    opp_val = getattr(item, "diva_Context74", None)
                    
                    setattr(item, "diva_Context74", self)
                    

    @property
    def diva_Scenario(self):
        return self.__diva_Scenario

    @diva_Scenario.setter
    def diva_Scenario(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Scenario__diva_Scenario", None)
        self.__diva_Scenario = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_SimulationModel"):
                opp_val = getattr(old_value, "diva_SimulationModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_SimulationModel"):
                opp_val = getattr(value, "diva_SimulationModel", None)
                if opp_val is None:
                    setattr(value, "diva_SimulationModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def accept(self, context: str, visitor: str):
        # TODO: Implement accept method
        pass

class diva_Variant(NamedElement):

    def __init__(self, diva_Variant: "diva_VariantTerm" = None, diva_Variant23: "diva_AspectModel" = None, variant: "diva_Dimension" = None, diva_Variant26: set["diva_PropertyValue"] = None, diva_Variant28: "diva_VariantExpression" = None, diva_Variant30: "diva_ContextExpression" = None, diva_Variant32: "diva_ContextExpression" = None, Variant: "diva_Dimension" = None, diva_Variant71: "diva_ConfigVariant" = None):
        self.diva_Variant = diva_Variant
        self.diva_Variant23 = diva_Variant23
        self.variant = variant
        self.diva_Variant26 = diva_Variant26 if diva_Variant26 is not None else set()
        self.diva_Variant28 = diva_Variant28
        self.diva_Variant30 = diva_Variant30
        self.diva_Variant32 = diva_Variant32
        self.Variant = Variant
        self.diva_Variant71 = diva_Variant71
        
    @property
    def diva_Variant26(self):
        return self.__diva_Variant26

    @diva_Variant26.setter
    def diva_Variant26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Variant__diva_Variant26", None)
        self.__diva_Variant26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diva_PropertyValue"):
                    opp_val = getattr(item, "diva_PropertyValue", None)
                    
                    if opp_val == self:
                        setattr(item, "diva_PropertyValue", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diva_PropertyValue"):
                    opp_val = getattr(item, "diva_PropertyValue", None)
                    
                    setattr(item, "diva_PropertyValue", self)
                    

    @property
    def diva_Variant71(self):
        return self.__diva_Variant71

    @diva_Variant71.setter
    def diva_Variant71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Variant__diva_Variant71", None)
        self.__diva_Variant71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_ConfigVariant70"):
                opp_val = getattr(old_value, "diva_ConfigVariant70", None)
                if opp_val == self:
                    setattr(old_value, "diva_ConfigVariant70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_ConfigVariant70"):
                opp_val = getattr(value, "diva_ConfigVariant70", None)
                setattr(value, "diva_ConfigVariant70", self)

    @property
    def diva_Variant32(self):
        return self.__diva_Variant32

    @diva_Variant32.setter
    def diva_Variant32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Variant__diva_Variant32", None)
        self.__diva_Variant32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_ContextExpression33"):
                opp_val = getattr(old_value, "diva_ContextExpression33", None)
                if opp_val == self:
                    setattr(old_value, "diva_ContextExpression33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_ContextExpression33"):
                opp_val = getattr(value, "diva_ContextExpression33", None)
                setattr(value, "diva_ContextExpression33", self)

    @property
    def Variant(self):
        return self.__Variant

    @Variant.setter
    def Variant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Variant__Variant", None)
        self.__Variant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "type"):
                opp_val = getattr(old_value, "type", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "type"):
                opp_val = getattr(value, "type", None)
                if opp_val is None:
                    setattr(value, "type", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def diva_Variant28(self):
        return self.__diva_Variant28

    @diva_Variant28.setter
    def diva_Variant28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Variant__diva_Variant28", None)
        self.__diva_Variant28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_VariantExpression"):
                opp_val = getattr(old_value, "diva_VariantExpression", None)
                if opp_val == self:
                    setattr(old_value, "diva_VariantExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_VariantExpression"):
                opp_val = getattr(value, "diva_VariantExpression", None)
                setattr(value, "diva_VariantExpression", self)

    @property
    def diva_Variant30(self):
        return self.__diva_Variant30

    @diva_Variant30.setter
    def diva_Variant30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Variant__diva_Variant30", None)
        self.__diva_Variant30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_ContextExpression"):
                opp_val = getattr(old_value, "diva_ContextExpression", None)
                if opp_val == self:
                    setattr(old_value, "diva_ContextExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_ContextExpression"):
                opp_val = getattr(value, "diva_ContextExpression", None)
                setattr(value, "diva_ContextExpression", self)

    @property
    def diva_Variant23(self):
        return self.__diva_Variant23

    @diva_Variant23.setter
    def diva_Variant23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Variant__diva_Variant23", None)
        self.__diva_Variant23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_AspectModel"):
                opp_val = getattr(old_value, "diva_AspectModel", None)
                if opp_val == self:
                    setattr(old_value, "diva_AspectModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_AspectModel"):
                opp_val = getattr(value, "diva_AspectModel", None)
                setattr(value, "diva_AspectModel", self)

    @property
    def diva_Variant(self):
        return self.__diva_Variant

    @diva_Variant.setter
    def diva_Variant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Variant__diva_Variant", None)
        self.__diva_Variant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_VariantTerm"):
                opp_val = getattr(old_value, "diva_VariantTerm", None)
                if opp_val == self:
                    setattr(old_value, "diva_VariantTerm", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_VariantTerm"):
                opp_val = getattr(value, "diva_VariantTerm", None)
                setattr(value, "diva_VariantTerm", self)

    @property
    def variant(self):
        return self.__variant

    @variant.setter
    def variant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Variant__variant", None)
        self.__variant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Dimension"):
                opp_val = getattr(old_value, "Dimension", None)
                if opp_val == self:
                    setattr(old_value, "Dimension", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Dimension"):
                opp_val = getattr(value, "Dimension", None)
                setattr(value, "Dimension", self)

    def accept(self, visitor: str, context: str):
        # TODO: Implement accept method
        pass

class diva_EnumLiteral(NamedElement):

    def __init__(self, diva_EnumLiteral: "diva_EnumVariable" = None, diva_EnumLiteral21: "diva_EnumTerm" = None, diva_EnumLiteral86: "diva_EnumVariableValue" = None):
        self.diva_EnumLiteral = diva_EnumLiteral
        self.diva_EnumLiteral21 = diva_EnumLiteral21
        self.diva_EnumLiteral86 = diva_EnumLiteral86
        
    @property
    def diva_EnumLiteral(self):
        return self.__diva_EnumLiteral

    @diva_EnumLiteral.setter
    def diva_EnumLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_EnumLiteral__diva_EnumLiteral", None)
        self.__diva_EnumLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_EnumVariable"):
                opp_val = getattr(old_value, "diva_EnumVariable", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_EnumVariable"):
                opp_val = getattr(value, "diva_EnumVariable", None)
                if opp_val is None:
                    setattr(value, "diva_EnumVariable", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def diva_EnumLiteral21(self):
        return self.__diva_EnumLiteral21

    @diva_EnumLiteral21.setter
    def diva_EnumLiteral21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_EnumLiteral__diva_EnumLiteral21", None)
        self.__diva_EnumLiteral21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_EnumTerm"):
                opp_val = getattr(old_value, "diva_EnumTerm", None)
                if opp_val == self:
                    setattr(old_value, "diva_EnumTerm", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_EnumTerm"):
                opp_val = getattr(value, "diva_EnumTerm", None)
                setattr(value, "diva_EnumTerm", self)

    @property
    def diva_EnumLiteral86(self):
        return self.__diva_EnumLiteral86

    @diva_EnumLiteral86.setter
    def diva_EnumLiteral86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_EnumLiteral__diva_EnumLiteral86", None)
        self.__diva_EnumLiteral86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_EnumVariableValue"):
                opp_val = getattr(old_value, "diva_EnumVariableValue", None)
                if opp_val == self:
                    setattr(old_value, "diva_EnumVariableValue", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_EnumVariableValue"):
                opp_val = getattr(value, "diva_EnumVariableValue", None)
                setattr(value, "diva_EnumVariableValue", self)

    def accept(self, visitor: str, context: str):
        # TODO: Implement accept method
        pass

class Variable:

    pass
class diva_BooleanVariable(Variable):

    def __init__(self):
        
    def accept(self, context: str, visitor: str):
        # TODO: Implement accept method
        pass

class diva_EnumVariable(Variable):

    def __init__(self, diva_EnumVariable: set["diva_EnumLiteral"] = None):
        self.diva_EnumVariable = diva_EnumVariable if diva_EnumVariable is not None else set()
        
    @property
    def diva_EnumVariable(self):
        return self.__diva_EnumVariable

    @diva_EnumVariable.setter
    def diva_EnumVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_EnumVariable__diva_EnumVariable", None)
        self.__diva_EnumVariable = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diva_EnumLiteral"):
                    opp_val = getattr(item, "diva_EnumLiteral", None)
                    
                    if opp_val == self:
                        setattr(item, "diva_EnumLiteral", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diva_EnumLiteral"):
                    opp_val = getattr(item, "diva_EnumLiteral", None)
                    
                    setattr(item, "diva_EnumLiteral", self)
                    

    def accept(self, visitor: str, context: str):
        # TODO: Implement accept method
        pass

class Model:

    pass
class diva_AspectModel(Model):

    def __init__(self, diva_AspectModel: "diva_Variant" = None):
        self.diva_AspectModel = diva_AspectModel
        
    @property
    def diva_AspectModel(self):
        return self.__diva_AspectModel

    @diva_AspectModel.setter
    def diva_AspectModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_AspectModel__diva_AspectModel", None)
        self.__diva_AspectModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Variant23"):
                opp_val = getattr(old_value, "diva_Variant23", None)
                if opp_val == self:
                    setattr(old_value, "diva_Variant23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Variant23"):
                opp_val = getattr(value, "diva_Variant23", None)
                setattr(value, "diva_Variant23", self)

    def accept(self, context: str, visitor: str):
        # TODO: Implement accept method
        pass

class Constraint:

    pass
class diva_MultiplicityConstraint(Constraint):

    def __init__(self, upper: str, lower: str, diva_MultiplicityConstraint: "diva_Dimension" = None, diva_MultiplicityConstraint54: "diva_ContextExpression" = None):
        self.upper = upper
        self.lower = lower
        self.diva_MultiplicityConstraint = diva_MultiplicityConstraint
        self.diva_MultiplicityConstraint54 = diva_MultiplicityConstraint54
        
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

    def accept(self, visitor: str, context: str):
        # TODO: Implement accept method
        pass

class diva_Invariant(Constraint):

    def __init__(self, diva_Invariant: "diva_Expression" = None):
        self.diva_Invariant = diva_Invariant
        
    @property
    def diva_Invariant(self):
        return self.__diva_Invariant

    @diva_Invariant.setter
    def diva_Invariant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Invariant__diva_Invariant", None)
        self.__diva_Invariant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Expression"):
                opp_val = getattr(old_value, "diva_Expression", None)
                if opp_val == self:
                    setattr(old_value, "diva_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Expression"):
                opp_val = getattr(value, "diva_Expression", None)
                setattr(value, "diva_Expression", self)

    def accept(self, visitor: str, context: str):
        # TODO: Implement accept method
        pass

class diva_Constraint(NamedElement):

    pass
class diva_Rule(NamedElement):

    pass
class diva_Dimension(NamedElement):

    def __init__(self, upper: str, lower: str, diva_Dimension: "diva_VariabilityModel" = None, Dimension: "diva_Variant" = None, type: set["diva_Variant"] = None, diva_Dimension36: set["diva_Property"] = None, diva_Dimension39: set["diva_MultiplicityConstraint"] = None):
        self.upper = upper
        self.lower = lower
        self.diva_Dimension = diva_Dimension
        self.Dimension = Dimension
        self.type = type if type is not None else set()
        self.diva_Dimension36 = diva_Dimension36 if diva_Dimension36 is not None else set()
        self.diva_Dimension39 = diva_Dimension39 if diva_Dimension39 is not None else set()
        
    @property
    def lower(self) -> str:
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower

    @property
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

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
                    

    def accept(self, context: str, visitor: str):
        # TODO: Implement accept method
        pass

class diva_Property(NamedElement):

    def __init__(self, direction: str, diva_Property: "diva_VariabilityModel" = None, diva_Property37: "diva_Dimension" = None, diva_Property49: "diva_PropertyValue" = None, diva_Property52: "diva_PropertyPriority" = None, diva_Property78: "diva_Score" = None, diva_Property81: "diva_Priority" = None):
        self.direction = direction
        self.diva_Property = diva_Property
        self.diva_Property37 = diva_Property37
        self.diva_Property49 = diva_Property49
        self.diva_Property52 = diva_Property52
        self.diva_Property78 = diva_Property78
        self.diva_Property81 = diva_Property81
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

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

    def accept(self, visitor: str, context: str):
        # TODO: Implement accept method
        pass

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

    def accept(self, visitor: str, context: str):
        # TODO: Implement accept method
        pass

    def weave(self):
        # TODO: Implement weave method
        pass

class DiVAModelElement:

    pass
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

class diva_Score(DiVAModelElement):

    def __init__(self, score: int, diva_Score: "diva_ScoredElement" = None, diva_Score77: "diva_Property" = None):
        self.score = score
        self.diva_Score = diva_Score
        self.diva_Score77 = diva_Score77
        
    @property
    def score(self) -> int:
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

    def accept(self, context: str, visitor: str):
        # TODO: Implement accept method
        pass

class diva_VariableValue(DiVAModelElement):

    pass
class diva_PropertyPriority(DiVAModelElement):

    def __init__(self, priority: str, diva_PropertyPriority: "diva_PriorityRule" = None, diva_PropertyPriority51: "diva_Property" = None):
        self.priority = priority
        self.diva_PropertyPriority = diva_PropertyPriority
        self.diva_PropertyPriority51 = diva_PropertyPriority51
        
    @property
    def priority(self) -> str:
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

    def accept(self, visitor: str, context: str):
        # TODO: Implement accept method
        pass

class diva_Expression(DiVAModelElement):

    def __init__(self, text: str, diva_Expression: "diva_Invariant" = None, diva_Expression41: "diva_Term" = None):
        self.text = text
        self.diva_Expression = diva_Expression
        self.diva_Expression41 = diva_Expression41
        
    @property
    def text(self) -> str:
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

    def accept(self, context: str, visitor: str):
        # TODO: Implement accept method
        pass

class diva_Priority(DiVAModelElement):

    def __init__(self, priority: int, diva_Priority: "diva_Context" = None, diva_Priority80: "diva_Property" = None):
        self.priority = priority
        self.diva_Priority = diva_Priority
        self.diva_Priority80 = diva_Priority80
        
    @property
    def priority(self) -> int:
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority

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

    def accept(self, visitor: str, context: str):
        # TODO: Implement accept method
        pass

class diva_Model(DiVAModelElement):

    pass
class diva_PropertyValue(DiVAModelElement):

    def __init__(self, value: str, diva_PropertyValue: "diva_Variant" = None, diva_PropertyValue48: "diva_Property" = None):
        self.value = value
        self.diva_PropertyValue = diva_PropertyValue
        self.diva_PropertyValue48 = diva_PropertyValue48
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

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

    def accept(self, context: str, visitor: str):
        # TODO: Implement accept method
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
                    

class diva_SimulationModel(DiVAModelElement):

    def __init__(self, SimulationModel: "diva_VariabilityModel" = None, diva_SimulationModel: set["diva_Scenario"] = None, simulation: "diva_VariabilityModel" = None):
        self.SimulationModel = SimulationModel
        self.diva_SimulationModel = diva_SimulationModel if diva_SimulationModel is not None else set()
        self.simulation = simulation
        
    @property
    def SimulationModel(self):
        return self.__SimulationModel

    @SimulationModel.setter
    def SimulationModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_SimulationModel__SimulationModel", None)
        self.__SimulationModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model"):
                opp_val = getattr(old_value, "model", None)
                if opp_val == self:
                    setattr(old_value, "model", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model"):
                opp_val = getattr(value, "model", None)
                setattr(value, "model", self)

    @property
    def diva_SimulationModel(self):
        return self.__diva_SimulationModel

    @diva_SimulationModel.setter
    def diva_SimulationModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_SimulationModel__diva_SimulationModel", None)
        self.__diva_SimulationModel = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diva_Scenario"):
                    opp_val = getattr(item, "diva_Scenario", None)
                    
                    if opp_val == self:
                        setattr(item, "diva_Scenario", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diva_Scenario"):
                    opp_val = getattr(item, "diva_Scenario", None)
                    
                    setattr(item, "diva_Scenario", self)
                    

    @property
    def simulation(self):
        return self.__simulation

    @simulation.setter
    def simulation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_SimulationModel__simulation", None)
        self.__simulation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VariabilityModel"):
                opp_val = getattr(old_value, "VariabilityModel", None)
                if opp_val == self:
                    setattr(old_value, "VariabilityModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VariabilityModel"):
                opp_val = getattr(value, "VariabilityModel", None)
                setattr(value, "VariabilityModel", self)

    def accept(self, context: str, visitor: str):
        # TODO: Implement accept method
        pass

class diva_VariabilityModel(DiVAModelElement):

    def __init__(self, diva_VariabilityModel: "diva_BaseModel" = None, diva_VariabilityModel2: set["diva_Variable"] = None, diva_VariabilityModel4: set["diva_Property"] = None, diva_VariabilityModel6: set["diva_Dimension"] = None, diva_VariabilityModel8: set["diva_Rule"] = None, diva_VariabilityModel10: set["diva_Constraint"] = None, model: "diva_SimulationModel" = None, VariabilityModel: "diva_SimulationModel" = None):
        self.diva_VariabilityModel = diva_VariabilityModel
        self.diva_VariabilityModel2 = diva_VariabilityModel2 if diva_VariabilityModel2 is not None else set()
        self.diva_VariabilityModel4 = diva_VariabilityModel4 if diva_VariabilityModel4 is not None else set()
        self.diva_VariabilityModel6 = diva_VariabilityModel6 if diva_VariabilityModel6 is not None else set()
        self.diva_VariabilityModel8 = diva_VariabilityModel8 if diva_VariabilityModel8 is not None else set()
        self.diva_VariabilityModel10 = diva_VariabilityModel10 if diva_VariabilityModel10 is not None else set()
        self.model = model
        self.VariabilityModel = VariabilityModel
        
    @property
    def diva_VariabilityModel2(self):
        return self.__diva_VariabilityModel2

    @diva_VariabilityModel2.setter
    def diva_VariabilityModel2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_VariabilityModel__diva_VariabilityModel2", None)
        self.__diva_VariabilityModel2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diva_Variable"):
                    opp_val = getattr(item, "diva_Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "diva_Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diva_Variable"):
                    opp_val = getattr(item, "diva_Variable", None)
                    
                    setattr(item, "diva_Variable", self)
                    

    @property
    def diva_VariabilityModel(self):
        return self.__diva_VariabilityModel

    @diva_VariabilityModel.setter
    def diva_VariabilityModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_VariabilityModel__diva_VariabilityModel", None)
        self.__diva_VariabilityModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_BaseModel"):
                opp_val = getattr(old_value, "diva_BaseModel", None)
                if opp_val == self:
                    setattr(old_value, "diva_BaseModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_BaseModel"):
                opp_val = getattr(value, "diva_BaseModel", None)
                setattr(value, "diva_BaseModel", self)

    @property
    def diva_VariabilityModel8(self):
        return self.__diva_VariabilityModel8

    @diva_VariabilityModel8.setter
    def diva_VariabilityModel8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_VariabilityModel__diva_VariabilityModel8", None)
        self.__diva_VariabilityModel8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diva_Rule"):
                    opp_val = getattr(item, "diva_Rule", None)
                    
                    if opp_val == self:
                        setattr(item, "diva_Rule", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diva_Rule"):
                    opp_val = getattr(item, "diva_Rule", None)
                    
                    setattr(item, "diva_Rule", self)
                    

    @property
    def VariabilityModel(self):
        return self.__VariabilityModel

    @VariabilityModel.setter
    def VariabilityModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_VariabilityModel__VariabilityModel", None)
        self.__VariabilityModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "simulation"):
                opp_val = getattr(old_value, "simulation", None)
                if opp_val == self:
                    setattr(old_value, "simulation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "simulation"):
                opp_val = getattr(value, "simulation", None)
                setattr(value, "simulation", self)

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_VariabilityModel__model", None)
        self.__model = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SimulationModel"):
                opp_val = getattr(old_value, "SimulationModel", None)
                if opp_val == self:
                    setattr(old_value, "SimulationModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SimulationModel"):
                opp_val = getattr(value, "SimulationModel", None)
                setattr(value, "SimulationModel", self)

    @property
    def diva_VariabilityModel4(self):
        return self.__diva_VariabilityModel4

    @diva_VariabilityModel4.setter
    def diva_VariabilityModel4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_VariabilityModel__diva_VariabilityModel4", None)
        self.__diva_VariabilityModel4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diva_Property"):
                    opp_val = getattr(item, "diva_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "diva_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diva_Property"):
                    opp_val = getattr(item, "diva_Property", None)
                    
                    setattr(item, "diva_Property", self)
                    

    @property
    def diva_VariabilityModel6(self):
        return self.__diva_VariabilityModel6

    @diva_VariabilityModel6.setter
    def diva_VariabilityModel6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_VariabilityModel__diva_VariabilityModel6", None)
        self.__diva_VariabilityModel6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diva_Dimension"):
                    opp_val = getattr(item, "diva_Dimension", None)
                    
                    if opp_val == self:
                        setattr(item, "diva_Dimension", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diva_Dimension"):
                    opp_val = getattr(item, "diva_Dimension", None)
                    
                    setattr(item, "diva_Dimension", self)
                    

    @property
    def diva_VariabilityModel10(self):
        return self.__diva_VariabilityModel10

    @diva_VariabilityModel10.setter
    def diva_VariabilityModel10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_VariabilityModel__diva_VariabilityModel10", None)
        self.__diva_VariabilityModel10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diva_Constraint"):
                    opp_val = getattr(item, "diva_Constraint", None)
                    
                    if opp_val == self:
                        setattr(item, "diva_Constraint", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diva_Constraint"):
                    opp_val = getattr(item, "diva_Constraint", None)
                    
                    setattr(item, "diva_Constraint", self)
                    

    def accept(self, visitor: str, context: str):
        # TODO: Implement accept method
        pass
