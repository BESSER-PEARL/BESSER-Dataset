from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ChannelSelectorKeyword(Enum):
    ALL = "ALL"
    ANY = "ANY"


############################################
# Definition of Classes
############################################

class Relation:

    pass
class caltrop_ConversionRelation(Relation):

    def __init__(self, valueVar: str, caltrop_ConversionRelation: "caltrop_XExpression" = None, caltrop_ConversionRelation66: "caltrop_XExpression" = None):
        self.valueVar = valueVar
        self.caltrop_ConversionRelation = caltrop_ConversionRelation
        self.caltrop_ConversionRelation66 = caltrop_ConversionRelation66
        
    @property
    def valueVar(self) -> str:
        return self.__valueVar

    @valueVar.setter
    def valueVar(self, valueVar: str):
        self.__valueVar = valueVar

    @property
    def caltrop_ConversionRelation66(self):
        return self.__caltrop_ConversionRelation66

    @caltrop_ConversionRelation66.setter
    def caltrop_ConversionRelation66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caltrop_ConversionRelation__caltrop_ConversionRelation66", None)
        self.__caltrop_ConversionRelation66 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caltrop_XExpression67"):
                opp_val = getattr(old_value, "caltrop_XExpression67", None)
                if opp_val == self:
                    setattr(old_value, "caltrop_XExpression67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caltrop_XExpression67"):
                opp_val = getattr(value, "caltrop_XExpression67", None)
                setattr(value, "caltrop_XExpression67", self)

    @property
    def caltrop_ConversionRelation(self):
        return self.__caltrop_ConversionRelation

    @caltrop_ConversionRelation.setter
    def caltrop_ConversionRelation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caltrop_ConversionRelation__caltrop_ConversionRelation", None)
        self.__caltrop_ConversionRelation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caltrop_XExpression64"):
                opp_val = getattr(old_value, "caltrop_XExpression64", None)
                if opp_val == self:
                    setattr(old_value, "caltrop_XExpression64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caltrop_XExpression64"):
                opp_val = getattr(value, "caltrop_XExpression64", None)
                setattr(value, "caltrop_XExpression64", self)

class ChannelSelector:

    pass
class caltrop_ExpressionChannelSelector(ChannelSelector):

    def __init__(self, many: bool, caltrop_ExpressionChannelSelector: set["caltrop_XExpression"] = None):
        self.many = many
        self.caltrop_ExpressionChannelSelector = caltrop_ExpressionChannelSelector if caltrop_ExpressionChannelSelector is not None else set()
        
    @property
    def many(self) -> bool:
        return self.__many

    @many.setter
    def many(self, many: bool):
        self.__many = many

    @property
    def caltrop_ExpressionChannelSelector(self):
        return self.__caltrop_ExpressionChannelSelector

    @caltrop_ExpressionChannelSelector.setter
    def caltrop_ExpressionChannelSelector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caltrop_ExpressionChannelSelector__caltrop_ExpressionChannelSelector", None)
        self.__caltrop_ExpressionChannelSelector = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "caltrop_XExpression36"):
                    opp_val = getattr(item, "caltrop_XExpression36", None)
                    
                    if opp_val == self:
                        setattr(item, "caltrop_XExpression36", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "caltrop_XExpression36"):
                    opp_val = getattr(item, "caltrop_XExpression36", None)
                    
                    setattr(item, "caltrop_XExpression36", self)
                    

class caltrop_Transition:

    def __init__(self, tags: str, Transition: "caltrop_State" = None, caltrop_Transition: "caltrop_State" = None, transitions: "caltrop_State" = None):
        self.tags = tags
        self.Transition = Transition
        self.caltrop_Transition = caltrop_Transition
        self.transitions = transitions
        
    @property
    def tags(self) -> str:
        return self.__tags

    @tags.setter
    def tags(self, tags: str):
        self.__tags = tags

    @property
    def caltrop_Transition(self):
        return self.__caltrop_Transition

    @caltrop_Transition.setter
    def caltrop_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caltrop_Transition__caltrop_Transition", None)
        self.__caltrop_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caltrop_State52"):
                opp_val = getattr(old_value, "caltrop_State52", None)
                if opp_val == self:
                    setattr(old_value, "caltrop_State52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caltrop_State52"):
                opp_val = getattr(value, "caltrop_State52", None)
                setattr(value, "caltrop_State52", self)

    @property
    def transitions(self):
        return self.__transitions

    @transitions.setter
    def transitions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caltrop_Transition__transitions", None)
        self.__transitions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "State50"):
                opp_val = getattr(old_value, "State50", None)
                if opp_val == self:
                    setattr(old_value, "State50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "State50"):
                opp_val = getattr(value, "State50", None)
                setattr(value, "State50", self)

    @property
    def Transition(self):
        return self.__Transition

    @Transition.setter
    def Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caltrop_Transition__Transition", None)
        self.__Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "source"):
                opp_val = getattr(old_value, "source", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "source"):
                opp_val = getattr(value, "source", None)
                if opp_val is None:
                    setattr(value, "source", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class caltrop_JvmTypeReference:

    pass
class caltrop_JvmTypedObj:

    pass
class JvmTypedObj:

    pass
class caltrop_KeywordChannelSelector(ChannelSelector):

    def __init__(self, keyword: str):
        self.keyword = keyword
        
    @property
    def keyword(self) -> str:
        return self.__keyword

    @keyword.setter
    def keyword(self, keyword: str):
        self.__keyword = keyword

class caltrop_XExpression:

    pass
class ActionPattern:

    pass
class caltrop_EventPattern(ActionPattern):

    def __init__(self, name: str, qualifier: str, variables: str, property: bool, caltrop_EventPattern: "caltrop_EventAction" = None, caltrop_EventPattern55: "caltrop_StateVariable" = None, caltrop_EventPattern58: "caltrop_XExpression" = None, caltrop_EventPattern61: "caltrop_XExpression" = None):
        self.name = name
        self.qualifier = qualifier
        self.variables = variables
        self.property = property
        self.caltrop_EventPattern = caltrop_EventPattern
        self.caltrop_EventPattern55 = caltrop_EventPattern55
        self.caltrop_EventPattern58 = caltrop_EventPattern58
        self.caltrop_EventPattern61 = caltrop_EventPattern61
        
    @property
    def variables(self) -> str:
        return self.__variables

    @variables.setter
    def variables(self, variables: str):
        self.__variables = variables

    @property
    def property(self) -> bool:
        return self.__property

    @property.setter
    def property(self, property: bool):
        self.__property = property

    @property
    def qualifier(self) -> str:
        return self.__qualifier

    @qualifier.setter
    def qualifier(self, qualifier: str):
        self.__qualifier = qualifier

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def caltrop_EventPattern61(self):
        return self.__caltrop_EventPattern61

    @caltrop_EventPattern61.setter
    def caltrop_EventPattern61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caltrop_EventPattern__caltrop_EventPattern61", None)
        self.__caltrop_EventPattern61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caltrop_XExpression62"):
                opp_val = getattr(old_value, "caltrop_XExpression62", None)
                if opp_val == self:
                    setattr(old_value, "caltrop_XExpression62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caltrop_XExpression62"):
                opp_val = getattr(value, "caltrop_XExpression62", None)
                setattr(value, "caltrop_XExpression62", self)

    @property
    def caltrop_EventPattern58(self):
        return self.__caltrop_EventPattern58

    @caltrop_EventPattern58.setter
    def caltrop_EventPattern58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caltrop_EventPattern__caltrop_EventPattern58", None)
        self.__caltrop_EventPattern58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caltrop_XExpression59"):
                opp_val = getattr(old_value, "caltrop_XExpression59", None)
                if opp_val == self:
                    setattr(old_value, "caltrop_XExpression59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caltrop_XExpression59"):
                opp_val = getattr(value, "caltrop_XExpression59", None)
                setattr(value, "caltrop_XExpression59", self)

    @property
    def caltrop_EventPattern(self):
        return self.__caltrop_EventPattern

    @caltrop_EventPattern.setter
    def caltrop_EventPattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caltrop_EventPattern__caltrop_EventPattern", None)
        self.__caltrop_EventPattern = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caltrop_EventAction"):
                opp_val = getattr(old_value, "caltrop_EventAction", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caltrop_EventAction"):
                opp_val = getattr(value, "caltrop_EventAction", None)
                if opp_val is None:
                    setattr(value, "caltrop_EventAction", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def caltrop_EventPattern55(self):
        return self.__caltrop_EventPattern55

    @caltrop_EventPattern55.setter
    def caltrop_EventPattern55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caltrop_EventPattern__caltrop_EventPattern55", None)
        self.__caltrop_EventPattern55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caltrop_StateVariable56"):
                opp_val = getattr(old_value, "caltrop_StateVariable56", None)
                if opp_val == self:
                    setattr(old_value, "caltrop_StateVariable56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caltrop_StateVariable56"):
                opp_val = getattr(value, "caltrop_StateVariable56", None)
                setattr(value, "caltrop_StateVariable56", self)

class PortPattern:

    pass
class caltrop_ActionPattern:

    def __init__(self):
        
    def getPatternVariables(self) -> str:
        # TODO: Implement getPatternVariables method
        pass

    def getGuardExpression(self) -> str:
        # TODO: Implement getGuardExpression method
        pass

class caltrop_Port:

    pass
class caltrop_ChannelSelector(ABC):

    pass
class caltrop_PortPattern(ABC):

    def __init__(self, caltrop_PortPattern: "caltrop_XExpression" = None, caltrop_PortPattern26: "caltrop_ChannelSelector" = None, caltrop_PortPattern28: "caltrop_Port" = None, caltrop_PortPattern30: "caltrop_XExpression" = None):
        self.caltrop_PortPattern = caltrop_PortPattern
        self.caltrop_PortPattern26 = caltrop_PortPattern26
        self.caltrop_PortPattern28 = caltrop_PortPattern28
        self.caltrop_PortPattern30 = caltrop_PortPattern30
        
    @property
    def caltrop_PortPattern28(self):
        return self.__caltrop_PortPattern28

    @caltrop_PortPattern28.setter
    def caltrop_PortPattern28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caltrop_PortPattern__caltrop_PortPattern28", None)
        self.__caltrop_PortPattern28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caltrop_Port"):
                opp_val = getattr(old_value, "caltrop_Port", None)
                if opp_val == self:
                    setattr(old_value, "caltrop_Port", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caltrop_Port"):
                opp_val = getattr(value, "caltrop_Port", None)
                setattr(value, "caltrop_Port", self)

    @property
    def caltrop_PortPattern(self):
        return self.__caltrop_PortPattern

    @caltrop_PortPattern.setter
    def caltrop_PortPattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caltrop_PortPattern__caltrop_PortPattern", None)
        self.__caltrop_PortPattern = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caltrop_XExpression24"):
                opp_val = getattr(old_value, "caltrop_XExpression24", None)
                if opp_val == self:
                    setattr(old_value, "caltrop_XExpression24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caltrop_XExpression24"):
                opp_val = getattr(value, "caltrop_XExpression24", None)
                setattr(value, "caltrop_XExpression24", self)

    @property
    def caltrop_PortPattern26(self):
        return self.__caltrop_PortPattern26

    @caltrop_PortPattern26.setter
    def caltrop_PortPattern26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caltrop_PortPattern__caltrop_PortPattern26", None)
        self.__caltrop_PortPattern26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caltrop_ChannelSelector"):
                opp_val = getattr(old_value, "caltrop_ChannelSelector", None)
                if opp_val == self:
                    setattr(old_value, "caltrop_ChannelSelector", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caltrop_ChannelSelector"):
                opp_val = getattr(value, "caltrop_ChannelSelector", None)
                setattr(value, "caltrop_ChannelSelector", self)

    @property
    def caltrop_PortPattern30(self):
        return self.__caltrop_PortPattern30

    @caltrop_PortPattern30.setter
    def caltrop_PortPattern30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caltrop_PortPattern__caltrop_PortPattern30", None)
        self.__caltrop_PortPattern30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caltrop_XExpression31"):
                opp_val = getattr(old_value, "caltrop_XExpression31", None)
                if opp_val == self:
                    setattr(old_value, "caltrop_XExpression31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caltrop_XExpression31"):
                opp_val = getattr(value, "caltrop_XExpression31", None)
                setattr(value, "caltrop_XExpression31", self)

    def size(self) -> int:
        # TODO: Implement size method
        pass

class caltrop_OutputPattern(PortPattern):

    pass
class NamedObj:

    pass
class caltrop_State(NamedObj):

    pass
class OutputAction:

    pass
class caltrop_InputPattern(PortPattern, ActionPattern):

    def __init__(self, variables: str, caltrop_InputPattern: "caltrop_FireAction" = None):
        self.variables = variables
        self.caltrop_InputPattern = caltrop_InputPattern
        
    @property
    def variables(self) -> str:
        return self.__variables

    @variables.setter
    def variables(self, variables: str):
        self.__variables = variables

    @property
    def caltrop_InputPattern(self):
        return self.__caltrop_InputPattern

    @caltrop_InputPattern.setter
    def caltrop_InputPattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caltrop_InputPattern__caltrop_InputPattern", None)
        self.__caltrop_InputPattern = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caltrop_FireAction"):
                opp_val = getattr(old_value, "caltrop_FireAction", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caltrop_FireAction"):
                opp_val = getattr(value, "caltrop_FireAction", None)
                if opp_val is None:
                    setattr(value, "caltrop_FireAction", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ReAction:

    pass
class caltrop_EventAction(ReAction):

    pass
class caltrop_FireAction(ReAction):

    pass
class Variable:

    pass
class caltrop_StateVariable(Variable):

    def __init__(self, constant: bool, caltrop_StateVariable: "caltrop_CaltropActorImpl" = None, caltrop_StateVariable56: "caltrop_EventPattern" = None):
        self.constant = constant
        self.caltrop_StateVariable = caltrop_StateVariable
        self.caltrop_StateVariable56 = caltrop_StateVariable56
        
    @property
    def constant(self) -> bool:
        return self.__constant

    @constant.setter
    def constant(self, constant: bool):
        self.__constant = constant

    @property
    def caltrop_StateVariable56(self):
        return self.__caltrop_StateVariable56

    @caltrop_StateVariable56.setter
    def caltrop_StateVariable56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caltrop_StateVariable__caltrop_StateVariable56", None)
        self.__caltrop_StateVariable56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caltrop_EventPattern55"):
                opp_val = getattr(old_value, "caltrop_EventPattern55", None)
                if opp_val == self:
                    setattr(old_value, "caltrop_EventPattern55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caltrop_EventPattern55"):
                opp_val = getattr(value, "caltrop_EventPattern55", None)
                setattr(value, "caltrop_EventPattern55", self)

    @property
    def caltrop_StateVariable(self):
        return self.__caltrop_StateVariable

    @caltrop_StateVariable.setter
    def caltrop_StateVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caltrop_StateVariable__caltrop_StateVariable", None)
        self.__caltrop_StateVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caltrop_CaltropActorImpl"):
                opp_val = getattr(old_value, "caltrop_CaltropActorImpl", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caltrop_CaltropActorImpl"):
                opp_val = getattr(value, "caltrop_CaltropActorImpl", None)
                if opp_val is None:
                    setattr(value, "caltrop_CaltropActorImpl", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class AbstractTypedIOPort:

    pass
class caltrop_TypedOutputPort(AbstractTypedIOPort):

    pass
class caltrop_TypedInputPort(AbstractTypedIOPort):

    pass
class Parameter:

    pass
class caltrop_ActorParameter(Parameter):

    pass
class caltrop_Schedule:

    pass
class caltrop_FunctionDeclaration(JvmTypedObj):

    pass
class caltrop_OutputAction(NamedObj):

    def __init__(self, caltrop_OutputAction: "caltrop_CaltropActorImpl" = None, caltrop_OutputAction13: set["caltrop_OutputPattern"] = None, caltrop_OutputAction15: "caltrop_XExpression" = None, caltrop_OutputAction18: "caltrop_XExpression" = None, caltrop_OutputAction21: "caltrop_XExpression" = None, caltrop_OutputAction11: "caltrop_XExpression" = None):
        self.caltrop_OutputAction = caltrop_OutputAction
        self.caltrop_OutputAction13 = caltrop_OutputAction13 if caltrop_OutputAction13 is not None else set()
        self.caltrop_OutputAction15 = caltrop_OutputAction15
        self.caltrop_OutputAction18 = caltrop_OutputAction18
        self.caltrop_OutputAction21 = caltrop_OutputAction21
        self.caltrop_OutputAction11 = caltrop_OutputAction11
        
    @property
    def caltrop_OutputAction(self):
        return self.__caltrop_OutputAction

    @caltrop_OutputAction.setter
    def caltrop_OutputAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caltrop_OutputAction__caltrop_OutputAction", None)
        self.__caltrop_OutputAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caltrop_CaltropActorImpl4"):
                opp_val = getattr(old_value, "caltrop_CaltropActorImpl4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caltrop_CaltropActorImpl4"):
                opp_val = getattr(value, "caltrop_CaltropActorImpl4", None)
                if opp_val is None:
                    setattr(value, "caltrop_CaltropActorImpl4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def caltrop_OutputAction11(self):
        return self.__caltrop_OutputAction11

    @caltrop_OutputAction11.setter
    def caltrop_OutputAction11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caltrop_OutputAction__caltrop_OutputAction11", None)
        self.__caltrop_OutputAction11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caltrop_XExpression"):
                opp_val = getattr(old_value, "caltrop_XExpression", None)
                if opp_val == self:
                    setattr(old_value, "caltrop_XExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caltrop_XExpression"):
                opp_val = getattr(value, "caltrop_XExpression", None)
                setattr(value, "caltrop_XExpression", self)

    @property
    def caltrop_OutputAction21(self):
        return self.__caltrop_OutputAction21

    @caltrop_OutputAction21.setter
    def caltrop_OutputAction21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caltrop_OutputAction__caltrop_OutputAction21", None)
        self.__caltrop_OutputAction21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caltrop_XExpression22"):
                opp_val = getattr(old_value, "caltrop_XExpression22", None)
                if opp_val == self:
                    setattr(old_value, "caltrop_XExpression22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caltrop_XExpression22"):
                opp_val = getattr(value, "caltrop_XExpression22", None)
                setattr(value, "caltrop_XExpression22", self)

    @property
    def caltrop_OutputAction15(self):
        return self.__caltrop_OutputAction15

    @caltrop_OutputAction15.setter
    def caltrop_OutputAction15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caltrop_OutputAction__caltrop_OutputAction15", None)
        self.__caltrop_OutputAction15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caltrop_XExpression16"):
                opp_val = getattr(old_value, "caltrop_XExpression16", None)
                if opp_val == self:
                    setattr(old_value, "caltrop_XExpression16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caltrop_XExpression16"):
                opp_val = getattr(value, "caltrop_XExpression16", None)
                setattr(value, "caltrop_XExpression16", self)

    @property
    def caltrop_OutputAction18(self):
        return self.__caltrop_OutputAction18

    @caltrop_OutputAction18.setter
    def caltrop_OutputAction18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caltrop_OutputAction__caltrop_OutputAction18", None)
        self.__caltrop_OutputAction18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caltrop_XExpression19"):
                opp_val = getattr(old_value, "caltrop_XExpression19", None)
                if opp_val == self:
                    setattr(old_value, "caltrop_XExpression19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caltrop_XExpression19"):
                opp_val = getattr(value, "caltrop_XExpression19", None)
                setattr(value, "caltrop_XExpression19", self)

    @property
    def caltrop_OutputAction13(self):
        return self.__caltrop_OutputAction13

    @caltrop_OutputAction13.setter
    def caltrop_OutputAction13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caltrop_OutputAction__caltrop_OutputAction13", None)
        self.__caltrop_OutputAction13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "caltrop_OutputPattern"):
                    opp_val = getattr(item, "caltrop_OutputPattern", None)
                    
                    if opp_val == self:
                        setattr(item, "caltrop_OutputPattern", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "caltrop_OutputPattern"):
                    opp_val = getattr(item, "caltrop_OutputPattern", None)
                    
                    setattr(item, "caltrop_OutputPattern", self)
                    

    def getInputPatterns(self) -> str:
        # TODO: Implement getInputPatterns method
        pass

class caltrop_ReAction(OutputAction):

    pass
class caltrop_CaltropActorImpl:

    pass