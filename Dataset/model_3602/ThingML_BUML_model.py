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

# Classes
thingML_Protocol = Class(name="thingML::Protocol")
thingML_Configuration = Class(name="thingML::Configuration")
thingML_PlatformAnnotation = Class(name="thingML::PlatformAnnotation")
thingML_AnnotatedElement = Class(name="thingML::AnnotatedElement", is_abstract=True)
thingML_TypeRef = Class(name="thingML::TypeRef")
thingML_Expression = Class(name="thingML::Expression", is_abstract=True)
thingML_ThingMLModel = Class(name="thingML::ThingMLModel")
thingML_Import = Class(name="thingML::Import")
thingML_Type = Class(name="thingML::Type", is_abstract=True)
thingML_Message = Class(name="thingML::Message")
thingML_Port = Class(name="thingML::Port", is_abstract=True)
thingML_Property = Class(name="thingML::Property")
thingML_Function = Class(name="thingML::Function")
thingML_PropertyAssign = Class(name="thingML::PropertyAssign")
thingML_CompositeState = Class(name="thingML::CompositeState")
thingML_Stream = Class(name="thingML::Stream")
AnnotatedElement = Class(name="AnnotatedElement")
thingML_PrimitiveType = Class(name="thingML::PrimitiveType")
Type = Class(name="Type")
thingML_ObjectType = Class(name="thingML::ObjectType")
thingML_Enumeration = Class(name="thingML::Enumeration")
thingML_EnumerationLiteral = Class(name="thingML::EnumerationLiteral")
thingML_Thing = Class(name="thingML::Thing")
thingML_RequiredPort = Class(name="thingML::RequiredPort")
Port = Class(name="Port")
thingML_Parameter = Class(name="thingML::Parameter")
thingML_ActionBlock = Class(name="thingML::ActionBlock")
ReferencedElmt = Class(name="ReferencedElmt")
Variable = Class(name="Variable")
thingML_MergeSources = Class(name="thingML::MergeSources")
thingML_SimpleSource = Class(name="thingML::SimpleSource")
thingML_ProvidedPort = Class(name="thingML::ProvidedPort")
thingML_InternalPort = Class(name="thingML::InternalPort")
thingML_Source = Class(name="thingML::Source", is_abstract=True)
thingML_LocalVariable = Class(name="thingML::LocalVariable")
thingML_SendAction = Class(name="thingML::SendAction")
thingML_ViewSource = Class(name="thingML::ViewSource", is_abstract=True)
thingML_ReferencedElmt = Class(name="thingML::ReferencedElmt", is_abstract=True)
thingML_ElmtProperty = Class(name="thingML::ElmtProperty", is_abstract=True)
thingML_JoinSources = Class(name="thingML::JoinSources")
Source = Class(name="Source")
thingML_SimpleParamRef = Class(name="thingML::SimpleParamRef")
ElmtProperty = Class(name="ElmtProperty")
thingML_ArrayParamRef = Class(name="thingML::ArrayParamRef")
thingML_LengthArray = Class(name="thingML::LengthArray")
thingML_Region = Class(name="thingML::Region")
Region = Class(name="Region")
State = Class(name="State")
thingML_State = Class(name="thingML::State")
thingML_ReceiveMessage = Class(name="thingML::ReceiveMessage")
thingML_Filter = Class(name="thingML::Filter")
ViewSource = Class(name="ViewSource")
thingML_LengthWindow = Class(name="thingML::LengthWindow")
thingML_TimeWindow = Class(name="thingML::TimeWindow")
thingML_MessageParameter = Class(name="thingML::MessageParameter")
thingML_ParallelRegion = Class(name="thingML::ParallelRegion")
thingML_FinalState = Class(name="thingML::FinalState")
thingML_Session = Class(name="thingML::Session")
Event = Class(name="Event")
thingML_Action = Class(name="thingML::Action", is_abstract=True)
thingML_InternalTransition = Class(name="thingML::InternalTransition")
thingML_Transition = Class(name="thingML::Transition")
thingML_Handler = Class(name="thingML::Handler", is_abstract=True)
thingML_Event = Class(name="thingML::Event", is_abstract=True)
Handler = Class(name="Handler")
thingML_Variable = Class(name="thingML::Variable", is_abstract=True)
Action = Class(name="Action")
thingML_ExternStatement = Class(name="thingML::ExternStatement")
thingML_ReturnAction = Class(name="thingML::ReturnAction")
thingML_PrintAction = Class(name="thingML::PrintAction")
thingML_VariableAssignment = Class(name="thingML::VariableAssignment")
thingML_Increment = Class(name="thingML::Increment")
thingML_Decrement = Class(name="thingML::Decrement")
thingML_LoopAction = Class(name="thingML::LoopAction")
thingML_ConditionalAction = Class(name="thingML::ConditionalAction")
thingML_Reference = Class(name="thingML::Reference")
thingML_FunctionCallExpression = Class(name="thingML::FunctionCallExpression")
thingML_ErrorAction = Class(name="thingML::ErrorAction")
thingML_StartSession = Class(name="thingML::StartSession")
thingML_FunctionCallStatement = Class(name="thingML::FunctionCallStatement")
thingML_ExternExpression = Class(name="thingML::ExternExpression")
Expression = Class(name="Expression")
thingML_EnumLiteralRef = Class(name="thingML::EnumLiteralRef")
thingML_IntegerLiteral = Class(name="thingML::IntegerLiteral")
thingML_BooleanLiteral = Class(name="thingML::BooleanLiteral")
thingML_StringLiteral = Class(name="thingML::StringLiteral")
thingML_DoubleLiteral = Class(name="thingML::DoubleLiteral")
thingML_PropertyReference = Class(name="thingML::PropertyReference")
thingML_Connector = Class(name="thingML::Connector")
AbstractConnector = Class(name="AbstractConnector")
thingML_Instance = Class(name="thingML::Instance")
thingML_AbstractConnector = Class(name="thingML::AbstractConnector", is_abstract=True)
thingML_ConfigPropertyAssign = Class(name="thingML::ConfigPropertyAssign")
thingML_InstanceRef = Class(name="thingML::InstanceRef")
thingML_NotEqualsExpression = Class(name="thingML::NotEqualsExpression")
thingML_ExternalConnector = Class(name="thingML::ExternalConnector")
thingML_OrExpression = Class(name="thingML::OrExpression")
thingML_AndExpression = Class(name="thingML::AndExpression")
thingML_EqualsExpression = Class(name="thingML::EqualsExpression")
thingML_PlusExpression = Class(name="thingML::PlusExpression")
thingML_MinusExpression = Class(name="thingML::MinusExpression")
thingML_GreaterExpression = Class(name="thingML::GreaterExpression")
thingML_LowerExpression = Class(name="thingML::LowerExpression")
thingML_GreaterOrEqualExpression = Class(name="thingML::GreaterOrEqualExpression")
thingML_LowerOrEqualExpression = Class(name="thingML::LowerOrEqualExpression")
thingML_TimesExpression = Class(name="thingML::TimesExpression")
thingML_DivExpression = Class(name="thingML::DivExpression")
thingML_ModExpression = Class(name="thingML::ModExpression")
thingML_NotExpression = Class(name="thingML::NotExpression")
thingML_UnaryMinus = Class(name="thingML::UnaryMinus")
thingML_ArrayIndex = Class(name="thingML::ArrayIndex")

# thingML_Protocol class attributes and methods
thingML_Protocol_name: Property = Property(name="name", type=StringType)
thingML_Protocol.attributes={thingML_Protocol_name}

# thingML_Configuration class attributes and methods
thingML_Configuration_name: Property = Property(name="name", type=StringType)
thingML_Configuration.attributes={thingML_Configuration_name}

# thingML_PlatformAnnotation class attributes and methods
thingML_PlatformAnnotation_name: Property = Property(name="name", type=StringType)
thingML_PlatformAnnotation_value: Property = Property(name="value", type=StringType)
thingML_PlatformAnnotation.attributes={thingML_PlatformAnnotation_value, thingML_PlatformAnnotation_name}

# thingML_AnnotatedElement class attributes and methods

# thingML_TypeRef class attributes and methods
thingML_TypeRef_isArray: Property = Property(name="isArray", type=BooleanType)
thingML_TypeRef.attributes={thingML_TypeRef_isArray}

# thingML_Expression class attributes and methods

# thingML_ThingMLModel class attributes and methods

# thingML_Import class attributes and methods
thingML_Import_importURI: Property = Property(name="importURI", type=StringType)
thingML_Import.attributes={thingML_Import_importURI}

# thingML_Type class attributes and methods
thingML_Type_name: Property = Property(name="name", type=StringType)
thingML_Type.attributes={thingML_Type_name}

# thingML_Message class attributes and methods
thingML_Message_name: Property = Property(name="name", type=StringType)
thingML_Message.attributes={thingML_Message_name}

# thingML_Port class attributes and methods
thingML_Port_name: Property = Property(name="name", type=StringType)
thingML_Port.attributes={thingML_Port_name}

# thingML_Property class attributes and methods
thingML_Property_changeable: Property = Property(name="changeable", type=BooleanType)
thingML_Property_name: Property = Property(name="name", type=StringType)
thingML_Property.attributes={thingML_Property_name, thingML_Property_changeable}

# thingML_Function class attributes and methods
thingML_Function_name: Property = Property(name="name", type=StringType)
thingML_Function.attributes={thingML_Function_name}

# thingML_PropertyAssign class attributes and methods

# thingML_CompositeState class attributes and methods
thingML_CompositeState_history: Property = Property(name="history", type=BooleanType)
thingML_CompositeState.attributes={thingML_CompositeState_history}

# thingML_Stream class attributes and methods
thingML_Stream_name: Property = Property(name="name", type=StringType)
thingML_Stream.attributes={thingML_Stream_name}

# AnnotatedElement class attributes and methods

# thingML_PrimitiveType class attributes and methods
thingML_PrimitiveType_ByteSize: Property = Property(name="ByteSize", type=IntegerType)
thingML_PrimitiveType.attributes={thingML_PrimitiveType_ByteSize}

# Type class attributes and methods

# thingML_ObjectType class attributes and methods

# thingML_Enumeration class attributes and methods

# thingML_EnumerationLiteral class attributes and methods
thingML_EnumerationLiteral_name: Property = Property(name="name", type=StringType)
thingML_EnumerationLiteral.attributes={thingML_EnumerationLiteral_name}

# thingML_Thing class attributes and methods
thingML_Thing_fragment: Property = Property(name="fragment", type=BooleanType)
thingML_Thing.attributes={thingML_Thing_fragment}

# thingML_RequiredPort class attributes and methods
thingML_RequiredPort_optional: Property = Property(name="optional", type=BooleanType)
thingML_RequiredPort.attributes={thingML_RequiredPort_optional}

# Port class attributes and methods

# thingML_Parameter class attributes and methods
thingML_Parameter_name: Property = Property(name="name", type=StringType)
thingML_Parameter.attributes={thingML_Parameter_name}

# thingML_ActionBlock class attributes and methods

# ReferencedElmt class attributes and methods

# Variable class attributes and methods

# thingML_MergeSources class attributes and methods
thingML_MergeSources_name: Property = Property(name="name", type=StringType)
thingML_MergeSources.attributes={thingML_MergeSources_name}

# thingML_SimpleSource class attributes and methods
thingML_SimpleSource_name: Property = Property(name="name", type=StringType)
thingML_SimpleSource.attributes={thingML_SimpleSource_name}

# thingML_ProvidedPort class attributes and methods

# thingML_InternalPort class attributes and methods

# thingML_Source class attributes and methods

# thingML_LocalVariable class attributes and methods
thingML_LocalVariable_changeable: Property = Property(name="changeable", type=BooleanType)
thingML_LocalVariable_name: Property = Property(name="name", type=StringType)
thingML_LocalVariable.attributes={thingML_LocalVariable_name, thingML_LocalVariable_changeable}

# thingML_SendAction class attributes and methods

# thingML_ViewSource class attributes and methods

# thingML_ReferencedElmt class attributes and methods

# thingML_ElmtProperty class attributes and methods

# thingML_JoinSources class attributes and methods
thingML_JoinSources_name: Property = Property(name="name", type=StringType)
thingML_JoinSources.attributes={thingML_JoinSources_name}

# Source class attributes and methods

# thingML_SimpleParamRef class attributes and methods

# ElmtProperty class attributes and methods

# thingML_ArrayParamRef class attributes and methods

# thingML_LengthArray class attributes and methods

# thingML_Region class attributes and methods

# Region class attributes and methods

# State class attributes and methods

# thingML_State class attributes and methods
thingML_State_name: Property = Property(name="name", type=StringType)
thingML_State.attributes={thingML_State_name}

# thingML_ReceiveMessage class attributes and methods
thingML_ReceiveMessage_name: Property = Property(name="name", type=StringType)
thingML_ReceiveMessage.attributes={thingML_ReceiveMessage_name}

# thingML_Filter class attributes and methods

# ViewSource class attributes and methods

# thingML_LengthWindow class attributes and methods

# thingML_TimeWindow class attributes and methods

# thingML_MessageParameter class attributes and methods
thingML_MessageParameter_name: Property = Property(name="name", type=StringType)
thingML_MessageParameter.attributes={thingML_MessageParameter_name}

# thingML_ParallelRegion class attributes and methods
thingML_ParallelRegion_name: Property = Property(name="name", type=StringType)
thingML_ParallelRegion_history: Property = Property(name="history", type=BooleanType)
thingML_ParallelRegion.attributes={thingML_ParallelRegion_history, thingML_ParallelRegion_name}

# thingML_FinalState class attributes and methods

# thingML_Session class attributes and methods
thingML_Session_maxInstances: Property = Property(name="maxInstances", type=IntegerType)
thingML_Session.attributes={thingML_Session_maxInstances}

# Event class attributes and methods

# thingML_Action class attributes and methods

# thingML_InternalTransition class attributes and methods

# thingML_Transition class attributes and methods

# thingML_Handler class attributes and methods
thingML_Handler_name: Property = Property(name="name", type=StringType)
thingML_Handler.attributes={thingML_Handler_name}

# thingML_Event class attributes and methods

# Handler class attributes and methods

# thingML_Variable class attributes and methods

# Action class attributes and methods

# thingML_ExternStatement class attributes and methods
thingML_ExternStatement_statement: Property = Property(name="statement", type=StringType)
thingML_ExternStatement.attributes={thingML_ExternStatement_statement}

# thingML_ReturnAction class attributes and methods

# thingML_PrintAction class attributes and methods

# thingML_VariableAssignment class attributes and methods

# thingML_Increment class attributes and methods

# thingML_Decrement class attributes and methods

# thingML_LoopAction class attributes and methods

# thingML_ConditionalAction class attributes and methods

# thingML_Reference class attributes and methods

# thingML_FunctionCallExpression class attributes and methods

# thingML_ErrorAction class attributes and methods

# thingML_StartSession class attributes and methods

# thingML_FunctionCallStatement class attributes and methods

# thingML_ExternExpression class attributes and methods
thingML_ExternExpression_expression: Property = Property(name="expression", type=StringType)
thingML_ExternExpression.attributes={thingML_ExternExpression_expression}

# Expression class attributes and methods

# thingML_EnumLiteralRef class attributes and methods

# thingML_IntegerLiteral class attributes and methods
thingML_IntegerLiteral_intValue: Property = Property(name="intValue", type=IntegerType)
thingML_IntegerLiteral.attributes={thingML_IntegerLiteral_intValue}

# thingML_BooleanLiteral class attributes and methods
thingML_BooleanLiteral_boolValue: Property = Property(name="boolValue", type=StringType)
thingML_BooleanLiteral.attributes={thingML_BooleanLiteral_boolValue}

# thingML_StringLiteral class attributes and methods
thingML_StringLiteral_stringValue: Property = Property(name="stringValue", type=StringType)
thingML_StringLiteral.attributes={thingML_StringLiteral_stringValue}

# thingML_DoubleLiteral class attributes and methods
thingML_DoubleLiteral_doubleValue: Property = Property(name="doubleValue", type=FloatType)
thingML_DoubleLiteral.attributes={thingML_DoubleLiteral_doubleValue}

# thingML_PropertyReference class attributes and methods

# thingML_Connector class attributes and methods

# AbstractConnector class attributes and methods

# thingML_Instance class attributes and methods
thingML_Instance_name: Property = Property(name="name", type=StringType)
thingML_Instance.attributes={thingML_Instance_name}

# thingML_AbstractConnector class attributes and methods
thingML_AbstractConnector_name: Property = Property(name="name", type=StringType)
thingML_AbstractConnector.attributes={thingML_AbstractConnector_name}

# thingML_ConfigPropertyAssign class attributes and methods

# thingML_InstanceRef class attributes and methods

# thingML_NotEqualsExpression class attributes and methods

# thingML_ExternalConnector class attributes and methods

# thingML_OrExpression class attributes and methods

# thingML_AndExpression class attributes and methods

# thingML_EqualsExpression class attributes and methods

# thingML_PlusExpression class attributes and methods

# thingML_MinusExpression class attributes and methods

# thingML_GreaterExpression class attributes and methods

# thingML_LowerExpression class attributes and methods

# thingML_GreaterOrEqualExpression class attributes and methods

# thingML_LowerOrEqualExpression class attributes and methods

# thingML_TimesExpression class attributes and methods

# thingML_DivExpression class attributes and methods

# thingML_ModExpression class attributes and methods

# thingML_NotExpression class attributes and methods

# thingML_UnaryMinus class attributes and methods

# thingML_ArrayIndex class attributes and methods

# Relationships
protocols3: BinaryAssociation = BinaryAssociation(
    name="protocols3",
    ends={
        Property(name="thingML_Protocol", type=thingML_ThingMLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ThingMLModel4", type=thingML_Protocol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
configs5: BinaryAssociation = BinaryAssociation(
    name="configs5",
    ends={
        Property(name="thingML_Configuration", type=thingML_ThingMLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ThingMLModel6", type=thingML_Configuration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations7: BinaryAssociation = BinaryAssociation(
    name="annotations7",
    ends={
        Property(name="thingML_PlatformAnnotation", type=thingML_AnnotatedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_AnnotatedElement", type=thingML_PlatformAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type8: BinaryAssociation = BinaryAssociation(
    name="type8",
    ends={
        Property(name="thingML_Type9", type=thingML_TypeRef, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_TypeRef", type=thingML_Type, multiplicity=Multiplicity(1, 1))
    }
)
imports0: BinaryAssociation = BinaryAssociation(
    name="imports0",
    ends={
        Property(name="thingML_Import", type=thingML_ThingMLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ThingMLModel", type=thingML_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types1: BinaryAssociation = BinaryAssociation(
    name="types1",
    ends={
        Property(name="thingML_Type", type=thingML_ThingMLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ThingMLModel2", type=thingML_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
includes17: BinaryAssociation = BinaryAssociation(
    name="includes17",
    ends={
        Property(name="thingML_Thing", type=thingML_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Thing16", type=thingML_Thing, multiplicity=Multiplicity(0, 9999))
    }
)
messages18: BinaryAssociation = BinaryAssociation(
    name="messages18",
    ends={
        Property(name="thingML_Message", type=thingML_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Thing19", type=thingML_Message, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ports20: BinaryAssociation = BinaryAssociation(
    name="ports20",
    ends={
        Property(name="thingML_Port", type=thingML_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Thing21", type=thingML_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties22: BinaryAssociation = BinaryAssociation(
    name="properties22",
    ends={
        Property(name="thingML_Property", type=thingML_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Thing23", type=thingML_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functions24: BinaryAssociation = BinaryAssociation(
    name="functions24",
    ends={
        Property(name="thingML_Function", type=thingML_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Thing25", type=thingML_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assign26: BinaryAssociation = BinaryAssociation(
    name="assign26",
    ends={
        Property(name="thingML_PropertyAssign", type=thingML_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Thing27", type=thingML_PropertyAssign, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
behaviour28: BinaryAssociation = BinaryAssociation(
    name="behaviour28",
    ends={
        Property(name="thingML_CompositeState", type=thingML_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Thing29", type=thingML_CompositeState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
streams30: BinaryAssociation = BinaryAssociation(
    name="streams30",
    ends={
        Property(name="thingML_Stream", type=thingML_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Thing31", type=thingML_Stream, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property32: BinaryAssociation = BinaryAssociation(
    name="property32",
    ends={
        Property(name="thingML_Property34", type=thingML_PropertyAssign, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_PropertyAssign33", type=thingML_Property, multiplicity=Multiplicity(1, 1))
    }
)
cardinality10: BinaryAssociation = BinaryAssociation(
    name="cardinality10",
    ends={
        Property(name="thingML_Expression", type=thingML_TypeRef, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_TypeRef11", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
literals12: BinaryAssociation = BinaryAssociation(
    name="literals12",
    ends={
        Property(name="thingML_EnumerationLiteral", type=thingML_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Enumeration", type=thingML_EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotations13: BinaryAssociation = BinaryAssociation(
    name="annotations13",
    ends={
        Property(name="thingML_PlatformAnnotation15", type=thingML_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_EnumerationLiteral14", type=thingML_PlatformAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters54: BinaryAssociation = BinaryAssociation(
    name="parameters54",
    ends={
        Property(name="thingML_Parameter56", type=thingML_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Message55", type=thingML_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeRef57: BinaryAssociation = BinaryAssociation(
    name="typeRef57",
    ends={
        Property(name="thingML_TypeRef59", type=thingML_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Parameter58", type=thingML_TypeRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sends60: BinaryAssociation = BinaryAssociation(
    name="sends60",
    ends={
        Property(name="thingML_Message62", type=thingML_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Port61", type=thingML_Message, multiplicity=Multiplicity(0, 9999))
    }
)
receives63: BinaryAssociation = BinaryAssociation(
    name="receives63",
    ends={
        Property(name="thingML_Message65", type=thingML_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Port64", type=thingML_Message, multiplicity=Multiplicity(0, 9999))
    }
)
index35: BinaryAssociation = BinaryAssociation(
    name="index35",
    ends={
        Property(name="thingML_Expression37", type=thingML_PropertyAssign, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_PropertyAssign36", type=thingML_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
init38: BinaryAssociation = BinaryAssociation(
    name="init38",
    ends={
        Property(name="thingML_Expression40", type=thingML_PropertyAssign, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_PropertyAssign39", type=thingML_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters41: BinaryAssociation = BinaryAssociation(
    name="parameters41",
    ends={
        Property(name="thingML_Parameter", type=thingML_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Function42", type=thingML_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeRef43: BinaryAssociation = BinaryAssociation(
    name="typeRef43",
    ends={
        Property(name="thingML_TypeRef45", type=thingML_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Function44", type=thingML_TypeRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body46: BinaryAssociation = BinaryAssociation(
    name="body46",
    ends={
        Property(name="thingML_ActionBlock", type=thingML_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Function47", type=thingML_ActionBlock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
typeRef48: BinaryAssociation = BinaryAssociation(
    name="typeRef48",
    ends={
        Property(name="thingML_TypeRef50", type=thingML_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Property49", type=thingML_TypeRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
init51: BinaryAssociation = BinaryAssociation(
    name="init51",
    ends={
        Property(name="thingML_Expression53", type=thingML_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Property52", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resultMessage74: BinaryAssociation = BinaryAssociation(
    name="resultMessage74",
    ends={
        Property(name="thingML_Message76", type=thingML_JoinSources, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_JoinSources75", type=thingML_Message, multiplicity=Multiplicity(1, 1))
    }
)
rules77: BinaryAssociation = BinaryAssociation(
    name="rules77",
    ends={
        Property(name="thingML_Expression79", type=thingML_JoinSources, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_JoinSources78", type=thingML_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operators80: BinaryAssociation = BinaryAssociation(
    name="operators80",
    ends={
        Property(name="thingML_ViewSource", type=thingML_JoinSources, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_JoinSources81", type=thingML_ViewSource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sources82: BinaryAssociation = BinaryAssociation(
    name="sources82",
    ends={
        Property(name="thingML_Source83", type=thingML_MergeSources, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_MergeSources", type=thingML_Source, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
resultMessage84: BinaryAssociation = BinaryAssociation(
    name="resultMessage84",
    ends={
        Property(name="thingML_Message86", type=thingML_MergeSources, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_MergeSources85", type=thingML_Message, multiplicity=Multiplicity(1, 1))
    }
)
operators87: BinaryAssociation = BinaryAssociation(
    name="operators87",
    ends={
        Property(name="thingML_ViewSource89", type=thingML_MergeSources, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_MergeSources88", type=thingML_ViewSource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
input66: BinaryAssociation = BinaryAssociation(
    name="input66",
    ends={
        Property(name="thingML_Source", type=thingML_Stream, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Stream67", type=thingML_Source, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
selection68: BinaryAssociation = BinaryAssociation(
    name="selection68",
    ends={
        Property(name="thingML_LocalVariable", type=thingML_Stream, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Stream69", type=thingML_LocalVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
output70: BinaryAssociation = BinaryAssociation(
    name="output70",
    ends={
        Property(name="thingML_SendAction", type=thingML_Stream, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Stream71", type=thingML_SendAction, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sources72: BinaryAssociation = BinaryAssociation(
    name="sources72",
    ends={
        Property(name="thingML_Source73", type=thingML_JoinSources, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_JoinSources", type=thingML_Source, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
msgRef106: BinaryAssociation = BinaryAssociation(
    name="msgRef106",
    ends={
        Property(name="thingML_Message107", type=thingML_MessageParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_MessageParameter", type=thingML_Message, multiplicity=Multiplicity(1, 1))
    }
)
parameterRef108: BinaryAssociation = BinaryAssociation(
    name="parameterRef108",
    ends={
        Property(name="thingML_Parameter109", type=thingML_SimpleParamRef, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_SimpleParamRef", type=thingML_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
parameterRef110: BinaryAssociation = BinaryAssociation(
    name="parameterRef110",
    ends={
        Property(name="thingML_Parameter111", type=thingML_ArrayParamRef, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ArrayParamRef", type=thingML_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
initial112: BinaryAssociation = BinaryAssociation(
    name="initial112",
    ends={
        Property(name="thingML_State", type=thingML_CompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_CompositeState113", type=thingML_State, multiplicity=Multiplicity(1, 1))
    }
)
message90: BinaryAssociation = BinaryAssociation(
    name="message90",
    ends={
        Property(name="thingML_ReceiveMessage", type=thingML_SimpleSource, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_SimpleSource", type=thingML_ReceiveMessage, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operators91: BinaryAssociation = BinaryAssociation(
    name="operators91",
    ends={
        Property(name="thingML_ViewSource93", type=thingML_SimpleSource, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_SimpleSource92", type=thingML_ViewSource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guard94: BinaryAssociation = BinaryAssociation(
    name="guard94",
    ends={
        Property(name="thingML_Expression95", type=thingML_Filter, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Filter", type=thingML_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
size96: BinaryAssociation = BinaryAssociation(
    name="size96",
    ends={
        Property(name="thingML_Expression97", type=thingML_LengthWindow, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_LengthWindow", type=thingML_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
step98: BinaryAssociation = BinaryAssociation(
    name="step98",
    ends={
        Property(name="thingML_Expression100", type=thingML_LengthWindow, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_LengthWindow99", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
duration101: BinaryAssociation = BinaryAssociation(
    name="duration101",
    ends={
        Property(name="thingML_Expression102", type=thingML_TimeWindow, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_TimeWindow", type=thingML_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
step103: BinaryAssociation = BinaryAssociation(
    name="step103",
    ends={
        Property(name="thingML_Expression105", type=thingML_TimeWindow, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_TimeWindow104", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
substate114: BinaryAssociation = BinaryAssociation(
    name="substate114",
    ends={
        Property(name="thingML_State116", type=thingML_CompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_CompositeState115", type=thingML_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
region117: BinaryAssociation = BinaryAssociation(
    name="region117",
    ends={
        Property(name="thingML_ParallelRegion", type=thingML_CompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_CompositeState118", type=thingML_ParallelRegion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target152: BinaryAssociation = BinaryAssociation(
    name="target152",
    ends={
        Property(name="thingML_State154", type=thingML_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Transition153", type=thingML_State, multiplicity=Multiplicity(1, 1))
    }
)
initial127: BinaryAssociation = BinaryAssociation(
    name="initial127",
    ends={
        Property(name="thingML_State129", type=thingML_ParallelRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ParallelRegion128", type=thingML_State, multiplicity=Multiplicity(1, 1))
    }
)
substate130: BinaryAssociation = BinaryAssociation(
    name="substate130",
    ends={
        Property(name="thingML_State132", type=thingML_ParallelRegion, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ParallelRegion131", type=thingML_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initial119: BinaryAssociation = BinaryAssociation(
    name="initial119",
    ends={
        Property(name="thingML_State120", type=thingML_Session, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Session", type=thingML_State, multiplicity=Multiplicity(1, 1))
    }
)
substate121: BinaryAssociation = BinaryAssociation(
    name="substate121",
    ends={
        Property(name="thingML_State123", type=thingML_Session, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Session122", type=thingML_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
region124: BinaryAssociation = BinaryAssociation(
    name="region124",
    ends={
        Property(name="thingML_ParallelRegion126", type=thingML_Session, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Session125", type=thingML_ParallelRegion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties133: BinaryAssociation = BinaryAssociation(
    name="properties133",
    ends={
        Property(name="thingML_Property135", type=thingML_State, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_State134", type=thingML_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entry136: BinaryAssociation = BinaryAssociation(
    name="entry136",
    ends={
        Property(name="thingML_Action", type=thingML_State, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_State137", type=thingML_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exit138: BinaryAssociation = BinaryAssociation(
    name="exit138",
    ends={
        Property(name="thingML_Action140", type=thingML_State, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_State139", type=thingML_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
internal141: BinaryAssociation = BinaryAssociation(
    name="internal141",
    ends={
        Property(name="thingML_InternalTransition", type=thingML_State, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_State142", type=thingML_InternalTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoing143: BinaryAssociation = BinaryAssociation(
    name="outgoing143",
    ends={
        Property(name="thingML_Transition", type=thingML_State, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_State144", type=thingML_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event145: BinaryAssociation = BinaryAssociation(
    name="event145",
    ends={
        Property(name="thingML_Event", type=thingML_Handler, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Handler", type=thingML_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guard146: BinaryAssociation = BinaryAssociation(
    name="guard146",
    ends={
        Property(name="thingML_Expression148", type=thingML_Handler, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Handler147", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action149: BinaryAssociation = BinaryAssociation(
    name="action149",
    ends={
        Property(name="thingML_Action151", type=thingML_Handler, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Handler150", type=thingML_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeRef166: BinaryAssociation = BinaryAssociation(
    name="typeRef166",
    ends={
        Property(name="thingML_TypeRef168", type=thingML_LocalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_LocalVariable167", type=thingML_TypeRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
init169: BinaryAssociation = BinaryAssociation(
    name="init169",
    ends={
        Property(name="thingML_Expression171", type=thingML_LocalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_LocalVariable170", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
port172: BinaryAssociation = BinaryAssociation(
    name="port172",
    ends={
        Property(name="thingML_Port174", type=thingML_SendAction, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_SendAction173", type=thingML_Port, multiplicity=Multiplicity(1, 1))
    }
)
port155: BinaryAssociation = BinaryAssociation(
    name="port155",
    ends={
        Property(name="thingML_Port157", type=thingML_ReceiveMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ReceiveMessage156", type=thingML_Port, multiplicity=Multiplicity(0, 1))
    }
)
message158: BinaryAssociation = BinaryAssociation(
    name="message158",
    ends={
        Property(name="thingML_Message160", type=thingML_ReceiveMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ReceiveMessage159", type=thingML_Message, multiplicity=Multiplicity(1, 1))
    }
)
actions161: BinaryAssociation = BinaryAssociation(
    name="actions161",
    ends={
        Property(name="thingML_Action163", type=thingML_ActionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ActionBlock162", type=thingML_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
segments164: BinaryAssociation = BinaryAssociation(
    name="segments164",
    ends={
        Property(name="thingML_Expression165", type=thingML_ExternStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ExternStatement", type=thingML_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseAction202: BinaryAssociation = BinaryAssociation(
    name="elseAction202",
    ends={
        Property(name="thingML_Action204", type=thingML_ConditionalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ConditionalAction203", type=thingML_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp205: BinaryAssociation = BinaryAssociation(
    name="exp205",
    ends={
        Property(name="thingML_Expression206", type=thingML_ReturnAction, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ReturnAction", type=thingML_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
message175: BinaryAssociation = BinaryAssociation(
    name="message175",
    ends={
        Property(name="thingML_Message177", type=thingML_SendAction, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_SendAction176", type=thingML_Message, multiplicity=Multiplicity(1, 1))
    }
)
parameters178: BinaryAssociation = BinaryAssociation(
    name="parameters178",
    ends={
        Property(name="thingML_Expression180", type=thingML_SendAction, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_SendAction179", type=thingML_Expression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
property181: BinaryAssociation = BinaryAssociation(
    name="property181",
    ends={
        Property(name="thingML_Variable", type=thingML_VariableAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_VariableAssignment", type=thingML_Variable, multiplicity=Multiplicity(1, 1))
    }
)
index182: BinaryAssociation = BinaryAssociation(
    name="index182",
    ends={
        Property(name="thingML_Expression184", type=thingML_VariableAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_VariableAssignment183", type=thingML_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression185: BinaryAssociation = BinaryAssociation(
    name="expression185",
    ends={
        Property(name="thingML_Expression187", type=thingML_VariableAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_VariableAssignment186", type=thingML_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
var188: BinaryAssociation = BinaryAssociation(
    name="var188",
    ends={
        Property(name="thingML_Variable189", type=thingML_Increment, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Increment", type=thingML_Variable, multiplicity=Multiplicity(1, 1))
    }
)
var190: BinaryAssociation = BinaryAssociation(
    name="var190",
    ends={
        Property(name="thingML_Variable191", type=thingML_Decrement, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Decrement", type=thingML_Variable, multiplicity=Multiplicity(1, 1))
    }
)
condition192: BinaryAssociation = BinaryAssociation(
    name="condition192",
    ends={
        Property(name="thingML_Expression193", type=thingML_LoopAction, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_LoopAction", type=thingML_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
action194: BinaryAssociation = BinaryAssociation(
    name="action194",
    ends={
        Property(name="thingML_Action196", type=thingML_LoopAction, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_LoopAction195", type=thingML_Action, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition197: BinaryAssociation = BinaryAssociation(
    name="condition197",
    ends={
        Property(name="thingML_Expression198", type=thingML_ConditionalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ConditionalAction", type=thingML_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
action199: BinaryAssociation = BinaryAssociation(
    name="action199",
    ends={
        Property(name="thingML_Action201", type=thingML_ConditionalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ConditionalAction200", type=thingML_Action, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
reference227: BinaryAssociation = BinaryAssociation(
    name="reference227",
    ends={
        Property(name="thingML_ReferencedElmt", type=thingML_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Reference", type=thingML_ReferencedElmt, multiplicity=Multiplicity(1, 1))
    }
)
parameter228: BinaryAssociation = BinaryAssociation(
    name="parameter228",
    ends={
        Property(name="thingML_ElmtProperty", type=thingML_Reference, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Reference229", type=thingML_ElmtProperty, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
msg207: BinaryAssociation = BinaryAssociation(
    name="msg207",
    ends={
        Property(name="thingML_Expression208", type=thingML_PrintAction, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_PrintAction", type=thingML_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
msg209: BinaryAssociation = BinaryAssociation(
    name="msg209",
    ends={
        Property(name="thingML_Expression210", type=thingML_ErrorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ErrorAction", type=thingML_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
session211: BinaryAssociation = BinaryAssociation(
    name="session211",
    ends={
        Property(name="thingML_Session212", type=thingML_StartSession, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_StartSession", type=thingML_Session, multiplicity=Multiplicity(1, 1))
    }
)
function213: BinaryAssociation = BinaryAssociation(
    name="function213",
    ends={
        Property(name="thingML_Function214", type=thingML_FunctionCallStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_FunctionCallStatement", type=thingML_Function, multiplicity=Multiplicity(1, 1))
    }
)
parameters215: BinaryAssociation = BinaryAssociation(
    name="parameters215",
    ends={
        Property(name="thingML_Expression217", type=thingML_FunctionCallStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_FunctionCallStatement216", type=thingML_Expression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
segments218: BinaryAssociation = BinaryAssociation(
    name="segments218",
    ends={
        Property(name="thingML_Expression219", type=thingML_ExternExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ExternExpression", type=thingML_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enum220: BinaryAssociation = BinaryAssociation(
    name="enum220",
    ends={
        Property(name="thingML_Enumeration221", type=thingML_EnumLiteralRef, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_EnumLiteralRef", type=thingML_Enumeration, multiplicity=Multiplicity(1, 1))
    }
)
literal222: BinaryAssociation = BinaryAssociation(
    name="literal222",
    ends={
        Property(name="thingML_EnumerationLiteral224", type=thingML_EnumLiteralRef, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_EnumLiteralRef223", type=thingML_EnumerationLiteral, multiplicity=Multiplicity(1, 1))
    }
)
property225: BinaryAssociation = BinaryAssociation(
    name="property225",
    ends={
        Property(name="thingML_Variable226", type=thingML_PropertyReference, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_PropertyReference", type=thingML_Variable, multiplicity=Multiplicity(1, 1))
    }
)
cli258: BinaryAssociation = BinaryAssociation(
    name="cli258",
    ends={
        Property(name="thingML_InstanceRef259", type=thingML_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Connector", type=thingML_InstanceRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
required260: BinaryAssociation = BinaryAssociation(
    name="required260",
    ends={
        Property(name="thingML_RequiredPort", type=thingML_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Connector261", type=thingML_RequiredPort, multiplicity=Multiplicity(1, 1))
    }
)
function230: BinaryAssociation = BinaryAssociation(
    name="function230",
    ends={
        Property(name="thingML_Function231", type=thingML_FunctionCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_FunctionCallExpression", type=thingML_Function, multiplicity=Multiplicity(1, 1))
    }
)
parameters232: BinaryAssociation = BinaryAssociation(
    name="parameters232",
    ends={
        Property(name="thingML_Expression234", type=thingML_FunctionCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_FunctionCallExpression233", type=thingML_Expression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
instances235: BinaryAssociation = BinaryAssociation(
    name="instances235",
    ends={
        Property(name="thingML_Instance", type=thingML_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Configuration236", type=thingML_Instance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connectors237: BinaryAssociation = BinaryAssociation(
    name="connectors237",
    ends={
        Property(name="thingML_AbstractConnector", type=thingML_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Configuration238", type=thingML_AbstractConnector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
propassigns239: BinaryAssociation = BinaryAssociation(
    name="propassigns239",
    ends={
        Property(name="thingML_ConfigPropertyAssign", type=thingML_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Configuration240", type=thingML_ConfigPropertyAssign, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type241: BinaryAssociation = BinaryAssociation(
    name="type241",
    ends={
        Property(name="thingML_Thing243", type=thingML_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Instance242", type=thingML_Thing, multiplicity=Multiplicity(1, 1))
    }
)
instance244: BinaryAssociation = BinaryAssociation(
    name="instance244",
    ends={
        Property(name="thingML_InstanceRef", type=thingML_ConfigPropertyAssign, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ConfigPropertyAssign245", type=thingML_InstanceRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
property246: BinaryAssociation = BinaryAssociation(
    name="property246",
    ends={
        Property(name="thingML_Property248", type=thingML_ConfigPropertyAssign, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ConfigPropertyAssign247", type=thingML_Property, multiplicity=Multiplicity(1, 1))
    }
)
index249: BinaryAssociation = BinaryAssociation(
    name="index249",
    ends={
        Property(name="thingML_Expression251", type=thingML_ConfigPropertyAssign, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ConfigPropertyAssign250", type=thingML_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
init252: BinaryAssociation = BinaryAssociation(
    name="init252",
    ends={
        Property(name="thingML_Expression254", type=thingML_ConfigPropertyAssign, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ConfigPropertyAssign253", type=thingML_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
annotations255: BinaryAssociation = BinaryAssociation(
    name="annotations255",
    ends={
        Property(name="thingML_PlatformAnnotation257", type=thingML_ConfigPropertyAssign, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ConfigPropertyAssign256", type=thingML_PlatformAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lhs288: BinaryAssociation = BinaryAssociation(
    name="lhs288",
    ends={
        Property(name="thingML_Expression289", type=thingML_EqualsExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_EqualsExpression", type=thingML_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs290: BinaryAssociation = BinaryAssociation(
    name="rhs290",
    ends={
        Property(name="thingML_Expression292", type=thingML_EqualsExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_EqualsExpression291", type=thingML_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
srv262: BinaryAssociation = BinaryAssociation(
    name="srv262",
    ends={
        Property(name="thingML_InstanceRef264", type=thingML_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Connector263", type=thingML_InstanceRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
provided265: BinaryAssociation = BinaryAssociation(
    name="provided265",
    ends={
        Property(name="thingML_ProvidedPort", type=thingML_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Connector266", type=thingML_ProvidedPort, multiplicity=Multiplicity(1, 1))
    }
)
inst267: BinaryAssociation = BinaryAssociation(
    name="inst267",
    ends={
        Property(name="thingML_InstanceRef268", type=thingML_ExternalConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ExternalConnector", type=thingML_InstanceRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
port269: BinaryAssociation = BinaryAssociation(
    name="port269",
    ends={
        Property(name="thingML_Port271", type=thingML_ExternalConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ExternalConnector270", type=thingML_Port, multiplicity=Multiplicity(1, 1))
    }
)
protocol272: BinaryAssociation = BinaryAssociation(
    name="protocol272",
    ends={
        Property(name="thingML_Protocol274", type=thingML_ExternalConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ExternalConnector273", type=thingML_Protocol, multiplicity=Multiplicity(1, 1))
    }
)
instance275: BinaryAssociation = BinaryAssociation(
    name="instance275",
    ends={
        Property(name="thingML_Instance277", type=thingML_InstanceRef, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_InstanceRef276", type=thingML_Instance, multiplicity=Multiplicity(1, 1))
    }
)
lhs278: BinaryAssociation = BinaryAssociation(
    name="lhs278",
    ends={
        Property(name="thingML_Expression279", type=thingML_OrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_OrExpression", type=thingML_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs280: BinaryAssociation = BinaryAssociation(
    name="rhs280",
    ends={
        Property(name="thingML_Expression282", type=thingML_OrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_OrExpression281", type=thingML_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs283: BinaryAssociation = BinaryAssociation(
    name="lhs283",
    ends={
        Property(name="thingML_Expression284", type=thingML_AndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_AndExpression", type=thingML_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs285: BinaryAssociation = BinaryAssociation(
    name="rhs285",
    ends={
        Property(name="thingML_Expression287", type=thingML_AndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_AndExpression286", type=thingML_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs318: BinaryAssociation = BinaryAssociation(
    name="lhs318",
    ends={
        Property(name="thingML_Expression319", type=thingML_PlusExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_PlusExpression", type=thingML_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs320: BinaryAssociation = BinaryAssociation(
    name="rhs320",
    ends={
        Property(name="thingML_Expression322", type=thingML_PlusExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_PlusExpression321", type=thingML_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs293: BinaryAssociation = BinaryAssociation(
    name="lhs293",
    ends={
        Property(name="thingML_Expression294", type=thingML_NotEqualsExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_NotEqualsExpression", type=thingML_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs295: BinaryAssociation = BinaryAssociation(
    name="rhs295",
    ends={
        Property(name="thingML_Expression297", type=thingML_NotEqualsExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_NotEqualsExpression296", type=thingML_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs298: BinaryAssociation = BinaryAssociation(
    name="lhs298",
    ends={
        Property(name="thingML_Expression299", type=thingML_GreaterExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_GreaterExpression", type=thingML_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs300: BinaryAssociation = BinaryAssociation(
    name="rhs300",
    ends={
        Property(name="thingML_Expression302", type=thingML_GreaterExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_GreaterExpression301", type=thingML_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs303: BinaryAssociation = BinaryAssociation(
    name="lhs303",
    ends={
        Property(name="thingML_Expression304", type=thingML_LowerExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_LowerExpression", type=thingML_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs305: BinaryAssociation = BinaryAssociation(
    name="rhs305",
    ends={
        Property(name="thingML_Expression307", type=thingML_LowerExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_LowerExpression306", type=thingML_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs308: BinaryAssociation = BinaryAssociation(
    name="lhs308",
    ends={
        Property(name="thingML_Expression309", type=thingML_GreaterOrEqualExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_GreaterOrEqualExpression", type=thingML_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs310: BinaryAssociation = BinaryAssociation(
    name="rhs310",
    ends={
        Property(name="thingML_Expression312", type=thingML_GreaterOrEqualExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_GreaterOrEqualExpression311", type=thingML_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs313: BinaryAssociation = BinaryAssociation(
    name="lhs313",
    ends={
        Property(name="thingML_Expression314", type=thingML_LowerOrEqualExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_LowerOrEqualExpression", type=thingML_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs315: BinaryAssociation = BinaryAssociation(
    name="rhs315",
    ends={
        Property(name="thingML_Expression317", type=thingML_LowerOrEqualExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_LowerOrEqualExpression316", type=thingML_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs323: BinaryAssociation = BinaryAssociation(
    name="lhs323",
    ends={
        Property(name="thingML_Expression324", type=thingML_MinusExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_MinusExpression", type=thingML_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs325: BinaryAssociation = BinaryAssociation(
    name="rhs325",
    ends={
        Property(name="thingML_Expression327", type=thingML_MinusExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_MinusExpression326", type=thingML_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
array347: BinaryAssociation = BinaryAssociation(
    name="array347",
    ends={
        Property(name="thingML_Expression348", type=thingML_ArrayIndex, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ArrayIndex", type=thingML_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs328: BinaryAssociation = BinaryAssociation(
    name="lhs328",
    ends={
        Property(name="thingML_Expression329", type=thingML_TimesExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_TimesExpression", type=thingML_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs330: BinaryAssociation = BinaryAssociation(
    name="rhs330",
    ends={
        Property(name="thingML_Expression332", type=thingML_TimesExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_TimesExpression331", type=thingML_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs333: BinaryAssociation = BinaryAssociation(
    name="lhs333",
    ends={
        Property(name="thingML_Expression334", type=thingML_DivExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_DivExpression", type=thingML_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs335: BinaryAssociation = BinaryAssociation(
    name="rhs335",
    ends={
        Property(name="thingML_Expression337", type=thingML_DivExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_DivExpression336", type=thingML_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs338: BinaryAssociation = BinaryAssociation(
    name="lhs338",
    ends={
        Property(name="thingML_Expression339", type=thingML_ModExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ModExpression", type=thingML_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rhs340: BinaryAssociation = BinaryAssociation(
    name="rhs340",
    ends={
        Property(name="thingML_Expression342", type=thingML_ModExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ModExpression341", type=thingML_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
term343: BinaryAssociation = BinaryAssociation(
    name="term343",
    ends={
        Property(name="thingML_Expression344", type=thingML_NotExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_NotExpression", type=thingML_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
term345: BinaryAssociation = BinaryAssociation(
    name="term345",
    ends={
        Property(name="thingML_Expression346", type=thingML_UnaryMinus, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_UnaryMinus", type=thingML_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
index349: BinaryAssociation = BinaryAssociation(
    name="index349",
    ends={
        Property(name="thingML_Expression351", type=thingML_ArrayIndex, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ArrayIndex350", type=thingML_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_thingML_PropertyAssign_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingML_PropertyAssign)
gen_thingML_Type_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingML_Type)
gen_thingML_PrimitiveType_Type = Generalization(general=Type, specific=thingML_PrimitiveType)
gen_thingML_ObjectType_Type = Generalization(general=Type, specific=thingML_ObjectType)
gen_thingML_Enumeration_Type = Generalization(general=Type, specific=thingML_Enumeration)
gen_thingML_Thing_Type = Generalization(general=Type, specific=thingML_Thing)
gen_thingML_Parameter_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingML_Parameter)
gen_thingML_Parameter_ReferencedElmt = Generalization(general=ReferencedElmt, specific=thingML_Parameter)
gen_thingML_Parameter_Variable = Generalization(general=Variable, specific=thingML_Parameter)
gen_thingML_Port_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingML_Port)
gen_thingML_RequiredPort_Port = Generalization(general=Port, specific=thingML_RequiredPort)
gen_thingML_Protocol_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingML_Protocol)
gen_thingML_Function_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingML_Function)
gen_thingML_Property_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingML_Property)
gen_thingML_Property_ReferencedElmt = Generalization(general=ReferencedElmt, specific=thingML_Property)
gen_thingML_Property_Variable = Generalization(general=Variable, specific=thingML_Property)
gen_thingML_Message_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingML_Message)
gen_thingML_Message_ReferencedElmt = Generalization(general=ReferencedElmt, specific=thingML_Message)
gen_thingML_MergeSources_Source = Generalization(general=Source, specific=thingML_MergeSources)
gen_thingML_MergeSources_ReferencedElmt = Generalization(general=ReferencedElmt, specific=thingML_MergeSources)
gen_thingML_SimpleSource_Source = Generalization(general=Source, specific=thingML_SimpleSource)
gen_thingML_SimpleSource_ReferencedElmt = Generalization(general=ReferencedElmt, specific=thingML_SimpleSource)
gen_thingML_ProvidedPort_Port = Generalization(general=Port, specific=thingML_ProvidedPort)
gen_thingML_InternalPort_Port = Generalization(general=Port, specific=thingML_InternalPort)
gen_thingML_Stream_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingML_Stream)
gen_thingML_JoinSources_Source = Generalization(general=Source, specific=thingML_JoinSources)
gen_thingML_JoinSources_ReferencedElmt = Generalization(general=ReferencedElmt, specific=thingML_JoinSources)
gen_thingML_SimpleParamRef_ElmtProperty = Generalization(general=ElmtProperty, specific=thingML_SimpleParamRef)
gen_thingML_ArrayParamRef_ElmtProperty = Generalization(general=ElmtProperty, specific=thingML_ArrayParamRef)
gen_thingML_LengthArray_ElmtProperty = Generalization(general=ElmtProperty, specific=thingML_LengthArray)
gen_thingML_CompositeState_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingML_CompositeState)
gen_thingML_CompositeState_Region = Generalization(general=Region, specific=thingML_CompositeState)
gen_thingML_CompositeState_State = Generalization(general=State, specific=thingML_CompositeState)
gen_thingML_Filter_ViewSource = Generalization(general=ViewSource, specific=thingML_Filter)
gen_thingML_LengthWindow_ViewSource = Generalization(general=ViewSource, specific=thingML_LengthWindow)
gen_thingML_TimeWindow_ViewSource = Generalization(general=ViewSource, specific=thingML_TimeWindow)
gen_thingML_MessageParameter_ReferencedElmt = Generalization(general=ReferencedElmt, specific=thingML_MessageParameter)
gen_thingML_ParallelRegion_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingML_ParallelRegion)
gen_thingML_ParallelRegion_Region = Generalization(general=Region, specific=thingML_ParallelRegion)
gen_thingML_FinalState_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingML_FinalState)
gen_thingML_FinalState_State = Generalization(general=State, specific=thingML_FinalState)
gen_thingML_InternalTransition_Handler = Generalization(general=Handler, specific=thingML_InternalTransition)
gen_thingML_Session_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingML_Session)
gen_thingML_Session_Region = Generalization(general=Region, specific=thingML_Session)
gen_thingML_Session_State = Generalization(general=State, specific=thingML_Session)
gen_thingML_ReceiveMessage_ReferencedElmt = Generalization(general=ReferencedElmt, specific=thingML_ReceiveMessage)
gen_thingML_ReceiveMessage_Event = Generalization(general=Event, specific=thingML_ReceiveMessage)
gen_thingML_State_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingML_State)
gen_thingML_Handler_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingML_Handler)
gen_thingML_Transition_Handler = Generalization(general=Handler, specific=thingML_Transition)
gen_thingML_SendAction_Action = Generalization(general=Action, specific=thingML_SendAction)
gen_thingML_ActionBlock_Action = Generalization(general=Action, specific=thingML_ActionBlock)
gen_thingML_ExternStatement_Action = Generalization(general=Action, specific=thingML_ExternStatement)
gen_thingML_LocalVariable_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingML_LocalVariable)
gen_thingML_LocalVariable_ReferencedElmt = Generalization(general=ReferencedElmt, specific=thingML_LocalVariable)
gen_thingML_LocalVariable_Action = Generalization(general=Action, specific=thingML_LocalVariable)
gen_thingML_LocalVariable_Variable = Generalization(general=Variable, specific=thingML_LocalVariable)
gen_thingML_ReturnAction_Action = Generalization(general=Action, specific=thingML_ReturnAction)
gen_thingML_PrintAction_Action = Generalization(general=Action, specific=thingML_PrintAction)
gen_thingML_VariableAssignment_Action = Generalization(general=Action, specific=thingML_VariableAssignment)
gen_thingML_Increment_Action = Generalization(general=Action, specific=thingML_Increment)
gen_thingML_Decrement_Action = Generalization(general=Action, specific=thingML_Decrement)
gen_thingML_LoopAction_Action = Generalization(general=Action, specific=thingML_LoopAction)
gen_thingML_ConditionalAction_Action = Generalization(general=Action, specific=thingML_ConditionalAction)
gen_thingML_Reference_Expression = Generalization(general=Expression, specific=thingML_Reference)
gen_thingML_FunctionCallExpression_Expression = Generalization(general=Expression, specific=thingML_FunctionCallExpression)
gen_thingML_ErrorAction_Action = Generalization(general=Action, specific=thingML_ErrorAction)
gen_thingML_StartSession_Action = Generalization(general=Action, specific=thingML_StartSession)
gen_thingML_FunctionCallStatement_Action = Generalization(general=Action, specific=thingML_FunctionCallStatement)
gen_thingML_ExternExpression_Expression = Generalization(general=Expression, specific=thingML_ExternExpression)
gen_thingML_EnumLiteralRef_Expression = Generalization(general=Expression, specific=thingML_EnumLiteralRef)
gen_thingML_IntegerLiteral_Expression = Generalization(general=Expression, specific=thingML_IntegerLiteral)
gen_thingML_BooleanLiteral_Expression = Generalization(general=Expression, specific=thingML_BooleanLiteral)
gen_thingML_StringLiteral_Expression = Generalization(general=Expression, specific=thingML_StringLiteral)
gen_thingML_DoubleLiteral_Expression = Generalization(general=Expression, specific=thingML_DoubleLiteral)
gen_thingML_PropertyReference_Expression = Generalization(general=Expression, specific=thingML_PropertyReference)
gen_thingML_Connector_AbstractConnector = Generalization(general=AbstractConnector, specific=thingML_Connector)
gen_thingML_Configuration_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingML_Configuration)
gen_thingML_Instance_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingML_Instance)
gen_thingML_AbstractConnector_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingML_AbstractConnector)
gen_thingML_NotEqualsExpression_Expression = Generalization(general=Expression, specific=thingML_NotEqualsExpression)
gen_thingML_ExternalConnector_AbstractConnector = Generalization(general=AbstractConnector, specific=thingML_ExternalConnector)
gen_thingML_OrExpression_Expression = Generalization(general=Expression, specific=thingML_OrExpression)
gen_thingML_AndExpression_Expression = Generalization(general=Expression, specific=thingML_AndExpression)
gen_thingML_EqualsExpression_Expression = Generalization(general=Expression, specific=thingML_EqualsExpression)
gen_thingML_PlusExpression_Expression = Generalization(general=Expression, specific=thingML_PlusExpression)
gen_thingML_GreaterExpression_Expression = Generalization(general=Expression, specific=thingML_GreaterExpression)
gen_thingML_LowerExpression_Expression = Generalization(general=Expression, specific=thingML_LowerExpression)
gen_thingML_GreaterOrEqualExpression_Expression = Generalization(general=Expression, specific=thingML_GreaterOrEqualExpression)
gen_thingML_LowerOrEqualExpression_Expression = Generalization(general=Expression, specific=thingML_LowerOrEqualExpression)
gen_thingML_MinusExpression_Expression = Generalization(general=Expression, specific=thingML_MinusExpression)
gen_thingML_TimesExpression_Expression = Generalization(general=Expression, specific=thingML_TimesExpression)
gen_thingML_DivExpression_Expression = Generalization(general=Expression, specific=thingML_DivExpression)
gen_thingML_ModExpression_Expression = Generalization(general=Expression, specific=thingML_ModExpression)
gen_thingML_NotExpression_Expression = Generalization(general=Expression, specific=thingML_NotExpression)
gen_thingML_UnaryMinus_Expression = Generalization(general=Expression, specific=thingML_UnaryMinus)
gen_thingML_ArrayIndex_Expression = Generalization(general=Expression, specific=thingML_ArrayIndex)

# Domain Model
domain_model = DomainModel(
    name="thingML",
    types={thingML_Protocol, thingML_Configuration, thingML_PlatformAnnotation, thingML_AnnotatedElement, thingML_TypeRef, thingML_Expression, thingML_ThingMLModel, thingML_Import, thingML_Type, thingML_Message, thingML_Port, thingML_Property, thingML_Function, thingML_PropertyAssign, thingML_CompositeState, thingML_Stream, AnnotatedElement, thingML_PrimitiveType, Type, thingML_ObjectType, thingML_Enumeration, thingML_EnumerationLiteral, thingML_Thing, thingML_RequiredPort, Port, thingML_Parameter, thingML_ActionBlock, ReferencedElmt, Variable, thingML_MergeSources, thingML_SimpleSource, thingML_ProvidedPort, thingML_InternalPort, thingML_Source, thingML_LocalVariable, thingML_SendAction, thingML_ViewSource, thingML_ReferencedElmt, thingML_ElmtProperty, thingML_JoinSources, Source, thingML_SimpleParamRef, ElmtProperty, thingML_ArrayParamRef, thingML_LengthArray, thingML_Region, Region, State, thingML_State, thingML_ReceiveMessage, thingML_Filter, ViewSource, thingML_LengthWindow, thingML_TimeWindow, thingML_MessageParameter, thingML_ParallelRegion, thingML_FinalState, thingML_Session, Event, thingML_Action, thingML_InternalTransition, thingML_Transition, thingML_Handler, thingML_Event, Handler, thingML_Variable, Action, thingML_ExternStatement, thingML_ReturnAction, thingML_PrintAction, thingML_VariableAssignment, thingML_Increment, thingML_Decrement, thingML_LoopAction, thingML_ConditionalAction, thingML_Reference, thingML_FunctionCallExpression, thingML_ErrorAction, thingML_StartSession, thingML_FunctionCallStatement, thingML_ExternExpression, Expression, thingML_EnumLiteralRef, thingML_IntegerLiteral, thingML_BooleanLiteral, thingML_StringLiteral, thingML_DoubleLiteral, thingML_PropertyReference, thingML_Connector, AbstractConnector, thingML_Instance, thingML_AbstractConnector, thingML_ConfigPropertyAssign, thingML_InstanceRef, thingML_NotEqualsExpression, thingML_ExternalConnector, thingML_OrExpression, thingML_AndExpression, thingML_EqualsExpression, thingML_PlusExpression, thingML_MinusExpression, thingML_GreaterExpression, thingML_LowerExpression, thingML_GreaterOrEqualExpression, thingML_LowerOrEqualExpression, thingML_TimesExpression, thingML_DivExpression, thingML_ModExpression, thingML_NotExpression, thingML_UnaryMinus, thingML_ArrayIndex},
    associations={protocols3, configs5, annotations7, type8, imports0, types1, includes17, messages18, ports20, properties22, functions24, assign26, behaviour28, streams30, property32, cardinality10, literals12, annotations13, parameters54, typeRef57, sends60, receives63, index35, init38, parameters41, typeRef43, body46, typeRef48, init51, resultMessage74, rules77, operators80, sources82, resultMessage84, operators87, input66, selection68, output70, sources72, msgRef106, parameterRef108, parameterRef110, initial112, message90, operators91, guard94, size96, step98, duration101, step103, substate114, region117, target152, initial127, substate130, initial119, substate121, region124, properties133, entry136, exit138, internal141, outgoing143, event145, guard146, action149, typeRef166, init169, port172, port155, message158, actions161, segments164, elseAction202, exp205, message175, parameters178, property181, index182, expression185, var188, var190, condition192, action194, condition197, action199, reference227, parameter228, msg207, msg209, session211, function213, parameters215, segments218, enum220, literal222, property225, cli258, required260, function230, parameters232, instances235, connectors237, propassigns239, type241, instance244, property246, index249, init252, annotations255, lhs288, rhs290, srv262, provided265, inst267, port269, protocol272, instance275, lhs278, rhs280, lhs283, rhs285, lhs318, rhs320, lhs293, rhs295, lhs298, rhs300, lhs303, rhs305, lhs308, rhs310, lhs313, rhs315, lhs323, rhs325, array347, lhs328, rhs330, lhs333, rhs335, lhs338, rhs340, term343, term345, index349},
    generalizations={gen_thingML_PropertyAssign_AnnotatedElement, gen_thingML_Type_AnnotatedElement, gen_thingML_PrimitiveType_Type, gen_thingML_ObjectType_Type, gen_thingML_Enumeration_Type, gen_thingML_Thing_Type, gen_thingML_Parameter_AnnotatedElement, gen_thingML_Parameter_ReferencedElmt, gen_thingML_Parameter_Variable, gen_thingML_Port_AnnotatedElement, gen_thingML_RequiredPort_Port, gen_thingML_Protocol_AnnotatedElement, gen_thingML_Function_AnnotatedElement, gen_thingML_Property_AnnotatedElement, gen_thingML_Property_ReferencedElmt, gen_thingML_Property_Variable, gen_thingML_Message_AnnotatedElement, gen_thingML_Message_ReferencedElmt, gen_thingML_MergeSources_Source, gen_thingML_MergeSources_ReferencedElmt, gen_thingML_SimpleSource_Source, gen_thingML_SimpleSource_ReferencedElmt, gen_thingML_ProvidedPort_Port, gen_thingML_InternalPort_Port, gen_thingML_Stream_AnnotatedElement, gen_thingML_JoinSources_Source, gen_thingML_JoinSources_ReferencedElmt, gen_thingML_SimpleParamRef_ElmtProperty, gen_thingML_ArrayParamRef_ElmtProperty, gen_thingML_LengthArray_ElmtProperty, gen_thingML_CompositeState_AnnotatedElement, gen_thingML_CompositeState_Region, gen_thingML_CompositeState_State, gen_thingML_Filter_ViewSource, gen_thingML_LengthWindow_ViewSource, gen_thingML_TimeWindow_ViewSource, gen_thingML_MessageParameter_ReferencedElmt, gen_thingML_ParallelRegion_AnnotatedElement, gen_thingML_ParallelRegion_Region, gen_thingML_FinalState_AnnotatedElement, gen_thingML_FinalState_State, gen_thingML_InternalTransition_Handler, gen_thingML_Session_AnnotatedElement, gen_thingML_Session_Region, gen_thingML_Session_State, gen_thingML_ReceiveMessage_ReferencedElmt, gen_thingML_ReceiveMessage_Event, gen_thingML_State_AnnotatedElement, gen_thingML_Handler_AnnotatedElement, gen_thingML_Transition_Handler, gen_thingML_SendAction_Action, gen_thingML_ActionBlock_Action, gen_thingML_ExternStatement_Action, gen_thingML_LocalVariable_AnnotatedElement, gen_thingML_LocalVariable_ReferencedElmt, gen_thingML_LocalVariable_Action, gen_thingML_LocalVariable_Variable, gen_thingML_ReturnAction_Action, gen_thingML_PrintAction_Action, gen_thingML_VariableAssignment_Action, gen_thingML_Increment_Action, gen_thingML_Decrement_Action, gen_thingML_LoopAction_Action, gen_thingML_ConditionalAction_Action, gen_thingML_Reference_Expression, gen_thingML_FunctionCallExpression_Expression, gen_thingML_ErrorAction_Action, gen_thingML_StartSession_Action, gen_thingML_FunctionCallStatement_Action, gen_thingML_ExternExpression_Expression, gen_thingML_EnumLiteralRef_Expression, gen_thingML_IntegerLiteral_Expression, gen_thingML_BooleanLiteral_Expression, gen_thingML_StringLiteral_Expression, gen_thingML_DoubleLiteral_Expression, gen_thingML_PropertyReference_Expression, gen_thingML_Connector_AbstractConnector, gen_thingML_Configuration_AnnotatedElement, gen_thingML_Instance_AnnotatedElement, gen_thingML_AbstractConnector_AnnotatedElement, gen_thingML_NotEqualsExpression_Expression, gen_thingML_ExternalConnector_AbstractConnector, gen_thingML_OrExpression_Expression, gen_thingML_AndExpression_Expression, gen_thingML_EqualsExpression_Expression, gen_thingML_PlusExpression_Expression, gen_thingML_GreaterExpression_Expression, gen_thingML_LowerExpression_Expression, gen_thingML_GreaterOrEqualExpression_Expression, gen_thingML_LowerOrEqualExpression_Expression, gen_thingML_MinusExpression_Expression, gen_thingML_TimesExpression_Expression, gen_thingML_DivExpression_Expression, gen_thingML_ModExpression_Expression, gen_thingML_NotExpression_Expression, gen_thingML_UnaryMinus_Expression, gen_thingML_ArrayIndex_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)