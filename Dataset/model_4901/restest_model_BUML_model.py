####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Enumerations
ContentType: Enumeration = Enumeration(
    name="ContentType",
    literals={
            EnumerationLiteral(name="TEXT"),
			EnumerationLiteral(name="TEXT_PLAIN"),
			EnumerationLiteral(name="JSON"),
			EnumerationLiteral(name="JAVASCRIPT"),
			EnumerationLiteral(name="XML_TEXT"),
			EnumerationLiteral(name="XML_APPLICATION"),
			EnumerationLiteral(name="HTML"),
			EnumerationLiteral(name="JAVA_LANG_EXCEPTION")
    }
)

HttpVerb: Enumeration = Enumeration(
    name="HttpVerb",
    literals={
            EnumerationLiteral(name="GET"),
			EnumerationLiteral(name="POST"),
			EnumerationLiteral(name="PUT"),
			EnumerationLiteral(name="DELETE")
    }
)

StatusCode: Enumeration = Enumeration(
    name="StatusCode",
    literals={
            EnumerationLiteral(name="PROCESSING"),
			EnumerationLiteral(name="OK"),
			EnumerationLiteral(name="CREATED"),
			EnumerationLiteral(name="ACCEPTED"),
			EnumerationLiteral(name="NON_AUTHORITATIVE_INFORMATION"),
			EnumerationLiteral(name="NO_CONTENT"),
			EnumerationLiteral(name="RESET_CONTENT"),
			EnumerationLiteral(name="PARTIAL_CONTENT"),
			EnumerationLiteral(name="MULTI_STATUS"),
			EnumerationLiteral(name="MULTIPLE_CHOICES"),
			EnumerationLiteral(name="MOVED_PERMANENTLY"),
			EnumerationLiteral(name="MOVED_TEMPORARILY"),
			EnumerationLiteral(name="SEE_OTHER"),
			EnumerationLiteral(name="NOT_MODIFIED"),
			EnumerationLiteral(name="USE_PROXY"),
			EnumerationLiteral(name="TEMPORARY_REDIRECT"),
			EnumerationLiteral(name="BAD_REQUEST"),
			EnumerationLiteral(name="UNAUTHORIZED"),
			EnumerationLiteral(name="PAYMENT_REQUIRED"),
			EnumerationLiteral(name="FORBIDDEN"),
			EnumerationLiteral(name="NOT_FOUND"),
			EnumerationLiteral(name="METHOD_NOT_ALLOWED"),
			EnumerationLiteral(name="NOT_ACCEPTABLE"),
			EnumerationLiteral(name="PROXY_AUTHENTICATION_REQUIRED"),
			EnumerationLiteral(name="REQUEST_TIMEOUT"),
			EnumerationLiteral(name="CONFLICT"),
			EnumerationLiteral(name="GONE"),
			EnumerationLiteral(name="LENGTH_REQUIRED"),
			EnumerationLiteral(name="PRECONDITION_FAILED"),
			EnumerationLiteral(name="REQUEST_TOO_LONG"),
			EnumerationLiteral(name="REQUEST_URI_TOO_LONG"),
			EnumerationLiteral(name="UNSUPPORTED_MEDIA_TYPE"),
			EnumerationLiteral(name="REQUESTED_RANGE_NOT_SATISFIABLE"),
			EnumerationLiteral(name="EXPECTATION_FAILED"),
			EnumerationLiteral(name="INSUFFICIENT_SPACE_ON_RESOURCE"),
			EnumerationLiteral(name="METHOD_FAILURE"),
			EnumerationLiteral(name="UNPROCESSABLE_ENTITY"),
			EnumerationLiteral(name="LOCKED"),
			EnumerationLiteral(name="FAILED_DEPENDENCY"),
			EnumerationLiteral(name="INTERNAL_SERVER_ERROR"),
			EnumerationLiteral(name="NOT_IMPLEMENTED"),
			EnumerationLiteral(name="BAD_GATEWAY"),
			EnumerationLiteral(name="CONTINUE"),
			EnumerationLiteral(name="SWITCHING_PROTOCOLS"),
			EnumerationLiteral(name="SERVICE_UNAVAILABLE"),
			EnumerationLiteral(name="GATEWAY_TIMEOUT"),
			EnumerationLiteral(name="HTTP_VERSION_NOT_SUPPORTED"),
			EnumerationLiteral(name="INSUFFICIENT_STORAGE"),
			EnumerationLiteral(name="CONNECTION_EXCEPTION")
    }
)

# Classes
model_Config = Class(name="model::Config")
model_Response = Class(name="model::Response")
model_Scenario = Class(name="model::Scenario")
model_ConfigExpectedResultPair = Class(name="model::ConfigExpectedResultPair")
model_ExpectedResult = Class(name="model::ExpectedResult")

# model_Config class attributes and methods
model_Config_name: Property = Property(name="name", type=StringType)
model_Config_requestURL: Property = Property(name="requestURL", type=StringType)
model_Config_httpVerb: Property = Property(name="httpVerb", type=StringType)
model_Config_contentType: Property = Property(name="contentType", type=StringType)
model_Config_requestBody: Property = Property(name="requestBody", type=StringType)
model_Config.attributes={model_Config_requestURL, model_Config_requestBody, model_Config_name, model_Config_httpVerb, model_Config_contentType}

# model_Response class attributes and methods
model_Response_statusCode: Property = Property(name="statusCode", type=StringType)
model_Response_contentType: Property = Property(name="contentType", type=StringType)
model_Response_responseTime: Property = Property(name="responseTime", type=StringType)
model_Response_responseBody: Property = Property(name="responseBody", type=StringType)
model_Response.attributes={model_Response_statusCode, model_Response_responseTime, model_Response_responseBody, model_Response_contentType}

# model_Scenario class attributes and methods
model_Scenario_scenarioFilePath: Property = Property(name="scenarioFilePath", type=StringType)
model_Scenario.attributes={model_Scenario_scenarioFilePath}

# model_ConfigExpectedResultPair class attributes and methods

# model_ExpectedResult class attributes and methods
model_ExpectedResult_statusCode: Property = Property(name="statusCode", type=StringType)
model_ExpectedResult_contentType: Property = Property(name="contentType", type=StringType)
model_ExpectedResult_responseBody: Property = Property(name="responseBody", type=StringType)
model_ExpectedResult.attributes={model_ExpectedResult_contentType, model_ExpectedResult_responseBody, model_ExpectedResult_statusCode}

# Relationships
response0: BinaryAssociation = BinaryAssociation(
    name="response0",
    ends={
        Property(name="model_Response", type=model_Config, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Config", type=model_Response, multiplicity=Multiplicity(0, 1))
    }
)
configExpectedResultPairList1: BinaryAssociation = BinaryAssociation(
    name="configExpectedResultPairList1",
    ends={
        Property(name="model_ConfigExpectedResultPair", type=model_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Scenario", type=model_ConfigExpectedResultPair, multiplicity=Multiplicity(0, 9999))
    }
)
config2: BinaryAssociation = BinaryAssociation(
    name="config2",
    ends={
        Property(name="model_Config4", type=model_ConfigExpectedResultPair, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ConfigExpectedResultPair3", type=model_Config, multiplicity=Multiplicity(0, 1))
    }
)
expectedResult5: BinaryAssociation = BinaryAssociation(
    name="expectedResult5",
    ends={
        Property(name="model_ExpectedResult", type=model_ConfigExpectedResultPair, multiplicity=Multiplicity(1, 1)),
        Property(name="model_ConfigExpectedResultPair6", type=model_ExpectedResult, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_Config, model_Response, model_Scenario, model_ConfigExpectedResultPair, model_ExpectedResult, ContentType, HttpVerb, StatusCode},
    associations={response0, configExpectedResultPairList1, config2, expectedResult5},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)