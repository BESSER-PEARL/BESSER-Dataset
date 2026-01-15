from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Element:

    pass
class MMInterModel_StringEnumeration(Element):

    def __init__(self, attribute: str, MMInterModel_StringEnumeration: "MMInterModel_Attribute" = None):
        self.attribute = attribute
        self.MMInterModel_StringEnumeration = MMInterModel_StringEnumeration
        
    @property
    def attribute(self) -> str:
        return self.__attribute

    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def MMInterModel_StringEnumeration(self):
        return self.__MMInterModel_StringEnumeration

    @MMInterModel_StringEnumeration.setter
    def MMInterModel_StringEnumeration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMInterModel_StringEnumeration__MMInterModel_StringEnumeration", None)
        self.__MMInterModel_StringEnumeration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MMInterModel_Attribute43"):
                opp_val = getattr(old_value, "MMInterModel_Attribute43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MMInterModel_Attribute43"):
                opp_val = getattr(value, "MMInterModel_Attribute43", None)
                if opp_val is None:
                    setattr(value, "MMInterModel_Attribute43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MMInterModel_Component(Element):

    def __init__(self, numberOfSpares: int, model: str, MMInterModel_Component: "MMInterModel_Model" = None, MMInterModel_Component8: "MMInterModel_StateMachine" = None, MMInterModel_Component10: set["MMInterModel_Attribute"] = None, MMInterModel_Component13: set["MMInterModel_StateMachine"] = None):
        self.numberOfSpares = numberOfSpares
        self.model = model
        self.MMInterModel_Component = MMInterModel_Component
        self.MMInterModel_Component8 = MMInterModel_Component8
        self.MMInterModel_Component10 = MMInterModel_Component10 if MMInterModel_Component10 is not None else set()
        self.MMInterModel_Component13 = MMInterModel_Component13 if MMInterModel_Component13 is not None else set()
        
    @property
    def model(self) -> str:
        return self.__model

    @model.setter
    def model(self, model: str):
        self.__model = model

    @property
    def numberOfSpares(self) -> int:
        return self.__numberOfSpares

    @numberOfSpares.setter
    def numberOfSpares(self, numberOfSpares: int):
        self.__numberOfSpares = numberOfSpares

    @property
    def MMInterModel_Component13(self):
        return self.__MMInterModel_Component13

    @MMInterModel_Component13.setter
    def MMInterModel_Component13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMInterModel_Component__MMInterModel_Component13", None)
        self.__MMInterModel_Component13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MMInterModel_StateMachine14"):
                    opp_val = getattr(item, "MMInterModel_StateMachine14", None)
                    
                    if opp_val == self:
                        setattr(item, "MMInterModel_StateMachine14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MMInterModel_StateMachine14"):
                    opp_val = getattr(item, "MMInterModel_StateMachine14", None)
                    
                    setattr(item, "MMInterModel_StateMachine14", self)
                    

    @property
    def MMInterModel_Component10(self):
        return self.__MMInterModel_Component10

    @MMInterModel_Component10.setter
    def MMInterModel_Component10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMInterModel_Component__MMInterModel_Component10", None)
        self.__MMInterModel_Component10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MMInterModel_Attribute11"):
                    opp_val = getattr(item, "MMInterModel_Attribute11", None)
                    
                    if opp_val == self:
                        setattr(item, "MMInterModel_Attribute11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MMInterModel_Attribute11"):
                    opp_val = getattr(item, "MMInterModel_Attribute11", None)
                    
                    setattr(item, "MMInterModel_Attribute11", self)
                    

    @property
    def MMInterModel_Component8(self):
        return self.__MMInterModel_Component8

    @MMInterModel_Component8.setter
    def MMInterModel_Component8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMInterModel_Component__MMInterModel_Component8", None)
        self.__MMInterModel_Component8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MMInterModel_StateMachine"):
                opp_val = getattr(old_value, "MMInterModel_StateMachine", None)
                if opp_val == self:
                    setattr(old_value, "MMInterModel_StateMachine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MMInterModel_StateMachine"):
                opp_val = getattr(value, "MMInterModel_StateMachine", None)
                setattr(value, "MMInterModel_StateMachine", self)

    @property
    def MMInterModel_Component(self):
        return self.__MMInterModel_Component

    @MMInterModel_Component.setter
    def MMInterModel_Component(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMInterModel_Component__MMInterModel_Component", None)
        self.__MMInterModel_Component = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MMInterModel_Model"):
                opp_val = getattr(old_value, "MMInterModel_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MMInterModel_Model"):
                opp_val = getattr(value, "MMInterModel_Model", None)
                if opp_val is None:
                    setattr(value, "MMInterModel_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MMInterModel_StateConfiguration(Element):

    def __init__(self, configOperator: str, condition: str, negation: bool, model: str, MMInterModel_StateConfiguration: "MMInterModel_Model" = None, MMInterModel_StateConfiguration48: set["MMInterModel_State"] = None, MMInterModel_StateConfiguration52: "MMInterModel_StateConfiguration" = None, MMInterModel_StateConfiguration50: set["MMInterModel_StateConfiguration"] = None):
        self.configOperator = configOperator
        self.condition = condition
        self.negation = negation
        self.model = model
        self.MMInterModel_StateConfiguration = MMInterModel_StateConfiguration
        self.MMInterModel_StateConfiguration48 = MMInterModel_StateConfiguration48 if MMInterModel_StateConfiguration48 is not None else set()
        self.MMInterModel_StateConfiguration52 = MMInterModel_StateConfiguration52
        self.MMInterModel_StateConfiguration50 = MMInterModel_StateConfiguration50 if MMInterModel_StateConfiguration50 is not None else set()
        
    @property
    def configOperator(self) -> str:
        return self.__configOperator

    @configOperator.setter
    def configOperator(self, configOperator: str):
        self.__configOperator = configOperator

    @property
    def negation(self) -> bool:
        return self.__negation

    @negation.setter
    def negation(self, negation: bool):
        self.__negation = negation

    @property
    def condition(self) -> str:
        return self.__condition

    @condition.setter
    def condition(self, condition: str):
        self.__condition = condition

    @property
    def model(self) -> str:
        return self.__model

    @model.setter
    def model(self, model: str):
        self.__model = model

    @property
    def MMInterModel_StateConfiguration(self):
        return self.__MMInterModel_StateConfiguration

    @MMInterModel_StateConfiguration.setter
    def MMInterModel_StateConfiguration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMInterModel_StateConfiguration__MMInterModel_StateConfiguration", None)
        self.__MMInterModel_StateConfiguration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MMInterModel_Model6"):
                opp_val = getattr(old_value, "MMInterModel_Model6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MMInterModel_Model6"):
                opp_val = getattr(value, "MMInterModel_Model6", None)
                if opp_val is None:
                    setattr(value, "MMInterModel_Model6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MMInterModel_StateConfiguration50(self):
        return self.__MMInterModel_StateConfiguration50

    @MMInterModel_StateConfiguration50.setter
    def MMInterModel_StateConfiguration50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMInterModel_StateConfiguration__MMInterModel_StateConfiguration50", None)
        self.__MMInterModel_StateConfiguration50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MMInterModel_StateConfiguration52"):
                    opp_val = getattr(item, "MMInterModel_StateConfiguration52", None)
                    
                    if opp_val == self:
                        setattr(item, "MMInterModel_StateConfiguration52", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MMInterModel_StateConfiguration52"):
                    opp_val = getattr(item, "MMInterModel_StateConfiguration52", None)
                    
                    setattr(item, "MMInterModel_StateConfiguration52", self)
                    

    @property
    def MMInterModel_StateConfiguration52(self):
        return self.__MMInterModel_StateConfiguration52

    @MMInterModel_StateConfiguration52.setter
    def MMInterModel_StateConfiguration52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMInterModel_StateConfiguration__MMInterModel_StateConfiguration52", None)
        self.__MMInterModel_StateConfiguration52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MMInterModel_StateConfiguration50"):
                opp_val = getattr(old_value, "MMInterModel_StateConfiguration50", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MMInterModel_StateConfiguration50"):
                opp_val = getattr(value, "MMInterModel_StateConfiguration50", None)
                if opp_val is None:
                    setattr(value, "MMInterModel_StateConfiguration50", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MMInterModel_StateConfiguration48(self):
        return self.__MMInterModel_StateConfiguration48

    @MMInterModel_StateConfiguration48.setter
    def MMInterModel_StateConfiguration48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMInterModel_StateConfiguration__MMInterModel_StateConfiguration48", None)
        self.__MMInterModel_StateConfiguration48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MMInterModel_State49"):
                    opp_val = getattr(item, "MMInterModel_State49", None)
                    
                    if opp_val == self:
                        setattr(item, "MMInterModel_State49", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MMInterModel_State49"):
                    opp_val = getattr(item, "MMInterModel_State49", None)
                    
                    setattr(item, "MMInterModel_State49", self)
                    

class MMInterModel_Event(Element):

    def __init__(self, type: str, model: str, MMInterModel_Event: "MMInterModel_Model" = None, MMInterModel_Event30: "MMInterModel_Transition" = None, MMInterModel_Event45: set["MMInterModel_Transition"] = None):
        self.type = type
        self.model = model
        self.MMInterModel_Event = MMInterModel_Event
        self.MMInterModel_Event30 = MMInterModel_Event30
        self.MMInterModel_Event45 = MMInterModel_Event45 if MMInterModel_Event45 is not None else set()
        
    @property
    def model(self) -> str:
        return self.__model

    @model.setter
    def model(self, model: str):
        self.__model = model

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def MMInterModel_Event45(self):
        return self.__MMInterModel_Event45

    @MMInterModel_Event45.setter
    def MMInterModel_Event45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMInterModel_Event__MMInterModel_Event45", None)
        self.__MMInterModel_Event45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MMInterModel_Transition46"):
                    opp_val = getattr(item, "MMInterModel_Transition46", None)
                    
                    if opp_val == self:
                        setattr(item, "MMInterModel_Transition46", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MMInterModel_Transition46"):
                    opp_val = getattr(item, "MMInterModel_Transition46", None)
                    
                    setattr(item, "MMInterModel_Transition46", self)
                    

    @property
    def MMInterModel_Event30(self):
        return self.__MMInterModel_Event30

    @MMInterModel_Event30.setter
    def MMInterModel_Event30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMInterModel_Event__MMInterModel_Event30", None)
        self.__MMInterModel_Event30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MMInterModel_Transition29"):
                opp_val = getattr(old_value, "MMInterModel_Transition29", None)
                if opp_val == self:
                    setattr(old_value, "MMInterModel_Transition29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MMInterModel_Transition29"):
                opp_val = getattr(value, "MMInterModel_Transition29", None)
                setattr(value, "MMInterModel_Transition29", self)

    @property
    def MMInterModel_Event(self):
        return self.__MMInterModel_Event

    @MMInterModel_Event.setter
    def MMInterModel_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMInterModel_Event__MMInterModel_Event", None)
        self.__MMInterModel_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MMInterModel_Model4"):
                opp_val = getattr(old_value, "MMInterModel_Model4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MMInterModel_Model4"):
                opp_val = getattr(value, "MMInterModel_Model4", None)
                if opp_val is None:
                    setattr(value, "MMInterModel_Model4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MMInterModel_Attribute(Element):

    def __init__(self, lowerBound: int, upperBound: int, type: str, isArray: bool, arraySize: int, defaultValue: str, model: str, component: str, MMInterModel_Attribute: "MMInterModel_Model" = None, MMInterModel_Attribute11: "MMInterModel_Component" = None, MMInterModel_Attribute43: set["MMInterModel_StringEnumeration"] = None):
        self.lowerBound = lowerBound
        self.upperBound = upperBound
        self.type = type
        self.isArray = isArray
        self.arraySize = arraySize
        self.defaultValue = defaultValue
        self.model = model
        self.component = component
        self.MMInterModel_Attribute = MMInterModel_Attribute
        self.MMInterModel_Attribute11 = MMInterModel_Attribute11
        self.MMInterModel_Attribute43 = MMInterModel_Attribute43 if MMInterModel_Attribute43 is not None else set()
        
    @property
    def defaultValue(self) -> str:
        return self.__defaultValue

    @defaultValue.setter
    def defaultValue(self, defaultValue: str):
        self.__defaultValue = defaultValue

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def lowerBound(self) -> int:
        return self.__lowerBound

    @lowerBound.setter
    def lowerBound(self, lowerBound: int):
        self.__lowerBound = lowerBound

    @property
    def component(self) -> str:
        return self.__component

    @component.setter
    def component(self, component: str):
        self.__component = component

    @property
    def arraySize(self) -> int:
        return self.__arraySize

    @arraySize.setter
    def arraySize(self, arraySize: int):
        self.__arraySize = arraySize

    @property
    def isArray(self) -> bool:
        return self.__isArray

    @isArray.setter
    def isArray(self, isArray: bool):
        self.__isArray = isArray

    @property
    def upperBound(self) -> int:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: int):
        self.__upperBound = upperBound

    @property
    def model(self) -> str:
        return self.__model

    @model.setter
    def model(self, model: str):
        self.__model = model

    @property
    def MMInterModel_Attribute(self):
        return self.__MMInterModel_Attribute

    @MMInterModel_Attribute.setter
    def MMInterModel_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMInterModel_Attribute__MMInterModel_Attribute", None)
        self.__MMInterModel_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MMInterModel_Model2"):
                opp_val = getattr(old_value, "MMInterModel_Model2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MMInterModel_Model2"):
                opp_val = getattr(value, "MMInterModel_Model2", None)
                if opp_val is None:
                    setattr(value, "MMInterModel_Model2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MMInterModel_Attribute11(self):
        return self.__MMInterModel_Attribute11

    @MMInterModel_Attribute11.setter
    def MMInterModel_Attribute11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMInterModel_Attribute__MMInterModel_Attribute11", None)
        self.__MMInterModel_Attribute11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MMInterModel_Component10"):
                opp_val = getattr(old_value, "MMInterModel_Component10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MMInterModel_Component10"):
                opp_val = getattr(value, "MMInterModel_Component10", None)
                if opp_val is None:
                    setattr(value, "MMInterModel_Component10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MMInterModel_Attribute43(self):
        return self.__MMInterModel_Attribute43

    @MMInterModel_Attribute43.setter
    def MMInterModel_Attribute43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMInterModel_Attribute__MMInterModel_Attribute43", None)
        self.__MMInterModel_Attribute43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MMInterModel_StringEnumeration"):
                    opp_val = getattr(item, "MMInterModel_StringEnumeration", None)
                    
                    if opp_val == self:
                        setattr(item, "MMInterModel_StringEnumeration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MMInterModel_StringEnumeration"):
                    opp_val = getattr(item, "MMInterModel_StringEnumeration", None)
                    
                    setattr(item, "MMInterModel_StringEnumeration", self)
                    

class MMInterModel_Guard(Element):

    def __init__(self, specification: str, transition: str, MMInterModel_Guard: "MMInterModel_Transition" = None):
        self.specification = specification
        self.transition = transition
        self.MMInterModel_Guard = MMInterModel_Guard
        
    @property
    def specification(self) -> str:
        return self.__specification

    @specification.setter
    def specification(self, specification: str):
        self.__specification = specification

    @property
    def transition(self) -> str:
        return self.__transition

    @transition.setter
    def transition(self, transition: str):
        self.__transition = transition

    @property
    def MMInterModel_Guard(self):
        return self.__MMInterModel_Guard

    @MMInterModel_Guard.setter
    def MMInterModel_Guard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMInterModel_Guard__MMInterModel_Guard", None)
        self.__MMInterModel_Guard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MMInterModel_Transition32"):
                opp_val = getattr(old_value, "MMInterModel_Transition32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MMInterModel_Transition32"):
                opp_val = getattr(value, "MMInterModel_Transition32", None)
                if opp_val is None:
                    setattr(value, "MMInterModel_Transition32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MMInterModel_StateMachine(Element):

    def __init__(self, type: str, superState: str, component: str, MMInterModel_StateMachine16: set["MMInterModel_Transition"] = None, MMInterModel_StateMachine18: set["MMInterModel_State"] = None, MMInterModel_StateMachine20: "MMInterModel_State" = None, MMInterModel_StateMachine: "MMInterModel_Component" = None, MMInterModel_StateMachine14: "MMInterModel_Component" = None, MMInterModel_StateMachine41: "MMInterModel_State" = None):
        self.type = type
        self.superState = superState
        self.component = component
        self.MMInterModel_StateMachine16 = MMInterModel_StateMachine16 if MMInterModel_StateMachine16 is not None else set()
        self.MMInterModel_StateMachine18 = MMInterModel_StateMachine18 if MMInterModel_StateMachine18 is not None else set()
        self.MMInterModel_StateMachine20 = MMInterModel_StateMachine20
        self.MMInterModel_StateMachine = MMInterModel_StateMachine
        self.MMInterModel_StateMachine14 = MMInterModel_StateMachine14
        self.MMInterModel_StateMachine41 = MMInterModel_StateMachine41
        
    @property
    def superState(self) -> str:
        return self.__superState

    @superState.setter
    def superState(self, superState: str):
        self.__superState = superState

    @property
    def component(self) -> str:
        return self.__component

    @component.setter
    def component(self, component: str):
        self.__component = component

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def MMInterModel_StateMachine14(self):
        return self.__MMInterModel_StateMachine14

    @MMInterModel_StateMachine14.setter
    def MMInterModel_StateMachine14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMInterModel_StateMachine__MMInterModel_StateMachine14", None)
        self.__MMInterModel_StateMachine14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MMInterModel_Component13"):
                opp_val = getattr(old_value, "MMInterModel_Component13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MMInterModel_Component13"):
                opp_val = getattr(value, "MMInterModel_Component13", None)
                if opp_val is None:
                    setattr(value, "MMInterModel_Component13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MMInterModel_StateMachine16(self):
        return self.__MMInterModel_StateMachine16

    @MMInterModel_StateMachine16.setter
    def MMInterModel_StateMachine16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMInterModel_StateMachine__MMInterModel_StateMachine16", None)
        self.__MMInterModel_StateMachine16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MMInterModel_Transition"):
                    opp_val = getattr(item, "MMInterModel_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "MMInterModel_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MMInterModel_Transition"):
                    opp_val = getattr(item, "MMInterModel_Transition", None)
                    
                    setattr(item, "MMInterModel_Transition", self)
                    

    @property
    def MMInterModel_StateMachine41(self):
        return self.__MMInterModel_StateMachine41

    @MMInterModel_StateMachine41.setter
    def MMInterModel_StateMachine41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMInterModel_StateMachine__MMInterModel_StateMachine41", None)
        self.__MMInterModel_StateMachine41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MMInterModel_State40"):
                opp_val = getattr(old_value, "MMInterModel_State40", None)
                if opp_val == self:
                    setattr(old_value, "MMInterModel_State40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MMInterModel_State40"):
                opp_val = getattr(value, "MMInterModel_State40", None)
                setattr(value, "MMInterModel_State40", self)

    @property
    def MMInterModel_StateMachine18(self):
        return self.__MMInterModel_StateMachine18

    @MMInterModel_StateMachine18.setter
    def MMInterModel_StateMachine18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMInterModel_StateMachine__MMInterModel_StateMachine18", None)
        self.__MMInterModel_StateMachine18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MMInterModel_State"):
                    opp_val = getattr(item, "MMInterModel_State", None)
                    
                    if opp_val == self:
                        setattr(item, "MMInterModel_State", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MMInterModel_State"):
                    opp_val = getattr(item, "MMInterModel_State", None)
                    
                    setattr(item, "MMInterModel_State", self)
                    

    @property
    def MMInterModel_StateMachine(self):
        return self.__MMInterModel_StateMachine

    @MMInterModel_StateMachine.setter
    def MMInterModel_StateMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMInterModel_StateMachine__MMInterModel_StateMachine", None)
        self.__MMInterModel_StateMachine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MMInterModel_Component8"):
                opp_val = getattr(old_value, "MMInterModel_Component8", None)
                if opp_val == self:
                    setattr(old_value, "MMInterModel_Component8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MMInterModel_Component8"):
                opp_val = getattr(value, "MMInterModel_Component8", None)
                setattr(value, "MMInterModel_Component8", self)

    @property
    def MMInterModel_StateMachine20(self):
        return self.__MMInterModel_StateMachine20

    @MMInterModel_StateMachine20.setter
    def MMInterModel_StateMachine20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMInterModel_StateMachine__MMInterModel_StateMachine20", None)
        self.__MMInterModel_StateMachine20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MMInterModel_State21"):
                opp_val = getattr(old_value, "MMInterModel_State21", None)
                if opp_val == self:
                    setattr(old_value, "MMInterModel_State21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MMInterModel_State21"):
                opp_val = getattr(value, "MMInterModel_State21", None)
                setattr(value, "MMInterModel_State21", self)

class MMInterModel_Model(Element):

    pass
class MMInterModel_Element:

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

class MMInterModel_State(Element):

    def __init__(self, duringBehaviour: str, entryBehaviour: str, exitBehaviour: str, stateMachine: str, stateConfiguration: str, stateNumber: int, MMInterModel_State: "MMInterModel_StateMachine" = None, MMInterModel_State21: "MMInterModel_StateMachine" = None, MMInterModel_State24: "MMInterModel_Transition" = None, MMInterModel_State27: "MMInterModel_Transition" = None, MMInterModel_State34: set["MMInterModel_Transition"] = None, MMInterModel_State37: set["MMInterModel_Transition"] = None, MMInterModel_State40: "MMInterModel_StateMachine" = None, MMInterModel_State49: "MMInterModel_StateConfiguration" = None):
        self.duringBehaviour = duringBehaviour
        self.entryBehaviour = entryBehaviour
        self.exitBehaviour = exitBehaviour
        self.stateMachine = stateMachine
        self.stateConfiguration = stateConfiguration
        self.stateNumber = stateNumber
        self.MMInterModel_State = MMInterModel_State
        self.MMInterModel_State21 = MMInterModel_State21
        self.MMInterModel_State24 = MMInterModel_State24
        self.MMInterModel_State27 = MMInterModel_State27
        self.MMInterModel_State34 = MMInterModel_State34 if MMInterModel_State34 is not None else set()
        self.MMInterModel_State37 = MMInterModel_State37 if MMInterModel_State37 is not None else set()
        self.MMInterModel_State40 = MMInterModel_State40
        self.MMInterModel_State49 = MMInterModel_State49
        
    @property
    def stateConfiguration(self) -> str:
        return self.__stateConfiguration

    @stateConfiguration.setter
    def stateConfiguration(self, stateConfiguration: str):
        self.__stateConfiguration = stateConfiguration

    @property
    def stateNumber(self) -> int:
        return self.__stateNumber

    @stateNumber.setter
    def stateNumber(self, stateNumber: int):
        self.__stateNumber = stateNumber

    @property
    def duringBehaviour(self) -> str:
        return self.__duringBehaviour

    @duringBehaviour.setter
    def duringBehaviour(self, duringBehaviour: str):
        self.__duringBehaviour = duringBehaviour

    @property
    def exitBehaviour(self) -> str:
        return self.__exitBehaviour

    @exitBehaviour.setter
    def exitBehaviour(self, exitBehaviour: str):
        self.__exitBehaviour = exitBehaviour

    @property
    def entryBehaviour(self) -> str:
        return self.__entryBehaviour

    @entryBehaviour.setter
    def entryBehaviour(self, entryBehaviour: str):
        self.__entryBehaviour = entryBehaviour

    @property
    def stateMachine(self) -> str:
        return self.__stateMachine

    @stateMachine.setter
    def stateMachine(self, stateMachine: str):
        self.__stateMachine = stateMachine

    @property
    def MMInterModel_State24(self):
        return self.__MMInterModel_State24

    @MMInterModel_State24.setter
    def MMInterModel_State24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMInterModel_State__MMInterModel_State24", None)
        self.__MMInterModel_State24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MMInterModel_Transition23"):
                opp_val = getattr(old_value, "MMInterModel_Transition23", None)
                if opp_val == self:
                    setattr(old_value, "MMInterModel_Transition23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MMInterModel_Transition23"):
                opp_val = getattr(value, "MMInterModel_Transition23", None)
                setattr(value, "MMInterModel_Transition23", self)

    @property
    def MMInterModel_State21(self):
        return self.__MMInterModel_State21

    @MMInterModel_State21.setter
    def MMInterModel_State21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMInterModel_State__MMInterModel_State21", None)
        self.__MMInterModel_State21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MMInterModel_StateMachine20"):
                opp_val = getattr(old_value, "MMInterModel_StateMachine20", None)
                if opp_val == self:
                    setattr(old_value, "MMInterModel_StateMachine20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MMInterModel_StateMachine20"):
                opp_val = getattr(value, "MMInterModel_StateMachine20", None)
                setattr(value, "MMInterModel_StateMachine20", self)

    @property
    def MMInterModel_State37(self):
        return self.__MMInterModel_State37

    @MMInterModel_State37.setter
    def MMInterModel_State37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMInterModel_State__MMInterModel_State37", None)
        self.__MMInterModel_State37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MMInterModel_Transition38"):
                    opp_val = getattr(item, "MMInterModel_Transition38", None)
                    
                    if opp_val == self:
                        setattr(item, "MMInterModel_Transition38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MMInterModel_Transition38"):
                    opp_val = getattr(item, "MMInterModel_Transition38", None)
                    
                    setattr(item, "MMInterModel_Transition38", self)
                    

    @property
    def MMInterModel_State49(self):
        return self.__MMInterModel_State49

    @MMInterModel_State49.setter
    def MMInterModel_State49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMInterModel_State__MMInterModel_State49", None)
        self.__MMInterModel_State49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MMInterModel_StateConfiguration48"):
                opp_val = getattr(old_value, "MMInterModel_StateConfiguration48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MMInterModel_StateConfiguration48"):
                opp_val = getattr(value, "MMInterModel_StateConfiguration48", None)
                if opp_val is None:
                    setattr(value, "MMInterModel_StateConfiguration48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MMInterModel_State34(self):
        return self.__MMInterModel_State34

    @MMInterModel_State34.setter
    def MMInterModel_State34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMInterModel_State__MMInterModel_State34", None)
        self.__MMInterModel_State34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MMInterModel_Transition35"):
                    opp_val = getattr(item, "MMInterModel_Transition35", None)
                    
                    if opp_val == self:
                        setattr(item, "MMInterModel_Transition35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MMInterModel_Transition35"):
                    opp_val = getattr(item, "MMInterModel_Transition35", None)
                    
                    setattr(item, "MMInterModel_Transition35", self)
                    

    @property
    def MMInterModel_State27(self):
        return self.__MMInterModel_State27

    @MMInterModel_State27.setter
    def MMInterModel_State27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMInterModel_State__MMInterModel_State27", None)
        self.__MMInterModel_State27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MMInterModel_Transition26"):
                opp_val = getattr(old_value, "MMInterModel_Transition26", None)
                if opp_val == self:
                    setattr(old_value, "MMInterModel_Transition26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MMInterModel_Transition26"):
                opp_val = getattr(value, "MMInterModel_Transition26", None)
                setattr(value, "MMInterModel_Transition26", self)

    @property
    def MMInterModel_State40(self):
        return self.__MMInterModel_State40

    @MMInterModel_State40.setter
    def MMInterModel_State40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMInterModel_State__MMInterModel_State40", None)
        self.__MMInterModel_State40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MMInterModel_StateMachine41"):
                opp_val = getattr(old_value, "MMInterModel_StateMachine41", None)
                if opp_val == self:
                    setattr(old_value, "MMInterModel_StateMachine41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MMInterModel_StateMachine41"):
                opp_val = getattr(value, "MMInterModel_StateMachine41", None)
                setattr(value, "MMInterModel_StateMachine41", self)

    @property
    def MMInterModel_State(self):
        return self.__MMInterModel_State

    @MMInterModel_State.setter
    def MMInterModel_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMInterModel_State__MMInterModel_State", None)
        self.__MMInterModel_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MMInterModel_StateMachine18"):
                opp_val = getattr(old_value, "MMInterModel_StateMachine18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MMInterModel_StateMachine18"):
                opp_val = getattr(value, "MMInterModel_StateMachine18", None)
                if opp_val is None:
                    setattr(value, "MMInterModel_StateMachine18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class MMInterModel_Transition(Element):

    def __init__(self, action: str, stateMachine: str, MMInterModel_Transition: "MMInterModel_StateMachine" = None, MMInterModel_Transition23: "MMInterModel_State" = None, MMInterModel_Transition26: "MMInterModel_State" = None, MMInterModel_Transition29: "MMInterModel_Event" = None, MMInterModel_Transition32: set["MMInterModel_Guard"] = None, MMInterModel_Transition35: "MMInterModel_State" = None, MMInterModel_Transition38: "MMInterModel_State" = None, MMInterModel_Transition46: "MMInterModel_Event" = None):
        self.action = action
        self.stateMachine = stateMachine
        self.MMInterModel_Transition = MMInterModel_Transition
        self.MMInterModel_Transition23 = MMInterModel_Transition23
        self.MMInterModel_Transition26 = MMInterModel_Transition26
        self.MMInterModel_Transition29 = MMInterModel_Transition29
        self.MMInterModel_Transition32 = MMInterModel_Transition32 if MMInterModel_Transition32 is not None else set()
        self.MMInterModel_Transition35 = MMInterModel_Transition35
        self.MMInterModel_Transition38 = MMInterModel_Transition38
        self.MMInterModel_Transition46 = MMInterModel_Transition46
        
    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

    @property
    def stateMachine(self) -> str:
        return self.__stateMachine

    @stateMachine.setter
    def stateMachine(self, stateMachine: str):
        self.__stateMachine = stateMachine

    @property
    def MMInterModel_Transition38(self):
        return self.__MMInterModel_Transition38

    @MMInterModel_Transition38.setter
    def MMInterModel_Transition38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMInterModel_Transition__MMInterModel_Transition38", None)
        self.__MMInterModel_Transition38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MMInterModel_State37"):
                opp_val = getattr(old_value, "MMInterModel_State37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MMInterModel_State37"):
                opp_val = getattr(value, "MMInterModel_State37", None)
                if opp_val is None:
                    setattr(value, "MMInterModel_State37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MMInterModel_Transition26(self):
        return self.__MMInterModel_Transition26

    @MMInterModel_Transition26.setter
    def MMInterModel_Transition26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMInterModel_Transition__MMInterModel_Transition26", None)
        self.__MMInterModel_Transition26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MMInterModel_State27"):
                opp_val = getattr(old_value, "MMInterModel_State27", None)
                if opp_val == self:
                    setattr(old_value, "MMInterModel_State27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MMInterModel_State27"):
                opp_val = getattr(value, "MMInterModel_State27", None)
                setattr(value, "MMInterModel_State27", self)

    @property
    def MMInterModel_Transition29(self):
        return self.__MMInterModel_Transition29

    @MMInterModel_Transition29.setter
    def MMInterModel_Transition29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMInterModel_Transition__MMInterModel_Transition29", None)
        self.__MMInterModel_Transition29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MMInterModel_Event30"):
                opp_val = getattr(old_value, "MMInterModel_Event30", None)
                if opp_val == self:
                    setattr(old_value, "MMInterModel_Event30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MMInterModel_Event30"):
                opp_val = getattr(value, "MMInterModel_Event30", None)
                setattr(value, "MMInterModel_Event30", self)

    @property
    def MMInterModel_Transition(self):
        return self.__MMInterModel_Transition

    @MMInterModel_Transition.setter
    def MMInterModel_Transition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMInterModel_Transition__MMInterModel_Transition", None)
        self.__MMInterModel_Transition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MMInterModel_StateMachine16"):
                opp_val = getattr(old_value, "MMInterModel_StateMachine16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MMInterModel_StateMachine16"):
                opp_val = getattr(value, "MMInterModel_StateMachine16", None)
                if opp_val is None:
                    setattr(value, "MMInterModel_StateMachine16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MMInterModel_Transition35(self):
        return self.__MMInterModel_Transition35

    @MMInterModel_Transition35.setter
    def MMInterModel_Transition35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMInterModel_Transition__MMInterModel_Transition35", None)
        self.__MMInterModel_Transition35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MMInterModel_State34"):
                opp_val = getattr(old_value, "MMInterModel_State34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MMInterModel_State34"):
                opp_val = getattr(value, "MMInterModel_State34", None)
                if opp_val is None:
                    setattr(value, "MMInterModel_State34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MMInterModel_Transition32(self):
        return self.__MMInterModel_Transition32

    @MMInterModel_Transition32.setter
    def MMInterModel_Transition32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMInterModel_Transition__MMInterModel_Transition32", None)
        self.__MMInterModel_Transition32 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MMInterModel_Guard"):
                    opp_val = getattr(item, "MMInterModel_Guard", None)
                    
                    if opp_val == self:
                        setattr(item, "MMInterModel_Guard", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MMInterModel_Guard"):
                    opp_val = getattr(item, "MMInterModel_Guard", None)
                    
                    setattr(item, "MMInterModel_Guard", self)
                    

    @property
    def MMInterModel_Transition46(self):
        return self.__MMInterModel_Transition46

    @MMInterModel_Transition46.setter
    def MMInterModel_Transition46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMInterModel_Transition__MMInterModel_Transition46", None)
        self.__MMInterModel_Transition46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MMInterModel_Event45"):
                opp_val = getattr(old_value, "MMInterModel_Event45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MMInterModel_Event45"):
                opp_val = getattr(value, "MMInterModel_Event45", None)
                if opp_val is None:
                    setattr(value, "MMInterModel_Event45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MMInterModel_Transition23(self):
        return self.__MMInterModel_Transition23

    @MMInterModel_Transition23.setter
    def MMInterModel_Transition23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_MMInterModel_Transition__MMInterModel_Transition23", None)
        self.__MMInterModel_Transition23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MMInterModel_State24"):
                opp_val = getattr(old_value, "MMInterModel_State24", None)
                if opp_val == self:
                    setattr(old_value, "MMInterModel_State24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MMInterModel_State24"):
                opp_val = getattr(value, "MMInterModel_State24", None)
                setattr(value, "MMInterModel_State24", self)
