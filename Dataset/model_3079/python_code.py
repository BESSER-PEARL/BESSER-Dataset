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

    def __init__(self, valueVar: str, caltrop_ConversionRelation: "caltrop_XExpression" = None, caltrop_ConversionRelation74: "caltrop_XExpression" = None):
        self.valueVar = valueVar
        self.caltrop_ConversionRelation = caltrop_ConversionRelation
        self.caltrop_ConversionRelation74 = caltrop_ConversionRelation74
        
    @property
    def valueVar(self) -> str:
        return self.__valueVar

    @valueVar.setter
    def valueVar(self, valueVar: str):
        self.__valueVar = valueVar

    @property
    def caltrop_ConversionRelation74(self):
        return self.__caltrop_ConversionRelation74

    @caltrop_ConversionRelation74.setter
    def caltrop_ConversionRelation74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caltrop_ConversionRelation__caltrop_ConversionRelation74", None)
        self.__caltrop_ConversionRelation74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caltrop_XExpression75"):
                opp_val = getattr(old_value, "caltrop_XExpression75", None)
                if opp_val == self:
                    setattr(old_value, "caltrop_XExpression75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caltrop_XExpression75"):
                opp_val = getattr(value, "caltrop_XExpression75", None)
                setattr(value, "caltrop_XExpression75", self)

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
            if hasattr(old_value, "caltrop_XExpression72"):
                opp_val = getattr(old_value, "caltrop_XExpression72", None)
                if opp_val == self:
                    setattr(old_value, "caltrop_XExpression72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caltrop_XExpression72"):
                opp_val = getattr(value, "caltrop_XExpression72", None)
                setattr(value, "caltrop_XExpression72", self)

class caltrop_JvmTypedObj:

    pass
class JvmTypedObj:

    pass
class caltrop_Transition:

    pass
class caltrop_JvmTypeReference:

    pass
class PortPattern:

    pass
class caltrop_ActionPattern:

    def __init__(self):
        
    def getGuardExpression(self) -> str:
        # TODO: Implement getGuardExpression method
        pass

    def getPatternVariables(self) -> str:
        # TODO: Implement getPatternVariables method
        pass

class caltrop_Port:

    pass
class caltrop_ChannelSelector(ABC):

    pass
class ChannelSelector:

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
                if hasattr(item, "caltrop_XExpression41"):
                    opp_val = getattr(item, "caltrop_XExpression41", None)
                    
                    if opp_val == self:
                        setattr(item, "caltrop_XExpression41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "caltrop_XExpression41"):
                    opp_val = getattr(item, "caltrop_XExpression41", None)
                    
                    setattr(item, "caltrop_XExpression41", self)
                    

class ActionPattern:

    pass
class caltrop_EventPattern(ActionPattern):

    def __init__(self, name: str, qualifier: str, variables: str, property: bool, caltrop_EventPattern: "caltrop_EventAction" = None, caltrop_EventPattern63: "caltrop_StateVariable" = None, caltrop_EventPattern66: "caltrop_XExpression" = None, caltrop_EventPattern69: "caltrop_XExpression" = None):
        self.name = name
        self.qualifier = qualifier
        self.variables = variables
        self.property = property
        self.caltrop_EventPattern = caltrop_EventPattern
        self.caltrop_EventPattern63 = caltrop_EventPattern63
        self.caltrop_EventPattern66 = caltrop_EventPattern66
        self.caltrop_EventPattern69 = caltrop_EventPattern69
        
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
    def caltrop_EventPattern66(self):
        return self.__caltrop_EventPattern66

    @caltrop_EventPattern66.setter
    def caltrop_EventPattern66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caltrop_EventPattern__caltrop_EventPattern66", None)
        self.__caltrop_EventPattern66 = value
        
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
    def caltrop_EventPattern63(self):
        return self.__caltrop_EventPattern63

    @caltrop_EventPattern63.setter
    def caltrop_EventPattern63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caltrop_EventPattern__caltrop_EventPattern63", None)
        self.__caltrop_EventPattern63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caltrop_StateVariable64"):
                opp_val = getattr(old_value, "caltrop_StateVariable64", None)
                if opp_val == self:
                    setattr(old_value, "caltrop_StateVariable64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caltrop_StateVariable64"):
                opp_val = getattr(value, "caltrop_StateVariable64", None)
                setattr(value, "caltrop_StateVariable64", self)

    @property
    def caltrop_EventPattern69(self):
        return self.__caltrop_EventPattern69

    @caltrop_EventPattern69.setter
    def caltrop_EventPattern69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caltrop_EventPattern__caltrop_EventPattern69", None)
        self.__caltrop_EventPattern69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caltrop_XExpression70"):
                opp_val = getattr(old_value, "caltrop_XExpression70", None)
                if opp_val == self:
                    setattr(old_value, "caltrop_XExpression70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caltrop_XExpression70"):
                opp_val = getattr(value, "caltrop_XExpression70", None)
                setattr(value, "caltrop_XExpression70", self)

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
class caltrop_PortPattern(ABC):

    def __init__(self, caltrop_PortPattern: "caltrop_XExpression" = None, caltrop_PortPattern31: "caltrop_ChannelSelector" = None, caltrop_PortPattern33: "caltrop_Port" = None, caltrop_PortPattern35: "caltrop_XExpression" = None):
        self.caltrop_PortPattern = caltrop_PortPattern
        self.caltrop_PortPattern31 = caltrop_PortPattern31
        self.caltrop_PortPattern33 = caltrop_PortPattern33
        self.caltrop_PortPattern35 = caltrop_PortPattern35
        
    @property
    def caltrop_PortPattern31(self):
        return self.__caltrop_PortPattern31

    @caltrop_PortPattern31.setter
    def caltrop_PortPattern31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caltrop_PortPattern__caltrop_PortPattern31", None)
        self.__caltrop_PortPattern31 = value
        
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
    def caltrop_PortPattern(self):
        return self.__caltrop_PortPattern

    @caltrop_PortPattern.setter
    def caltrop_PortPattern(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caltrop_PortPattern__caltrop_PortPattern", None)
        self.__caltrop_PortPattern = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caltrop_XExpression29"):
                opp_val = getattr(old_value, "caltrop_XExpression29", None)
                if opp_val == self:
                    setattr(old_value, "caltrop_XExpression29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caltrop_XExpression29"):
                opp_val = getattr(value, "caltrop_XExpression29", None)
                setattr(value, "caltrop_XExpression29", self)

    @property
    def caltrop_PortPattern33(self):
        return self.__caltrop_PortPattern33

    @caltrop_PortPattern33.setter
    def caltrop_PortPattern33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caltrop_PortPattern__caltrop_PortPattern33", None)
        self.__caltrop_PortPattern33 = value
        
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
    def caltrop_PortPattern35(self):
        return self.__caltrop_PortPattern35

    @caltrop_PortPattern35.setter
    def caltrop_PortPattern35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caltrop_PortPattern__caltrop_PortPattern35", None)
        self.__caltrop_PortPattern35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caltrop_XExpression36"):
                opp_val = getattr(old_value, "caltrop_XExpression36", None)
                if opp_val == self:
                    setattr(old_value, "caltrop_XExpression36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caltrop_XExpression36"):
                opp_val = getattr(value, "caltrop_XExpression36", None)
                setattr(value, "caltrop_XExpression36", self)

    def size(self) -> int:
        # TODO: Implement size method
        pass

class caltrop_OutputPattern(PortPattern):

    pass
class caltrop_FunctionDeclaration(JvmTypedObj):

    pass
class caltrop_OutputAction(NamedObj):

    def __init__(self, caltrop_OutputAction: "caltrop_CaltropActorImpl" = None, caltrop_OutputAction15: "caltrop_XExpression" = None, caltrop_OutputAction18: set["caltrop_OutputPattern"] = None, caltrop_OutputAction20: "caltrop_XExpression" = None, caltrop_OutputAction23: "caltrop_XExpression" = None, caltrop_OutputAction26: "caltrop_XExpression" = None, caltrop_OutputAction60: "caltrop_Transition" = None):
        self.caltrop_OutputAction = caltrop_OutputAction
        self.caltrop_OutputAction15 = caltrop_OutputAction15
        self.caltrop_OutputAction18 = caltrop_OutputAction18 if caltrop_OutputAction18 is not None else set()
        self.caltrop_OutputAction20 = caltrop_OutputAction20
        self.caltrop_OutputAction23 = caltrop_OutputAction23
        self.caltrop_OutputAction26 = caltrop_OutputAction26
        self.caltrop_OutputAction60 = caltrop_OutputAction60
        
    @property
    def caltrop_OutputAction26(self):
        return self.__caltrop_OutputAction26

    @caltrop_OutputAction26.setter
    def caltrop_OutputAction26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caltrop_OutputAction__caltrop_OutputAction26", None)
        self.__caltrop_OutputAction26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caltrop_XExpression27"):
                opp_val = getattr(old_value, "caltrop_XExpression27", None)
                if opp_val == self:
                    setattr(old_value, "caltrop_XExpression27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caltrop_XExpression27"):
                opp_val = getattr(value, "caltrop_XExpression27", None)
                setattr(value, "caltrop_XExpression27", self)

    @property
    def caltrop_OutputAction18(self):
        return self.__caltrop_OutputAction18

    @caltrop_OutputAction18.setter
    def caltrop_OutputAction18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caltrop_OutputAction__caltrop_OutputAction18", None)
        self.__caltrop_OutputAction18 = value if value is not None else set()
        
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
                    

    @property
    def caltrop_OutputAction60(self):
        return self.__caltrop_OutputAction60

    @caltrop_OutputAction60.setter
    def caltrop_OutputAction60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caltrop_OutputAction__caltrop_OutputAction60", None)
        self.__caltrop_OutputAction60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caltrop_Transition59"):
                opp_val = getattr(old_value, "caltrop_Transition59", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caltrop_Transition59"):
                opp_val = getattr(value, "caltrop_Transition59", None)
                if opp_val is None:
                    setattr(value, "caltrop_Transition59", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def caltrop_OutputAction23(self):
        return self.__caltrop_OutputAction23

    @caltrop_OutputAction23.setter
    def caltrop_OutputAction23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caltrop_OutputAction__caltrop_OutputAction23", None)
        self.__caltrop_OutputAction23 = value
        
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
    def caltrop_OutputAction20(self):
        return self.__caltrop_OutputAction20

    @caltrop_OutputAction20.setter
    def caltrop_OutputAction20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caltrop_OutputAction__caltrop_OutputAction20", None)
        self.__caltrop_OutputAction20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caltrop_XExpression21"):
                opp_val = getattr(old_value, "caltrop_XExpression21", None)
                if opp_val == self:
                    setattr(old_value, "caltrop_XExpression21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caltrop_XExpression21"):
                opp_val = getattr(value, "caltrop_XExpression21", None)
                setattr(value, "caltrop_XExpression21", self)

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

    def getInputPatterns(self) -> str:
        # TODO: Implement getInputPatterns method
        pass

class caltrop_ReAction(OutputAction):

    pass
class caltrop_CaltropActorImpl:

    pass
class caltrop_Realm:

    def __init__(self, key: str, caltrop_Realm: "caltrop_StateVariable" = None):
        self.key = key
        self.caltrop_Realm = caltrop_Realm
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

    @property
    def caltrop_Realm(self):
        return self.__caltrop_Realm

    @caltrop_Realm.setter
    def caltrop_Realm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caltrop_Realm__caltrop_Realm", None)
        self.__caltrop_Realm = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caltrop_StateVariable12"):
                opp_val = getattr(old_value, "caltrop_StateVariable12", None)
                if opp_val == self:
                    setattr(old_value, "caltrop_StateVariable12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caltrop_StateVariable12"):
                opp_val = getattr(value, "caltrop_StateVariable12", None)
                setattr(value, "caltrop_StateVariable12", self)

class caltrop_XExpression:

    pass
class Variable:

    pass
class caltrop_StateVariable(Variable):

    def __init__(self, constant: bool, binding: bool, caltrop_StateVariable10: "caltrop_XExpression" = None, caltrop_StateVariable: "caltrop_CaltropActorImpl" = None, caltrop_StateVariable12: "caltrop_Realm" = None, caltrop_StateVariable64: "caltrop_EventPattern" = None):
        self.constant = constant
        self.binding = binding
        self.caltrop_StateVariable10 = caltrop_StateVariable10
        self.caltrop_StateVariable = caltrop_StateVariable
        self.caltrop_StateVariable12 = caltrop_StateVariable12
        self.caltrop_StateVariable64 = caltrop_StateVariable64
        
    @property
    def constant(self) -> bool:
        return self.__constant

    @constant.setter
    def constant(self, constant: bool):
        self.__constant = constant

    @property
    def binding(self) -> bool:
        return self.__binding

    @binding.setter
    def binding(self, binding: bool):
        self.__binding = binding

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

    @property
    def caltrop_StateVariable64(self):
        return self.__caltrop_StateVariable64

    @caltrop_StateVariable64.setter
    def caltrop_StateVariable64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caltrop_StateVariable__caltrop_StateVariable64", None)
        self.__caltrop_StateVariable64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caltrop_EventPattern63"):
                opp_val = getattr(old_value, "caltrop_EventPattern63", None)
                if opp_val == self:
                    setattr(old_value, "caltrop_EventPattern63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caltrop_EventPattern63"):
                opp_val = getattr(value, "caltrop_EventPattern63", None)
                setattr(value, "caltrop_EventPattern63", self)

    @property
    def caltrop_StateVariable12(self):
        return self.__caltrop_StateVariable12

    @caltrop_StateVariable12.setter
    def caltrop_StateVariable12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caltrop_StateVariable__caltrop_StateVariable12", None)
        self.__caltrop_StateVariable12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "caltrop_Realm"):
                opp_val = getattr(old_value, "caltrop_Realm", None)
                if opp_val == self:
                    setattr(old_value, "caltrop_Realm", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "caltrop_Realm"):
                opp_val = getattr(value, "caltrop_Realm", None)
                setattr(value, "caltrop_Realm", self)

    @property
    def caltrop_StateVariable10(self):
        return self.__caltrop_StateVariable10

    @caltrop_StateVariable10.setter
    def caltrop_StateVariable10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_caltrop_StateVariable__caltrop_StateVariable10", None)
        self.__caltrop_StateVariable10 = value
        
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