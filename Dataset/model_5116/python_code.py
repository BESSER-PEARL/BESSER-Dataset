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

class diva_SuitableConfiguration:

    def __init__(self, score: int, diva_SuitableConfiguration: "diva_ConfigurationModel" = None, diva_SuitableConfiguration87: set["diva_ConfigVariant"] = None):
        self.score = score
        self.diva_SuitableConfiguration = diva_SuitableConfiguration
        self.diva_SuitableConfiguration87 = diva_SuitableConfiguration87 if diva_SuitableConfiguration87 is not None else set()
        
    @property
    def score(self) -> int:
        return self.__score

    @score.setter
    def score(self, score: int):
        self.__score = score

    @property
    def diva_SuitableConfiguration(self):
        return self.__diva_SuitableConfiguration

    @diva_SuitableConfiguration.setter
    def diva_SuitableConfiguration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_SuitableConfiguration__diva_SuitableConfiguration", None)
        self.__diva_SuitableConfiguration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_ConfigurationModel"):
                opp_val = getattr(old_value, "diva_ConfigurationModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_ConfigurationModel"):
                opp_val = getattr(value, "diva_ConfigurationModel", None)
                if opp_val is None:
                    setattr(value, "diva_ConfigurationModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def diva_SuitableConfiguration87(self):
        return self.__diva_SuitableConfiguration87

    @diva_SuitableConfiguration87.setter
    def diva_SuitableConfiguration87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_SuitableConfiguration__diva_SuitableConfiguration87", None)
        self.__diva_SuitableConfiguration87 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diva_ConfigVariant88"):
                    opp_val = getattr(item, "diva_ConfigVariant88", None)
                    
                    if opp_val == self:
                        setattr(item, "diva_ConfigVariant88", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diva_ConfigVariant88"):
                    opp_val = getattr(item, "diva_ConfigVariant88", None)
                    
                    setattr(item, "diva_ConfigVariant88", self)
                    

class diva_ConfigurationModel:

    pass
class diva_ModelContainer(ABC):

    pass
class diva_ContextModel:

    pass
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

class ScoredElement:

    pass
class diva_ConfigVariant(ScoredElement):

    pass
class diva_Configuration(ScoredElement):

    def __init__(self, verdict: str, diva_Configuration66: set["diva_ConfigVariant"] = None, diva_Configuration: "diva_Context" = None):
        self.verdict = verdict
        self.diva_Configuration66 = diva_Configuration66 if diva_Configuration66 is not None else set()
        self.diva_Configuration = diva_Configuration
        
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
            if hasattr(old_value, "diva_Context59"):
                opp_val = getattr(old_value, "diva_Context59", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Context59"):
                opp_val = getattr(value, "diva_Context59", None)
                if opp_val is None:
                    setattr(value, "diva_Context59", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def diva_Configuration66(self):
        return self.__diva_Configuration66

    @diva_Configuration66.setter
    def diva_Configuration66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Configuration__diva_Configuration66", None)
        self.__diva_Configuration66 = value if value is not None else set()
        
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
                    

class Rule:

    pass
class diva_DiVAModelElement(ABC):

    pass
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
class diva_BooleanTerm(VariableTerm):

    pass
class diva_EnumTerm(VariableTerm):

    pass
class Term:

    pass
class diva_NaryTerm(Term):

    pass
class diva_VariantTerm(Term):

    pass
class diva_VariableTerm(Term):

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
class diva_BaseModel(Model):

    def __init__(self):
        
    def weave(self):
        # TODO: Implement weave method
        pass

class DiVAModelElement:

    pass
class diva_VariableValue(DiVAModelElement):

    pass
class diva_Term(DiVAModelElement):

    pass
class diva_SimulationModel(DiVAModelElement):

    pass
class diva_Priority(DiVAModelElement):

    def __init__(self, priority: int, diva_Priority78: "diva_Property" = None, diva_Priority: "diva_Context" = None):
        self.priority = priority
        self.diva_Priority78 = diva_Priority78
        self.diva_Priority = diva_Priority
        
    @property
    def priority(self) -> int:
        return self.__priority

    @priority.setter
    def priority(self, priority: int):
        self.__priority = priority

    @property
    def diva_Priority78(self):
        return self.__diva_Priority78

    @diva_Priority78.setter
    def diva_Priority78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Priority__diva_Priority78", None)
        self.__diva_Priority78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Property79"):
                opp_val = getattr(old_value, "diva_Property79", None)
                if opp_val == self:
                    setattr(old_value, "diva_Property79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Property79"):
                opp_val = getattr(value, "diva_Property79", None)
                setattr(value, "diva_Property79", self)

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
            if hasattr(old_value, "diva_Context64"):
                opp_val = getattr(old_value, "diva_Context64", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Context64"):
                opp_val = getattr(value, "diva_Context64", None)
                if opp_val is None:
                    setattr(value, "diva_Context64", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class diva_PropertyValue(DiVAModelElement):

    def __init__(self, value: str, diva_PropertyValue: "diva_Variant" = None, diva_PropertyValue46: "diva_Property" = None):
        self.value = value
        self.diva_PropertyValue = diva_PropertyValue
        self.diva_PropertyValue46 = diva_PropertyValue46
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def diva_PropertyValue46(self):
        return self.__diva_PropertyValue46

    @diva_PropertyValue46.setter
    def diva_PropertyValue46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_PropertyValue__diva_PropertyValue46", None)
        self.__diva_PropertyValue46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Property47"):
                opp_val = getattr(old_value, "diva_Property47", None)
                if opp_val == self:
                    setattr(old_value, "diva_Property47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Property47"):
                opp_val = getattr(value, "diva_Property47", None)
                setattr(value, "diva_Property47", self)

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
            if hasattr(old_value, "diva_Variant22"):
                opp_val = getattr(old_value, "diva_Variant22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Variant22"):
                opp_val = getattr(value, "diva_Variant22", None)
                if opp_val is None:
                    setattr(value, "diva_Variant22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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

class diva_Score(DiVAModelElement):

    def __init__(self, score: int, diva_Score: "diva_ScoredElement" = None, diva_Score75: "diva_Property" = None):
        self.score = score
        self.diva_Score = diva_Score
        self.diva_Score75 = diva_Score75
        
    @property
    def score(self) -> int:
        return self.__score

    @score.setter
    def score(self, score: int):
        self.__score = score

    @property
    def diva_Score75(self):
        return self.__diva_Score75

    @diva_Score75.setter
    def diva_Score75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Score__diva_Score75", None)
        self.__diva_Score75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Property76"):
                opp_val = getattr(old_value, "diva_Property76", None)
                if opp_val == self:
                    setattr(old_value, "diva_Property76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Property76"):
                opp_val = getattr(value, "diva_Property76", None)
                setattr(value, "diva_Property76", self)

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

class diva_PropertyPriority(DiVAModelElement):

    def __init__(self, priority: str, diva_PropertyPriority49: "diva_Property" = None, diva_PropertyPriority: "diva_PriorityRule" = None):
        self.priority = priority
        self.diva_PropertyPriority49 = diva_PropertyPriority49
        self.diva_PropertyPriority = diva_PropertyPriority
        
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
            if hasattr(old_value, "diva_PriorityRule42"):
                opp_val = getattr(old_value, "diva_PriorityRule42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_PriorityRule42"):
                opp_val = getattr(value, "diva_PriorityRule42", None)
                if opp_val is None:
                    setattr(value, "diva_PriorityRule42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def diva_PropertyPriority49(self):
        return self.__diva_PropertyPriority49

    @diva_PropertyPriority49.setter
    def diva_PropertyPriority49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_PropertyPriority__diva_PropertyPriority49", None)
        self.__diva_PropertyPriority49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Property50"):
                opp_val = getattr(old_value, "diva_Property50", None)
                if opp_val == self:
                    setattr(old_value, "diva_Property50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Property50"):
                opp_val = getattr(value, "diva_Property50", None)
                setattr(value, "diva_Property50", self)

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
                    

class diva_Model(DiVAModelElement):

    def __init__(self, uri: str, diva_Model: "diva_ModelContainer" = None):
        self.uri = uri
        self.diva_Model = diva_Model
        
    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

    @property
    def diva_Model(self):
        return self.__diva_Model

    @diva_Model.setter
    def diva_Model(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Model__diva_Model", None)
        self.__diva_Model = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_ModelContainer"):
                opp_val = getattr(old_value, "diva_ModelContainer", None)
                if opp_val == self:
                    setattr(old_value, "diva_ModelContainer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_ModelContainer"):
                opp_val = getattr(value, "diva_ModelContainer", None)
                setattr(value, "diva_ModelContainer", self)

class NamedElement:

    pass
class diva_Constraint(NamedElement):

    pass
class diva_Scenario(NamedElement):

    pass
class diva_EnumLiteral(NamedElement):

    pass
class diva_Rule(NamedElement):

    pass
class diva_Context(NamedElement):

    def __init__(self, verdict: str, diva_Context: set["diva_VariableValue"] = None, diva_Context72: "diva_Scenario" = None, diva_Context59: set["diva_Configuration"] = None, diva_Context61: "diva_VariantExpression" = None, diva_Context64: set["diva_Priority"] = None):
        self.verdict = verdict
        self.diva_Context = diva_Context if diva_Context is not None else set()
        self.diva_Context72 = diva_Context72
        self.diva_Context59 = diva_Context59 if diva_Context59 is not None else set()
        self.diva_Context61 = diva_Context61
        self.diva_Context64 = diva_Context64 if diva_Context64 is not None else set()
        
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
    def diva_Context59(self):
        return self.__diva_Context59

    @diva_Context59.setter
    def diva_Context59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Context__diva_Context59", None)
        self.__diva_Context59 = value if value is not None else set()
        
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
    def diva_Context72(self):
        return self.__diva_Context72

    @diva_Context72.setter
    def diva_Context72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Context__diva_Context72", None)
        self.__diva_Context72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Scenario71"):
                opp_val = getattr(old_value, "diva_Scenario71", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Scenario71"):
                opp_val = getattr(value, "diva_Scenario71", None)
                if opp_val is None:
                    setattr(value, "diva_Scenario71", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def diva_Context61(self):
        return self.__diva_Context61

    @diva_Context61.setter
    def diva_Context61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Context__diva_Context61", None)
        self.__diva_Context61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_VariantExpression62"):
                opp_val = getattr(old_value, "diva_VariantExpression62", None)
                if opp_val == self:
                    setattr(old_value, "diva_VariantExpression62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_VariantExpression62"):
                opp_val = getattr(value, "diva_VariantExpression62", None)
                setattr(value, "diva_VariantExpression62", self)

    @property
    def diva_Context64(self):
        return self.__diva_Context64

    @diva_Context64.setter
    def diva_Context64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Context__diva_Context64", None)
        self.__diva_Context64 = value if value is not None else set()
        
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
                    

class diva_PropertyLiteral(NamedElement):

    def __init__(self, value: str, diva_PropertyLiteral: "diva_Property" = None):
        self.value = value
        self.diva_PropertyLiteral = diva_PropertyLiteral
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def diva_PropertyLiteral(self):
        return self.__diva_PropertyLiteral

    @diva_PropertyLiteral.setter
    def diva_PropertyLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_PropertyLiteral__diva_PropertyLiteral", None)
        self.__diva_PropertyLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Property44"):
                opp_val = getattr(old_value, "diva_Property44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Property44"):
                opp_val = getattr(value, "diva_Property44", None)
                if opp_val is None:
                    setattr(value, "diva_Property44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class diva_Expression(DiVAModelElement):

    def __init__(self, text: str, diva_Expression: "diva_Invariant" = None, diva_Expression37: "diva_Term" = None):
        self.text = text
        self.diva_Expression = diva_Expression
        self.diva_Expression37 = diva_Expression37
        
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
    def diva_Expression37(self):
        return self.__diva_Expression37

    @diva_Expression37.setter
    def diva_Expression37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Expression__diva_Expression37", None)
        self.__diva_Expression37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Term38"):
                opp_val = getattr(old_value, "diva_Term38", None)
                if opp_val == self:
                    setattr(old_value, "diva_Term38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Term38"):
                opp_val = getattr(value, "diva_Term38", None)
                setattr(value, "diva_Term38", self)

class Constraint:

    pass
class diva_MultiplicityConstraint(Constraint):

    def __init__(self, upper: str, lower: str, diva_MultiplicityConstraint: "diva_Dimension" = None, diva_MultiplicityConstraint52: "diva_ContextExpression" = None):
        self.upper = upper
        self.lower = lower
        self.diva_MultiplicityConstraint = diva_MultiplicityConstraint
        self.diva_MultiplicityConstraint52 = diva_MultiplicityConstraint52
        
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
    def diva_MultiplicityConstraint52(self):
        return self.__diva_MultiplicityConstraint52

    @diva_MultiplicityConstraint52.setter
    def diva_MultiplicityConstraint52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_MultiplicityConstraint__diva_MultiplicityConstraint52", None)
        self.__diva_MultiplicityConstraint52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_ContextExpression53"):
                opp_val = getattr(old_value, "diva_ContextExpression53", None)
                if opp_val == self:
                    setattr(old_value, "diva_ContextExpression53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_ContextExpression53"):
                opp_val = getattr(value, "diva_ContextExpression53", None)
                setattr(value, "diva_ContextExpression53", self)

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

class diva_Invariant(Constraint):

    pass
class diva_Dimension(NamedElement):

    def __init__(self, upper: str, lower: str, diva_Dimension: "diva_VariabilityModel" = None, Dimension: "diva_Variant" = None, type: set["diva_Variant"] = None, diva_Dimension32: set["diva_Property"] = None, diva_Dimension35: set["diva_MultiplicityConstraint"] = None):
        self.upper = upper
        self.lower = lower
        self.diva_Dimension = diva_Dimension
        self.Dimension = Dimension
        self.type = type if type is not None else set()
        self.diva_Dimension32 = diva_Dimension32 if diva_Dimension32 is not None else set()
        self.diva_Dimension35 = diva_Dimension35 if diva_Dimension35 is not None else set()
        
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
    def diva_Dimension(self):
        return self.__diva_Dimension

    @diva_Dimension.setter
    def diva_Dimension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Dimension__diva_Dimension", None)
        self.__diva_Dimension = value
        
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
    def diva_Dimension32(self):
        return self.__diva_Dimension32

    @diva_Dimension32.setter
    def diva_Dimension32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Dimension__diva_Dimension32", None)
        self.__diva_Dimension32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diva_Property33"):
                    opp_val = getattr(item, "diva_Property33", None)
                    
                    if opp_val == self:
                        setattr(item, "diva_Property33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diva_Property33"):
                    opp_val = getattr(item, "diva_Property33", None)
                    
                    setattr(item, "diva_Property33", self)
                    

class diva_Property(NamedElement):

    def __init__(self, direction: str, diva_Property: "diva_VariabilityModel" = None, diva_Property33: "diva_Dimension" = None, diva_Property44: set["diva_PropertyLiteral"] = None, diva_Property47: "diva_PropertyValue" = None, diva_Property50: "diva_PropertyPriority" = None, diva_Property76: "diva_Score" = None, diva_Property79: "diva_Priority" = None):
        self.direction = direction
        self.diva_Property = diva_Property
        self.diva_Property33 = diva_Property33
        self.diva_Property44 = diva_Property44 if diva_Property44 is not None else set()
        self.diva_Property47 = diva_Property47
        self.diva_Property50 = diva_Property50
        self.diva_Property76 = diva_Property76
        self.diva_Property79 = diva_Property79
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def diva_Property33(self):
        return self.__diva_Property33

    @diva_Property33.setter
    def diva_Property33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Property__diva_Property33", None)
        self.__diva_Property33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Dimension32"):
                opp_val = getattr(old_value, "diva_Dimension32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Dimension32"):
                opp_val = getattr(value, "diva_Dimension32", None)
                if opp_val is None:
                    setattr(value, "diva_Dimension32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def diva_Property76(self):
        return self.__diva_Property76

    @diva_Property76.setter
    def diva_Property76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Property__diva_Property76", None)
        self.__diva_Property76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Score75"):
                opp_val = getattr(old_value, "diva_Score75", None)
                if opp_val == self:
                    setattr(old_value, "diva_Score75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Score75"):
                opp_val = getattr(value, "diva_Score75", None)
                setattr(value, "diva_Score75", self)

    @property
    def diva_Property50(self):
        return self.__diva_Property50

    @diva_Property50.setter
    def diva_Property50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Property__diva_Property50", None)
        self.__diva_Property50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_PropertyPriority49"):
                opp_val = getattr(old_value, "diva_PropertyPriority49", None)
                if opp_val == self:
                    setattr(old_value, "diva_PropertyPriority49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_PropertyPriority49"):
                opp_val = getattr(value, "diva_PropertyPriority49", None)
                setattr(value, "diva_PropertyPriority49", self)

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
            if hasattr(old_value, "diva_VariabilityModel2"):
                opp_val = getattr(old_value, "diva_VariabilityModel2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_VariabilityModel2"):
                opp_val = getattr(value, "diva_VariabilityModel2", None)
                if opp_val is None:
                    setattr(value, "diva_VariabilityModel2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def diva_Property47(self):
        return self.__diva_Property47

    @diva_Property47.setter
    def diva_Property47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Property__diva_Property47", None)
        self.__diva_Property47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_PropertyValue46"):
                opp_val = getattr(old_value, "diva_PropertyValue46", None)
                if opp_val == self:
                    setattr(old_value, "diva_PropertyValue46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_PropertyValue46"):
                opp_val = getattr(value, "diva_PropertyValue46", None)
                setattr(value, "diva_PropertyValue46", self)

    @property
    def diva_Property79(self):
        return self.__diva_Property79

    @diva_Property79.setter
    def diva_Property79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Property__diva_Property79", None)
        self.__diva_Property79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_Priority78"):
                opp_val = getattr(old_value, "diva_Priority78", None)
                if opp_val == self:
                    setattr(old_value, "diva_Priority78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_Priority78"):
                opp_val = getattr(value, "diva_Priority78", None)
                setattr(value, "diva_Priority78", self)

    @property
    def diva_Property44(self):
        return self.__diva_Property44

    @diva_Property44.setter
    def diva_Property44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Property__diva_Property44", None)
        self.__diva_Property44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diva_PropertyLiteral"):
                    opp_val = getattr(item, "diva_PropertyLiteral", None)
                    
                    if opp_val == self:
                        setattr(item, "diva_PropertyLiteral", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diva_PropertyLiteral"):
                    opp_val = getattr(item, "diva_PropertyLiteral", None)
                    
                    setattr(item, "diva_PropertyLiteral", self)
                    

class diva_Variable(NamedElement):

    pass
class ModelContainer:

    pass
class diva_Variant(NamedElement, ModelContainer):

    def __init__(self, weaveLevel: str, diva_Variant: "diva_VariantTerm" = None, variant: "diva_Dimension" = None, diva_Variant22: set["diva_PropertyValue"] = None, diva_Variant24: "diva_VariantExpression" = None, diva_Variant26: "diva_ContextExpression" = None, diva_Variant28: "diva_ContextExpression" = None, Variant: "diva_Dimension" = None, diva_Variant69: "diva_ConfigVariant" = None):
        self.weaveLevel = weaveLevel
        self.diva_Variant = diva_Variant
        self.variant = variant
        self.diva_Variant22 = diva_Variant22 if diva_Variant22 is not None else set()
        self.diva_Variant24 = diva_Variant24
        self.diva_Variant26 = diva_Variant26
        self.diva_Variant28 = diva_Variant28
        self.Variant = Variant
        self.diva_Variant69 = diva_Variant69
        
    @property
    def weaveLevel(self) -> str:
        return self.__weaveLevel

    @weaveLevel.setter
    def weaveLevel(self, weaveLevel: str):
        self.__weaveLevel = weaveLevel

    @property
    def diva_Variant69(self):
        return self.__diva_Variant69

    @diva_Variant69.setter
    def diva_Variant69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Variant__diva_Variant69", None)
        self.__diva_Variant69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diva_ConfigVariant68"):
                opp_val = getattr(old_value, "diva_ConfigVariant68", None)
                if opp_val == self:
                    setattr(old_value, "diva_ConfigVariant68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_ConfigVariant68"):
                opp_val = getattr(value, "diva_ConfigVariant68", None)
                setattr(value, "diva_ConfigVariant68", self)

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
    def diva_Variant26(self):
        return self.__diva_Variant26

    @diva_Variant26.setter
    def diva_Variant26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Variant__diva_Variant26", None)
        self.__diva_Variant26 = value
        
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
            if hasattr(old_value, "diva_ContextExpression29"):
                opp_val = getattr(old_value, "diva_ContextExpression29", None)
                if opp_val == self:
                    setattr(old_value, "diva_ContextExpression29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diva_ContextExpression29"):
                opp_val = getattr(value, "diva_ContextExpression29", None)
                setattr(value, "diva_ContextExpression29", self)

    @property
    def diva_Variant22(self):
        return self.__diva_Variant22

    @diva_Variant22.setter
    def diva_Variant22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Variant__diva_Variant22", None)
        self.__diva_Variant22 = value if value is not None else set()
        
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
    def diva_Variant24(self):
        return self.__diva_Variant24

    @diva_Variant24.setter
    def diva_Variant24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diva_Variant__diva_Variant24", None)
        self.__diva_Variant24 = value
        
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

class diva_VariabilityModel(ModelContainer):

    pass