from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class thingML_InstanceRef:

    pass
class thingML_ConfigPropertyAssign:

    pass
class AbstractConnector:

    pass
class thingML_ExternalConnector(AbstractConnector):

    pass
class thingML_Connector(AbstractConnector):

    pass
class Expression:

    pass
class thingML_EnumLiteralRef(Expression):

    pass
class thingML_LowerExpression(Expression):

    pass
class thingML_DoubleLiteral(Expression):

    def __init__(self, doubleValue: float):
        self.doubleValue = doubleValue
        
    @property
    def doubleValue(self) -> float:
        return self.__doubleValue

    @doubleValue.setter
    def doubleValue(self, doubleValue: float):
        self.__doubleValue = doubleValue

class thingML_NotExpression(Expression):

    pass
class thingML_IntegerLiteral(Expression):

    def __init__(self, intValue: int):
        self.intValue = intValue
        
    @property
    def intValue(self) -> int:
        return self.__intValue

    @intValue.setter
    def intValue(self, intValue: int):
        self.__intValue = intValue

class thingML_GreaterOrEqualExpression(Expression):

    pass
class thingML_AndExpression(Expression):

    pass
class thingML_GreaterExpression(Expression):

    pass
class thingML_PlusExpression(Expression):

    pass
class thingML_BooleanLiteral(Expression):

    def __init__(self, boolValue: str):
        self.boolValue = boolValue
        
    @property
    def boolValue(self) -> str:
        return self.__boolValue

    @boolValue.setter
    def boolValue(self, boolValue: str):
        self.__boolValue = boolValue

class thingML_LowerOrEqualExpression(Expression):

    pass
class thingML_PropertyReference(Expression):

    pass
class thingML_UnaryMinus(Expression):

    pass
class thingML_DivExpression(Expression):

    pass
class thingML_TimesExpression(Expression):

    pass
class thingML_ModExpression(Expression):

    pass
class thingML_OrExpression(Expression):

    pass
class thingML_ArrayIndex(Expression):

    pass
class thingML_NotEqualsExpression(Expression):

    pass
class thingML_EqualsExpression(Expression):

    pass
class thingML_StringLiteral(Expression):

    def __init__(self, stringValue: str):
        self.stringValue = stringValue
        
    @property
    def stringValue(self) -> str:
        return self.__stringValue

    @stringValue.setter
    def stringValue(self, stringValue: str):
        self.__stringValue = stringValue

class thingML_MinusExpression(Expression):

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
                if hasattr(item, "thingML_Expression219"):
                    opp_val = getattr(item, "thingML_Expression219", None)
                    
                    if opp_val == self:
                        setattr(item, "thingML_Expression219", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingML_Expression219"):
                    opp_val = getattr(item, "thingML_Expression219", None)
                    
                    setattr(item, "thingML_Expression219", self)
                    

class thingML_FunctionCallExpression(Expression):

    pass
class thingML_Reference(Expression):

    pass
class Action:

    pass
class thingML_FunctionCallStatement(Action):

    pass
class thingML_VariableAssignment(Action):

    pass
class thingML_PrintAction(Action):

    pass
class thingML_ConditionalAction(Action):

    pass
class thingML_LoopAction(Action):

    pass
class thingML_ReturnAction(Action):

    pass
class thingML_ErrorAction(Action):

    pass
class thingML_Decrement(Action):

    pass
class thingML_StartSession(Action):

    pass
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
                if hasattr(item, "thingML_Expression165"):
                    opp_val = getattr(item, "thingML_Expression165", None)
                    
                    if opp_val == self:
                        setattr(item, "thingML_Expression165", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingML_Expression165"):
                    opp_val = getattr(item, "thingML_Expression165", None)
                    
                    setattr(item, "thingML_Expression165", self)
                    

class thingML_Increment(Action):

    pass
class thingML_Variable(ABC):

    pass
class Handler:

    pass
class thingML_Event(ABC):

    pass
class thingML_Transition(Handler):

    pass
class thingML_InternalTransition(Handler):

    pass
class thingML_Action(ABC):

    pass
class Event:

    pass
class ViewSource:

    pass
class thingML_LengthWindow(ViewSource):

    pass
class thingML_TimeWindow(ViewSource):

    pass
class thingML_Filter(ViewSource):

    pass
class State:

    pass
class Region:

    pass
class thingML_Region:

    pass
class ElmtProperty:

    pass
class thingML_ArrayParamRef(ElmtProperty):

    pass
class thingML_LengthArray(ElmtProperty):

    pass
class thingML_SimpleParamRef(ElmtProperty):

    pass
class Source:

    pass
class thingML_ElmtProperty(ABC):

    pass
class thingML_ReferencedElmt(ABC):

    pass
class thingML_ViewSource(ABC):

    pass
class thingML_SendAction(Action):

    pass
class thingML_Source(ABC):

    pass
class Variable:

    pass
class ReferencedElmt:

    pass
class thingML_MergeSources(ReferencedElmt, Source):

    def __init__(self, name: str, thingML_MergeSources: set["thingML_Source"] = None, thingML_MergeSources85: "thingML_Message" = None, thingML_MergeSources88: set["thingML_ViewSource"] = None):
        self.name = name
        self.thingML_MergeSources = thingML_MergeSources if thingML_MergeSources is not None else set()
        self.thingML_MergeSources85 = thingML_MergeSources85
        self.thingML_MergeSources88 = thingML_MergeSources88 if thingML_MergeSources88 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def thingML_MergeSources(self):
        return self.__thingML_MergeSources

    @thingML_MergeSources.setter
    def thingML_MergeSources(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_MergeSources__thingML_MergeSources", None)
        self.__thingML_MergeSources = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingML_Source83"):
                    opp_val = getattr(item, "thingML_Source83", None)
                    
                    if opp_val == self:
                        setattr(item, "thingML_Source83", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingML_Source83"):
                    opp_val = getattr(item, "thingML_Source83", None)
                    
                    setattr(item, "thingML_Source83", self)
                    

    @property
    def thingML_MergeSources85(self):
        return self.__thingML_MergeSources85

    @thingML_MergeSources85.setter
    def thingML_MergeSources85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_MergeSources__thingML_MergeSources85", None)
        self.__thingML_MergeSources85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Message86"):
                opp_val = getattr(old_value, "thingML_Message86", None)
                if opp_val == self:
                    setattr(old_value, "thingML_Message86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Message86"):
                opp_val = getattr(value, "thingML_Message86", None)
                setattr(value, "thingML_Message86", self)

    @property
    def thingML_MergeSources88(self):
        return self.__thingML_MergeSources88

    @thingML_MergeSources88.setter
    def thingML_MergeSources88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_MergeSources__thingML_MergeSources88", None)
        self.__thingML_MergeSources88 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingML_ViewSource89"):
                    opp_val = getattr(item, "thingML_ViewSource89", None)
                    
                    if opp_val == self:
                        setattr(item, "thingML_ViewSource89", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingML_ViewSource89"):
                    opp_val = getattr(item, "thingML_ViewSource89", None)
                    
                    setattr(item, "thingML_ViewSource89", self)
                    

class thingML_SimpleSource(ReferencedElmt, Source):

    def __init__(self, name: str, thingML_SimpleSource: "thingML_ReceiveMessage" = None, thingML_SimpleSource92: set["thingML_ViewSource"] = None):
        self.name = name
        self.thingML_SimpleSource = thingML_SimpleSource
        self.thingML_SimpleSource92 = thingML_SimpleSource92 if thingML_SimpleSource92 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def thingML_SimpleSource92(self):
        return self.__thingML_SimpleSource92

    @thingML_SimpleSource92.setter
    def thingML_SimpleSource92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_SimpleSource__thingML_SimpleSource92", None)
        self.__thingML_SimpleSource92 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingML_ViewSource93"):
                    opp_val = getattr(item, "thingML_ViewSource93", None)
                    
                    if opp_val == self:
                        setattr(item, "thingML_ViewSource93", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingML_ViewSource93"):
                    opp_val = getattr(item, "thingML_ViewSource93", None)
                    
                    setattr(item, "thingML_ViewSource93", self)
                    

    @property
    def thingML_SimpleSource(self):
        return self.__thingML_SimpleSource

    @thingML_SimpleSource.setter
    def thingML_SimpleSource(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_SimpleSource__thingML_SimpleSource", None)
        self.__thingML_SimpleSource = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_ReceiveMessage"):
                opp_val = getattr(old_value, "thingML_ReceiveMessage", None)
                if opp_val == self:
                    setattr(old_value, "thingML_ReceiveMessage", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_ReceiveMessage"):
                opp_val = getattr(value, "thingML_ReceiveMessage", None)
                setattr(value, "thingML_ReceiveMessage", self)

class thingML_JoinSources(ReferencedElmt, Source):

    def __init__(self, name: str, thingML_JoinSources75: "thingML_Message" = None, thingML_JoinSources78: set["thingML_Expression"] = None, thingML_JoinSources81: set["thingML_ViewSource"] = None, thingML_JoinSources: set["thingML_Source"] = None):
        self.name = name
        self.thingML_JoinSources75 = thingML_JoinSources75
        self.thingML_JoinSources78 = thingML_JoinSources78 if thingML_JoinSources78 is not None else set()
        self.thingML_JoinSources81 = thingML_JoinSources81 if thingML_JoinSources81 is not None else set()
        self.thingML_JoinSources = thingML_JoinSources if thingML_JoinSources is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def thingML_JoinSources81(self):
        return self.__thingML_JoinSources81

    @thingML_JoinSources81.setter
    def thingML_JoinSources81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_JoinSources__thingML_JoinSources81", None)
        self.__thingML_JoinSources81 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingML_ViewSource"):
                    opp_val = getattr(item, "thingML_ViewSource", None)
                    
                    if opp_val == self:
                        setattr(item, "thingML_ViewSource", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingML_ViewSource"):
                    opp_val = getattr(item, "thingML_ViewSource", None)
                    
                    setattr(item, "thingML_ViewSource", self)
                    

    @property
    def thingML_JoinSources78(self):
        return self.__thingML_JoinSources78

    @thingML_JoinSources78.setter
    def thingML_JoinSources78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_JoinSources__thingML_JoinSources78", None)
        self.__thingML_JoinSources78 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingML_Expression79"):
                    opp_val = getattr(item, "thingML_Expression79", None)
                    
                    if opp_val == self:
                        setattr(item, "thingML_Expression79", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingML_Expression79"):
                    opp_val = getattr(item, "thingML_Expression79", None)
                    
                    setattr(item, "thingML_Expression79", self)
                    

    @property
    def thingML_JoinSources(self):
        return self.__thingML_JoinSources

    @thingML_JoinSources.setter
    def thingML_JoinSources(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_JoinSources__thingML_JoinSources", None)
        self.__thingML_JoinSources = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingML_Source73"):
                    opp_val = getattr(item, "thingML_Source73", None)
                    
                    if opp_val == self:
                        setattr(item, "thingML_Source73", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingML_Source73"):
                    opp_val = getattr(item, "thingML_Source73", None)
                    
                    setattr(item, "thingML_Source73", self)
                    

    @property
    def thingML_JoinSources75(self):
        return self.__thingML_JoinSources75

    @thingML_JoinSources75.setter
    def thingML_JoinSources75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_JoinSources__thingML_JoinSources75", None)
        self.__thingML_JoinSources75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Message76"):
                opp_val = getattr(old_value, "thingML_Message76", None)
                if opp_val == self:
                    setattr(old_value, "thingML_Message76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Message76"):
                opp_val = getattr(value, "thingML_Message76", None)
                setattr(value, "thingML_Message76", self)

class thingML_ReceiveMessage(ReferencedElmt, Event):

    def __init__(self, name: str, thingML_ReceiveMessage: "thingML_SimpleSource" = None, thingML_ReceiveMessage156: "thingML_Port" = None, thingML_ReceiveMessage159: "thingML_Message" = None):
        self.name = name
        self.thingML_ReceiveMessage = thingML_ReceiveMessage
        self.thingML_ReceiveMessage156 = thingML_ReceiveMessage156
        self.thingML_ReceiveMessage159 = thingML_ReceiveMessage159
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def thingML_ReceiveMessage159(self):
        return self.__thingML_ReceiveMessage159

    @thingML_ReceiveMessage159.setter
    def thingML_ReceiveMessage159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_ReceiveMessage__thingML_ReceiveMessage159", None)
        self.__thingML_ReceiveMessage159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Message160"):
                opp_val = getattr(old_value, "thingML_Message160", None)
                if opp_val == self:
                    setattr(old_value, "thingML_Message160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Message160"):
                opp_val = getattr(value, "thingML_Message160", None)
                setattr(value, "thingML_Message160", self)

    @property
    def thingML_ReceiveMessage(self):
        return self.__thingML_ReceiveMessage

    @thingML_ReceiveMessage.setter
    def thingML_ReceiveMessage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_ReceiveMessage__thingML_ReceiveMessage", None)
        self.__thingML_ReceiveMessage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_SimpleSource"):
                opp_val = getattr(old_value, "thingML_SimpleSource", None)
                if opp_val == self:
                    setattr(old_value, "thingML_SimpleSource", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_SimpleSource"):
                opp_val = getattr(value, "thingML_SimpleSource", None)
                setattr(value, "thingML_SimpleSource", self)

    @property
    def thingML_ReceiveMessage156(self):
        return self.__thingML_ReceiveMessage156

    @thingML_ReceiveMessage156.setter
    def thingML_ReceiveMessage156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_ReceiveMessage__thingML_ReceiveMessage156", None)
        self.__thingML_ReceiveMessage156 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Port157"):
                opp_val = getattr(old_value, "thingML_Port157", None)
                if opp_val == self:
                    setattr(old_value, "thingML_Port157", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Port157"):
                opp_val = getattr(value, "thingML_Port157", None)
                setattr(value, "thingML_Port157", self)

class thingML_MessageParameter(ReferencedElmt):

    def __init__(self, name: str, thingML_MessageParameter: "thingML_Message" = None):
        self.name = name
        self.thingML_MessageParameter = thingML_MessageParameter
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def thingML_MessageParameter(self):
        return self.__thingML_MessageParameter

    @thingML_MessageParameter.setter
    def thingML_MessageParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_MessageParameter__thingML_MessageParameter", None)
        self.__thingML_MessageParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Message107"):
                opp_val = getattr(old_value, "thingML_Message107", None)
                if opp_val == self:
                    setattr(old_value, "thingML_Message107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Message107"):
                opp_val = getattr(value, "thingML_Message107", None)
                setattr(value, "thingML_Message107", self)

class thingML_ActionBlock(Action):

    pass
class Port:

    pass
class thingML_ProvidedPort(Port):

    pass
class thingML_InternalPort(Port):

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
            if hasattr(old_value, "thingML_Connector261"):
                opp_val = getattr(old_value, "thingML_Connector261", None)
                if opp_val == self:
                    setattr(old_value, "thingML_Connector261", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Connector261"):
                opp_val = getattr(value, "thingML_Connector261", None)
                setattr(value, "thingML_Connector261", self)

class thingML_EnumerationLiteral:

    def __init__(self, name: str, thingML_EnumerationLiteral: "thingML_Enumeration" = None, thingML_EnumerationLiteral14: set["thingML_PlatformAnnotation"] = None, thingML_EnumerationLiteral224: "thingML_EnumLiteralRef" = None):
        self.name = name
        self.thingML_EnumerationLiteral = thingML_EnumerationLiteral
        self.thingML_EnumerationLiteral14 = thingML_EnumerationLiteral14 if thingML_EnumerationLiteral14 is not None else set()
        self.thingML_EnumerationLiteral224 = thingML_EnumerationLiteral224
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def thingML_EnumerationLiteral(self):
        return self.__thingML_EnumerationLiteral

    @thingML_EnumerationLiteral.setter
    def thingML_EnumerationLiteral(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_EnumerationLiteral__thingML_EnumerationLiteral", None)
        self.__thingML_EnumerationLiteral = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Enumeration"):
                opp_val = getattr(old_value, "thingML_Enumeration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Enumeration"):
                opp_val = getattr(value, "thingML_Enumeration", None)
                if opp_val is None:
                    setattr(value, "thingML_Enumeration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def thingML_EnumerationLiteral224(self):
        return self.__thingML_EnumerationLiteral224

    @thingML_EnumerationLiteral224.setter
    def thingML_EnumerationLiteral224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_EnumerationLiteral__thingML_EnumerationLiteral224", None)
        self.__thingML_EnumerationLiteral224 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_EnumLiteralRef223"):
                opp_val = getattr(old_value, "thingML_EnumLiteralRef223", None)
                if opp_val == self:
                    setattr(old_value, "thingML_EnumLiteralRef223", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_EnumLiteralRef223"):
                opp_val = getattr(value, "thingML_EnumLiteralRef223", None)
                setattr(value, "thingML_EnumLiteralRef223", self)

    @property
    def thingML_EnumerationLiteral14(self):
        return self.__thingML_EnumerationLiteral14

    @thingML_EnumerationLiteral14.setter
    def thingML_EnumerationLiteral14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_EnumerationLiteral__thingML_EnumerationLiteral14", None)
        self.__thingML_EnumerationLiteral14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingML_PlatformAnnotation15"):
                    opp_val = getattr(item, "thingML_PlatformAnnotation15", None)
                    
                    if opp_val == self:
                        setattr(item, "thingML_PlatformAnnotation15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingML_PlatformAnnotation15"):
                    opp_val = getattr(item, "thingML_PlatformAnnotation15", None)
                    
                    setattr(item, "thingML_PlatformAnnotation15", self)
                    

class Type:

    pass
class thingML_Enumeration(Type):

    pass
class thingML_Thing(Type):

    def __init__(self, fragment: bool, thingML_Thing: "thingML_Thing" = None, thingML_Thing16: set["thingML_Thing"] = None, thingML_Thing19: set["thingML_Message"] = None, thingML_Thing21: set["thingML_Port"] = None, thingML_Thing23: set["thingML_Property"] = None, thingML_Thing25: set["thingML_Function"] = None, thingML_Thing27: set["thingML_PropertyAssign"] = None, thingML_Thing29: set["thingML_CompositeState"] = None, thingML_Thing31: set["thingML_Stream"] = None, thingML_Thing243: "thingML_Instance" = None):
        self.fragment = fragment
        self.thingML_Thing = thingML_Thing
        self.thingML_Thing16 = thingML_Thing16 if thingML_Thing16 is not None else set()
        self.thingML_Thing19 = thingML_Thing19 if thingML_Thing19 is not None else set()
        self.thingML_Thing21 = thingML_Thing21 if thingML_Thing21 is not None else set()
        self.thingML_Thing23 = thingML_Thing23 if thingML_Thing23 is not None else set()
        self.thingML_Thing25 = thingML_Thing25 if thingML_Thing25 is not None else set()
        self.thingML_Thing27 = thingML_Thing27 if thingML_Thing27 is not None else set()
        self.thingML_Thing29 = thingML_Thing29 if thingML_Thing29 is not None else set()
        self.thingML_Thing31 = thingML_Thing31 if thingML_Thing31 is not None else set()
        self.thingML_Thing243 = thingML_Thing243
        
    @property
    def fragment(self) -> bool:
        return self.__fragment

    @fragment.setter
    def fragment(self, fragment: bool):
        self.__fragment = fragment

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
            if hasattr(old_value, "thingML_Thing16"):
                opp_val = getattr(old_value, "thingML_Thing16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Thing16"):
                opp_val = getattr(value, "thingML_Thing16", None)
                if opp_val is None:
                    setattr(value, "thingML_Thing16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def thingML_Thing16(self):
        return self.__thingML_Thing16

    @thingML_Thing16.setter
    def thingML_Thing16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Thing__thingML_Thing16", None)
        self.__thingML_Thing16 = value if value is not None else set()
        
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
    def thingML_Thing243(self):
        return self.__thingML_Thing243

    @thingML_Thing243.setter
    def thingML_Thing243(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Thing__thingML_Thing243", None)
        self.__thingML_Thing243 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Instance242"):
                opp_val = getattr(old_value, "thingML_Instance242", None)
                if opp_val == self:
                    setattr(old_value, "thingML_Instance242", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Instance242"):
                opp_val = getattr(value, "thingML_Instance242", None)
                setattr(value, "thingML_Instance242", self)

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
                if hasattr(item, "thingML_CompositeState"):
                    opp_val = getattr(item, "thingML_CompositeState", None)
                    
                    if opp_val == self:
                        setattr(item, "thingML_CompositeState", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingML_CompositeState"):
                    opp_val = getattr(item, "thingML_CompositeState", None)
                    
                    setattr(item, "thingML_CompositeState", self)
                    

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
    def thingML_Thing19(self):
        return self.__thingML_Thing19

    @thingML_Thing19.setter
    def thingML_Thing19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Thing__thingML_Thing19", None)
        self.__thingML_Thing19 = value if value is not None else set()
        
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
                if hasattr(item, "thingML_Stream"):
                    opp_val = getattr(item, "thingML_Stream", None)
                    
                    if opp_val == self:
                        setattr(item, "thingML_Stream", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingML_Stream"):
                    opp_val = getattr(item, "thingML_Stream", None)
                    
                    setattr(item, "thingML_Stream", self)
                    

    @property
    def thingML_Thing21(self):
        return self.__thingML_Thing21

    @thingML_Thing21.setter
    def thingML_Thing21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Thing__thingML_Thing21", None)
        self.__thingML_Thing21 = value if value is not None else set()
        
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
                    

class thingML_ObjectType(Type):

    pass
class thingML_PrimitiveType(Type):

    def __init__(self, ByteSize: int):
        self.ByteSize = ByteSize
        
    @property
    def ByteSize(self) -> int:
        return self.__ByteSize

    @ByteSize.setter
    def ByteSize(self, ByteSize: int):
        self.__ByteSize = ByteSize

class AnnotatedElement:

    pass
class thingML_Handler(AnnotatedElement):

    def __init__(self, name: str, thingML_Handler: set["thingML_Event"] = None, thingML_Handler147: "thingML_Expression" = None, thingML_Handler150: "thingML_Action" = None):
        self.name = name
        self.thingML_Handler = thingML_Handler if thingML_Handler is not None else set()
        self.thingML_Handler147 = thingML_Handler147
        self.thingML_Handler150 = thingML_Handler150
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def thingML_Handler(self):
        return self.__thingML_Handler

    @thingML_Handler.setter
    def thingML_Handler(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Handler__thingML_Handler", None)
        self.__thingML_Handler = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingML_Event"):
                    opp_val = getattr(item, "thingML_Event", None)
                    
                    if opp_val == self:
                        setattr(item, "thingML_Event", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingML_Event"):
                    opp_val = getattr(item, "thingML_Event", None)
                    
                    setattr(item, "thingML_Event", self)
                    

    @property
    def thingML_Handler147(self):
        return self.__thingML_Handler147

    @thingML_Handler147.setter
    def thingML_Handler147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Handler__thingML_Handler147", None)
        self.__thingML_Handler147 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Expression148"):
                opp_val = getattr(old_value, "thingML_Expression148", None)
                if opp_val == self:
                    setattr(old_value, "thingML_Expression148", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Expression148"):
                opp_val = getattr(value, "thingML_Expression148", None)
                setattr(value, "thingML_Expression148", self)

    @property
    def thingML_Handler150(self):
        return self.__thingML_Handler150

    @thingML_Handler150.setter
    def thingML_Handler150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Handler__thingML_Handler150", None)
        self.__thingML_Handler150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Action151"):
                opp_val = getattr(old_value, "thingML_Action151", None)
                if opp_val == self:
                    setattr(old_value, "thingML_Action151", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Action151"):
                opp_val = getattr(value, "thingML_Action151", None)
                setattr(value, "thingML_Action151", self)

class thingML_Session(State, Region, AnnotatedElement):

    def __init__(self, maxInstances: int, thingML_Session: "thingML_State" = None, thingML_Session122: set["thingML_State"] = None, thingML_Session125: set["thingML_ParallelRegion"] = None, thingML_Session212: "thingML_StartSession" = None):
        self.maxInstances = maxInstances
        self.thingML_Session = thingML_Session
        self.thingML_Session122 = thingML_Session122 if thingML_Session122 is not None else set()
        self.thingML_Session125 = thingML_Session125 if thingML_Session125 is not None else set()
        self.thingML_Session212 = thingML_Session212
        
    @property
    def maxInstances(self) -> int:
        return self.__maxInstances

    @maxInstances.setter
    def maxInstances(self, maxInstances: int):
        self.__maxInstances = maxInstances

    @property
    def thingML_Session212(self):
        return self.__thingML_Session212

    @thingML_Session212.setter
    def thingML_Session212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Session__thingML_Session212", None)
        self.__thingML_Session212 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_StartSession"):
                opp_val = getattr(old_value, "thingML_StartSession", None)
                if opp_val == self:
                    setattr(old_value, "thingML_StartSession", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_StartSession"):
                opp_val = getattr(value, "thingML_StartSession", None)
                setattr(value, "thingML_StartSession", self)

    @property
    def thingML_Session122(self):
        return self.__thingML_Session122

    @thingML_Session122.setter
    def thingML_Session122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Session__thingML_Session122", None)
        self.__thingML_Session122 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingML_State123"):
                    opp_val = getattr(item, "thingML_State123", None)
                    
                    if opp_val == self:
                        setattr(item, "thingML_State123", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingML_State123"):
                    opp_val = getattr(item, "thingML_State123", None)
                    
                    setattr(item, "thingML_State123", self)
                    

    @property
    def thingML_Session125(self):
        return self.__thingML_Session125

    @thingML_Session125.setter
    def thingML_Session125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Session__thingML_Session125", None)
        self.__thingML_Session125 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingML_ParallelRegion126"):
                    opp_val = getattr(item, "thingML_ParallelRegion126", None)
                    
                    if opp_val == self:
                        setattr(item, "thingML_ParallelRegion126", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingML_ParallelRegion126"):
                    opp_val = getattr(item, "thingML_ParallelRegion126", None)
                    
                    setattr(item, "thingML_ParallelRegion126", self)
                    

    @property
    def thingML_Session(self):
        return self.__thingML_Session

    @thingML_Session.setter
    def thingML_Session(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Session__thingML_Session", None)
        self.__thingML_Session = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_State120"):
                opp_val = getattr(old_value, "thingML_State120", None)
                if opp_val == self:
                    setattr(old_value, "thingML_State120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_State120"):
                opp_val = getattr(value, "thingML_State120", None)
                setattr(value, "thingML_State120", self)

class thingML_LocalVariable(ReferencedElmt, Action, Variable, AnnotatedElement):

    def __init__(self, changeable: bool, name: str, thingML_LocalVariable: "thingML_Stream" = None, thingML_LocalVariable167: "thingML_TypeRef" = None, thingML_LocalVariable170: "thingML_Expression" = None):
        self.changeable = changeable
        self.name = name
        self.thingML_LocalVariable = thingML_LocalVariable
        self.thingML_LocalVariable167 = thingML_LocalVariable167
        self.thingML_LocalVariable170 = thingML_LocalVariable170
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def changeable(self) -> bool:
        return self.__changeable

    @changeable.setter
    def changeable(self, changeable: bool):
        self.__changeable = changeable

    @property
    def thingML_LocalVariable170(self):
        return self.__thingML_LocalVariable170

    @thingML_LocalVariable170.setter
    def thingML_LocalVariable170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_LocalVariable__thingML_LocalVariable170", None)
        self.__thingML_LocalVariable170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Expression171"):
                opp_val = getattr(old_value, "thingML_Expression171", None)
                if opp_val == self:
                    setattr(old_value, "thingML_Expression171", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Expression171"):
                opp_val = getattr(value, "thingML_Expression171", None)
                setattr(value, "thingML_Expression171", self)

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
            if hasattr(old_value, "thingML_Stream69"):
                opp_val = getattr(old_value, "thingML_Stream69", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Stream69"):
                opp_val = getattr(value, "thingML_Stream69", None)
                if opp_val is None:
                    setattr(value, "thingML_Stream69", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def thingML_LocalVariable167(self):
        return self.__thingML_LocalVariable167

    @thingML_LocalVariable167.setter
    def thingML_LocalVariable167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_LocalVariable__thingML_LocalVariable167", None)
        self.__thingML_LocalVariable167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_TypeRef168"):
                opp_val = getattr(old_value, "thingML_TypeRef168", None)
                if opp_val == self:
                    setattr(old_value, "thingML_TypeRef168", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_TypeRef168"):
                opp_val = getattr(value, "thingML_TypeRef168", None)
                setattr(value, "thingML_TypeRef168", self)

class thingML_Instance(AnnotatedElement):

    def __init__(self, name: str, thingML_Instance: "thingML_Configuration" = None, thingML_Instance242: "thingML_Thing" = None, thingML_Instance277: "thingML_InstanceRef" = None):
        self.name = name
        self.thingML_Instance = thingML_Instance
        self.thingML_Instance242 = thingML_Instance242
        self.thingML_Instance277 = thingML_Instance277
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def thingML_Instance242(self):
        return self.__thingML_Instance242

    @thingML_Instance242.setter
    def thingML_Instance242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Instance__thingML_Instance242", None)
        self.__thingML_Instance242 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Thing243"):
                opp_val = getattr(old_value, "thingML_Thing243", None)
                if opp_val == self:
                    setattr(old_value, "thingML_Thing243", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Thing243"):
                opp_val = getattr(value, "thingML_Thing243", None)
                setattr(value, "thingML_Thing243", self)

    @property
    def thingML_Instance277(self):
        return self.__thingML_Instance277

    @thingML_Instance277.setter
    def thingML_Instance277(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Instance__thingML_Instance277", None)
        self.__thingML_Instance277 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_InstanceRef276"):
                opp_val = getattr(old_value, "thingML_InstanceRef276", None)
                if opp_val == self:
                    setattr(old_value, "thingML_InstanceRef276", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_InstanceRef276"):
                opp_val = getattr(value, "thingML_InstanceRef276", None)
                setattr(value, "thingML_InstanceRef276", self)

    @property
    def thingML_Instance(self):
        return self.__thingML_Instance

    @thingML_Instance.setter
    def thingML_Instance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Instance__thingML_Instance", None)
        self.__thingML_Instance = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Configuration236"):
                opp_val = getattr(old_value, "thingML_Configuration236", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Configuration236"):
                opp_val = getattr(value, "thingML_Configuration236", None)
                if opp_val is None:
                    setattr(value, "thingML_Configuration236", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class thingML_State(AnnotatedElement):

    def __init__(self, name: str, thingML_State: "thingML_CompositeState" = None, thingML_State116: "thingML_CompositeState" = None, thingML_State154: "thingML_Transition" = None, thingML_State129: "thingML_ParallelRegion" = None, thingML_State132: "thingML_ParallelRegion" = None, thingML_State120: "thingML_Session" = None, thingML_State123: "thingML_Session" = None, thingML_State134: set["thingML_Property"] = None, thingML_State137: "thingML_Action" = None, thingML_State139: "thingML_Action" = None, thingML_State142: set["thingML_InternalTransition"] = None, thingML_State144: set["thingML_Transition"] = None):
        self.name = name
        self.thingML_State = thingML_State
        self.thingML_State116 = thingML_State116
        self.thingML_State154 = thingML_State154
        self.thingML_State129 = thingML_State129
        self.thingML_State132 = thingML_State132
        self.thingML_State120 = thingML_State120
        self.thingML_State123 = thingML_State123
        self.thingML_State134 = thingML_State134 if thingML_State134 is not None else set()
        self.thingML_State137 = thingML_State137
        self.thingML_State139 = thingML_State139
        self.thingML_State142 = thingML_State142 if thingML_State142 is not None else set()
        self.thingML_State144 = thingML_State144 if thingML_State144 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def thingML_State154(self):
        return self.__thingML_State154

    @thingML_State154.setter
    def thingML_State154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_State__thingML_State154", None)
        self.__thingML_State154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Transition153"):
                opp_val = getattr(old_value, "thingML_Transition153", None)
                if opp_val == self:
                    setattr(old_value, "thingML_Transition153", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Transition153"):
                opp_val = getattr(value, "thingML_Transition153", None)
                setattr(value, "thingML_Transition153", self)

    @property
    def thingML_State139(self):
        return self.__thingML_State139

    @thingML_State139.setter
    def thingML_State139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_State__thingML_State139", None)
        self.__thingML_State139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Action140"):
                opp_val = getattr(old_value, "thingML_Action140", None)
                if opp_val == self:
                    setattr(old_value, "thingML_Action140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Action140"):
                opp_val = getattr(value, "thingML_Action140", None)
                setattr(value, "thingML_Action140", self)

    @property
    def thingML_State134(self):
        return self.__thingML_State134

    @thingML_State134.setter
    def thingML_State134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_State__thingML_State134", None)
        self.__thingML_State134 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingML_Property135"):
                    opp_val = getattr(item, "thingML_Property135", None)
                    
                    if opp_val == self:
                        setattr(item, "thingML_Property135", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingML_Property135"):
                    opp_val = getattr(item, "thingML_Property135", None)
                    
                    setattr(item, "thingML_Property135", self)
                    

    @property
    def thingML_State137(self):
        return self.__thingML_State137

    @thingML_State137.setter
    def thingML_State137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_State__thingML_State137", None)
        self.__thingML_State137 = value
        
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
    def thingML_State116(self):
        return self.__thingML_State116

    @thingML_State116.setter
    def thingML_State116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_State__thingML_State116", None)
        self.__thingML_State116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_CompositeState115"):
                opp_val = getattr(old_value, "thingML_CompositeState115", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_CompositeState115"):
                opp_val = getattr(value, "thingML_CompositeState115", None)
                if opp_val is None:
                    setattr(value, "thingML_CompositeState115", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def thingML_State144(self):
        return self.__thingML_State144

    @thingML_State144.setter
    def thingML_State144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_State__thingML_State144", None)
        self.__thingML_State144 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingML_Transition"):
                    opp_val = getattr(item, "thingML_Transition", None)
                    
                    if opp_val == self:
                        setattr(item, "thingML_Transition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingML_Transition"):
                    opp_val = getattr(item, "thingML_Transition", None)
                    
                    setattr(item, "thingML_Transition", self)
                    

    @property
    def thingML_State120(self):
        return self.__thingML_State120

    @thingML_State120.setter
    def thingML_State120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_State__thingML_State120", None)
        self.__thingML_State120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Session"):
                opp_val = getattr(old_value, "thingML_Session", None)
                if opp_val == self:
                    setattr(old_value, "thingML_Session", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Session"):
                opp_val = getattr(value, "thingML_Session", None)
                setattr(value, "thingML_Session", self)

    @property
    def thingML_State142(self):
        return self.__thingML_State142

    @thingML_State142.setter
    def thingML_State142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_State__thingML_State142", None)
        self.__thingML_State142 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingML_InternalTransition"):
                    opp_val = getattr(item, "thingML_InternalTransition", None)
                    
                    if opp_val == self:
                        setattr(item, "thingML_InternalTransition", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingML_InternalTransition"):
                    opp_val = getattr(item, "thingML_InternalTransition", None)
                    
                    setattr(item, "thingML_InternalTransition", self)
                    

    @property
    def thingML_State132(self):
        return self.__thingML_State132

    @thingML_State132.setter
    def thingML_State132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_State__thingML_State132", None)
        self.__thingML_State132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_ParallelRegion131"):
                opp_val = getattr(old_value, "thingML_ParallelRegion131", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_ParallelRegion131"):
                opp_val = getattr(value, "thingML_ParallelRegion131", None)
                if opp_val is None:
                    setattr(value, "thingML_ParallelRegion131", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def thingML_State129(self):
        return self.__thingML_State129

    @thingML_State129.setter
    def thingML_State129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_State__thingML_State129", None)
        self.__thingML_State129 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_ParallelRegion128"):
                opp_val = getattr(old_value, "thingML_ParallelRegion128", None)
                if opp_val == self:
                    setattr(old_value, "thingML_ParallelRegion128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_ParallelRegion128"):
                opp_val = getattr(value, "thingML_ParallelRegion128", None)
                setattr(value, "thingML_ParallelRegion128", self)

    @property
    def thingML_State123(self):
        return self.__thingML_State123

    @thingML_State123.setter
    def thingML_State123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_State__thingML_State123", None)
        self.__thingML_State123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Session122"):
                opp_val = getattr(old_value, "thingML_Session122", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Session122"):
                opp_val = getattr(value, "thingML_Session122", None)
                if opp_val is None:
                    setattr(value, "thingML_Session122", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def thingML_State(self):
        return self.__thingML_State

    @thingML_State.setter
    def thingML_State(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_State__thingML_State", None)
        self.__thingML_State = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_CompositeState113"):
                opp_val = getattr(old_value, "thingML_CompositeState113", None)
                if opp_val == self:
                    setattr(old_value, "thingML_CompositeState113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_CompositeState113"):
                opp_val = getattr(value, "thingML_CompositeState113", None)
                setattr(value, "thingML_CompositeState113", self)

class thingML_AbstractConnector(AnnotatedElement):

    def __init__(self, name: str, thingML_AbstractConnector: "thingML_Configuration" = None):
        self.name = name
        self.thingML_AbstractConnector = thingML_AbstractConnector
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def thingML_AbstractConnector(self):
        return self.__thingML_AbstractConnector

    @thingML_AbstractConnector.setter
    def thingML_AbstractConnector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_AbstractConnector__thingML_AbstractConnector", None)
        self.__thingML_AbstractConnector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Configuration238"):
                opp_val = getattr(old_value, "thingML_Configuration238", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Configuration238"):
                opp_val = getattr(value, "thingML_Configuration238", None)
                if opp_val is None:
                    setattr(value, "thingML_Configuration238", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class thingML_FinalState(State, AnnotatedElement):

    pass
class thingML_ParallelRegion(Region, AnnotatedElement):

    def __init__(self, name: str, history: bool, thingML_ParallelRegion: "thingML_CompositeState" = None, thingML_ParallelRegion128: "thingML_State" = None, thingML_ParallelRegion131: set["thingML_State"] = None, thingML_ParallelRegion126: "thingML_Session" = None):
        self.name = name
        self.history = history
        self.thingML_ParallelRegion = thingML_ParallelRegion
        self.thingML_ParallelRegion128 = thingML_ParallelRegion128
        self.thingML_ParallelRegion131 = thingML_ParallelRegion131 if thingML_ParallelRegion131 is not None else set()
        self.thingML_ParallelRegion126 = thingML_ParallelRegion126
        
    @property
    def history(self) -> bool:
        return self.__history

    @history.setter
    def history(self, history: bool):
        self.__history = history

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def thingML_ParallelRegion128(self):
        return self.__thingML_ParallelRegion128

    @thingML_ParallelRegion128.setter
    def thingML_ParallelRegion128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_ParallelRegion__thingML_ParallelRegion128", None)
        self.__thingML_ParallelRegion128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_State129"):
                opp_val = getattr(old_value, "thingML_State129", None)
                if opp_val == self:
                    setattr(old_value, "thingML_State129", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_State129"):
                opp_val = getattr(value, "thingML_State129", None)
                setattr(value, "thingML_State129", self)

    @property
    def thingML_ParallelRegion126(self):
        return self.__thingML_ParallelRegion126

    @thingML_ParallelRegion126.setter
    def thingML_ParallelRegion126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_ParallelRegion__thingML_ParallelRegion126", None)
        self.__thingML_ParallelRegion126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Session125"):
                opp_val = getattr(old_value, "thingML_Session125", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Session125"):
                opp_val = getattr(value, "thingML_Session125", None)
                if opp_val is None:
                    setattr(value, "thingML_Session125", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def thingML_ParallelRegion131(self):
        return self.__thingML_ParallelRegion131

    @thingML_ParallelRegion131.setter
    def thingML_ParallelRegion131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_ParallelRegion__thingML_ParallelRegion131", None)
        self.__thingML_ParallelRegion131 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingML_State132"):
                    opp_val = getattr(item, "thingML_State132", None)
                    
                    if opp_val == self:
                        setattr(item, "thingML_State132", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingML_State132"):
                    opp_val = getattr(item, "thingML_State132", None)
                    
                    setattr(item, "thingML_State132", self)
                    

    @property
    def thingML_ParallelRegion(self):
        return self.__thingML_ParallelRegion

    @thingML_ParallelRegion.setter
    def thingML_ParallelRegion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_ParallelRegion__thingML_ParallelRegion", None)
        self.__thingML_ParallelRegion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_CompositeState118"):
                opp_val = getattr(old_value, "thingML_CompositeState118", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_CompositeState118"):
                opp_val = getattr(value, "thingML_CompositeState118", None)
                if opp_val is None:
                    setattr(value, "thingML_CompositeState118", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class thingML_Parameter(ReferencedElmt, Variable, AnnotatedElement):

    def __init__(self, name: str, thingML_Parameter56: "thingML_Message" = None, thingML_Parameter58: "thingML_TypeRef" = None, thingML_Parameter: "thingML_Function" = None, thingML_Parameter109: "thingML_SimpleParamRef" = None, thingML_Parameter111: "thingML_ArrayParamRef" = None):
        self.name = name
        self.thingML_Parameter56 = thingML_Parameter56
        self.thingML_Parameter58 = thingML_Parameter58
        self.thingML_Parameter = thingML_Parameter
        self.thingML_Parameter109 = thingML_Parameter109
        self.thingML_Parameter111 = thingML_Parameter111
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def thingML_Parameter58(self):
        return self.__thingML_Parameter58

    @thingML_Parameter58.setter
    def thingML_Parameter58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Parameter__thingML_Parameter58", None)
        self.__thingML_Parameter58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_TypeRef59"):
                opp_val = getattr(old_value, "thingML_TypeRef59", None)
                if opp_val == self:
                    setattr(old_value, "thingML_TypeRef59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_TypeRef59"):
                opp_val = getattr(value, "thingML_TypeRef59", None)
                setattr(value, "thingML_TypeRef59", self)

    @property
    def thingML_Parameter109(self):
        return self.__thingML_Parameter109

    @thingML_Parameter109.setter
    def thingML_Parameter109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Parameter__thingML_Parameter109", None)
        self.__thingML_Parameter109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_SimpleParamRef"):
                opp_val = getattr(old_value, "thingML_SimpleParamRef", None)
                if opp_val == self:
                    setattr(old_value, "thingML_SimpleParamRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_SimpleParamRef"):
                opp_val = getattr(value, "thingML_SimpleParamRef", None)
                setattr(value, "thingML_SimpleParamRef", self)

    @property
    def thingML_Parameter56(self):
        return self.__thingML_Parameter56

    @thingML_Parameter56.setter
    def thingML_Parameter56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Parameter__thingML_Parameter56", None)
        self.__thingML_Parameter56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Message55"):
                opp_val = getattr(old_value, "thingML_Message55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Message55"):
                opp_val = getattr(value, "thingML_Message55", None)
                if opp_val is None:
                    setattr(value, "thingML_Message55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def thingML_Parameter(self):
        return self.__thingML_Parameter

    @thingML_Parameter.setter
    def thingML_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Parameter__thingML_Parameter", None)
        self.__thingML_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Function42"):
                opp_val = getattr(old_value, "thingML_Function42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Function42"):
                opp_val = getattr(value, "thingML_Function42", None)
                if opp_val is None:
                    setattr(value, "thingML_Function42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def thingML_Parameter111(self):
        return self.__thingML_Parameter111

    @thingML_Parameter111.setter
    def thingML_Parameter111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Parameter__thingML_Parameter111", None)
        self.__thingML_Parameter111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_ArrayParamRef"):
                opp_val = getattr(old_value, "thingML_ArrayParamRef", None)
                if opp_val == self:
                    setattr(old_value, "thingML_ArrayParamRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_ArrayParamRef"):
                opp_val = getattr(value, "thingML_ArrayParamRef", None)
                setattr(value, "thingML_ArrayParamRef", self)

class thingML_Stream(AnnotatedElement):

    def __init__(self, name: str, thingML_Stream: "thingML_Thing" = None, thingML_Stream67: "thingML_Source" = None, thingML_Stream69: set["thingML_LocalVariable"] = None, thingML_Stream71: "thingML_SendAction" = None):
        self.name = name
        self.thingML_Stream = thingML_Stream
        self.thingML_Stream67 = thingML_Stream67
        self.thingML_Stream69 = thingML_Stream69 if thingML_Stream69 is not None else set()
        self.thingML_Stream71 = thingML_Stream71
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def thingML_Stream(self):
        return self.__thingML_Stream

    @thingML_Stream.setter
    def thingML_Stream(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Stream__thingML_Stream", None)
        self.__thingML_Stream = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Thing31"):
                opp_val = getattr(old_value, "thingML_Thing31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Thing31"):
                opp_val = getattr(value, "thingML_Thing31", None)
                if opp_val is None:
                    setattr(value, "thingML_Thing31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def thingML_Stream67(self):
        return self.__thingML_Stream67

    @thingML_Stream67.setter
    def thingML_Stream67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Stream__thingML_Stream67", None)
        self.__thingML_Stream67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Source"):
                opp_val = getattr(old_value, "thingML_Source", None)
                if opp_val == self:
                    setattr(old_value, "thingML_Source", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Source"):
                opp_val = getattr(value, "thingML_Source", None)
                setattr(value, "thingML_Source", self)

    @property
    def thingML_Stream69(self):
        return self.__thingML_Stream69

    @thingML_Stream69.setter
    def thingML_Stream69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Stream__thingML_Stream69", None)
        self.__thingML_Stream69 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingML_LocalVariable"):
                    opp_val = getattr(item, "thingML_LocalVariable", None)
                    
                    if opp_val == self:
                        setattr(item, "thingML_LocalVariable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingML_LocalVariable"):
                    opp_val = getattr(item, "thingML_LocalVariable", None)
                    
                    setattr(item, "thingML_LocalVariable", self)
                    

    @property
    def thingML_Stream71(self):
        return self.__thingML_Stream71

    @thingML_Stream71.setter
    def thingML_Stream71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Stream__thingML_Stream71", None)
        self.__thingML_Stream71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_SendAction"):
                opp_val = getattr(old_value, "thingML_SendAction", None)
                if opp_val == self:
                    setattr(old_value, "thingML_SendAction", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_SendAction"):
                opp_val = getattr(value, "thingML_SendAction", None)
                setattr(value, "thingML_SendAction", self)

class thingML_CompositeState(State, Region, AnnotatedElement):

    def __init__(self, history: bool, thingML_CompositeState: "thingML_Thing" = None, thingML_CompositeState113: "thingML_State" = None, thingML_CompositeState115: set["thingML_State"] = None, thingML_CompositeState118: set["thingML_ParallelRegion"] = None):
        self.history = history
        self.thingML_CompositeState = thingML_CompositeState
        self.thingML_CompositeState113 = thingML_CompositeState113
        self.thingML_CompositeState115 = thingML_CompositeState115 if thingML_CompositeState115 is not None else set()
        self.thingML_CompositeState118 = thingML_CompositeState118 if thingML_CompositeState118 is not None else set()
        
    @property
    def history(self) -> bool:
        return self.__history

    @history.setter
    def history(self, history: bool):
        self.__history = history

    @property
    def thingML_CompositeState(self):
        return self.__thingML_CompositeState

    @thingML_CompositeState.setter
    def thingML_CompositeState(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_CompositeState__thingML_CompositeState", None)
        self.__thingML_CompositeState = value
        
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

    @property
    def thingML_CompositeState113(self):
        return self.__thingML_CompositeState113

    @thingML_CompositeState113.setter
    def thingML_CompositeState113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_CompositeState__thingML_CompositeState113", None)
        self.__thingML_CompositeState113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_State"):
                opp_val = getattr(old_value, "thingML_State", None)
                if opp_val == self:
                    setattr(old_value, "thingML_State", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_State"):
                opp_val = getattr(value, "thingML_State", None)
                setattr(value, "thingML_State", self)

    @property
    def thingML_CompositeState118(self):
        return self.__thingML_CompositeState118

    @thingML_CompositeState118.setter
    def thingML_CompositeState118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_CompositeState__thingML_CompositeState118", None)
        self.__thingML_CompositeState118 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingML_ParallelRegion"):
                    opp_val = getattr(item, "thingML_ParallelRegion", None)
                    
                    if opp_val == self:
                        setattr(item, "thingML_ParallelRegion", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingML_ParallelRegion"):
                    opp_val = getattr(item, "thingML_ParallelRegion", None)
                    
                    setattr(item, "thingML_ParallelRegion", self)
                    

    @property
    def thingML_CompositeState115(self):
        return self.__thingML_CompositeState115

    @thingML_CompositeState115.setter
    def thingML_CompositeState115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_CompositeState__thingML_CompositeState115", None)
        self.__thingML_CompositeState115 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingML_State116"):
                    opp_val = getattr(item, "thingML_State116", None)
                    
                    if opp_val == self:
                        setattr(item, "thingML_State116", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingML_State116"):
                    opp_val = getattr(item, "thingML_State116", None)
                    
                    setattr(item, "thingML_State116", self)
                    

class thingML_PropertyAssign(AnnotatedElement):

    pass
class thingML_Function(AnnotatedElement):

    def __init__(self, name: str, thingML_Function: "thingML_Thing" = None, thingML_Function42: set["thingML_Parameter"] = None, thingML_Function44: "thingML_TypeRef" = None, thingML_Function47: "thingML_ActionBlock" = None, thingML_Function231: "thingML_FunctionCallExpression" = None, thingML_Function214: "thingML_FunctionCallStatement" = None):
        self.name = name
        self.thingML_Function = thingML_Function
        self.thingML_Function42 = thingML_Function42 if thingML_Function42 is not None else set()
        self.thingML_Function44 = thingML_Function44
        self.thingML_Function47 = thingML_Function47
        self.thingML_Function231 = thingML_Function231
        self.thingML_Function214 = thingML_Function214
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def thingML_Function44(self):
        return self.__thingML_Function44

    @thingML_Function44.setter
    def thingML_Function44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Function__thingML_Function44", None)
        self.__thingML_Function44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_TypeRef45"):
                opp_val = getattr(old_value, "thingML_TypeRef45", None)
                if opp_val == self:
                    setattr(old_value, "thingML_TypeRef45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_TypeRef45"):
                opp_val = getattr(value, "thingML_TypeRef45", None)
                setattr(value, "thingML_TypeRef45", self)

    @property
    def thingML_Function214(self):
        return self.__thingML_Function214

    @thingML_Function214.setter
    def thingML_Function214(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Function__thingML_Function214", None)
        self.__thingML_Function214 = value
        
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
    def thingML_Function231(self):
        return self.__thingML_Function231

    @thingML_Function231.setter
    def thingML_Function231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Function__thingML_Function231", None)
        self.__thingML_Function231 = value
        
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
    def thingML_Function(self):
        return self.__thingML_Function

    @thingML_Function.setter
    def thingML_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Function__thingML_Function", None)
        self.__thingML_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Thing25"):
                opp_val = getattr(old_value, "thingML_Thing25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Thing25"):
                opp_val = getattr(value, "thingML_Thing25", None)
                if opp_val is None:
                    setattr(value, "thingML_Thing25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def thingML_Function42(self):
        return self.__thingML_Function42

    @thingML_Function42.setter
    def thingML_Function42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Function__thingML_Function42", None)
        self.__thingML_Function42 = value if value is not None else set()
        
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
    def thingML_Function47(self):
        return self.__thingML_Function47

    @thingML_Function47.setter
    def thingML_Function47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Function__thingML_Function47", None)
        self.__thingML_Function47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_ActionBlock"):
                opp_val = getattr(old_value, "thingML_ActionBlock", None)
                if opp_val == self:
                    setattr(old_value, "thingML_ActionBlock", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_ActionBlock"):
                opp_val = getattr(value, "thingML_ActionBlock", None)
                setattr(value, "thingML_ActionBlock", self)

class thingML_Property(ReferencedElmt, Variable, AnnotatedElement):

    def __init__(self, changeable: bool, name: str, thingML_Property: "thingML_Thing" = None, thingML_Property34: "thingML_PropertyAssign" = None, thingML_Property49: "thingML_TypeRef" = None, thingML_Property52: "thingML_Expression" = None, thingML_Property135: "thingML_State" = None, thingML_Property248: "thingML_ConfigPropertyAssign" = None):
        self.changeable = changeable
        self.name = name
        self.thingML_Property = thingML_Property
        self.thingML_Property34 = thingML_Property34
        self.thingML_Property49 = thingML_Property49
        self.thingML_Property52 = thingML_Property52
        self.thingML_Property135 = thingML_Property135
        self.thingML_Property248 = thingML_Property248
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def changeable(self) -> bool:
        return self.__changeable

    @changeable.setter
    def changeable(self, changeable: bool):
        self.__changeable = changeable

    @property
    def thingML_Property34(self):
        return self.__thingML_Property34

    @thingML_Property34.setter
    def thingML_Property34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Property__thingML_Property34", None)
        self.__thingML_Property34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_PropertyAssign33"):
                opp_val = getattr(old_value, "thingML_PropertyAssign33", None)
                if opp_val == self:
                    setattr(old_value, "thingML_PropertyAssign33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_PropertyAssign33"):
                opp_val = getattr(value, "thingML_PropertyAssign33", None)
                setattr(value, "thingML_PropertyAssign33", self)

    @property
    def thingML_Property135(self):
        return self.__thingML_Property135

    @thingML_Property135.setter
    def thingML_Property135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Property__thingML_Property135", None)
        self.__thingML_Property135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_State134"):
                opp_val = getattr(old_value, "thingML_State134", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_State134"):
                opp_val = getattr(value, "thingML_State134", None)
                if opp_val is None:
                    setattr(value, "thingML_State134", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def thingML_Property52(self):
        return self.__thingML_Property52

    @thingML_Property52.setter
    def thingML_Property52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Property__thingML_Property52", None)
        self.__thingML_Property52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Expression53"):
                opp_val = getattr(old_value, "thingML_Expression53", None)
                if opp_val == self:
                    setattr(old_value, "thingML_Expression53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Expression53"):
                opp_val = getattr(value, "thingML_Expression53", None)
                setattr(value, "thingML_Expression53", self)

    @property
    def thingML_Property248(self):
        return self.__thingML_Property248

    @thingML_Property248.setter
    def thingML_Property248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Property__thingML_Property248", None)
        self.__thingML_Property248 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_ConfigPropertyAssign247"):
                opp_val = getattr(old_value, "thingML_ConfigPropertyAssign247", None)
                if opp_val == self:
                    setattr(old_value, "thingML_ConfigPropertyAssign247", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_ConfigPropertyAssign247"):
                opp_val = getattr(value, "thingML_ConfigPropertyAssign247", None)
                setattr(value, "thingML_ConfigPropertyAssign247", self)

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
            if hasattr(old_value, "thingML_Thing23"):
                opp_val = getattr(old_value, "thingML_Thing23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Thing23"):
                opp_val = getattr(value, "thingML_Thing23", None)
                if opp_val is None:
                    setattr(value, "thingML_Thing23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def thingML_Property49(self):
        return self.__thingML_Property49

    @thingML_Property49.setter
    def thingML_Property49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Property__thingML_Property49", None)
        self.__thingML_Property49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_TypeRef50"):
                opp_val = getattr(old_value, "thingML_TypeRef50", None)
                if opp_val == self:
                    setattr(old_value, "thingML_TypeRef50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_TypeRef50"):
                opp_val = getattr(value, "thingML_TypeRef50", None)
                setattr(value, "thingML_TypeRef50", self)

class thingML_Port(AnnotatedElement):

    def __init__(self, name: str, thingML_Port: "thingML_Thing" = None, thingML_Port61: set["thingML_Message"] = None, thingML_Port64: set["thingML_Message"] = None, thingML_Port174: "thingML_SendAction" = None, thingML_Port157: "thingML_ReceiveMessage" = None, thingML_Port271: "thingML_ExternalConnector" = None):
        self.name = name
        self.thingML_Port = thingML_Port
        self.thingML_Port61 = thingML_Port61 if thingML_Port61 is not None else set()
        self.thingML_Port64 = thingML_Port64 if thingML_Port64 is not None else set()
        self.thingML_Port174 = thingML_Port174
        self.thingML_Port157 = thingML_Port157
        self.thingML_Port271 = thingML_Port271
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def thingML_Port174(self):
        return self.__thingML_Port174

    @thingML_Port174.setter
    def thingML_Port174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Port__thingML_Port174", None)
        self.__thingML_Port174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_SendAction173"):
                opp_val = getattr(old_value, "thingML_SendAction173", None)
                if opp_val == self:
                    setattr(old_value, "thingML_SendAction173", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_SendAction173"):
                opp_val = getattr(value, "thingML_SendAction173", None)
                setattr(value, "thingML_SendAction173", self)

    @property
    def thingML_Port(self):
        return self.__thingML_Port

    @thingML_Port.setter
    def thingML_Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Port__thingML_Port", None)
        self.__thingML_Port = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Thing21"):
                opp_val = getattr(old_value, "thingML_Thing21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Thing21"):
                opp_val = getattr(value, "thingML_Thing21", None)
                if opp_val is None:
                    setattr(value, "thingML_Thing21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def thingML_Port271(self):
        return self.__thingML_Port271

    @thingML_Port271.setter
    def thingML_Port271(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Port__thingML_Port271", None)
        self.__thingML_Port271 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_ExternalConnector270"):
                opp_val = getattr(old_value, "thingML_ExternalConnector270", None)
                if opp_val == self:
                    setattr(old_value, "thingML_ExternalConnector270", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_ExternalConnector270"):
                opp_val = getattr(value, "thingML_ExternalConnector270", None)
                setattr(value, "thingML_ExternalConnector270", self)

    @property
    def thingML_Port157(self):
        return self.__thingML_Port157

    @thingML_Port157.setter
    def thingML_Port157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Port__thingML_Port157", None)
        self.__thingML_Port157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_ReceiveMessage156"):
                opp_val = getattr(old_value, "thingML_ReceiveMessage156", None)
                if opp_val == self:
                    setattr(old_value, "thingML_ReceiveMessage156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_ReceiveMessage156"):
                opp_val = getattr(value, "thingML_ReceiveMessage156", None)
                setattr(value, "thingML_ReceiveMessage156", self)

    @property
    def thingML_Port61(self):
        return self.__thingML_Port61

    @thingML_Port61.setter
    def thingML_Port61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Port__thingML_Port61", None)
        self.__thingML_Port61 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingML_Message62"):
                    opp_val = getattr(item, "thingML_Message62", None)
                    
                    if opp_val == self:
                        setattr(item, "thingML_Message62", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingML_Message62"):
                    opp_val = getattr(item, "thingML_Message62", None)
                    
                    setattr(item, "thingML_Message62", self)
                    

    @property
    def thingML_Port64(self):
        return self.__thingML_Port64

    @thingML_Port64.setter
    def thingML_Port64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Port__thingML_Port64", None)
        self.__thingML_Port64 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingML_Message65"):
                    opp_val = getattr(item, "thingML_Message65", None)
                    
                    if opp_val == self:
                        setattr(item, "thingML_Message65", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingML_Message65"):
                    opp_val = getattr(item, "thingML_Message65", None)
                    
                    setattr(item, "thingML_Message65", self)
                    

class thingML_Message(ReferencedElmt, AnnotatedElement):

    def __init__(self, name: str, thingML_Message: "thingML_Thing" = None, thingML_Message55: set["thingML_Parameter"] = None, thingML_Message62: "thingML_Port" = None, thingML_Message65: "thingML_Port" = None, thingML_Message76: "thingML_JoinSources" = None, thingML_Message86: "thingML_MergeSources" = None, thingML_Message107: "thingML_MessageParameter" = None, thingML_Message160: "thingML_ReceiveMessage" = None, thingML_Message177: "thingML_SendAction" = None):
        self.name = name
        self.thingML_Message = thingML_Message
        self.thingML_Message55 = thingML_Message55 if thingML_Message55 is not None else set()
        self.thingML_Message62 = thingML_Message62
        self.thingML_Message65 = thingML_Message65
        self.thingML_Message76 = thingML_Message76
        self.thingML_Message86 = thingML_Message86
        self.thingML_Message107 = thingML_Message107
        self.thingML_Message160 = thingML_Message160
        self.thingML_Message177 = thingML_Message177
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def thingML_Message160(self):
        return self.__thingML_Message160

    @thingML_Message160.setter
    def thingML_Message160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Message__thingML_Message160", None)
        self.__thingML_Message160 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_ReceiveMessage159"):
                opp_val = getattr(old_value, "thingML_ReceiveMessage159", None)
                if opp_val == self:
                    setattr(old_value, "thingML_ReceiveMessage159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_ReceiveMessage159"):
                opp_val = getattr(value, "thingML_ReceiveMessage159", None)
                setattr(value, "thingML_ReceiveMessage159", self)

    @property
    def thingML_Message(self):
        return self.__thingML_Message

    @thingML_Message.setter
    def thingML_Message(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Message__thingML_Message", None)
        self.__thingML_Message = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Thing19"):
                opp_val = getattr(old_value, "thingML_Thing19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Thing19"):
                opp_val = getattr(value, "thingML_Thing19", None)
                if opp_val is None:
                    setattr(value, "thingML_Thing19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def thingML_Message55(self):
        return self.__thingML_Message55

    @thingML_Message55.setter
    def thingML_Message55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Message__thingML_Message55", None)
        self.__thingML_Message55 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingML_Parameter56"):
                    opp_val = getattr(item, "thingML_Parameter56", None)
                    
                    if opp_val == self:
                        setattr(item, "thingML_Parameter56", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingML_Parameter56"):
                    opp_val = getattr(item, "thingML_Parameter56", None)
                    
                    setattr(item, "thingML_Parameter56", self)
                    

    @property
    def thingML_Message65(self):
        return self.__thingML_Message65

    @thingML_Message65.setter
    def thingML_Message65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Message__thingML_Message65", None)
        self.__thingML_Message65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Port64"):
                opp_val = getattr(old_value, "thingML_Port64", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Port64"):
                opp_val = getattr(value, "thingML_Port64", None)
                if opp_val is None:
                    setattr(value, "thingML_Port64", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def thingML_Message86(self):
        return self.__thingML_Message86

    @thingML_Message86.setter
    def thingML_Message86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Message__thingML_Message86", None)
        self.__thingML_Message86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_MergeSources85"):
                opp_val = getattr(old_value, "thingML_MergeSources85", None)
                if opp_val == self:
                    setattr(old_value, "thingML_MergeSources85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_MergeSources85"):
                opp_val = getattr(value, "thingML_MergeSources85", None)
                setattr(value, "thingML_MergeSources85", self)

    @property
    def thingML_Message62(self):
        return self.__thingML_Message62

    @thingML_Message62.setter
    def thingML_Message62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Message__thingML_Message62", None)
        self.__thingML_Message62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Port61"):
                opp_val = getattr(old_value, "thingML_Port61", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Port61"):
                opp_val = getattr(value, "thingML_Port61", None)
                if opp_val is None:
                    setattr(value, "thingML_Port61", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def thingML_Message177(self):
        return self.__thingML_Message177

    @thingML_Message177.setter
    def thingML_Message177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Message__thingML_Message177", None)
        self.__thingML_Message177 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_SendAction176"):
                opp_val = getattr(old_value, "thingML_SendAction176", None)
                if opp_val == self:
                    setattr(old_value, "thingML_SendAction176", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_SendAction176"):
                opp_val = getattr(value, "thingML_SendAction176", None)
                setattr(value, "thingML_SendAction176", self)

    @property
    def thingML_Message107(self):
        return self.__thingML_Message107

    @thingML_Message107.setter
    def thingML_Message107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Message__thingML_Message107", None)
        self.__thingML_Message107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_MessageParameter"):
                opp_val = getattr(old_value, "thingML_MessageParameter", None)
                if opp_val == self:
                    setattr(old_value, "thingML_MessageParameter", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_MessageParameter"):
                opp_val = getattr(value, "thingML_MessageParameter", None)
                setattr(value, "thingML_MessageParameter", self)

    @property
    def thingML_Message76(self):
        return self.__thingML_Message76

    @thingML_Message76.setter
    def thingML_Message76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Message__thingML_Message76", None)
        self.__thingML_Message76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_JoinSources75"):
                opp_val = getattr(old_value, "thingML_JoinSources75", None)
                if opp_val == self:
                    setattr(old_value, "thingML_JoinSources75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_JoinSources75"):
                opp_val = getattr(value, "thingML_JoinSources75", None)
                setattr(value, "thingML_JoinSources75", self)

class thingML_Type(AnnotatedElement):

    def __init__(self, name: str, thingML_Type9: "thingML_TypeRef" = None, thingML_Type: "thingML_ThingMLModel" = None):
        self.name = name
        self.thingML_Type9 = thingML_Type9
        self.thingML_Type = thingML_Type
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def thingML_Type(self):
        return self.__thingML_Type

    @thingML_Type.setter
    def thingML_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Type__thingML_Type", None)
        self.__thingML_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_ThingMLModel2"):
                opp_val = getattr(old_value, "thingML_ThingMLModel2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_ThingMLModel2"):
                opp_val = getattr(value, "thingML_ThingMLModel2", None)
                if opp_val is None:
                    setattr(value, "thingML_ThingMLModel2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def thingML_Type9(self):
        return self.__thingML_Type9

    @thingML_Type9.setter
    def thingML_Type9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Type__thingML_Type9", None)
        self.__thingML_Type9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_TypeRef"):
                opp_val = getattr(old_value, "thingML_TypeRef", None)
                if opp_val == self:
                    setattr(old_value, "thingML_TypeRef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_TypeRef"):
                opp_val = getattr(value, "thingML_TypeRef", None)
                setattr(value, "thingML_TypeRef", self)

class thingML_Import:

    def __init__(self, importURI: str, thingML_Import: "thingML_ThingMLModel" = None):
        self.importURI = importURI
        self.thingML_Import = thingML_Import
        
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
class thingML_Expression(ABC):

    pass
class thingML_TypeRef:

    def __init__(self, isArray: bool, thingML_TypeRef: "thingML_Type" = None, thingML_TypeRef11: "thingML_Expression" = None, thingML_TypeRef59: "thingML_Parameter" = None, thingML_TypeRef45: "thingML_Function" = None, thingML_TypeRef50: "thingML_Property" = None, thingML_TypeRef168: "thingML_LocalVariable" = None):
        self.isArray = isArray
        self.thingML_TypeRef = thingML_TypeRef
        self.thingML_TypeRef11 = thingML_TypeRef11
        self.thingML_TypeRef59 = thingML_TypeRef59
        self.thingML_TypeRef45 = thingML_TypeRef45
        self.thingML_TypeRef50 = thingML_TypeRef50
        self.thingML_TypeRef168 = thingML_TypeRef168
        
    @property
    def isArray(self) -> bool:
        return self.__isArray

    @isArray.setter
    def isArray(self, isArray: bool):
        self.__isArray = isArray

    @property
    def thingML_TypeRef11(self):
        return self.__thingML_TypeRef11

    @thingML_TypeRef11.setter
    def thingML_TypeRef11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_TypeRef__thingML_TypeRef11", None)
        self.__thingML_TypeRef11 = value
        
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
    def thingML_TypeRef45(self):
        return self.__thingML_TypeRef45

    @thingML_TypeRef45.setter
    def thingML_TypeRef45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_TypeRef__thingML_TypeRef45", None)
        self.__thingML_TypeRef45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Function44"):
                opp_val = getattr(old_value, "thingML_Function44", None)
                if opp_val == self:
                    setattr(old_value, "thingML_Function44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Function44"):
                opp_val = getattr(value, "thingML_Function44", None)
                setattr(value, "thingML_Function44", self)

    @property
    def thingML_TypeRef59(self):
        return self.__thingML_TypeRef59

    @thingML_TypeRef59.setter
    def thingML_TypeRef59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_TypeRef__thingML_TypeRef59", None)
        self.__thingML_TypeRef59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Parameter58"):
                opp_val = getattr(old_value, "thingML_Parameter58", None)
                if opp_val == self:
                    setattr(old_value, "thingML_Parameter58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Parameter58"):
                opp_val = getattr(value, "thingML_Parameter58", None)
                setattr(value, "thingML_Parameter58", self)

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
            if hasattr(old_value, "thingML_Type9"):
                opp_val = getattr(old_value, "thingML_Type9", None)
                if opp_val == self:
                    setattr(old_value, "thingML_Type9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Type9"):
                opp_val = getattr(value, "thingML_Type9", None)
                setattr(value, "thingML_Type9", self)

    @property
    def thingML_TypeRef168(self):
        return self.__thingML_TypeRef168

    @thingML_TypeRef168.setter
    def thingML_TypeRef168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_TypeRef__thingML_TypeRef168", None)
        self.__thingML_TypeRef168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_LocalVariable167"):
                opp_val = getattr(old_value, "thingML_LocalVariable167", None)
                if opp_val == self:
                    setattr(old_value, "thingML_LocalVariable167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_LocalVariable167"):
                opp_val = getattr(value, "thingML_LocalVariable167", None)
                setattr(value, "thingML_LocalVariable167", self)

    @property
    def thingML_TypeRef50(self):
        return self.__thingML_TypeRef50

    @thingML_TypeRef50.setter
    def thingML_TypeRef50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_TypeRef__thingML_TypeRef50", None)
        self.__thingML_TypeRef50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_Property49"):
                opp_val = getattr(old_value, "thingML_Property49", None)
                if opp_val == self:
                    setattr(old_value, "thingML_Property49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_Property49"):
                opp_val = getattr(value, "thingML_Property49", None)
                setattr(value, "thingML_Property49", self)

class thingML_AnnotatedElement(ABC):

    pass
class thingML_PlatformAnnotation:

    def __init__(self, name: str, value: str, thingML_PlatformAnnotation: "thingML_AnnotatedElement" = None, thingML_PlatformAnnotation15: "thingML_EnumerationLiteral" = None, thingML_PlatformAnnotation257: "thingML_ConfigPropertyAssign" = None):
        self.name = name
        self.value = value
        self.thingML_PlatformAnnotation = thingML_PlatformAnnotation
        self.thingML_PlatformAnnotation15 = thingML_PlatformAnnotation15
        self.thingML_PlatformAnnotation257 = thingML_PlatformAnnotation257
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def thingML_PlatformAnnotation15(self):
        return self.__thingML_PlatformAnnotation15

    @thingML_PlatformAnnotation15.setter
    def thingML_PlatformAnnotation15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_PlatformAnnotation__thingML_PlatformAnnotation15", None)
        self.__thingML_PlatformAnnotation15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_EnumerationLiteral14"):
                opp_val = getattr(old_value, "thingML_EnumerationLiteral14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_EnumerationLiteral14"):
                opp_val = getattr(value, "thingML_EnumerationLiteral14", None)
                if opp_val is None:
                    setattr(value, "thingML_EnumerationLiteral14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def thingML_PlatformAnnotation257(self):
        return self.__thingML_PlatformAnnotation257

    @thingML_PlatformAnnotation257.setter
    def thingML_PlatformAnnotation257(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_PlatformAnnotation__thingML_PlatformAnnotation257", None)
        self.__thingML_PlatformAnnotation257 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_ConfigPropertyAssign256"):
                opp_val = getattr(old_value, "thingML_ConfigPropertyAssign256", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_ConfigPropertyAssign256"):
                opp_val = getattr(value, "thingML_ConfigPropertyAssign256", None)
                if opp_val is None:
                    setattr(value, "thingML_ConfigPropertyAssign256", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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

class thingML_Configuration(AnnotatedElement):

    def __init__(self, name: str, thingML_Configuration: "thingML_ThingMLModel" = None, thingML_Configuration236: set["thingML_Instance"] = None, thingML_Configuration238: set["thingML_AbstractConnector"] = None, thingML_Configuration240: set["thingML_ConfigPropertyAssign"] = None):
        self.name = name
        self.thingML_Configuration = thingML_Configuration
        self.thingML_Configuration236 = thingML_Configuration236 if thingML_Configuration236 is not None else set()
        self.thingML_Configuration238 = thingML_Configuration238 if thingML_Configuration238 is not None else set()
        self.thingML_Configuration240 = thingML_Configuration240 if thingML_Configuration240 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def thingML_Configuration240(self):
        return self.__thingML_Configuration240

    @thingML_Configuration240.setter
    def thingML_Configuration240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Configuration__thingML_Configuration240", None)
        self.__thingML_Configuration240 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingML_ConfigPropertyAssign"):
                    opp_val = getattr(item, "thingML_ConfigPropertyAssign", None)
                    
                    if opp_val == self:
                        setattr(item, "thingML_ConfigPropertyAssign", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingML_ConfigPropertyAssign"):
                    opp_val = getattr(item, "thingML_ConfigPropertyAssign", None)
                    
                    setattr(item, "thingML_ConfigPropertyAssign", self)
                    

    @property
    def thingML_Configuration(self):
        return self.__thingML_Configuration

    @thingML_Configuration.setter
    def thingML_Configuration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Configuration__thingML_Configuration", None)
        self.__thingML_Configuration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_ThingMLModel6"):
                opp_val = getattr(old_value, "thingML_ThingMLModel6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_ThingMLModel6"):
                opp_val = getattr(value, "thingML_ThingMLModel6", None)
                if opp_val is None:
                    setattr(value, "thingML_ThingMLModel6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def thingML_Configuration236(self):
        return self.__thingML_Configuration236

    @thingML_Configuration236.setter
    def thingML_Configuration236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Configuration__thingML_Configuration236", None)
        self.__thingML_Configuration236 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingML_Instance"):
                    opp_val = getattr(item, "thingML_Instance", None)
                    
                    if opp_val == self:
                        setattr(item, "thingML_Instance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingML_Instance"):
                    opp_val = getattr(item, "thingML_Instance", None)
                    
                    setattr(item, "thingML_Instance", self)
                    

    @property
    def thingML_Configuration238(self):
        return self.__thingML_Configuration238

    @thingML_Configuration238.setter
    def thingML_Configuration238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Configuration__thingML_Configuration238", None)
        self.__thingML_Configuration238 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "thingML_AbstractConnector"):
                    opp_val = getattr(item, "thingML_AbstractConnector", None)
                    
                    if opp_val == self:
                        setattr(item, "thingML_AbstractConnector", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "thingML_AbstractConnector"):
                    opp_val = getattr(item, "thingML_AbstractConnector", None)
                    
                    setattr(item, "thingML_AbstractConnector", self)
                    

class thingML_Protocol(AnnotatedElement):

    def __init__(self, name: str, thingML_Protocol: "thingML_ThingMLModel" = None, thingML_Protocol274: "thingML_ExternalConnector" = None):
        self.name = name
        self.thingML_Protocol = thingML_Protocol
        self.thingML_Protocol274 = thingML_Protocol274
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def thingML_Protocol(self):
        return self.__thingML_Protocol

    @thingML_Protocol.setter
    def thingML_Protocol(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Protocol__thingML_Protocol", None)
        self.__thingML_Protocol = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_ThingMLModel4"):
                opp_val = getattr(old_value, "thingML_ThingMLModel4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_ThingMLModel4"):
                opp_val = getattr(value, "thingML_ThingMLModel4", None)
                if opp_val is None:
                    setattr(value, "thingML_ThingMLModel4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def thingML_Protocol274(self):
        return self.__thingML_Protocol274

    @thingML_Protocol274.setter
    def thingML_Protocol274(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_thingML_Protocol__thingML_Protocol274", None)
        self.__thingML_Protocol274 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "thingML_ExternalConnector273"):
                opp_val = getattr(old_value, "thingML_ExternalConnector273", None)
                if opp_val == self:
                    setattr(old_value, "thingML_ExternalConnector273", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "thingML_ExternalConnector273"):
                opp_val = getattr(value, "thingML_ExternalConnector273", None)
                setattr(value, "thingML_ExternalConnector273", self)
