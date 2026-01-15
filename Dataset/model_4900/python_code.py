from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ServerErrorKind(Enum):
    BAD_GATEWAY = "BAD_GATEWAY"
    MESSAGE_TOO_LARGE = "MESSAGE_TOO_LARGE"
    NOT_IMPLEMENTED = "NOT_IMPLEMENTED"
    SERVER_INTERNAL_ERROR = "SERVER_INTERNAL_ERROR"
    SERVER_TIMEOUT = "SERVER_TIMEOUT"
    SERVICE_UNAVAILABLE = "SERVICE_UNAVAILABLE"
    VERSION_NOT_SUPPORTED = "VERSION_NOT_SUPPORTED"
class FunctionLocation(Enum):
    remote = "remote"
    local = "local"
class ControlMethod(Enum):
    deploy = "deploy"
    undeploy = "undeploy"
    uninvite = "uninvite"
    unregister = "unregister"
    unsubscribe = "unsubscribe"
class Direction(Enum):
    out = "out"
    inout = "inout"
    in = "in"
class PrimitiveType(Enum):
    void = "void"
    bool = "bool"
    int = "int"
    request = "request"
    response = "response"
    string = "string"
    time = "time"
    uri = "uri"
class ClientErrorKind(Enum):
    ADDRESS_INCOMPLETE = "ADDRESS_INCOMPLETE"
    AMBIGUOUS = "AMBIGUOUS"
    BAD_EXTENSION = "BAD_EXTENSION"
    BAD_REQUEST = "BAD_REQUEST"
    BUSY_HERE = "BUSY_HERE"
    CALL_OR_TRANSACTION_DOES_NOT_EXIST = "CALL_OR_TRANSACTION_DOES_NOT_EXIST"
    EXTENSION_REQUIRED = "EXTENSION_REQUIRED"
    FORBIDDEN = "FORBIDDEN"
    GONE = "GONE"
    INTERVAL_TOO_BRIEF = "INTERVAL_TOO_BRIEF"
    LOOP_DETECTED = "LOOP_DETECTED"
    METHOD_NOT_ALLOWED = "METHOD_NOT_ALLOWED"
    NOT_ACCEPTABLE_HERE = "NOT_ACCEPTABLE_HERE"
    NOT_ACCEPTABLE = "NOT_ACCEPTABLE"
    NOT_FOUND = "NOT_FOUND"
    PAYMENT_REQUIRED = "PAYMENT_REQUIRED"
    PROXY_AUTHENTICATION_REQUIRED = "PROXY_AUTHENTICATION_REQUIRED"
    REQUESTURI_TOO_LONG = "REQUESTURI_TOO_LONG"
    REQUEST_ENTITY_TOO_LARGE = "REQUEST_ENTITY_TOO_LARGE"
    REQUEST_PENDING = "REQUEST_PENDING"
    REQUEST_TERMINATED = "REQUEST_TERMINATED"
    REQUEST_TIMEOUT = "REQUEST_TIMEOUT"
    TEMPORARILY_UNAVAILABLE = "TEMPORARILY_UNAVAILABLE"
    TOO_MANY_HOPS = "TOO_MANY_HOPS"
    UNAUTHORIZED = "UNAUTHORIZED"
    UNDECIPHERABLE = "UNDECIPHERABLE"
    UNSUPPORTED_MEDIA_TYPE = "UNSUPPORTED_MEDIA_TYPE"
    UNSUPPORTED_URI_SCHEME = "UNSUPPORTED_URI_SCHEME"
class SuccessKind(Enum):
    OK = "OK"
    ACCEPTED = "ACCEPTED"
class GlobalErrorKind(Enum):
    DOES_NOT_EXIST_ANYWHERE = "DOES_NOT_EXIST_ANYWHERE"
    NOT_ACCEPTABLE = "NOT_ACCEPTABLE"
    BUSY_EVERYWHERE = "BUSY_EVERYWHERE"
    DECLINE = "DECLINE"
class SIPHeader(Enum):
    CALL_ID = "CALL_ID"
    CONTACT = "CONTACT"
    CSEQ = "CSEQ"
    EVENT = "EVENT"
    FROM = "FROM"
    MAX_FORWARDS = "MAX_FORWARDS"
    SUBSCRIPTION_STATE = "SUBSCRIPTION_STATE"
    TO = "TO"
    VIA = "VIA"
class SIPMethod(Enum):
    ACK = "ACK"
    BYE = "BYE"
    CANCEL = "CANCEL"
    INVITE = "INVITE"
    NOTIFY = "NOTIFY"
    OPTIONS = "OPTIONS"
    REACK = "REACK"
    REGISTER = "REGISTER"
    REINVITE = "REINVITE"
    REREGISTER = "REREGISTER"
    RESUBSCRIBE = "RESUBSCRIBE"
    SUBSCRIBE = "SUBSCRIBE"
class Modifier(Enum):
    LIFO = "LIFO"
    FIFO = "FIFO"
class RedirectionErrorKind(Enum):
    ALTERNATIVE_SERVICE = "ALTERNATIVE_SERVICE"
    MOVED_PERMANENTLY = "MOVED_PERMANENTLY"
    MOVED_TEMPORARILY = "MOVED_TEMPORARILY"
    MULTIPLE_CHOICES = "MULTIPLE_CHOICES"
    USE_PROXY = "USE_PROXY"


############################################
# Definition of Classes
############################################

class ErrorResponse:

    pass
class SPL_ServerErrorResponse(ErrorResponse):

    def __init__(self, errorKind: str):
        self.errorKind = errorKind
        
    @property
    def errorKind(self) -> str:
        return self.__errorKind

    @errorKind.setter
    def errorKind(self, errorKind: str):
        self.__errorKind = errorKind

class SPL_RedirectionErrorResponse(ErrorResponse):

    def __init__(self, errorKind: str):
        self.errorKind = errorKind
        
    @property
    def errorKind(self) -> str:
        return self.__errorKind

    @errorKind.setter
    def errorKind(self, errorKind: str):
        self.__errorKind = errorKind

class SPL_GlobalErrorResponse(ErrorResponse):

    def __init__(self, errorKind: str):
        self.errorKind = errorKind
        
    @property
    def errorKind(self) -> str:
        return self.__errorKind

    @errorKind.setter
    def errorKind(self, errorKind: str):
        self.__errorKind = errorKind

class SPL_ClientErrorResponse(ErrorResponse):

    def __init__(self, errorKind: str):
        self.errorKind = errorKind
        
    @property
    def errorKind(self) -> str:
        return self.__errorKind

    @errorKind.setter
    def errorKind(self, errorKind: str):
        self.__errorKind = errorKind

class Response:

    pass
class SPL_ErrorResponse(Response):

    pass
class SPL_SuccessResponse(Response):

    def __init__(self, successKind: str):
        self.successKind = successKind
        
    @property
    def successKind(self) -> str:
        return self.__successKind

    @successKind.setter
    def successKind(self, successKind: str):
        self.__successKind = successKind

class VariablePlace:

    pass
class SPL_PropertyCallPlace(VariablePlace):

    def __init__(self, propName: str, SPL_PropertyCallPlace: "SPL_VariablePlace" = None):
        self.propName = propName
        self.SPL_PropertyCallPlace = SPL_PropertyCallPlace
        
    @property
    def propName(self) -> str:
        return self.__propName

    @propName.setter
    def propName(self, propName: str):
        self.__propName = propName

    @property
    def SPL_PropertyCallPlace(self):
        return self.__SPL_PropertyCallPlace

    @SPL_PropertyCallPlace.setter
    def SPL_PropertyCallPlace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SPL_PropertyCallPlace__SPL_PropertyCallPlace", None)
        self.__SPL_PropertyCallPlace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SPL_VariablePlace"):
                opp_val = getattr(old_value, "SPL_VariablePlace", None)
                if opp_val == self:
                    setattr(old_value, "SPL_VariablePlace", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SPL_VariablePlace"):
                opp_val = getattr(value, "SPL_VariablePlace", None)
                setattr(value, "SPL_VariablePlace", self)

class Place:

    pass
class SPL_VariablePlace(Place):

    pass
class SPL_SIPHeaderPlace(Place):

    def __init__(self, header: str):
        self.header = header
        
    @property
    def header(self) -> str:
        return self.__header

    @header.setter
    def header(self, header: str):
        self.__header = header

class Constant:

    pass
class SPL_StringConstant(Constant):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class SPL_ResponseConstant(Constant):

    pass
class SPL_IntegerConstant(Constant):

    def __init__(self, value: int):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class SPL_SequenceConstant(Constant):

    pass
class SPL_URIConstant(Constant):

    def __init__(self, uri: str):
        self.uri = uri
        
    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

class SPL_BooleanConstant(Constant):

    def __init__(self, value: bool):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class MessageField:

    pass
class SPL_HeadedMessageField(MessageField):

    def __init__(self, headerId: str):
        self.headerId = headerId
        
    @property
    def headerId(self) -> str:
        return self.__headerId

    @headerId.setter
    def headerId(self, headerId: str):
        self.__headerId = headerId

class SPL_ReasonMessageField(MessageField):

    pass
class Expression:

    pass
class SPL_ForwardExp(Expression):

    def __init__(self, isParallel: bool, SPL_ForwardExp: "SPL_Expression" = None):
        self.isParallel = isParallel
        self.SPL_ForwardExp = SPL_ForwardExp
        
    @property
    def isParallel(self) -> bool:
        return self.__isParallel

    @isParallel.setter
    def isParallel(self, isParallel: bool):
        self.__isParallel = isParallel

    @property
    def SPL_ForwardExp(self):
        return self.__SPL_ForwardExp

    @SPL_ForwardExp.setter
    def SPL_ForwardExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SPL_ForwardExp__SPL_ForwardExp", None)
        self.__SPL_ForwardExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SPL_Expression114"):
                opp_val = getattr(old_value, "SPL_Expression114", None)
                if opp_val == self:
                    setattr(old_value, "SPL_Expression114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SPL_Expression114"):
                opp_val = getattr(value, "SPL_Expression114", None)
                setattr(value, "SPL_Expression114", self)

class SPL_OperatorExp(Expression):

    def __init__(self, opName: str, SPL_OperatorExp: "SPL_Expression" = None, SPL_OperatorExp111: "SPL_Expression" = None):
        self.opName = opName
        self.SPL_OperatorExp = SPL_OperatorExp
        self.SPL_OperatorExp111 = SPL_OperatorExp111
        
    @property
    def opName(self) -> str:
        return self.__opName

    @opName.setter
    def opName(self, opName: str):
        self.__opName = opName

    @property
    def SPL_OperatorExp111(self):
        return self.__SPL_OperatorExp111

    @SPL_OperatorExp111.setter
    def SPL_OperatorExp111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SPL_OperatorExp__SPL_OperatorExp111", None)
        self.__SPL_OperatorExp111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SPL_Expression112"):
                opp_val = getattr(old_value, "SPL_Expression112", None)
                if opp_val == self:
                    setattr(old_value, "SPL_Expression112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SPL_Expression112"):
                opp_val = getattr(value, "SPL_Expression112", None)
                setattr(value, "SPL_Expression112", self)

    @property
    def SPL_OperatorExp(self):
        return self.__SPL_OperatorExp

    @SPL_OperatorExp.setter
    def SPL_OperatorExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SPL_OperatorExp__SPL_OperatorExp", None)
        self.__SPL_OperatorExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SPL_Expression109"):
                opp_val = getattr(old_value, "SPL_Expression109", None)
                if opp_val == self:
                    setattr(old_value, "SPL_Expression109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SPL_Expression109"):
                opp_val = getattr(value, "SPL_Expression109", None)
                setattr(value, "SPL_Expression109", self)

class SPL_ConstantExp(Expression):

    pass
class SelectMember:

    pass
class SPL_FunctionCallExp(Expression):

    pass
class SPL_PopExp(Expression):

    pass
class SPL_RequestURIExp(Expression):

    pass
class SPL_BODYExp(Expression):

    pass
class SPL_ReasonExp(Expression):

    pass
class SPL_BlockExp(Expression):

    pass
class SPL_WithExp(Expression):

    pass
class SPL_SelectDefault(SelectMember):

    pass
class SPL_SelectCase(SelectMember):

    pass
class SPL_Place(Expression):

    pass
class Statement:

    pass
class SPL_BreakStat(Statement):

    pass
class SPL_SelectStat(Statement):

    pass
class SPL_ForeachStat(Statement):

    def __init__(self, iteratorName: str, SPL_ForeachStat: "SPL_Expression" = None, SPL_ForeachStat84: set["SPL_Statement"] = None):
        self.iteratorName = iteratorName
        self.SPL_ForeachStat = SPL_ForeachStat
        self.SPL_ForeachStat84 = SPL_ForeachStat84 if SPL_ForeachStat84 is not None else set()
        
    @property
    def iteratorName(self) -> str:
        return self.__iteratorName

    @iteratorName.setter
    def iteratorName(self, iteratorName: str):
        self.__iteratorName = iteratorName

    @property
    def SPL_ForeachStat84(self):
        return self.__SPL_ForeachStat84

    @SPL_ForeachStat84.setter
    def SPL_ForeachStat84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SPL_ForeachStat__SPL_ForeachStat84", None)
        self.__SPL_ForeachStat84 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SPL_Statement85"):
                    opp_val = getattr(item, "SPL_Statement85", None)
                    
                    if opp_val == self:
                        setattr(item, "SPL_Statement85", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SPL_Statement85"):
                    opp_val = getattr(item, "SPL_Statement85", None)
                    
                    setattr(item, "SPL_Statement85", self)
                    

    @property
    def SPL_ForeachStat(self):
        return self.__SPL_ForeachStat

    @SPL_ForeachStat.setter
    def SPL_ForeachStat(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SPL_ForeachStat__SPL_ForeachStat", None)
        self.__SPL_ForeachStat = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SPL_Expression82"):
                opp_val = getattr(old_value, "SPL_Expression82", None)
                if opp_val == self:
                    setattr(old_value, "SPL_Expression82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SPL_Expression82"):
                opp_val = getattr(value, "SPL_Expression82", None)
                setattr(value, "SPL_Expression82", self)

class SPL_PushStat(Statement):

    pass
class SPL_ContinueStat(Statement):

    pass
class SPL_FunctionCallStat(Statement):

    pass
class SPL_SetStat(Statement):

    pass
class SPL_CompoundStat(Statement):

    pass
class SPL_Variable(VariablePlace):

    pass
class SPL_WhenStat(Statement):

    pass
class SPL_IfStat(Statement):

    pass
class SPL_ReturnStat(Statement):

    pass
class SPL_DeclarationStat(Statement):

    pass
class Declaration:

    pass
class SPL_StructureDeclaration(Declaration):

    pass
class SPL_FunctionDeclaration(Declaration):

    pass
class SPL_VariableDeclaration(Declaration):

    pass
class FunctionDeclaration:

    pass
class SPL_LocalFunctionDeclaration(FunctionDeclaration):

    pass
class SPL_RemoteFunctionDeclaration(FunctionDeclaration):

    def __init__(self, functionLocation: str):
        self.functionLocation = functionLocation
        
    @property
    def functionLocation(self) -> str:
        return self.__functionLocation

    @functionLocation.setter
    def functionLocation(self, functionLocation: str):
        self.__functionLocation = functionLocation

class TypeExpression:

    pass
class SPL_SequenceType(TypeExpression):

    def __init__(self, modifier: str, type: str, size: int):
        self.modifier = modifier
        self.type = type
        self.size = size
        
    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def modifier(self) -> str:
        return self.__modifier

    @modifier.setter
    def modifier(self, modifier: str):
        self.__modifier = modifier

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class SPL_DefinedType(TypeExpression):

    def __init__(self, typeName: str):
        self.typeName = typeName
        
    @property
    def typeName(self) -> str:
        return self.__typeName

    @typeName.setter
    def typeName(self, typeName: str):
        self.__typeName = typeName

class SPL_SimpleType(TypeExpression):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class Branch:

    pass
class SPL_NamedBranch(Branch):

    def __init__(self, name: str, SPL_NamedBranch: "SPL_ReturnStat" = None):
        self.name = name
        self.SPL_NamedBranch = SPL_NamedBranch
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SPL_NamedBranch(self):
        return self.__SPL_NamedBranch

    @SPL_NamedBranch.setter
    def SPL_NamedBranch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SPL_NamedBranch__SPL_NamedBranch", None)
        self.__SPL_NamedBranch = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SPL_ReturnStat63"):
                opp_val = getattr(old_value, "SPL_ReturnStat63", None)
                if opp_val == self:
                    setattr(old_value, "SPL_ReturnStat63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SPL_ReturnStat63"):
                opp_val = getattr(value, "SPL_ReturnStat63", None)
                setattr(value, "SPL_ReturnStat63", self)

class SPL_DefaultBranch(Branch):

    pass
class MethodName:

    pass
class SPL_ControlMethodName(MethodName):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class SPL_SIPMethodName(MethodName):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class VariableDeclaration:

    pass
class SPL_WhenHeader(VariableDeclaration):

    def __init__(self, headerId: str, SPL_WhenHeader100: "SPL_Constant" = None, SPL_WhenHeader: "SPL_WhenStat" = None):
        self.headerId = headerId
        self.SPL_WhenHeader100 = SPL_WhenHeader100
        self.SPL_WhenHeader = SPL_WhenHeader
        
    @property
    def headerId(self) -> str:
        return self.__headerId

    @headerId.setter
    def headerId(self, headerId: str):
        self.__headerId = headerId

    @property
    def SPL_WhenHeader(self):
        return self.__SPL_WhenHeader

    @SPL_WhenHeader.setter
    def SPL_WhenHeader(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SPL_WhenHeader__SPL_WhenHeader", None)
        self.__SPL_WhenHeader = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SPL_WhenStat74"):
                opp_val = getattr(old_value, "SPL_WhenStat74", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SPL_WhenStat74"):
                opp_val = getattr(value, "SPL_WhenStat74", None)
                if opp_val is None:
                    setattr(value, "SPL_WhenStat74", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SPL_WhenHeader100(self):
        return self.__SPL_WhenHeader100

    @SPL_WhenHeader100.setter
    def SPL_WhenHeader100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SPL_WhenHeader__SPL_WhenHeader100", None)
        self.__SPL_WhenHeader100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SPL_Constant"):
                opp_val = getattr(old_value, "SPL_Constant", None)
                if opp_val == self:
                    setattr(old_value, "SPL_Constant", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SPL_Constant"):
                opp_val = getattr(value, "SPL_Constant", None)
                setattr(value, "SPL_Constant", self)

class SPL_Argument(VariableDeclaration):

    pass
class LocatedElement:

    pass
class SPL_Constant(LocatedElement):

    pass
class SPL_Response(LocatedElement):

    pass
class SPL_FunctionCall(LocatedElement):

    pass
class SPL_Statement(LocatedElement):

    pass
class SPL_StructureProperty(LocatedElement):

    def __init__(self, name: str, SPL_StructureProperty: "SPL_TypeExpression" = None):
        self.name = name
        self.SPL_StructureProperty = SPL_StructureProperty
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SPL_StructureProperty(self):
        return self.__SPL_StructureProperty

    @SPL_StructureProperty.setter
    def SPL_StructureProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SPL_StructureProperty__SPL_StructureProperty", None)
        self.__SPL_StructureProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SPL_TypeExpression46"):
                opp_val = getattr(old_value, "SPL_TypeExpression46", None)
                if opp_val == self:
                    setattr(old_value, "SPL_TypeExpression46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SPL_TypeExpression46"):
                opp_val = getattr(value, "SPL_TypeExpression46", None)
                setattr(value, "SPL_TypeExpression46", self)

class SPL_Expression(LocatedElement):

    pass
class SPL_MethodName(LocatedElement):

    pass
class SPL_Branch(LocatedElement):

    pass
class SPL_TypeExpression(LocatedElement):

    pass
class SPL_Service(LocatedElement):

    def __init__(self, name: str, SPL_Service2: set["SPL_Declaration"] = None, SPL_Service4: set["SPL_Session"] = None, SPL_Service: "SPL_Program" = None):
        self.name = name
        self.SPL_Service2 = SPL_Service2 if SPL_Service2 is not None else set()
        self.SPL_Service4 = SPL_Service4 if SPL_Service4 is not None else set()
        self.SPL_Service = SPL_Service
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SPL_Service4(self):
        return self.__SPL_Service4

    @SPL_Service4.setter
    def SPL_Service4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SPL_Service__SPL_Service4", None)
        self.__SPL_Service4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SPL_Session"):
                    opp_val = getattr(item, "SPL_Session", None)
                    
                    if opp_val == self:
                        setattr(item, "SPL_Session", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SPL_Session"):
                    opp_val = getattr(item, "SPL_Session", None)
                    
                    setattr(item, "SPL_Session", self)
                    

    @property
    def SPL_Service2(self):
        return self.__SPL_Service2

    @SPL_Service2.setter
    def SPL_Service2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SPL_Service__SPL_Service2", None)
        self.__SPL_Service2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SPL_Declaration"):
                    opp_val = getattr(item, "SPL_Declaration", None)
                    
                    if opp_val == self:
                        setattr(item, "SPL_Declaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SPL_Declaration"):
                    opp_val = getattr(item, "SPL_Declaration", None)
                    
                    setattr(item, "SPL_Declaration", self)
                    

    @property
    def SPL_Service(self):
        return self.__SPL_Service

    @SPL_Service.setter
    def SPL_Service(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SPL_Service__SPL_Service", None)
        self.__SPL_Service = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SPL_Program"):
                opp_val = getattr(old_value, "SPL_Program", None)
                if opp_val == self:
                    setattr(old_value, "SPL_Program", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SPL_Program"):
                opp_val = getattr(value, "SPL_Program", None)
                setattr(value, "SPL_Program", self)

class SPL_SelectMember(LocatedElement):

    pass
class SPL_MessageField(LocatedElement):

    pass
class SPL_Program(LocatedElement):

    pass
class SPL_LocatedElement(ABC):

    def __init__(self, location: str, commentsBefore: str, commentsAfter: str):
        self.location = location
        self.commentsBefore = commentsBefore
        self.commentsAfter = commentsAfter
        
    @property
    def commentsBefore(self) -> str:
        return self.__commentsBefore

    @commentsBefore.setter
    def commentsBefore(self, commentsBefore: str):
        self.__commentsBefore = commentsBefore

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def commentsAfter(self) -> str:
        return self.__commentsAfter

    @commentsAfter.setter
    def commentsAfter(self, commentsAfter: str):
        self.__commentsAfter = commentsAfter

class Session:

    pass
class SPL_Dialog(Session):

    pass
class SPL_Method(Session):

    def __init__(self, direction: str, SPL_Method: "SPL_Dialog" = None, SPL_Method18: "SPL_Event" = None, SPL_Method20: "SPL_TypeExpression" = None, SPL_Method22: "SPL_MethodName" = None, SPL_Method24: set["SPL_Argument"] = None, SPL_Method26: set["SPL_Statement"] = None, SPL_Method28: set["SPL_Branch"] = None):
        self.direction = direction
        self.SPL_Method = SPL_Method
        self.SPL_Method18 = SPL_Method18
        self.SPL_Method20 = SPL_Method20
        self.SPL_Method22 = SPL_Method22
        self.SPL_Method24 = SPL_Method24 if SPL_Method24 is not None else set()
        self.SPL_Method26 = SPL_Method26 if SPL_Method26 is not None else set()
        self.SPL_Method28 = SPL_Method28 if SPL_Method28 is not None else set()
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def SPL_Method(self):
        return self.__SPL_Method

    @SPL_Method.setter
    def SPL_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SPL_Method__SPL_Method", None)
        self.__SPL_Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SPL_Dialog13"):
                opp_val = getattr(old_value, "SPL_Dialog13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SPL_Dialog13"):
                opp_val = getattr(value, "SPL_Dialog13", None)
                if opp_val is None:
                    setattr(value, "SPL_Dialog13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SPL_Method26(self):
        return self.__SPL_Method26

    @SPL_Method26.setter
    def SPL_Method26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SPL_Method__SPL_Method26", None)
        self.__SPL_Method26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SPL_Statement"):
                    opp_val = getattr(item, "SPL_Statement", None)
                    
                    if opp_val == self:
                        setattr(item, "SPL_Statement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SPL_Statement"):
                    opp_val = getattr(item, "SPL_Statement", None)
                    
                    setattr(item, "SPL_Statement", self)
                    

    @property
    def SPL_Method22(self):
        return self.__SPL_Method22

    @SPL_Method22.setter
    def SPL_Method22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SPL_Method__SPL_Method22", None)
        self.__SPL_Method22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SPL_MethodName"):
                opp_val = getattr(old_value, "SPL_MethodName", None)
                if opp_val == self:
                    setattr(old_value, "SPL_MethodName", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SPL_MethodName"):
                opp_val = getattr(value, "SPL_MethodName", None)
                setattr(value, "SPL_MethodName", self)

    @property
    def SPL_Method20(self):
        return self.__SPL_Method20

    @SPL_Method20.setter
    def SPL_Method20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SPL_Method__SPL_Method20", None)
        self.__SPL_Method20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SPL_TypeExpression"):
                opp_val = getattr(old_value, "SPL_TypeExpression", None)
                if opp_val == self:
                    setattr(old_value, "SPL_TypeExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SPL_TypeExpression"):
                opp_val = getattr(value, "SPL_TypeExpression", None)
                setattr(value, "SPL_TypeExpression", self)

    @property
    def SPL_Method24(self):
        return self.__SPL_Method24

    @SPL_Method24.setter
    def SPL_Method24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SPL_Method__SPL_Method24", None)
        self.__SPL_Method24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SPL_Argument"):
                    opp_val = getattr(item, "SPL_Argument", None)
                    
                    if opp_val == self:
                        setattr(item, "SPL_Argument", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SPL_Argument"):
                    opp_val = getattr(item, "SPL_Argument", None)
                    
                    setattr(item, "SPL_Argument", self)
                    

    @property
    def SPL_Method28(self):
        return self.__SPL_Method28

    @SPL_Method28.setter
    def SPL_Method28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SPL_Method__SPL_Method28", None)
        self.__SPL_Method28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SPL_Branch"):
                    opp_val = getattr(item, "SPL_Branch", None)
                    
                    if opp_val == self:
                        setattr(item, "SPL_Branch", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SPL_Branch"):
                    opp_val = getattr(item, "SPL_Branch", None)
                    
                    setattr(item, "SPL_Branch", self)
                    

    @property
    def SPL_Method18(self):
        return self.__SPL_Method18

    @SPL_Method18.setter
    def SPL_Method18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SPL_Method__SPL_Method18", None)
        self.__SPL_Method18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SPL_Event17"):
                opp_val = getattr(old_value, "SPL_Event17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SPL_Event17"):
                opp_val = getattr(value, "SPL_Event17", None)
                if opp_val is None:
                    setattr(value, "SPL_Event17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class SPL_Event(Session):

    def __init__(self, eventId: str, SPL_Event: set["SPL_Declaration"] = None, SPL_Event17: set["SPL_Method"] = None):
        self.eventId = eventId
        self.SPL_Event = SPL_Event if SPL_Event is not None else set()
        self.SPL_Event17 = SPL_Event17 if SPL_Event17 is not None else set()
        
    @property
    def eventId(self) -> str:
        return self.__eventId

    @eventId.setter
    def eventId(self, eventId: str):
        self.__eventId = eventId

    @property
    def SPL_Event(self):
        return self.__SPL_Event

    @SPL_Event.setter
    def SPL_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SPL_Event__SPL_Event", None)
        self.__SPL_Event = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SPL_Declaration15"):
                    opp_val = getattr(item, "SPL_Declaration15", None)
                    
                    if opp_val == self:
                        setattr(item, "SPL_Declaration15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SPL_Declaration15"):
                    opp_val = getattr(item, "SPL_Declaration15", None)
                    
                    setattr(item, "SPL_Declaration15", self)
                    

    @property
    def SPL_Event17(self):
        return self.__SPL_Event17

    @SPL_Event17.setter
    def SPL_Event17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SPL_Event__SPL_Event17", None)
        self.__SPL_Event17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SPL_Method18"):
                    opp_val = getattr(item, "SPL_Method18", None)
                    
                    if opp_val == self:
                        setattr(item, "SPL_Method18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SPL_Method18"):
                    opp_val = getattr(item, "SPL_Method18", None)
                    
                    setattr(item, "SPL_Method18", self)
                    

class SPL_Registration(Session):

    pass
class SPL_Session(LocatedElement):

    pass
class SPL_Declaration(LocatedElement):

    def __init__(self, name: str, SPL_Declaration: "SPL_Service" = None, SPL_Declaration6: "SPL_Registration" = None, SPL_Declaration11: "SPL_Dialog" = None, SPL_Declaration15: "SPL_Event" = None, SPL_Declaration59: "SPL_DeclarationStat" = None, SPL_Declaration128: "SPL_Variable" = None):
        self.name = name
        self.SPL_Declaration = SPL_Declaration
        self.SPL_Declaration6 = SPL_Declaration6
        self.SPL_Declaration11 = SPL_Declaration11
        self.SPL_Declaration15 = SPL_Declaration15
        self.SPL_Declaration59 = SPL_Declaration59
        self.SPL_Declaration128 = SPL_Declaration128
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def SPL_Declaration11(self):
        return self.__SPL_Declaration11

    @SPL_Declaration11.setter
    def SPL_Declaration11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SPL_Declaration__SPL_Declaration11", None)
        self.__SPL_Declaration11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SPL_Dialog"):
                opp_val = getattr(old_value, "SPL_Dialog", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SPL_Dialog"):
                opp_val = getattr(value, "SPL_Dialog", None)
                if opp_val is None:
                    setattr(value, "SPL_Dialog", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SPL_Declaration6(self):
        return self.__SPL_Declaration6

    @SPL_Declaration6.setter
    def SPL_Declaration6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SPL_Declaration__SPL_Declaration6", None)
        self.__SPL_Declaration6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SPL_Registration"):
                opp_val = getattr(old_value, "SPL_Registration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SPL_Registration"):
                opp_val = getattr(value, "SPL_Registration", None)
                if opp_val is None:
                    setattr(value, "SPL_Registration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SPL_Declaration(self):
        return self.__SPL_Declaration

    @SPL_Declaration.setter
    def SPL_Declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SPL_Declaration__SPL_Declaration", None)
        self.__SPL_Declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SPL_Service2"):
                opp_val = getattr(old_value, "SPL_Service2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SPL_Service2"):
                opp_val = getattr(value, "SPL_Service2", None)
                if opp_val is None:
                    setattr(value, "SPL_Service2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SPL_Declaration15(self):
        return self.__SPL_Declaration15

    @SPL_Declaration15.setter
    def SPL_Declaration15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SPL_Declaration__SPL_Declaration15", None)
        self.__SPL_Declaration15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SPL_Event"):
                opp_val = getattr(old_value, "SPL_Event", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SPL_Event"):
                opp_val = getattr(value, "SPL_Event", None)
                if opp_val is None:
                    setattr(value, "SPL_Event", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def SPL_Declaration59(self):
        return self.__SPL_Declaration59

    @SPL_Declaration59.setter
    def SPL_Declaration59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SPL_Declaration__SPL_Declaration59", None)
        self.__SPL_Declaration59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SPL_DeclarationStat"):
                opp_val = getattr(old_value, "SPL_DeclarationStat", None)
                if opp_val == self:
                    setattr(old_value, "SPL_DeclarationStat", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SPL_DeclarationStat"):
                opp_val = getattr(value, "SPL_DeclarationStat", None)
                setattr(value, "SPL_DeclarationStat", self)

    @property
    def SPL_Declaration128(self):
        return self.__SPL_Declaration128

    @SPL_Declaration128.setter
    def SPL_Declaration128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SPL_Declaration__SPL_Declaration128", None)
        self.__SPL_Declaration128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SPL_Variable127"):
                opp_val = getattr(old_value, "SPL_Variable127", None)
                if opp_val == self:
                    setattr(old_value, "SPL_Variable127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SPL_Variable127"):
                opp_val = getattr(value, "SPL_Variable127", None)
                setattr(value, "SPL_Variable127", self)
