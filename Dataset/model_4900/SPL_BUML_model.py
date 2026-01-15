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
SIPMethod: Enumeration = Enumeration(
    name="SIPMethod",
    literals={
            EnumerationLiteral(name="ACK"),
			EnumerationLiteral(name="BYE"),
			EnumerationLiteral(name="CANCEL"),
			EnumerationLiteral(name="INVITE"),
			EnumerationLiteral(name="NOTIFY"),
			EnumerationLiteral(name="OPTIONS"),
			EnumerationLiteral(name="REACK"),
			EnumerationLiteral(name="REGISTER"),
			EnumerationLiteral(name="REINVITE"),
			EnumerationLiteral(name="REREGISTER"),
			EnumerationLiteral(name="RESUBSCRIBE"),
			EnumerationLiteral(name="SUBSCRIBE")
    }
)

ControlMethod: Enumeration = Enumeration(
    name="ControlMethod",
    literals={
            EnumerationLiteral(name="deploy"),
			EnumerationLiteral(name="undeploy"),
			EnumerationLiteral(name="uninvite"),
			EnumerationLiteral(name="unregister"),
			EnumerationLiteral(name="unsubscribe")
    }
)

PrimitiveType: Enumeration = Enumeration(
    name="PrimitiveType",
    literals={
            EnumerationLiteral(name="void"),
			EnumerationLiteral(name="bool"),
			EnumerationLiteral(name="int"),
			EnumerationLiteral(name="request"),
			EnumerationLiteral(name="response"),
			EnumerationLiteral(name="string"),
			EnumerationLiteral(name="time"),
			EnumerationLiteral(name="uri")
    }
)

Modifier: Enumeration = Enumeration(
    name="Modifier",
    literals={
            EnumerationLiteral(name="LIFO"),
			EnumerationLiteral(name="FIFO")
    }
)

FunctionLocation: Enumeration = Enumeration(
    name="FunctionLocation",
    literals={
            EnumerationLiteral(name="remote"),
			EnumerationLiteral(name="local")
    }
)

SIPHeader: Enumeration = Enumeration(
    name="SIPHeader",
    literals={
            EnumerationLiteral(name="CALL_ID"),
			EnumerationLiteral(name="CONTACT"),
			EnumerationLiteral(name="CSEQ"),
			EnumerationLiteral(name="EVENT"),
			EnumerationLiteral(name="FROM"),
			EnumerationLiteral(name="MAX_FORWARDS"),
			EnumerationLiteral(name="SUBSCRIPTION_STATE"),
			EnumerationLiteral(name="TO"),
			EnumerationLiteral(name="VIA")
    }
)

Direction: Enumeration = Enumeration(
    name="Direction",
    literals={
            EnumerationLiteral(name="out"),
			EnumerationLiteral(name="inout"),
			EnumerationLiteral(name="in")
    }
)

RedirectionErrorKind: Enumeration = Enumeration(
    name="RedirectionErrorKind",
    literals={
            EnumerationLiteral(name="ALTERNATIVE_SERVICE"),
			EnumerationLiteral(name="MOVED_PERMANENTLY"),
			EnumerationLiteral(name="MOVED_TEMPORARILY"),
			EnumerationLiteral(name="MULTIPLE_CHOICES"),
			EnumerationLiteral(name="USE_PROXY")
    }
)

ServerErrorKind: Enumeration = Enumeration(
    name="ServerErrorKind",
    literals={
            EnumerationLiteral(name="BAD_GATEWAY"),
			EnumerationLiteral(name="MESSAGE_TOO_LARGE"),
			EnumerationLiteral(name="NOT_IMPLEMENTED"),
			EnumerationLiteral(name="SERVER_INTERNAL_ERROR"),
			EnumerationLiteral(name="SERVER_TIMEOUT"),
			EnumerationLiteral(name="SERVICE_UNAVAILABLE"),
			EnumerationLiteral(name="VERSION_NOT_SUPPORTED")
    }
)

SuccessKind: Enumeration = Enumeration(
    name="SuccessKind",
    literals={
            EnumerationLiteral(name="OK"),
			EnumerationLiteral(name="ACCEPTED")
    }
)

ClientErrorKind: Enumeration = Enumeration(
    name="ClientErrorKind",
    literals={
            EnumerationLiteral(name="ADDRESS_INCOMPLETE"),
			EnumerationLiteral(name="AMBIGUOUS"),
			EnumerationLiteral(name="BAD_EXTENSION"),
			EnumerationLiteral(name="BAD_REQUEST"),
			EnumerationLiteral(name="BUSY_HERE"),
			EnumerationLiteral(name="CALL_OR_TRANSACTION_DOES_NOT_EXIST"),
			EnumerationLiteral(name="EXTENSION_REQUIRED"),
			EnumerationLiteral(name="FORBIDDEN"),
			EnumerationLiteral(name="GONE"),
			EnumerationLiteral(name="INTERVAL_TOO_BRIEF"),
			EnumerationLiteral(name="LOOP_DETECTED"),
			EnumerationLiteral(name="METHOD_NOT_ALLOWED"),
			EnumerationLiteral(name="NOT_ACCEPTABLE_HERE"),
			EnumerationLiteral(name="NOT_ACCEPTABLE"),
			EnumerationLiteral(name="NOT_FOUND"),
			EnumerationLiteral(name="PAYMENT_REQUIRED"),
			EnumerationLiteral(name="PROXY_AUTHENTICATION_REQUIRED"),
			EnumerationLiteral(name="REQUESTURI_TOO_LONG"),
			EnumerationLiteral(name="REQUEST_ENTITY_TOO_LARGE"),
			EnumerationLiteral(name="REQUEST_PENDING"),
			EnumerationLiteral(name="REQUEST_TERMINATED"),
			EnumerationLiteral(name="REQUEST_TIMEOUT"),
			EnumerationLiteral(name="TEMPORARILY_UNAVAILABLE"),
			EnumerationLiteral(name="TOO_MANY_HOPS"),
			EnumerationLiteral(name="UNAUTHORIZED"),
			EnumerationLiteral(name="UNDECIPHERABLE"),
			EnumerationLiteral(name="UNSUPPORTED_MEDIA_TYPE"),
			EnumerationLiteral(name="UNSUPPORTED_URI_SCHEME")
    }
)

GlobalErrorKind: Enumeration = Enumeration(
    name="GlobalErrorKind",
    literals={
            EnumerationLiteral(name="DOES_NOT_EXIST_ANYWHERE"),
			EnumerationLiteral(name="NOT_ACCEPTABLE"),
			EnumerationLiteral(name="BUSY_EVERYWHERE"),
			EnumerationLiteral(name="DECLINE")
    }
)

# Classes
SPL_Declaration = Class(name="SPL::Declaration", is_abstract=True)
SPL_Session = Class(name="SPL::Session", is_abstract=True)
SPL_Registration = Class(name="SPL::Registration")
Session = Class(name="Session")
SPL_Dialog = Class(name="SPL::Dialog")
SPL_Method = Class(name="SPL::Method")
SPL_LocatedElement = Class(name="SPL::LocatedElement", is_abstract=True)
SPL_Program = Class(name="SPL::Program")
LocatedElement = Class(name="LocatedElement")
SPL_Service = Class(name="SPL::Service")
VariableDeclaration = Class(name="VariableDeclaration")
SPL_SIPMethodName = Class(name="SPL::SIPMethodName")
MethodName = Class(name="MethodName")
SPL_ControlMethodName = Class(name="SPL::ControlMethodName")
SPL_DefaultBranch = Class(name="SPL::DefaultBranch")
Branch = Class(name="Branch")
SPL_NamedBranch = Class(name="SPL::NamedBranch")
SPL_SimpleType = Class(name="SPL::SimpleType")
TypeExpression = Class(name="TypeExpression")
SPL_Event = Class(name="SPL::Event")
SPL_SequenceType = Class(name="SPL::SequenceType")
SPL_TypeExpression = Class(name="SPL::TypeExpression", is_abstract=True)
SPL_MethodName = Class(name="SPL::MethodName", is_abstract=True)
SPL_Argument = Class(name="SPL::Argument")
SPL_Statement = Class(name="SPL::Statement", is_abstract=True)
SPL_Branch = Class(name="SPL::Branch")
SPL_RemoteFunctionDeclaration = Class(name="SPL::RemoteFunctionDeclaration")
FunctionDeclaration = Class(name="FunctionDeclaration")
SPL_LocalFunctionDeclaration = Class(name="SPL::LocalFunctionDeclaration")
SPL_DefinedType = Class(name="SPL::DefinedType")
SPL_VariableDeclaration = Class(name="SPL::VariableDeclaration")
Declaration = Class(name="Declaration")
SPL_Expression = Class(name="SPL::Expression", is_abstract=True)
SPL_DeclarationStat = Class(name="SPL::DeclarationStat")
SPL_FunctionDeclaration = Class(name="SPL::FunctionDeclaration", is_abstract=True)
SPL_ReturnStat = Class(name="SPL::ReturnStat")
SPL_IfStat = Class(name="SPL::IfStat")
SPL_StructureDeclaration = Class(name="SPL::StructureDeclaration")
SPL_WhenStat = Class(name="SPL::WhenStat")
SPL_Variable = Class(name="SPL::Variable")
SPL_StructureProperty = Class(name="SPL::StructureProperty")
SPL_FunctionCall = Class(name="SPL::FunctionCall")
SPL_CompoundStat = Class(name="SPL::CompoundStat")
Statement = Class(name="Statement")
SPL_SetStat = Class(name="SPL::SetStat")
SPL_Place = Class(name="SPL::Place", is_abstract=True)
SPL_FunctionCallStat = Class(name="SPL::FunctionCallStat")
SPL_ContinueStat = Class(name="SPL::ContinueStat")
SPL_BreakStat = Class(name="SPL::BreakStat")
SPL_PushStat = Class(name="SPL::PushStat")
SPL_Constant = Class(name="SPL::Constant", is_abstract=True)
SPL_SelectMember = Class(name="SPL::SelectMember", is_abstract=True)
SPL_WhenHeader = Class(name="SPL::WhenHeader")
SPL_ForeachStat = Class(name="SPL::ForeachStat")
SPL_SelectStat = Class(name="SPL::SelectStat")
SPL_SelectCase = Class(name="SPL::SelectCase")
SPL_SelectDefault = Class(name="SPL::SelectDefault")
SPL_WithExp = Class(name="SPL::WithExp")
SPL_MessageField = Class(name="SPL::MessageField", is_abstract=True)
SPL_BlockExp = Class(name="SPL::BlockExp")
SPL_ReasonExp = Class(name="SPL::ReasonExp")
SPL_BODYExp = Class(name="SPL::BODYExp")
SPL_RequestURIExp = Class(name="SPL::RequestURIExp")
SPL_PopExp = Class(name="SPL::PopExp")
SPL_FunctionCallExp = Class(name="SPL::FunctionCallExp")
SelectMember = Class(name="SelectMember")
SPL_ConstantExp = Class(name="SPL::ConstantExp")
Expression = Class(name="Expression")
SPL_OperatorExp = Class(name="SPL::OperatorExp")
SPL_ForwardExp = Class(name="SPL::ForwardExp")
SPL_ReasonMessageField = Class(name="SPL::ReasonMessageField")
MessageField = Class(name="MessageField")
SPL_HeadedMessageField = Class(name="SPL::HeadedMessageField")
SPL_BooleanConstant = Class(name="SPL::BooleanConstant")
Constant = Class(name="Constant")
SPL_IntegerConstant = Class(name="SPL::IntegerConstant")
SPL_StringConstant = Class(name="SPL::StringConstant")
SPL_URIConstant = Class(name="SPL::URIConstant")
SPL_SequenceConstant = Class(name="SPL::SequenceConstant")
SPL_SIPHeaderPlace = Class(name="SPL::SIPHeaderPlace")
Place = Class(name="Place")
SPL_VariablePlace = Class(name="SPL::VariablePlace", is_abstract=True)
SPL_PropertyCallPlace = Class(name="SPL::PropertyCallPlace")
VariablePlace = Class(name="VariablePlace")
SPL_ResponseConstant = Class(name="SPL::ResponseConstant")
SPL_Response = Class(name="SPL::Response", is_abstract=True)
SPL_SuccessResponse = Class(name="SPL::SuccessResponse")
Response = Class(name="Response")
SPL_ErrorResponse = Class(name="SPL::ErrorResponse")
SPL_ClientErrorResponse = Class(name="SPL::ClientErrorResponse")
ErrorResponse = Class(name="ErrorResponse")
SPL_GlobalErrorResponse = Class(name="SPL::GlobalErrorResponse")
SPL_RedirectionErrorResponse = Class(name="SPL::RedirectionErrorResponse")
SPL_ServerErrorResponse = Class(name="SPL::ServerErrorResponse")

# SPL_Declaration class attributes and methods
SPL_Declaration_name: Property = Property(name="name", type=StringType)
SPL_Declaration.attributes={SPL_Declaration_name}

# SPL_Session class attributes and methods

# SPL_Registration class attributes and methods

# Session class attributes and methods

# SPL_Dialog class attributes and methods

# SPL_Method class attributes and methods
SPL_Method_direction: Property = Property(name="direction", type=StringType)
SPL_Method.attributes={SPL_Method_direction}

# SPL_LocatedElement class attributes and methods
SPL_LocatedElement_location: Property = Property(name="location", type=StringType)
SPL_LocatedElement_commentsBefore: Property = Property(name="commentsBefore", type=StringType)
SPL_LocatedElement_commentsAfter: Property = Property(name="commentsAfter", type=StringType)
SPL_LocatedElement.attributes={SPL_LocatedElement_commentsBefore, SPL_LocatedElement_location, SPL_LocatedElement_commentsAfter}

# SPL_Program class attributes and methods

# LocatedElement class attributes and methods

# SPL_Service class attributes and methods
SPL_Service_name: Property = Property(name="name", type=StringType)
SPL_Service.attributes={SPL_Service_name}

# VariableDeclaration class attributes and methods

# SPL_SIPMethodName class attributes and methods
SPL_SIPMethodName_name: Property = Property(name="name", type=StringType)
SPL_SIPMethodName.attributes={SPL_SIPMethodName_name}

# MethodName class attributes and methods

# SPL_ControlMethodName class attributes and methods
SPL_ControlMethodName_name: Property = Property(name="name", type=StringType)
SPL_ControlMethodName.attributes={SPL_ControlMethodName_name}

# SPL_DefaultBranch class attributes and methods

# Branch class attributes and methods

# SPL_NamedBranch class attributes and methods
SPL_NamedBranch_name: Property = Property(name="name", type=StringType)
SPL_NamedBranch.attributes={SPL_NamedBranch_name}

# SPL_SimpleType class attributes and methods
SPL_SimpleType_type: Property = Property(name="type", type=StringType)
SPL_SimpleType.attributes={SPL_SimpleType_type}

# TypeExpression class attributes and methods

# SPL_Event class attributes and methods
SPL_Event_eventId: Property = Property(name="eventId", type=StringType)
SPL_Event.attributes={SPL_Event_eventId}

# SPL_SequenceType class attributes and methods
SPL_SequenceType_modifier: Property = Property(name="modifier", type=StringType)
SPL_SequenceType_type: Property = Property(name="type", type=StringType)
SPL_SequenceType_size: Property = Property(name="size", type=IntegerType)
SPL_SequenceType.attributes={SPL_SequenceType_size, SPL_SequenceType_modifier, SPL_SequenceType_type}

# SPL_TypeExpression class attributes and methods

# SPL_MethodName class attributes and methods

# SPL_Argument class attributes and methods

# SPL_Statement class attributes and methods

# SPL_Branch class attributes and methods

# SPL_RemoteFunctionDeclaration class attributes and methods
SPL_RemoteFunctionDeclaration_functionLocation: Property = Property(name="functionLocation", type=StringType)
SPL_RemoteFunctionDeclaration.attributes={SPL_RemoteFunctionDeclaration_functionLocation}

# FunctionDeclaration class attributes and methods

# SPL_LocalFunctionDeclaration class attributes and methods

# SPL_DefinedType class attributes and methods
SPL_DefinedType_typeName: Property = Property(name="typeName", type=StringType)
SPL_DefinedType.attributes={SPL_DefinedType_typeName}

# SPL_VariableDeclaration class attributes and methods

# Declaration class attributes and methods

# SPL_Expression class attributes and methods

# SPL_DeclarationStat class attributes and methods

# SPL_FunctionDeclaration class attributes and methods

# SPL_ReturnStat class attributes and methods

# SPL_IfStat class attributes and methods

# SPL_StructureDeclaration class attributes and methods

# SPL_WhenStat class attributes and methods

# SPL_Variable class attributes and methods

# SPL_StructureProperty class attributes and methods
SPL_StructureProperty_name: Property = Property(name="name", type=StringType)
SPL_StructureProperty.attributes={SPL_StructureProperty_name}

# SPL_FunctionCall class attributes and methods

# SPL_CompoundStat class attributes and methods

# Statement class attributes and methods

# SPL_SetStat class attributes and methods

# SPL_Place class attributes and methods

# SPL_FunctionCallStat class attributes and methods

# SPL_ContinueStat class attributes and methods

# SPL_BreakStat class attributes and methods

# SPL_PushStat class attributes and methods

# SPL_Constant class attributes and methods

# SPL_SelectMember class attributes and methods

# SPL_WhenHeader class attributes and methods
SPL_WhenHeader_headerId: Property = Property(name="headerId", type=StringType)
SPL_WhenHeader.attributes={SPL_WhenHeader_headerId}

# SPL_ForeachStat class attributes and methods
SPL_ForeachStat_iteratorName: Property = Property(name="iteratorName", type=StringType)
SPL_ForeachStat.attributes={SPL_ForeachStat_iteratorName}

# SPL_SelectStat class attributes and methods

# SPL_SelectCase class attributes and methods

# SPL_SelectDefault class attributes and methods

# SPL_WithExp class attributes and methods

# SPL_MessageField class attributes and methods

# SPL_BlockExp class attributes and methods

# SPL_ReasonExp class attributes and methods

# SPL_BODYExp class attributes and methods

# SPL_RequestURIExp class attributes and methods

# SPL_PopExp class attributes and methods

# SPL_FunctionCallExp class attributes and methods

# SelectMember class attributes and methods

# SPL_ConstantExp class attributes and methods

# Expression class attributes and methods

# SPL_OperatorExp class attributes and methods
SPL_OperatorExp_opName: Property = Property(name="opName", type=StringType)
SPL_OperatorExp.attributes={SPL_OperatorExp_opName}

# SPL_ForwardExp class attributes and methods
SPL_ForwardExp_isParallel: Property = Property(name="isParallel", type=BooleanType)
SPL_ForwardExp.attributes={SPL_ForwardExp_isParallel}

# SPL_ReasonMessageField class attributes and methods

# MessageField class attributes and methods

# SPL_HeadedMessageField class attributes and methods
SPL_HeadedMessageField_headerId: Property = Property(name="headerId", type=StringType)
SPL_HeadedMessageField.attributes={SPL_HeadedMessageField_headerId}

# SPL_BooleanConstant class attributes and methods
SPL_BooleanConstant_value: Property = Property(name="value", type=BooleanType)
SPL_BooleanConstant.attributes={SPL_BooleanConstant_value}

# Constant class attributes and methods

# SPL_IntegerConstant class attributes and methods
SPL_IntegerConstant_value: Property = Property(name="value", type=IntegerType)
SPL_IntegerConstant.attributes={SPL_IntegerConstant_value}

# SPL_StringConstant class attributes and methods
SPL_StringConstant_value: Property = Property(name="value", type=StringType)
SPL_StringConstant.attributes={SPL_StringConstant_value}

# SPL_URIConstant class attributes and methods
SPL_URIConstant_uri: Property = Property(name="uri", type=StringType)
SPL_URIConstant.attributes={SPL_URIConstant_uri}

# SPL_SequenceConstant class attributes and methods

# SPL_SIPHeaderPlace class attributes and methods
SPL_SIPHeaderPlace_header: Property = Property(name="header", type=StringType)
SPL_SIPHeaderPlace.attributes={SPL_SIPHeaderPlace_header}

# Place class attributes and methods

# SPL_VariablePlace class attributes and methods

# SPL_PropertyCallPlace class attributes and methods
SPL_PropertyCallPlace_propName: Property = Property(name="propName", type=StringType)
SPL_PropertyCallPlace.attributes={SPL_PropertyCallPlace_propName}

# VariablePlace class attributes and methods

# SPL_ResponseConstant class attributes and methods

# SPL_Response class attributes and methods

# SPL_SuccessResponse class attributes and methods
SPL_SuccessResponse_successKind: Property = Property(name="successKind", type=StringType)
SPL_SuccessResponse.attributes={SPL_SuccessResponse_successKind}

# Response class attributes and methods

# SPL_ErrorResponse class attributes and methods

# SPL_ClientErrorResponse class attributes and methods
SPL_ClientErrorResponse_errorKind: Property = Property(name="errorKind", type=StringType)
SPL_ClientErrorResponse.attributes={SPL_ClientErrorResponse_errorKind}

# ErrorResponse class attributes and methods

# SPL_GlobalErrorResponse class attributes and methods
SPL_GlobalErrorResponse_errorKind: Property = Property(name="errorKind", type=StringType)
SPL_GlobalErrorResponse.attributes={SPL_GlobalErrorResponse_errorKind}

# SPL_RedirectionErrorResponse class attributes and methods
SPL_RedirectionErrorResponse_errorKind: Property = Property(name="errorKind", type=StringType)
SPL_RedirectionErrorResponse.attributes={SPL_RedirectionErrorResponse_errorKind}

# SPL_ServerErrorResponse class attributes and methods
SPL_ServerErrorResponse_errorKind: Property = Property(name="errorKind", type=StringType)
SPL_ServerErrorResponse.attributes={SPL_ServerErrorResponse_errorKind}

# Relationships
declarations1: BinaryAssociation = BinaryAssociation(
    name="declarations1",
    ends={
        Property(name="SPL_Declaration", type=SPL_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_Service2", type=SPL_Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sessions3: BinaryAssociation = BinaryAssociation(
    name="sessions3",
    ends={
        Property(name="SPL_Session", type=SPL_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_Service4", type=SPL_Session, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declarations5: BinaryAssociation = BinaryAssociation(
    name="declarations5",
    ends={
        Property(name="SPL_Declaration6", type=SPL_Registration, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_Registration", type=SPL_Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sessions7: BinaryAssociation = BinaryAssociation(
    name="sessions7",
    ends={
        Property(name="SPL_Session9", type=SPL_Registration, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_Registration8", type=SPL_Session, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declarations10: BinaryAssociation = BinaryAssociation(
    name="declarations10",
    ends={
        Property(name="SPL_Declaration11", type=SPL_Dialog, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_Dialog", type=SPL_Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods12: BinaryAssociation = BinaryAssociation(
    name="methods12",
    ends={
        Property(name="SPL_Method", type=SPL_Dialog, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_Dialog13", type=SPL_Method, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
service0: BinaryAssociation = BinaryAssociation(
    name="service0",
    ends={
        Property(name="SPL_Service", type=SPL_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_Program", type=SPL_Service, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements29: BinaryAssociation = BinaryAssociation(
    name="statements29",
    ends={
        Property(name="SPL_Statement31", type=SPL_Branch, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_Branch30", type=SPL_Statement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
declarations14: BinaryAssociation = BinaryAssociation(
    name="declarations14",
    ends={
        Property(name="SPL_Declaration15", type=SPL_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_Event", type=SPL_Declaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods16: BinaryAssociation = BinaryAssociation(
    name="methods16",
    ends={
        Property(name="SPL_Method18", type=SPL_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_Event17", type=SPL_Method, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
type19: BinaryAssociation = BinaryAssociation(
    name="type19",
    ends={
        Property(name="SPL_TypeExpression", type=SPL_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_Method20", type=SPL_TypeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
methodName21: BinaryAssociation = BinaryAssociation(
    name="methodName21",
    ends={
        Property(name="SPL_MethodName", type=SPL_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_Method22", type=SPL_MethodName, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments23: BinaryAssociation = BinaryAssociation(
    name="arguments23",
    ends={
        Property(name="SPL_Argument", type=SPL_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_Method24", type=SPL_Argument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements25: BinaryAssociation = BinaryAssociation(
    name="statements25",
    ends={
        Property(name="SPL_Statement", type=SPL_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_Method26", type=SPL_Statement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
branches27: BinaryAssociation = BinaryAssociation(
    name="branches27",
    ends={
        Property(name="SPL_Branch", type=SPL_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_Method28", type=SPL_Branch, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
returnType36: BinaryAssociation = BinaryAssociation(
    name="returnType36",
    ends={
        Property(name="SPL_TypeExpression37", type=SPL_FunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_FunctionDeclaration", type=SPL_TypeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
arguments38: BinaryAssociation = BinaryAssociation(
    name="arguments38",
    ends={
        Property(name="SPL_Argument40", type=SPL_FunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_FunctionDeclaration39", type=SPL_Argument, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements41: BinaryAssociation = BinaryAssociation(
    name="statements41",
    ends={
        Property(name="SPL_Statement42", type=SPL_LocalFunctionDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_LocalFunctionDeclaration", type=SPL_Statement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
type32: BinaryAssociation = BinaryAssociation(
    name="type32",
    ends={
        Property(name="SPL_TypeExpression33", type=SPL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_VariableDeclaration", type=SPL_TypeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initExp34: BinaryAssociation = BinaryAssociation(
    name="initExp34",
    ends={
        Property(name="SPL_Expression", type=SPL_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_VariableDeclaration35", type=SPL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaration58: BinaryAssociation = BinaryAssociation(
    name="declaration58",
    ends={
        Property(name="SPL_Declaration59", type=SPL_DeclarationStat, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_DeclarationStat", type=SPL_Declaration, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnedValue60: BinaryAssociation = BinaryAssociation(
    name="returnedValue60",
    ends={
        Property(name="SPL_Expression61", type=SPL_ReturnStat, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_ReturnStat", type=SPL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
branch62: BinaryAssociation = BinaryAssociation(
    name="branch62",
    ends={
        Property(name="SPL_NamedBranch", type=SPL_ReturnStat, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_ReturnStat63", type=SPL_NamedBranch, multiplicity=Multiplicity(0, 1))
    }
)
condition64: BinaryAssociation = BinaryAssociation(
    name="condition64",
    ends={
        Property(name="SPL_Expression65", type=SPL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_IfStat", type=SPL_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenStatements66: BinaryAssociation = BinaryAssociation(
    name="thenStatements66",
    ends={
        Property(name="SPL_Statement68", type=SPL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_IfStat67", type=SPL_Statement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
elseStatements69: BinaryAssociation = BinaryAssociation(
    name="elseStatements69",
    ends={
        Property(name="SPL_Statement71", type=SPL_IfStat, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_IfStat70", type=SPL_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties43: BinaryAssociation = BinaryAssociation(
    name="properties43",
    ends={
        Property(name="SPL_Argument44", type=SPL_StructureDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_StructureDeclaration", type=SPL_Argument, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
type45: BinaryAssociation = BinaryAssociation(
    name="type45",
    ends={
        Property(name="SPL_TypeExpression46", type=SPL_StructureProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_StructureProperty", type=SPL_TypeExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
function47: BinaryAssociation = BinaryAssociation(
    name="function47",
    ends={
        Property(name="SPL_FunctionDeclaration48", type=SPL_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_FunctionCall", type=SPL_FunctionDeclaration, multiplicity=Multiplicity(1, 1))
    }
)
parameters49: BinaryAssociation = BinaryAssociation(
    name="parameters49",
    ends={
        Property(name="SPL_Expression51", type=SPL_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_FunctionCall50", type=SPL_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements52: BinaryAssociation = BinaryAssociation(
    name="statements52",
    ends={
        Property(name="SPL_Statement53", type=SPL_CompoundStat, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_CompoundStat", type=SPL_Statement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
target54: BinaryAssociation = BinaryAssociation(
    name="target54",
    ends={
        Property(name="SPL_Place", type=SPL_SetStat, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_SetStat", type=SPL_Place, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
setValue55: BinaryAssociation = BinaryAssociation(
    name="setValue55",
    ends={
        Property(name="SPL_Expression57", type=SPL_SetStat, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_SetStat56", type=SPL_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
selectDefault90: BinaryAssociation = BinaryAssociation(
    name="selectDefault90",
    ends={
        Property(name="SPL_SelectStat91", type=SPL_SelectDefault, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="SPL_SelectDefault", type=SPL_SelectStat, multiplicity=Multiplicity(1, 1))
    }
)
functionCall92: BinaryAssociation = BinaryAssociation(
    name="functionCall92",
    ends={
        Property(name="SPL_FunctionCall93", type=SPL_FunctionCallStat, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_FunctionCallStat", type=SPL_FunctionCall, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target94: BinaryAssociation = BinaryAssociation(
    name="target94",
    ends={
        Property(name="SPL_Place95", type=SPL_PushStat, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_PushStat", type=SPL_Place, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
pushedValue96: BinaryAssociation = BinaryAssociation(
    name="pushedValue96",
    ends={
        Property(name="SPL_Expression98", type=SPL_PushStat, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_PushStat97", type=SPL_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value99: BinaryAssociation = BinaryAssociation(
    name="value99",
    ends={
        Property(name="SPL_Constant", type=SPL_WhenHeader, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_WhenHeader100", type=SPL_Constant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements101: BinaryAssociation = BinaryAssociation(
    name="statements101",
    ends={
        Property(name="SPL_Statement102", type=SPL_SelectMember, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_SelectMember", type=SPL_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
idExp72: BinaryAssociation = BinaryAssociation(
    name="idExp72",
    ends={
        Property(name="SPL_Variable", type=SPL_WhenStat, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_WhenStat", type=SPL_Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
whenHeaders73: BinaryAssociation = BinaryAssociation(
    name="whenHeaders73",
    ends={
        Property(name="SPL_WhenHeader", type=SPL_WhenStat, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_WhenStat74", type=SPL_WhenHeader, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
statements75: BinaryAssociation = BinaryAssociation(
    name="statements75",
    ends={
        Property(name="SPL_Statement77", type=SPL_WhenStat, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_WhenStat76", type=SPL_Statement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
elseStatements78: BinaryAssociation = BinaryAssociation(
    name="elseStatements78",
    ends={
        Property(name="SPL_Statement80", type=SPL_WhenStat, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_WhenStat79", type=SPL_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sequenceExp81: BinaryAssociation = BinaryAssociation(
    name="sequenceExp81",
    ends={
        Property(name="SPL_Expression82", type=SPL_ForeachStat, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_ForeachStat", type=SPL_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements83: BinaryAssociation = BinaryAssociation(
    name="statements83",
    ends={
        Property(name="SPL_Statement85", type=SPL_ForeachStat, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_ForeachStat84", type=SPL_Statement, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
matchedExp86: BinaryAssociation = BinaryAssociation(
    name="matchedExp86",
    ends={
        Property(name="SPL_Expression87", type=SPL_SelectStat, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_SelectStat", type=SPL_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
selectCases88: BinaryAssociation = BinaryAssociation(
    name="selectCases88",
    ends={
        Property(name="SPL_SelectCase", type=SPL_SelectStat, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_SelectStat89", type=SPL_SelectCase, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exp115: BinaryAssociation = BinaryAssociation(
    name="exp115",
    ends={
        Property(name="SPL_Expression116", type=SPL_WithExp, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_WithExp", type=SPL_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
msgFields117: BinaryAssociation = BinaryAssociation(
    name="msgFields117",
    ends={
        Property(name="SPL_MessageField", type=SPL_WithExp, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_WithExp118", type=SPL_MessageField, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
exp119: BinaryAssociation = BinaryAssociation(
    name="exp119",
    ends={
        Property(name="SPL_Expression120", type=SPL_BlockExp, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_BlockExp", type=SPL_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source121: BinaryAssociation = BinaryAssociation(
    name="source121",
    ends={
        Property(name="SPL_Place122", type=SPL_PopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_PopExp", type=SPL_Place, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
functionCall123: BinaryAssociation = BinaryAssociation(
    name="functionCall123",
    ends={
        Property(name="SPL_FunctionCall124", type=SPL_FunctionCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_FunctionCallExp", type=SPL_FunctionCall, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
values103: BinaryAssociation = BinaryAssociation(
    name="values103",
    ends={
        Property(name="SPL_Constant105", type=SPL_SelectCase, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_SelectCase104", type=SPL_Constant, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
value106: BinaryAssociation = BinaryAssociation(
    name="value106",
    ends={
        Property(name="SPL_Constant107", type=SPL_ConstantExp, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_ConstantExp", type=SPL_Constant, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftExp108: BinaryAssociation = BinaryAssociation(
    name="leftExp108",
    ends={
        Property(name="SPL_Expression109", type=SPL_OperatorExp, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_OperatorExp", type=SPL_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightExp110: BinaryAssociation = BinaryAssociation(
    name="rightExp110",
    ends={
        Property(name="SPL_Expression112", type=SPL_OperatorExp, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_OperatorExp111", type=SPL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp113: BinaryAssociation = BinaryAssociation(
    name="exp113",
    ends={
        Property(name="SPL_Expression114", type=SPL_ForwardExp, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_ForwardExp", type=SPL_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp129: BinaryAssociation = BinaryAssociation(
    name="exp129",
    ends={
        Property(name="SPL_Expression131", type=SPL_MessageField, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_MessageField130", type=SPL_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
values132: BinaryAssociation = BinaryAssociation(
    name="values132",
    ends={
        Property(name="SPL_Constant133", type=SPL_SequenceConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_SequenceConstant", type=SPL_Constant, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source125: BinaryAssociation = BinaryAssociation(
    name="source125",
    ends={
        Property(name="SPL_VariablePlace", type=SPL_PropertyCallPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_PropertyCallPlace", type=SPL_VariablePlace, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source126: BinaryAssociation = BinaryAssociation(
    name="source126",
    ends={
        Property(name="SPL_Declaration128", type=SPL_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_Variable127", type=SPL_Declaration, multiplicity=Multiplicity(1, 1))
    }
)
response134: BinaryAssociation = BinaryAssociation(
    name="response134",
    ends={
        Property(name="SPL_Response", type=SPL_ResponseConstant, multiplicity=Multiplicity(1, 1)),
        Property(name="SPL_ResponseConstant", type=SPL_Response, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_SPL_Session_LocatedElement = Generalization(general=LocatedElement, specific=SPL_Session)
gen_SPL_Registration_Session = Generalization(general=Session, specific=SPL_Registration)
gen_SPL_Dialog_Session = Generalization(general=Session, specific=SPL_Dialog)
gen_SPL_Program_LocatedElement = Generalization(general=LocatedElement, specific=SPL_Program)
gen_SPL_Argument_VariableDeclaration = Generalization(general=VariableDeclaration, specific=SPL_Argument)
gen_SPL_Service_LocatedElement = Generalization(general=LocatedElement, specific=SPL_Service)
gen_SPL_MethodName_LocatedElement = Generalization(general=LocatedElement, specific=SPL_MethodName)
gen_SPL_SIPMethodName_MethodName = Generalization(general=MethodName, specific=SPL_SIPMethodName)
gen_SPL_ControlMethodName_MethodName = Generalization(general=MethodName, specific=SPL_ControlMethodName)
gen_SPL_Branch_LocatedElement = Generalization(general=LocatedElement, specific=SPL_Branch)
gen_SPL_DefaultBranch_Branch = Generalization(general=Branch, specific=SPL_DefaultBranch)
gen_SPL_NamedBranch_Branch = Generalization(general=Branch, specific=SPL_NamedBranch)
gen_SPL_TypeExpression_LocatedElement = Generalization(general=LocatedElement, specific=SPL_TypeExpression)
gen_SPL_SimpleType_TypeExpression = Generalization(general=TypeExpression, specific=SPL_SimpleType)
gen_SPL_Event_Session = Generalization(general=Session, specific=SPL_Event)
gen_SPL_SequenceType_TypeExpression = Generalization(general=TypeExpression, specific=SPL_SequenceType)
gen_SPL_Method_Session = Generalization(general=Session, specific=SPL_Method)
gen_SPL_FunctionDeclaration_Declaration = Generalization(general=Declaration, specific=SPL_FunctionDeclaration)
gen_SPL_RemoteFunctionDeclaration_FunctionDeclaration = Generalization(general=FunctionDeclaration, specific=SPL_RemoteFunctionDeclaration)
gen_SPL_LocalFunctionDeclaration_FunctionDeclaration = Generalization(general=FunctionDeclaration, specific=SPL_LocalFunctionDeclaration)
gen_SPL_DefinedType_TypeExpression = Generalization(general=TypeExpression, specific=SPL_DefinedType)
gen_SPL_Declaration_LocatedElement = Generalization(general=LocatedElement, specific=SPL_Declaration)
gen_SPL_VariableDeclaration_Declaration = Generalization(general=Declaration, specific=SPL_VariableDeclaration)
gen_SPL_DeclarationStat_Statement = Generalization(general=Statement, specific=SPL_DeclarationStat)
gen_SPL_ReturnStat_Statement = Generalization(general=Statement, specific=SPL_ReturnStat)
gen_SPL_IfStat_Statement = Generalization(general=Statement, specific=SPL_IfStat)
gen_SPL_StructureDeclaration_Declaration = Generalization(general=Declaration, specific=SPL_StructureDeclaration)
gen_SPL_WhenStat_Statement = Generalization(general=Statement, specific=SPL_WhenStat)
gen_SPL_StructureProperty_LocatedElement = Generalization(general=LocatedElement, specific=SPL_StructureProperty)
gen_SPL_FunctionCall_LocatedElement = Generalization(general=LocatedElement, specific=SPL_FunctionCall)
gen_SPL_Statement_LocatedElement = Generalization(general=LocatedElement, specific=SPL_Statement)
gen_SPL_CompoundStat_Statement = Generalization(general=Statement, specific=SPL_CompoundStat)
gen_SPL_SetStat_Statement = Generalization(general=Statement, specific=SPL_SetStat)
gen_SPL_FunctionCallStat_Statement = Generalization(general=Statement, specific=SPL_FunctionCallStat)
gen_SPL_ContinueStat_Statement = Generalization(general=Statement, specific=SPL_ContinueStat)
gen_SPL_BreakStat_Statement = Generalization(general=Statement, specific=SPL_BreakStat)
gen_SPL_PushStat_Statement = Generalization(general=Statement, specific=SPL_PushStat)
gen_SPL_WhenHeader_VariableDeclaration = Generalization(general=VariableDeclaration, specific=SPL_WhenHeader)
gen_SPL_SelectMember_LocatedElement = Generalization(general=LocatedElement, specific=SPL_SelectMember)
gen_SPL_ForeachStat_Statement = Generalization(general=Statement, specific=SPL_ForeachStat)
gen_SPL_SelectStat_Statement = Generalization(general=Statement, specific=SPL_SelectStat)
gen_SPL_WithExp_Expression = Generalization(general=Expression, specific=SPL_WithExp)
gen_SPL_BlockExp_Expression = Generalization(general=Expression, specific=SPL_BlockExp)
gen_SPL_ReasonExp_Expression = Generalization(general=Expression, specific=SPL_ReasonExp)
gen_SPL_BODYExp_Expression = Generalization(general=Expression, specific=SPL_BODYExp)
gen_SPL_RequestURIExp_Expression = Generalization(general=Expression, specific=SPL_RequestURIExp)
gen_SPL_PopExp_Expression = Generalization(general=Expression, specific=SPL_PopExp)
gen_SPL_FunctionCallExp_Expression = Generalization(general=Expression, specific=SPL_FunctionCallExp)
gen_SPL_Place_Expression = Generalization(general=Expression, specific=SPL_Place)
gen_SPL_SelectDefault_SelectMember = Generalization(general=SelectMember, specific=SPL_SelectDefault)
gen_SPL_SelectCase_SelectMember = Generalization(general=SelectMember, specific=SPL_SelectCase)
gen_SPL_Expression_LocatedElement = Generalization(general=LocatedElement, specific=SPL_Expression)
gen_SPL_ConstantExp_Expression = Generalization(general=Expression, specific=SPL_ConstantExp)
gen_SPL_OperatorExp_Expression = Generalization(general=Expression, specific=SPL_OperatorExp)
gen_SPL_ForwardExp_Expression = Generalization(general=Expression, specific=SPL_ForwardExp)
gen_SPL_MessageField_LocatedElement = Generalization(general=LocatedElement, specific=SPL_MessageField)
gen_SPL_ReasonMessageField_MessageField = Generalization(general=MessageField, specific=SPL_ReasonMessageField)
gen_SPL_HeadedMessageField_MessageField = Generalization(general=MessageField, specific=SPL_HeadedMessageField)
gen_SPL_Constant_LocatedElement = Generalization(general=LocatedElement, specific=SPL_Constant)
gen_SPL_BooleanConstant_Constant = Generalization(general=Constant, specific=SPL_BooleanConstant)
gen_SPL_IntegerConstant_Constant = Generalization(general=Constant, specific=SPL_IntegerConstant)
gen_SPL_StringConstant_Constant = Generalization(general=Constant, specific=SPL_StringConstant)
gen_SPL_URIConstant_Constant = Generalization(general=Constant, specific=SPL_URIConstant)
gen_SPL_SequenceConstant_Constant = Generalization(general=Constant, specific=SPL_SequenceConstant)
gen_SPL_SIPHeaderPlace_Place = Generalization(general=Place, specific=SPL_SIPHeaderPlace)
gen_SPL_VariablePlace_Place = Generalization(general=Place, specific=SPL_VariablePlace)
gen_SPL_PropertyCallPlace_VariablePlace = Generalization(general=VariablePlace, specific=SPL_PropertyCallPlace)
gen_SPL_Variable_VariablePlace = Generalization(general=VariablePlace, specific=SPL_Variable)
gen_SPL_ResponseConstant_Constant = Generalization(general=Constant, specific=SPL_ResponseConstant)
gen_SPL_Response_LocatedElement = Generalization(general=LocatedElement, specific=SPL_Response)
gen_SPL_SuccessResponse_Response = Generalization(general=Response, specific=SPL_SuccessResponse)
gen_SPL_ErrorResponse_Response = Generalization(general=Response, specific=SPL_ErrorResponse)
gen_SPL_ClientErrorResponse_ErrorResponse = Generalization(general=ErrorResponse, specific=SPL_ClientErrorResponse)
gen_SPL_GlobalErrorResponse_ErrorResponse = Generalization(general=ErrorResponse, specific=SPL_GlobalErrorResponse)
gen_SPL_RedirectionErrorResponse_ErrorResponse = Generalization(general=ErrorResponse, specific=SPL_RedirectionErrorResponse)
gen_SPL_ServerErrorResponse_ErrorResponse = Generalization(general=ErrorResponse, specific=SPL_ServerErrorResponse)

# Domain Model
domain_model = DomainModel(
    name="SPL",
    types={SPL_Declaration, SPL_Session, SPL_Registration, Session, SPL_Dialog, SPL_Method, SPL_LocatedElement, SPL_Program, LocatedElement, SPL_Service, VariableDeclaration, SPL_SIPMethodName, MethodName, SPL_ControlMethodName, SPL_DefaultBranch, Branch, SPL_NamedBranch, SPL_SimpleType, TypeExpression, SPL_Event, SPL_SequenceType, SPL_TypeExpression, SPL_MethodName, SPL_Argument, SPL_Statement, SPL_Branch, SPL_RemoteFunctionDeclaration, FunctionDeclaration, SPL_LocalFunctionDeclaration, SPL_DefinedType, SPL_VariableDeclaration, Declaration, SPL_Expression, SPL_DeclarationStat, SPL_FunctionDeclaration, SPL_ReturnStat, SPL_IfStat, SPL_StructureDeclaration, SPL_WhenStat, SPL_Variable, SPL_StructureProperty, SPL_FunctionCall, SPL_CompoundStat, Statement, SPL_SetStat, SPL_Place, SPL_FunctionCallStat, SPL_ContinueStat, SPL_BreakStat, SPL_PushStat, SPL_Constant, SPL_SelectMember, SPL_WhenHeader, SPL_ForeachStat, SPL_SelectStat, SPL_SelectCase, SPL_SelectDefault, SPL_WithExp, SPL_MessageField, SPL_BlockExp, SPL_ReasonExp, SPL_BODYExp, SPL_RequestURIExp, SPL_PopExp, SPL_FunctionCallExp, SelectMember, SPL_ConstantExp, Expression, SPL_OperatorExp, SPL_ForwardExp, SPL_ReasonMessageField, MessageField, SPL_HeadedMessageField, SPL_BooleanConstant, Constant, SPL_IntegerConstant, SPL_StringConstant, SPL_URIConstant, SPL_SequenceConstant, SPL_SIPHeaderPlace, Place, SPL_VariablePlace, SPL_PropertyCallPlace, VariablePlace, SPL_ResponseConstant, SPL_Response, SPL_SuccessResponse, Response, SPL_ErrorResponse, SPL_ClientErrorResponse, ErrorResponse, SPL_GlobalErrorResponse, SPL_RedirectionErrorResponse, SPL_ServerErrorResponse, SIPMethod, ControlMethod, PrimitiveType, Modifier, FunctionLocation, SIPHeader, Direction, RedirectionErrorKind, ServerErrorKind, SuccessKind, ClientErrorKind, GlobalErrorKind},
    associations={declarations1, sessions3, declarations5, sessions7, declarations10, methods12, service0, statements29, declarations14, methods16, type19, methodName21, arguments23, statements25, branches27, returnType36, arguments38, statements41, type32, initExp34, declaration58, returnedValue60, branch62, condition64, thenStatements66, elseStatements69, properties43, type45, function47, parameters49, statements52, target54, setValue55, selectDefault90, functionCall92, target94, pushedValue96, value99, statements101, idExp72, whenHeaders73, statements75, elseStatements78, sequenceExp81, statements83, matchedExp86, selectCases88, exp115, msgFields117, exp119, source121, functionCall123, values103, value106, leftExp108, rightExp110, exp113, exp129, values132, source125, source126, response134},
    generalizations={gen_SPL_Session_LocatedElement, gen_SPL_Registration_Session, gen_SPL_Dialog_Session, gen_SPL_Program_LocatedElement, gen_SPL_Argument_VariableDeclaration, gen_SPL_Service_LocatedElement, gen_SPL_MethodName_LocatedElement, gen_SPL_SIPMethodName_MethodName, gen_SPL_ControlMethodName_MethodName, gen_SPL_Branch_LocatedElement, gen_SPL_DefaultBranch_Branch, gen_SPL_NamedBranch_Branch, gen_SPL_TypeExpression_LocatedElement, gen_SPL_SimpleType_TypeExpression, gen_SPL_Event_Session, gen_SPL_SequenceType_TypeExpression, gen_SPL_Method_Session, gen_SPL_FunctionDeclaration_Declaration, gen_SPL_RemoteFunctionDeclaration_FunctionDeclaration, gen_SPL_LocalFunctionDeclaration_FunctionDeclaration, gen_SPL_DefinedType_TypeExpression, gen_SPL_Declaration_LocatedElement, gen_SPL_VariableDeclaration_Declaration, gen_SPL_DeclarationStat_Statement, gen_SPL_ReturnStat_Statement, gen_SPL_IfStat_Statement, gen_SPL_StructureDeclaration_Declaration, gen_SPL_WhenStat_Statement, gen_SPL_StructureProperty_LocatedElement, gen_SPL_FunctionCall_LocatedElement, gen_SPL_Statement_LocatedElement, gen_SPL_CompoundStat_Statement, gen_SPL_SetStat_Statement, gen_SPL_FunctionCallStat_Statement, gen_SPL_ContinueStat_Statement, gen_SPL_BreakStat_Statement, gen_SPL_PushStat_Statement, gen_SPL_WhenHeader_VariableDeclaration, gen_SPL_SelectMember_LocatedElement, gen_SPL_ForeachStat_Statement, gen_SPL_SelectStat_Statement, gen_SPL_WithExp_Expression, gen_SPL_BlockExp_Expression, gen_SPL_ReasonExp_Expression, gen_SPL_BODYExp_Expression, gen_SPL_RequestURIExp_Expression, gen_SPL_PopExp_Expression, gen_SPL_FunctionCallExp_Expression, gen_SPL_Place_Expression, gen_SPL_SelectDefault_SelectMember, gen_SPL_SelectCase_SelectMember, gen_SPL_Expression_LocatedElement, gen_SPL_ConstantExp_Expression, gen_SPL_OperatorExp_Expression, gen_SPL_ForwardExp_Expression, gen_SPL_MessageField_LocatedElement, gen_SPL_ReasonMessageField_MessageField, gen_SPL_HeadedMessageField_MessageField, gen_SPL_Constant_LocatedElement, gen_SPL_BooleanConstant_Constant, gen_SPL_IntegerConstant_Constant, gen_SPL_StringConstant_Constant, gen_SPL_URIConstant_Constant, gen_SPL_SequenceConstant_Constant, gen_SPL_SIPHeaderPlace_Place, gen_SPL_VariablePlace_Place, gen_SPL_PropertyCallPlace_VariablePlace, gen_SPL_Variable_VariablePlace, gen_SPL_ResponseConstant_Constant, gen_SPL_Response_LocatedElement, gen_SPL_SuccessResponse_Response, gen_SPL_ErrorResponse_Response, gen_SPL_ClientErrorResponse_ErrorResponse, gen_SPL_GlobalErrorResponse_ErrorResponse, gen_SPL_RedirectionErrorResponse_ErrorResponse, gen_SPL_ServerErrorResponse_ErrorResponse},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)