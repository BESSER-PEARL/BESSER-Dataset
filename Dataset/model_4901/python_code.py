from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class StatusCode(Enum):
    PROCESSING = "PROCESSING"
    OK = "OK"
    CREATED = "CREATED"
    ACCEPTED = "ACCEPTED"
    NON_AUTHORITATIVE_INFORMATION = "NON_AUTHORITATIVE_INFORMATION"
    NO_CONTENT = "NO_CONTENT"
    RESET_CONTENT = "RESET_CONTENT"
    PARTIAL_CONTENT = "PARTIAL_CONTENT"
    MULTI_STATUS = "MULTI_STATUS"
    MULTIPLE_CHOICES = "MULTIPLE_CHOICES"
    MOVED_PERMANENTLY = "MOVED_PERMANENTLY"
    MOVED_TEMPORARILY = "MOVED_TEMPORARILY"
    SEE_OTHER = "SEE_OTHER"
    NOT_MODIFIED = "NOT_MODIFIED"
    USE_PROXY = "USE_PROXY"
    TEMPORARY_REDIRECT = "TEMPORARY_REDIRECT"
    BAD_REQUEST = "BAD_REQUEST"
    UNAUTHORIZED = "UNAUTHORIZED"
    PAYMENT_REQUIRED = "PAYMENT_REQUIRED"
    FORBIDDEN = "FORBIDDEN"
    NOT_FOUND = "NOT_FOUND"
    METHOD_NOT_ALLOWED = "METHOD_NOT_ALLOWED"
    NOT_ACCEPTABLE = "NOT_ACCEPTABLE"
    PROXY_AUTHENTICATION_REQUIRED = "PROXY_AUTHENTICATION_REQUIRED"
    REQUEST_TIMEOUT = "REQUEST_TIMEOUT"
    CONFLICT = "CONFLICT"
    GONE = "GONE"
    LENGTH_REQUIRED = "LENGTH_REQUIRED"
    PRECONDITION_FAILED = "PRECONDITION_FAILED"
    REQUEST_TOO_LONG = "REQUEST_TOO_LONG"
    REQUEST_URI_TOO_LONG = "REQUEST_URI_TOO_LONG"
    UNSUPPORTED_MEDIA_TYPE = "UNSUPPORTED_MEDIA_TYPE"
    REQUESTED_RANGE_NOT_SATISFIABLE = "REQUESTED_RANGE_NOT_SATISFIABLE"
    EXPECTATION_FAILED = "EXPECTATION_FAILED"
    INSUFFICIENT_SPACE_ON_RESOURCE = "INSUFFICIENT_SPACE_ON_RESOURCE"
    METHOD_FAILURE = "METHOD_FAILURE"
    UNPROCESSABLE_ENTITY = "UNPROCESSABLE_ENTITY"
    LOCKED = "LOCKED"
    FAILED_DEPENDENCY = "FAILED_DEPENDENCY"
    INTERNAL_SERVER_ERROR = "INTERNAL_SERVER_ERROR"
    NOT_IMPLEMENTED = "NOT_IMPLEMENTED"
    BAD_GATEWAY = "BAD_GATEWAY"
    CONTINUE = "CONTINUE"
    SWITCHING_PROTOCOLS = "SWITCHING_PROTOCOLS"
    SERVICE_UNAVAILABLE = "SERVICE_UNAVAILABLE"
    GATEWAY_TIMEOUT = "GATEWAY_TIMEOUT"
    HTTP_VERSION_NOT_SUPPORTED = "HTTP_VERSION_NOT_SUPPORTED"
    INSUFFICIENT_STORAGE = "INSUFFICIENT_STORAGE"
    CONNECTION_EXCEPTION = "CONNECTION_EXCEPTION"
class HttpVerb(Enum):
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
class ContentType(Enum):
    TEXT = "TEXT"
    TEXT_PLAIN = "TEXT_PLAIN"
    JSON = "JSON"
    JAVASCRIPT = "JAVASCRIPT"
    XML_TEXT = "XML_TEXT"
    XML_APPLICATION = "XML_APPLICATION"
    HTML = "HTML"
    JAVA_LANG_EXCEPTION = "JAVA_LANG_EXCEPTION"


############################################
# Definition of Classes
############################################

class model_ExpectedResult:

    def __init__(self, statusCode: str, contentType: str, responseBody: str, model_ExpectedResult: "model_ConfigExpectedResultPair" = None):
        self.statusCode = statusCode
        self.contentType = contentType
        self.responseBody = responseBody
        self.model_ExpectedResult = model_ExpectedResult
        
    @property
    def contentType(self) -> str:
        return self.__contentType

    @contentType.setter
    def contentType(self, contentType: str):
        self.__contentType = contentType

    @property
    def responseBody(self) -> str:
        return self.__responseBody

    @responseBody.setter
    def responseBody(self, responseBody: str):
        self.__responseBody = responseBody

    @property
    def statusCode(self) -> str:
        return self.__statusCode

    @statusCode.setter
    def statusCode(self, statusCode: str):
        self.__statusCode = statusCode

    @property
    def model_ExpectedResult(self):
        return self.__model_ExpectedResult

    @model_ExpectedResult.setter
    def model_ExpectedResult(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_ExpectedResult__model_ExpectedResult", None)
        self.__model_ExpectedResult = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ConfigExpectedResultPair6"):
                opp_val = getattr(old_value, "model_ConfigExpectedResultPair6", None)
                if opp_val == self:
                    setattr(old_value, "model_ConfigExpectedResultPair6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ConfigExpectedResultPair6"):
                opp_val = getattr(value, "model_ConfigExpectedResultPair6", None)
                setattr(value, "model_ConfigExpectedResultPair6", self)

class model_ConfigExpectedResultPair:

    pass
class model_Scenario:

    def __init__(self, scenarioFilePath: str, model_Scenario: set["model_ConfigExpectedResultPair"] = None):
        self.scenarioFilePath = scenarioFilePath
        self.model_Scenario = model_Scenario if model_Scenario is not None else set()
        
    @property
    def scenarioFilePath(self) -> str:
        return self.__scenarioFilePath

    @scenarioFilePath.setter
    def scenarioFilePath(self, scenarioFilePath: str):
        self.__scenarioFilePath = scenarioFilePath

    @property
    def model_Scenario(self):
        return self.__model_Scenario

    @model_Scenario.setter
    def model_Scenario(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Scenario__model_Scenario", None)
        self.__model_Scenario = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_ConfigExpectedResultPair"):
                    opp_val = getattr(item, "model_ConfigExpectedResultPair", None)
                    
                    if opp_val == self:
                        setattr(item, "model_ConfigExpectedResultPair", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_ConfigExpectedResultPair"):
                    opp_val = getattr(item, "model_ConfigExpectedResultPair", None)
                    
                    setattr(item, "model_ConfigExpectedResultPair", self)
                    

class model_Response:

    def __init__(self, statusCode: str, contentType: str, responseTime: str, responseBody: str, model_Response: "model_Config" = None):
        self.statusCode = statusCode
        self.contentType = contentType
        self.responseTime = responseTime
        self.responseBody = responseBody
        self.model_Response = model_Response
        
    @property
    def statusCode(self) -> str:
        return self.__statusCode

    @statusCode.setter
    def statusCode(self, statusCode: str):
        self.__statusCode = statusCode

    @property
    def responseTime(self) -> str:
        return self.__responseTime

    @responseTime.setter
    def responseTime(self, responseTime: str):
        self.__responseTime = responseTime

    @property
    def responseBody(self) -> str:
        return self.__responseBody

    @responseBody.setter
    def responseBody(self, responseBody: str):
        self.__responseBody = responseBody

    @property
    def contentType(self) -> str:
        return self.__contentType

    @contentType.setter
    def contentType(self, contentType: str):
        self.__contentType = contentType

    @property
    def model_Response(self):
        return self.__model_Response

    @model_Response.setter
    def model_Response(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Response__model_Response", None)
        self.__model_Response = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Config"):
                opp_val = getattr(old_value, "model_Config", None)
                if opp_val == self:
                    setattr(old_value, "model_Config", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Config"):
                opp_val = getattr(value, "model_Config", None)
                setattr(value, "model_Config", self)

class model_Config:

    def __init__(self, name: str, requestURL: str, httpVerb: str, contentType: str, requestBody: str, model_Config: "model_Response" = None, model_Config4: "model_ConfigExpectedResultPair" = None):
        self.name = name
        self.requestURL = requestURL
        self.httpVerb = httpVerb
        self.contentType = contentType
        self.requestBody = requestBody
        self.model_Config = model_Config
        self.model_Config4 = model_Config4
        
    @property
    def requestURL(self) -> str:
        return self.__requestURL

    @requestURL.setter
    def requestURL(self, requestURL: str):
        self.__requestURL = requestURL

    @property
    def requestBody(self) -> str:
        return self.__requestBody

    @requestBody.setter
    def requestBody(self, requestBody: str):
        self.__requestBody = requestBody

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def httpVerb(self) -> str:
        return self.__httpVerb

    @httpVerb.setter
    def httpVerb(self, httpVerb: str):
        self.__httpVerb = httpVerb

    @property
    def contentType(self) -> str:
        return self.__contentType

    @contentType.setter
    def contentType(self, contentType: str):
        self.__contentType = contentType

    @property
    def model_Config4(self):
        return self.__model_Config4

    @model_Config4.setter
    def model_Config4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Config__model_Config4", None)
        self.__model_Config4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_ConfigExpectedResultPair3"):
                opp_val = getattr(old_value, "model_ConfigExpectedResultPair3", None)
                if opp_val == self:
                    setattr(old_value, "model_ConfigExpectedResultPair3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_ConfigExpectedResultPair3"):
                opp_val = getattr(value, "model_ConfigExpectedResultPair3", None)
                setattr(value, "model_ConfigExpectedResultPair3", self)

    @property
    def model_Config(self):
        return self.__model_Config

    @model_Config.setter
    def model_Config(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Config__model_Config", None)
        self.__model_Config = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Response"):
                opp_val = getattr(old_value, "model_Response", None)
                if opp_val == self:
                    setattr(old_value, "model_Response", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Response"):
                opp_val = getattr(value, "model_Response", None)
                setattr(value, "model_Response", self)
