from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

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
class Modifier(Enum):
    LIFO = "LIFO"
    FIFO = "FIFO"
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
class FunctionLocation(Enum):
    remote = "remote"
    local = "local"
class RedirectionErrorKind(Enum):
    ALTERNATIVE_SERVICE = "ALTERNATIVE_SERVICE"
    MOVED_PERMANENTLY = "MOVED_PERMANENTLY"
    MOVED_TEMPORARILY = "MOVED_TEMPORARILY"
    MULTIPLE_CHOICES = "MULTIPLE_CHOICES"
    USE_PROXY = "USE_PROXY"
class GlobalErrorKind(Enum):
    BUSY_EVERYWHERE = "BUSY_EVERYWHERE"
    DECLINE = "DECLINE"
    DOES_NOT_EXIST_ANYWHERE = "DOES_NOT_EXIST_ANYWHERE"
    NOT_ACCEPTABLE = "NOT_ACCEPTABLE"
class ControlMethod(Enum):
    deploy = "deploy"
    undeploy = "undeploy"
    uninvite = "uninvite"
    unregister = "unregister"
    unsubscribe = "unsubscribe"
class PrimitiveType(Enum):
    void = "void"
    bool = "bool"
    int = "int"
    request = "request"
    response = "response"
    string = "string"
    time = "time"
    uri = "uri"
class Direction(Enum):
    inout = "inout"
    in = "in"
    out = "out"
class ServerErrorKind(Enum):
    BAD_GATEWAY = "BAD_GATEWAY"
    MESSAGE_TOO_LARGE = "MESSAGE_TOO_LARGE"
    NOT_IMPLEMENTED = "NOT_IMPLEMENTED"
    SERVER_INTERNAL_ERROR = "SERVER_INTERNAL_ERROR"
    SERVER_TIMEOUT = "SERVER_TIMEOUT"
    SERVICE_UNAVAILABLE = "SERVICE_UNAVAILABLE"
    VERSION_NOT_SUPPORTED = "VERSION_NOT_SUPPORTED"
class SuccessKind(Enum):
    OK = "OK"
    ACCEPTED = "ACCEPTED"


############################################
# Definition of Classes
############################################

class TrgResponse:

    pass
class jointPackage_CPL2SPL_TrgErrorResponse(TrgResponse):

    pass
class jointPackage_CPL2SPL_TrgSuccessResponse(TrgResponse):

    def __init__(self, successKind: str, TrgResponse: "jointPackage_CPL2SPL_TrgResponseConstant"):
        self.successKind = successKind
        
    @property
    def successKind(self) -> str:
        return self.__successKind

    @successKind.setter
    def successKind(self, successKind: str):
        self.__successKind = successKind

class TrgVariablePlace:

    pass
class jointPackage_CPL2SPL_TrgVariable(TrgVariablePlace):

    pass
class jointPackage_CPL2SPL_TrgPropertyCallPlace(TrgVariablePlace):

    def __init__(self, propName: str, jointPackage_CPL2SPL_TrgPropertyCallPlace: "TrgVariablePlace" = None, TrgVariablePlace: "jointPackage_CPL2SPL_TrgPropertyCallPlace"):
        self.propName = propName
        self.jointPackage_CPL2SPL_TrgPropertyCallPlace = jointPackage_CPL2SPL_TrgPropertyCallPlace
        
    @property
    def propName(self) -> str:
        return self.__propName

    @propName.setter
    def propName(self, propName: str):
        self.__propName = propName

    @property
    def jointPackage_CPL2SPL_TrgPropertyCallPlace(self):
        return self.__jointPackage_CPL2SPL_TrgPropertyCallPlace

    @jointPackage_CPL2SPL_TrgPropertyCallPlace.setter
    def jointPackage_CPL2SPL_TrgPropertyCallPlace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_CPL2SPL_TrgPropertyCallPlace__jointPackage_CPL2SPL_TrgPropertyCallPlace", None)
        self.__jointPackage_CPL2SPL_TrgPropertyCallPlace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TrgVariablePlace"):
                opp_val = getattr(old_value, "TrgVariablePlace", None)
                if opp_val == self:
                    setattr(old_value, "TrgVariablePlace", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TrgVariablePlace"):
                opp_val = getattr(value, "TrgVariablePlace", None)
                setattr(value, "TrgVariablePlace", self)

class TrgMessageField:

    pass
class jointPackage_CPL2SPL_TrgHeadedMessageField(TrgMessageField):

    def __init__(self, headerId: str, TrgMessageField: "jointPackage_CPL2SPL_TrgWithExp"):
        self.headerId = headerId
        
    @property
    def headerId(self) -> str:
        return self.__headerId

    @headerId.setter
    def headerId(self, headerId: str):
        self.__headerId = headerId

class jointPackage_CPL2SPL_TrgReasonMessageField(TrgMessageField):

    pass
class TrgFunctionCall:

    pass
class TrgSelectMember:

    pass
class jointPackage_CPL2SPL_TrgSelectCase(TrgSelectMember):

    pass
class jointPackage_CPL2SPL_TrgSelectDefault(TrgSelectMember):

    pass
class TrgConstant:

    pass
class jointPackage_CPL2SPL_TrgBooleanConstant(TrgConstant):

    def __init__(self, value: bool, TrgConstant: "jointPackage_CPL2SPL_TrgWhenHeader", TrgConstant151: "jointPackage_CPL2SPL_TrgSequenceConstant", TrgConstant127: "jointPackage_CPL2SPL_TrgConstantExp", TrgConstant125: "jointPackage_CPL2SPL_TrgSelectCase"):
        self.value = value
        
    @property
    def value(self) -> bool:
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value

class jointPackage_CPL2SPL_TrgSequenceConstant(TrgConstant):

    pass
class jointPackage_CPL2SPL_TrgStringConstant(TrgConstant):

    def __init__(self, value: str, TrgConstant: "jointPackage_CPL2SPL_TrgWhenHeader", TrgConstant151: "jointPackage_CPL2SPL_TrgSequenceConstant", TrgConstant127: "jointPackage_CPL2SPL_TrgConstantExp", TrgConstant125: "jointPackage_CPL2SPL_TrgSelectCase"):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class jointPackage_CPL2SPL_TrgResponseConstant(TrgConstant):

    pass
class jointPackage_CPL2SPL_TrgIntegerConstant(TrgConstant):

    def __init__(self, value: int, TrgConstant: "jointPackage_CPL2SPL_TrgWhenHeader", TrgConstant151: "jointPackage_CPL2SPL_TrgSequenceConstant", TrgConstant127: "jointPackage_CPL2SPL_TrgConstantExp", TrgConstant125: "jointPackage_CPL2SPL_TrgSelectCase"):
        self.value = value
        
    @property
    def value(self) -> int:
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value

class jointPackage_CPL2SPL_TrgURIConstant(TrgConstant):

    def __init__(self, uri: str, TrgConstant: "jointPackage_CPL2SPL_TrgWhenHeader", TrgConstant151: "jointPackage_CPL2SPL_TrgSequenceConstant", TrgConstant127: "jointPackage_CPL2SPL_TrgConstantExp", TrgConstant125: "jointPackage_CPL2SPL_TrgSelectCase"):
        self.uri = uri
        
    @property
    def uri(self) -> str:
        return self.__uri

    @uri.setter
    def uri(self, uri: str):
        self.__uri = uri

class TrgWhenHeader:

    pass
class TrgVariable:

    pass
class TrgSelectDefault:

    pass
class TrgSelectCase:

    pass
class TrgNamedBranch:

    pass
class TrgPlace:

    pass
class jointPackage_CPL2SPL_TrgSIPHeaderPlace(TrgPlace):

    def __init__(self, header: str, TrgPlace117: "jointPackage_CPL2SPL_TrgPushStat", TrgPlace142: "jointPackage_CPL2SPL_TrgPopExp", TrgPlace: "jointPackage_CPL2SPL_TrgSetStat"):
        self.header = header
        
    @property
    def header(self) -> str:
        return self.__header

    @header.setter
    def header(self, header: str):
        self.__header = header

class jointPackage_CPL2SPL_TrgVariablePlace(TrgPlace):

    pass
class TrgExpression:

    pass
class jointPackage_CPL2SPL_TrgOperatorExp(TrgExpression):

    def __init__(self, opName: str, jointPackage_CPL2SPL_TrgOperatorExp131: "TrgExpression" = None, jointPackage_CPL2SPL_TrgOperatorExp: "TrgExpression" = None, TrgExpression140: "jointPackage_CPL2SPL_TrgBlockExp", TrgExpression134: "jointPackage_CPL2SPL_TrgForwardExp", TrgExpression74: "jointPackage_CPL2SPL_TrgFunctionCall", TrgExpression80: "jointPackage_CPL2SPL_TrgSetStat", TrgExpression132: "jointPackage_CPL2SPL_TrgOperatorExp", TrgExpression120: "jointPackage_CPL2SPL_TrgPushStat", TrgExpression84: "jointPackage_CPL2SPL_TrgReturnStat", TrgExpression129: "jointPackage_CPL2SPL_TrgOperatorExp", TrgExpression149: "jointPackage_CPL2SPL_TrgMessageField", TrgExpression136: "jointPackage_CPL2SPL_TrgWithExp", TrgExpression110: "jointPackage_CPL2SPL_TrgSelectStat", TrgExpression105: "jointPackage_CPL2SPL_TrgForeachStat", TrgExpression88: "jointPackage_CPL2SPL_TrgIfStat", TrgExpression: "jointPackage_CPL2SPL_TrgVariableDeclaration"):
        self.opName = opName
        self.jointPackage_CPL2SPL_TrgOperatorExp131 = jointPackage_CPL2SPL_TrgOperatorExp131
        self.jointPackage_CPL2SPL_TrgOperatorExp = jointPackage_CPL2SPL_TrgOperatorExp
        
    @property
    def opName(self) -> str:
        return self.__opName

    @opName.setter
    def opName(self, opName: str):
        self.__opName = opName

    @property
    def jointPackage_CPL2SPL_TrgOperatorExp131(self):
        return self.__jointPackage_CPL2SPL_TrgOperatorExp131

    @jointPackage_CPL2SPL_TrgOperatorExp131.setter
    def jointPackage_CPL2SPL_TrgOperatorExp131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_CPL2SPL_TrgOperatorExp__jointPackage_CPL2SPL_TrgOperatorExp131", None)
        self.__jointPackage_CPL2SPL_TrgOperatorExp131 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TrgExpression132"):
                opp_val = getattr(old_value, "TrgExpression132", None)
                if opp_val == self:
                    setattr(old_value, "TrgExpression132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TrgExpression132"):
                opp_val = getattr(value, "TrgExpression132", None)
                setattr(value, "TrgExpression132", self)

    @property
    def jointPackage_CPL2SPL_TrgOperatorExp(self):
        return self.__jointPackage_CPL2SPL_TrgOperatorExp

    @jointPackage_CPL2SPL_TrgOperatorExp.setter
    def jointPackage_CPL2SPL_TrgOperatorExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_CPL2SPL_TrgOperatorExp__jointPackage_CPL2SPL_TrgOperatorExp", None)
        self.__jointPackage_CPL2SPL_TrgOperatorExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TrgExpression129"):
                opp_val = getattr(old_value, "TrgExpression129", None)
                if opp_val == self:
                    setattr(old_value, "TrgExpression129", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TrgExpression129"):
                opp_val = getattr(value, "TrgExpression129", None)
                setattr(value, "TrgExpression129", self)

class jointPackage_CPL2SPL_TrgConstantExp(TrgExpression):

    pass
class jointPackage_CPL2SPL_TrgFunctionCallExp(TrgExpression):

    pass
class jointPackage_CPL2SPL_TrgRequestURIExp(TrgExpression):

    pass
class jointPackage_CPL2SPL_TrgWithExp(TrgExpression):

    pass
class jointPackage_CPL2SPL_TrgBlockExp(TrgExpression):

    pass
class jointPackage_CPL2SPL_TrgPopExp(TrgExpression):

    pass
class jointPackage_CPL2SPL_TrgPlace(TrgExpression):

    pass
class jointPackage_CPL2SPL_TrgForwardExp(TrgExpression):

    def __init__(self, isParallel: bool, jointPackage_CPL2SPL_TrgForwardExp: "TrgExpression" = None, TrgExpression140: "jointPackage_CPL2SPL_TrgBlockExp", TrgExpression134: "jointPackage_CPL2SPL_TrgForwardExp", TrgExpression74: "jointPackage_CPL2SPL_TrgFunctionCall", TrgExpression80: "jointPackage_CPL2SPL_TrgSetStat", TrgExpression132: "jointPackage_CPL2SPL_TrgOperatorExp", TrgExpression120: "jointPackage_CPL2SPL_TrgPushStat", TrgExpression84: "jointPackage_CPL2SPL_TrgReturnStat", TrgExpression129: "jointPackage_CPL2SPL_TrgOperatorExp", TrgExpression149: "jointPackage_CPL2SPL_TrgMessageField", TrgExpression136: "jointPackage_CPL2SPL_TrgWithExp", TrgExpression110: "jointPackage_CPL2SPL_TrgSelectStat", TrgExpression105: "jointPackage_CPL2SPL_TrgForeachStat", TrgExpression88: "jointPackage_CPL2SPL_TrgIfStat", TrgExpression: "jointPackage_CPL2SPL_TrgVariableDeclaration"):
        self.isParallel = isParallel
        self.jointPackage_CPL2SPL_TrgForwardExp = jointPackage_CPL2SPL_TrgForwardExp
        
    @property
    def isParallel(self) -> bool:
        return self.__isParallel

    @isParallel.setter
    def isParallel(self, isParallel: bool):
        self.__isParallel = isParallel

    @property
    def jointPackage_CPL2SPL_TrgForwardExp(self):
        return self.__jointPackage_CPL2SPL_TrgForwardExp

    @jointPackage_CPL2SPL_TrgForwardExp.setter
    def jointPackage_CPL2SPL_TrgForwardExp(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_CPL2SPL_TrgForwardExp__jointPackage_CPL2SPL_TrgForwardExp", None)
        self.__jointPackage_CPL2SPL_TrgForwardExp = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TrgExpression134"):
                opp_val = getattr(old_value, "TrgExpression134", None)
                if opp_val == self:
                    setattr(old_value, "TrgExpression134", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TrgExpression134"):
                opp_val = getattr(value, "TrgExpression134", None)
                setattr(value, "TrgExpression134", self)

class jointPackage_CPL2SPL_TrgBODYExp(TrgExpression):

    pass
class jointPackage_CPL2SPL_TrgReasonExp(TrgExpression):

    pass
class TrgFunctionDeclaration:

    pass
class jointPackage_CPL2SPL_TrgLocalFunctionDeclaration(TrgFunctionDeclaration):

    pass
class jointPackage_CPL2SPL_TrgRemoteFunctionDeclaration(TrgFunctionDeclaration):

    def __init__(self, functionLocation: str, TrgFunctionDeclaration: "jointPackage_CPL2SPL_TrgFunctionCall"):
        self.functionLocation = functionLocation
        
    @property
    def functionLocation(self) -> str:
        return self.__functionLocation

    @functionLocation.setter
    def functionLocation(self, functionLocation: str):
        self.__functionLocation = functionLocation

class TrgVariableDeclaration:

    pass
class jointPackage_CPL2SPL_TrgWhenHeader(TrgVariableDeclaration):

    def __init__(self, headerId: str, jointPackage_CPL2SPL_TrgWhenHeader: "TrgConstant" = None):
        self.headerId = headerId
        self.jointPackage_CPL2SPL_TrgWhenHeader = jointPackage_CPL2SPL_TrgWhenHeader
        
    @property
    def headerId(self) -> str:
        return self.__headerId

    @headerId.setter
    def headerId(self, headerId: str):
        self.__headerId = headerId

    @property
    def jointPackage_CPL2SPL_TrgWhenHeader(self):
        return self.__jointPackage_CPL2SPL_TrgWhenHeader

    @jointPackage_CPL2SPL_TrgWhenHeader.setter
    def jointPackage_CPL2SPL_TrgWhenHeader(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_CPL2SPL_TrgWhenHeader__jointPackage_CPL2SPL_TrgWhenHeader", None)
        self.__jointPackage_CPL2SPL_TrgWhenHeader = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TrgConstant"):
                opp_val = getattr(old_value, "TrgConstant", None)
                if opp_val == self:
                    setattr(old_value, "TrgConstant", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TrgConstant"):
                opp_val = getattr(value, "TrgConstant", None)
                setattr(value, "TrgConstant", self)

class jointPackage_CPL2SPL_TrgArgument(TrgVariableDeclaration):

    pass
class TrgBranch:

    pass
class TrgStatement:

    pass
class jointPackage_CPL2SPL_TrgContinueStat(TrgStatement):

    pass
class jointPackage_CPL2SPL_TrgDeclarationStat(TrgStatement):

    pass
class jointPackage_CPL2SPL_TrgSelectStat(TrgStatement):

    pass
class jointPackage_CPL2SPL_TrgForeachStat(TrgStatement):

    def __init__(self, iteratorName: str, jointPackage_CPL2SPL_TrgForeachStat: "TrgExpression" = None, jointPackage_CPL2SPL_TrgForeachStat107: set["TrgStatement"] = None, TrgStatement123: "jointPackage_CPL2SPL_TrgSelectMember", TrgStatement68: "jointPackage_CPL2SPL_TrgLocalFunctionDeclaration", TrgStatement91: "jointPackage_CPL2SPL_TrgIfStat", TrgStatement76: "jointPackage_CPL2SPL_TrgCompoundStat", TrgStatement100: "jointPackage_CPL2SPL_TrgWhenStat", TrgStatement57: "jointPackage_CPL2SPL_TrgBranch", TrgStatement94: "jointPackage_CPL2SPL_TrgIfStat", TrgStatement108: "jointPackage_CPL2SPL_TrgForeachStat", TrgStatement103: "jointPackage_CPL2SPL_TrgWhenStat", TrgStatement: "jointPackage_CPL2SPL_TrgMethod"):
        self.iteratorName = iteratorName
        self.jointPackage_CPL2SPL_TrgForeachStat = jointPackage_CPL2SPL_TrgForeachStat
        self.jointPackage_CPL2SPL_TrgForeachStat107 = jointPackage_CPL2SPL_TrgForeachStat107 if jointPackage_CPL2SPL_TrgForeachStat107 is not None else set()
        
    @property
    def iteratorName(self) -> str:
        return self.__iteratorName

    @iteratorName.setter
    def iteratorName(self, iteratorName: str):
        self.__iteratorName = iteratorName

    @property
    def jointPackage_CPL2SPL_TrgForeachStat(self):
        return self.__jointPackage_CPL2SPL_TrgForeachStat

    @jointPackage_CPL2SPL_TrgForeachStat.setter
    def jointPackage_CPL2SPL_TrgForeachStat(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_CPL2SPL_TrgForeachStat__jointPackage_CPL2SPL_TrgForeachStat", None)
        self.__jointPackage_CPL2SPL_TrgForeachStat = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TrgExpression105"):
                opp_val = getattr(old_value, "TrgExpression105", None)
                if opp_val == self:
                    setattr(old_value, "TrgExpression105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TrgExpression105"):
                opp_val = getattr(value, "TrgExpression105", None)
                setattr(value, "TrgExpression105", self)

    @property
    def jointPackage_CPL2SPL_TrgForeachStat107(self):
        return self.__jointPackage_CPL2SPL_TrgForeachStat107

    @jointPackage_CPL2SPL_TrgForeachStat107.setter
    def jointPackage_CPL2SPL_TrgForeachStat107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_CPL2SPL_TrgForeachStat__jointPackage_CPL2SPL_TrgForeachStat107", None)
        self.__jointPackage_CPL2SPL_TrgForeachStat107 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TrgStatement108"):
                    opp_val = getattr(item, "TrgStatement108", None)
                    
                    if opp_val == self:
                        setattr(item, "TrgStatement108", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TrgStatement108"):
                    opp_val = getattr(item, "TrgStatement108", None)
                    
                    setattr(item, "TrgStatement108", self)
                    

class jointPackage_CPL2SPL_TrgWhenStat(TrgStatement):

    pass
class jointPackage_CPL2SPL_TrgSetStat(TrgStatement):

    pass
class jointPackage_CPL2SPL_TrgIfStat(TrgStatement):

    pass
class jointPackage_CPL2SPL_TrgFunctionCallStat(TrgStatement):

    pass
class jointPackage_CPL2SPL_TrgCompoundStat(TrgStatement):

    pass
class jointPackage_CPL2SPL_TrgReturnStat(TrgStatement):

    pass
class jointPackage_CPL2SPL_TrgPushStat(TrgStatement):

    pass
class jointPackage_CPL2SPL_TrgBreakStat(TrgStatement):

    pass
class TrgArgument:

    pass
class TrgMethodName:

    pass
class jointPackage_CPL2SPL_TrgNamedBranch(TrgBranch):

    def __init__(self, name: str, TrgBranch: "jointPackage_CPL2SPL_TrgMethod"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class jointPackage_CPL2SPL_TrgDefaultBranch(TrgBranch):

    pass
class jointPackage_CPL2SPL_TrgControlMethodName(TrgMethodName):

    def __init__(self, name: str, TrgMethodName: "jointPackage_CPL2SPL_TrgMethod"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class jointPackage_CPL2SPL_TrgSIPMethodName(TrgMethodName):

    def __init__(self, name: str, TrgMethodName: "jointPackage_CPL2SPL_TrgMethod"):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class TrgSession:

    pass
class TrgDeclaration:

    pass
class jointPackage_CPL2SPL_TrgFunctionDeclaration(TrgDeclaration):

    pass
class jointPackage_CPL2SPL_TrgVariableDeclaration(TrgDeclaration):

    pass
class jointPackage_CPL2SPL_TrgStructureDeclaration(TrgDeclaration):

    pass
class jointPackage_CPL2SPL_TrgLocatedElement(ABC):

    def __init__(self, location: str, commentsBefore: str, commentsAfter: str):
        self.location = location
        self.commentsBefore = commentsBefore
        self.commentsAfter = commentsAfter
        
    @property
    def commentsAfter(self) -> str:
        return self.__commentsAfter

    @commentsAfter.setter
    def commentsAfter(self, commentsAfter: str):
        self.__commentsAfter = commentsAfter

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

class jointPackage_CPL2SPL_TrgMethod(TrgSession):

    def __init__(self, direction: str, jointPackage_CPL2SPL_TrgMethod: "TrgTypeExpression" = None, jointPackage_CPL2SPL_TrgMethod49: "TrgMethodName" = None, jointPackage_CPL2SPL_TrgMethod51: set["TrgArgument"] = None, jointPackage_CPL2SPL_TrgMethod53: set["TrgStatement"] = None, jointPackage_CPL2SPL_TrgMethod55: set["TrgBranch"] = None, TrgSession: "jointPackage_CPL2SPL_TrgService", TrgSession36: "jointPackage_CPL2SPL_TrgRegistration"):
        self.direction = direction
        self.jointPackage_CPL2SPL_TrgMethod = jointPackage_CPL2SPL_TrgMethod
        self.jointPackage_CPL2SPL_TrgMethod49 = jointPackage_CPL2SPL_TrgMethod49
        self.jointPackage_CPL2SPL_TrgMethod51 = jointPackage_CPL2SPL_TrgMethod51 if jointPackage_CPL2SPL_TrgMethod51 is not None else set()
        self.jointPackage_CPL2SPL_TrgMethod53 = jointPackage_CPL2SPL_TrgMethod53 if jointPackage_CPL2SPL_TrgMethod53 is not None else set()
        self.jointPackage_CPL2SPL_TrgMethod55 = jointPackage_CPL2SPL_TrgMethod55 if jointPackage_CPL2SPL_TrgMethod55 is not None else set()
        
    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, direction: str):
        self.__direction = direction

    @property
    def jointPackage_CPL2SPL_TrgMethod(self):
        return self.__jointPackage_CPL2SPL_TrgMethod

    @jointPackage_CPL2SPL_TrgMethod.setter
    def jointPackage_CPL2SPL_TrgMethod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_CPL2SPL_TrgMethod__jointPackage_CPL2SPL_TrgMethod", None)
        self.__jointPackage_CPL2SPL_TrgMethod = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TrgTypeExpression47"):
                opp_val = getattr(old_value, "TrgTypeExpression47", None)
                if opp_val == self:
                    setattr(old_value, "TrgTypeExpression47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TrgTypeExpression47"):
                opp_val = getattr(value, "TrgTypeExpression47", None)
                setattr(value, "TrgTypeExpression47", self)

    @property
    def jointPackage_CPL2SPL_TrgMethod55(self):
        return self.__jointPackage_CPL2SPL_TrgMethod55

    @jointPackage_CPL2SPL_TrgMethod55.setter
    def jointPackage_CPL2SPL_TrgMethod55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_CPL2SPL_TrgMethod__jointPackage_CPL2SPL_TrgMethod55", None)
        self.__jointPackage_CPL2SPL_TrgMethod55 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TrgBranch"):
                    opp_val = getattr(item, "TrgBranch", None)
                    
                    if opp_val == self:
                        setattr(item, "TrgBranch", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TrgBranch"):
                    opp_val = getattr(item, "TrgBranch", None)
                    
                    setattr(item, "TrgBranch", self)
                    

    @property
    def jointPackage_CPL2SPL_TrgMethod53(self):
        return self.__jointPackage_CPL2SPL_TrgMethod53

    @jointPackage_CPL2SPL_TrgMethod53.setter
    def jointPackage_CPL2SPL_TrgMethod53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_CPL2SPL_TrgMethod__jointPackage_CPL2SPL_TrgMethod53", None)
        self.__jointPackage_CPL2SPL_TrgMethod53 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TrgStatement"):
                    opp_val = getattr(item, "TrgStatement", None)
                    
                    if opp_val == self:
                        setattr(item, "TrgStatement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TrgStatement"):
                    opp_val = getattr(item, "TrgStatement", None)
                    
                    setattr(item, "TrgStatement", self)
                    

    @property
    def jointPackage_CPL2SPL_TrgMethod49(self):
        return self.__jointPackage_CPL2SPL_TrgMethod49

    @jointPackage_CPL2SPL_TrgMethod49.setter
    def jointPackage_CPL2SPL_TrgMethod49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_CPL2SPL_TrgMethod__jointPackage_CPL2SPL_TrgMethod49", None)
        self.__jointPackage_CPL2SPL_TrgMethod49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TrgMethodName"):
                opp_val = getattr(old_value, "TrgMethodName", None)
                if opp_val == self:
                    setattr(old_value, "TrgMethodName", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TrgMethodName"):
                opp_val = getattr(value, "TrgMethodName", None)
                setattr(value, "TrgMethodName", self)

    @property
    def jointPackage_CPL2SPL_TrgMethod51(self):
        return self.__jointPackage_CPL2SPL_TrgMethod51

    @jointPackage_CPL2SPL_TrgMethod51.setter
    def jointPackage_CPL2SPL_TrgMethod51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_CPL2SPL_TrgMethod__jointPackage_CPL2SPL_TrgMethod51", None)
        self.__jointPackage_CPL2SPL_TrgMethod51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TrgArgument"):
                    opp_val = getattr(item, "TrgArgument", None)
                    
                    if opp_val == self:
                        setattr(item, "TrgArgument", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TrgArgument"):
                    opp_val = getattr(item, "TrgArgument", None)
                    
                    setattr(item, "TrgArgument", self)
                    

class jointPackage_CPL2SPL_TrgEvent(TrgSession):

    def __init__(self, eventId: str, jointPackage_CPL2SPL_TrgEvent: set["TrgDeclaration"] = None, jointPackage_CPL2SPL_TrgEvent44: set["TrgMethod"] = None, TrgSession: "jointPackage_CPL2SPL_TrgService", TrgSession36: "jointPackage_CPL2SPL_TrgRegistration"):
        self.eventId = eventId
        self.jointPackage_CPL2SPL_TrgEvent = jointPackage_CPL2SPL_TrgEvent if jointPackage_CPL2SPL_TrgEvent is not None else set()
        self.jointPackage_CPL2SPL_TrgEvent44 = jointPackage_CPL2SPL_TrgEvent44 if jointPackage_CPL2SPL_TrgEvent44 is not None else set()
        
    @property
    def eventId(self) -> str:
        return self.__eventId

    @eventId.setter
    def eventId(self, eventId: str):
        self.__eventId = eventId

    @property
    def jointPackage_CPL2SPL_TrgEvent44(self):
        return self.__jointPackage_CPL2SPL_TrgEvent44

    @jointPackage_CPL2SPL_TrgEvent44.setter
    def jointPackage_CPL2SPL_TrgEvent44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_CPL2SPL_TrgEvent__jointPackage_CPL2SPL_TrgEvent44", None)
        self.__jointPackage_CPL2SPL_TrgEvent44 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TrgMethod45"):
                    opp_val = getattr(item, "TrgMethod45", None)
                    
                    if opp_val == self:
                        setattr(item, "TrgMethod45", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TrgMethod45"):
                    opp_val = getattr(item, "TrgMethod45", None)
                    
                    setattr(item, "TrgMethod45", self)
                    

    @property
    def jointPackage_CPL2SPL_TrgEvent(self):
        return self.__jointPackage_CPL2SPL_TrgEvent

    @jointPackage_CPL2SPL_TrgEvent.setter
    def jointPackage_CPL2SPL_TrgEvent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_CPL2SPL_TrgEvent__jointPackage_CPL2SPL_TrgEvent", None)
        self.__jointPackage_CPL2SPL_TrgEvent = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TrgDeclaration42"):
                    opp_val = getattr(item, "TrgDeclaration42", None)
                    
                    if opp_val == self:
                        setattr(item, "TrgDeclaration42", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TrgDeclaration42"):
                    opp_val = getattr(item, "TrgDeclaration42", None)
                    
                    setattr(item, "TrgDeclaration42", self)
                    

class TrgMethod:

    pass
class jointPackage_CPL2SPL_TrgDialog(TrgSession):

    pass
class jointPackage_CPL2SPL_TrgRegistration(TrgSession):

    pass
class SrcOtherwise:

    pass
class SrcNotPresent:

    pass
class TrgErrorResponse:

    pass
class jointPackage_CPL2SPL_TrgServerErrorResponse(TrgErrorResponse):

    def __init__(self, errorKind: str):
        self.errorKind = errorKind
        
    @property
    def errorKind(self) -> str:
        return self.__errorKind

    @errorKind.setter
    def errorKind(self, errorKind: str):
        self.__errorKind = errorKind

class jointPackage_CPL2SPL_TrgRedirectionErrorResponse(TrgErrorResponse):

    def __init__(self, errorKind: str):
        self.errorKind = errorKind
        
    @property
    def errorKind(self) -> str:
        return self.__errorKind

    @errorKind.setter
    def errorKind(self, errorKind: str):
        self.__errorKind = errorKind

class jointPackage_CPL2SPL_TrgGlobalErrorResponse(TrgErrorResponse):

    def __init__(self, errorKind: str):
        self.errorKind = errorKind
        
    @property
    def errorKind(self) -> str:
        return self.__errorKind

    @errorKind.setter
    def errorKind(self, errorKind: str):
        self.__errorKind = errorKind

class jointPackage_CPL2SPL_TrgClientErrorResponse(TrgErrorResponse):

    def __init__(self, errorKind: str):
        self.errorKind = errorKind
        
    @property
    def errorKind(self) -> str:
        return self.__errorKind

    @errorKind.setter
    def errorKind(self, errorKind: str):
        self.__errorKind = errorKind

class TrgTypeExpression:

    pass
class jointPackage_CPL2SPL_TrgDefinedType(TrgTypeExpression):

    def __init__(self, typeName: str, TrgTypeExpression: "jointPackage_CPL2SPL_TrgStructureProperty", TrgTypeExpression47: "jointPackage_CPL2SPL_TrgMethod", TrgTypeExpression59: "jointPackage_CPL2SPL_TrgVariableDeclaration", TrgTypeExpression63: "jointPackage_CPL2SPL_TrgFunctionDeclaration"):
        self.typeName = typeName
        
    @property
    def typeName(self) -> str:
        return self.__typeName

    @typeName.setter
    def typeName(self, typeName: str):
        self.__typeName = typeName

class jointPackage_CPL2SPL_TrgSimpleType(TrgTypeExpression):

    def __init__(self, type: str, TrgTypeExpression: "jointPackage_CPL2SPL_TrgStructureProperty", TrgTypeExpression47: "jointPackage_CPL2SPL_TrgMethod", TrgTypeExpression59: "jointPackage_CPL2SPL_TrgVariableDeclaration", TrgTypeExpression63: "jointPackage_CPL2SPL_TrgFunctionDeclaration"):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class jointPackage_CPL2SPL_TrgSequenceType(TrgTypeExpression):

    def __init__(self, modifier: str, type: str, size: int, TrgTypeExpression: "jointPackage_CPL2SPL_TrgStructureProperty", TrgTypeExpression47: "jointPackage_CPL2SPL_TrgMethod", TrgTypeExpression59: "jointPackage_CPL2SPL_TrgVariableDeclaration", TrgTypeExpression63: "jointPackage_CPL2SPL_TrgFunctionDeclaration"):
        self.modifier = modifier
        self.type = type
        self.size = size
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def modifier(self) -> str:
        return self.__modifier

    @modifier.setter
    def modifier(self, modifier: str):
        self.__modifier = modifier

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

class TrgService:

    pass
class TrgLocatedElement:

    pass
class jointPackage_CPL2SPL_TrgStatement(TrgLocatedElement):

    pass
class jointPackage_CPL2SPL_TrgDeclaration(TrgLocatedElement):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class jointPackage_CPL2SPL_TrgTypeExpression(TrgLocatedElement):

    pass
class jointPackage_CPL2SPL_TrgBranch(TrgLocatedElement):

    pass
class jointPackage_CPL2SPL_TrgService(TrgLocatedElement):

    def __init__(self, name: str, jointPackage_CPL2SPL_TrgService31: set["TrgSession"] = None, jointPackage_CPL2SPL_TrgService: set["TrgDeclaration"] = None):
        self.name = name
        self.jointPackage_CPL2SPL_TrgService31 = jointPackage_CPL2SPL_TrgService31 if jointPackage_CPL2SPL_TrgService31 is not None else set()
        self.jointPackage_CPL2SPL_TrgService = jointPackage_CPL2SPL_TrgService if jointPackage_CPL2SPL_TrgService is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def jointPackage_CPL2SPL_TrgService(self):
        return self.__jointPackage_CPL2SPL_TrgService

    @jointPackage_CPL2SPL_TrgService.setter
    def jointPackage_CPL2SPL_TrgService(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_CPL2SPL_TrgService__jointPackage_CPL2SPL_TrgService", None)
        self.__jointPackage_CPL2SPL_TrgService = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TrgDeclaration"):
                    opp_val = getattr(item, "TrgDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "TrgDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TrgDeclaration"):
                    opp_val = getattr(item, "TrgDeclaration", None)
                    
                    setattr(item, "TrgDeclaration", self)
                    

    @property
    def jointPackage_CPL2SPL_TrgService31(self):
        return self.__jointPackage_CPL2SPL_TrgService31

    @jointPackage_CPL2SPL_TrgService31.setter
    def jointPackage_CPL2SPL_TrgService31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_CPL2SPL_TrgService__jointPackage_CPL2SPL_TrgService31", None)
        self.__jointPackage_CPL2SPL_TrgService31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TrgSession"):
                    opp_val = getattr(item, "TrgSession", None)
                    
                    if opp_val == self:
                        setattr(item, "TrgSession", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TrgSession"):
                    opp_val = getattr(item, "TrgSession", None)
                    
                    setattr(item, "TrgSession", self)
                    

class jointPackage_CPL2SPL_TrgExpression(TrgLocatedElement):

    pass
class jointPackage_CPL2SPL_TrgSelectMember(TrgLocatedElement):

    pass
class jointPackage_CPL2SPL_TrgConstant(TrgLocatedElement):

    pass
class jointPackage_CPL2SPL_TrgStructureProperty(TrgLocatedElement):

    def __init__(self, name: str, jointPackage_CPL2SPL_TrgStructureProperty: "TrgTypeExpression" = None):
        self.name = name
        self.jointPackage_CPL2SPL_TrgStructureProperty = jointPackage_CPL2SPL_TrgStructureProperty
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def jointPackage_CPL2SPL_TrgStructureProperty(self):
        return self.__jointPackage_CPL2SPL_TrgStructureProperty

    @jointPackage_CPL2SPL_TrgStructureProperty.setter
    def jointPackage_CPL2SPL_TrgStructureProperty(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_CPL2SPL_TrgStructureProperty__jointPackage_CPL2SPL_TrgStructureProperty", None)
        self.__jointPackage_CPL2SPL_TrgStructureProperty = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TrgTypeExpression"):
                opp_val = getattr(old_value, "TrgTypeExpression", None)
                if opp_val == self:
                    setattr(old_value, "TrgTypeExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TrgTypeExpression"):
                opp_val = getattr(value, "TrgTypeExpression", None)
                setattr(value, "TrgTypeExpression", self)

class jointPackage_CPL2SPL_TrgMethodName(TrgLocatedElement):

    pass
class jointPackage_CPL2SPL_TrgSession(TrgLocatedElement):

    pass
class jointPackage_CPL2SPL_TrgResponse(TrgLocatedElement):

    pass
class jointPackage_CPL2SPL_TrgMessageField(TrgLocatedElement):

    pass
class jointPackage_CPL2SPL_TrgFunctionCall(TrgLocatedElement):

    pass
class jointPackage_CPL2SPL_TrgProgram(TrgLocatedElement):

    pass
class SrcAction:

    pass
class jointPackage_CPL2SPL_SrcSignallingAction(SrcAction):

    pass
class SrcFailure:

    pass
class SrcRedirection:

    pass
class SrcNoAnswer:

    pass
class SrcBusy:

    pass
class SrcSignallingAction:

    pass
class jointPackage_CPL2SPL_SrcProxy(SrcSignallingAction):

    def __init__(self, timeout: str, recurse: str, ordering: str, jointPackage_CPL2SPL_SrcProxy22: "SrcDefault" = None, jointPackage_CPL2SPL_SrcProxy: "SrcBusy" = None, jointPackage_CPL2SPL_SrcProxy16: "SrcNoAnswer" = None, jointPackage_CPL2SPL_SrcProxy18: "SrcRedirection" = None, jointPackage_CPL2SPL_SrcProxy20: "SrcFailure" = None):
        self.timeout = timeout
        self.recurse = recurse
        self.ordering = ordering
        self.jointPackage_CPL2SPL_SrcProxy22 = jointPackage_CPL2SPL_SrcProxy22
        self.jointPackage_CPL2SPL_SrcProxy = jointPackage_CPL2SPL_SrcProxy
        self.jointPackage_CPL2SPL_SrcProxy16 = jointPackage_CPL2SPL_SrcProxy16
        self.jointPackage_CPL2SPL_SrcProxy18 = jointPackage_CPL2SPL_SrcProxy18
        self.jointPackage_CPL2SPL_SrcProxy20 = jointPackage_CPL2SPL_SrcProxy20
        
    @property
    def timeout(self) -> str:
        return self.__timeout

    @timeout.setter
    def timeout(self, timeout: str):
        self.__timeout = timeout

    @property
    def recurse(self) -> str:
        return self.__recurse

    @recurse.setter
    def recurse(self, recurse: str):
        self.__recurse = recurse

    @property
    def ordering(self) -> str:
        return self.__ordering

    @ordering.setter
    def ordering(self, ordering: str):
        self.__ordering = ordering

    @property
    def jointPackage_CPL2SPL_SrcProxy18(self):
        return self.__jointPackage_CPL2SPL_SrcProxy18

    @jointPackage_CPL2SPL_SrcProxy18.setter
    def jointPackage_CPL2SPL_SrcProxy18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_CPL2SPL_SrcProxy__jointPackage_CPL2SPL_SrcProxy18", None)
        self.__jointPackage_CPL2SPL_SrcProxy18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SrcRedirection"):
                opp_val = getattr(old_value, "SrcRedirection", None)
                if opp_val == self:
                    setattr(old_value, "SrcRedirection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SrcRedirection"):
                opp_val = getattr(value, "SrcRedirection", None)
                setattr(value, "SrcRedirection", self)

    @property
    def jointPackage_CPL2SPL_SrcProxy(self):
        return self.__jointPackage_CPL2SPL_SrcProxy

    @jointPackage_CPL2SPL_SrcProxy.setter
    def jointPackage_CPL2SPL_SrcProxy(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_CPL2SPL_SrcProxy__jointPackage_CPL2SPL_SrcProxy", None)
        self.__jointPackage_CPL2SPL_SrcProxy = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SrcBusy"):
                opp_val = getattr(old_value, "SrcBusy", None)
                if opp_val == self:
                    setattr(old_value, "SrcBusy", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SrcBusy"):
                opp_val = getattr(value, "SrcBusy", None)
                setattr(value, "SrcBusy", self)

    @property
    def jointPackage_CPL2SPL_SrcProxy16(self):
        return self.__jointPackage_CPL2SPL_SrcProxy16

    @jointPackage_CPL2SPL_SrcProxy16.setter
    def jointPackage_CPL2SPL_SrcProxy16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_CPL2SPL_SrcProxy__jointPackage_CPL2SPL_SrcProxy16", None)
        self.__jointPackage_CPL2SPL_SrcProxy16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SrcNoAnswer"):
                opp_val = getattr(old_value, "SrcNoAnswer", None)
                if opp_val == self:
                    setattr(old_value, "SrcNoAnswer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SrcNoAnswer"):
                opp_val = getattr(value, "SrcNoAnswer", None)
                setattr(value, "SrcNoAnswer", self)

    @property
    def jointPackage_CPL2SPL_SrcProxy22(self):
        return self.__jointPackage_CPL2SPL_SrcProxy22

    @jointPackage_CPL2SPL_SrcProxy22.setter
    def jointPackage_CPL2SPL_SrcProxy22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_CPL2SPL_SrcProxy__jointPackage_CPL2SPL_SrcProxy22", None)
        self.__jointPackage_CPL2SPL_SrcProxy22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SrcDefault"):
                opp_val = getattr(old_value, "SrcDefault", None)
                if opp_val == self:
                    setattr(old_value, "SrcDefault", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SrcDefault"):
                opp_val = getattr(value, "SrcDefault", None)
                setattr(value, "SrcDefault", self)

    @property
    def jointPackage_CPL2SPL_SrcProxy20(self):
        return self.__jointPackage_CPL2SPL_SrcProxy20

    @jointPackage_CPL2SPL_SrcProxy20.setter
    def jointPackage_CPL2SPL_SrcProxy20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_CPL2SPL_SrcProxy__jointPackage_CPL2SPL_SrcProxy20", None)
        self.__jointPackage_CPL2SPL_SrcProxy20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SrcFailure"):
                opp_val = getattr(old_value, "SrcFailure", None)
                if opp_val == self:
                    setattr(old_value, "SrcFailure", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SrcFailure"):
                opp_val = getattr(value, "SrcFailure", None)
                setattr(value, "SrcFailure", self)

class SrcNodeContainer:

    pass
class jointPackage_CPL2SPL_SrcBusy(SrcNodeContainer):

    pass
class jointPackage_CPL2SPL_SrcSwitchedAddress(SrcNodeContainer):

    def __init__(self, is: str, contains: str, subDomainOf: str):
        self.is = is
        self.contains = contains
        self.subDomainOf = subDomainOf
        
    @property
    def subDomainOf(self) -> str:
        return self.__subDomainOf

    @subDomainOf.setter
    def subDomainOf(self, subDomainOf: str):
        self.__subDomainOf = subDomainOf

    @property
    def contains(self) -> str:
        return self.__contains

    @contains.setter
    def contains(self, contains: str):
        self.__contains = contains

    @property
    def is(self) -> str:
        return self.__is

    @is.setter
    def is(self, is: str):
        self.__is = is

class jointPackage_CPL2SPL_SrcFailure(SrcNodeContainer):

    pass
class jointPackage_CPL2SPL_SrcRedirection(SrcNodeContainer):

    pass
class jointPackage_CPL2SPL_SrcDefault(SrcNodeContainer):

    pass
class jointPackage_CPL2SPL_SrcSwitchedLanguage(SrcNodeContainer):

    def __init__(self, matches: str):
        self.matches = matches
        
    @property
    def matches(self) -> str:
        return self.__matches

    @matches.setter
    def matches(self, matches: str):
        self.__matches = matches

class jointPackage_CPL2SPL_SrcNoAnswer(SrcNodeContainer):

    pass
class jointPackage_CPL2SPL_SrcOtherwise(SrcNodeContainer):

    pass
class jointPackage_CPL2SPL_SrcSwitchedPriority(SrcNodeContainer):

    def __init__(self, less: str, greater: str, equal: str):
        self.less = less
        self.greater = greater
        self.equal = equal
        
    @property
    def equal(self) -> str:
        return self.__equal

    @equal.setter
    def equal(self, equal: str):
        self.__equal = equal

    @property
    def greater(self) -> str:
        return self.__greater

    @greater.setter
    def greater(self, greater: str):
        self.__greater = greater

    @property
    def less(self) -> str:
        return self.__less

    @less.setter
    def less(self, less: str):
        self.__less = less

class jointPackage_CPL2SPL_SrcOutgoing(SrcNodeContainer):

    pass
class jointPackage_CPL2SPL_SrcSwitchedString(SrcNodeContainer):

    def __init__(self, is: str, contains: str):
        self.is = is
        self.contains = contains
        
    @property
    def is(self) -> str:
        return self.__is

    @is.setter
    def is(self, is: str):
        self.__is = is

    @property
    def contains(self) -> str:
        return self.__contains

    @contains.setter
    def contains(self, contains: str):
        self.__contains = contains

class jointPackage_CPL2SPL_SrcSwitchedTime(SrcNodeContainer):

    def __init__(self, duration: str, freq: str, until: str, count: str, interval: str, bySecond: str, byMinute: str, byHour: str, byDay: str, byMonthDay: str, byYearDay: str, byWeekNo: str, byMonth: str, wkst: str, bySetPos: str, dtstart: str, dtend: str):
        self.duration = duration
        self.freq = freq
        self.until = until
        self.count = count
        self.interval = interval
        self.bySecond = bySecond
        self.byMinute = byMinute
        self.byHour = byHour
        self.byDay = byDay
        self.byMonthDay = byMonthDay
        self.byYearDay = byYearDay
        self.byWeekNo = byWeekNo
        self.byMonth = byMonth
        self.wkst = wkst
        self.bySetPos = bySetPos
        self.dtstart = dtstart
        self.dtend = dtend
        
    @property
    def dtstart(self) -> str:
        return self.__dtstart

    @dtstart.setter
    def dtstart(self, dtstart: str):
        self.__dtstart = dtstart

    @property
    def byYearDay(self) -> str:
        return self.__byYearDay

    @byYearDay.setter
    def byYearDay(self, byYearDay: str):
        self.__byYearDay = byYearDay

    @property
    def byMonth(self) -> str:
        return self.__byMonth

    @byMonth.setter
    def byMonth(self, byMonth: str):
        self.__byMonth = byMonth

    @property
    def freq(self) -> str:
        return self.__freq

    @freq.setter
    def freq(self, freq: str):
        self.__freq = freq

    @property
    def dtend(self) -> str:
        return self.__dtend

    @dtend.setter
    def dtend(self, dtend: str):
        self.__dtend = dtend

    @property
    def byWeekNo(self) -> str:
        return self.__byWeekNo

    @byWeekNo.setter
    def byWeekNo(self, byWeekNo: str):
        self.__byWeekNo = byWeekNo

    @property
    def byMinute(self) -> str:
        return self.__byMinute

    @byMinute.setter
    def byMinute(self, byMinute: str):
        self.__byMinute = byMinute

    @property
    def byDay(self) -> str:
        return self.__byDay

    @byDay.setter
    def byDay(self, byDay: str):
        self.__byDay = byDay

    @property
    def count(self) -> str:
        return self.__count

    @count.setter
    def count(self, count: str):
        self.__count = count

    @property
    def byMonthDay(self) -> str:
        return self.__byMonthDay

    @byMonthDay.setter
    def byMonthDay(self, byMonthDay: str):
        self.__byMonthDay = byMonthDay

    @property
    def byHour(self) -> str:
        return self.__byHour

    @byHour.setter
    def byHour(self, byHour: str):
        self.__byHour = byHour

    @property
    def bySetPos(self) -> str:
        return self.__bySetPos

    @bySetPos.setter
    def bySetPos(self, bySetPos: str):
        self.__bySetPos = bySetPos

    @property
    def until(self) -> str:
        return self.__until

    @until.setter
    def until(self, until: str):
        self.__until = until

    @property
    def wkst(self) -> str:
        return self.__wkst

    @wkst.setter
    def wkst(self, wkst: str):
        self.__wkst = wkst

    @property
    def interval(self) -> str:
        return self.__interval

    @interval.setter
    def interval(self, interval: str):
        self.__interval = interval

    @property
    def bySecond(self) -> str:
        return self.__bySecond

    @bySecond.setter
    def bySecond(self, bySecond: str):
        self.__bySecond = bySecond

    @property
    def duration(self) -> str:
        return self.__duration

    @duration.setter
    def duration(self, duration: str):
        self.__duration = duration

class jointPackage_CPL2SPL_SrcNotPresent(SrcNodeContainer):

    pass
class jointPackage_CPL2SPL_SrcIncoming(SrcNodeContainer):

    pass
class jointPackage_CPL2SPL_SrcSubAction(SrcNodeContainer):

    def __init__(self, id: str):
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class SrcNode:

    pass
class jointPackage_CPL2SPL_SrcAction(SrcNode):

    pass
class jointPackage_CPL2SPL_SrcSwitch(SrcNode):

    pass
class jointPackage_CPL2SPL_SrcLocation(SrcNodeContainer, SrcNode):

    def __init__(self, url: str, priority: str, clear: str, SrcNode: "jointPackage_CPL2SPL_SrcNodeContainer"):
        self.url = url
        self.priority = priority
        self.clear = clear
        
    @property
    def clear(self) -> str:
        return self.__clear

    @clear.setter
    def clear(self, clear: str):
        self.__clear = clear

    @property
    def priority(self) -> str:
        return self.__priority

    @priority.setter
    def priority(self, priority: str):
        self.__priority = priority

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url = url

class jointPackage_CPL2SPL_SrcSubCall(SrcNode):

    def __init__(self, ref: str, SrcNode: "jointPackage_CPL2SPL_SrcNodeContainer"):
        self.ref = ref
        
    @property
    def ref(self) -> str:
        return self.__ref

    @ref.setter
    def ref(self, ref: str):
        self.__ref = ref

class jointPackage_CPL2SPL_SrcElement(ABC):

    pass
class jointPackage_CPL2SPL_SrcReject(SrcSignallingAction):

    def __init__(self, status: str, reason: str):
        self.status = status
        self.reason = reason
        
    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def reason(self) -> str:
        return self.__reason

    @reason.setter
    def reason(self, reason: str):
        self.__reason = reason

class jointPackage_CPL2SPL_SrcRedirect(SrcSignallingAction):

    def __init__(self, permanent: str):
        self.permanent = permanent
        
    @property
    def permanent(self) -> str:
        return self.__permanent

    @permanent.setter
    def permanent(self, permanent: str):
        self.__permanent = permanent

class SrcDefault:

    pass
class SrcIncoming:

    pass
class SrcOutgoing:

    pass
class SrcSubAction:

    pass
class SrcElement:

    pass
class jointPackage_CPL2SPL_SrcNodeContainer(SrcElement):

    pass
class jointPackage_CPL2SPL_SrcNode(SrcElement):

    pass
class jointPackage_CPL2SPL_SrcCPL(SrcElement):

    pass
class jointPackage_CPL2SPL_SrcCPLModel:

    pass
class TrgServerErrorResponse:

    pass
class SrcSwitchedPriority:

    pass
class SrcSwitchedTime:

    pass
class SrcSwitchedLanguage:

    pass
class SrcSwitchedString:

    pass
class SrcSwitchedAddress:

    pass
class SrcSwitch:

    pass
class jointPackage_CPL2SPL_SrcStringSwitch(SrcSwitch):

    def __init__(self, field: str, jointPackage_CPL2SPL_SrcStringSwitch: set["SrcSwitchedString"] = None):
        self.field = field
        self.jointPackage_CPL2SPL_SrcStringSwitch = jointPackage_CPL2SPL_SrcStringSwitch if jointPackage_CPL2SPL_SrcStringSwitch is not None else set()
        
    @property
    def field(self) -> str:
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field

    @property
    def jointPackage_CPL2SPL_SrcStringSwitch(self):
        return self.__jointPackage_CPL2SPL_SrcStringSwitch

    @jointPackage_CPL2SPL_SrcStringSwitch.setter
    def jointPackage_CPL2SPL_SrcStringSwitch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_CPL2SPL_SrcStringSwitch__jointPackage_CPL2SPL_SrcStringSwitch", None)
        self.__jointPackage_CPL2SPL_SrcStringSwitch = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SrcSwitchedString"):
                    opp_val = getattr(item, "SrcSwitchedString", None)
                    
                    if opp_val == self:
                        setattr(item, "SrcSwitchedString", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SrcSwitchedString"):
                    opp_val = getattr(item, "SrcSwitchedString", None)
                    
                    setattr(item, "SrcSwitchedString", self)
                    

class jointPackage_CPL2SPL_SrcLanguageSwitch(SrcSwitch):

    pass
class jointPackage_CPL2SPL_SrcTimeSwitch(SrcSwitch):

    def __init__(self, tzid: str, tzurl: str, jointPackage_CPL2SPL_SrcTimeSwitch: set["SrcSwitchedTime"] = None):
        self.tzid = tzid
        self.tzurl = tzurl
        self.jointPackage_CPL2SPL_SrcTimeSwitch = jointPackage_CPL2SPL_SrcTimeSwitch if jointPackage_CPL2SPL_SrcTimeSwitch is not None else set()
        
    @property
    def tzurl(self) -> str:
        return self.__tzurl

    @tzurl.setter
    def tzurl(self, tzurl: str):
        self.__tzurl = tzurl

    @property
    def tzid(self) -> str:
        return self.__tzid

    @tzid.setter
    def tzid(self, tzid: str):
        self.__tzid = tzid

    @property
    def jointPackage_CPL2SPL_SrcTimeSwitch(self):
        return self.__jointPackage_CPL2SPL_SrcTimeSwitch

    @jointPackage_CPL2SPL_SrcTimeSwitch.setter
    def jointPackage_CPL2SPL_SrcTimeSwitch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_CPL2SPL_SrcTimeSwitch__jointPackage_CPL2SPL_SrcTimeSwitch", None)
        self.__jointPackage_CPL2SPL_SrcTimeSwitch = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SrcSwitchedTime"):
                    opp_val = getattr(item, "SrcSwitchedTime", None)
                    
                    if opp_val == self:
                        setattr(item, "SrcSwitchedTime", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SrcSwitchedTime"):
                    opp_val = getattr(item, "SrcSwitchedTime", None)
                    
                    setattr(item, "SrcSwitchedTime", self)
                    

class jointPackage_CPL2SPL_SrcPrioritySwitch(SrcSwitch):

    pass
class jointPackage_CPL2SPL_SrcAddressSwitch(SrcSwitch):

    def __init__(self, field: str, subField: str, jointPackage_CPL2SPL_SrcAddressSwitch: set["SrcSwitchedAddress"] = None):
        self.field = field
        self.subField = subField
        self.jointPackage_CPL2SPL_SrcAddressSwitch = jointPackage_CPL2SPL_SrcAddressSwitch if jointPackage_CPL2SPL_SrcAddressSwitch is not None else set()
        
    @property
    def subField(self) -> str:
        return self.__subField

    @subField.setter
    def subField(self, subField: str):
        self.__subField = subField

    @property
    def field(self) -> str:
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field

    @property
    def jointPackage_CPL2SPL_SrcAddressSwitch(self):
        return self.__jointPackage_CPL2SPL_SrcAddressSwitch

    @jointPackage_CPL2SPL_SrcAddressSwitch.setter
    def jointPackage_CPL2SPL_SrcAddressSwitch(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_jointPackage_CPL2SPL_SrcAddressSwitch__jointPackage_CPL2SPL_SrcAddressSwitch", None)
        self.__jointPackage_CPL2SPL_SrcAddressSwitch = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SrcSwitchedAddress"):
                    opp_val = getattr(item, "SrcSwitchedAddress", None)
                    
                    if opp_val == self:
                        setattr(item, "SrcSwitchedAddress", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SrcSwitchedAddress"):
                    opp_val = getattr(item, "SrcSwitchedAddress", None)
                    
                    setattr(item, "SrcSwitchedAddress", self)
                    

class SrcReject:

    pass
class jointPackage_CPL2SPL_JointMM:

    pass