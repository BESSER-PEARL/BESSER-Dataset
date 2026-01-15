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
ParameterLocation: Enumeration = Enumeration(
    name="ParameterLocation",
    literals={
            EnumerationLiteral(name="undefined"),
			EnumerationLiteral(name="query"),
			EnumerationLiteral(name="path"),
			EnumerationLiteral(name="header"),
			EnumerationLiteral(name="body"),
			EnumerationLiteral(name="formData")
    }
)

SchemeType: Enumeration = Enumeration(
    name="SchemeType",
    literals={
            EnumerationLiteral(name="undefined"),
			EnumerationLiteral(name="http"),
			EnumerationLiteral(name="https")
    }
)

HTTPMethod: Enumeration = Enumeration(
    name="HTTPMethod",
    literals={
            EnumerationLiteral(name="undefined"),
			EnumerationLiteral(name="GET"),
			EnumerationLiteral(name="POST"),
			EnumerationLiteral(name="PUT"),
			EnumerationLiteral(name="DELETE"),
			EnumerationLiteral(name="OPTIONS")
    }
)

PathLanguage: Enumeration = Enumeration(
    name="PathLanguage",
    literals={
            EnumerationLiteral(name="undefined"),
			EnumerationLiteral(name="XPath"),
			EnumerationLiteral(name="JSONPath")
    }
)

# Classes
test_TestSuite = Class(name="test::TestSuite")
NamedElement = Class(name="NamedElement")
test_TestCase = Class(name="test::TestCase")
test_Parameter = Class(name="test::Parameter")
test_Assertion = Class(name="test::Assertion", is_abstract=True)
test_Authorization = Class(name="test::Authorization", is_abstract=True)
test_NamedElement = Class(name="test::NamedElement", is_abstract=True)
test_TestStep = Class(name="test::TestStep", is_abstract=True)
test_APIRequest = Class(name="test::APIRequest")
TestStep = Class(name="TestStep")
test_ResponseMessageContainsAssertion = Class(name="test::ResponseMessageContainsAssertion")
ResponseMessageAssertion = Class(name="ResponseMessageAssertion")
test_ResponseMessageEqualsAssertion = Class(name="test::ResponseMessageEqualsAssertion")
test_SchemaComplianceAssertion = Class(name="test::SchemaComplianceAssertion")
ComplianceAssertion = Class(name="ComplianceAssertion")
test_SLAAssertion = Class(name="test::SLAAssertion")
PerformanceAssertion = Class(name="PerformanceAssertion")
test_HeaderAssertion = Class(name="test::HeaderAssertion", is_abstract=True)
test_HeaderEqualsAssertion = Class(name="test::HeaderEqualsAssertion")
HeaderAssertion = Class(name="HeaderAssertion")
test_ComplianceAssertion = Class(name="test::ComplianceAssertion", is_abstract=True)
Assertion = Class(name="Assertion")
test_PerformanceAssertion = Class(name="test::PerformanceAssertion", is_abstract=True)
test_ResponseMessageAssertion = Class(name="test::ResponseMessageAssertion", is_abstract=True)
test_InvalidStatusCodesAssertion = Class(name="test::InvalidStatusCodesAssertion")
HTTPStatusAssertion = Class(name="HTTPStatusAssertion")
test_ValidStatusCodesAssertion = Class(name="test::ValidStatusCodesAssertion")
test_Basic = Class(name="test::Basic")
Authorization = Class(name="Authorization")
test_OAuth2 = Class(name="test::OAuth2")
test_PropertyTransfer = Class(name="test::PropertyTransfer")
test_Property = Class(name="test::Property", is_abstract=True)
test_HeaderExistsAssertion = Class(name="test::HeaderExistsAssertion")
test_HTTPStatusAssertion = Class(name="test::HTTPStatusAssertion", is_abstract=True)
test_InputProperty = Class(name="test::InputProperty", is_abstract=True)
Property_ = Class(name="Property")
test_OutputProperty = Class(name="test::OutputProperty", is_abstract=True)
test_HeaderProperty = Class(name="test::HeaderProperty")
test_ParameterProperty = Class(name="test::ParameterProperty")
InputProperty = Class(name="InputProperty")
test_ResponseProperty = Class(name="test::ResponseProperty")
OutputProperty = Class(name="OutputProperty")

# test_TestSuite class attributes and methods
test_TestSuite_description: Property = Property(name="description", type=StringType)
test_TestSuite_api: Property = Property(name="api", type=StringType)
test_TestSuite.attributes={test_TestSuite_api, test_TestSuite_description}

# NamedElement class attributes and methods

# test_TestCase class attributes and methods
test_TestCase_description: Property = Property(name="description", type=StringType)
test_TestCase.attributes={test_TestCase_description}

# test_Parameter class attributes and methods
test_Parameter_location: Property = Property(name="location", type=StringType)
test_Parameter_name: Property = Property(name="name", type=StringType)
test_Parameter_value: Property = Property(name="value", type=StringType)
test_Parameter.attributes={test_Parameter_name, test_Parameter_location, test_Parameter_value}

# test_Assertion class attributes and methods
test_Assertion_errorMessage: Property = Property(name="errorMessage", type=StringType)
test_Assertion.attributes={test_Assertion_errorMessage}

# test_Authorization class attributes and methods

# test_NamedElement class attributes and methods
test_NamedElement_name: Property = Property(name="name", type=StringType)
test_NamedElement.attributes={test_NamedElement_name}

# test_TestStep class attributes and methods

# test_APIRequest class attributes and methods
test_APIRequest_scheme: Property = Property(name="scheme", type=StringType)
test_APIRequest_operationId: Property = Property(name="operationId", type=StringType)
test_APIRequest_contentType: Property = Property(name="contentType", type=StringType)
test_APIRequest_accept: Property = Property(name="accept", type=StringType)
test_APIRequest.attributes={test_APIRequest_operationId, test_APIRequest_accept, test_APIRequest_scheme, test_APIRequest_contentType}

# TestStep class attributes and methods

# test_ResponseMessageContainsAssertion class attributes and methods

# ResponseMessageAssertion class attributes and methods

# test_ResponseMessageEqualsAssertion class attributes and methods

# test_SchemaComplianceAssertion class attributes and methods

# ComplianceAssertion class attributes and methods

# test_SLAAssertion class attributes and methods
test_SLAAssertion_maxTime: Property = Property(name="maxTime", type=StringType)
test_SLAAssertion.attributes={test_SLAAssertion_maxTime}

# PerformanceAssertion class attributes and methods

# test_HeaderAssertion class attributes and methods
test_HeaderAssertion_key: Property = Property(name="key", type=StringType)
test_HeaderAssertion.attributes={test_HeaderAssertion_key}

# test_HeaderEqualsAssertion class attributes and methods
test_HeaderEqualsAssertion_value: Property = Property(name="value", type=StringType)
test_HeaderEqualsAssertion.attributes={test_HeaderEqualsAssertion_value}

# HeaderAssertion class attributes and methods

# test_ComplianceAssertion class attributes and methods
test_ComplianceAssertion_path: Property = Property(name="path", type=StringType)
test_ComplianceAssertion.attributes={test_ComplianceAssertion_path}

# Assertion class attributes and methods

# test_PerformanceAssertion class attributes and methods

# test_ResponseMessageAssertion class attributes and methods
test_ResponseMessageAssertion_value: Property = Property(name="value", type=StringType)
test_ResponseMessageAssertion.attributes={test_ResponseMessageAssertion_value}

# test_InvalidStatusCodesAssertion class attributes and methods

# HTTPStatusAssertion class attributes and methods

# test_ValidStatusCodesAssertion class attributes and methods

# test_Basic class attributes and methods
test_Basic_username: Property = Property(name="username", type=StringType)
test_Basic_password: Property = Property(name="password", type=StringType)
test_Basic.attributes={test_Basic_username, test_Basic_password}

# Authorization class attributes and methods

# test_OAuth2 class attributes and methods
test_OAuth2_token: Property = Property(name="token", type=StringType)
test_OAuth2.attributes={test_OAuth2_token}

# test_PropertyTransfer class attributes and methods

# test_Property class attributes and methods
test_Property_expression: Property = Property(name="expression", type=StringType)
test_Property_pathLanguage: Property = Property(name="pathLanguage", type=StringType)
test_Property.attributes={test_Property_pathLanguage, test_Property_expression}

# test_HeaderExistsAssertion class attributes and methods

# test_HTTPStatusAssertion class attributes and methods
test_HTTPStatusAssertion_code: Property = Property(name="code", type=StringType)
test_HTTPStatusAssertion.attributes={test_HTTPStatusAssertion_code}

# test_InputProperty class attributes and methods

# Property class attributes and methods

# test_OutputProperty class attributes and methods

# test_HeaderProperty class attributes and methods

# test_ParameterProperty class attributes and methods

# InputProperty class attributes and methods

# test_ResponseProperty class attributes and methods

# OutputProperty class attributes and methods

# Relationships
testCases0: BinaryAssociation = BinaryAssociation(
    name="testCases0",
    ends={
        Property(name="test_TestCase", type=test_TestSuite, multiplicity=Multiplicity(1, 1)),
        Property(name="test_TestSuite", type=test_TestCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters3: BinaryAssociation = BinaryAssociation(
    name="parameters3",
    ends={
        Property(name="test_Parameter", type=test_APIRequest, multiplicity=Multiplicity(1, 1)),
        Property(name="test_APIRequest", type=test_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assertions4: BinaryAssociation = BinaryAssociation(
    name="assertions4",
    ends={
        Property(name="test_Assertion", type=test_APIRequest, multiplicity=Multiplicity(1, 1)),
        Property(name="test_APIRequest5", type=test_Assertion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
authorization6: BinaryAssociation = BinaryAssociation(
    name="authorization6",
    ends={
        Property(name="test_Authorization", type=test_APIRequest, multiplicity=Multiplicity(1, 1)),
        Property(name="test_APIRequest7", type=test_Authorization, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
testSteps1: BinaryAssociation = BinaryAssociation(
    name="testSteps1",
    ends={
        Property(name="test_TestStep", type=test_TestCase, multiplicity=Multiplicity(1, 1)),
        Property(name="test_TestCase2", type=test_TestStep, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source8: BinaryAssociation = BinaryAssociation(
    name="source8",
    ends={
        Property(name="test_Property", type=test_PropertyTransfer, multiplicity=Multiplicity(1, 1)),
        Property(name="test_PropertyTransfer", type=test_Property, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target9: BinaryAssociation = BinaryAssociation(
    name="target9",
    ends={
        Property(name="test_Property11", type=test_PropertyTransfer, multiplicity=Multiplicity(1, 1)),
        Property(name="test_PropertyTransfer10", type=test_Property, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
request14: BinaryAssociation = BinaryAssociation(
    name="request14",
    ends={
        Property(name="test_APIRequest15", type=test_OutputProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="test_OutputProperty", type=test_APIRequest, multiplicity=Multiplicity(1, 1))
    }
)
parameter12: BinaryAssociation = BinaryAssociation(
    name="parameter12",
    ends={
        Property(name="test_Parameter13", type=test_ParameterProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="test_ParameterProperty", type=test_Parameter, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_test_TestSuite_NamedElement = Generalization(general=NamedElement, specific=test_TestSuite)
gen_test_TestCase_NamedElement = Generalization(general=NamedElement, specific=test_TestCase)
gen_test_TestStep_NamedElement = Generalization(general=NamedElement, specific=test_TestStep)
gen_test_APIRequest_TestStep = Generalization(general=TestStep, specific=test_APIRequest)
gen_test_ResponseMessageContainsAssertion_ResponseMessageAssertion = Generalization(general=ResponseMessageAssertion, specific=test_ResponseMessageContainsAssertion)
gen_test_ResponseMessageEqualsAssertion_ResponseMessageAssertion = Generalization(general=ResponseMessageAssertion, specific=test_ResponseMessageEqualsAssertion)
gen_test_SchemaComplianceAssertion_ComplianceAssertion = Generalization(general=ComplianceAssertion, specific=test_SchemaComplianceAssertion)
gen_test_SLAAssertion_PerformanceAssertion = Generalization(general=PerformanceAssertion, specific=test_SLAAssertion)
gen_test_HeaderAssertion_Assertion = Generalization(general=Assertion, specific=test_HeaderAssertion)
gen_test_HeaderEqualsAssertion_HeaderAssertion = Generalization(general=HeaderAssertion, specific=test_HeaderEqualsAssertion)
gen_test_ComplianceAssertion_Assertion = Generalization(general=Assertion, specific=test_ComplianceAssertion)
gen_test_PerformanceAssertion_Assertion = Generalization(general=Assertion, specific=test_PerformanceAssertion)
gen_test_ResponseMessageAssertion_Assertion = Generalization(general=Assertion, specific=test_ResponseMessageAssertion)
gen_test_InvalidStatusCodesAssertion_HTTPStatusAssertion = Generalization(general=HTTPStatusAssertion, specific=test_InvalidStatusCodesAssertion)
gen_test_ValidStatusCodesAssertion_HTTPStatusAssertion = Generalization(general=HTTPStatusAssertion, specific=test_ValidStatusCodesAssertion)
gen_test_Basic_Authorization = Generalization(general=Authorization, specific=test_Basic)
gen_test_OAuth2_Authorization = Generalization(general=Authorization, specific=test_OAuth2)
gen_test_PropertyTransfer_TestStep = Generalization(general=TestStep, specific=test_PropertyTransfer)
gen_test_HeaderExistsAssertion_HeaderAssertion = Generalization(general=HeaderAssertion, specific=test_HeaderExistsAssertion)
gen_test_HTTPStatusAssertion_Assertion = Generalization(general=Assertion, specific=test_HTTPStatusAssertion)
gen_test_InputProperty_Property = Generalization(general=Property_, specific=test_InputProperty)
gen_test_OutputProperty_Property = Generalization(general=Property_, specific=test_OutputProperty)
gen_test_HeaderProperty_OutputProperty = Generalization(general=OutputProperty, specific=test_HeaderProperty)
gen_test_ParameterProperty_InputProperty = Generalization(general=InputProperty, specific=test_ParameterProperty)
gen_test_ResponseProperty_OutputProperty = Generalization(general=OutputProperty, specific=test_ResponseProperty)

# Domain Model
domain_model = DomainModel(
    name="test",
    types={test_TestSuite, NamedElement, test_TestCase, test_Parameter, test_Assertion, test_Authorization, test_NamedElement, test_TestStep, test_APIRequest, TestStep, test_ResponseMessageContainsAssertion, ResponseMessageAssertion, test_ResponseMessageEqualsAssertion, test_SchemaComplianceAssertion, ComplianceAssertion, test_SLAAssertion, PerformanceAssertion, test_HeaderAssertion, test_HeaderEqualsAssertion, HeaderAssertion, test_ComplianceAssertion, Assertion, test_PerformanceAssertion, test_ResponseMessageAssertion, test_InvalidStatusCodesAssertion, HTTPStatusAssertion, test_ValidStatusCodesAssertion, test_Basic, Authorization, test_OAuth2, test_PropertyTransfer, test_Property, test_HeaderExistsAssertion, test_HTTPStatusAssertion, test_InputProperty, Property_, test_OutputProperty, test_HeaderProperty, test_ParameterProperty, InputProperty, test_ResponseProperty, OutputProperty, ParameterLocation, SchemeType, HTTPMethod, PathLanguage},
    associations={testCases0, parameters3, assertions4, authorization6, testSteps1, source8, target9, request14, parameter12},
    generalizations={gen_test_TestSuite_NamedElement, gen_test_TestCase_NamedElement, gen_test_TestStep_NamedElement, gen_test_APIRequest_TestStep, gen_test_ResponseMessageContainsAssertion_ResponseMessageAssertion, gen_test_ResponseMessageEqualsAssertion_ResponseMessageAssertion, gen_test_SchemaComplianceAssertion_ComplianceAssertion, gen_test_SLAAssertion_PerformanceAssertion, gen_test_HeaderAssertion_Assertion, gen_test_HeaderEqualsAssertion_HeaderAssertion, gen_test_ComplianceAssertion_Assertion, gen_test_PerformanceAssertion_Assertion, gen_test_ResponseMessageAssertion_Assertion, gen_test_InvalidStatusCodesAssertion_HTTPStatusAssertion, gen_test_ValidStatusCodesAssertion_HTTPStatusAssertion, gen_test_Basic_Authorization, gen_test_OAuth2_Authorization, gen_test_PropertyTransfer_TestStep, gen_test_HeaderExistsAssertion_HeaderAssertion, gen_test_HTTPStatusAssertion_Assertion, gen_test_InputProperty_Property, gen_test_OutputProperty_Property, gen_test_HeaderProperty_OutputProperty, gen_test_ParameterProperty_InputProperty, gen_test_ResponseProperty_OutputProperty},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)