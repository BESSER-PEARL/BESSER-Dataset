from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class FunctionCall:

    pass
class thingml_InstanceRef:

    pass
class thingml_FunctionCall(ABC):

    pass
class PropertyReference:

    pass
class thingml_DictionaryReference(PropertyReference):

    pass
class ControlStructure:

    pass
class thingml_ConditionalAction(ControlStructure):

    pass
class thingml_LoopAction(ControlStructure):

    pass
class UnaryExpression:

    pass
class thingml_UnaryMinus(UnaryExpression):

    pass
class thingml_NotExpression(UnaryExpression):

    pass
class Literal:

    pass
class thingml_DoubleLiteral(Literal):

    def __init__(self, doubleValue: float):
        self.doubleValue = doubleValue
        
    @property
    def doubleValue(self) -> float:
        return self.__doubleValue

    @doubleValue.setter
    def doubleValue(self, doubleValue: float):
        self.__doubleValue = doubleValue

class thingml_BooleanLiteral(Literal):

    def __init__(self, boolValue: bool):
        self.boolValue = boolValue
        
    @property
    def boolValue(self) -> bool:
        return self.__boolValue

    @boolValue.setter
    def boolValue(self, boolValue: bool):
        self.__boolValue = boolValue

class thingml_IntegerLiteral(Literal):

    def __init__(self, intValue: int):
        self.intValue = intValue
        
    @property
    def intValue(self) -> int:
        return self.__intValue

    @intValue.setter
    def intValue(self, intValue: int):
        self.__intValue = intValue

class thingml_StringLiteral(Literal):

    def __init__(self, stringValue: str):
        self.stringValue = stringValue
        
    @property
    def stringValue(self) -> str:
        return self.__stringValue

    @stringValue.setter
    def stringValue(self, stringValue: str):
        self.__stringValue = stringValue

class thingml_EnumLiteralRef(Literal):

    pass
class BinaryExpression:

    pass
class thingml_LowerExpression(BinaryExpression):

    pass
class thingml_MinusExpression(BinaryExpression):

    pass
class thingml_ModExpression(BinaryExpression):

    pass
class thingml_TimesExpression(BinaryExpression):

    pass
class thingml_OrExpression(BinaryExpression):

    pass
class thingml_AndExpression(BinaryExpression):

    pass
class thingml_GreaterExpression(BinaryExpression):

    pass
class thingml_EqualsExpression(BinaryExpression):

    pass
class thingml_DivExpression(BinaryExpression):

    pass
class thingml_PlusExpression(BinaryExpression):

    pass
class Property:

    pass
class thingml_Dictionary(Property):

    pass
class Event:

    pass
class thingml_ReceiveMessage(Event):

    pass
class Port:

    pass
class thingml_ProvidedPort(Port):

    pass
class thingml_RequiredPort(Port):

    def __init__(self, optional: bool, thingml_RequiredPort: "thingml_Connector" = None):
        self.optional = optional
        self.thingml_RequiredPort = thingml_RequiredPort
        
    @property
    def optional(self) -> bool:
        return self.__optional

    @optional.setter
    def optional(self, optional: bool):
        self.__optional = optional

    @property
    def thingml_RequiredPort(self):
        return self.__thingml_RequiredPort

    @thingml_RequiredPort.setter
    def thingml_RequiredPort(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingml_RequiredPort__thingml_RequiredPort", None)
        self.__thingml_RequiredPort = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingml_Connector170"):
                opp_val = getattr(old_value, "thingml_Connector170", None)
                if opp_val == self:
                    setattr(old_value, "thingml_Connector170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingml_Connector170"):
                opp_val = getattr(value, "thingml_Connector170", None)
                setattr(value, "thingml_Connector170", self)

class Region:

    pass
class thingml_ParallelRegion(Region):

    pass
class State:

    pass
class thingml_CompositeState(State, Region):

    pass
class Expression:

    pass
class thingml_ArrayIndex(Expression):

    pass
class thingml_BinaryExpression(Expression):

    pass
class thingml_EventReference(Expression):

    pass
class thingml_PropertyReference(Expression):

    pass
class thingml_Literal(Expression):

    pass
class thingml_UnaryExpression(Expression):

    pass
class thingml_ExpressionGroup(Expression):

    pass
class thingml_FunctionCallExpression(FunctionCall, Expression):

    pass
class thingml_ExternExpression(Expression):

    def __init__(self, expression: str, thingml_ExternExpression: set["thingml_Expression"] = None):
        self.expression = expression
        self.thingml_ExternExpression = thingml_ExternExpression if thingml_ExternExpression is not None else set()
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def thingml_ExternExpression(self):
        return self.__thingml_ExternExpression

    @thingml_ExternExpression.setter
    def thingml_ExternExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingml_ExternExpression__thingml_ExternExpression", None)
        self.__thingml_ExternExpression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingml_Expression84"):
                    opp_val = getattr(item, "thingml_Expression84", None)
                    
                    if opp_val == self:
                        setattr(item, "thingml_Expression84", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingml_Expression84"):
                    opp_val = getattr(item, "thingml_Expression84", None)
                    
                    setattr(item, "thingml_Expression84", self)
                    

class Action:

    pass
class thingml_ReturnAction(Action):

    pass
class thingml_VariableAssignment(Action):

    pass
class thingml_SendAction(Action):

    pass
class thingml_ControlStructure(Action):

    pass
class thingml_FunctionCallStatement(FunctionCall, Action):

    pass
class thingml_ErrorAction(Action):

    pass
class thingml_ExternStatement(Action):

    def __init__(self, statement: str, thingml_ExternStatement: set["thingml_Expression"] = None):
        self.statement = statement
        self.thingml_ExternStatement = thingml_ExternStatement if thingml_ExternStatement is not None else set()
        
    @property
    def statement(self) -> str:
        return self.__statement

    @statement.setter
    def statement(self, statement: str):
        self.__statement = statement

    @property
    def thingml_ExternStatement(self):
        return self.__thingml_ExternStatement

    @thingml_ExternStatement.setter
    def thingml_ExternStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingml_ExternStatement__thingml_ExternStatement", None)
        self.__thingml_ExternStatement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingml_Expression82"):
                    opp_val = getattr(item, "thingml_Expression82", None)
                    
                    if opp_val == self:
                        setattr(item, "thingml_Expression82", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingml_Expression82"):
                    opp_val = getattr(item, "thingml_Expression82", None)
                    
                    setattr(item, "thingml_Expression82", self)
                    

class thingml_PrintAction(Action):

    pass
class thingml_ActionBlock(Action):

    pass
class CompositeState:

    pass
class ThingMLElement:

    pass
class thingml_Event(ThingMLElement):

    pass
class thingml_AnnotatedElement(ThingMLElement):

    pass
class thingml_PlatformAnnotation(ThingMLElement):

    def __init__(self, value: str, thingml_PlatformAnnotation: "thingml_AnnotatedElement" = None):
        self.value = value
        self.thingml_PlatformAnnotation = thingml_PlatformAnnotation
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def thingml_PlatformAnnotation(self):
        return self.__thingml_PlatformAnnotation

    @thingml_PlatformAnnotation.setter
    def thingml_PlatformAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingml_PlatformAnnotation__thingml_PlatformAnnotation", None)
        self.__thingml_PlatformAnnotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingml_AnnotatedElement"):
                opp_val = getattr(old_value, "thingml_AnnotatedElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingml_AnnotatedElement"):
                opp_val = getattr(value, "thingml_AnnotatedElement", None)
                if opp_val is None:
                    setattr(value, "thingml_AnnotatedElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Handler:

    pass
class thingml_InternalTransition(Handler):

    pass
class thingml_Transition(Handler):

    pass
class Variable:

    pass
class thingml_LocalVariable(Variable, Action):

    def __init__(self, changeable: bool, thingml_LocalVariable: "thingml_Expression" = None):
        self.changeable = changeable
        self.thingml_LocalVariable = thingml_LocalVariable
        
    @property
    def changeable(self) -> bool:
        return self.__changeable

    @changeable.setter
    def changeable(self, changeable: bool):
        self.__changeable = changeable

    @property
    def thingml_LocalVariable(self):
        return self.__thingml_LocalVariable

    @thingml_LocalVariable.setter
    def thingml_LocalVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingml_LocalVariable__thingml_LocalVariable", None)
        self.__thingml_LocalVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingml_Expression200"):
                opp_val = getattr(old_value, "thingml_Expression200", None)
                if opp_val == self:
                    setattr(old_value, "thingml_Expression200", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingml_Expression200"):
                opp_val = getattr(value, "thingml_Expression200", None)
                setattr(value, "thingml_Expression200", self)

class thingml_StateMachine(CompositeState):

    pass
class thingml_Property(Variable):

    def __init__(self, changeable: bool, thingml_Property: "thingml_Thing" = None, thingml_Property31: "thingml_Expression" = None, thingml_Property38: "thingml_PropertyAssign" = None, thingml_Property70: "thingml_State" = None, thingml_Property178: "thingml_ConfigPropertyAssign" = None):
        self.changeable = changeable
        self.thingml_Property = thingml_Property
        self.thingml_Property31 = thingml_Property31
        self.thingml_Property38 = thingml_Property38
        self.thingml_Property70 = thingml_Property70
        self.thingml_Property178 = thingml_Property178
        
    @property
    def changeable(self) -> bool:
        return self.__changeable

    @changeable.setter
    def changeable(self, changeable: bool):
        self.__changeable = changeable

    @property
    def thingml_Property70(self):
        return self.__thingml_Property70

    @thingml_Property70.setter
    def thingml_Property70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingml_Property__thingml_Property70", None)
        self.__thingml_Property70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingml_State69"):
                opp_val = getattr(old_value, "thingml_State69", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingml_State69"):
                opp_val = getattr(value, "thingml_State69", None)
                if opp_val is None:
                    setattr(value, "thingml_State69", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def thingml_Property38(self):
        return self.__thingml_Property38

    @thingml_Property38.setter
    def thingml_Property38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingml_Property__thingml_Property38", None)
        self.__thingml_Property38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingml_PropertyAssign37"):
                opp_val = getattr(old_value, "thingml_PropertyAssign37", None)
                if opp_val == self:
                    setattr(old_value, "thingml_PropertyAssign37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingml_PropertyAssign37"):
                opp_val = getattr(value, "thingml_PropertyAssign37", None)
                setattr(value, "thingml_PropertyAssign37", self)

    @property
    def thingml_Property31(self):
        return self.__thingml_Property31

    @thingml_Property31.setter
    def thingml_Property31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingml_Property__thingml_Property31", None)
        self.__thingml_Property31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingml_Expression32"):
                opp_val = getattr(old_value, "thingml_Expression32", None)
                if opp_val == self:
                    setattr(old_value, "thingml_Expression32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingml_Expression32"):
                opp_val = getattr(value, "thingml_Expression32", None)
                setattr(value, "thingml_Expression32", self)

    @property
    def thingml_Property178(self):
        return self.__thingml_Property178

    @thingml_Property178.setter
    def thingml_Property178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingml_Property__thingml_Property178", None)
        self.__thingml_Property178 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingml_ConfigPropertyAssign177"):
                opp_val = getattr(old_value, "thingml_ConfigPropertyAssign177", None)
                if opp_val == self:
                    setattr(old_value, "thingml_ConfigPropertyAssign177", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingml_ConfigPropertyAssign177"):
                opp_val = getattr(value, "thingml_ConfigPropertyAssign177", None)
                setattr(value, "thingml_ConfigPropertyAssign177", self)

    @property
    def thingml_Property(self):
        return self.__thingml_Property

    @thingml_Property.setter
    def thingml_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingml_Property__thingml_Property", None)
        self.__thingml_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingml_Thing"):
                opp_val = getattr(old_value, "thingml_Thing", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingml_Thing"):
                opp_val = getattr(value, "thingml_Thing", None)
                if opp_val is None:
                    setattr(value, "thingml_Thing", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Type:

    pass
class thingml_Enumeration(Type):

    pass
class thingml_PrimitiveType(Type):

    pass
class thingml_Thing(Type):

    def __init__(self, fragment: bool, thingml_Thing: set["thingml_Property"] = None, owner: set["thingml_Port"] = None, thingml_Thing14: set["thingml_StateMachine"] = None, thingml_Thing17: "thingml_Thing" = None, thingml_Thing15: set["thingml_Thing"] = None, thingml_Thing19: set["thingml_PropertyAssign"] = None, thingml_Thing21: set["thingml_Message"] = None, thingml_Thing24: set["thingml_Function"] = None, Thing: "thingml_Port" = None, thingml_Thing160: "thingml_Instance" = None):
        self.fragment = fragment
        self.thingml_Thing = thingml_Thing if thingml_Thing is not None else set()
        self.owner = owner if owner is not None else set()
        self.thingml_Thing14 = thingml_Thing14 if thingml_Thing14 is not None else set()
        self.thingml_Thing17 = thingml_Thing17
        self.thingml_Thing15 = thingml_Thing15 if thingml_Thing15 is not None else set()
        self.thingml_Thing19 = thingml_Thing19 if thingml_Thing19 is not None else set()
        self.thingml_Thing21 = thingml_Thing21 if thingml_Thing21 is not None else set()
        self.thingml_Thing24 = thingml_Thing24 if thingml_Thing24 is not None else set()
        self.Thing = Thing
        self.thingml_Thing160 = thingml_Thing160
        
    @property
    def fragment(self) -> bool:
        return self.__fragment

    @fragment.setter
    def fragment(self, fragment: bool):
        self.__fragment = fragment

    @property
    def Thing(self):
        return self.__Thing

    @Thing.setter
    def Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingml_Thing__Thing", None)
        self.__Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ports"):
                opp_val = getattr(old_value, "ports", None)
                if opp_val == self:
                    setattr(old_value, "ports", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ports"):
                opp_val = getattr(value, "ports", None)
                setattr(value, "ports", self)

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingml_Thing__owner", None)
        self.__owner = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Port"):
                    opp_val = getattr(item, "Port", None)
                    
                    if opp_val == self:
                        setattr(item, "Port", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Port"):
                    opp_val = getattr(item, "Port", None)
                    
                    setattr(item, "Port", self)
                    

    @property
    def thingml_Thing19(self):
        return self.__thingml_Thing19

    @thingml_Thing19.setter
    def thingml_Thing19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingml_Thing__thingml_Thing19", None)
        self.__thingml_Thing19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingml_PropertyAssign"):
                    opp_val = getattr(item, "thingml_PropertyAssign", None)
                    
                    if opp_val == self:
                        setattr(item, "thingml_PropertyAssign", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingml_PropertyAssign"):
                    opp_val = getattr(item, "thingml_PropertyAssign", None)
                    
                    setattr(item, "thingml_PropertyAssign", self)
                    

    @property
    def thingml_Thing160(self):
        return self.__thingml_Thing160

    @thingml_Thing160.setter
    def thingml_Thing160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingml_Thing__thingml_Thing160", None)
        self.__thingml_Thing160 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingml_Instance159"):
                opp_val = getattr(old_value, "thingml_Instance159", None)
                if opp_val == self:
                    setattr(old_value, "thingml_Instance159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingml_Instance159"):
                opp_val = getattr(value, "thingml_Instance159", None)
                setattr(value, "thingml_Instance159", self)

    @property
    def thingml_Thing14(self):
        return self.__thingml_Thing14

    @thingml_Thing14.setter
    def thingml_Thing14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingml_Thing__thingml_Thing14", None)
        self.__thingml_Thing14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingml_StateMachine"):
                    opp_val = getattr(item, "thingml_StateMachine", None)
                    
                    if opp_val == self:
                        setattr(item, "thingml_StateMachine", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingml_StateMachine"):
                    opp_val = getattr(item, "thingml_StateMachine", None)
                    
                    setattr(item, "thingml_StateMachine", self)
                    

    @property
    def thingml_Thing24(self):
        return self.__thingml_Thing24

    @thingml_Thing24.setter
    def thingml_Thing24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingml_Thing__thingml_Thing24", None)
        self.__thingml_Thing24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingml_Function25"):
                    opp_val = getattr(item, "thingml_Function25", None)
                    
                    if opp_val == self:
                        setattr(item, "thingml_Function25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingml_Function25"):
                    opp_val = getattr(item, "thingml_Function25", None)
                    
                    setattr(item, "thingml_Function25", self)
                    

    @property
    def thingml_Thing17(self):
        return self.__thingml_Thing17

    @thingml_Thing17.setter
    def thingml_Thing17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingml_Thing__thingml_Thing17", None)
        self.__thingml_Thing17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingml_Thing15"):
                opp_val = getattr(old_value, "thingml_Thing15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingml_Thing15"):
                opp_val = getattr(value, "thingml_Thing15", None)
                if opp_val is None:
                    setattr(value, "thingml_Thing15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def thingml_Thing21(self):
        return self.__thingml_Thing21

    @thingml_Thing21.setter
    def thingml_Thing21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingml_Thing__thingml_Thing21", None)
        self.__thingml_Thing21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingml_Message22"):
                    opp_val = getattr(item, "thingml_Message22", None)
                    
                    if opp_val == self:
                        setattr(item, "thingml_Message22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingml_Message22"):
                    opp_val = getattr(item, "thingml_Message22", None)
                    
                    setattr(item, "thingml_Message22", self)
                    

    @property
    def thingml_Thing(self):
        return self.__thingml_Thing

    @thingml_Thing.setter
    def thingml_Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingml_Thing__thingml_Thing", None)
        self.__thingml_Thing = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingml_Property"):
                    opp_val = getattr(item, "thingml_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "thingml_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingml_Property"):
                    opp_val = getattr(item, "thingml_Property", None)
                    
                    setattr(item, "thingml_Property", self)
                    

    @property
    def thingml_Thing15(self):
        return self.__thingml_Thing15

    @thingml_Thing15.setter
    def thingml_Thing15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingml_Thing__thingml_Thing15", None)
        self.__thingml_Thing15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingml_Thing17"):
                    opp_val = getattr(item, "thingml_Thing17", None)
                    
                    if opp_val == self:
                        setattr(item, "thingml_Thing17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingml_Thing17"):
                    opp_val = getattr(item, "thingml_Thing17", None)
                    
                    setattr(item, "thingml_Thing17", self)
                    

class thingml_Action(ABC):

    pass
class thingml_Expression(ABC):

    pass
class thingml_TypedElement(ABC):

    pass
class thingml_ThingMLElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class thingml_ThingMLModel:

    pass
class thingml_Parameter(Variable):

    pass
class TypedElement:

    pass
class AnnotatedElement:

    pass
class thingml_Type(AnnotatedElement):

    pass
class thingml_ConfigInclude(AnnotatedElement):

    pass
class thingml_Handler(AnnotatedElement):

    pass
class thingml_PropertyAssign(AnnotatedElement):

    pass
class thingml_Region(AnnotatedElement):

    def __init__(self, history: bool, thingml_Region: set["thingml_State"] = None, thingml_Region77: "thingml_State" = None):
        self.history = history
        self.thingml_Region = thingml_Region if thingml_Region is not None else set()
        self.thingml_Region77 = thingml_Region77
        
    @property
    def history(self) -> bool:
        return self.__history

    @history.setter
    def history(self, history: bool):
        self.__history = history

    @property
    def thingml_Region77(self):
        return self.__thingml_Region77

    @thingml_Region77.setter
    def thingml_Region77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingml_Region__thingml_Region77", None)
        self.__thingml_Region77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingml_State78"):
                opp_val = getattr(old_value, "thingml_State78", None)
                if opp_val == self:
                    setattr(old_value, "thingml_State78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingml_State78"):
                opp_val = getattr(value, "thingml_State78", None)
                setattr(value, "thingml_State78", self)

    @property
    def thingml_Region(self):
        return self.__thingml_Region

    @thingml_Region.setter
    def thingml_Region(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingml_Region__thingml_Region", None)
        self.__thingml_Region = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingml_State75"):
                    opp_val = getattr(item, "thingml_State75", None)
                    
                    if opp_val == self:
                        setattr(item, "thingml_State75", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingml_State75"):
                    opp_val = getattr(item, "thingml_State75", None)
                    
                    setattr(item, "thingml_State75", self)
                    

class thingml_Message(AnnotatedElement):

    pass
class thingml_ConfigPropertyAssign(AnnotatedElement):

    pass
class thingml_State(AnnotatedElement):

    pass
class thingml_Port(AnnotatedElement):

    pass
class thingml_Connector(AnnotatedElement):

    pass
class thingml_Instance(AnnotatedElement):

    pass
class thingml_EnumerationLiteral(AnnotatedElement):

    pass
class thingml_Variable(AnnotatedElement, TypedElement):

    pass
class thingml_Configuration(AnnotatedElement):

    def __init__(self, fragment: bool, thingml_Configuration: "thingml_ThingMLModel" = None, thingml_Configuration151: set["thingml_Instance"] = None, thingml_Configuration187: "thingml_ConfigInclude" = None, thingml_Configuration153: set["thingml_Connector"] = None, thingml_Configuration155: set["thingml_ConfigInclude"] = None, thingml_Configuration157: set["thingml_ConfigPropertyAssign"] = None):
        self.fragment = fragment
        self.thingml_Configuration = thingml_Configuration
        self.thingml_Configuration151 = thingml_Configuration151 if thingml_Configuration151 is not None else set()
        self.thingml_Configuration187 = thingml_Configuration187
        self.thingml_Configuration153 = thingml_Configuration153 if thingml_Configuration153 is not None else set()
        self.thingml_Configuration155 = thingml_Configuration155 if thingml_Configuration155 is not None else set()
        self.thingml_Configuration157 = thingml_Configuration157 if thingml_Configuration157 is not None else set()
        
    @property
    def fragment(self) -> bool:
        return self.__fragment

    @fragment.setter
    def fragment(self, fragment: bool):
        self.__fragment = fragment

    @property
    def thingml_Configuration(self):
        return self.__thingml_Configuration

    @thingml_Configuration.setter
    def thingml_Configuration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingml_Configuration__thingml_Configuration", None)
        self.__thingml_Configuration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingml_ThingMLModel5"):
                opp_val = getattr(old_value, "thingml_ThingMLModel5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingml_ThingMLModel5"):
                opp_val = getattr(value, "thingml_ThingMLModel5", None)
                if opp_val is None:
                    setattr(value, "thingml_ThingMLModel5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def thingml_Configuration153(self):
        return self.__thingml_Configuration153

    @thingml_Configuration153.setter
    def thingml_Configuration153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingml_Configuration__thingml_Configuration153", None)
        self.__thingml_Configuration153 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingml_Connector"):
                    opp_val = getattr(item, "thingml_Connector", None)
                    
                    if opp_val == self:
                        setattr(item, "thingml_Connector", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingml_Connector"):
                    opp_val = getattr(item, "thingml_Connector", None)
                    
                    setattr(item, "thingml_Connector", self)
                    

    @property
    def thingml_Configuration151(self):
        return self.__thingml_Configuration151

    @thingml_Configuration151.setter
    def thingml_Configuration151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingml_Configuration__thingml_Configuration151", None)
        self.__thingml_Configuration151 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingml_Instance"):
                    opp_val = getattr(item, "thingml_Instance", None)
                    
                    if opp_val == self:
                        setattr(item, "thingml_Instance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingml_Instance"):
                    opp_val = getattr(item, "thingml_Instance", None)
                    
                    setattr(item, "thingml_Instance", self)
                    

    @property
    def thingml_Configuration155(self):
        return self.__thingml_Configuration155

    @thingml_Configuration155.setter
    def thingml_Configuration155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingml_Configuration__thingml_Configuration155", None)
        self.__thingml_Configuration155 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingml_ConfigInclude"):
                    opp_val = getattr(item, "thingml_ConfigInclude", None)
                    
                    if opp_val == self:
                        setattr(item, "thingml_ConfigInclude", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingml_ConfigInclude"):
                    opp_val = getattr(item, "thingml_ConfigInclude", None)
                    
                    setattr(item, "thingml_ConfigInclude", self)
                    

    @property
    def thingml_Configuration157(self):
        return self.__thingml_Configuration157

    @thingml_Configuration157.setter
    def thingml_Configuration157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingml_Configuration__thingml_Configuration157", None)
        self.__thingml_Configuration157 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingml_ConfigPropertyAssign"):
                    opp_val = getattr(item, "thingml_ConfigPropertyAssign", None)
                    
                    if opp_val == self:
                        setattr(item, "thingml_ConfigPropertyAssign", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingml_ConfigPropertyAssign"):
                    opp_val = getattr(item, "thingml_ConfigPropertyAssign", None)
                    
                    setattr(item, "thingml_ConfigPropertyAssign", self)
                    

    @property
    def thingml_Configuration187(self):
        return self.__thingml_Configuration187

    @thingml_Configuration187.setter
    def thingml_Configuration187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingml_Configuration__thingml_Configuration187", None)
        self.__thingml_Configuration187 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingml_ConfigInclude186"):
                opp_val = getattr(old_value, "thingml_ConfigInclude186", None)
                if opp_val == self:
                    setattr(old_value, "thingml_ConfigInclude186", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingml_ConfigInclude186"):
                opp_val = getattr(value, "thingml_ConfigInclude186", None)
                setattr(value, "thingml_ConfigInclude186", self)

class thingml_Function(AnnotatedElement, TypedElement):

    pass