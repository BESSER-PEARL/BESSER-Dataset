from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class AbstractConnector:

    pass
class thingML_Connector(AbstractConnector):

    pass
class thingML_ExternalConnector(AbstractConnector):

    pass
class thingML_ConfigPropertyAssign:

    pass
class Literal:

    pass
class thingML_IntegerLiteral(Literal):

    def __init__(self, intValue: str):
        self.intValue = intValue
        
    @property
    def intValue(self) -> str:
        return self.__intValue

    @intValue.setter
    def intValue(self, intValue: str):
        self.__intValue = intValue

class thingML_CharLiteral(Literal):

    def __init__(self, charValue: str):
        self.charValue = charValue
        
    @property
    def charValue(self) -> str:
        return self.__charValue

    @charValue.setter
    def charValue(self, charValue: str):
        self.__charValue = charValue

class thingML_ByteLiteral(Literal):

    def __init__(self, byteValue: str):
        self.byteValue = byteValue
        
    @property
    def byteValue(self) -> str:
        return self.__byteValue

    @byteValue.setter
    def byteValue(self, byteValue: str):
        self.__byteValue = byteValue

class thingML_EnumLiteralRef(Literal):

    pass
class thingML_DoubleLiteral(Literal):

    def __init__(self, doubleValue: float):
        self.doubleValue = doubleValue
        
    @property
    def doubleValue(self) -> float:
        return self.__doubleValue

    @doubleValue.setter
    def doubleValue(self, doubleValue: float):
        self.__doubleValue = doubleValue

class thingML_StringLiteral(Literal):

    def __init__(self, stringValue: str):
        self.stringValue = stringValue
        
    @property
    def stringValue(self) -> str:
        return self.__stringValue

    @stringValue.setter
    def stringValue(self, stringValue: str):
        self.__stringValue = stringValue

class thingML_BooleanLiteral(Literal):

    def __init__(self, boolValue: bool):
        self.boolValue = boolValue
        
    @property
    def boolValue(self) -> bool:
        return self.__boolValue

    @boolValue.setter
    def boolValue(self, boolValue: bool):
        self.__boolValue = boolValue

class Expression:

    pass
class thingML_ModExpression(Expression):

    pass
class thingML_GreaterExpression(Expression):

    pass
class thingML_MinusExpression(Expression):

    pass
class thingML_UnaryMinus(Expression):

    pass
class thingML_LowerExpression(Expression):

    pass
class thingML_EventReference(Expression):

    pass
class thingML_NotExpression(Expression):

    pass
class thingML_ExpressionGroup(Expression):

    pass
class thingML_DivExpression(Expression):

    pass
class thingML_OrExpression(Expression):

    pass
class thingML_PlusExpression(Expression):

    pass
class thingML_AndExpression(Expression):

    pass
class thingML_ArrayIndex(Expression):

    pass
class thingML_NotEqualsExpression(Expression):

    pass
class thingML_GreaterOrEqualExpression(Expression):

    pass
class thingML_LowerOrEqualExpression(Expression):

    pass
class thingML_TimesExpression(Expression):

    pass
class thingML_CastExpression(Expression):

    def __init__(self, isArray: bool, thingML_CastExpression: "thingML_Expression" = None, thingML_CastExpression294: "thingML_Type" = None):
        self.isArray = isArray
        self.thingML_CastExpression = thingML_CastExpression
        self.thingML_CastExpression294 = thingML_CastExpression294
        
    @property
    def isArray(self) -> bool:
        return self.__isArray

    @isArray.setter
    def isArray(self, isArray: bool):
        self.__isArray = isArray

    @property
    def thingML_CastExpression(self):
        return self.__thingML_CastExpression

    @thingML_CastExpression.setter
    def thingML_CastExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_CastExpression__thingML_CastExpression", None)
        self.__thingML_CastExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Expression292"):
                opp_val = getattr(old_value, "thingML_Expression292", None)
                if opp_val == self:
                    setattr(old_value, "thingML_Expression292", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Expression292"):
                opp_val = getattr(value, "thingML_Expression292", None)
                setattr(value, "thingML_Expression292", self)

    @property
    def thingML_CastExpression294(self):
        return self.__thingML_CastExpression294

    @thingML_CastExpression294.setter
    def thingML_CastExpression294(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_CastExpression__thingML_CastExpression294", None)
        self.__thingML_CastExpression294 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Type295"):
                opp_val = getattr(old_value, "thingML_Type295", None)
                if opp_val == self:
                    setattr(old_value, "thingML_Type295", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Type295"):
                opp_val = getattr(value, "thingML_Type295", None)
                setattr(value, "thingML_Type295", self)

class thingML_ArrayInit(Expression):

    pass
class thingML_FunctionCallExpression(Expression):

    pass
class thingML_EqualsExpression(Expression):

    pass
class thingML_ExternExpression(Expression):

    def __init__(self, expression: str, thingML_ExternExpression: set["thingML_Expression"] = None):
        self.expression = expression
        self.thingML_ExternExpression = thingML_ExternExpression if thingML_ExternExpression is not None else set()
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def thingML_ExternExpression(self):
        return self.__thingML_ExternExpression

    @thingML_ExternExpression.setter
    def thingML_ExternExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_ExternExpression__thingML_ExternExpression", None)
        self.__thingML_ExternExpression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingML_Expression164"):
                    opp_val = getattr(item, "thingML_Expression164", None)
                    
                    if opp_val == self:
                        setattr(item, "thingML_Expression164", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingML_Expression164"):
                    opp_val = getattr(item, "thingML_Expression164", None)
                    
                    setattr(item, "thingML_Expression164", self)
                    

class thingML_PropertyReference(Expression):

    pass
class StateContainer:

    pass
class thingML_Region(StateContainer):

    pass
class thingML_Session(StateContainer):

    pass
class State:

    pass
class thingML_FinalState(State):

    pass
class Handler:

    pass
class Action:

    pass
class thingML_ForAction(Action):

    pass
class thingML_Increment(Action):

    pass
class thingML_LoopAction(Action):

    pass
class thingML_ReturnAction(Action):

    pass
class thingML_PrintAction(Action):

    def __init__(self, line: bool, thingML_PrintAction: set["thingML_Expression"] = None):
        self.line = line
        self.thingML_PrintAction = thingML_PrintAction if thingML_PrintAction is not None else set()
        
    @property
    def line(self) -> bool:
        return self.__line

    @line.setter
    def line(self, line: bool):
        self.__line = line

    @property
    def thingML_PrintAction(self):
        return self.__thingML_PrintAction

    @thingML_PrintAction.setter
    def thingML_PrintAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_PrintAction__thingML_PrintAction", None)
        self.__thingML_PrintAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingML_Expression153"):
                    opp_val = getattr(item, "thingML_Expression153", None)
                    
                    if opp_val == self:
                        setattr(item, "thingML_Expression153", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingML_Expression153"):
                    opp_val = getattr(item, "thingML_Expression153", None)
                    
                    setattr(item, "thingML_Expression153", self)
                    

class thingML_ExternStatement(Action):

    def __init__(self, statement: str, thingML_ExternStatement: set["thingML_Expression"] = None):
        self.statement = statement
        self.thingML_ExternStatement = thingML_ExternStatement if thingML_ExternStatement is not None else set()
        
    @property
    def statement(self) -> str:
        return self.__statement

    @statement.setter
    def statement(self, statement: str):
        self.__statement = statement

    @property
    def thingML_ExternStatement(self):
        return self.__thingML_ExternStatement

    @thingML_ExternStatement.setter
    def thingML_ExternStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_ExternStatement__thingML_ExternStatement", None)
        self.__thingML_ExternStatement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingML_Expression104"):
                    opp_val = getattr(item, "thingML_Expression104", None)
                    
                    if opp_val == self:
                        setattr(item, "thingML_Expression104", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingML_Expression104"):
                    opp_val = getattr(item, "thingML_Expression104", None)
                    
                    setattr(item, "thingML_Expression104", self)
                    

class thingML_StartSession(Action):

    pass
class thingML_Decrement(Action):

    pass
class thingML_FunctionCallStatement(Action):

    pass
class thingML_SendAction(Action):

    pass
class thingML_VariableAssignment(Action):

    pass
class thingML_ConditionalAction(Action):

    pass
class thingML_ErrorAction(Action):

    def __init__(self, line: bool, thingML_ErrorAction: set["thingML_Expression"] = None):
        self.line = line
        self.thingML_ErrorAction = thingML_ErrorAction if thingML_ErrorAction is not None else set()
        
    @property
    def line(self) -> bool:
        return self.__line

    @line.setter
    def line(self, line: bool):
        self.__line = line

    @property
    def thingML_ErrorAction(self):
        return self.__thingML_ErrorAction

    @thingML_ErrorAction.setter
    def thingML_ErrorAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_ErrorAction__thingML_ErrorAction", None)
        self.__thingML_ErrorAction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingML_Expression155"):
                    opp_val = getattr(item, "thingML_Expression155", None)
                    
                    if opp_val == self:
                        setattr(item, "thingML_Expression155", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingML_Expression155"):
                    opp_val = getattr(item, "thingML_Expression155", None)
                    
                    setattr(item, "thingML_Expression155", self)
                    

class thingML_ActionBlock(Action):

    pass
class Event:

    pass
class thingML_ReceiveMessage(Event):

    pass
class Port:

    pass
class thingML_ProvidedPort(Port):

    pass
class thingML_RequiredPort(Port):

    def __init__(self, optional: bool, thingML_RequiredPort: "thingML_Connector" = None):
        self.optional = optional
        self.thingML_RequiredPort = thingML_RequiredPort
        
    @property
    def optional(self) -> bool:
        return self.__optional

    @optional.setter
    def optional(self, optional: bool):
        self.__optional = optional

    @property
    def thingML_RequiredPort(self):
        return self.__thingML_RequiredPort

    @thingML_RequiredPort.setter
    def thingML_RequiredPort(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_RequiredPort__thingML_RequiredPort", None)
        self.__thingML_RequiredPort = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Connector212"):
                opp_val = getattr(old_value, "thingML_Connector212", None)
                if opp_val == self:
                    setattr(old_value, "thingML_Connector212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Connector212"):
                opp_val = getattr(value, "thingML_Connector212", None)
                setattr(value, "thingML_Connector212", self)

class Variable:

    pass
class thingML_LocalVariable(Variable, Action):

    def __init__(self, readonly: bool, thingML_LocalVariable: "thingML_Expression" = None):
        self.readonly = readonly
        self.thingML_LocalVariable = thingML_LocalVariable
        
    @property
    def readonly(self) -> bool:
        return self.__readonly

    @readonly.setter
    def readonly(self, readonly: bool):
        self.__readonly = readonly

    @property
    def thingML_LocalVariable(self):
        return self.__thingML_LocalVariable

    @thingML_LocalVariable.setter
    def thingML_LocalVariable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_LocalVariable__thingML_LocalVariable", None)
        self.__thingML_LocalVariable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Expression106"):
                opp_val = getattr(old_value, "thingML_Expression106", None)
                if opp_val == self:
                    setattr(old_value, "thingML_Expression106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Expression106"):
                opp_val = getattr(value, "thingML_Expression106", None)
                setattr(value, "thingML_Expression106", self)

class thingML_Transition(Handler):

    pass
class thingML_InternalTransition(Handler):

    pass
class thingML_InternalPort(Port):

    pass
class thingML_Property(Variable):

    def __init__(self, readonly: bool, thingML_Property36: "thingML_PropertyAssign" = None, thingML_Property: "thingML_Thing" = None, thingML_Property63: "thingML_State" = None, thingML_Property51: "thingML_Expression" = None, thingML_Property199: "thingML_ConfigPropertyAssign" = None):
        self.readonly = readonly
        self.thingML_Property36 = thingML_Property36
        self.thingML_Property = thingML_Property
        self.thingML_Property63 = thingML_Property63
        self.thingML_Property51 = thingML_Property51
        self.thingML_Property199 = thingML_Property199
        
    @property
    def readonly(self) -> bool:
        return self.__readonly

    @readonly.setter
    def readonly(self, readonly: bool):
        self.__readonly = readonly

    @property
    def thingML_Property(self):
        return self.__thingML_Property

    @thingML_Property.setter
    def thingML_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Property__thingML_Property", None)
        self.__thingML_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Thing27"):
                opp_val = getattr(old_value, "thingML_Thing27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Thing27"):
                opp_val = getattr(value, "thingML_Thing27", None)
                if opp_val is None:
                    setattr(value, "thingML_Thing27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def thingML_Property51(self):
        return self.__thingML_Property51

    @thingML_Property51.setter
    def thingML_Property51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Property__thingML_Property51", None)
        self.__thingML_Property51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Expression52"):
                opp_val = getattr(old_value, "thingML_Expression52", None)
                if opp_val == self:
                    setattr(old_value, "thingML_Expression52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Expression52"):
                opp_val = getattr(value, "thingML_Expression52", None)
                setattr(value, "thingML_Expression52", self)

    @property
    def thingML_Property36(self):
        return self.__thingML_Property36

    @thingML_Property36.setter
    def thingML_Property36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Property__thingML_Property36", None)
        self.__thingML_Property36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_PropertyAssign35"):
                opp_val = getattr(old_value, "thingML_PropertyAssign35", None)
                if opp_val == self:
                    setattr(old_value, "thingML_PropertyAssign35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_PropertyAssign35"):
                opp_val = getattr(value, "thingML_PropertyAssign35", None)
                setattr(value, "thingML_PropertyAssign35", self)

    @property
    def thingML_Property199(self):
        return self.__thingML_Property199

    @thingML_Property199.setter
    def thingML_Property199(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Property__thingML_Property199", None)
        self.__thingML_Property199 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_ConfigPropertyAssign198"):
                opp_val = getattr(old_value, "thingML_ConfigPropertyAssign198", None)
                if opp_val == self:
                    setattr(old_value, "thingML_ConfigPropertyAssign198", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_ConfigPropertyAssign198"):
                opp_val = getattr(value, "thingML_ConfigPropertyAssign198", None)
                setattr(value, "thingML_ConfigPropertyAssign198", self)

    @property
    def thingML_Property63(self):
        return self.__thingML_Property63

    @thingML_Property63.setter
    def thingML_Property63(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Property__thingML_Property63", None)
        self.__thingML_Property63 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_State"):
                opp_val = getattr(old_value, "thingML_State", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_State"):
                opp_val = getattr(value, "thingML_State", None)
                if opp_val is None:
                    setattr(value, "thingML_State", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class thingML_Action:

    pass
class thingML_Parameter(Variable):

    pass
class thingML_CompositeState(StateContainer, State):

    pass
class thingML_TypeRef:

    def __init__(self, isArray: bool, thingML_TypeRef13: "thingML_Expression" = None, thingML_TypeRef15: "thingML_Enumeration" = None, thingML_TypeRef: "thingML_Variable" = None, thingML_TypeRef10: "thingML_Type" = None, thingML_TypeRef47: "thingML_Function" = None):
        self.isArray = isArray
        self.thingML_TypeRef13 = thingML_TypeRef13
        self.thingML_TypeRef15 = thingML_TypeRef15
        self.thingML_TypeRef = thingML_TypeRef
        self.thingML_TypeRef10 = thingML_TypeRef10
        self.thingML_TypeRef47 = thingML_TypeRef47
        
    @property
    def isArray(self) -> bool:
        return self.__isArray

    @isArray.setter
    def isArray(self, isArray: bool):
        self.__isArray = isArray

    @property
    def thingML_TypeRef13(self):
        return self.__thingML_TypeRef13

    @thingML_TypeRef13.setter
    def thingML_TypeRef13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_TypeRef__thingML_TypeRef13", None)
        self.__thingML_TypeRef13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Expression"):
                opp_val = getattr(old_value, "thingML_Expression", None)
                if opp_val == self:
                    setattr(old_value, "thingML_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Expression"):
                opp_val = getattr(value, "thingML_Expression", None)
                setattr(value, "thingML_Expression", self)

    @property
    def thingML_TypeRef(self):
        return self.__thingML_TypeRef

    @thingML_TypeRef.setter
    def thingML_TypeRef(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_TypeRef__thingML_TypeRef", None)
        self.__thingML_TypeRef = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Variable"):
                opp_val = getattr(old_value, "thingML_Variable", None)
                if opp_val == self:
                    setattr(old_value, "thingML_Variable", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Variable"):
                opp_val = getattr(value, "thingML_Variable", None)
                setattr(value, "thingML_Variable", self)

    @property
    def thingML_TypeRef10(self):
        return self.__thingML_TypeRef10

    @thingML_TypeRef10.setter
    def thingML_TypeRef10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_TypeRef__thingML_TypeRef10", None)
        self.__thingML_TypeRef10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Type11"):
                opp_val = getattr(old_value, "thingML_Type11", None)
                if opp_val == self:
                    setattr(old_value, "thingML_Type11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Type11"):
                opp_val = getattr(value, "thingML_Type11", None)
                setattr(value, "thingML_Type11", self)

    @property
    def thingML_TypeRef15(self):
        return self.__thingML_TypeRef15

    @thingML_TypeRef15.setter
    def thingML_TypeRef15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_TypeRef__thingML_TypeRef15", None)
        self.__thingML_TypeRef15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Enumeration"):
                opp_val = getattr(old_value, "thingML_Enumeration", None)
                if opp_val == self:
                    setattr(old_value, "thingML_Enumeration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Enumeration"):
                opp_val = getattr(value, "thingML_Enumeration", None)
                setattr(value, "thingML_Enumeration", self)

    @property
    def thingML_TypeRef47(self):
        return self.__thingML_TypeRef47

    @thingML_TypeRef47.setter
    def thingML_TypeRef47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_TypeRef__thingML_TypeRef47", None)
        self.__thingML_TypeRef47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Function46"):
                opp_val = getattr(old_value, "thingML_Function46", None)
                if opp_val == self:
                    setattr(old_value, "thingML_Function46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Function46"):
                opp_val = getattr(value, "thingML_Function46", None)
                setattr(value, "thingML_Function46", self)

class AnnotatedElement:

    pass
class thingML_PropertyAssign(AnnotatedElement):

    pass
class NamedElement:

    pass
class thingML_Event(NamedElement):

    pass
class thingML_Function(NamedElement, AnnotatedElement):

    def __init__(self, abstract: bool, thingML_Function44: set["thingML_Parameter"] = None, thingML_Function46: "thingML_TypeRef" = None, thingML_Function49: "thingML_Action" = None, thingML_Function: "thingML_Thing" = None, thingML_Function159: "thingML_FunctionCallStatement" = None, thingML_Function181: "thingML_FunctionCallExpression" = None):
        self.abstract = abstract
        self.thingML_Function44 = thingML_Function44 if thingML_Function44 is not None else set()
        self.thingML_Function46 = thingML_Function46
        self.thingML_Function49 = thingML_Function49
        self.thingML_Function = thingML_Function
        self.thingML_Function159 = thingML_Function159
        self.thingML_Function181 = thingML_Function181
        
    @property
    def abstract(self) -> bool:
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: bool):
        self.__abstract = abstract

    @property
    def thingML_Function181(self):
        return self.__thingML_Function181

    @thingML_Function181.setter
    def thingML_Function181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Function__thingML_Function181", None)
        self.__thingML_Function181 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_FunctionCallExpression"):
                opp_val = getattr(old_value, "thingML_FunctionCallExpression", None)
                if opp_val == self:
                    setattr(old_value, "thingML_FunctionCallExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_FunctionCallExpression"):
                opp_val = getattr(value, "thingML_FunctionCallExpression", None)
                setattr(value, "thingML_FunctionCallExpression", self)

    @property
    def thingML_Function159(self):
        return self.__thingML_Function159

    @thingML_Function159.setter
    def thingML_Function159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Function__thingML_Function159", None)
        self.__thingML_Function159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_FunctionCallStatement"):
                opp_val = getattr(old_value, "thingML_FunctionCallStatement", None)
                if opp_val == self:
                    setattr(old_value, "thingML_FunctionCallStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_FunctionCallStatement"):
                opp_val = getattr(value, "thingML_FunctionCallStatement", None)
                setattr(value, "thingML_FunctionCallStatement", self)

    @property
    def thingML_Function46(self):
        return self.__thingML_Function46

    @thingML_Function46.setter
    def thingML_Function46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Function__thingML_Function46", None)
        self.__thingML_Function46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_TypeRef47"):
                opp_val = getattr(old_value, "thingML_TypeRef47", None)
                if opp_val == self:
                    setattr(old_value, "thingML_TypeRef47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_TypeRef47"):
                opp_val = getattr(value, "thingML_TypeRef47", None)
                setattr(value, "thingML_TypeRef47", self)

    @property
    def thingML_Function44(self):
        return self.__thingML_Function44

    @thingML_Function44.setter
    def thingML_Function44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Function__thingML_Function44", None)
        self.__thingML_Function44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingML_Parameter"):
                    opp_val = getattr(item, "thingML_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "thingML_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingML_Parameter"):
                    opp_val = getattr(item, "thingML_Parameter", None)
                    
                    setattr(item, "thingML_Parameter", self)
                    

    @property
    def thingML_Function49(self):
        return self.__thingML_Function49

    @thingML_Function49.setter
    def thingML_Function49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Function__thingML_Function49", None)
        self.__thingML_Function49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Action"):
                opp_val = getattr(old_value, "thingML_Action", None)
                if opp_val == self:
                    setattr(old_value, "thingML_Action", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Action"):
                opp_val = getattr(value, "thingML_Action", None)
                setattr(value, "thingML_Action", self)

    @property
    def thingML_Function(self):
        return self.__thingML_Function

    @thingML_Function.setter
    def thingML_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Function__thingML_Function", None)
        self.__thingML_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Thing29"):
                opp_val = getattr(old_value, "thingML_Thing29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Thing29"):
                opp_val = getattr(value, "thingML_Thing29", None)
                if opp_val is None:
                    setattr(value, "thingML_Thing29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class thingML_Instance(NamedElement, AnnotatedElement):

    pass
class thingML_Handler(NamedElement, AnnotatedElement):

    pass
class thingML_StateContainer(NamedElement, AnnotatedElement):

    def __init__(self, history: bool, thingML_StateContainer: "thingML_State" = None, thingML_StateContainer94: set["thingML_State"] = None):
        self.history = history
        self.thingML_StateContainer = thingML_StateContainer
        self.thingML_StateContainer94 = thingML_StateContainer94 if thingML_StateContainer94 is not None else set()
        
    @property
    def history(self) -> bool:
        return self.__history

    @history.setter
    def history(self, history: bool):
        self.__history = history

    @property
    def thingML_StateContainer(self):
        return self.__thingML_StateContainer

    @thingML_StateContainer.setter
    def thingML_StateContainer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_StateContainer__thingML_StateContainer", None)
        self.__thingML_StateContainer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_State92"):
                opp_val = getattr(old_value, "thingML_State92", None)
                if opp_val == self:
                    setattr(old_value, "thingML_State92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_State92"):
                opp_val = getattr(value, "thingML_State92", None)
                setattr(value, "thingML_State92", self)

    @property
    def thingML_StateContainer94(self):
        return self.__thingML_StateContainer94

    @thingML_StateContainer94.setter
    def thingML_StateContainer94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_StateContainer__thingML_StateContainer94", None)
        self.__thingML_StateContainer94 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingML_State95"):
                    opp_val = getattr(item, "thingML_State95", None)
                    
                    if opp_val == self:
                        setattr(item, "thingML_State95", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingML_State95"):
                    opp_val = getattr(item, "thingML_State95", None)
                    
                    setattr(item, "thingML_State95", self)
                    

class thingML_State(NamedElement, AnnotatedElement):

    pass
class thingML_Port(NamedElement, AnnotatedElement):

    pass
class thingML_AbstractConnector(NamedElement, AnnotatedElement):

    pass
class thingML_Variable(NamedElement, AnnotatedElement):

    pass
class thingML_AnnotatedElement:

    pass
class thingML_NamedElement:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class thingML_PlatformAnnotation:

    def __init__(self, name: str, value: str, thingML_PlatformAnnotation: "thingML_AnnotatedElement" = None, thingML_PlatformAnnotation208: "thingML_ConfigPropertyAssign" = None):
        self.name = name
        self.value = value
        self.thingML_PlatformAnnotation = thingML_PlatformAnnotation
        self.thingML_PlatformAnnotation208 = thingML_PlatformAnnotation208
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def thingML_PlatformAnnotation(self):
        return self.__thingML_PlatformAnnotation

    @thingML_PlatformAnnotation.setter
    def thingML_PlatformAnnotation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_PlatformAnnotation__thingML_PlatformAnnotation", None)
        self.__thingML_PlatformAnnotation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_AnnotatedElement"):
                opp_val = getattr(old_value, "thingML_AnnotatedElement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_AnnotatedElement"):
                opp_val = getattr(value, "thingML_AnnotatedElement", None)
                if opp_val is None:
                    setattr(value, "thingML_AnnotatedElement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def thingML_PlatformAnnotation208(self):
        return self.__thingML_PlatformAnnotation208

    @thingML_PlatformAnnotation208.setter
    def thingML_PlatformAnnotation208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_PlatformAnnotation__thingML_PlatformAnnotation208", None)
        self.__thingML_PlatformAnnotation208 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_ConfigPropertyAssign207"):
                opp_val = getattr(old_value, "thingML_ConfigPropertyAssign207", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_ConfigPropertyAssign207"):
                opp_val = getattr(value, "thingML_ConfigPropertyAssign207", None)
                if opp_val is None:
                    setattr(value, "thingML_ConfigPropertyAssign207", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class thingML_Configuration(NamedElement, AnnotatedElement):

    pass
class thingML_Message(NamedElement, AnnotatedElement):

    pass
class thingML_Literal(Expression):

    pass
class thingML_EnumerationLiteral(NamedElement, AnnotatedElement):

    pass
class Type:

    pass
class thingML_ObjectType(Type):

    pass
class thingML_Enumeration(Type):

    pass
class thingML_Thing(Type):

    def __init__(self, fragment: bool, thingML_Thing: "thingML_Thing" = None, thingML_Thing20: set["thingML_Thing"] = None, thingML_Thing31: set["thingML_PropertyAssign"] = None, thingML_Thing33: "thingML_CompositeState" = None, thingML_Thing23: set["thingML_Message"] = None, thingML_Thing25: set["thingML_Port"] = None, thingML_Thing27: set["thingML_Property"] = None, thingML_Thing29: set["thingML_Function"] = None, thingML_Thing193: "thingML_Instance" = None):
        self.fragment = fragment
        self.thingML_Thing = thingML_Thing
        self.thingML_Thing20 = thingML_Thing20 if thingML_Thing20 is not None else set()
        self.thingML_Thing31 = thingML_Thing31 if thingML_Thing31 is not None else set()
        self.thingML_Thing33 = thingML_Thing33
        self.thingML_Thing23 = thingML_Thing23 if thingML_Thing23 is not None else set()
        self.thingML_Thing25 = thingML_Thing25 if thingML_Thing25 is not None else set()
        self.thingML_Thing27 = thingML_Thing27 if thingML_Thing27 is not None else set()
        self.thingML_Thing29 = thingML_Thing29 if thingML_Thing29 is not None else set()
        self.thingML_Thing193 = thingML_Thing193
        
    @property
    def fragment(self) -> bool:
        return self.__fragment

    @fragment.setter
    def fragment(self, fragment: bool):
        self.__fragment = fragment

    @property
    def thingML_Thing27(self):
        return self.__thingML_Thing27

    @thingML_Thing27.setter
    def thingML_Thing27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Thing__thingML_Thing27", None)
        self.__thingML_Thing27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingML_Property"):
                    opp_val = getattr(item, "thingML_Property", None)
                    
                    if opp_val == self:
                        setattr(item, "thingML_Property", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingML_Property"):
                    opp_val = getattr(item, "thingML_Property", None)
                    
                    setattr(item, "thingML_Property", self)
                    

    @property
    def thingML_Thing(self):
        return self.__thingML_Thing

    @thingML_Thing.setter
    def thingML_Thing(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Thing__thingML_Thing", None)
        self.__thingML_Thing = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Thing20"):
                opp_val = getattr(old_value, "thingML_Thing20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Thing20"):
                opp_val = getattr(value, "thingML_Thing20", None)
                if opp_val is None:
                    setattr(value, "thingML_Thing20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def thingML_Thing23(self):
        return self.__thingML_Thing23

    @thingML_Thing23.setter
    def thingML_Thing23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Thing__thingML_Thing23", None)
        self.__thingML_Thing23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingML_Message"):
                    opp_val = getattr(item, "thingML_Message", None)
                    
                    if opp_val == self:
                        setattr(item, "thingML_Message", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingML_Message"):
                    opp_val = getattr(item, "thingML_Message", None)
                    
                    setattr(item, "thingML_Message", self)
                    

    @property
    def thingML_Thing29(self):
        return self.__thingML_Thing29

    @thingML_Thing29.setter
    def thingML_Thing29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Thing__thingML_Thing29", None)
        self.__thingML_Thing29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingML_Function"):
                    opp_val = getattr(item, "thingML_Function", None)
                    
                    if opp_val == self:
                        setattr(item, "thingML_Function", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingML_Function"):
                    opp_val = getattr(item, "thingML_Function", None)
                    
                    setattr(item, "thingML_Function", self)
                    

    @property
    def thingML_Thing25(self):
        return self.__thingML_Thing25

    @thingML_Thing25.setter
    def thingML_Thing25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Thing__thingML_Thing25", None)
        self.__thingML_Thing25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingML_Port"):
                    opp_val = getattr(item, "thingML_Port", None)
                    
                    if opp_val == self:
                        setattr(item, "thingML_Port", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingML_Port"):
                    opp_val = getattr(item, "thingML_Port", None)
                    
                    setattr(item, "thingML_Port", self)
                    

    @property
    def thingML_Thing33(self):
        return self.__thingML_Thing33

    @thingML_Thing33.setter
    def thingML_Thing33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Thing__thingML_Thing33", None)
        self.__thingML_Thing33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_CompositeState"):
                opp_val = getattr(old_value, "thingML_CompositeState", None)
                if opp_val == self:
                    setattr(old_value, "thingML_CompositeState", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_CompositeState"):
                opp_val = getattr(value, "thingML_CompositeState", None)
                setattr(value, "thingML_CompositeState", self)

    @property
    def thingML_Thing20(self):
        return self.__thingML_Thing20

    @thingML_Thing20.setter
    def thingML_Thing20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Thing__thingML_Thing20", None)
        self.__thingML_Thing20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingML_Thing"):
                    opp_val = getattr(item, "thingML_Thing", None)
                    
                    if opp_val == self:
                        setattr(item, "thingML_Thing", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingML_Thing"):
                    opp_val = getattr(item, "thingML_Thing", None)
                    
                    setattr(item, "thingML_Thing", self)
                    

    @property
    def thingML_Thing31(self):
        return self.__thingML_Thing31

    @thingML_Thing31.setter
    def thingML_Thing31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Thing__thingML_Thing31", None)
        self.__thingML_Thing31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingML_PropertyAssign"):
                    opp_val = getattr(item, "thingML_PropertyAssign", None)
                    
                    if opp_val == self:
                        setattr(item, "thingML_PropertyAssign", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingML_PropertyAssign"):
                    opp_val = getattr(item, "thingML_PropertyAssign", None)
                    
                    setattr(item, "thingML_PropertyAssign", self)
                    

    @property
    def thingML_Thing193(self):
        return self.__thingML_Thing193

    @thingML_Thing193.setter
    def thingML_Thing193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Thing__thingML_Thing193", None)
        self.__thingML_Thing193 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Instance192"):
                opp_val = getattr(old_value, "thingML_Instance192", None)
                if opp_val == self:
                    setattr(old_value, "thingML_Instance192", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Instance192"):
                opp_val = getattr(value, "thingML_Instance192", None)
                setattr(value, "thingML_Instance192", self)

class thingML_PrimitiveType(Type):

    def __init__(self, ByteSize: str):
        self.ByteSize = ByteSize
        
    @property
    def ByteSize(self) -> str:
        return self.__ByteSize

    @ByteSize.setter
    def ByteSize(self, ByteSize: str):
        self.__ByteSize = ByteSize

class thingML_Expression:

    pass
class thingML_Protocol(NamedElement, AnnotatedElement):

    pass
class thingML_Type(NamedElement, AnnotatedElement):

    pass
class thingML_Import:

    def __init__(self, importURI: str, from: str, thingML_Import: "thingML_ThingMLModel" = None):
        self.importURI = importURI
        self.from = from
        self.thingML_Import = thingML_Import
        
    @property
    def from(self) -> str:
        return self.__from

    @from.setter
    def from(self, from: str):
        self.__from = from

    @property
    def importURI(self) -> str:
        return self.__importURI

    @importURI.setter
    def importURI(self, importURI: str):
        self.__importURI = importURI

    @property
    def thingML_Import(self):
        return self.__thingML_Import

    @thingML_Import.setter
    def thingML_Import(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Import__thingML_Import", None)
        self.__thingML_Import = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_ThingMLModel"):
                opp_val = getattr(old_value, "thingML_ThingMLModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_ThingMLModel"):
                opp_val = getattr(value, "thingML_ThingMLModel", None)
                if opp_val is None:
                    setattr(value, "thingML_ThingMLModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class thingML_ThingMLModel:

    pass