from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class StateValueType(Enum):
    string = "string"
    long = "long"
    eventField = "eventField"
    eventName = "eventName"
    delete = "delete"
    query = "query"
    definedState = "definedState"
    int = "int"
    null = "null"
class StateAttributeType(Enum):
    null = "null"
    constant = "constant"
    eventField = "eventField"
    location = "location"
    query = "query"


############################################
# Definition of Classes
############################################

class AbstractCondition:

    pass
class statemachine_FieldCondition(AbstractCondition):

    def __init__(self, fieldName: str):
        self.fieldName = fieldName
        
    @property
    def fieldName(self) -> str:
        return self.__fieldName

    @fieldName.setter
    def fieldName(self, fieldName: str):
        self.__fieldName = fieldName

class statemachine_AttributeCondition(AbstractCondition):

    pass
class statemachine_StateAttribute:

    def __init__(self, type: str, value: str, statemachine_StateAttribute13: "statemachine_StateChange" = None, statemachine_StateAttribute: "statemachine_StateAttribute" = None, statemachine_StateAttribute8: set["statemachine_StateAttribute"] = None, statemachine_StateAttribute20: "statemachine_AttributeCondition" = None):
        self.type = type
        self.value = value
        self.statemachine_StateAttribute13 = statemachine_StateAttribute13
        self.statemachine_StateAttribute = statemachine_StateAttribute
        self.statemachine_StateAttribute8 = statemachine_StateAttribute8 if statemachine_StateAttribute8 is not None else set()
        self.statemachine_StateAttribute20 = statemachine_StateAttribute20
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def statemachine_StateAttribute(self):
        return self.__statemachine_StateAttribute

    @statemachine_StateAttribute.setter
    def statemachine_StateAttribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_StateAttribute__statemachine_StateAttribute", None)
        self.__statemachine_StateAttribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_StateAttribute8"):
                opp_val = getattr(old_value, "statemachine_StateAttribute8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_StateAttribute8"):
                opp_val = getattr(value, "statemachine_StateAttribute8", None)
                if opp_val is None:
                    setattr(value, "statemachine_StateAttribute8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statemachine_StateAttribute8(self):
        return self.__statemachine_StateAttribute8

    @statemachine_StateAttribute8.setter
    def statemachine_StateAttribute8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_StateAttribute__statemachine_StateAttribute8", None)
        self.__statemachine_StateAttribute8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_StateAttribute"):
                    opp_val = getattr(item, "statemachine_StateAttribute", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_StateAttribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_StateAttribute"):
                    opp_val = getattr(item, "statemachine_StateAttribute", None)
                    
                    setattr(item, "statemachine_StateAttribute", self)
                    

    @property
    def statemachine_StateAttribute20(self):
        return self.__statemachine_StateAttribute20

    @statemachine_StateAttribute20.setter
    def statemachine_StateAttribute20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_StateAttribute__statemachine_StateAttribute20", None)
        self.__statemachine_StateAttribute20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_AttributeCondition"):
                opp_val = getattr(old_value, "statemachine_AttributeCondition", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_AttributeCondition"):
                opp_val = getattr(value, "statemachine_AttributeCondition", None)
                if opp_val is None:
                    setattr(value, "statemachine_AttributeCondition", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def statemachine_StateAttribute13(self):
        return self.__statemachine_StateAttribute13

    @statemachine_StateAttribute13.setter
    def statemachine_StateAttribute13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_StateAttribute__statemachine_StateAttribute13", None)
        self.__statemachine_StateAttribute13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_StateChange12"):
                opp_val = getattr(old_value, "statemachine_StateChange12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_StateChange12"):
                opp_val = getattr(value, "statemachine_StateChange12", None)
                if opp_val is None:
                    setattr(value, "statemachine_StateChange12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class statemachine_AbstractCondition:

    def __init__(self, isNotCondition: bool, statemachine_AbstractCondition: "statemachine_ConditionalState" = None, statemachine_AbstractCondition17: "statemachine_StateValue" = None):
        self.isNotCondition = isNotCondition
        self.statemachine_AbstractCondition = statemachine_AbstractCondition
        self.statemachine_AbstractCondition17 = statemachine_AbstractCondition17
        
    @property
    def isNotCondition(self) -> bool:
        return self.__isNotCondition

    @isNotCondition.setter
    def isNotCondition(self, isNotCondition: bool):
        self.__isNotCondition = isNotCondition

    @property
    def statemachine_AbstractCondition17(self):
        return self.__statemachine_AbstractCondition17

    @statemachine_AbstractCondition17.setter
    def statemachine_AbstractCondition17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_AbstractCondition__statemachine_AbstractCondition17", None)
        self.__statemachine_AbstractCondition17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_StateValue18"):
                opp_val = getattr(old_value, "statemachine_StateValue18", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_StateValue18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_StateValue18"):
                opp_val = getattr(value, "statemachine_StateValue18", None)
                setattr(value, "statemachine_StateValue18", self)

    @property
    def statemachine_AbstractCondition(self):
        return self.__statemachine_AbstractCondition

    @statemachine_AbstractCondition.setter
    def statemachine_AbstractCondition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_AbstractCondition__statemachine_AbstractCondition", None)
        self.__statemachine_AbstractCondition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_ConditionalState"):
                opp_val = getattr(old_value, "statemachine_ConditionalState", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_ConditionalState"):
                opp_val = getattr(value, "statemachine_ConditionalState", None)
                if opp_val is None:
                    setattr(value, "statemachine_ConditionalState", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class AbstractTransition:

    pass
class statemachine_ConditionalTransition(AbstractTransition):

    pass
class statemachine_Transition(AbstractTransition):

    pass
class statemachine_StateValue:

    def __init__(self, type: str, value: str, statemachine_StateValue: "statemachine_StateChange" = None, statemachine_StateValue18: "statemachine_AbstractCondition" = None):
        self.type = type
        self.value = value
        self.statemachine_StateValue = statemachine_StateValue
        self.statemachine_StateValue18 = statemachine_StateValue18
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def statemachine_StateValue18(self):
        return self.__statemachine_StateValue18

    @statemachine_StateValue18.setter
    def statemachine_StateValue18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_StateValue__statemachine_StateValue18", None)
        self.__statemachine_StateValue18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_AbstractCondition17"):
                opp_val = getattr(old_value, "statemachine_AbstractCondition17", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_AbstractCondition17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_AbstractCondition17"):
                opp_val = getattr(value, "statemachine_AbstractCondition17", None)
                setattr(value, "statemachine_AbstractCondition17", self)

    @property
    def statemachine_StateValue(self):
        return self.__statemachine_StateValue

    @statemachine_StateValue.setter
    def statemachine_StateValue(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_StateValue__statemachine_StateValue", None)
        self.__statemachine_StateValue = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "statemachine_StateChange15"):
                opp_val = getattr(old_value, "statemachine_StateChange15", None)
                if opp_val == self:
                    setattr(old_value, "statemachine_StateChange15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "statemachine_StateChange15"):
                opp_val = getattr(value, "statemachine_StateChange15", None)
                setattr(value, "statemachine_StateChange15", self)

class statemachine_Named:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class AbstractState:

    pass
class statemachine_FinalState(AbstractState):

    pass
class statemachine_ConditionalState(AbstractState):

    def __init__(self, andExpression: bool, conditionsOrganization: str, statemachine_ConditionalState: set["statemachine_AbstractCondition"] = None):
        self.andExpression = andExpression
        self.conditionsOrganization = conditionsOrganization
        self.statemachine_ConditionalState = statemachine_ConditionalState if statemachine_ConditionalState is not None else set()
        
    @property
    def andExpression(self) -> bool:
        return self.__andExpression

    @andExpression.setter
    def andExpression(self, andExpression: bool):
        self.__andExpression = andExpression

    @property
    def conditionsOrganization(self) -> str:
        return self.__conditionsOrganization

    @conditionsOrganization.setter
    def conditionsOrganization(self, conditionsOrganization: str):
        self.__conditionsOrganization = conditionsOrganization

    @property
    def statemachine_ConditionalState(self):
        return self.__statemachine_ConditionalState

    @statemachine_ConditionalState.setter
    def statemachine_ConditionalState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_ConditionalState__statemachine_ConditionalState", None)
        self.__statemachine_ConditionalState = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_AbstractCondition"):
                    opp_val = getattr(item, "statemachine_AbstractCondition", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_AbstractCondition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_AbstractCondition"):
                    opp_val = getattr(item, "statemachine_AbstractCondition", None)
                    
                    setattr(item, "statemachine_AbstractCondition", self)
                    

class statemachine_State(AbstractState):

    def __init__(self, stateColor: str):
        self.stateColor = stateColor
        
    @property
    def stateColor(self) -> str:
        return self.__stateColor

    @stateColor.setter
    def stateColor(self, stateColor: str):
        self.__stateColor = stateColor

class statemachine_InitialState(AbstractState):

    pass
class statemachine_StateChange:

    pass
class Named:

    pass
class statemachine_AbstractTransition(Named):

    pass
class statemachine_AbstractState(Named):

    pass
class statemachine_Statemachine(Named):

    def __init__(self, associatedTree: str, associatedAttribute: str, statemachine_Statemachine: set["statemachine_AbstractState"] = None):
        self.associatedTree = associatedTree
        self.associatedAttribute = associatedAttribute
        self.statemachine_Statemachine = statemachine_Statemachine if statemachine_Statemachine is not None else set()
        
    @property
    def associatedTree(self) -> str:
        return self.__associatedTree

    @associatedTree.setter
    def associatedTree(self, associatedTree: str):
        self.__associatedTree = associatedTree

    @property
    def associatedAttribute(self) -> str:
        return self.__associatedAttribute

    @associatedAttribute.setter
    def associatedAttribute(self, associatedAttribute: str):
        self.__associatedAttribute = associatedAttribute

    @property
    def statemachine_Statemachine(self):
        return self.__statemachine_Statemachine

    @statemachine_Statemachine.setter
    def statemachine_Statemachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_statemachine_Statemachine__statemachine_Statemachine", None)
        self.__statemachine_Statemachine = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "statemachine_AbstractState"):
                    opp_val = getattr(item, "statemachine_AbstractState", None)
                    
                    if opp_val == self:
                        setattr(item, "statemachine_AbstractState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "statemachine_AbstractState"):
                    opp_val = getattr(item, "statemachine_AbstractState", None)
                    
                    setattr(item, "statemachine_AbstractState", self)
                    
