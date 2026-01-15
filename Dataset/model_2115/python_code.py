from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class ParameterLocation(Enum):
    undefined = "undefined"
    query = "query"
    path = "path"
    header = "header"
    body = "body"
    formData = "formData"
class PathLanguage(Enum):
    undefined = "undefined"
    XPath = "XPath"
    JSONPath = "JSONPath"
class HTTPMethod(Enum):
    undefined = "undefined"
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    OPTIONS = "OPTIONS"
class SchemeType(Enum):
    undefined = "undefined"
    http = "http"
    https = "https"


############################################
# Definition of Classes
############################################

class OutputProperty:

    pass
class test_ResponseProperty(OutputProperty):

    pass
class InputProperty:

    pass
class test_ParameterProperty(InputProperty):

    pass
class test_HeaderProperty(OutputProperty):

    pass
class Property:

    pass
class test_OutputProperty(Property):

    pass
class test_InputProperty(Property):

    pass
class test_Property(ABC):

    def __init__(self, expression: str, pathLanguage: str, test_Property: "test_PropertyTransfer" = None, test_Property11: "test_PropertyTransfer" = None):
        self.expression = expression
        self.pathLanguage = pathLanguage
        self.test_Property = test_Property
        self.test_Property11 = test_Property11
        
    @property
    def pathLanguage(self) -> str:
        return self.__pathLanguage

    @pathLanguage.setter
    def pathLanguage(self, pathLanguage: str):
        self.__pathLanguage = pathLanguage

    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def test_Property(self):
        return self.__test_Property

    @test_Property.setter
    def test_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_Property__test_Property", None)
        self.__test_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_PropertyTransfer"):
                opp_val = getattr(old_value, "test_PropertyTransfer", None)
                if opp_val == self:
                    setattr(old_value, "test_PropertyTransfer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_PropertyTransfer"):
                opp_val = getattr(value, "test_PropertyTransfer", None)
                setattr(value, "test_PropertyTransfer", self)

    @property
    def test_Property11(self):
        return self.__test_Property11

    @test_Property11.setter
    def test_Property11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_Property__test_Property11", None)
        self.__test_Property11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_PropertyTransfer10"):
                opp_val = getattr(old_value, "test_PropertyTransfer10", None)
                if opp_val == self:
                    setattr(old_value, "test_PropertyTransfer10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_PropertyTransfer10"):
                opp_val = getattr(value, "test_PropertyTransfer10", None)
                setattr(value, "test_PropertyTransfer10", self)

class Authorization:

    pass
class test_OAuth2(Authorization):

    def __init__(self, token: str):
        self.token = token
        
    @property
    def token(self) -> str:
        return self.__token

    @token.setter
    def token(self, token: str):
        self.__token = token

class test_Basic(Authorization):

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        
    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

class HTTPStatusAssertion:

    pass
class test_ValidStatusCodesAssertion(HTTPStatusAssertion):

    pass
class test_InvalidStatusCodesAssertion(HTTPStatusAssertion):

    pass
class Assertion:

    pass
class test_ResponseMessageAssertion(Assertion):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class test_PerformanceAssertion(Assertion):

    pass
class test_HTTPStatusAssertion(Assertion):

    def __init__(self, code: str):
        self.code = code
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

class test_ComplianceAssertion(Assertion):

    def __init__(self, path: str):
        self.path = path
        
    @property
    def path(self) -> str:
        return self.__path

    @path.setter
    def path(self, path: str):
        self.__path = path

class HeaderAssertion:

    pass
class test_HeaderExistsAssertion(HeaderAssertion):

    pass
class test_HeaderEqualsAssertion(HeaderAssertion):

    def __init__(self, value: str):
        self.value = value
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

class test_HeaderAssertion(Assertion):

    def __init__(self, key: str):
        self.key = key
        
    @property
    def key(self) -> str:
        return self.__key

    @key.setter
    def key(self, key: str):
        self.__key = key

class PerformanceAssertion:

    pass
class test_SLAAssertion(PerformanceAssertion):

    def __init__(self, maxTime: str):
        self.maxTime = maxTime
        
    @property
    def maxTime(self) -> str:
        return self.__maxTime

    @maxTime.setter
    def maxTime(self, maxTime: str):
        self.__maxTime = maxTime

class ComplianceAssertion:

    pass
class test_SchemaComplianceAssertion(ComplianceAssertion):

    pass
class ResponseMessageAssertion:

    pass
class test_ResponseMessageEqualsAssertion(ResponseMessageAssertion):

    pass
class test_ResponseMessageContainsAssertion(ResponseMessageAssertion):

    pass
class TestStep:

    pass
class test_PropertyTransfer(TestStep):

    pass
class test_APIRequest(TestStep):

    def __init__(self, scheme: str, operationId: str, contentType: str, accept: str, test_APIRequest: set["test_Parameter"] = None, test_APIRequest5: set["test_Assertion"] = None, test_APIRequest7: "test_Authorization" = None, test_APIRequest15: "test_OutputProperty" = None):
        self.scheme = scheme
        self.operationId = operationId
        self.contentType = contentType
        self.accept = accept
        self.test_APIRequest = test_APIRequest if test_APIRequest is not None else set()
        self.test_APIRequest5 = test_APIRequest5 if test_APIRequest5 is not None else set()
        self.test_APIRequest7 = test_APIRequest7
        self.test_APIRequest15 = test_APIRequest15
        
    @property
    def operationId(self) -> str:
        return self.__operationId

    @operationId.setter
    def operationId(self, operationId: str):
        self.__operationId = operationId

    @property
    def accept(self) -> str:
        return self.__accept

    @accept.setter
    def accept(self, accept: str):
        self.__accept = accept

    @property
    def scheme(self) -> str:
        return self.__scheme

    @scheme.setter
    def scheme(self, scheme: str):
        self.__scheme = scheme

    @property
    def contentType(self) -> str:
        return self.__contentType

    @contentType.setter
    def contentType(self, contentType: str):
        self.__contentType = contentType

    @property
    def test_APIRequest7(self):
        return self.__test_APIRequest7

    @test_APIRequest7.setter
    def test_APIRequest7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_APIRequest__test_APIRequest7", None)
        self.__test_APIRequest7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_Authorization"):
                opp_val = getattr(old_value, "test_Authorization", None)
                if opp_val == self:
                    setattr(old_value, "test_Authorization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_Authorization"):
                opp_val = getattr(value, "test_Authorization", None)
                setattr(value, "test_Authorization", self)

    @property
    def test_APIRequest5(self):
        return self.__test_APIRequest5

    @test_APIRequest5.setter
    def test_APIRequest5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_APIRequest__test_APIRequest5", None)
        self.__test_APIRequest5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "test_Assertion"):
                    opp_val = getattr(item, "test_Assertion", None)
                    
                    if opp_val == self:
                        setattr(item, "test_Assertion", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "test_Assertion"):
                    opp_val = getattr(item, "test_Assertion", None)
                    
                    setattr(item, "test_Assertion", self)
                    

    @property
    def test_APIRequest(self):
        return self.__test_APIRequest

    @test_APIRequest.setter
    def test_APIRequest(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_APIRequest__test_APIRequest", None)
        self.__test_APIRequest = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "test_Parameter"):
                    opp_val = getattr(item, "test_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "test_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "test_Parameter"):
                    opp_val = getattr(item, "test_Parameter", None)
                    
                    setattr(item, "test_Parameter", self)
                    

    @property
    def test_APIRequest15(self):
        return self.__test_APIRequest15

    @test_APIRequest15.setter
    def test_APIRequest15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_APIRequest__test_APIRequest15", None)
        self.__test_APIRequest15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_OutputProperty"):
                opp_val = getattr(old_value, "test_OutputProperty", None)
                if opp_val == self:
                    setattr(old_value, "test_OutputProperty", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_OutputProperty"):
                opp_val = getattr(value, "test_OutputProperty", None)
                setattr(value, "test_OutputProperty", self)

class test_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class test_Authorization(ABC):

    pass
class test_Assertion(ABC):

    def __init__(self, errorMessage: str, test_Assertion: "test_APIRequest" = None):
        self.errorMessage = errorMessage
        self.test_Assertion = test_Assertion
        
    @property
    def errorMessage(self) -> str:
        return self.__errorMessage

    @errorMessage.setter
    def errorMessage(self, errorMessage: str):
        self.__errorMessage = errorMessage

    @property
    def test_Assertion(self):
        return self.__test_Assertion

    @test_Assertion.setter
    def test_Assertion(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_Assertion__test_Assertion", None)
        self.__test_Assertion = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_APIRequest5"):
                opp_val = getattr(old_value, "test_APIRequest5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_APIRequest5"):
                opp_val = getattr(value, "test_APIRequest5", None)
                if opp_val is None:
                    setattr(value, "test_APIRequest5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class test_Parameter:

    def __init__(self, location: str, name: str, value: str, test_Parameter: "test_APIRequest" = None, test_Parameter13: "test_ParameterProperty" = None):
        self.location = location
        self.name = name
        self.value = value
        self.test_Parameter = test_Parameter
        self.test_Parameter13 = test_Parameter13
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def location(self) -> str:
        return self.__location

    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def test_Parameter(self):
        return self.__test_Parameter

    @test_Parameter.setter
    def test_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_Parameter__test_Parameter", None)
        self.__test_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_APIRequest"):
                opp_val = getattr(old_value, "test_APIRequest", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_APIRequest"):
                opp_val = getattr(value, "test_APIRequest", None)
                if opp_val is None:
                    setattr(value, "test_APIRequest", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def test_Parameter13(self):
        return self.__test_Parameter13

    @test_Parameter13.setter
    def test_Parameter13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_Parameter__test_Parameter13", None)
        self.__test_Parameter13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_ParameterProperty"):
                opp_val = getattr(old_value, "test_ParameterProperty", None)
                if opp_val == self:
                    setattr(old_value, "test_ParameterProperty", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_ParameterProperty"):
                opp_val = getattr(value, "test_ParameterProperty", None)
                setattr(value, "test_ParameterProperty", self)

class NamedElement:

    pass
class test_TestCase(NamedElement):

    def __init__(self, description: str, test_TestCase: "test_TestSuite" = None, test_TestCase2: set["test_TestStep"] = None):
        self.description = description
        self.test_TestCase = test_TestCase
        self.test_TestCase2 = test_TestCase2 if test_TestCase2 is not None else set()
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def test_TestCase(self):
        return self.__test_TestCase

    @test_TestCase.setter
    def test_TestCase(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestCase__test_TestCase", None)
        self.__test_TestCase = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test_TestSuite"):
                opp_val = getattr(old_value, "test_TestSuite", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test_TestSuite"):
                opp_val = getattr(value, "test_TestSuite", None)
                if opp_val is None:
                    setattr(value, "test_TestSuite", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def test_TestCase2(self):
        return self.__test_TestCase2

    @test_TestCase2.setter
    def test_TestCase2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestCase__test_TestCase2", None)
        self.__test_TestCase2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "test_TestStep"):
                    opp_val = getattr(item, "test_TestStep", None)
                    
                    if opp_val == self:
                        setattr(item, "test_TestStep", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "test_TestStep"):
                    opp_val = getattr(item, "test_TestStep", None)
                    
                    setattr(item, "test_TestStep", self)
                    

class test_TestStep(NamedElement):

    pass
class test_TestSuite(NamedElement):

    def __init__(self, description: str, api: str, test_TestSuite: set["test_TestCase"] = None):
        self.description = description
        self.api = api
        self.test_TestSuite = test_TestSuite if test_TestSuite is not None else set()
        
    @property
    def api(self) -> str:
        return self.__api

    @api.setter
    def api(self, api: str):
        self.__api = api

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def test_TestSuite(self):
        return self.__test_TestSuite

    @test_TestSuite.setter
    def test_TestSuite(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test_TestSuite__test_TestSuite", None)
        self.__test_TestSuite = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "test_TestCase"):
                    opp_val = getattr(item, "test_TestCase", None)
                    
                    if opp_val == self:
                        setattr(item, "test_TestCase", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "test_TestCase"):
                    opp_val = getattr(item, "test_TestCase", None)
                    
                    setattr(item, "test_TestCase", self)
                    
