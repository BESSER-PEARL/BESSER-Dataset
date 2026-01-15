from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class diva_DiVAModelElement(ABC):

    pass
class diva_Annotation:

    def __init__(self, key: str, value: str, diva_Annotation: "diva_DiVAModelElement" = None):
        self.key = key
        self.value = value
        self.diva_Annotation = diva_Annotation
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def value(self) -> str:
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
class Expression:

    pass
class diva_ContextExpression(Expression):

    pass
class diva_VariantExpression(Expression):

    pass
class VariableTerm:

    pass
class diva_EnumTerm(VariableTerm):

    pass
class Term:

    pass
class diva_VariantTerm(Term):

    pass
class diva_VariableTerm(Term):

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
class diva_EnumLiteral(NamedElement):

    pass
class diva_Variant(NamedElement):

    pass
class Constraint:

    pass
class diva_MultiplicityConstraint(Constraint):

    def __init__(self, upper: str, lower: str, diva_MultiplicityConstraint: "diva_Dimension" = None, diva_MultiplicityConstraint56: "diva_ContextExpression" = None):
        self.upper = upper
        self.lower = lower
        self.diva_MultiplicityConstraint = diva_MultiplicityConstraint
        self.diva_MultiplicityConstraint56 = diva_MultiplicityConstraint56
        
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
    def diva_MultiplicityConstraint(self):
        return self.__diva_MultiplicityConstraint

    @diva_MultiplicityConstraint.setter
    def diva_MultiplicityConstraint(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_MultiplicityConstraint__diva_MultiplicityConstraint", None)
        self.__diva_MultiplicityConstraint = value
        
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
    def diva_MultiplicityConstraint56(self):
        return self.__diva_MultiplicityConstraint56

    @diva_MultiplicityConstraint56.setter
    def diva_MultiplicityConstraint56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_MultiplicityConstraint__diva_MultiplicityConstraint56", None)
        self.__diva_MultiplicityConstraint56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_ContextExpression57"):
                opp_val = getattr(old_value, "diva_ContextExpression57", None)
                if opp_val == self:
                    setattr(old_value, "diva_ContextExpression57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_ContextExpression57"):
                opp_val = getattr(value, "diva_ContextExpression57", None)
                setattr(value, "diva_ContextExpression57", self)

class diva_Invariant(Constraint):

    pass
class diva_Constraint(NamedElement):

    pass
class diva_Rule(NamedElement):

    pass
class diva_BooleanTerm(VariableTerm):

    pass
class diva_Property(NamedElement):

    def __init__(self, direction: str, diva_Property: "diva_VariabilityModel" = None, diva_Property39: "diva_Dimension" = None, diva_Property51: "diva_PropertyValue" = None, diva_Property54: "diva_PropertyPriority" = None):
        self.direction = direction
        self.diva_Property = diva_Property
        self.diva_Property39 = diva_Property39
        self.diva_Property51 = diva_Property51
        self.diva_Property54 = diva_Property54
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

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
            if hasattr(old_value, "diva_PropertyPriority53"):
                opp_val = getattr(old_value, "diva_PropertyPriority53", None)
                if opp_val == self:
                    setattr(old_value, "diva_PropertyPriority53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_PropertyPriority53"):
                opp_val = getattr(value, "diva_PropertyPriority53", None)
                setattr(value, "diva_PropertyPriority53", self)

    @property
    def diva_Property51(self):
        return self.__diva_Property51

    @diva_Property51.setter
    def diva_Property51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Property__diva_Property51", None)
        self.__diva_Property51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_PropertyValue50"):
                opp_val = getattr(old_value, "diva_PropertyValue50", None)
                if opp_val == self:
                    setattr(old_value, "diva_PropertyValue50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_PropertyValue50"):
                opp_val = getattr(value, "diva_PropertyValue50", None)
                setattr(value, "diva_PropertyValue50", self)

    @property
    def diva_Property39(self):
        return self.__diva_Property39

    @diva_Property39.setter
    def diva_Property39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Property__diva_Property39", None)
        self.__diva_Property39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Dimension38"):
                opp_val = getattr(old_value, "diva_Dimension38", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Dimension38"):
                opp_val = getattr(value, "diva_Dimension38", None)
                if opp_val is None:
                    setattr(value, "diva_Dimension38", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
class diva_PropertyValue(DiVAModelElement):

    def __init__(self, value: str, diva_PropertyValue: "diva_Variant" = None, diva_PropertyValue50: "diva_Property" = None):
        self.value = value
        self.diva_PropertyValue = diva_PropertyValue
        self.diva_PropertyValue50 = diva_PropertyValue50
        
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
    def diva_PropertyValue50(self):
        return self.__diva_PropertyValue50

    @diva_PropertyValue50.setter
    def diva_PropertyValue50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_PropertyValue__diva_PropertyValue50", None)
        self.__diva_PropertyValue50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Property51"):
                opp_val = getattr(old_value, "diva_Property51", None)
                if opp_val == self:
                    setattr(old_value, "diva_Property51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Property51"):
                opp_val = getattr(value, "diva_Property51", None)
                setattr(value, "diva_Property51", self)

class diva_PropertyPriority(DiVAModelElement):

    def __init__(self, priority: str, diva_PropertyPriority: "diva_PriorityRule" = None, diva_PropertyPriority53: "diva_Property" = None):
        self.priority = priority
        self.diva_PropertyPriority = diva_PropertyPriority
        self.diva_PropertyPriority53 = diva_PropertyPriority53
        
    @property
    def priority(self) -> str:
        return self.__priority

    @priority.setter
    def priority(self, priority: str):
        self.__priority = priority

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
            if hasattr(old_value, "diva_PriorityRule48"):
                opp_val = getattr(old_value, "diva_PriorityRule48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_PriorityRule48"):
                opp_val = getattr(value, "diva_PriorityRule48", None)
                if opp_val is None:
                    setattr(value, "diva_PriorityRule48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def diva_PropertyPriority53(self):
        return self.__diva_PropertyPriority53

    @diva_PropertyPriority53.setter
    def diva_PropertyPriority53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_PropertyPriority__diva_PropertyPriority53", None)
        self.__diva_PropertyPriority53 = value
        
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
class diva_Expression(DiVAModelElement):

    def __init__(self, text: str, diva_Expression: "diva_Invariant" = None, diva_Expression43: "diva_Term" = None):
        self.text = text
        self.diva_Expression = diva_Expression
        self.diva_Expression43 = diva_Expression43
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

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

    @property
    def diva_Expression43(self):
        return self.__diva_Expression43

    @diva_Expression43.setter
    def diva_Expression43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Expression__diva_Expression43", None)
        self.__diva_Expression43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Term44"):
                opp_val = getattr(old_value, "diva_Term44", None)
                if opp_val == self:
                    setattr(old_value, "diva_Term44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Term44"):
                opp_val = getattr(value, "diva_Term44", None)
                setattr(value, "diva_Term44", self)

class diva_NamedElement(DiVAModelElement):

    def __init__(self, name: str, id: str):
        self.name = name
        self.id = id
        
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

class diva_Term(DiVAModelElement):

    pass
class diva_VariabilityModel(DiVAModelElement):

    pass
class diva_Dimension(NamedElement):

    def __init__(self, upper: str, lower: str, diva_Dimension: "diva_VariabilityModel" = None, 24: "diva_Variant" = None, 35: set["diva_Variant"] = None, diva_Dimension38: set["diva_Property"] = None, diva_Dimension41: set["diva_MultiplicityConstraint"] = None):
        self.upper = upper
        self.lower = lower
        self.diva_Dimension = diva_Dimension
        self.24 = 24
        self.35 = 35 if 35 is not None else set()
        self.diva_Dimension38 = diva_Dimension38 if diva_Dimension38 is not None else set()
        self.diva_Dimension41 = diva_Dimension41 if diva_Dimension41 is not None else set()
        
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
    def 24(self):
        return self.__24

    @24.setter
    def 24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Dimension__24", None)
        self.__24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, ""):
                opp_val = getattr(old_value, "", None)
                if opp_val == self:
                    setattr(old_value, "", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, ""):
                opp_val = getattr(value, "", None)
                setattr(value, "", self)

    @property
    def 35(self):
        return self.__35

    @35.setter
    def 35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Dimension__35", None)
        self.__35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "36"):
                    opp_val = getattr(item, "36", None)
                    
                    if opp_val == self:
                        setattr(item, "36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "36"):
                    opp_val = getattr(item, "36", None)
                    
                    setattr(item, "36", self)
                    

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
    def diva_Dimension38(self):
        return self.__diva_Dimension38

    @diva_Dimension38.setter
    def diva_Dimension38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Dimension__diva_Dimension38", None)
        self.__diva_Dimension38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diva_Property39"):
                    opp_val = getattr(item, "diva_Property39", None)
                    
                    if opp_val == self:
                        setattr(item, "diva_Property39", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diva_Property39"):
                    opp_val = getattr(item, "diva_Property39", None)
                    
                    setattr(item, "diva_Property39", self)
                    
