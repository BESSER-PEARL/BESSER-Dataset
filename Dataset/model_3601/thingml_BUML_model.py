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
thingml_Function = Class(name="thingml::Function")
AnnotatedElement = Class(name="AnnotatedElement")
TypedElement = Class(name="TypedElement")
thingml_Parameter = Class(name="thingml::Parameter")
thingml_ThingMLModel = Class(name="thingml::ThingMLModel")
thingml_Type = Class(name="thingml::Type", is_abstract=True)
thingml_Configuration = Class(name="thingml::Configuration")
thingml_ThingMLElement = Class(name="thingml::ThingMLElement", is_abstract=True)
thingml_TypedElement = Class(name="thingml::TypedElement", is_abstract=True)
thingml_Expression = Class(name="thingml::Expression", is_abstract=True)
thingml_Action = Class(name="thingml::Action", is_abstract=True)
thingml_Message = Class(name="thingml::Message")
thingml_Thing = Class(name="thingml::Thing")
Type = Class(name="Type")
thingml_Property = Class(name="thingml::Property")
thingml_Port = Class(name="thingml::Port", is_abstract=True)
thingml_StateMachine = Class(name="thingml::StateMachine")
thingml_PropertyAssign = Class(name="thingml::PropertyAssign")
Variable = Class(name="Variable")
thingml_Variable = Class(name="thingml::Variable", is_abstract=True)
thingml_Transition = Class(name="thingml::Transition")
Handler = Class(name="Handler")
thingml_State = Class(name="thingml::State")
thingml_PlatformAnnotation = Class(name="thingml::PlatformAnnotation")
ThingMLElement = Class(name="ThingMLElement")
thingml_Enumeration = Class(name="thingml::Enumeration")
thingml_EnumerationLiteral = Class(name="thingml::EnumerationLiteral")
thingml_PrimitiveType = Class(name="thingml::PrimitiveType")
thingml_AnnotatedElement = Class(name="thingml::AnnotatedElement", is_abstract=True)
CompositeState = Class(name="CompositeState")
thingml_Handler = Class(name="thingml::Handler", is_abstract=True)
thingml_Event = Class(name="thingml::Event", is_abstract=True)
thingml_ActionBlock = Class(name="thingml::ActionBlock")
Action = Class(name="Action")
thingml_ExternStatement = Class(name="thingml::ExternStatement")
thingml_ExternExpression = Class(name="thingml::ExternExpression")
Expression = Class(name="Expression")
thingml_InternalTransition = Class(name="thingml::InternalTransition")
thingml_CompositeState = Class(name="thingml::CompositeState")
State = Class(name="State")
Region = Class(name="Region")
thingml_ParallelRegion = Class(name="thingml::ParallelRegion")
thingml_Region = Class(name="thingml::Region", is_abstract=True)
thingml_RequiredPort = Class(name="thingml::RequiredPort")
Port = Class(name="Port")
thingml_ProvidedPort = Class(name="thingml::ProvidedPort")
thingml_EventReference = Class(name="thingml::EventReference")
thingml_SendAction = Class(name="thingml::SendAction")
thingml_VariableAssignment = Class(name="thingml::VariableAssignment")
thingml_ReceiveMessage = Class(name="thingml::ReceiveMessage")
Event = Class(name="Event")
thingml_Dictionary = Class(name="thingml::Dictionary")
Property_ = Class(name="Property")
thingml_PlusExpression = Class(name="thingml::PlusExpression")
BinaryExpression = Class(name="BinaryExpression")
thingml_MinusExpression = Class(name="thingml::MinusExpression")
thingml_TimesExpression = Class(name="thingml::TimesExpression")
thingml_DivExpression = Class(name="thingml::DivExpression")
thingml_ModExpression = Class(name="thingml::ModExpression")
thingml_EqualsExpression = Class(name="thingml::EqualsExpression")
thingml_GreaterExpression = Class(name="thingml::GreaterExpression")
thingml_LowerExpression = Class(name="thingml::LowerExpression")
thingml_AndExpression = Class(name="thingml::AndExpression")
thingml_OrExpression = Class(name="thingml::OrExpression")
thingml_Literal = Class(name="thingml::Literal", is_abstract=True)
thingml_EnumLiteralRef = Class(name="thingml::EnumLiteralRef")
Literal = Class(name="Literal")
thingml_IntegerLiteral = Class(name="thingml::IntegerLiteral")
thingml_BooleanLiteral = Class(name="thingml::BooleanLiteral")
thingml_StringLiteral = Class(name="thingml::StringLiteral")
thingml_DoubleLiteral = Class(name="thingml::DoubleLiteral")
thingml_UnaryExpression = Class(name="thingml::UnaryExpression", is_abstract=True)
thingml_NotExpression = Class(name="thingml::NotExpression")
UnaryExpression = Class(name="UnaryExpression")
thingml_UnaryMinus = Class(name="thingml::UnaryMinus")
thingml_BinaryExpression = Class(name="thingml::BinaryExpression", is_abstract=True)
thingml_PrintAction = Class(name="thingml::PrintAction")
thingml_ErrorAction = Class(name="thingml::ErrorAction")
thingml_Instance = Class(name="thingml::Instance")
thingml_Connector = Class(name="thingml::Connector")
thingml_ControlStructure = Class(name="thingml::ControlStructure", is_abstract=True)
thingml_LoopAction = Class(name="thingml::LoopAction")
ControlStructure = Class(name="ControlStructure")
thingml_ConditionalAction = Class(name="thingml::ConditionalAction")
thingml_PropertyReference = Class(name="thingml::PropertyReference")
thingml_ArrayIndex = Class(name="thingml::ArrayIndex")
thingml_DictionaryReference = Class(name="thingml::DictionaryReference")
PropertyReference = Class(name="PropertyReference")
thingml_ExpressionGroup = Class(name="thingml::ExpressionGroup")
thingml_ReturnAction = Class(name="thingml::ReturnAction")
thingml_FunctionCall = Class(name="thingml::FunctionCall", is_abstract=True)
thingml_ConfigInclude = Class(name="thingml::ConfigInclude")
thingml_ConfigPropertyAssign = Class(name="thingml::ConfigPropertyAssign")
thingml_InstanceRef = Class(name="thingml::InstanceRef")
thingml_FunctionCallStatement = Class(name="thingml::FunctionCallStatement")
FunctionCall = Class(name="FunctionCall")
thingml_FunctionCallExpression = Class(name="thingml::FunctionCallExpression")
thingml_LocalVariable = Class(name="thingml::LocalVariable")

# thingml_Function class attributes and methods

# AnnotatedElement class attributes and methods

# TypedElement class attributes and methods

# thingml_Parameter class attributes and methods

# thingml_ThingMLModel class attributes and methods

# thingml_Type class attributes and methods

# thingml_Configuration class attributes and methods
thingml_Configuration_fragment: Property = Property(name="fragment", type=BooleanType)
thingml_Configuration.attributes={thingml_Configuration_fragment}

# thingml_ThingMLElement class attributes and methods
thingml_ThingMLElement_name: Property = Property(name="name", type=StringType)
thingml_ThingMLElement.attributes={thingml_ThingMLElement_name}

# thingml_TypedElement class attributes and methods

# thingml_Expression class attributes and methods

# thingml_Action class attributes and methods

# thingml_Message class attributes and methods

# thingml_Thing class attributes and methods
thingml_Thing_fragment: Property = Property(name="fragment", type=BooleanType)
thingml_Thing.attributes={thingml_Thing_fragment}

# Type class attributes and methods

# thingml_Property class attributes and methods
thingml_Property_changeable: Property = Property(name="changeable", type=BooleanType)
thingml_Property.attributes={thingml_Property_changeable}

# thingml_Port class attributes and methods

# thingml_StateMachine class attributes and methods

# thingml_PropertyAssign class attributes and methods

# Variable class attributes and methods

# thingml_Variable class attributes and methods

# thingml_Transition class attributes and methods

# Handler class attributes and methods

# thingml_State class attributes and methods

# thingml_PlatformAnnotation class attributes and methods
thingml_PlatformAnnotation_value: Property = Property(name="value", type=StringType)
thingml_PlatformAnnotation.attributes={thingml_PlatformAnnotation_value}

# ThingMLElement class attributes and methods

# thingml_Enumeration class attributes and methods

# thingml_EnumerationLiteral class attributes and methods

# thingml_PrimitiveType class attributes and methods

# thingml_AnnotatedElement class attributes and methods

# CompositeState class attributes and methods

# thingml_Handler class attributes and methods

# thingml_Event class attributes and methods

# thingml_ActionBlock class attributes and methods

# Action class attributes and methods

# thingml_ExternStatement class attributes and methods
thingml_ExternStatement_statement: Property = Property(name="statement", type=StringType)
thingml_ExternStatement.attributes={thingml_ExternStatement_statement}

# thingml_ExternExpression class attributes and methods
thingml_ExternExpression_expression: Property = Property(name="expression", type=StringType)
thingml_ExternExpression.attributes={thingml_ExternExpression_expression}

# Expression class attributes and methods

# thingml_InternalTransition class attributes and methods

# thingml_CompositeState class attributes and methods

# State class attributes and methods

# Region class attributes and methods

# thingml_ParallelRegion class attributes and methods

# thingml_Region class attributes and methods
thingml_Region_history: Property = Property(name="history", type=BooleanType)
thingml_Region.attributes={thingml_Region_history}

# thingml_RequiredPort class attributes and methods
thingml_RequiredPort_optional: Property = Property(name="optional", type=BooleanType)
thingml_RequiredPort.attributes={thingml_RequiredPort_optional}

# Port class attributes and methods

# thingml_ProvidedPort class attributes and methods

# thingml_EventReference class attributes and methods

# thingml_SendAction class attributes and methods

# thingml_VariableAssignment class attributes and methods

# thingml_ReceiveMessage class attributes and methods

# Event class attributes and methods

# thingml_Dictionary class attributes and methods

# Property class attributes and methods

# thingml_PlusExpression class attributes and methods

# BinaryExpression class attributes and methods

# thingml_MinusExpression class attributes and methods

# thingml_TimesExpression class attributes and methods

# thingml_DivExpression class attributes and methods

# thingml_ModExpression class attributes and methods

# thingml_EqualsExpression class attributes and methods

# thingml_GreaterExpression class attributes and methods

# thingml_LowerExpression class attributes and methods

# thingml_AndExpression class attributes and methods

# thingml_OrExpression class attributes and methods

# thingml_Literal class attributes and methods

# thingml_EnumLiteralRef class attributes and methods

# Literal class attributes and methods

# thingml_IntegerLiteral class attributes and methods
thingml_IntegerLiteral_intValue: Property = Property(name="intValue", type=IntegerType)
thingml_IntegerLiteral.attributes={thingml_IntegerLiteral_intValue}

# thingml_BooleanLiteral class attributes and methods
thingml_BooleanLiteral_boolValue: Property = Property(name="boolValue", type=BooleanType)
thingml_BooleanLiteral.attributes={thingml_BooleanLiteral_boolValue}

# thingml_StringLiteral class attributes and methods
thingml_StringLiteral_stringValue: Property = Property(name="stringValue", type=StringType)
thingml_StringLiteral.attributes={thingml_StringLiteral_stringValue}

# thingml_DoubleLiteral class attributes and methods
thingml_DoubleLiteral_doubleValue: Property = Property(name="doubleValue", type=FloatType)
thingml_DoubleLiteral.attributes={thingml_DoubleLiteral_doubleValue}

# thingml_UnaryExpression class attributes and methods

# thingml_NotExpression class attributes and methods

# UnaryExpression class attributes and methods

# thingml_UnaryMinus class attributes and methods

# thingml_BinaryExpression class attributes and methods

# thingml_PrintAction class attributes and methods

# thingml_ErrorAction class attributes and methods

# thingml_Instance class attributes and methods

# thingml_Connector class attributes and methods

# thingml_ControlStructure class attributes and methods

# thingml_LoopAction class attributes and methods

# ControlStructure class attributes and methods

# thingml_ConditionalAction class attributes and methods

# thingml_PropertyReference class attributes and methods

# thingml_ArrayIndex class attributes and methods

# thingml_DictionaryReference class attributes and methods

# PropertyReference class attributes and methods

# thingml_ExpressionGroup class attributes and methods

# thingml_ReturnAction class attributes and methods

# thingml_FunctionCall class attributes and methods

# thingml_ConfigInclude class attributes and methods

# thingml_ConfigPropertyAssign class attributes and methods

# thingml_InstanceRef class attributes and methods

# thingml_FunctionCallStatement class attributes and methods

# FunctionCall class attributes and methods

# thingml_FunctionCallExpression class attributes and methods

# thingml_LocalVariable class attributes and methods
thingml_LocalVariable_changeable: Property = Property(name="changeable", type=BooleanType)
thingml_LocalVariable.attributes={thingml_LocalVariable_changeable}

# Relationships
configs4: BinaryAssociation = BinaryAssociation(
    name="configs4",
    ends={
        Property(name="thingml_Configuration", type=thingml_ThingMLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_ThingMLModel5", type=thingml_Configuration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types0: BinaryAssociation = BinaryAssociation(
    name="types0",
    ends={
        Property(name="thingml_Type", type=thingml_ThingMLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_ThingMLModel", type=thingml_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imports2: BinaryAssociation = BinaryAssociation(
    name="imports2",
    ends={
        Property(name="thingml_ThingMLModel3", type=thingml_ThingMLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_ThingMLModel1", type=thingml_ThingMLModel, multiplicity=Multiplicity(0, 9999))
    }
)
type26: BinaryAssociation = BinaryAssociation(
    name="type26",
    ends={
        Property(name="thingml_Type27", type=thingml_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_TypedElement", type=thingml_Type, multiplicity=Multiplicity(1, 1))
    }
)
cardinality28: BinaryAssociation = BinaryAssociation(
    name="cardinality28",
    ends={
        Property(name="thingml_Expression", type=thingml_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_TypedElement29", type=thingml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters6: BinaryAssociation = BinaryAssociation(
    name="parameters6",
    ends={
        Property(name="thingml_Parameter", type=thingml_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_Function", type=thingml_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body7: BinaryAssociation = BinaryAssociation(
    name="body7",
    ends={
        Property(name="thingml_Action", type=thingml_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_Function8", type=thingml_Action, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters9: BinaryAssociation = BinaryAssociation(
    name="parameters9",
    ends={
        Property(name="thingml_Parameter10", type=thingml_Message, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_Message", type=thingml_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
properties11: BinaryAssociation = BinaryAssociation(
    name="properties11",
    ends={
        Property(name="thingml_Property", type=thingml_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_Thing", type=thingml_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ports12: BinaryAssociation = BinaryAssociation(
    name="ports12",
    ends={
        Property(name="Port", type=thingml_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=thingml_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
behaviour13: BinaryAssociation = BinaryAssociation(
    name="behaviour13",
    ends={
        Property(name="thingml_StateMachine", type=thingml_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_Thing14", type=thingml_StateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
includes16: BinaryAssociation = BinaryAssociation(
    name="includes16",
    ends={
        Property(name="thingml_Thing17", type=thingml_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_Thing15", type=thingml_Thing, multiplicity=Multiplicity(0, 9999))
    }
)
assign18: BinaryAssociation = BinaryAssociation(
    name="assign18",
    ends={
        Property(name="thingml_PropertyAssign", type=thingml_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_Thing19", type=thingml_PropertyAssign, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
messages20: BinaryAssociation = BinaryAssociation(
    name="messages20",
    ends={
        Property(name="thingml_Message22", type=thingml_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_Thing21", type=thingml_Message, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functions23: BinaryAssociation = BinaryAssociation(
    name="functions23",
    ends={
        Property(name="thingml_Function25", type=thingml_Thing, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_Thing24", type=thingml_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action49: BinaryAssociation = BinaryAssociation(
    name="action49",
    ends={
        Property(name="thingml_Handler50", type=thingml_Action, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="thingml_Action51", type=thingml_Handler, multiplicity=Multiplicity(1, 1))
    }
)
target52: BinaryAssociation = BinaryAssociation(
    name="target52",
    ends={
        Property(name="State", type=thingml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=thingml_State, multiplicity=Multiplicity(1, 1))
    }
)
source53: BinaryAssociation = BinaryAssociation(
    name="source53",
    ends={
        Property(name="State54", type=thingml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=thingml_State, multiplicity=Multiplicity(1, 1))
    }
)
init30: BinaryAssociation = BinaryAssociation(
    name="init30",
    ends={
        Property(name="thingml_Expression32", type=thingml_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_Property31", type=thingml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
after55: BinaryAssociation = BinaryAssociation(
    name="after55",
    ends={
        Property(name="thingml_Action56", type=thingml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_Transition", type=thingml_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init33: BinaryAssociation = BinaryAssociation(
    name="init33",
    ends={
        Property(name="thingml_Expression35", type=thingml_PropertyAssign, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_PropertyAssign34", type=thingml_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
property36: BinaryAssociation = BinaryAssociation(
    name="property36",
    ends={
        Property(name="thingml_Property38", type=thingml_PropertyAssign, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_PropertyAssign37", type=thingml_Property, multiplicity=Multiplicity(1, 1))
    }
)
index39: BinaryAssociation = BinaryAssociation(
    name="index39",
    ends={
        Property(name="thingml_Expression41", type=thingml_PropertyAssign, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_PropertyAssign40", type=thingml_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
literals42: BinaryAssociation = BinaryAssociation(
    name="literals42",
    ends={
        Property(name="EnumerationLiteral", type=thingml_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="enum", type=thingml_EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enum43: BinaryAssociation = BinaryAssociation(
    name="enum43",
    ends={
        Property(name="Enumeration", type=thingml_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="literals", type=thingml_Enumeration, multiplicity=Multiplicity(1, 1))
    }
)
annotations44: BinaryAssociation = BinaryAssociation(
    name="annotations44",
    ends={
        Property(name="thingml_PlatformAnnotation", type=thingml_AnnotatedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_AnnotatedElement", type=thingml_PlatformAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
event45: BinaryAssociation = BinaryAssociation(
    name="event45",
    ends={
        Property(name="thingml_Event", type=thingml_Handler, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_Handler", type=thingml_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guard46: BinaryAssociation = BinaryAssociation(
    name="guard46",
    ends={
        Property(name="thingml_Expression48", type=thingml_Handler, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_Handler47", type=thingml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actions79: BinaryAssociation = BinaryAssociation(
    name="actions79",
    ends={
        Property(name="thingml_Action80", type=thingml_ActionBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_ActionBlock", type=thingml_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
segments81: BinaryAssociation = BinaryAssociation(
    name="segments81",
    ends={
        Property(name="thingml_Expression82", type=thingml_ExternStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_ExternStatement", type=thingml_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
before57: BinaryAssociation = BinaryAssociation(
    name="before57",
    ends={
        Property(name="thingml_Action59", type=thingml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_Transition58", type=thingml_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outgoing60: BinaryAssociation = BinaryAssociation(
    name="outgoing60",
    ends={
        Property(name="Transition", type=thingml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=thingml_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming61: BinaryAssociation = BinaryAssociation(
    name="incoming61",
    ends={
        Property(name="Transition62", type=thingml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=thingml_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
entry63: BinaryAssociation = BinaryAssociation(
    name="entry63",
    ends={
        Property(name="thingml_Action64", type=thingml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_State", type=thingml_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exit65: BinaryAssociation = BinaryAssociation(
    name="exit65",
    ends={
        Property(name="thingml_Action67", type=thingml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_State66", type=thingml_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
properties68: BinaryAssociation = BinaryAssociation(
    name="properties68",
    ends={
        Property(name="thingml_Property70", type=thingml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_State69", type=thingml_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
internal71: BinaryAssociation = BinaryAssociation(
    name="internal71",
    ends={
        Property(name="thingml_InternalTransition", type=thingml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_State72", type=thingml_InternalTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
region73: BinaryAssociation = BinaryAssociation(
    name="region73",
    ends={
        Property(name="thingml_ParallelRegion", type=thingml_CompositeState, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_CompositeState", type=thingml_ParallelRegion, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
substate74: BinaryAssociation = BinaryAssociation(
    name="substate74",
    ends={
        Property(name="thingml_State75", type=thingml_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_Region", type=thingml_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initial76: BinaryAssociation = BinaryAssociation(
    name="initial76",
    ends={
        Property(name="thingml_State78", type=thingml_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_Region77", type=thingml_State, multiplicity=Multiplicity(1, 1))
    }
)
owner106: BinaryAssociation = BinaryAssociation(
    name="owner106",
    ends={
        Property(name="Thing", type=thingml_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="ports", type=thingml_Thing, multiplicity=Multiplicity(0, 1))
    }
)
receives107: BinaryAssociation = BinaryAssociation(
    name="receives107",
    ends={
        Property(name="thingml_Message109", type=thingml_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_Port108", type=thingml_Message, multiplicity=Multiplicity(0, 9999))
    }
)
sends110: BinaryAssociation = BinaryAssociation(
    name="sends110",
    ends={
        Property(name="thingml_Message112", type=thingml_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_Port111", type=thingml_Message, multiplicity=Multiplicity(0, 9999))
    }
)
msgRef113: BinaryAssociation = BinaryAssociation(
    name="msgRef113",
    ends={
        Property(name="thingml_ReceiveMessage114", type=thingml_EventReference, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_EventReference", type=thingml_ReceiveMessage, multiplicity=Multiplicity(1, 1))
    }
)
segments83: BinaryAssociation = BinaryAssociation(
    name="segments83",
    ends={
        Property(name="thingml_Expression84", type=thingml_ExternExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_ExternExpression", type=thingml_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters85: BinaryAssociation = BinaryAssociation(
    name="parameters85",
    ends={
        Property(name="thingml_Expression86", type=thingml_SendAction, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_SendAction", type=thingml_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
message87: BinaryAssociation = BinaryAssociation(
    name="message87",
    ends={
        Property(name="thingml_Message89", type=thingml_SendAction, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_SendAction88", type=thingml_Message, multiplicity=Multiplicity(1, 1))
    }
)
port90: BinaryAssociation = BinaryAssociation(
    name="port90",
    ends={
        Property(name="thingml_Port", type=thingml_SendAction, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_SendAction91", type=thingml_Port, multiplicity=Multiplicity(1, 1))
    }
)
property92: BinaryAssociation = BinaryAssociation(
    name="property92",
    ends={
        Property(name="thingml_Variable", type=thingml_VariableAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_VariableAssignment", type=thingml_Variable, multiplicity=Multiplicity(1, 1))
    }
)
expression93: BinaryAssociation = BinaryAssociation(
    name="expression93",
    ends={
        Property(name="thingml_Expression95", type=thingml_VariableAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_VariableAssignment94", type=thingml_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
index96: BinaryAssociation = BinaryAssociation(
    name="index96",
    ends={
        Property(name="thingml_Expression98", type=thingml_VariableAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_VariableAssignment97", type=thingml_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
message99: BinaryAssociation = BinaryAssociation(
    name="message99",
    ends={
        Property(name="thingml_Message100", type=thingml_ReceiveMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_ReceiveMessage", type=thingml_Message, multiplicity=Multiplicity(1, 1))
    }
)
port101: BinaryAssociation = BinaryAssociation(
    name="port101",
    ends={
        Property(name="thingml_Port103", type=thingml_ReceiveMessage, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_ReceiveMessage102", type=thingml_Port, multiplicity=Multiplicity(1, 1))
    }
)
indexType104: BinaryAssociation = BinaryAssociation(
    name="indexType104",
    ends={
        Property(name="thingml_Type105", type=thingml_Dictionary, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_Dictionary", type=thingml_Type, multiplicity=Multiplicity(1, 1))
    }
)
rhs125: BinaryAssociation = BinaryAssociation(
    name="rhs125",
    ends={
        Property(name="thingml_Expression127", type=thingml_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_BinaryExpression126", type=thingml_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
paramRef115: BinaryAssociation = BinaryAssociation(
    name="paramRef115",
    ends={
        Property(name="thingml_Parameter117", type=thingml_EventReference, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_EventReference116", type=thingml_Parameter, multiplicity=Multiplicity(1, 1))
    }
)
enum118: BinaryAssociation = BinaryAssociation(
    name="enum118",
    ends={
        Property(name="thingml_Enumeration", type=thingml_EnumLiteralRef, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_EnumLiteralRef", type=thingml_Enumeration, multiplicity=Multiplicity(1, 1))
    }
)
literal119: BinaryAssociation = BinaryAssociation(
    name="literal119",
    ends={
        Property(name="thingml_EnumerationLiteral", type=thingml_EnumLiteralRef, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_EnumLiteralRef120", type=thingml_EnumerationLiteral, multiplicity=Multiplicity(1, 1))
    }
)
term121: BinaryAssociation = BinaryAssociation(
    name="term121",
    ends={
        Property(name="thingml_Expression122", type=thingml_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_UnaryExpression", type=thingml_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lhs123: BinaryAssociation = BinaryAssociation(
    name="lhs123",
    ends={
        Property(name="thingml_Expression124", type=thingml_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_BinaryExpression", type=thingml_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exp144: BinaryAssociation = BinaryAssociation(
    name="exp144",
    ends={
        Property(name="thingml_Expression145", type=thingml_ReturnAction, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_ReturnAction", type=thingml_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
msg146: BinaryAssociation = BinaryAssociation(
    name="msg146",
    ends={
        Property(name="thingml_Expression147", type=thingml_PrintAction, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_PrintAction", type=thingml_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
msg148: BinaryAssociation = BinaryAssociation(
    name="msg148",
    ends={
        Property(name="thingml_Expression149", type=thingml_ErrorAction, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_ErrorAction", type=thingml_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
instances150: BinaryAssociation = BinaryAssociation(
    name="instances150",
    ends={
        Property(name="thingml_Instance", type=thingml_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_Configuration151", type=thingml_Instance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action128: BinaryAssociation = BinaryAssociation(
    name="action128",
    ends={
        Property(name="thingml_Action129", type=thingml_ControlStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_ControlStructure", type=thingml_Action, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition130: BinaryAssociation = BinaryAssociation(
    name="condition130",
    ends={
        Property(name="thingml_Expression132", type=thingml_ControlStructure, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_ControlStructure131", type=thingml_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
property133: BinaryAssociation = BinaryAssociation(
    name="property133",
    ends={
        Property(name="thingml_Variable134", type=thingml_PropertyReference, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_PropertyReference", type=thingml_Variable, multiplicity=Multiplicity(1, 1))
    }
)
array135: BinaryAssociation = BinaryAssociation(
    name="array135",
    ends={
        Property(name="thingml_Expression136", type=thingml_ArrayIndex, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_ArrayIndex", type=thingml_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
index137: BinaryAssociation = BinaryAssociation(
    name="index137",
    ends={
        Property(name="thingml_Expression139", type=thingml_ArrayIndex, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_ArrayIndex138", type=thingml_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
index140: BinaryAssociation = BinaryAssociation(
    name="index140",
    ends={
        Property(name="thingml_Expression141", type=thingml_DictionaryReference, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_DictionaryReference", type=thingml_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exp142: BinaryAssociation = BinaryAssociation(
    name="exp142",
    ends={
        Property(name="thingml_Expression143", type=thingml_ExpressionGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_ExpressionGroup", type=thingml_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
instance179: BinaryAssociation = BinaryAssociation(
    name="instance179",
    ends={
        Property(name="thingml_InstanceRef181", type=thingml_ConfigPropertyAssign, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_ConfigPropertyAssign180", type=thingml_InstanceRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
index182: BinaryAssociation = BinaryAssociation(
    name="index182",
    ends={
        Property(name="thingml_Expression184", type=thingml_ConfigPropertyAssign, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_ConfigPropertyAssign183", type=thingml_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
config185: BinaryAssociation = BinaryAssociation(
    name="config185",
    ends={
        Property(name="thingml_Configuration187", type=thingml_ConfigInclude, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_ConfigInclude186", type=thingml_Configuration, multiplicity=Multiplicity(1, 1))
    }
)
config188: BinaryAssociation = BinaryAssociation(
    name="config188",
    ends={
        Property(name="thingml_ConfigInclude190", type=thingml_InstanceRef, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_InstanceRef189", type=thingml_ConfigInclude, multiplicity=Multiplicity(0, 9999))
    }
)
instance191: BinaryAssociation = BinaryAssociation(
    name="instance191",
    ends={
        Property(name="thingml_Instance193", type=thingml_InstanceRef, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_InstanceRef192", type=thingml_Instance, multiplicity=Multiplicity(1, 1))
    }
)
connectors152: BinaryAssociation = BinaryAssociation(
    name="connectors152",
    ends={
        Property(name="thingml_Connector", type=thingml_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_Configuration153", type=thingml_Connector, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
configs154: BinaryAssociation = BinaryAssociation(
    name="configs154",
    ends={
        Property(name="thingml_ConfigInclude", type=thingml_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_Configuration155", type=thingml_ConfigInclude, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
propassigns156: BinaryAssociation = BinaryAssociation(
    name="propassigns156",
    ends={
        Property(name="thingml_ConfigPropertyAssign", type=thingml_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_Configuration157", type=thingml_ConfigPropertyAssign, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type158: BinaryAssociation = BinaryAssociation(
    name="type158",
    ends={
        Property(name="thingml_Thing160", type=thingml_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_Instance159", type=thingml_Thing, multiplicity=Multiplicity(1, 1))
    }
)
assign161: BinaryAssociation = BinaryAssociation(
    name="assign161",
    ends={
        Property(name="thingml_PropertyAssign163", type=thingml_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_Instance162", type=thingml_PropertyAssign, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
srv164: BinaryAssociation = BinaryAssociation(
    name="srv164",
    ends={
        Property(name="thingml_InstanceRef", type=thingml_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_Connector165", type=thingml_InstanceRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
cli166: BinaryAssociation = BinaryAssociation(
    name="cli166",
    ends={
        Property(name="thingml_InstanceRef168", type=thingml_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_Connector167", type=thingml_InstanceRef, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
required169: BinaryAssociation = BinaryAssociation(
    name="required169",
    ends={
        Property(name="thingml_RequiredPort", type=thingml_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_Connector170", type=thingml_RequiredPort, multiplicity=Multiplicity(1, 1))
    }
)
provided171: BinaryAssociation = BinaryAssociation(
    name="provided171",
    ends={
        Property(name="thingml_ProvidedPort", type=thingml_Connector, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_Connector172", type=thingml_ProvidedPort, multiplicity=Multiplicity(1, 1))
    }
)
init173: BinaryAssociation = BinaryAssociation(
    name="init173",
    ends={
        Property(name="thingml_Expression175", type=thingml_ConfigPropertyAssign, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_ConfigPropertyAssign174", type=thingml_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
property176: BinaryAssociation = BinaryAssociation(
    name="property176",
    ends={
        Property(name="thingml_Property178", type=thingml_ConfigPropertyAssign, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_ConfigPropertyAssign177", type=thingml_Property, multiplicity=Multiplicity(1, 1))
    }
)
parameters194: BinaryAssociation = BinaryAssociation(
    name="parameters194",
    ends={
        Property(name="thingml_Expression195", type=thingml_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_FunctionCall", type=thingml_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
function196: BinaryAssociation = BinaryAssociation(
    name="function196",
    ends={
        Property(name="thingml_Function198", type=thingml_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_FunctionCall197", type=thingml_Function, multiplicity=Multiplicity(1, 1))
    }
)
init199: BinaryAssociation = BinaryAssociation(
    name="init199",
    ends={
        Property(name="thingml_Expression200", type=thingml_LocalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="thingml_LocalVariable", type=thingml_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_thingml_Function_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingml_Function)
gen_thingml_Function_TypedElement = Generalization(general=TypedElement, specific=thingml_Function)
gen_thingml_Type_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingml_Type)
gen_thingml_Message_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingml_Message)
gen_thingml_Thing_Type = Generalization(general=Type, specific=thingml_Thing)
gen_thingml_Parameter_Variable = Generalization(general=Variable, specific=thingml_Parameter)
gen_thingml_Variable_TypedElement = Generalization(general=TypedElement, specific=thingml_Variable)
gen_thingml_Variable_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingml_Variable)
gen_thingml_Transition_Handler = Generalization(general=Handler, specific=thingml_Transition)
gen_thingml_Property_Variable = Generalization(general=Variable, specific=thingml_Property)
gen_thingml_PropertyAssign_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingml_PropertyAssign)
gen_thingml_PlatformAnnotation_ThingMLElement = Generalization(general=ThingMLElement, specific=thingml_PlatformAnnotation)
gen_thingml_Enumeration_Type = Generalization(general=Type, specific=thingml_Enumeration)
gen_thingml_PrimitiveType_Type = Generalization(general=Type, specific=thingml_PrimitiveType)
gen_thingml_EnumerationLiteral_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingml_EnumerationLiteral)
gen_thingml_AnnotatedElement_ThingMLElement = Generalization(general=ThingMLElement, specific=thingml_AnnotatedElement)
gen_thingml_StateMachine_CompositeState = Generalization(general=CompositeState, specific=thingml_StateMachine)
gen_thingml_Handler_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingml_Handler)
gen_thingml_ParallelRegion_Region = Generalization(general=Region, specific=thingml_ParallelRegion)
gen_thingml_ActionBlock_Action = Generalization(general=Action, specific=thingml_ActionBlock)
gen_thingml_ExternStatement_Action = Generalization(general=Action, specific=thingml_ExternStatement)
gen_thingml_ExternExpression_Expression = Generalization(general=Expression, specific=thingml_ExternExpression)
gen_thingml_InternalTransition_Handler = Generalization(general=Handler, specific=thingml_InternalTransition)
gen_thingml_State_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingml_State)
gen_thingml_CompositeState_State = Generalization(general=State, specific=thingml_CompositeState)
gen_thingml_CompositeState_Region = Generalization(general=Region, specific=thingml_CompositeState)
gen_thingml_Region_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingml_Region)
gen_thingml_Port_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingml_Port)
gen_thingml_RequiredPort_Port = Generalization(general=Port, specific=thingml_RequiredPort)
gen_thingml_ProvidedPort_Port = Generalization(general=Port, specific=thingml_ProvidedPort)
gen_thingml_EventReference_Expression = Generalization(general=Expression, specific=thingml_EventReference)
gen_thingml_SendAction_Action = Generalization(general=Action, specific=thingml_SendAction)
gen_thingml_VariableAssignment_Action = Generalization(general=Action, specific=thingml_VariableAssignment)
gen_thingml_Event_ThingMLElement = Generalization(general=ThingMLElement, specific=thingml_Event)
gen_thingml_ReceiveMessage_Event = Generalization(general=Event, specific=thingml_ReceiveMessage)
gen_thingml_Dictionary_Property = Generalization(general=Property_, specific=thingml_Dictionary)
gen_thingml_PlusExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=thingml_PlusExpression)
gen_thingml_MinusExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=thingml_MinusExpression)
gen_thingml_TimesExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=thingml_TimesExpression)
gen_thingml_DivExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=thingml_DivExpression)
gen_thingml_ModExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=thingml_ModExpression)
gen_thingml_EqualsExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=thingml_EqualsExpression)
gen_thingml_GreaterExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=thingml_GreaterExpression)
gen_thingml_LowerExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=thingml_LowerExpression)
gen_thingml_AndExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=thingml_AndExpression)
gen_thingml_OrExpression_BinaryExpression = Generalization(general=BinaryExpression, specific=thingml_OrExpression)
gen_thingml_Literal_Expression = Generalization(general=Expression, specific=thingml_Literal)
gen_thingml_EnumLiteralRef_Literal = Generalization(general=Literal, specific=thingml_EnumLiteralRef)
gen_thingml_IntegerLiteral_Literal = Generalization(general=Literal, specific=thingml_IntegerLiteral)
gen_thingml_BooleanLiteral_Literal = Generalization(general=Literal, specific=thingml_BooleanLiteral)
gen_thingml_StringLiteral_Literal = Generalization(general=Literal, specific=thingml_StringLiteral)
gen_thingml_DoubleLiteral_Literal = Generalization(general=Literal, specific=thingml_DoubleLiteral)
gen_thingml_UnaryExpression_Expression = Generalization(general=Expression, specific=thingml_UnaryExpression)
gen_thingml_NotExpression_UnaryExpression = Generalization(general=UnaryExpression, specific=thingml_NotExpression)
gen_thingml_UnaryMinus_UnaryExpression = Generalization(general=UnaryExpression, specific=thingml_UnaryMinus)
gen_thingml_BinaryExpression_Expression = Generalization(general=Expression, specific=thingml_BinaryExpression)
gen_thingml_PrintAction_Action = Generalization(general=Action, specific=thingml_PrintAction)
gen_thingml_ErrorAction_Action = Generalization(general=Action, specific=thingml_ErrorAction)
gen_thingml_Configuration_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingml_Configuration)
gen_thingml_ControlStructure_Action = Generalization(general=Action, specific=thingml_ControlStructure)
gen_thingml_LoopAction_ControlStructure = Generalization(general=ControlStructure, specific=thingml_LoopAction)
gen_thingml_ConditionalAction_ControlStructure = Generalization(general=ControlStructure, specific=thingml_ConditionalAction)
gen_thingml_PropertyReference_Expression = Generalization(general=Expression, specific=thingml_PropertyReference)
gen_thingml_ArrayIndex_Expression = Generalization(general=Expression, specific=thingml_ArrayIndex)
gen_thingml_DictionaryReference_PropertyReference = Generalization(general=PropertyReference, specific=thingml_DictionaryReference)
gen_thingml_ExpressionGroup_Expression = Generalization(general=Expression, specific=thingml_ExpressionGroup)
gen_thingml_ReturnAction_Action = Generalization(general=Action, specific=thingml_ReturnAction)
gen_thingml_ConfigInclude_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingml_ConfigInclude)
gen_thingml_Instance_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingml_Instance)
gen_thingml_Connector_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingml_Connector)
gen_thingml_ConfigPropertyAssign_AnnotatedElement = Generalization(general=AnnotatedElement, specific=thingml_ConfigPropertyAssign)
gen_thingml_FunctionCallStatement_Action = Generalization(general=Action, specific=thingml_FunctionCallStatement)
gen_thingml_FunctionCallStatement_FunctionCall = Generalization(general=FunctionCall, specific=thingml_FunctionCallStatement)
gen_thingml_FunctionCallExpression_FunctionCall = Generalization(general=FunctionCall, specific=thingml_FunctionCallExpression)
gen_thingml_FunctionCallExpression_Expression = Generalization(general=Expression, specific=thingml_FunctionCallExpression)
gen_thingml_LocalVariable_Variable = Generalization(general=Variable, specific=thingml_LocalVariable)
gen_thingml_LocalVariable_Action = Generalization(general=Action, specific=thingml_LocalVariable)

# Domain Model
domain_model = DomainModel(
    name="thingml",
    types={thingml_Function, AnnotatedElement, TypedElement, thingml_Parameter, thingml_ThingMLModel, thingml_Type, thingml_Configuration, thingml_ThingMLElement, thingml_TypedElement, thingml_Expression, thingml_Action, thingml_Message, thingml_Thing, Type, thingml_Property, thingml_Port, thingml_StateMachine, thingml_PropertyAssign, Variable, thingml_Variable, thingml_Transition, Handler, thingml_State, thingml_PlatformAnnotation, ThingMLElement, thingml_Enumeration, thingml_EnumerationLiteral, thingml_PrimitiveType, thingml_AnnotatedElement, CompositeState, thingml_Handler, thingml_Event, thingml_ActionBlock, Action, thingml_ExternStatement, thingml_ExternExpression, Expression, thingml_InternalTransition, thingml_CompositeState, State, Region, thingml_ParallelRegion, thingml_Region, thingml_RequiredPort, Port, thingml_ProvidedPort, thingml_EventReference, thingml_SendAction, thingml_VariableAssignment, thingml_ReceiveMessage, Event, thingml_Dictionary, Property_, thingml_PlusExpression, BinaryExpression, thingml_MinusExpression, thingml_TimesExpression, thingml_DivExpression, thingml_ModExpression, thingml_EqualsExpression, thingml_GreaterExpression, thingml_LowerExpression, thingml_AndExpression, thingml_OrExpression, thingml_Literal, thingml_EnumLiteralRef, Literal, thingml_IntegerLiteral, thingml_BooleanLiteral, thingml_StringLiteral, thingml_DoubleLiteral, thingml_UnaryExpression, thingml_NotExpression, UnaryExpression, thingml_UnaryMinus, thingml_BinaryExpression, thingml_PrintAction, thingml_ErrorAction, thingml_Instance, thingml_Connector, thingml_ControlStructure, thingml_LoopAction, ControlStructure, thingml_ConditionalAction, thingml_PropertyReference, thingml_ArrayIndex, thingml_DictionaryReference, PropertyReference, thingml_ExpressionGroup, thingml_ReturnAction, thingml_FunctionCall, thingml_ConfigInclude, thingml_ConfigPropertyAssign, thingml_InstanceRef, thingml_FunctionCallStatement, FunctionCall, thingml_FunctionCallExpression, thingml_LocalVariable},
    associations={configs4, types0, imports2, type26, cardinality28, parameters6, body7, parameters9, properties11, ports12, behaviour13, includes16, assign18, messages20, functions23, action49, target52, source53, init30, after55, init33, property36, index39, literals42, enum43, annotations44, event45, guard46, actions79, segments81, before57, outgoing60, incoming61, entry63, exit65, properties68, internal71, region73, substate74, initial76, owner106, receives107, sends110, msgRef113, segments83, parameters85, message87, port90, property92, expression93, index96, message99, port101, indexType104, rhs125, paramRef115, enum118, literal119, term121, lhs123, exp144, msg146, msg148, instances150, action128, condition130, property133, array135, index137, index140, exp142, instance179, index182, config185, config188, instance191, connectors152, configs154, propassigns156, type158, assign161, srv164, cli166, required169, provided171, init173, property176, parameters194, function196, init199},
    generalizations={gen_thingml_Function_AnnotatedElement, gen_thingml_Function_TypedElement, gen_thingml_Type_AnnotatedElement, gen_thingml_Message_AnnotatedElement, gen_thingml_Thing_Type, gen_thingml_Parameter_Variable, gen_thingml_Variable_TypedElement, gen_thingml_Variable_AnnotatedElement, gen_thingml_Transition_Handler, gen_thingml_Property_Variable, gen_thingml_PropertyAssign_AnnotatedElement, gen_thingml_PlatformAnnotation_ThingMLElement, gen_thingml_Enumeration_Type, gen_thingml_PrimitiveType_Type, gen_thingml_EnumerationLiteral_AnnotatedElement, gen_thingml_AnnotatedElement_ThingMLElement, gen_thingml_StateMachine_CompositeState, gen_thingml_Handler_AnnotatedElement, gen_thingml_ParallelRegion_Region, gen_thingml_ActionBlock_Action, gen_thingml_ExternStatement_Action, gen_thingml_ExternExpression_Expression, gen_thingml_InternalTransition_Handler, gen_thingml_State_AnnotatedElement, gen_thingml_CompositeState_State, gen_thingml_CompositeState_Region, gen_thingml_Region_AnnotatedElement, gen_thingml_Port_AnnotatedElement, gen_thingml_RequiredPort_Port, gen_thingml_ProvidedPort_Port, gen_thingml_EventReference_Expression, gen_thingml_SendAction_Action, gen_thingml_VariableAssignment_Action, gen_thingml_Event_ThingMLElement, gen_thingml_ReceiveMessage_Event, gen_thingml_Dictionary_Property, gen_thingml_PlusExpression_BinaryExpression, gen_thingml_MinusExpression_BinaryExpression, gen_thingml_TimesExpression_BinaryExpression, gen_thingml_DivExpression_BinaryExpression, gen_thingml_ModExpression_BinaryExpression, gen_thingml_EqualsExpression_BinaryExpression, gen_thingml_GreaterExpression_BinaryExpression, gen_thingml_LowerExpression_BinaryExpression, gen_thingml_AndExpression_BinaryExpression, gen_thingml_OrExpression_BinaryExpression, gen_thingml_Literal_Expression, gen_thingml_EnumLiteralRef_Literal, gen_thingml_IntegerLiteral_Literal, gen_thingml_BooleanLiteral_Literal, gen_thingml_StringLiteral_Literal, gen_thingml_DoubleLiteral_Literal, gen_thingml_UnaryExpression_Expression, gen_thingml_NotExpression_UnaryExpression, gen_thingml_UnaryMinus_UnaryExpression, gen_thingml_BinaryExpression_Expression, gen_thingml_PrintAction_Action, gen_thingml_ErrorAction_Action, gen_thingml_Configuration_AnnotatedElement, gen_thingml_ControlStructure_Action, gen_thingml_LoopAction_ControlStructure, gen_thingml_ConditionalAction_ControlStructure, gen_thingml_PropertyReference_Expression, gen_thingml_ArrayIndex_Expression, gen_thingml_DictionaryReference_PropertyReference, gen_thingml_ExpressionGroup_Expression, gen_thingml_ReturnAction_Action, gen_thingml_ConfigInclude_AnnotatedElement, gen_thingml_Instance_AnnotatedElement, gen_thingml_Connector_AnnotatedElement, gen_thingml_ConfigPropertyAssign_AnnotatedElement, gen_thingml_FunctionCallStatement_Action, gen_thingml_FunctionCallStatement_FunctionCall, gen_thingml_FunctionCallExpression_FunctionCall, gen_thingml_FunctionCallExpression_Expression, gen_thingml_LocalVariable_Variable, gen_thingml_LocalVariable_Action},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)