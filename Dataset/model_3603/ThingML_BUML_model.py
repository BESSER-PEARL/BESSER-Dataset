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
thingML_ThingMLModel = Class(name="thingML::ThingMLModel")
thingML_Import = Class(name="thingML::Import")
thingML_Type = Class(name="thingML::Type")
thingML_Protocol = Class(name="thingML::Protocol")
thingML_Expression = Class(name="thingML::Expression")
thingML_PrimitiveType = Class(name="thingML::PrimitiveType")
Type = Class(name="Type")
thingML_ObjectType = Class(name="thingML::ObjectType")
thingML_Enumeration = Class(name="thingML::Enumeration")
thingML_EnumerationLiteral = Class(name="thingML::EnumerationLiteral")
thingML_Literal = Class(name="thingML::Literal")
thingML_Thing = Class(name="thingML::Thing")
thingML_Message = Class(name="thingML::Message")
thingML_Configuration = Class(name="thingML::Configuration")
thingML_PlatformAnnotation = Class(name="thingML::PlatformAnnotation")
thingML_NamedElement = Class(name="thingML::NamedElement")
thingML_AnnotatedElement = Class(name="thingML::AnnotatedElement")
thingML_Variable = Class(name="thingML::Variable")
NamedElement = Class(name="NamedElement")
AnnotatedElement = Class(name="AnnotatedElement")
thingML_TypeRef = Class(name="thingML::TypeRef")
thingML_CompositeState = Class(name="thingML::CompositeState")
thingML_Parameter = Class(name="thingML::Parameter")
thingML_Action = Class(name="thingML::Action")
thingML_Port = Class(name="thingML::Port")
thingML_Property = Class(name="thingML::Property")
thingML_Function = Class(name="thingML::Function")
thingML_PropertyAssign = Class(name="thingML::PropertyAssign")
thingML_InternalPort = Class(name="thingML::InternalPort")
thingML_State = Class(name="thingML::State")
thingML_InternalTransition = Class(name="thingML::InternalTransition")
thingML_Transition = Class(name="thingML::Transition")
thingML_Handler = Class(name="thingML::Handler")
thingML_Event = Class(name="thingML::Event")
Variable = Class(name="Variable")
thingML_RequiredPort = Class(name="thingML::RequiredPort")
Port = Class(name="Port")
thingML_ProvidedPort = Class(name="thingML::ProvidedPort")
thingML_ReceiveMessage = Class(name="thingML::ReceiveMessage")
Event = Class(name="Event")
thingML_ActionBlock = Class(name="thingML::ActionBlock")
Action = Class(name="Action")
thingML_ExternStatement = Class(name="thingML::ExternStatement")
thingML_LocalVariable = Class(name="thingML::LocalVariable")
Handler = Class(name="Handler")
State = Class(name="State")
StateContainer = Class(name="StateContainer")
thingML_Region = Class(name="thingML::Region")
thingML_Session = Class(name="thingML::Session")
thingML_FinalState = Class(name="thingML::FinalState")
thingML_StateContainer = Class(name="thingML::StateContainer")
thingML_Increment = Class(name="thingML::Increment")
thingML_Decrement = Class(name="thingML::Decrement")
thingML_ForAction = Class(name="thingML::ForAction")
thingML_PropertyReference = Class(name="thingML::PropertyReference")
thingML_LoopAction = Class(name="thingML::LoopAction")
thingML_SendAction = Class(name="thingML::SendAction")
thingML_VariableAssignment = Class(name="thingML::VariableAssignment")
thingML_ErrorAction = Class(name="thingML::ErrorAction")
thingML_StartSession = Class(name="thingML::StartSession")
thingML_FunctionCallStatement = Class(name="thingML::FunctionCallStatement")
thingML_ExternExpression = Class(name="thingML::ExternExpression")
Expression = Class(name="Expression")
thingML_ConditionalAction = Class(name="thingML::ConditionalAction")
thingML_ReturnAction = Class(name="thingML::ReturnAction")
thingML_PrintAction = Class(name="thingML::PrintAction")
thingML_BooleanLiteral = Class(name="thingML::BooleanLiteral")
thingML_StringLiteral = Class(name="thingML::StringLiteral")
thingML_DoubleLiteral = Class(name="thingML::DoubleLiteral")
thingML_EventReference = Class(name="thingML::EventReference")
thingML_FunctionCallExpression = Class(name="thingML::FunctionCallExpression")
thingML_ArrayInit = Class(name="thingML::ArrayInit")
thingML_EnumLiteralRef = Class(name="thingML::EnumLiteralRef")
Literal = Class(name="Literal")
thingML_ByteLiteral = Class(name="thingML::ByteLiteral")
thingML_CharLiteral = Class(name="thingML::CharLiteral")
thingML_IntegerLiteral = Class(name="thingML::IntegerLiteral")
thingML_AbstractConnector = Class(name="thingML::AbstractConnector")
thingML_ConfigPropertyAssign = Class(name="thingML::ConfigPropertyAssign")
thingML_Instance = Class(name="thingML::Instance")
thingML_ExternalConnector = Class(name="thingML::ExternalConnector")
thingML_OrExpression = Class(name="thingML::OrExpression")
thingML_Connector = Class(name="thingML::Connector")
AbstractConnector = Class(name="AbstractConnector")
thingML_NotEqualsExpression = Class(name="thingML::NotEqualsExpression")
thingML_GreaterExpression = Class(name="thingML::GreaterExpression")
thingML_AndExpression = Class(name="thingML::AndExpression")
thingML_EqualsExpression = Class(name="thingML::EqualsExpression")
thingML_GreaterOrEqualExpression = Class(name="thingML::GreaterOrEqualExpression")
thingML_LowerOrEqualExpression = Class(name="thingML::LowerOrEqualExpression")
thingML_LowerExpression = Class(name="thingML::LowerExpression")
thingML_TimesExpression = Class(name="thingML::TimesExpression")
thingML_DivExpression = Class(name="thingML::DivExpression")
thingML_PlusExpression = Class(name="thingML::PlusExpression")
thingML_MinusExpression = Class(name="thingML::MinusExpression")
thingML_CastExpression = Class(name="thingML::CastExpression")
thingML_ExpressionGroup = Class(name="thingML::ExpressionGroup")
thingML_ModExpression = Class(name="thingML::ModExpression")
thingML_ArrayIndex = Class(name="thingML::ArrayIndex")
thingML_NotExpression = Class(name="thingML::NotExpression")
thingML_UnaryMinus = Class(name="thingML::UnaryMinus")

# thingML_ThingMLModel class attributes and methods

# thingML_Import class attributes and methods
thingML_Import_importURI: Property = Property(name="importURI", type=StringType)
thingML_Import_from: Property = Property(name="from", type=StringType)
thingML_Import.attributes={thingML_Import_from, thingML_Import_importURI}

# thingML_Type class attributes and methods

# thingML_Protocol class attributes and methods

# thingML_Expression class attributes and methods

# thingML_PrimitiveType class attributes and methods
thingML_PrimitiveType_ByteSize: Property = Property(name="ByteSize", type=StringType)
thingML_PrimitiveType.attributes={thingML_PrimitiveType_ByteSize}

# Type class attributes and methods

# thingML_ObjectType class attributes and methods

# thingML_Enumeration class attributes and methods

# thingML_EnumerationLiteral class attributes and methods

# thingML_Literal class attributes and methods

# thingML_Thing class attributes and methods
thingML_Thing_fragment: Property = Property(name="fragment", type=BooleanType)
thingML_Thing.attributes={thingML_Thing_fragment}

# thingML_Message class attributes and methods

# thingML_Configuration class attributes and methods

# thingML_PlatformAnnotation class attributes and methods
thingML_PlatformAnnotation_name: Property = Property(name="name", type=StringType)
thingML_PlatformAnnotation_value: Property = Property(name="value", type=StringType)
thingML_PlatformAnnotation.attributes={thingML_PlatformAnnotation_name, thingML_PlatformAnnotation_value}

# thingML_NamedElement class attributes and methods
thingML_NamedElement_name: Property = Property(name="name", type=StringType)
thingML_NamedElement.attributes={thingML_NamedElement_name}

# thingML_AnnotatedElement class attributes and methods

# thingML_Variable class attributes and methods

# NamedElement class attributes and methods

# AnnotatedElement class attributes and methods

# thingML_TypeRef class attributes and methods
thingML_TypeRef_isArray: Property = Property(name="isArray", type=BooleanType)
thingML_TypeRef.attributes={thingML_TypeRef_isArray}

# thingML_CompositeState class attributes and methods

# thingML_Parameter class attributes and methods

# thingML_Action class attributes and methods

# thingML_Port class attributes and methods

# thingML_Property class attributes and methods
thingML_Property_readonly: Property = Property(name="readonly", type=BooleanType)
thingML_Property.attributes={thingML_Property_readonly}

# thingML_Function class attributes and methods
thingML_Function_abstract: Property = Property(name="abstract", type=BooleanType)
thingML_Function.attributes={thingML_Function_abstract}

# thingML_PropertyAssign class attributes and methods

# thingML_InternalPort class attributes and methods

# thingML_State class attributes and methods

# thingML_InternalTransition class attributes and methods

# thingML_Transition class attributes and methods

# thingML_Handler class attributes and methods

# thingML_Event class attributes and methods

# Variable class attributes and methods

# thingML_RequiredPort class attributes and methods
thingML_RequiredPort_optional: Property = Property(name="optional", type=BooleanType)
thingML_RequiredPort.attributes={thingML_RequiredPort_optional}

# Port class attributes and methods

# thingML_ProvidedPort class attributes and methods

# thingML_ReceiveMessage class attributes and methods

# Event class attributes and methods

# thingML_ActionBlock class attributes and methods

# Action class attributes and methods

# thingML_ExternStatement class attributes and methods
thingML_ExternStatement_statement: Property = Property(name="statement", type=StringType)
thingML_ExternStatement.attributes={thingML_ExternStatement_statement}

# thingML_LocalVariable class attributes and methods
thingML_LocalVariable_readonly: Property = Property(name="readonly", type=BooleanType)
thingML_LocalVariable.attributes={thingML_LocalVariable_readonly}

# Handler class attributes and methods

# State class attributes and methods

# StateContainer class attributes and methods

# thingML_Region class attributes and methods

# thingML_Session class attributes and methods

# thingML_FinalState class attributes and methods

# thingML_StateContainer class attributes and methods
thingML_StateContainer_history: Property = Property(name="history", type=BooleanType)
thingML_StateContainer.attributes={thingML_StateContainer_history}

# thingML_Increment class attributes and methods

# thingML_Decrement class attributes and methods

# thingML_ForAction class attributes and methods

# thingML_PropertyReference class attributes and methods

# thingML_LoopAction class attributes and methods

# thingML_SendAction class attributes and methods

# thingML_VariableAssignment class attributes and methods

# thingML_ErrorAction class attributes and methods
thingML_ErrorAction_line: Property = Property(name="line", type=BooleanType)
thingML_ErrorAction.attributes={thingML_ErrorAction_line}

# thingML_StartSession class attributes and methods

# thingML_FunctionCallStatement class attributes and methods

# thingML_ExternExpression class attributes and methods
thingML_ExternExpression_expression: Property = Property(name="expression", type=StringType)
thingML_ExternExpression.attributes={thingML_ExternExpression_expression}

# Expression class attributes and methods

# thingML_ConditionalAction class attributes and methods

# thingML_ReturnAction class attributes and methods

# thingML_PrintAction class attributes and methods
thingML_PrintAction_line: Property = Property(name="line", type=BooleanType)
thingML_PrintAction.attributes={thingML_PrintAction_line}

# thingML_BooleanLiteral class attributes and methods
thingML_BooleanLiteral_boolValue: Property = Property(name="boolValue", type=BooleanType)
thingML_BooleanLiteral.attributes={thingML_BooleanLiteral_boolValue}

# thingML_StringLiteral class attributes and methods
thingML_StringLiteral_stringValue: Property = Property(name="stringValue", type=StringType)
thingML_StringLiteral.attributes={thingML_StringLiteral_stringValue}

# thingML_DoubleLiteral class attributes and methods
thingML_DoubleLiteral_doubleValue: Property = Property(name="doubleValue", type=FloatType)
thingML_DoubleLiteral.attributes={thingML_DoubleLiteral_doubleValue}

# thingML_EventReference class attributes and methods

# thingML_FunctionCallExpression class attributes and methods

# thingML_ArrayInit class attributes and methods

# thingML_EnumLiteralRef class attributes and methods

# Literal class attributes and methods

# thingML_ByteLiteral class attributes and methods
thingML_ByteLiteral_byteValue: Property = Property(name="byteValue", type=StringType)
thingML_ByteLiteral.attributes={thingML_ByteLiteral_byteValue}

# thingML_CharLiteral class attributes and methods
thingML_CharLiteral_charValue: Property = Property(name="charValue", type=StringType)
thingML_CharLiteral.attributes={thingML_CharLiteral_charValue}

# thingML_IntegerLiteral class attributes and methods
thingML_IntegerLiteral_intValue: Property = Property(name="intValue", type=StringType)
thingML_IntegerLiteral.attributes={thingML_IntegerLiteral_intValue}

# thingML_AbstractConnector class attributes and methods

# thingML_ConfigPropertyAssign class attributes and methods

# thingML_Instance class attributes and methods

# thingML_ExternalConnector class attributes and methods

# thingML_OrExpression class attributes and methods

# thingML_Connector class attributes and methods

# AbstractConnector class attributes and methods

# thingML_NotEqualsExpression class attributes and methods

# thingML_GreaterExpression class attributes and methods

# thingML_AndExpression class attributes and methods

# thingML_EqualsExpression class attributes and methods

# thingML_GreaterOrEqualExpression class attributes and methods

# thingML_LowerOrEqualExpression class attributes and methods

# thingML_LowerExpression class attributes and methods

# thingML_TimesExpression class attributes and methods

# thingML_DivExpression class attributes and methods

# thingML_PlusExpression class attributes and methods

# thingML_MinusExpression class attributes and methods

# thingML_CastExpression class attributes and methods
thingML_CastExpression_isArray: Property = Property(name="isArray", type=BooleanType)
thingML_CastExpression.attributes={thingML_CastExpression_isArray}

# thingML_ExpressionGroup class attributes and methods

# thingML_ModExpression class attributes and methods

# thingML_ArrayIndex class attributes and methods

# thingML_NotExpression class attributes and methods

# thingML_UnaryMinus class attributes and methods

# Relationships
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
protocols3: BinaryAssociation = BinaryAssociation(
    name="protocols3",
    ends={
        Property(name="thingML_Protocol", type=thingML_ThingMLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ThingMLModel4", type=thingML_Protocol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cardinality12: BinaryAssociation = BinaryAssociation(
    name="cardinality12",
    ends={
        Property(name="thingML_Expression", type=thingML_TypeRef, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_TypeRef13", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeRef14: BinaryAssociation = BinaryAssociation(
    name="typeRef14",
    ends={
        Property(name="thingML_TypeRef15", type=thingML_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Enumeration", type=thingML_TypeRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
literals16: BinaryAssociation = BinaryAssociation(
    name="literals16",
    ends={
        Property(name="thingML_EnumerationLiteral", type=thingML_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Enumeration17", type=thingML_EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
init18: BinaryAssociation = BinaryAssociation(
    name="init18",
    ends={
        Property(name="thingML_Literal", type=thingML_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_EnumerationLiteral19", type=thingML_Literal, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
includes21: BinaryAssociation = BinaryAssociation(
    name="includes21",
    ends={
        Property(name="thingML_Thing", type=thingML_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Thing20", type=thingML_Thing, multiplicity=Multiplicity(0, 9999))
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
typeRef8: BinaryAssociation = BinaryAssociation(
    name="typeRef8",
    ends={
        Property(name="thingML_TypeRef", type=thingML_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Variable", type=thingML_TypeRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type9: BinaryAssociation = BinaryAssociation(
    name="type9",
    ends={
        Property(name="thingML_Type11", type=thingML_TypeRef, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_TypeRef10", type=thingML_Type, multiplicity=Multiplicity(0, 1))
    }
)
assign30: BinaryAssociation = BinaryAssociation(
    name="assign30",
    ends={
        Property(name="thingML_Thing31", type=thingML_PropertyAssign, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="thingML_PropertyAssign", type=thingML_Thing, multiplicity=Multiplicity(1, 1))
    }
)
behaviour32: BinaryAssociation = BinaryAssociation(
    name="behaviour32",
    ends={
        Property(name="thingML_CompositeState", type=thingML_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Thing33", type=thingML_CompositeState, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
property34: BinaryAssociation = BinaryAssociation(
    name="property34",
    ends={
        Property(name="thingML_Property36", type=thingML_PropertyAssign, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_PropertyAssign35", type=thingML_Property, multiplicity=Multiplicity(0, 1))
    }
)
index37: BinaryAssociation = BinaryAssociation(
    name="index37",
    ends={
        Property(name="thingML_Expression39", type=thingML_PropertyAssign, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_PropertyAssign38", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init40: BinaryAssociation = BinaryAssociation(
    name="init40",
    ends={
        Property(name="thingML_Expression42", type=thingML_PropertyAssign, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_PropertyAssign41", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters43: BinaryAssociation = BinaryAssociation(
    name="parameters43",
    ends={
        Property(name="thingML_Parameter", type=thingML_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Function44", type=thingML_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeRef45: BinaryAssociation = BinaryAssociation(
    name="typeRef45",
    ends={
        Property(name="thingML_TypeRef47", type=thingML_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Function46", type=thingML_TypeRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body48: BinaryAssociation = BinaryAssociation(
    name="body48",
    ends={
        Property(name="thingML_Action", type=thingML_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Function49", type=thingML_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
messages22: BinaryAssociation = BinaryAssociation(
    name="messages22",
    ends={
        Property(name="thingML_Message", type=thingML_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Thing23", type=thingML_Message, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ports24: BinaryAssociation = BinaryAssociation(
    name="ports24",
    ends={
        Property(name="thingML_Port", type=thingML_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Thing25", type=thingML_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties26: BinaryAssociation = BinaryAssociation(
    name="properties26",
    ends={
        Property(name="thingML_Property", type=thingML_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Thing27", type=thingML_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functions28: BinaryAssociation = BinaryAssociation(
    name="functions28",
    ends={
        Property(name="thingML_Function", type=thingML_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Thing29", type=thingML_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties62: BinaryAssociation = BinaryAssociation(
    name="properties62",
    ends={
        Property(name="thingML_Property63", type=thingML_State, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_State", type=thingML_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entry64: BinaryAssociation = BinaryAssociation(
    name="entry64",
    ends={
        Property(name="thingML_Action66", type=thingML_State, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_State65", type=thingML_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exit67: BinaryAssociation = BinaryAssociation(
    name="exit67",
    ends={
        Property(name="thingML_Action69", type=thingML_State, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_State68", type=thingML_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
internal70: BinaryAssociation = BinaryAssociation(
    name="internal70",
    ends={
        Property(name="thingML_InternalTransition", type=thingML_State, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_State71", type=thingML_InternalTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outgoing72: BinaryAssociation = BinaryAssociation(
    name="outgoing72",
    ends={
        Property(name="thingML_Transition", type=thingML_State, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_State73", type=thingML_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event74: BinaryAssociation = BinaryAssociation(
    name="event74",
    ends={
        Property(name="thingML_Event", type=thingML_Handler, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Handler", type=thingML_Event, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
guard75: BinaryAssociation = BinaryAssociation(
    name="guard75",
    ends={
        Property(name="thingML_Expression77", type=thingML_Handler, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Handler76", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action78: BinaryAssociation = BinaryAssociation(
    name="action78",
    ends={
        Property(name="thingML_Action80", type=thingML_Handler, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Handler79", type=thingML_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init50: BinaryAssociation = BinaryAssociation(
    name="init50",
    ends={
        Property(name="thingML_Expression52", type=thingML_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Property51", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters53: BinaryAssociation = BinaryAssociation(
    name="parameters53",
    ends={
        Property(name="thingML_Parameter55", type=thingML_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Message54", type=thingML_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sends56: BinaryAssociation = BinaryAssociation(
    name="sends56",
    ends={
        Property(name="thingML_Message58", type=thingML_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Port57", type=thingML_Message, multiplicity=Multiplicity(0, 9999))
    }
)
receives59: BinaryAssociation = BinaryAssociation(
    name="receives59",
    ends={
        Property(name="thingML_Message61", type=thingML_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Port60", type=thingML_Message, multiplicity=Multiplicity(0, 9999))
    }
)
initial91: BinaryAssociation = BinaryAssociation(
    name="initial91",
    ends={
        Property(name="thingML_State92", type=thingML_StateContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_StateContainer", type=thingML_State, multiplicity=Multiplicity(0, 1))
    }
)
substate93: BinaryAssociation = BinaryAssociation(
    name="substate93",
    ends={
        Property(name="thingML_State95", type=thingML_StateContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_StateContainer94", type=thingML_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
port96: BinaryAssociation = BinaryAssociation(
    name="port96",
    ends={
        Property(name="thingML_Port97", type=thingML_ReceiveMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ReceiveMessage", type=thingML_Port, multiplicity=Multiplicity(0, 1))
    }
)
message98: BinaryAssociation = BinaryAssociation(
    name="message98",
    ends={
        Property(name="thingML_Message100", type=thingML_ReceiveMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ReceiveMessage99", type=thingML_Message, multiplicity=Multiplicity(0, 1))
    }
)
actions101: BinaryAssociation = BinaryAssociation(
    name="actions101",
    ends={
        Property(name="thingML_Action102", type=thingML_ActionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ActionBlock", type=thingML_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
segments103: BinaryAssociation = BinaryAssociation(
    name="segments103",
    ends={
        Property(name="thingML_Expression104", type=thingML_ExternStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ExternStatement", type=thingML_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target81: BinaryAssociation = BinaryAssociation(
    name="target81",
    ends={
        Property(name="thingML_State83", type=thingML_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Transition82", type=thingML_State, multiplicity=Multiplicity(0, 1))
    }
)
region84: BinaryAssociation = BinaryAssociation(
    name="region84",
    ends={
        Property(name="thingML_Region", type=thingML_CompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_CompositeState85", type=thingML_Region, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
session86: BinaryAssociation = BinaryAssociation(
    name="session86",
    ends={
        Property(name="thingML_Session", type=thingML_CompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_CompositeState87", type=thingML_Session, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
maxInstances88: BinaryAssociation = BinaryAssociation(
    name="maxInstances88",
    ends={
        Property(name="thingML_Expression90", type=thingML_Session, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Session89", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
var123: BinaryAssociation = BinaryAssociation(
    name="var123",
    ends={
        Property(name="thingML_Variable124", type=thingML_Increment, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Increment", type=thingML_Variable, multiplicity=Multiplicity(0, 1))
    }
)
var125: BinaryAssociation = BinaryAssociation(
    name="var125",
    ends={
        Property(name="thingML_Variable126", type=thingML_Decrement, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Decrement", type=thingML_Variable, multiplicity=Multiplicity(0, 1))
    }
)
variable127: BinaryAssociation = BinaryAssociation(
    name="variable127",
    ends={
        Property(name="thingML_Parameter128", type=thingML_ForAction, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ForAction", type=thingML_Parameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
index129: BinaryAssociation = BinaryAssociation(
    name="index129",
    ends={
        Property(name="thingML_Parameter131", type=thingML_ForAction, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ForAction130", type=thingML_Parameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
array132: BinaryAssociation = BinaryAssociation(
    name="array132",
    ends={
        Property(name="thingML_PropertyReference", type=thingML_ForAction, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ForAction133", type=thingML_PropertyReference, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action134: BinaryAssociation = BinaryAssociation(
    name="action134",
    ends={
        Property(name="thingML_Action136", type=thingML_ForAction, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ForAction135", type=thingML_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init105: BinaryAssociation = BinaryAssociation(
    name="init105",
    ends={
        Property(name="thingML_Expression106", type=thingML_LocalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_LocalVariable", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
port107: BinaryAssociation = BinaryAssociation(
    name="port107",
    ends={
        Property(name="thingML_Port108", type=thingML_SendAction, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_SendAction", type=thingML_Port, multiplicity=Multiplicity(0, 1))
    }
)
message109: BinaryAssociation = BinaryAssociation(
    name="message109",
    ends={
        Property(name="thingML_Message111", type=thingML_SendAction, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_SendAction110", type=thingML_Message, multiplicity=Multiplicity(0, 1))
    }
)
parameters112: BinaryAssociation = BinaryAssociation(
    name="parameters112",
    ends={
        Property(name="thingML_Expression114", type=thingML_SendAction, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_SendAction113", type=thingML_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property115: BinaryAssociation = BinaryAssociation(
    name="property115",
    ends={
        Property(name="thingML_Variable116", type=thingML_VariableAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_VariableAssignment", type=thingML_Variable, multiplicity=Multiplicity(0, 1))
    }
)
index117: BinaryAssociation = BinaryAssociation(
    name="index117",
    ends={
        Property(name="thingML_Expression119", type=thingML_VariableAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_VariableAssignment118", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression120: BinaryAssociation = BinaryAssociation(
    name="expression120",
    ends={
        Property(name="thingML_Expression122", type=thingML_VariableAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_VariableAssignment121", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
msg152: BinaryAssociation = BinaryAssociation(
    name="msg152",
    ends={
        Property(name="thingML_Expression153", type=thingML_PrintAction, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_PrintAction", type=thingML_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
msg154: BinaryAssociation = BinaryAssociation(
    name="msg154",
    ends={
        Property(name="thingML_Expression155", type=thingML_ErrorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ErrorAction", type=thingML_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
session156: BinaryAssociation = BinaryAssociation(
    name="session156",
    ends={
        Property(name="thingML_Session157", type=thingML_StartSession, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_StartSession", type=thingML_Session, multiplicity=Multiplicity(0, 1))
    }
)
function158: BinaryAssociation = BinaryAssociation(
    name="function158",
    ends={
        Property(name="thingML_Function159", type=thingML_FunctionCallStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_FunctionCallStatement", type=thingML_Function, multiplicity=Multiplicity(0, 1))
    }
)
parameters160: BinaryAssociation = BinaryAssociation(
    name="parameters160",
    ends={
        Property(name="thingML_Expression162", type=thingML_FunctionCallStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_FunctionCallStatement161", type=thingML_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
segments163: BinaryAssociation = BinaryAssociation(
    name="segments163",
    ends={
        Property(name="thingML_Expression164", type=thingML_ExternExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ExternExpression", type=thingML_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition137: BinaryAssociation = BinaryAssociation(
    name="condition137",
    ends={
        Property(name="thingML_Expression138", type=thingML_LoopAction, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_LoopAction", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action139: BinaryAssociation = BinaryAssociation(
    name="action139",
    ends={
        Property(name="thingML_Action141", type=thingML_LoopAction, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_LoopAction140", type=thingML_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition142: BinaryAssociation = BinaryAssociation(
    name="condition142",
    ends={
        Property(name="thingML_Expression143", type=thingML_ConditionalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ConditionalAction", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action144: BinaryAssociation = BinaryAssociation(
    name="action144",
    ends={
        Property(name="thingML_Action146", type=thingML_ConditionalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ConditionalAction145", type=thingML_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseAction147: BinaryAssociation = BinaryAssociation(
    name="elseAction147",
    ends={
        Property(name="thingML_Action149", type=thingML_ConditionalAction, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ConditionalAction148", type=thingML_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp150: BinaryAssociation = BinaryAssociation(
    name="exp150",
    ends={
        Property(name="thingML_Expression151", type=thingML_ReturnAction, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ReturnAction", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
property172: BinaryAssociation = BinaryAssociation(
    name="property172",
    ends={
        Property(name="thingML_Variable174", type=thingML_PropertyReference, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_PropertyReference173", type=thingML_Variable, multiplicity=Multiplicity(0, 1))
    }
)
receiveMsg175: BinaryAssociation = BinaryAssociation(
    name="receiveMsg175",
    ends={
        Property(name="thingML_Event176", type=thingML_EventReference, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_EventReference", type=thingML_Event, multiplicity=Multiplicity(0, 1))
    }
)
parameter177: BinaryAssociation = BinaryAssociation(
    name="parameter177",
    ends={
        Property(name="thingML_Parameter179", type=thingML_EventReference, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_EventReference178", type=thingML_Parameter, multiplicity=Multiplicity(0, 1))
    }
)
function180: BinaryAssociation = BinaryAssociation(
    name="function180",
    ends={
        Property(name="thingML_Function181", type=thingML_FunctionCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_FunctionCallExpression", type=thingML_Function, multiplicity=Multiplicity(0, 1))
    }
)
parameters182: BinaryAssociation = BinaryAssociation(
    name="parameters182",
    ends={
        Property(name="thingML_Expression184", type=thingML_FunctionCallExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_FunctionCallExpression183", type=thingML_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values165: BinaryAssociation = BinaryAssociation(
    name="values165",
    ends={
        Property(name="thingML_Expression166", type=thingML_ArrayInit, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ArrayInit", type=thingML_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enum167: BinaryAssociation = BinaryAssociation(
    name="enum167",
    ends={
        Property(name="thingML_Enumeration168", type=thingML_EnumLiteralRef, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_EnumLiteralRef", type=thingML_Enumeration, multiplicity=Multiplicity(0, 1))
    }
)
literal169: BinaryAssociation = BinaryAssociation(
    name="literal169",
    ends={
        Property(name="thingML_EnumerationLiteral171", type=thingML_EnumLiteralRef, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_EnumLiteralRef170", type=thingML_EnumerationLiteral, multiplicity=Multiplicity(0, 1))
    }
)
connectors187: BinaryAssociation = BinaryAssociation(
    name="connectors187",
    ends={
        Property(name="thingML_AbstractConnector", type=thingML_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Configuration188", type=thingML_AbstractConnector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
propassigns189: BinaryAssociation = BinaryAssociation(
    name="propassigns189",
    ends={
        Property(name="thingML_ConfigPropertyAssign", type=thingML_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Configuration190", type=thingML_ConfigPropertyAssign, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type191: BinaryAssociation = BinaryAssociation(
    name="type191",
    ends={
        Property(name="thingML_Thing193", type=thingML_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Instance192", type=thingML_Thing, multiplicity=Multiplicity(0, 1))
    }
)
instance194: BinaryAssociation = BinaryAssociation(
    name="instance194",
    ends={
        Property(name="thingML_Instance196", type=thingML_ConfigPropertyAssign, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ConfigPropertyAssign195", type=thingML_Instance, multiplicity=Multiplicity(0, 1))
    }
)
property197: BinaryAssociation = BinaryAssociation(
    name="property197",
    ends={
        Property(name="thingML_Property199", type=thingML_ConfigPropertyAssign, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ConfigPropertyAssign198", type=thingML_Property, multiplicity=Multiplicity(0, 1))
    }
)
instances185: BinaryAssociation = BinaryAssociation(
    name="instances185",
    ends={
        Property(name="thingML_Instance", type=thingML_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Configuration186", type=thingML_Instance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
required211: BinaryAssociation = BinaryAssociation(
    name="required211",
    ends={
        Property(name="thingML_RequiredPort", type=thingML_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Connector212", type=thingML_RequiredPort, multiplicity=Multiplicity(0, 1))
    }
)
srv213: BinaryAssociation = BinaryAssociation(
    name="srv213",
    ends={
        Property(name="thingML_Instance215", type=thingML_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Connector214", type=thingML_Instance, multiplicity=Multiplicity(0, 1))
    }
)
provided216: BinaryAssociation = BinaryAssociation(
    name="provided216",
    ends={
        Property(name="thingML_ProvidedPort", type=thingML_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Connector217", type=thingML_ProvidedPort, multiplicity=Multiplicity(0, 1))
    }
)
inst218: BinaryAssociation = BinaryAssociation(
    name="inst218",
    ends={
        Property(name="thingML_Instance219", type=thingML_ExternalConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ExternalConnector", type=thingML_Instance, multiplicity=Multiplicity(0, 1))
    }
)
port220: BinaryAssociation = BinaryAssociation(
    name="port220",
    ends={
        Property(name="thingML_Port222", type=thingML_ExternalConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ExternalConnector221", type=thingML_Port, multiplicity=Multiplicity(0, 1))
    }
)
protocol223: BinaryAssociation = BinaryAssociation(
    name="protocol223",
    ends={
        Property(name="thingML_Protocol225", type=thingML_ExternalConnector, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ExternalConnector224", type=thingML_Protocol, multiplicity=Multiplicity(0, 1))
    }
)
index200: BinaryAssociation = BinaryAssociation(
    name="index200",
    ends={
        Property(name="thingML_Expression202", type=thingML_ConfigPropertyAssign, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ConfigPropertyAssign201", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs226: BinaryAssociation = BinaryAssociation(
    name="lhs226",
    ends={
        Property(name="thingML_Expression227", type=thingML_OrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_OrExpression", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init203: BinaryAssociation = BinaryAssociation(
    name="init203",
    ends={
        Property(name="thingML_Expression205", type=thingML_ConfigPropertyAssign, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ConfigPropertyAssign204", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
annotations206: BinaryAssociation = BinaryAssociation(
    name="annotations206",
    ends={
        Property(name="thingML_PlatformAnnotation208", type=thingML_ConfigPropertyAssign, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ConfigPropertyAssign207", type=thingML_PlatformAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cli209: BinaryAssociation = BinaryAssociation(
    name="cli209",
    ends={
        Property(name="thingML_Instance210", type=thingML_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_Connector", type=thingML_Instance, multiplicity=Multiplicity(0, 1))
    }
)
lhs236: BinaryAssociation = BinaryAssociation(
    name="lhs236",
    ends={
        Property(name="thingML_Expression237", type=thingML_EqualsExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_EqualsExpression", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs238: BinaryAssociation = BinaryAssociation(
    name="rhs238",
    ends={
        Property(name="thingML_Expression240", type=thingML_EqualsExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_EqualsExpression239", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs241: BinaryAssociation = BinaryAssociation(
    name="lhs241",
    ends={
        Property(name="thingML_Expression242", type=thingML_NotEqualsExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_NotEqualsExpression", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs243: BinaryAssociation = BinaryAssociation(
    name="rhs243",
    ends={
        Property(name="thingML_Expression245", type=thingML_NotEqualsExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_NotEqualsExpression244", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs246: BinaryAssociation = BinaryAssociation(
    name="lhs246",
    ends={
        Property(name="thingML_Expression247", type=thingML_GreaterExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_GreaterExpression", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs248: BinaryAssociation = BinaryAssociation(
    name="rhs248",
    ends={
        Property(name="thingML_Expression250", type=thingML_GreaterExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_GreaterExpression249", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs228: BinaryAssociation = BinaryAssociation(
    name="rhs228",
    ends={
        Property(name="thingML_Expression230", type=thingML_OrExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_OrExpression229", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs231: BinaryAssociation = BinaryAssociation(
    name="lhs231",
    ends={
        Property(name="thingML_Expression232", type=thingML_AndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_AndExpression", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs233: BinaryAssociation = BinaryAssociation(
    name="rhs233",
    ends={
        Property(name="thingML_Expression235", type=thingML_AndExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_AndExpression234", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs256: BinaryAssociation = BinaryAssociation(
    name="lhs256",
    ends={
        Property(name="thingML_Expression257", type=thingML_GreaterOrEqualExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_GreaterOrEqualExpression", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs258: BinaryAssociation = BinaryAssociation(
    name="rhs258",
    ends={
        Property(name="thingML_Expression260", type=thingML_GreaterOrEqualExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_GreaterOrEqualExpression259", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs261: BinaryAssociation = BinaryAssociation(
    name="lhs261",
    ends={
        Property(name="thingML_Expression262", type=thingML_LowerOrEqualExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_LowerOrEqualExpression", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs263: BinaryAssociation = BinaryAssociation(
    name="rhs263",
    ends={
        Property(name="thingML_Expression265", type=thingML_LowerOrEqualExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_LowerOrEqualExpression264", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs251: BinaryAssociation = BinaryAssociation(
    name="lhs251",
    ends={
        Property(name="thingML_Expression252", type=thingML_LowerExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_LowerExpression", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs253: BinaryAssociation = BinaryAssociation(
    name="rhs253",
    ends={
        Property(name="thingML_Expression255", type=thingML_LowerExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_LowerExpression254", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs273: BinaryAssociation = BinaryAssociation(
    name="rhs273",
    ends={
        Property(name="thingML_Expression275", type=thingML_MinusExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_MinusExpression274", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs276: BinaryAssociation = BinaryAssociation(
    name="lhs276",
    ends={
        Property(name="thingML_Expression277", type=thingML_TimesExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_TimesExpression", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs278: BinaryAssociation = BinaryAssociation(
    name="rhs278",
    ends={
        Property(name="thingML_Expression280", type=thingML_TimesExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_TimesExpression279", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs266: BinaryAssociation = BinaryAssociation(
    name="lhs266",
    ends={
        Property(name="thingML_Expression267", type=thingML_PlusExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_PlusExpression", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs268: BinaryAssociation = BinaryAssociation(
    name="rhs268",
    ends={
        Property(name="thingML_Expression270", type=thingML_PlusExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_PlusExpression269", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs271: BinaryAssociation = BinaryAssociation(
    name="lhs271",
    ends={
        Property(name="thingML_Expression272", type=thingML_MinusExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_MinusExpression", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs288: BinaryAssociation = BinaryAssociation(
    name="rhs288",
    ends={
        Property(name="thingML_Expression290", type=thingML_ModExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ModExpression289", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
term291: BinaryAssociation = BinaryAssociation(
    name="term291",
    ends={
        Property(name="thingML_Expression292", type=thingML_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_CastExpression", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type293: BinaryAssociation = BinaryAssociation(
    name="type293",
    ends={
        Property(name="thingML_Type295", type=thingML_CastExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_CastExpression294", type=thingML_Type, multiplicity=Multiplicity(0, 1))
    }
)
term296: BinaryAssociation = BinaryAssociation(
    name="term296",
    ends={
        Property(name="thingML_Expression297", type=thingML_ExpressionGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ExpressionGroup", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs281: BinaryAssociation = BinaryAssociation(
    name="lhs281",
    ends={
        Property(name="thingML_Expression282", type=thingML_DivExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_DivExpression", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rhs283: BinaryAssociation = BinaryAssociation(
    name="rhs283",
    ends={
        Property(name="thingML_Expression285", type=thingML_DivExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_DivExpression284", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lhs286: BinaryAssociation = BinaryAssociation(
    name="lhs286",
    ends={
        Property(name="thingML_Expression287", type=thingML_ModExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ModExpression", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
array302: BinaryAssociation = BinaryAssociation(
    name="array302",
    ends={
        Property(name="thingML_Expression303", type=thingML_ArrayIndex, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ArrayIndex", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
index304: BinaryAssociation = BinaryAssociation(
    name="index304",
    ends={
        Property(name="thingML_Expression306", type=thingML_ArrayIndex, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_ArrayIndex305", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
term298: BinaryAssociation = BinaryAssociation(
    name="term298",
    ends={
        Property(name="thingML_Expression299", type=thingML_NotExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_NotExpression", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
term300: BinaryAssociation = BinaryAssociation(
    name="term300",
    ends={
        Property(name="thingML_Expression301", type=thingML_UnaryMinus, multiplicity=Multiplicity(1, 1)),
        Property(name="thingML_UnaryMinus", type=thingML_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_thingML_Type_NamedElement = Generalization(general=NamedElement, specific=thingML_Type)
gen_thingML_Type_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingML_Type)
gen_thingML_PrimitiveType_Type = Generalization(general=Type, specific=thingML_PrimitiveType)
gen_thingML_ObjectType_Type = Generalization(general=Type, specific=thingML_ObjectType)
gen_thingML_Enumeration_Type = Generalization(general=Type, specific=thingML_Enumeration)
gen_thingML_EnumerationLiteral_NamedElement = Generalization(general=NamedElement, specific=thingML_EnumerationLiteral)
gen_thingML_EnumerationLiteral_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingML_EnumerationLiteral)
gen_thingML_Thing_Type = Generalization(general=Type, specific=thingML_Thing)
gen_thingML_Variable_NamedElement = Generalization(general=NamedElement, specific=thingML_Variable)
gen_thingML_Variable_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingML_Variable)
gen_thingML_PropertyAssign_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingML_PropertyAssign)
gen_thingML_Protocol_NamedElement = Generalization(general=NamedElement, specific=thingML_Protocol)
gen_thingML_Protocol_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingML_Protocol)
gen_thingML_Function_NamedElement = Generalization(general=NamedElement, specific=thingML_Function)
gen_thingML_Function_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingML_Function)
gen_thingML_InternalPort_Port = Generalization(general=Port, specific=thingML_InternalPort)
gen_thingML_State_NamedElement = Generalization(general=NamedElement, specific=thingML_State)
gen_thingML_State_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingML_State)
gen_thingML_Handler_NamedElement = Generalization(general=NamedElement, specific=thingML_Handler)
gen_thingML_Handler_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingML_Handler)
gen_thingML_Property_Variable = Generalization(general=Variable, specific=thingML_Property)
gen_thingML_Message_NamedElement = Generalization(general=NamedElement, specific=thingML_Message)
gen_thingML_Message_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingML_Message)
gen_thingML_Parameter_Variable = Generalization(general=Variable, specific=thingML_Parameter)
gen_thingML_Port_NamedElement = Generalization(general=NamedElement, specific=thingML_Port)
gen_thingML_Port_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingML_Port)
gen_thingML_RequiredPort_Port = Generalization(general=Port, specific=thingML_RequiredPort)
gen_thingML_ProvidedPort_Port = Generalization(general=Port, specific=thingML_ProvidedPort)
gen_thingML_Event_NamedElement = Generalization(general=NamedElement, specific=thingML_Event)
gen_thingML_ReceiveMessage_Event = Generalization(general=Event, specific=thingML_ReceiveMessage)
gen_thingML_ActionBlock_Action = Generalization(general=Action, specific=thingML_ActionBlock)
gen_thingML_ExternStatement_Action = Generalization(general=Action, specific=thingML_ExternStatement)
gen_thingML_LocalVariable_Variable = Generalization(general=Variable, specific=thingML_LocalVariable)
gen_thingML_LocalVariable_Action = Generalization(general=Action, specific=thingML_LocalVariable)
gen_thingML_Transition_Handler = Generalization(general=Handler, specific=thingML_Transition)
gen_thingML_InternalTransition_Handler = Generalization(general=Handler, specific=thingML_InternalTransition)
gen_thingML_CompositeState_State = Generalization(general=State, specific=thingML_CompositeState)
gen_thingML_CompositeState_StateContainer = Generalization(general=StateContainer, specific=thingML_CompositeState)
gen_thingML_Session_StateContainer = Generalization(general=StateContainer, specific=thingML_Session)
gen_thingML_Region_StateContainer = Generalization(general=StateContainer, specific=thingML_Region)
gen_thingML_FinalState_State = Generalization(general=State, specific=thingML_FinalState)
gen_thingML_StateContainer_NamedElement = Generalization(general=NamedElement, specific=thingML_StateContainer)
gen_thingML_StateContainer_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingML_StateContainer)
gen_thingML_Increment_Action = Generalization(general=Action, specific=thingML_Increment)
gen_thingML_Decrement_Action = Generalization(general=Action, specific=thingML_Decrement)
gen_thingML_ForAction_Action = Generalization(general=Action, specific=thingML_ForAction)
gen_thingML_LoopAction_Action = Generalization(general=Action, specific=thingML_LoopAction)
gen_thingML_SendAction_Action = Generalization(general=Action, specific=thingML_SendAction)
gen_thingML_VariableAssignment_Action = Generalization(general=Action, specific=thingML_VariableAssignment)
gen_thingML_ErrorAction_Action = Generalization(general=Action, specific=thingML_ErrorAction)
gen_thingML_StartSession_Action = Generalization(general=Action, specific=thingML_StartSession)
gen_thingML_FunctionCallStatement_Action = Generalization(general=Action, specific=thingML_FunctionCallStatement)
gen_thingML_ExternExpression_Expression = Generalization(general=Expression, specific=thingML_ExternExpression)
gen_thingML_ConditionalAction_Action = Generalization(general=Action, specific=thingML_ConditionalAction)
gen_thingML_ReturnAction_Action = Generalization(general=Action, specific=thingML_ReturnAction)
gen_thingML_PrintAction_Action = Generalization(general=Action, specific=thingML_PrintAction)
gen_thingML_BooleanLiteral_Literal = Generalization(general=Literal, specific=thingML_BooleanLiteral)
gen_thingML_StringLiteral_Literal = Generalization(general=Literal, specific=thingML_StringLiteral)
gen_thingML_DoubleLiteral_Literal = Generalization(general=Literal, specific=thingML_DoubleLiteral)
gen_thingML_PropertyReference_Expression = Generalization(general=Expression, specific=thingML_PropertyReference)
gen_thingML_EventReference_Expression = Generalization(general=Expression, specific=thingML_EventReference)
gen_thingML_FunctionCallExpression_Expression = Generalization(general=Expression, specific=thingML_FunctionCallExpression)
gen_thingML_Configuration_NamedElement = Generalization(general=NamedElement, specific=thingML_Configuration)
gen_thingML_Literal_Expression = Generalization(general=Expression, specific=thingML_Literal)
gen_thingML_ArrayInit_Expression = Generalization(general=Expression, specific=thingML_ArrayInit)
gen_thingML_EnumLiteralRef_Literal = Generalization(general=Literal, specific=thingML_EnumLiteralRef)
gen_thingML_ByteLiteral_Literal = Generalization(general=Literal, specific=thingML_ByteLiteral)
gen_thingML_CharLiteral_Literal = Generalization(general=Literal, specific=thingML_CharLiteral)
gen_thingML_IntegerLiteral_Literal = Generalization(general=Literal, specific=thingML_IntegerLiteral)
gen_thingML_Instance_NamedElement = Generalization(general=NamedElement, specific=thingML_Instance)
gen_thingML_Instance_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingML_Instance)
gen_thingML_Configuration_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingML_Configuration)
gen_thingML_ExternalConnector_AbstractConnector = Generalization(general=AbstractConnector, specific=thingML_ExternalConnector)
gen_thingML_OrExpression_Expression = Generalization(general=Expression, specific=thingML_OrExpression)
gen_thingML_AbstractConnector_NamedElement = Generalization(general=NamedElement, specific=thingML_AbstractConnector)
gen_thingML_AbstractConnector_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingML_AbstractConnector)
gen_thingML_Connector_AbstractConnector = Generalization(general=AbstractConnector, specific=thingML_Connector)
gen_thingML_NotEqualsExpression_Expression = Generalization(general=Expression, specific=thingML_NotEqualsExpression)
gen_thingML_GreaterExpression_Expression = Generalization(general=Expression, specific=thingML_GreaterExpression)
gen_thingML_AndExpression_Expression = Generalization(general=Expression, specific=thingML_AndExpression)
gen_thingML_EqualsExpression_Expression = Generalization(general=Expression, specific=thingML_EqualsExpression)
gen_thingML_GreaterOrEqualExpression_Expression = Generalization(general=Expression, specific=thingML_GreaterOrEqualExpression)
gen_thingML_LowerOrEqualExpression_Expression = Generalization(general=Expression, specific=thingML_LowerOrEqualExpression)
gen_thingML_LowerExpression_Expression = Generalization(general=Expression, specific=thingML_LowerExpression)
gen_thingML_TimesExpression_Expression = Generalization(general=Expression, specific=thingML_TimesExpression)
gen_thingML_DivExpression_Expression = Generalization(general=Expression, specific=thingML_DivExpression)
gen_thingML_PlusExpression_Expression = Generalization(general=Expression, specific=thingML_PlusExpression)
gen_thingML_MinusExpression_Expression = Generalization(general=Expression, specific=thingML_MinusExpression)
gen_thingML_CastExpression_Expression = Generalization(general=Expression, specific=thingML_CastExpression)
gen_thingML_ExpressionGroup_Expression = Generalization(general=Expression, specific=thingML_ExpressionGroup)
gen_thingML_ModExpression_Expression = Generalization(general=Expression, specific=thingML_ModExpression)
gen_thingML_ArrayIndex_Expression = Generalization(general=Expression, specific=thingML_ArrayIndex)
gen_thingML_NotExpression_Expression = Generalization(general=Expression, specific=thingML_NotExpression)
gen_thingML_UnaryMinus_Expression = Generalization(general=Expression, specific=thingML_UnaryMinus)

# Domain Model
domain_model = DomainModel(
    name="thingML",
    types={thingML_ThingMLModel, thingML_Import, thingML_Type, thingML_Protocol, thingML_Expression, thingML_PrimitiveType, Type, thingML_ObjectType, thingML_Enumeration, thingML_EnumerationLiteral, thingML_Literal, thingML_Thing, thingML_Message, thingML_Configuration, thingML_PlatformAnnotation, thingML_NamedElement, thingML_AnnotatedElement, thingML_Variable, NamedElement, AnnotatedElement, thingML_TypeRef, thingML_CompositeState, thingML_Parameter, thingML_Action, thingML_Port, thingML_Property, thingML_Function, thingML_PropertyAssign, thingML_InternalPort, thingML_State, thingML_InternalTransition, thingML_Transition, thingML_Handler, thingML_Event, Variable, thingML_RequiredPort, Port, thingML_ProvidedPort, thingML_ReceiveMessage, Event, thingML_ActionBlock, Action, thingML_ExternStatement, thingML_LocalVariable, Handler, State, StateContainer, thingML_Region, thingML_Session, thingML_FinalState, thingML_StateContainer, thingML_Increment, thingML_Decrement, thingML_ForAction, thingML_PropertyReference, thingML_LoopAction, thingML_SendAction, thingML_VariableAssignment, thingML_ErrorAction, thingML_StartSession, thingML_FunctionCallStatement, thingML_ExternExpression, Expression, thingML_ConditionalAction, thingML_ReturnAction, thingML_PrintAction, thingML_BooleanLiteral, thingML_StringLiteral, thingML_DoubleLiteral, thingML_EventReference, thingML_FunctionCallExpression, thingML_ArrayInit, thingML_EnumLiteralRef, Literal, thingML_ByteLiteral, thingML_CharLiteral, thingML_IntegerLiteral, thingML_AbstractConnector, thingML_ConfigPropertyAssign, thingML_Instance, thingML_ExternalConnector, thingML_OrExpression, thingML_Connector, AbstractConnector, thingML_NotEqualsExpression, thingML_GreaterExpression, thingML_AndExpression, thingML_EqualsExpression, thingML_GreaterOrEqualExpression, thingML_LowerOrEqualExpression, thingML_LowerExpression, thingML_TimesExpression, thingML_DivExpression, thingML_PlusExpression, thingML_MinusExpression, thingML_CastExpression, thingML_ExpressionGroup, thingML_ModExpression, thingML_ArrayIndex, thingML_NotExpression, thingML_UnaryMinus},
    associations={imports0, types1, protocols3, cardinality12, typeRef14, literals16, init18, includes21, configs5, annotations7, typeRef8, type9, assign30, behaviour32, property34, index37, init40, parameters43, typeRef45, body48, messages22, ports24, properties26, functions28, properties62, entry64, exit67, internal70, outgoing72, event74, guard75, action78, init50, parameters53, sends56, receives59, initial91, substate93, port96, message98, actions101, segments103, target81, region84, session86, maxInstances88, var123, var125, variable127, index129, array132, action134, init105, port107, message109, parameters112, property115, index117, expression120, msg152, msg154, session156, function158, parameters160, segments163, condition137, action139, condition142, action144, elseAction147, exp150, property172, receiveMsg175, parameter177, function180, parameters182, values165, enum167, literal169, connectors187, propassigns189, type191, instance194, property197, instances185, required211, srv213, provided216, inst218, port220, protocol223, index200, lhs226, init203, annotations206, cli209, lhs236, rhs238, lhs241, rhs243, lhs246, rhs248, rhs228, lhs231, rhs233, lhs256, rhs258, lhs261, rhs263, lhs251, rhs253, rhs273, lhs276, rhs278, lhs266, rhs268, lhs271, rhs288, term291, type293, term296, lhs281, rhs283, lhs286, array302, index304, term298, term300},
    generalizations={gen_thingML_Type_NamedElement, gen_thingML_Type_AnnotatedElement, gen_thingML_PrimitiveType_Type, gen_thingML_ObjectType_Type, gen_thingML_Enumeration_Type, gen_thingML_EnumerationLiteral_NamedElement, gen_thingML_EnumerationLiteral_AnnotatedElement, gen_thingML_Thing_Type, gen_thingML_Variable_NamedElement, gen_thingML_Variable_AnnotatedElement, gen_thingML_PropertyAssign_AnnotatedElement, gen_thingML_Protocol_NamedElement, gen_thingML_Protocol_AnnotatedElement, gen_thingML_Function_NamedElement, gen_thingML_Function_AnnotatedElement, gen_thingML_InternalPort_Port, gen_thingML_State_NamedElement, gen_thingML_State_AnnotatedElement, gen_thingML_Handler_NamedElement, gen_thingML_Handler_AnnotatedElement, gen_thingML_Property_Variable, gen_thingML_Message_NamedElement, gen_thingML_Message_AnnotatedElement, gen_thingML_Parameter_Variable, gen_thingML_Port_NamedElement, gen_thingML_Port_AnnotatedElement, gen_thingML_RequiredPort_Port, gen_thingML_ProvidedPort_Port, gen_thingML_Event_NamedElement, gen_thingML_ReceiveMessage_Event, gen_thingML_ActionBlock_Action, gen_thingML_ExternStatement_Action, gen_thingML_LocalVariable_Variable, gen_thingML_LocalVariable_Action, gen_thingML_Transition_Handler, gen_thingML_InternalTransition_Handler, gen_thingML_CompositeState_State, gen_thingML_CompositeState_StateContainer, gen_thingML_Session_StateContainer, gen_thingML_Region_StateContainer, gen_thingML_FinalState_State, gen_thingML_StateContainer_NamedElement, gen_thingML_StateContainer_AnnotatedElement, gen_thingML_Increment_Action, gen_thingML_Decrement_Action, gen_thingML_ForAction_Action, gen_thingML_LoopAction_Action, gen_thingML_SendAction_Action, gen_thingML_VariableAssignment_Action, gen_thingML_ErrorAction_Action, gen_thingML_StartSession_Action, gen_thingML_FunctionCallStatement_Action, gen_thingML_ExternExpression_Expression, gen_thingML_ConditionalAction_Action, gen_thingML_ReturnAction_Action, gen_thingML_PrintAction_Action, gen_thingML_BooleanLiteral_Literal, gen_thingML_StringLiteral_Literal, gen_thingML_DoubleLiteral_Literal, gen_thingML_PropertyReference_Expression, gen_thingML_EventReference_Expression, gen_thingML_FunctionCallExpression_Expression, gen_thingML_Configuration_NamedElement, gen_thingML_Literal_Expression, gen_thingML_ArrayInit_Expression, gen_thingML_EnumLiteralRef_Literal, gen_thingML_ByteLiteral_Literal, gen_thingML_CharLiteral_Literal, gen_thingML_IntegerLiteral_Literal, gen_thingML_Instance_NamedElement, gen_thingML_Instance_AnnotatedElement, gen_thingML_Configuration_AnnotatedElement, gen_thingML_ExternalConnector_AbstractConnector, gen_thingML_OrExpression_Expression, gen_thingML_AbstractConnector_NamedElement, gen_thingML_AbstractConnector_AnnotatedElement, gen_thingML_Connector_AbstractConnector, gen_thingML_NotEqualsExpression_Expression, gen_thingML_GreaterExpression_Expression, gen_thingML_AndExpression_Expression, gen_thingML_EqualsExpression_Expression, gen_thingML_GreaterOrEqualExpression_Expression, gen_thingML_LowerOrEqualExpression_Expression, gen_thingML_LowerExpression_Expression, gen_thingML_TimesExpression_Expression, gen_thingML_DivExpression_Expression, gen_thingML_PlusExpression_Expression, gen_thingML_MinusExpression_Expression, gen_thingML_CastExpression_Expression, gen_thingML_ExpressionGroup_Expression, gen_thingML_ModExpression_Expression, gen_thingML_ArrayIndex_Expression, gen_thingML_NotExpression_Expression, gen_thingML_UnaryMinus_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)