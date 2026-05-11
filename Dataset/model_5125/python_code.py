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
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def key(self):
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
class diva_VariantExpression(Expression):

    pass
class diva_ContextExpression(Expression):

    pass
class Term:

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
class VariableTerm:

    pass
class diva_BooleanTerm(VariableTerm):

    pass
class diva_EnumTerm(VariableTerm):

    pass
class diva_VariableTerm(Term):

    pass
class diva_Variant(NamedElement):

    pass
class diva_VariantTerm(Term):

    pass
class diva_NaryTerm(Term):

    pass
class DiVAModelElement:

    pass
class diva_PropertyValue(DiVAModelElement):

    def __init__(self, value: str, diva_PropertyValue: "diva_Variant" = None, diva_PropertyValue47: "diva_Property" = None):
        self.value = value
        self.diva_PropertyValue = diva_PropertyValue
        self.diva_PropertyValue47 = diva_PropertyValue47
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def diva_PropertyValue47(self):
        return self.__diva_PropertyValue47

    @diva_PropertyValue47.setter
    def diva_PropertyValue47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_PropertyValue__diva_PropertyValue47", None)
        self.__diva_PropertyValue47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Property48"):
                opp_val = getattr(old_value, "diva_Property48", None)
                if opp_val == self:
                    setattr(old_value, "diva_Property48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Property48"):
                opp_val = getattr(value, "diva_Property48", None)
                setattr(value, "diva_Property48", self)

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
            if hasattr(old_value, "diva_Variant25"):
                opp_val = getattr(old_value, "diva_Variant25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Variant25"):
                opp_val = getattr(value, "diva_Variant25", None)
                if opp_val is None:
                    setattr(value, "diva_Variant25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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


class diva_PropertyPriority(DiVAModelElement):

    def __init__(self, priority: str, diva_PropertyPriority: "diva_PriorityRule" = None, diva_PropertyPriority50: "diva_Property" = None):
        self.priority = priority
        self.diva_PropertyPriority = diva_PropertyPriority
        self.diva_PropertyPriority50 = diva_PropertyPriority50
        
        pass
    @property
    def priority(self):
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
            if hasattr(old_value, "diva_PriorityRule45"):
                opp_val = getattr(old_value, "diva_PriorityRule45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_PriorityRule45"):
                opp_val = getattr(value, "diva_PriorityRule45", None)
                if opp_val is None:
                    setattr(value, "diva_PriorityRule45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def diva_PropertyPriority50(self):
        return self.__diva_PropertyPriority50

    @diva_PropertyPriority50.setter
    def diva_PropertyPriority50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_PropertyPriority__diva_PropertyPriority50", None)
        self.__diva_PropertyPriority50 = value
        
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

class diva_Model(DiVAModelElement):

    pass
class diva_Term(DiVAModelElement):

    pass
class diva_VariabilityModel(DiVAModelElement):

    pass
class diva_Expression(DiVAModelElement):

    def __init__(self, text: str, diva_Expression40: "diva_Term" = None, diva_Expression: "diva_Invariant" = None):
        self.text = text
        self.diva_Expression40 = diva_Expression40
        self.diva_Expression = diva_Expression
        
        pass
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text


    @property
    def diva_Expression40(self):
        return self.__diva_Expression40

    @diva_Expression40.setter
    def diva_Expression40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Expression__diva_Expression40", None)
        self.__diva_Expression40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Term41"):
                opp_val = getattr(old_value, "diva_Term41", None)
                if opp_val == self:
                    setattr(old_value, "diva_Term41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Term41"):
                opp_val = getattr(value, "diva_Term41", None)
                setattr(value, "diva_Term41", self)

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

class Constraint:

    pass
class diva_MultiplicityConstraint(Constraint):

    def __init__(self, upper: str, lower: str, diva_MultiplicityConstraint: "diva_Dimension" = None, diva_MultiplicityConstraint53: "diva_ContextExpression" = None):
        self.upper = upper
        self.lower = lower
        self.diva_MultiplicityConstraint = diva_MultiplicityConstraint
        self.diva_MultiplicityConstraint53 = diva_MultiplicityConstraint53
        
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

    @property
    def diva_MultiplicityConstraint53(self):
        return self.__diva_MultiplicityConstraint53

    @diva_MultiplicityConstraint53.setter
    def diva_MultiplicityConstraint53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_MultiplicityConstraint__diva_MultiplicityConstraint53", None)
        self.__diva_MultiplicityConstraint53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_ContextExpression54"):
                opp_val = getattr(old_value, "diva_ContextExpression54", None)
                if opp_val == self:
                    setattr(old_value, "diva_ContextExpression54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_ContextExpression54"):
                opp_val = getattr(value, "diva_ContextExpression54", None)
                setattr(value, "diva_ContextExpression54", self)

class diva_Invariant(Constraint):

    pass
class diva_Constraint(NamedElement):

    pass
class diva_Rule(NamedElement):

    pass
class diva_Dimension(NamedElement):

    def __init__(self, upper: str, lower: str, diva_Dimension: "diva_VariabilityModel" = None, diva_Dimension35: set["diva_Property"] = None, diva_Dimension38: set["diva_MultiplicityConstraint"] = None, Dimension: "diva_Variant" = None, type: set["diva_Variant"] = None):
        self.upper = upper
        self.lower = lower
        self.diva_Dimension = diva_Dimension
        self.diva_Dimension35 = diva_Dimension35 if diva_Dimension35 is not None else set()
        self.diva_Dimension38 = diva_Dimension38 if diva_Dimension38 is not None else set()
        self.Dimension = Dimension
        self.type = type if type is not None else set()
        
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
    def diva_Dimension35(self):
        return self.__diva_Dimension35

    @diva_Dimension35.setter
    def diva_Dimension35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Dimension__diva_Dimension35", None)
        self.__diva_Dimension35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diva_Property36"):
                    opp_val = getattr(item, "diva_Property36", None)
                    
                    if opp_val == self:
                        setattr(item, "diva_Property36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diva_Property36"):
                    opp_val = getattr(item, "diva_Property36", None)
                    
                    setattr(item, "diva_Property36", self)
                    

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
                    

class diva_Property(NamedElement):

    def __init__(self, direction: str, diva_Property: "diva_VariabilityModel" = None, diva_Property36: "diva_Dimension" = None, diva_Property48: "diva_PropertyValue" = None, diva_Property51: "diva_PropertyPriority" = None):
        self.direction = direction
        self.diva_Property = diva_Property
        self.diva_Property36 = diva_Property36
        self.diva_Property48 = diva_Property48
        self.diva_Property51 = diva_Property51
        
        pass
    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction


    @property
    def diva_Property36(self):
        return self.__diva_Property36

    @diva_Property36.setter
    def diva_Property36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Property__diva_Property36", None)
        self.__diva_Property36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Dimension35"):
                opp_val = getattr(old_value, "diva_Dimension35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Dimension35"):
                opp_val = getattr(value, "diva_Dimension35", None)
                if opp_val is None:
                    setattr(value, "diva_Dimension35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def diva_Property48(self):
        return self.__diva_Property48

    @diva_Property48.setter
    def diva_Property48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Property__diva_Property48", None)
        self.__diva_Property48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_PropertyValue47"):
                opp_val = getattr(old_value, "diva_PropertyValue47", None)
                if opp_val == self:
                    setattr(old_value, "diva_PropertyValue47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_PropertyValue47"):
                opp_val = getattr(value, "diva_PropertyValue47", None)
                setattr(value, "diva_PropertyValue47", self)

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
            if hasattr(old_value, "diva_PropertyPriority50"):
                opp_val = getattr(old_value, "diva_PropertyPriority50", None)
                if opp_val == self:
                    setattr(old_value, "diva_PropertyPriority50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_PropertyPriority50"):
                opp_val = getattr(value, "diva_PropertyPriority50", None)
                setattr(value, "diva_PropertyPriority50", self)

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
