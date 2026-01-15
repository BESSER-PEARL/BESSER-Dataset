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
VariableModifier: Enumeration = Enumeration(
    name="VariableModifier",
    literals={
            EnumerationLiteral(name="VAR"),
			EnumerationLiteral(name="CONST")
    }
)

TriggerType: Enumeration = Enumeration(
    name="TriggerType",
    literals={
            EnumerationLiteral(name="SIMPLE"),
			EnumerationLiteral(name="INPUT"),
			EnumerationLiteral(name="OUTPUT"),
			EnumerationLiteral(name="SYNC"),
			EnumerationLiteral(name="EMPTY")
    }
)

# Classes
robochart_RCPackage = Class(name="robochart::RCPackage")
BasicPackage = Class(name="BasicPackage")
robochart_Interface = Class(name="robochart::Interface")
robochart_RoboticPlatformDef = Class(name="robochart::RoboticPlatformDef")
robochart_TypeDecl = Class(name="robochart::TypeDecl", is_abstract=True)
robochart_BasicPackage = Class(name="robochart::BasicPackage")
robochart_Import = Class(name="robochart::Import")
robochart_OperationDef = Class(name="robochart::OperationDef")
robochart_Function = Class(name="robochart::Function")
robochart_NamedElement = Class(name="robochart::NamedElement", is_abstract=True)
robochart_StateMachineDef = Class(name="robochart::StateMachineDef")
robochart_ControllerDef = Class(name="robochart::ControllerDef")
robochart_RCModule = Class(name="robochart::RCModule")
Member = Class(name="Member")
NamedExpression = Class(name="NamedExpression")
robochart_TypedNamedElement = Class(name="robochart::TypedNamedElement", is_abstract=True)
robochart_Type = Class(name="robochart::Type", is_abstract=True)
robochart_Member = Class(name="robochart::Member", is_abstract=True)
TypedNamedElement = Class(name="TypedNamedElement")
robochart_Enumeration = Class(name="robochart::Enumeration")
robochart_Literal = Class(name="robochart::Literal")
NamedElement = Class(name="NamedElement")
robochart_PrimitiveType = Class(name="robochart::PrimitiveType")
TypeDecl = Class(name="TypeDecl")
robochart_RecordType = Class(name="robochart::RecordType")
robochart_Field = Class(name="robochart::Field")
robochart_ProductType = Class(name="robochart::ProductType")
Type = Class(name="Type")
robochart_RelationType = Class(name="robochart::RelationType")
robochart_NameType = Class(name="robochart::NameType")
robochart_VariableList = Class(name="robochart::VariableList")
robochart_Variable = Class(name="robochart::Variable")
robochart_Expression = Class(name="robochart::Expression", is_abstract=True)
robochart_FunctionType = Class(name="robochart::FunctionType")
RelationType = Class(name="RelationType")
robochart_SetType = Class(name="robochart::SetType")
robochart_SeqType = Class(name="robochart::SeqType")
SetType = Class(name="SetType")
robochart_TypeRef = Class(name="robochart::TypeRef")
robochart_AnyType = Class(name="robochart::AnyType")
robochart_Parameter = Class(name="robochart::Parameter")
Variable = Class(name="Variable")
robochart_OperationSig = Class(name="robochart::OperationSig")
robochart_Event = Class(name="robochart::Event")
robochart_Operation = Class(name="robochart::Operation", is_abstract=True)
ConnectionNode = Class(name="ConnectionNode")
Operation = Class(name="Operation")
OperationSig = Class(name="OperationSig")
StateMachineBody = Class(name="StateMachineBody")
robochart_Reference = Class(name="robochart::Reference", is_abstract=True)
robochart_OperationRef = Class(name="robochart::OperationRef")
Reference = Class(name="Reference")
robochart_Clock = Class(name="robochart::Clock")
robochart_RoboticPlatform = Class(name="robochart::RoboticPlatform", is_abstract=True)
Context = Class(name="Context")
RoboticPlatform = Class(name="RoboticPlatform")
robochart_Context = Class(name="robochart::Context", is_abstract=True)
BasicContext = Class(name="BasicContext")
robochart_BasicContext = Class(name="robochart::BasicContext", is_abstract=True)
robochart_StateMachine = Class(name="robochart::StateMachine", is_abstract=True)
StateMachine = Class(name="StateMachine")
robochart_StateMachineRef = Class(name="robochart::StateMachineRef")
robochart_StateMachineBody = Class(name="robochart::StateMachineBody")
NodeContainer = Class(name="NodeContainer")
robochart_RoboticPlatformRef = Class(name="robochart::RoboticPlatformRef")
robochart_Initial = Class(name="robochart::Initial")
Junction = Class(name="Junction")
robochart_State = Class(name="robochart::State")
robochart_Action = Class(name="robochart::Action", is_abstract=True)
robochart_Final = Class(name="robochart::Final")
State = Class(name="State")
robochart_ProbabilisticJunction = Class(name="robochart::ProbabilisticJunction")
robochart_NodeContainer = Class(name="robochart::NodeContainer", is_abstract=True)
robochart_Node = Class(name="robochart::Node", is_abstract=True)
robochart_Transition = Class(name="robochart::Transition")
robochart_Junction = Class(name="robochart::Junction")
Node = Class(name="Node")
robochart_Statement = Class(name="robochart::Statement", is_abstract=True)
robochart_Trigger = Class(name="robochart::Trigger")
robochart_EntryAction = Class(name="robochart::EntryAction")
Action = Class(name="Action")
robochart_DuringAction = Class(name="robochart::DuringAction")
robochart_ExitAction = Class(name="robochart::ExitAction")
robochart_Controller = Class(name="robochart::Controller", is_abstract=True)
robochart_ClockReset = Class(name="robochart::ClockReset")
robochart_ConnectionNode = Class(name="robochart::ConnectionNode", is_abstract=True)
Controller = Class(name="Controller")
robochart_Connection = Class(name="robochart::Connection")
robochart_TimedStatement = Class(name="robochart::TimedStatement")
Statement = Class(name="Statement")
robochart_ControllerRef = Class(name="robochart::ControllerRef")
robochart_Wait = Class(name="robochart::Wait")
robochart_Skip = Class(name="robochart::Skip")
robochart_IfStmt = Class(name="robochart::IfStmt")
robochart_ResultExp = Class(name="robochart::ResultExp")
Expression = Class(name="Expression")
robochart_ArrayExp = Class(name="robochart::ArrayExp")
robochart_ClockExp = Class(name="robochart::ClockExp")
robochart_StateClockExp = Class(name="robochart::StateClockExp")
robochart_BinaryExpression = Class(name="robochart::BinaryExpression", is_abstract=True)
robochart_Assignment = Class(name="robochart::Assignment")
robochart_Assignable = Class(name="robochart::Assignable", is_abstract=True)
robochart_SendEvent = Class(name="robochart::SendEvent")
robochart_SeqStatement = Class(name="robochart::SeqStatement")
robochart_ParStmt = Class(name="robochart::ParStmt")
robochart_Call = Class(name="robochart::Call")
robochart_DefiniteDescription = Class(name="robochart::DefiniteDescription")
LambdaExp = Class(name="LambdaExp")
robochart_IfExpression = Class(name="robochart::IfExpression")
robochart_Declaration = Class(name="robochart::Declaration")
robochart_LetExpression = Class(name="robochart::LetExpression")
robochart_Iff = Class(name="robochart::Iff")
BinaryExpression = Class(name="BinaryExpression")
robochart_Implies = Class(name="robochart::Implies")
robochart_Or = Class(name="robochart::Or")
robochart_QuantifierExpression = Class(name="robochart::QuantifierExpression", is_abstract=True)
robochart_Forall = Class(name="robochart::Forall")
QuantifierExpression = Class(name="QuantifierExpression")
robochart_Exists = Class(name="robochart::Exists")
robochart_LambdaExp = Class(name="robochart::LambdaExp")
robochart_And = Class(name="robochart::And")
robochart_Not = Class(name="robochart::Not")
robochart_InExp = Class(name="robochart::InExp")
robochart_GreaterOrEqual = Class(name="robochart::GreaterOrEqual")
robochart_LessThan = Class(name="robochart::LessThan")
robochart_LessOrEqual = Class(name="robochart::LessOrEqual")
robochart_Plus = Class(name="robochart::Plus")
robochart_Minus = Class(name="robochart::Minus")
robochart_Modulus = Class(name="robochart::Modulus")
robochart_Mult = Class(name="robochart::Mult")
robochart_Div = Class(name="robochart::Div")
robochart_Cat = Class(name="robochart::Cat")
robochart_TypeExp = Class(name="robochart::TypeExp")
robochart_Equals = Class(name="robochart::Equals")
robochart_Different = Class(name="robochart::Different")
robochart_GreaterThan = Class(name="robochart::GreaterThan")
robochart_Selection = Class(name="robochart::Selection")
robochart_IntegerExp = Class(name="robochart::IntegerExp")
robochart_FloatExp = Class(name="robochart::FloatExp")
robochart_Neg = Class(name="robochart::Neg")
robochart_BooleanExp = Class(name="robochart::BooleanExp")
robochart_VarExp = Class(name="robochart::VarExp")
robochart_RefExp = Class(name="robochart::RefExp")
robochart_NamedExpression = Class(name="robochart::NamedExpression", is_abstract=True)
robochart_ToExp = Class(name="robochart::ToExp")
robochart_FromExp = Class(name="robochart::FromExp")
robochart_StringExp = Class(name="robochart::StringExp")
robochart_IsExp = Class(name="robochart::IsExp")
robochart_EnumExp = Class(name="robochart::EnumExp")
robochart_IdExp = Class(name="robochart::IdExp")
robochart_ParExp = Class(name="robochart::ParExp")
robochart_AsExp = Class(name="robochart::AsExp")
robochart_SeqExp = Class(name="robochart::SeqExp")
robochart_SetExp = Class(name="robochart::SetExp")
robochart_SetComp = Class(name="robochart::SetComp")
robochart_SetRange = Class(name="robochart::SetRange")
robochart_TupleExp = Class(name="robochart::TupleExp")
robochart_RangeExp = Class(name="robochart::RangeExp")
robochart_CallExp = Class(name="robochart::CallExp")
robochart_ElseExp = Class(name="robochart::ElseExp")
robochart_VarSelection = Class(name="robochart::VarSelection")
Assignable = Class(name="Assignable")
robochart_ArrayAssignable = Class(name="robochart::ArrayAssignable")
robochart_VarRef = Class(name="robochart::VarRef")
robochart_WaitingCondition = Class(name="robochart::WaitingCondition")
robochart_WaitingConditionRef = Class(name="robochart::WaitingConditionRef")
robochart_VectorType = Class(name="robochart::VectorType")
robochart_MatrixType = Class(name="robochart::MatrixType")

# robochart_RCPackage class attributes and methods

# BasicPackage class attributes and methods

# robochart_Interface class attributes and methods

# robochart_RoboticPlatformDef class attributes and methods

# robochart_TypeDecl class attributes and methods

# robochart_BasicPackage class attributes and methods
robochart_BasicPackage_name: Property = Property(name="name", type=StringType)
robochart_BasicPackage.attributes={robochart_BasicPackage_name}

# robochart_Import class attributes and methods
robochart_Import_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
robochart_Import.attributes={robochart_Import_importedNamespace}

# robochart_OperationDef class attributes and methods

# robochart_Function class attributes and methods

# robochart_NamedElement class attributes and methods
robochart_NamedElement_name: Property = Property(name="name", type=StringType)
robochart_NamedElement.attributes={robochart_NamedElement_name}

# robochart_StateMachineDef class attributes and methods

# robochart_ControllerDef class attributes and methods

# robochart_RCModule class attributes and methods

# Member class attributes and methods

# NamedExpression class attributes and methods

# robochart_TypedNamedElement class attributes and methods

# robochart_Type class attributes and methods

# robochart_Member class attributes and methods

# TypedNamedElement class attributes and methods

# robochart_Enumeration class attributes and methods

# robochart_Literal class attributes and methods

# NamedElement class attributes and methods

# robochart_PrimitiveType class attributes and methods

# TypeDecl class attributes and methods

# robochart_RecordType class attributes and methods

# robochart_Field class attributes and methods

# robochart_ProductType class attributes and methods

# Type class attributes and methods

# robochart_RelationType class attributes and methods

# robochart_NameType class attributes and methods

# robochart_VariableList class attributes and methods
robochart_VariableList_modifier: Property = Property(name="modifier", type=StringType)
robochart_VariableList.attributes={robochart_VariableList_modifier}

# robochart_Variable class attributes and methods
robochart_Variable_modifier: Property = Property(name="modifier", type=StringType)
robochart_Variable.attributes={robochart_Variable_modifier}

# robochart_Expression class attributes and methods

# robochart_FunctionType class attributes and methods

# RelationType class attributes and methods

# robochart_SetType class attributes and methods

# robochart_SeqType class attributes and methods

# SetType class attributes and methods

# robochart_TypeRef class attributes and methods

# robochart_AnyType class attributes and methods
robochart_AnyType_identifier: Property = Property(name="identifier", type=StringType)
robochart_AnyType.attributes={robochart_AnyType_identifier}

# robochart_Parameter class attributes and methods

# Variable class attributes and methods

# robochart_OperationSig class attributes and methods
robochart_OperationSig_terminates: Property = Property(name="terminates", type=BooleanType)
robochart_OperationSig.attributes={robochart_OperationSig_terminates}

# robochart_Event class attributes and methods
robochart_Event_broadcast: Property = Property(name="broadcast", type=BooleanType)
robochart_Event.attributes={robochart_Event_broadcast}

# robochart_Operation class attributes and methods

# ConnectionNode class attributes and methods

# Operation class attributes and methods

# OperationSig class attributes and methods

# StateMachineBody class attributes and methods

# robochart_Reference class attributes and methods

# robochart_OperationRef class attributes and methods

# Reference class attributes and methods

# robochart_Clock class attributes and methods

# robochart_RoboticPlatform class attributes and methods

# Context class attributes and methods

# RoboticPlatform class attributes and methods

# robochart_Context class attributes and methods

# BasicContext class attributes and methods

# robochart_BasicContext class attributes and methods

# robochart_StateMachine class attributes and methods

# StateMachine class attributes and methods

# robochart_StateMachineRef class attributes and methods

# robochart_StateMachineBody class attributes and methods

# NodeContainer class attributes and methods

# robochart_RoboticPlatformRef class attributes and methods

# robochart_Initial class attributes and methods

# Junction class attributes and methods

# robochart_State class attributes and methods

# robochart_Action class attributes and methods

# robochart_Final class attributes and methods

# State class attributes and methods

# robochart_ProbabilisticJunction class attributes and methods

# robochart_NodeContainer class attributes and methods

# robochart_Node class attributes and methods

# robochart_Transition class attributes and methods

# robochart_Junction class attributes and methods

# Node class attributes and methods

# robochart_Statement class attributes and methods

# robochart_Trigger class attributes and methods
robochart_Trigger__type: Property = Property(name="_type", type=StringType)
robochart_Trigger.attributes={robochart_Trigger__type}

# robochart_EntryAction class attributes and methods

# Action class attributes and methods

# robochart_DuringAction class attributes and methods

# robochart_ExitAction class attributes and methods

# robochart_Controller class attributes and methods

# robochart_ClockReset class attributes and methods

# robochart_ConnectionNode class attributes and methods

# Controller class attributes and methods

# robochart_Connection class attributes and methods
robochart_Connection_async: Property = Property(name="async", type=BooleanType)
robochart_Connection_bidirec: Property = Property(name="bidirec", type=BooleanType)
robochart_Connection.attributes={robochart_Connection_bidirec, robochart_Connection_async}

# robochart_TimedStatement class attributes and methods

# Statement class attributes and methods

# robochart_ControllerRef class attributes and methods

# robochart_Wait class attributes and methods

# robochart_Skip class attributes and methods

# robochart_IfStmt class attributes and methods

# robochart_ResultExp class attributes and methods

# Expression class attributes and methods

# robochart_ArrayExp class attributes and methods

# robochart_ClockExp class attributes and methods

# robochart_StateClockExp class attributes and methods

# robochart_BinaryExpression class attributes and methods

# robochart_Assignment class attributes and methods

# robochart_Assignable class attributes and methods

# robochart_SendEvent class attributes and methods

# robochart_SeqStatement class attributes and methods

# robochart_ParStmt class attributes and methods

# robochart_Call class attributes and methods

# robochart_DefiniteDescription class attributes and methods

# LambdaExp class attributes and methods

# robochart_IfExpression class attributes and methods

# robochart_Declaration class attributes and methods

# robochart_LetExpression class attributes and methods

# robochart_Iff class attributes and methods

# BinaryExpression class attributes and methods

# robochart_Implies class attributes and methods

# robochart_Or class attributes and methods

# robochart_QuantifierExpression class attributes and methods

# robochart_Forall class attributes and methods

# QuantifierExpression class attributes and methods

# robochart_Exists class attributes and methods
robochart_Exists_unique: Property = Property(name="unique", type=BooleanType)
robochart_Exists.attributes={robochart_Exists_unique}

# robochart_LambdaExp class attributes and methods

# robochart_And class attributes and methods

# robochart_Not class attributes and methods

# robochart_InExp class attributes and methods

# robochart_GreaterOrEqual class attributes and methods

# robochart_LessThan class attributes and methods

# robochart_LessOrEqual class attributes and methods

# robochart_Plus class attributes and methods

# robochart_Minus class attributes and methods

# robochart_Modulus class attributes and methods

# robochart_Mult class attributes and methods

# robochart_Div class attributes and methods

# robochart_Cat class attributes and methods

# robochart_TypeExp class attributes and methods

# robochart_Equals class attributes and methods

# robochart_Different class attributes and methods

# robochart_GreaterThan class attributes and methods

# robochart_Selection class attributes and methods

# robochart_IntegerExp class attributes and methods
robochart_IntegerExp_value: Property = Property(name="value", type=IntegerType)
robochart_IntegerExp.attributes={robochart_IntegerExp_value}

# robochart_FloatExp class attributes and methods
robochart_FloatExp_value: Property = Property(name="value", type=FloatType)
robochart_FloatExp.attributes={robochart_FloatExp_value}

# robochart_Neg class attributes and methods

# robochart_BooleanExp class attributes and methods
robochart_BooleanExp_value: Property = Property(name="value", type=StringType)
robochart_BooleanExp.attributes={robochart_BooleanExp_value}

# robochart_VarExp class attributes and methods

# robochart_RefExp class attributes and methods

# robochart_NamedExpression class attributes and methods

# robochart_ToExp class attributes and methods

# robochart_FromExp class attributes and methods

# robochart_StringExp class attributes and methods
robochart_StringExp_value: Property = Property(name="value", type=StringType)
robochart_StringExp.attributes={robochart_StringExp_value}

# robochart_IsExp class attributes and methods

# robochart_EnumExp class attributes and methods

# robochart_IdExp class attributes and methods

# robochart_ParExp class attributes and methods

# robochart_AsExp class attributes and methods

# robochart_SeqExp class attributes and methods

# robochart_SetExp class attributes and methods

# robochart_SetComp class attributes and methods

# robochart_SetRange class attributes and methods

# robochart_TupleExp class attributes and methods

# robochart_RangeExp class attributes and methods
robochart_RangeExp_linterval: Property = Property(name="linterval", type=StringType)
robochart_RangeExp_rinterval: Property = Property(name="rinterval", type=StringType)
robochart_RangeExp.attributes={robochart_RangeExp_linterval, robochart_RangeExp_rinterval}

# robochart_CallExp class attributes and methods

# robochart_ElseExp class attributes and methods

# robochart_VarSelection class attributes and methods

# Assignable class attributes and methods

# robochart_ArrayAssignable class attributes and methods

# robochart_VarRef class attributes and methods

# robochart_WaitingCondition class attributes and methods

# robochart_WaitingConditionRef class attributes and methods

# robochart_VectorType class attributes and methods
robochart_VectorType_size: Property = Property(name="size", type=IntegerType)
robochart_VectorType.attributes={robochart_VectorType_size}

# robochart_MatrixType class attributes and methods
robochart_MatrixType_rows: Property = Property(name="rows", type=IntegerType)
robochart_MatrixType_columns: Property = Property(name="columns", type=IntegerType)
robochart_MatrixType.attributes={robochart_MatrixType_columns, robochart_MatrixType_rows}

# Relationships
interfaces1: BinaryAssociation = BinaryAssociation(
    name="interfaces1",
    ends={
        Property(name="robochart_Interface", type=robochart_RCPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_RCPackage", type=robochart_Interface, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
robots2: BinaryAssociation = BinaryAssociation(
    name="robots2",
    ends={
        Property(name="robochart_RoboticPlatformDef", type=robochart_RCPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_RCPackage3", type=robochart_RoboticPlatformDef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types4: BinaryAssociation = BinaryAssociation(
    name="types4",
    ends={
        Property(name="robochart_TypeDecl", type=robochart_RCPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_RCPackage5", type=robochart_TypeDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imports0: BinaryAssociation = BinaryAssociation(
    name="imports0",
    ends={
        Property(name="robochart_Import", type=robochart_BasicPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_BasicPackage", type=robochart_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modules10: BinaryAssociation = BinaryAssociation(
    name="modules10",
    ends={
        Property(name="robochart_RCPackage11", type=robochart_RCModule, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="robochart_RCModule", type=robochart_RCPackage, multiplicity=Multiplicity(1, 1))
    }
)
operations12: BinaryAssociation = BinaryAssociation(
    name="operations12",
    ends={
        Property(name="robochart_OperationDef", type=robochart_RCPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_RCPackage13", type=robochart_OperationDef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functions14: BinaryAssociation = BinaryAssociation(
    name="functions14",
    ends={
        Property(name="robochart_Function", type=robochart_RCPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_RCPackage15", type=robochart_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
machines6: BinaryAssociation = BinaryAssociation(
    name="machines6",
    ends={
        Property(name="robochart_StateMachineDef", type=robochart_RCPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_RCPackage7", type=robochart_StateMachineDef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
controllers8: BinaryAssociation = BinaryAssociation(
    name="controllers8",
    ends={
        Property(name="robochart_ControllerDef", type=robochart_RCPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_RCPackage9", type=robochart_ControllerDef, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type17: BinaryAssociation = BinaryAssociation(
    name="type17",
    ends={
        Property(name="robochart_Type", type=robochart_TypedNamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_TypedNamedElement", type=robochart_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
literals18: BinaryAssociation = BinaryAssociation(
    name="literals18",
    ends={
        Property(name="robochart_Literal", type=robochart_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_Enumeration", type=robochart_Literal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fields16: BinaryAssociation = BinaryAssociation(
    name="fields16",
    ends={
        Property(name="robochart_Field", type=robochart_RecordType, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_RecordType", type=robochart_Field, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
types24: BinaryAssociation = BinaryAssociation(
    name="types24",
    ends={
        Property(name="robochart_Type25", type=robochart_ProductType, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_ProductType", type=robochart_Type, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
domain26: BinaryAssociation = BinaryAssociation(
    name="domain26",
    ends={
        Property(name="robochart_Type27", type=robochart_RelationType, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_RelationType", type=robochart_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
range28: BinaryAssociation = BinaryAssociation(
    name="range28",
    ends={
        Property(name="robochart_Type30", type=robochart_RelationType, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_RelationType29", type=robochart_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
types19: BinaryAssociation = BinaryAssociation(
    name="types19",
    ends={
        Property(name="robochart_Type21", type=robochart_Literal, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_Literal20", type=robochart_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type22: BinaryAssociation = BinaryAssociation(
    name="type22",
    ends={
        Property(name="robochart_Type23", type=robochart_NameType, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_NameType", type=robochart_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
vars35: BinaryAssociation = BinaryAssociation(
    name="vars35",
    ends={
        Property(name="robochart_Variable", type=robochart_VariableList, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_VariableList", type=robochart_Variable, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
domain31: BinaryAssociation = BinaryAssociation(
    name="domain31",
    ends={
        Property(name="robochart_Type32", type=robochart_SetType, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_SetType", type=robochart_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ref33: BinaryAssociation = BinaryAssociation(
    name="ref33",
    ends={
        Property(name="robochart_TypeDecl34", type=robochart_TypeRef, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_TypeRef", type=robochart_TypeDecl, multiplicity=Multiplicity(1, 1))
    }
)
parameters40: BinaryAssociation = BinaryAssociation(
    name="parameters40",
    ends={
        Property(name="robochart_Parameter", type=robochart_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_Function41", type=robochart_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
preconditions42: BinaryAssociation = BinaryAssociation(
    name="preconditions42",
    ends={
        Property(name="robochart_Expression44", type=robochart_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_Function43", type=robochart_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
postconditions45: BinaryAssociation = BinaryAssociation(
    name="postconditions45",
    ends={
        Property(name="robochart_Expression47", type=robochart_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_Function46", type=robochart_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initial36: BinaryAssociation = BinaryAssociation(
    name="initial36",
    ends={
        Property(name="robochart_Expression", type=robochart_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_Variable37", type=robochart_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type38: BinaryAssociation = BinaryAssociation(
    name="type38",
    ends={
        Property(name="robochart_Type39", type=robochart_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_Event", type=robochart_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
postconditions53: BinaryAssociation = BinaryAssociation(
    name="postconditions53",
    ends={
        Property(name="robochart_Expression55", type=robochart_OperationSig, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_OperationSig54", type=robochart_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref56: BinaryAssociation = BinaryAssociation(
    name="ref56",
    ends={
        Property(name="robochart_OperationDef57", type=robochart_OperationRef, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_OperationRef", type=robochart_OperationDef, multiplicity=Multiplicity(1, 1))
    }
)
parameters48: BinaryAssociation = BinaryAssociation(
    name="parameters48",
    ends={
        Property(name="robochart_Parameter49", type=robochart_OperationSig, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_OperationSig", type=robochart_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
preconditions50: BinaryAssociation = BinaryAssociation(
    name="preconditions50",
    ends={
        Property(name="robochart_Expression52", type=robochart_OperationSig, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_OperationSig51", type=robochart_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
events63: BinaryAssociation = BinaryAssociation(
    name="events63",
    ends={
        Property(name="robochart_Event65", type=robochart_BasicContext, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_BasicContext64", type=robochart_Event, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
clocks66: BinaryAssociation = BinaryAssociation(
    name="clocks66",
    ends={
        Property(name="robochart_Clock", type=robochart_BasicContext, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_BasicContext67", type=robochart_Clock, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pInterfaces68: BinaryAssociation = BinaryAssociation(
    name="pInterfaces68",
    ends={
        Property(name="robochart_Interface69", type=robochart_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_Context", type=robochart_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
variableList58: BinaryAssociation = BinaryAssociation(
    name="variableList58",
    ends={
        Property(name="robochart_VariableList59", type=robochart_BasicContext, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_BasicContext", type=robochart_VariableList, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operations60: BinaryAssociation = BinaryAssociation(
    name="operations60",
    ends={
        Property(name="robochart_OperationSig62", type=robochart_BasicContext, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_BasicContext61", type=robochart_OperationSig, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref76: BinaryAssociation = BinaryAssociation(
    name="ref76",
    ends={
        Property(name="robochart_RoboticPlatformDef77", type=robochart_RoboticPlatformRef, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_RoboticPlatformRef", type=robochart_RoboticPlatformDef, multiplicity=Multiplicity(1, 1))
    }
)
ref78: BinaryAssociation = BinaryAssociation(
    name="ref78",
    ends={
        Property(name="robochart_StateMachineDef79", type=robochart_StateMachineRef, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_StateMachineRef", type=robochart_StateMachineDef, multiplicity=Multiplicity(1, 1))
    }
)
rInterfaces70: BinaryAssociation = BinaryAssociation(
    name="rInterfaces70",
    ends={
        Property(name="robochart_Interface72", type=robochart_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_Context71", type=robochart_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
interfaces73: BinaryAssociation = BinaryAssociation(
    name="interfaces73",
    ends={
        Property(name="robochart_Interface75", type=robochart_Context, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_Context74", type=robochart_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
actions83: BinaryAssociation = BinaryAssociation(
    name="actions83",
    ends={
        Property(name="robochart_Action", type=robochart_State, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_State", type=robochart_Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source84: BinaryAssociation = BinaryAssociation(
    name="source84",
    ends={
        Property(name="robochart_Node86", type=robochart_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_Transition85", type=robochart_Node, multiplicity=Multiplicity(1, 1))
    }
)
nodes80: BinaryAssociation = BinaryAssociation(
    name="nodes80",
    ends={
        Property(name="robochart_Node", type=robochart_NodeContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_NodeContainer", type=robochart_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions81: BinaryAssociation = BinaryAssociation(
    name="transitions81",
    ends={
        Property(name="robochart_Transition", type=robochart_NodeContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_NodeContainer82", type=robochart_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
action101: BinaryAssociation = BinaryAssociation(
    name="action101",
    ends={
        Property(name="robochart_Statement", type=robochart_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_Transition102", type=robochart_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
probability103: BinaryAssociation = BinaryAssociation(
    name="probability103",
    ends={
        Property(name="robochart_Expression105", type=robochart_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_Transition104", type=robochart_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
event106: BinaryAssociation = BinaryAssociation(
    name="event106",
    ends={
        Property(name="robochart_Event108", type=robochart_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_Trigger107", type=robochart_Event, multiplicity=Multiplicity(0, 1))
    }
)
_from109: BinaryAssociation = BinaryAssociation(
    name="_from109",
    ends={
        Property(name="robochart_Variable111", type=robochart_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_Trigger110", type=robochart_Variable, multiplicity=Multiplicity(0, 1))
    }
)
_predicate112: BinaryAssociation = BinaryAssociation(
    name="_predicate112",
    ends={
        Property(name="robochart_Expression114", type=robochart_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_Trigger113", type=robochart_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter115: BinaryAssociation = BinaryAssociation(
    name="parameter115",
    ends={
        Property(name="robochart_Variable117", type=robochart_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_Trigger116", type=robochart_Variable, multiplicity=Multiplicity(0, 1))
    }
)
target87: BinaryAssociation = BinaryAssociation(
    name="target87",
    ends={
        Property(name="robochart_Node89", type=robochart_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_Transition88", type=robochart_Node, multiplicity=Multiplicity(1, 1))
    }
)
start90: BinaryAssociation = BinaryAssociation(
    name="start90",
    ends={
        Property(name="robochart_Expression92", type=robochart_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_Transition91", type=robochart_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
trigger93: BinaryAssociation = BinaryAssociation(
    name="trigger93",
    ends={
        Property(name="robochart_Trigger", type=robochart_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_Transition94", type=robochart_Trigger, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
end95: BinaryAssociation = BinaryAssociation(
    name="end95",
    ends={
        Property(name="robochart_Expression97", type=robochart_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_Transition96", type=robochart_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition98: BinaryAssociation = BinaryAssociation(
    name="condition98",
    ends={
        Property(name="robochart_Expression100", type=robochart_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_Transition99", type=robochart_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
action126: BinaryAssociation = BinaryAssociation(
    name="action126",
    ends={
        Property(name="robochart_Statement128", type=robochart_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_Action127", type=robochart_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value118: BinaryAssociation = BinaryAssociation(
    name="value118",
    ends={
        Property(name="robochart_Expression120", type=robochart_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_Trigger119", type=robochart_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
time121: BinaryAssociation = BinaryAssociation(
    name="time121",
    ends={
        Property(name="robochart_Variable123", type=robochart_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_Trigger122", type=robochart_Variable, multiplicity=Multiplicity(0, 1))
    }
)
reset124: BinaryAssociation = BinaryAssociation(
    name="reset124",
    ends={
        Property(name="robochart_ClockReset", type=robochart_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_Trigger125", type=robochart_ClockReset, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connections133: BinaryAssociation = BinaryAssociation(
    name="connections133",
    ends={
        Property(name="robochart_Connection", type=robochart_ControllerDef, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_ControllerDef134", type=robochart_Connection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from135: BinaryAssociation = BinaryAssociation(
    name="from135",
    ends={
        Property(name="robochart_ConnectionNode", type=robochart_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_Connection136", type=robochart_ConnectionNode, multiplicity=Multiplicity(1, 1))
    }
)
to137: BinaryAssociation = BinaryAssociation(
    name="to137",
    ends={
        Property(name="robochart_ConnectionNode139", type=robochart_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_Connection138", type=robochart_ConnectionNode, multiplicity=Multiplicity(1, 1))
    }
)
efrom140: BinaryAssociation = BinaryAssociation(
    name="efrom140",
    ends={
        Property(name="robochart_Event142", type=robochart_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_Connection141", type=robochart_Event, multiplicity=Multiplicity(1, 1))
    }
)
eto143: BinaryAssociation = BinaryAssociation(
    name="eto143",
    ends={
        Property(name="robochart_Event145", type=robochart_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_Connection144", type=robochart_Event, multiplicity=Multiplicity(1, 1))
    }
)
machines129: BinaryAssociation = BinaryAssociation(
    name="machines129",
    ends={
        Property(name="robochart_StateMachine", type=robochart_ControllerDef, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_ControllerDef130", type=robochart_StateMachine, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lOperations131: BinaryAssociation = BinaryAssociation(
    name="lOperations131",
    ends={
        Property(name="robochart_Operation", type=robochart_ControllerDef, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_ControllerDef132", type=robochart_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodes151: BinaryAssociation = BinaryAssociation(
    name="nodes151",
    ends={
        Property(name="robochart_ConnectionNode153", type=robochart_RCModule, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_RCModule152", type=robochart_ConnectionNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ref146: BinaryAssociation = BinaryAssociation(
    name="ref146",
    ends={
        Property(name="robochart_ControllerDef147", type=robochart_ControllerRef, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_ControllerRef", type=robochart_ControllerDef, multiplicity=Multiplicity(1, 1))
    }
)
connections148: BinaryAssociation = BinaryAssociation(
    name="connections148",
    ends={
        Property(name="robochart_Connection150", type=robochart_RCModule, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_RCModule149", type=robochart_Connection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
duration162: BinaryAssociation = BinaryAssociation(
    name="duration162",
    ends={
        Property(name="robochart_Expression163", type=robochart_Wait, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_Wait", type=robochart_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression164: BinaryAssociation = BinaryAssociation(
    name="expression164",
    ends={
        Property(name="robochart_Expression165", type=robochart_IfStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_IfStmt", type=robochart_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
then166: BinaryAssociation = BinaryAssociation(
    name="then166",
    ends={
        Property(name="robochart_Statement168", type=robochart_IfStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_IfStmt167", type=robochart_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
start154: BinaryAssociation = BinaryAssociation(
    name="start154",
    ends={
        Property(name="robochart_Expression155", type=robochart_TimedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_TimedStatement", type=robochart_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
stmt156: BinaryAssociation = BinaryAssociation(
    name="stmt156",
    ends={
        Property(name="robochart_Statement158", type=robochart_TimedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_TimedStatement157", type=robochart_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
end159: BinaryAssociation = BinaryAssociation(
    name="end159",
    ends={
        Property(name="robochart_Expression161", type=robochart_TimedStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_TimedStatement160", type=robochart_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
args184: BinaryAssociation = BinaryAssociation(
    name="args184",
    ends={
        Property(name="robochart_Expression186", type=robochart_Call, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_Call185", type=robochart_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
clock187: BinaryAssociation = BinaryAssociation(
    name="clock187",
    ends={
        Property(name="robochart_Clock189", type=robochart_ClockReset, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_ClockReset188", type=robochart_Clock, multiplicity=Multiplicity(1, 1))
    }
)
value190: BinaryAssociation = BinaryAssociation(
    name="value190",
    ends={
        Property(name="robochart_Expression191", type=robochart_ArrayExp, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_ArrayExp", type=robochart_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters192: BinaryAssociation = BinaryAssociation(
    name="parameters192",
    ends={
        Property(name="robochart_Expression194", type=robochart_ArrayExp, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_ArrayExp193", type=robochart_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
clock195: BinaryAssociation = BinaryAssociation(
    name="clock195",
    ends={
        Property(name="robochart_Clock196", type=robochart_ClockExp, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_ClockExp", type=robochart_Clock, multiplicity=Multiplicity(1, 1))
    }
)
state197: BinaryAssociation = BinaryAssociation(
    name="state197",
    ends={
        Property(name="robochart_State198", type=robochart_StateClockExp, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_StateClockExp", type=robochart_State, multiplicity=Multiplicity(1, 1))
    }
)
left199: BinaryAssociation = BinaryAssociation(
    name="left199",
    ends={
        Property(name="robochart_Expression200", type=robochart_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_BinaryExpression", type=robochart_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
else169: BinaryAssociation = BinaryAssociation(
    name="else169",
    ends={
        Property(name="robochart_Statement171", type=robochart_IfStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_IfStmt170", type=robochart_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left172: BinaryAssociation = BinaryAssociation(
    name="left172",
    ends={
        Property(name="robochart_Assignable", type=robochart_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_Assignment", type=robochart_Assignable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right173: BinaryAssociation = BinaryAssociation(
    name="right173",
    ends={
        Property(name="robochart_Expression175", type=robochart_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_Assignment174", type=robochart_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
trigger176: BinaryAssociation = BinaryAssociation(
    name="trigger176",
    ends={
        Property(name="robochart_Trigger177", type=robochart_SendEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_SendEvent", type=robochart_Trigger, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements178: BinaryAssociation = BinaryAssociation(
    name="statements178",
    ends={
        Property(name="robochart_Statement179", type=robochart_SeqStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_SeqStatement", type=robochart_Statement, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
stmt180: BinaryAssociation = BinaryAssociation(
    name="stmt180",
    ends={
        Property(name="robochart_Statement181", type=robochart_ParStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_ParStmt", type=robochart_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operation182: BinaryAssociation = BinaryAssociation(
    name="operation182",
    ends={
        Property(name="robochart_OperationSig183", type=robochart_Call, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_Call", type=robochart_OperationSig, multiplicity=Multiplicity(1, 1))
    }
)
suchthat214: BinaryAssociation = BinaryAssociation(
    name="suchthat214",
    ends={
        Property(name="robochart_Expression216", type=robochart_LambdaExp, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_LambdaExp215", type=robochart_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression217: BinaryAssociation = BinaryAssociation(
    name="expression217",
    ends={
        Property(name="robochart_Expression219", type=robochart_LambdaExp, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_LambdaExp218", type=robochart_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition220: BinaryAssociation = BinaryAssociation(
    name="condition220",
    ends={
        Property(name="robochart_Expression221", type=robochart_IfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_IfExpression", type=robochart_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ifexp222: BinaryAssociation = BinaryAssociation(
    name="ifexp222",
    ends={
        Property(name="robochart_Expression224", type=robochart_IfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_IfExpression223", type=robochart_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseexp225: BinaryAssociation = BinaryAssociation(
    name="elseexp225",
    ends={
        Property(name="robochart_Expression227", type=robochart_IfExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_IfExpression226", type=robochart_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value228: BinaryAssociation = BinaryAssociation(
    name="value228",
    ends={
        Property(name="robochart_Expression229", type=robochart_Declaration, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_Declaration", type=robochart_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right201: BinaryAssociation = BinaryAssociation(
    name="right201",
    ends={
        Property(name="robochart_Expression203", type=robochart_BinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_BinaryExpression202", type=robochart_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variables204: BinaryAssociation = BinaryAssociation(
    name="variables204",
    ends={
        Property(name="robochart_Variable205", type=robochart_QuantifierExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_QuantifierExpression", type=robochart_Variable, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
suchthat206: BinaryAssociation = BinaryAssociation(
    name="suchthat206",
    ends={
        Property(name="robochart_Expression208", type=robochart_QuantifierExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_QuantifierExpression207", type=robochart_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
predicate209: BinaryAssociation = BinaryAssociation(
    name="predicate209",
    ends={
        Property(name="robochart_Expression211", type=robochart_QuantifierExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_QuantifierExpression210", type=robochart_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variables212: BinaryAssociation = BinaryAssociation(
    name="variables212",
    ends={
        Property(name="robochart_Variable213", type=robochart_LambdaExp, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_LambdaExp", type=robochart_Variable, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
expression232: BinaryAssociation = BinaryAssociation(
    name="expression232",
    ends={
        Property(name="robochart_Expression234", type=robochart_LetExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_LetExpression233", type=robochart_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exp235: BinaryAssociation = BinaryAssociation(
    name="exp235",
    ends={
        Property(name="robochart_Expression236", type=robochart_Not, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_Not", type=robochart_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
member237: BinaryAssociation = BinaryAssociation(
    name="member237",
    ends={
        Property(name="robochart_Expression238", type=robochart_InExp, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_InExp", type=robochart_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
set239: BinaryAssociation = BinaryAssociation(
    name="set239",
    ends={
        Property(name="robochart_Expression241", type=robochart_InExp, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_InExp240", type=robochart_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
declarations230: BinaryAssociation = BinaryAssociation(
    name="declarations230",
    ends={
        Property(name="robochart_Declaration231", type=robochart_LetExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_LetExpression", type=robochart_Declaration, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
type242: BinaryAssociation = BinaryAssociation(
    name="type242",
    ends={
        Property(name="robochart_Type243", type=robochart_TypeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_TypeExp", type=robochart_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
receiver246: BinaryAssociation = BinaryAssociation(
    name="receiver246",
    ends={
        Property(name="robochart_Expression247", type=robochart_Selection, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_Selection", type=robochart_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
member248: BinaryAssociation = BinaryAssociation(
    name="member248",
    ends={
        Property(name="robochart_Member", type=robochart_Selection, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_Selection249", type=robochart_Member, multiplicity=Multiplicity(1, 1))
    }
)
exp244: BinaryAssociation = BinaryAssociation(
    name="exp244",
    ends={
        Property(name="robochart_Expression245", type=robochart_Neg, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_Neg", type=robochart_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value250: BinaryAssociation = BinaryAssociation(
    name="value250",
    ends={
        Property(name="robochart_Variable251", type=robochart_VarExp, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_VarExp", type=robochart_Variable, multiplicity=Multiplicity(1, 1))
    }
)
ref252: BinaryAssociation = BinaryAssociation(
    name="ref252",
    ends={
        Property(name="robochart_NamedExpression", type=robochart_RefExp, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_RefExp", type=robochart_NamedExpression, multiplicity=Multiplicity(1, 1))
    }
)
exp253: BinaryAssociation = BinaryAssociation(
    name="exp253",
    ends={
        Property(name="robochart_AsExp", type=robochart_Expression, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="robochart_Expression254", type=robochart_AsExp, multiplicity=Multiplicity(1, 1))
    }
)
type255: BinaryAssociation = BinaryAssociation(
    name="type255",
    ends={
        Property(name="robochart_Type257", type=robochart_AsExp, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_AsExp256", type=robochart_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exp258: BinaryAssociation = BinaryAssociation(
    name="exp258",
    ends={
        Property(name="robochart_Expression259", type=robochart_IsExp, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_IsExp", type=robochart_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type260: BinaryAssociation = BinaryAssociation(
    name="type260",
    ends={
        Property(name="robochart_Type262", type=robochart_IsExp, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_IsExp261", type=robochart_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
type263: BinaryAssociation = BinaryAssociation(
    name="type263",
    ends={
        Property(name="robochart_Enumeration264", type=robochart_EnumExp, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_EnumExp", type=robochart_Enumeration, multiplicity=Multiplicity(1, 1))
    }
)
literal265: BinaryAssociation = BinaryAssociation(
    name="literal265",
    ends={
        Property(name="robochart_Literal267", type=robochart_EnumExp, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_EnumExp266", type=robochart_Literal, multiplicity=Multiplicity(1, 1))
    }
)
values270: BinaryAssociation = BinaryAssociation(
    name="values270",
    ends={
        Property(name="robochart_Expression271", type=robochart_SeqExp, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_SeqExp", type=robochart_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
values272: BinaryAssociation = BinaryAssociation(
    name="values272",
    ends={
        Property(name="robochart_Expression273", type=robochart_SetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_SetExp", type=robochart_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variables274: BinaryAssociation = BinaryAssociation(
    name="variables274",
    ends={
        Property(name="robochart_Variable275", type=robochart_SetComp, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_SetComp", type=robochart_Variable, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
predicate276: BinaryAssociation = BinaryAssociation(
    name="predicate276",
    ends={
        Property(name="robochart_Expression278", type=robochart_SetComp, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_SetComp277", type=robochart_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exp268: BinaryAssociation = BinaryAssociation(
    name="exp268",
    ends={
        Property(name="robochart_Expression269", type=robochart_ParExp, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_ParExp", type=robochart_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
start282: BinaryAssociation = BinaryAssociation(
    name="start282",
    ends={
        Property(name="robochart_Expression283", type=robochart_SetRange, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_SetRange", type=robochart_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
end284: BinaryAssociation = BinaryAssociation(
    name="end284",
    ends={
        Property(name="robochart_Expression286", type=robochart_SetRange, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_SetRange285", type=robochart_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
values287: BinaryAssociation = BinaryAssociation(
    name="values287",
    ends={
        Property(name="robochart_Expression288", type=robochart_TupleExp, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_TupleExp", type=robochart_Expression, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
lrange289: BinaryAssociation = BinaryAssociation(
    name="lrange289",
    ends={
        Property(name="robochart_Expression290", type=robochart_RangeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_RangeExp", type=robochart_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression279: BinaryAssociation = BinaryAssociation(
    name="expression279",
    ends={
        Property(name="robochart_Expression281", type=robochart_SetComp, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_SetComp280", type=robochart_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rrange291: BinaryAssociation = BinaryAssociation(
    name="rrange291",
    ends={
        Property(name="robochart_RangeExp292", type=robochart_Expression, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="robochart_Expression293", type=robochart_RangeExp, multiplicity=Multiplicity(1, 1))
    }
)
function294: BinaryAssociation = BinaryAssociation(
    name="function294",
    ends={
        Property(name="robochart_Expression295", type=robochart_CallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_CallExp", type=robochart_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
args296: BinaryAssociation = BinaryAssociation(
    name="args296",
    ends={
        Property(name="robochart_Expression298", type=robochart_CallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_CallExp297", type=robochart_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
receiver299: BinaryAssociation = BinaryAssociation(
    name="receiver299",
    ends={
        Property(name="robochart_Assignable300", type=robochart_VarSelection, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_VarSelection", type=robochart_Assignable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
member301: BinaryAssociation = BinaryAssociation(
    name="member301",
    ends={
        Property(name="robochart_Member303", type=robochart_VarSelection, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_VarSelection302", type=robochart_Member, multiplicity=Multiplicity(1, 1))
    }
)
value304: BinaryAssociation = BinaryAssociation(
    name="value304",
    ends={
        Property(name="robochart_Assignable305", type=robochart_ArrayAssignable, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_ArrayAssignable", type=robochart_Assignable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameters306: BinaryAssociation = BinaryAssociation(
    name="parameters306",
    ends={
        Property(name="robochart_Expression308", type=robochart_ArrayAssignable, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_ArrayAssignable307", type=robochart_Expression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
name309: BinaryAssociation = BinaryAssociation(
    name="name309",
    ends={
        Property(name="robochart_Variable310", type=robochart_VarRef, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_VarRef", type=robochart_Variable, multiplicity=Multiplicity(1, 1))
    }
)
expression311: BinaryAssociation = BinaryAssociation(
    name="expression311",
    ends={
        Property(name="robochart_Expression312", type=robochart_WaitingCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_WaitingCondition", type=robochart_Expression, multiplicity=Multiplicity(0, 1))
    }
)
transitions313: BinaryAssociation = BinaryAssociation(
    name="transitions313",
    ends={
        Property(name="robochart_Transition315", type=robochart_WaitingCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_WaitingCondition314", type=robochart_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
base318: BinaryAssociation = BinaryAssociation(
    name="base318",
    ends={
        Property(name="robochart_Type319", type=robochart_VectorType, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_VectorType", type=robochart_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
base320: BinaryAssociation = BinaryAssociation(
    name="base320",
    ends={
        Property(name="robochart_Type321", type=robochart_MatrixType, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_MatrixType", type=robochart_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ref316: BinaryAssociation = BinaryAssociation(
    name="ref316",
    ends={
        Property(name="robochart_WaitingCondition317", type=robochart_WaitingConditionRef, multiplicity=Multiplicity(1, 1)),
        Property(name="robochart_WaitingConditionRef", type=robochart_WaitingCondition, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_robochart_RCPackage_BasicPackage = Generalization(general=BasicPackage, specific=robochart_RCPackage)
gen_robochart_Field_Member = Generalization(general=Member, specific=robochart_Field)
gen_robochart_Field_NamedExpression = Generalization(general=NamedExpression, specific=robochart_Field)
gen_robochart_TypedNamedElement_NamedElement = Generalization(general=NamedElement, specific=robochart_TypedNamedElement)
gen_robochart_Member_TypedNamedElement = Generalization(general=TypedNamedElement, specific=robochart_Member)
gen_robochart_Enumeration_TypeDecl = Generalization(general=TypeDecl, specific=robochart_Enumeration)
gen_robochart_TypeDecl_NamedElement = Generalization(general=NamedElement, specific=robochart_TypeDecl)
gen_robochart_PrimitiveType_TypeDecl = Generalization(general=TypeDecl, specific=robochart_PrimitiveType)
gen_robochart_RecordType_TypeDecl = Generalization(general=TypeDecl, specific=robochart_RecordType)
gen_robochart_ProductType_Type = Generalization(general=Type, specific=robochart_ProductType)
gen_robochart_RelationType_Type = Generalization(general=Type, specific=robochart_RelationType)
gen_robochart_Literal_TypeDecl = Generalization(general=TypeDecl, specific=robochart_Literal)
gen_robochart_Literal_NamedExpression = Generalization(general=NamedExpression, specific=robochart_Literal)
gen_robochart_NameType_TypeDecl = Generalization(general=TypeDecl, specific=robochart_NameType)
gen_robochart_Variable_TypedNamedElement = Generalization(general=TypedNamedElement, specific=robochart_Variable)
gen_robochart_Variable_NamedExpression = Generalization(general=NamedExpression, specific=robochart_Variable)
gen_robochart_Variable_Member = Generalization(general=Member, specific=robochart_Variable)
gen_robochart_FunctionType_RelationType = Generalization(general=RelationType, specific=robochart_FunctionType)
gen_robochart_SetType_Type = Generalization(general=Type, specific=robochart_SetType)
gen_robochart_SeqType_SetType = Generalization(general=SetType, specific=robochart_SeqType)
gen_robochart_TypeRef_Type = Generalization(general=Type, specific=robochart_TypeRef)
gen_robochart_AnyType_Type = Generalization(general=Type, specific=robochart_AnyType)
gen_robochart_Parameter_Variable = Generalization(general=Variable, specific=robochart_Parameter)
gen_robochart_OperationSig_NamedElement = Generalization(general=NamedElement, specific=robochart_OperationSig)
gen_robochart_Event_NamedElement = Generalization(general=NamedElement, specific=robochart_Event)
gen_robochart_Function_TypedNamedElement = Generalization(general=TypedNamedElement, specific=robochart_Function)
gen_robochart_Function_NamedExpression = Generalization(general=NamedExpression, specific=robochart_Function)
gen_robochart_Operation_NamedElement = Generalization(general=NamedElement, specific=robochart_Operation)
gen_robochart_Operation_ConnectionNode = Generalization(general=ConnectionNode, specific=robochart_Operation)
gen_robochart_OperationDef_Operation = Generalization(general=Operation, specific=robochart_OperationDef)
gen_robochart_OperationDef_OperationSig = Generalization(general=OperationSig, specific=robochart_OperationDef)
gen_robochart_OperationDef_StateMachineBody = Generalization(general=StateMachineBody, specific=robochart_OperationDef)
gen_robochart_OperationRef_Operation = Generalization(general=Operation, specific=robochart_OperationRef)
gen_robochart_OperationRef_Reference = Generalization(general=Reference, specific=robochart_OperationRef)
gen_robochart_RoboticPlatform_NamedElement = Generalization(general=NamedElement, specific=robochart_RoboticPlatform)
gen_robochart_RoboticPlatform_ConnectionNode = Generalization(general=ConnectionNode, specific=robochart_RoboticPlatform)
gen_robochart_RoboticPlatformDef_Context = Generalization(general=Context, specific=robochart_RoboticPlatformDef)
gen_robochart_RoboticPlatformDef_RoboticPlatform = Generalization(general=RoboticPlatform, specific=robochart_RoboticPlatformDef)
gen_robochart_Context_BasicContext = Generalization(general=BasicContext, specific=robochart_Context)
gen_robochart_Interface_NamedElement = Generalization(general=NamedElement, specific=robochart_Interface)
gen_robochart_Interface_BasicContext = Generalization(general=BasicContext, specific=robochart_Interface)
gen_robochart_StateMachine_NamedElement = Generalization(general=NamedElement, specific=robochart_StateMachine)
gen_robochart_StateMachine_ConnectionNode = Generalization(general=ConnectionNode, specific=robochart_StateMachine)
gen_robochart_StateMachineDef_StateMachineBody = Generalization(general=StateMachineBody, specific=robochart_StateMachineDef)
gen_robochart_StateMachineDef_StateMachine = Generalization(general=StateMachine, specific=robochart_StateMachineDef)
gen_robochart_StateMachineRef_StateMachine = Generalization(general=StateMachine, specific=robochart_StateMachineRef)
gen_robochart_StateMachineRef_Reference = Generalization(general=Reference, specific=robochart_StateMachineRef)
gen_robochart_StateMachineBody_Context = Generalization(general=Context, specific=robochart_StateMachineBody)
gen_robochart_StateMachineBody_NodeContainer = Generalization(general=NodeContainer, specific=robochart_StateMachineBody)
gen_robochart_Clock_NamedElement = Generalization(general=NamedElement, specific=robochart_Clock)
gen_robochart_RoboticPlatformRef_RoboticPlatform = Generalization(general=RoboticPlatform, specific=robochart_RoboticPlatformRef)
gen_robochart_RoboticPlatformRef_Reference = Generalization(general=Reference, specific=robochart_RoboticPlatformRef)
gen_robochart_Initial_Junction = Generalization(general=Junction, specific=robochart_Initial)
gen_robochart_State_Node = Generalization(general=Node, specific=robochart_State)
gen_robochart_State_NodeContainer = Generalization(general=NodeContainer, specific=robochart_State)
gen_robochart_Final_State = Generalization(general=State, specific=robochart_Final)
gen_robochart_ProbabilisticJunction_Junction = Generalization(general=Junction, specific=robochart_ProbabilisticJunction)
gen_robochart_Transition_NamedElement = Generalization(general=NamedElement, specific=robochart_Transition)
gen_robochart_Node_NamedElement = Generalization(general=NamedElement, specific=robochart_Node)
gen_robochart_Junction_Node = Generalization(general=Node, specific=robochart_Junction)
gen_robochart_EntryAction_Action = Generalization(general=Action, specific=robochart_EntryAction)
gen_robochart_DuringAction_Action = Generalization(general=Action, specific=robochart_DuringAction)
gen_robochart_ExitAction_Action = Generalization(general=Action, specific=robochart_ExitAction)
gen_robochart_Controller_NamedElement = Generalization(general=NamedElement, specific=robochart_Controller)
gen_robochart_Controller_ConnectionNode = Generalization(general=ConnectionNode, specific=robochart_Controller)
gen_robochart_ControllerDef_Context = Generalization(general=Context, specific=robochart_ControllerDef)
gen_robochart_ControllerDef_Controller = Generalization(general=Controller, specific=robochart_ControllerDef)
gen_robochart_TimedStatement_Statement = Generalization(general=Statement, specific=robochart_TimedStatement)
gen_robochart_ControllerRef_Controller = Generalization(general=Controller, specific=robochart_ControllerRef)
gen_robochart_RCModule_NamedElement = Generalization(general=NamedElement, specific=robochart_RCModule)
gen_robochart_Wait_Statement = Generalization(general=Statement, specific=robochart_Wait)
gen_robochart_Skip_Statement = Generalization(general=Statement, specific=robochart_Skip)
gen_robochart_IfStmt_Statement = Generalization(general=Statement, specific=robochart_IfStmt)
gen_robochart_ClockReset_Statement = Generalization(general=Statement, specific=robochart_ClockReset)
gen_robochart_ResultExp_Expression = Generalization(general=Expression, specific=robochart_ResultExp)
gen_robochart_ArrayExp_Expression = Generalization(general=Expression, specific=robochart_ArrayExp)
gen_robochart_ClockExp_Expression = Generalization(general=Expression, specific=robochart_ClockExp)
gen_robochart_StateClockExp_Expression = Generalization(general=Expression, specific=robochart_StateClockExp)
gen_robochart_BinaryExpression_Expression = Generalization(general=Expression, specific=robochart_BinaryExpression)
gen_robochart_Assignment_Statement = Generalization(general=Statement, specific=robochart_Assignment)
gen_robochart_SendEvent_Statement = Generalization(general=Statement, specific=robochart_SendEvent)
gen_robochart_SeqStatement_Statement = Generalization(general=Statement, specific=robochart_SeqStatement)
gen_robochart_ParStmt_Statement = Generalization(general=Statement, specific=robochart_ParStmt)
gen_robochart_Call_Statement = Generalization(general=Statement, specific=robochart_Call)
gen_robochart_DefiniteDescription_LambdaExp = Generalization(general=LambdaExp, specific=robochart_DefiniteDescription)
gen_robochart_IfExpression_Expression = Generalization(general=Expression, specific=robochart_IfExpression)
gen_robochart_Declaration_NamedElement = Generalization(general=NamedElement, specific=robochart_Declaration)
gen_robochart_Declaration_NamedExpression = Generalization(general=NamedExpression, specific=robochart_Declaration)
gen_robochart_LetExpression_Expression = Generalization(general=Expression, specific=robochart_LetExpression)
gen_robochart_Iff_BinaryExpression = Generalization(general=BinaryExpression, specific=robochart_Iff)
gen_robochart_Implies_BinaryExpression = Generalization(general=BinaryExpression, specific=robochart_Implies)
gen_robochart_Or_BinaryExpression = Generalization(general=BinaryExpression, specific=robochart_Or)
gen_robochart_QuantifierExpression_Expression = Generalization(general=Expression, specific=robochart_QuantifierExpression)
gen_robochart_Forall_QuantifierExpression = Generalization(general=QuantifierExpression, specific=robochart_Forall)
gen_robochart_Exists_QuantifierExpression = Generalization(general=QuantifierExpression, specific=robochart_Exists)
gen_robochart_LambdaExp_Expression = Generalization(general=Expression, specific=robochart_LambdaExp)
gen_robochart_And_BinaryExpression = Generalization(general=BinaryExpression, specific=robochart_And)
gen_robochart_Not_Expression = Generalization(general=Expression, specific=robochart_Not)
gen_robochart_InExp_Expression = Generalization(general=Expression, specific=robochart_InExp)
gen_robochart_GreaterOrEqual_BinaryExpression = Generalization(general=BinaryExpression, specific=robochart_GreaterOrEqual)
gen_robochart_LessThan_BinaryExpression = Generalization(general=BinaryExpression, specific=robochart_LessThan)
gen_robochart_LessOrEqual_BinaryExpression = Generalization(general=BinaryExpression, specific=robochart_LessOrEqual)
gen_robochart_Plus_BinaryExpression = Generalization(general=BinaryExpression, specific=robochart_Plus)
gen_robochart_Minus_BinaryExpression = Generalization(general=BinaryExpression, specific=robochart_Minus)
gen_robochart_Modulus_BinaryExpression = Generalization(general=BinaryExpression, specific=robochart_Modulus)
gen_robochart_Mult_BinaryExpression = Generalization(general=BinaryExpression, specific=robochart_Mult)
gen_robochart_Div_BinaryExpression = Generalization(general=BinaryExpression, specific=robochart_Div)
gen_robochart_Cat_BinaryExpression = Generalization(general=BinaryExpression, specific=robochart_Cat)
gen_robochart_TypeExp_Expression = Generalization(general=Expression, specific=robochart_TypeExp)
gen_robochart_Equals_BinaryExpression = Generalization(general=BinaryExpression, specific=robochart_Equals)
gen_robochart_Different_BinaryExpression = Generalization(general=BinaryExpression, specific=robochart_Different)
gen_robochart_GreaterThan_BinaryExpression = Generalization(general=BinaryExpression, specific=robochart_GreaterThan)
gen_robochart_Selection_Expression = Generalization(general=Expression, specific=robochart_Selection)
gen_robochart_IntegerExp_Expression = Generalization(general=Expression, specific=robochart_IntegerExp)
gen_robochart_FloatExp_Expression = Generalization(general=Expression, specific=robochart_FloatExp)
gen_robochart_Neg_Expression = Generalization(general=Expression, specific=robochart_Neg)
gen_robochart_BooleanExp_Expression = Generalization(general=Expression, specific=robochart_BooleanExp)
gen_robochart_VarExp_Expression = Generalization(general=Expression, specific=robochart_VarExp)
gen_robochart_RefExp_Expression = Generalization(general=Expression, specific=robochart_RefExp)
gen_robochart_ToExp_Expression = Generalization(general=Expression, specific=robochart_ToExp)
gen_robochart_FromExp_Expression = Generalization(general=Expression, specific=robochart_FromExp)
gen_robochart_StringExp_Expression = Generalization(general=Expression, specific=robochart_StringExp)
gen_robochart_IsExp_Expression = Generalization(general=Expression, specific=robochart_IsExp)
gen_robochart_EnumExp_Expression = Generalization(general=Expression, specific=robochart_EnumExp)
gen_robochart_IdExp_Expression = Generalization(general=Expression, specific=robochart_IdExp)
gen_robochart_ParExp_Expression = Generalization(general=Expression, specific=robochart_ParExp)
gen_robochart_AsExp_Expression = Generalization(general=Expression, specific=robochart_AsExp)
gen_robochart_SeqExp_Expression = Generalization(general=Expression, specific=robochart_SeqExp)
gen_robochart_SetExp_Expression = Generalization(general=Expression, specific=robochart_SetExp)
gen_robochart_SetComp_Expression = Generalization(general=Expression, specific=robochart_SetComp)
gen_robochart_SetRange_Expression = Generalization(general=Expression, specific=robochart_SetRange)
gen_robochart_TupleExp_Expression = Generalization(general=Expression, specific=robochart_TupleExp)
gen_robochart_RangeExp_Expression = Generalization(general=Expression, specific=robochart_RangeExp)
gen_robochart_CallExp_Expression = Generalization(general=Expression, specific=robochart_CallExp)
gen_robochart_ElseExp_Expression = Generalization(general=Expression, specific=robochart_ElseExp)
gen_robochart_VarSelection_Assignable = Generalization(general=Assignable, specific=robochart_VarSelection)
gen_robochart_ArrayAssignable_Assignable = Generalization(general=Assignable, specific=robochart_ArrayAssignable)
gen_robochart_VarRef_Assignable = Generalization(general=Assignable, specific=robochart_VarRef)
gen_robochart_WaitingCondition_NamedElement = Generalization(general=NamedElement, specific=robochart_WaitingCondition)
gen_robochart_WaitingConditionRef_Expression = Generalization(general=Expression, specific=robochart_WaitingConditionRef)
gen_robochart_VectorType_Type = Generalization(general=Type, specific=robochart_VectorType)
gen_robochart_MatrixType_Type = Generalization(general=Type, specific=robochart_MatrixType)

# Domain Model
domain_model = DomainModel(
    name="robochart",
    types={robochart_RCPackage, BasicPackage, robochart_Interface, robochart_RoboticPlatformDef, robochart_TypeDecl, robochart_BasicPackage, robochart_Import, robochart_OperationDef, robochart_Function, robochart_NamedElement, robochart_StateMachineDef, robochart_ControllerDef, robochart_RCModule, Member, NamedExpression, robochart_TypedNamedElement, robochart_Type, robochart_Member, TypedNamedElement, robochart_Enumeration, robochart_Literal, NamedElement, robochart_PrimitiveType, TypeDecl, robochart_RecordType, robochart_Field, robochart_ProductType, Type, robochart_RelationType, robochart_NameType, robochart_VariableList, robochart_Variable, robochart_Expression, robochart_FunctionType, RelationType, robochart_SetType, robochart_SeqType, SetType, robochart_TypeRef, robochart_AnyType, robochart_Parameter, Variable, robochart_OperationSig, robochart_Event, robochart_Operation, ConnectionNode, Operation, OperationSig, StateMachineBody, robochart_Reference, robochart_OperationRef, Reference, robochart_Clock, robochart_RoboticPlatform, Context, RoboticPlatform, robochart_Context, BasicContext, robochart_BasicContext, robochart_StateMachine, StateMachine, robochart_StateMachineRef, robochart_StateMachineBody, NodeContainer, robochart_RoboticPlatformRef, robochart_Initial, Junction, robochart_State, robochart_Action, robochart_Final, State, robochart_ProbabilisticJunction, robochart_NodeContainer, robochart_Node, robochart_Transition, robochart_Junction, Node, robochart_Statement, robochart_Trigger, robochart_EntryAction, Action, robochart_DuringAction, robochart_ExitAction, robochart_Controller, robochart_ClockReset, robochart_ConnectionNode, Controller, robochart_Connection, robochart_TimedStatement, Statement, robochart_ControllerRef, robochart_Wait, robochart_Skip, robochart_IfStmt, robochart_ResultExp, Expression, robochart_ArrayExp, robochart_ClockExp, robochart_StateClockExp, robochart_BinaryExpression, robochart_Assignment, robochart_Assignable, robochart_SendEvent, robochart_SeqStatement, robochart_ParStmt, robochart_Call, robochart_DefiniteDescription, LambdaExp, robochart_IfExpression, robochart_Declaration, robochart_LetExpression, robochart_Iff, BinaryExpression, robochart_Implies, robochart_Or, robochart_QuantifierExpression, robochart_Forall, QuantifierExpression, robochart_Exists, robochart_LambdaExp, robochart_And, robochart_Not, robochart_InExp, robochart_GreaterOrEqual, robochart_LessThan, robochart_LessOrEqual, robochart_Plus, robochart_Minus, robochart_Modulus, robochart_Mult, robochart_Div, robochart_Cat, robochart_TypeExp, robochart_Equals, robochart_Different, robochart_GreaterThan, robochart_Selection, robochart_IntegerExp, robochart_FloatExp, robochart_Neg, robochart_BooleanExp, robochart_VarExp, robochart_RefExp, robochart_NamedExpression, robochart_ToExp, robochart_FromExp, robochart_StringExp, robochart_IsExp, robochart_EnumExp, robochart_IdExp, robochart_ParExp, robochart_AsExp, robochart_SeqExp, robochart_SetExp, robochart_SetComp, robochart_SetRange, robochart_TupleExp, robochart_RangeExp, robochart_CallExp, robochart_ElseExp, robochart_VarSelection, Assignable, robochart_ArrayAssignable, robochart_VarRef, robochart_WaitingCondition, robochart_WaitingConditionRef, robochart_VectorType, robochart_MatrixType, VariableModifier, TriggerType},
    associations={interfaces1, robots2, types4, imports0, modules10, operations12, functions14, machines6, controllers8, type17, literals18, fields16, types24, domain26, range28, types19, type22, vars35, domain31, ref33, parameters40, preconditions42, postconditions45, initial36, type38, postconditions53, ref56, parameters48, preconditions50, events63, clocks66, pInterfaces68, variableList58, operations60, ref76, ref78, rInterfaces70, interfaces73, actions83, source84, nodes80, transitions81, action101, probability103, event106, _from109, _predicate112, parameter115, target87, start90, trigger93, end95, condition98, action126, value118, time121, reset124, connections133, from135, to137, efrom140, eto143, machines129, lOperations131, nodes151, ref146, connections148, duration162, expression164, then166, start154, stmt156, end159, args184, clock187, value190, parameters192, clock195, state197, left199, else169, left172, right173, trigger176, statements178, stmt180, operation182, suchthat214, expression217, condition220, ifexp222, elseexp225, value228, right201, variables204, suchthat206, predicate209, variables212, expression232, exp235, member237, set239, declarations230, type242, receiver246, member248, exp244, value250, ref252, exp253, type255, exp258, type260, type263, literal265, values270, values272, variables274, predicate276, exp268, start282, end284, values287, lrange289, expression279, rrange291, function294, args296, receiver299, member301, value304, parameters306, name309, expression311, transitions313, base318, base320, ref316},
    generalizations={gen_robochart_RCPackage_BasicPackage, gen_robochart_Field_Member, gen_robochart_Field_NamedExpression, gen_robochart_TypedNamedElement_NamedElement, gen_robochart_Member_TypedNamedElement, gen_robochart_Enumeration_TypeDecl, gen_robochart_TypeDecl_NamedElement, gen_robochart_PrimitiveType_TypeDecl, gen_robochart_RecordType_TypeDecl, gen_robochart_ProductType_Type, gen_robochart_RelationType_Type, gen_robochart_Literal_TypeDecl, gen_robochart_Literal_NamedExpression, gen_robochart_NameType_TypeDecl, gen_robochart_Variable_TypedNamedElement, gen_robochart_Variable_NamedExpression, gen_robochart_Variable_Member, gen_robochart_FunctionType_RelationType, gen_robochart_SetType_Type, gen_robochart_SeqType_SetType, gen_robochart_TypeRef_Type, gen_robochart_AnyType_Type, gen_robochart_Parameter_Variable, gen_robochart_OperationSig_NamedElement, gen_robochart_Event_NamedElement, gen_robochart_Function_TypedNamedElement, gen_robochart_Function_NamedExpression, gen_robochart_Operation_NamedElement, gen_robochart_Operation_ConnectionNode, gen_robochart_OperationDef_Operation, gen_robochart_OperationDef_OperationSig, gen_robochart_OperationDef_StateMachineBody, gen_robochart_OperationRef_Operation, gen_robochart_OperationRef_Reference, gen_robochart_RoboticPlatform_NamedElement, gen_robochart_RoboticPlatform_ConnectionNode, gen_robochart_RoboticPlatformDef_Context, gen_robochart_RoboticPlatformDef_RoboticPlatform, gen_robochart_Context_BasicContext, gen_robochart_Interface_NamedElement, gen_robochart_Interface_BasicContext, gen_robochart_StateMachine_NamedElement, gen_robochart_StateMachine_ConnectionNode, gen_robochart_StateMachineDef_StateMachineBody, gen_robochart_StateMachineDef_StateMachine, gen_robochart_StateMachineRef_StateMachine, gen_robochart_StateMachineRef_Reference, gen_robochart_StateMachineBody_Context, gen_robochart_StateMachineBody_NodeContainer, gen_robochart_Clock_NamedElement, gen_robochart_RoboticPlatformRef_RoboticPlatform, gen_robochart_RoboticPlatformRef_Reference, gen_robochart_Initial_Junction, gen_robochart_State_Node, gen_robochart_State_NodeContainer, gen_robochart_Final_State, gen_robochart_ProbabilisticJunction_Junction, gen_robochart_Transition_NamedElement, gen_robochart_Node_NamedElement, gen_robochart_Junction_Node, gen_robochart_EntryAction_Action, gen_robochart_DuringAction_Action, gen_robochart_ExitAction_Action, gen_robochart_Controller_NamedElement, gen_robochart_Controller_ConnectionNode, gen_robochart_ControllerDef_Context, gen_robochart_ControllerDef_Controller, gen_robochart_TimedStatement_Statement, gen_robochart_ControllerRef_Controller, gen_robochart_RCModule_NamedElement, gen_robochart_Wait_Statement, gen_robochart_Skip_Statement, gen_robochart_IfStmt_Statement, gen_robochart_ClockReset_Statement, gen_robochart_ResultExp_Expression, gen_robochart_ArrayExp_Expression, gen_robochart_ClockExp_Expression, gen_robochart_StateClockExp_Expression, gen_robochart_BinaryExpression_Expression, gen_robochart_Assignment_Statement, gen_robochart_SendEvent_Statement, gen_robochart_SeqStatement_Statement, gen_robochart_ParStmt_Statement, gen_robochart_Call_Statement, gen_robochart_DefiniteDescription_LambdaExp, gen_robochart_IfExpression_Expression, gen_robochart_Declaration_NamedElement, gen_robochart_Declaration_NamedExpression, gen_robochart_LetExpression_Expression, gen_robochart_Iff_BinaryExpression, gen_robochart_Implies_BinaryExpression, gen_robochart_Or_BinaryExpression, gen_robochart_QuantifierExpression_Expression, gen_robochart_Forall_QuantifierExpression, gen_robochart_Exists_QuantifierExpression, gen_robochart_LambdaExp_Expression, gen_robochart_And_BinaryExpression, gen_robochart_Not_Expression, gen_robochart_InExp_Expression, gen_robochart_GreaterOrEqual_BinaryExpression, gen_robochart_LessThan_BinaryExpression, gen_robochart_LessOrEqual_BinaryExpression, gen_robochart_Plus_BinaryExpression, gen_robochart_Minus_BinaryExpression, gen_robochart_Modulus_BinaryExpression, gen_robochart_Mult_BinaryExpression, gen_robochart_Div_BinaryExpression, gen_robochart_Cat_BinaryExpression, gen_robochart_TypeExp_Expression, gen_robochart_Equals_BinaryExpression, gen_robochart_Different_BinaryExpression, gen_robochart_GreaterThan_BinaryExpression, gen_robochart_Selection_Expression, gen_robochart_IntegerExp_Expression, gen_robochart_FloatExp_Expression, gen_robochart_Neg_Expression, gen_robochart_BooleanExp_Expression, gen_robochart_VarExp_Expression, gen_robochart_RefExp_Expression, gen_robochart_ToExp_Expression, gen_robochart_FromExp_Expression, gen_robochart_StringExp_Expression, gen_robochart_IsExp_Expression, gen_robochart_EnumExp_Expression, gen_robochart_IdExp_Expression, gen_robochart_ParExp_Expression, gen_robochart_AsExp_Expression, gen_robochart_SeqExp_Expression, gen_robochart_SetExp_Expression, gen_robochart_SetComp_Expression, gen_robochart_SetRange_Expression, gen_robochart_TupleExp_Expression, gen_robochart_RangeExp_Expression, gen_robochart_CallExp_Expression, gen_robochart_ElseExp_Expression, gen_robochart_VarSelection_Assignable, gen_robochart_ArrayAssignable_Assignable, gen_robochart_VarRef_Assignable, gen_robochart_WaitingCondition_NamedElement, gen_robochart_WaitingConditionRef_Expression, gen_robochart_VectorType_Type, gen_robochart_MatrixType_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)