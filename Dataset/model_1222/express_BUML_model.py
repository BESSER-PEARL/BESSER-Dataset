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
express_rules_ONEOFConstraint = Class(name="express::rules::ONEOFConstraint")
SubtypeConstraint = Class(name="SubtypeConstraint")
express_rules_SupertypeRule = Class(name="express::rules::SupertypeRule")
CommonElement = Class(name="CommonElement")
EntityType = Class(name="EntityType")
Population = Class(name="Population")
GlobalRule = Class(name="GlobalRule")
ScopedId = Class(name="ScopedId")
express_rules_TOTAL_OVERConstraint = Class(name="express::rules::TOTAL::OVERConstraint")
express_rules_ANDConstraint = Class(name="express::rules::ANDConstraint")
express_rules_GlobalRule = Class(name="express::rules::GlobalRule")
core_SchemaElement = Class(name="core::SchemaElement")
core_AlgorithmScope = Class(name="core::AlgorithmScope")
express_rules_SubtypeConstraint = Class(name="express::rules::SubtypeConstraint")
Extent = Class(name="Extent")
Expression = Class(name="Expression")
SupertypeRule = Class(name="SupertypeRule")
express_rules_Extent = Class(name="express::rules::Extent")
SETValue = Class(name="SETValue")
EntityInstance = Class(name="EntityInstance")
express_statements_SkipStatement = Class(name="express::statements::SkipStatement")
ControlStatement = Class(name="ControlStatement")
express_statements_AliasStatement = Class(name="express::statements::AliasStatement")
algorithms_Statement = Class(name="algorithms::Statement")
core_LocalScope = Class(name="core::LocalScope")
VARExpression = Class(name="VARExpression")
AliasVariable = Class(name="AliasVariable")
Statement = Class(name="Statement")
NamedRule = Class(name="NamedRule")
express_rules_NamedRule = Class(name="express::rules::NamedRule")
LocalElement = Class(name="LocalElement")
express_statements_ProcedureCall = Class(name="express::statements::ProcedureCall")
Procedure = Class(name="Procedure")
ActualParameter = Class(name="ActualParameter")
VARVariable = Class(name="VARVariable")
express_statements_NullStatement = Class(name="express::statements::NullStatement")
express_statements_VARExpression = Class(name="express::statements::VARExpression", is_abstract=True)
express_statements_AttributeCell = Class(name="express::statements::AttributeCell")
ExplicitAttribute = Class(name="ExplicitAttribute")
express_statements_ControlVariable = Class(name="express::statements::ControlVariable")
NamedVariable = Class(name="NamedVariable")
express_statements_AliasVariable = Class(name="express::statements::AliasVariable")
algorithms_NamedVariable = Class(name="algorithms::NamedVariable")
algorithms_VARVariable = Class(name="algorithms::VARVariable")
express_statements_ControlStatement = Class(name="express::statements::ControlStatement", is_abstract=True)
express_statements_VARCell = Class(name="express::statements::VARCell")
express_statements_StatementBlock = Class(name="express::statements::StatementBlock")
express_statements_CaseAction = Class(name="express::statements::CaseAction")
express_statements_MemberCell = Class(name="express::statements::MemberCell")
ControlVariable = Class(name="ControlVariable")
express_statements_GroupCell = Class(name="express::statements::GroupCell")
SingleEntityType = Class(name="SingleEntityType")
express_statements_VariableCell = Class(name="express::statements::VariableCell")
express_statements_RepeatStatement = Class(name="express::statements::RepeatStatement")
express_statements_IfStatement = Class(name="express::statements::IfStatement")
express_statements_EscapeStatement = Class(name="express::statements::EscapeStatement")
express_statements_ReturnStatement = Class(name="express::statements::ReturnStatement")
express_statements_Assignment = Class(name="express::statements::Assignment")
Variable = Class(name="Variable")
express_statements_CaseStatement = Class(name="express::statements::CaseStatement")
CaseAction = Class(name="CaseAction")
express_expressions_Selector = Class(name="express::expressions::Selector", is_abstract=True)
express_expressions_RepeatCount = Class(name="express::expressions::RepeatCount")
express_expressions_EnumItemRef = Class(name="express::expressions::EnumItemRef")
Primary = Class(name="Primary")
EnumerationItem = Class(name="EnumerationItem")
express_expressions_IndeterminateRef = Class(name="express::expressions::IndeterminateRef")
Indeterminate = Class(name="Indeterminate")
express_expressions_SELFRef = Class(name="express::expressions::SELFRef")
express_expressions_IndexOperation = Class(name="express::expressions::IndexOperation", is_abstract=True)
express_expressions_BinaryOperation = Class(name="express::expressions::BinaryOperation")
Operation = Class(name="Operation")
express_expressions_Literal = Class(name="express::expressions::Literal")
SimpleValue = Class(name="SimpleValue")
express_expressions_BinaryIndex = Class(name="express::expressions::BinaryIndex")
IndexOperation = Class(name="IndexOperation")
express_expressions_PartialEntityConstructor = Class(name="express::expressions::PartialEntityConstructor")
PartialEntityValue = Class(name="PartialEntityValue")
AttributeBinding = Class(name="AttributeBinding")
express_expressions_Coercion = Class(name="express::expressions::Coercion")
express_expressions_AggregateInitializer = Class(name="express::expressions::AggregateInitializer")
VariableType = Class(name="VariableType")
GenericAggregate = Class(name="GenericAggregate")
express_expressions_Primary = Class(name="express::expressions::Primary", is_abstract=True)
MemberBinding = Class(name="MemberBinding")
express_expressions_ActualParameter = Class(name="express::expressions::ActualParameter")
express_expressions_StringIndex = Class(name="express::expressions::StringIndex")
FunctionCall = Class(name="FunctionCall")
Parameter_ = Class(name="Parameter")
express_expressions_ParameterRef = Class(name="express::expressions::ParameterRef")
ProcedureCall = Class(name="ProcedureCall")
express_expressions_AttributeRef = Class(name="express::expressions::AttributeRef")
Selector = Class(name="Selector")
Attribute = Class(name="Attribute")
express_expressions_AggregateIndex = Class(name="express::expressions::AggregateIndex")
express_expressions_GroupRef = Class(name="express::expressions::GroupRef")
express_expressions_UnaryOperation = Class(name="express::expressions::UnaryOperation")
express_expressions_UsedInRef = Class(name="express::expressions::UsedInRef")
express_expressions_ConstantRef = Class(name="express::expressions::ConstantRef")
Constant = Class(name="Constant")
express_expressions_QueryExpression = Class(name="express::expressions::QueryExpression")
core_Expression = Class(name="core::Expression")
QueryVariable = Class(name="QueryVariable")
express_expressions_QueryVariable = Class(name="express::expressions::QueryVariable")
express_expressions_Operation = Class(name="express::expressions::Operation", is_abstract=True)
express_expressions_AttributeBinding = Class(name="express::expressions::AttributeBinding")
AttributeValue = Class(name="AttributeValue")
express_expressions_FunctionCall = Class(name="express::expressions::FunctionCall")
Function = Class(name="Function")
FunctionResult = Class(name="FunctionResult")
express_expressions_MemberBinding = Class(name="express::expressions::MemberBinding")
RepeatCount = Class(name="RepeatCount")
ListMember = Class(name="ListMember")
express_expressions_ExtentRef = Class(name="express::expressions::ExtentRef")
NamedType = Class(name="NamedType")
express_expressions_VariableRef = Class(name="express::expressions::VariableRef")
express_core_TypeElement = Class(name="express::core::TypeElement", is_abstract=True)
NamedElement = Class(name="NamedElement")
express_core_SingleEntityType = Class(name="express::core::SingleEntityType")
PartialEntityType = Class(name="PartialEntityType")
express_core_AGGREGATEType = Class(name="express::core::AGGREGATEType")
GeneralizedType = Class(name="GeneralizedType")
SizeConstraint = Class(name="SizeConstraint")
ParameterType = Class(name="ParameterType")
ActualStructureConstraint = Class(name="ActualStructureConstraint")
express_core_DomainRule = Class(name="express::core::DomainRule")
core_DomainConstraint = Class(name="core::DomainConstraint")
core_TypeElement = Class(name="core::TypeElement")
express_core_GeneralAggregationType = Class(name="express::core::GeneralAggregationType", is_abstract=True)
core_GeneralizedType = Class(name="core::GeneralizedType")
core_AggregationType = Class(name="core::AggregationType")
express_core_ConcreteType = Class(name="express::core::ConcreteType", is_abstract=True)
InstantiableType = Class(name="InstantiableType")
express_core_Expression = Class(name="express::core::Expression")
Instance = Class(name="Instance")
Scope = Class(name="Scope")
DataType = Class(name="DataType")
express_core_InverseAttribute = Class(name="express::core::InverseAttribute")
DomainRole = Class(name="DomainRole")
InvertibleAttribute = Class(name="InvertibleAttribute")
express_core_EnumerationType = Class(name="express::core::EnumerationType")
DefinedType = Class(name="DefinedType")
express_core_GeneralBAGType = Class(name="express::core::GeneralBAGType")
GeneralAggregationType = Class(name="GeneralAggregationType")
EnumerationType = Class(name="EnumerationType")
express_core_VariableType = Class(name="express::core::VariableType", is_abstract=True)
core_DataType = Class(name="core::DataType")
core_AttributeType = Class(name="core::AttributeType")
express_core_ArrayBound = Class(name="express::core::ArrayBound")
express_core_GeneralSETType = Class(name="express::core::GeneralSETType")
express_core_LISTType = Class(name="express::core::LISTType")
ConcreteAggregationType = Class(name="ConcreteAggregationType")
express_core_Redeclaration = Class(name="express::core::Redeclaration")
AttributeType = Class(name="AttributeType")
Redeclaration = Class(name="Redeclaration")
Role = Class(name="Role")
express_core_EntityType = Class(name="express::core::EntityType")
core_NamedType = Class(name="core::NamedType")
core_InstantiableType = Class(name="core::InstantiableType")
RangeRole = Class(name="RangeRole")
UniqueRule = Class(name="UniqueRule")
express_core_DataType = Class(name="express::core::DataType", is_abstract=True)
express_core_PartialEntityType = Class(name="express::core::PartialEntityType")
InterfacedElement = Class(name="InterfacedElement")
SchemaElement = Class(name="SchemaElement")
express_core_InvertibleAttribute = Class(name="express::core::InvertibleAttribute")
InverseAttribute = Class(name="InverseAttribute")
Relationship = Class(name="Relationship")
express_core_GeneralizedType = Class(name="express::core::GeneralizedType", is_abstract=True)
core_ParameterType = Class(name="core::ParameterType")
express_core_Schema = Class(name="express::core::Schema")
Remark = Class(name="Remark")
express_core_InterfacedElement = Class(name="express::core::InterfacedElement")
Schema = Class(name="Schema")
express_core_NumericType = Class(name="express::core::NumericType")
SimpleType = Class(name="SimpleType")
express_core_DefinedType = Class(name="express::core::DefinedType", is_abstract=True)
core_ConcreteType = Class(name="core::ConcreteType")
express_core_UniqueRule = Class(name="express::core::UniqueRule")
TypeElement = Class(name="TypeElement")
express_core_DomainRole = Class(name="express::core::DomainRole")
express_core_BAGType = Class(name="express::core::BAGType")
express_core_RealType = Class(name="express::core::RealType")
NumericType = Class(name="NumericType")
express_core_InstantiableType = Class(name="express::core::InstantiableType", is_abstract=True)
core_VariableType = Class(name="core::VariableType")
express_core_GeneralLISTType = Class(name="express::core::GeneralLISTType")
express_core_NamedElement = Class(name="express::core::NamedElement", is_abstract=True)
express_core_Attribute = Class(name="express::core::Attribute", is_abstract=True)
express_core_DomainConstraint = Class(name="express::core::DomainConstraint", is_abstract=True)
express_core_AttributeType = Class(name="express::core::AttributeType", is_abstract=True)
express_core_LogicType = Class(name="express::core::LogicType")
express_core_GenericType = Class(name="express::core::GenericType")
ActualTypeConstraint = Class(name="ActualTypeConstraint")
express_core_StringType = Class(name="express::core::StringType")
LengthConstraint = Class(name="LengthConstraint")
express_core_AnonymousType = Class(name="express::core::AnonymousType", is_abstract=True)
AnonymousType = Class(name="AnonymousType")
express_core_AlgorithmScope = Class(name="express::core::AlgorithmScope", is_abstract=True)
LocalScope = Class(name="LocalScope")
express_core_Instance = Class(name="express::core::Instance", is_abstract=True)
express_core_LocalElement = Class(name="express::core::LocalElement", is_abstract=True)
DomainConstraint = Class(name="DomainConstraint")
express_core_DerivedAttribute = Class(name="express::core::DerivedAttribute")
express_core_RangeRole = Class(name="express::core::RangeRole")
express_core_Role = Class(name="express::core::Role", is_abstract=True)
express_core_Remark = Class(name="express::core::Remark")
express_core_SizeConstraint = Class(name="express::core::SizeConstraint")
express_core_SpecializedType = Class(name="express::core::SpecializedType")
ConcreteType = Class(name="ConcreteType")
express_core_SETType = Class(name="express::core::SETType")
express_core_GeneralARRAYType = Class(name="express::core::GeneralARRAYType")
ArrayBound = Class(name="ArrayBound")
express_core_Relationship = Class(name="express::core::Relationship")
express_core_NamedType = Class(name="express::core::NamedType", is_abstract=True)
core_Scope = Class(name="core::Scope")
core_CommonElement = Class(name="core::CommonElement")
express_core_LengthConstraint = Class(name="express::core::LengthConstraint")
express_core_LocalScope = Class(name="express::core::LocalScope", is_abstract=True)
express_core_Scope = Class(name="express::core::Scope", is_abstract=True)
SelectType = Class(name="SelectType")
express_core_ParameterType = Class(name="express::core::ParameterType", is_abstract=True)
express_core_SelectType = Class(name="express::core::SelectType")
DomainRule = Class(name="DomainRule")
express_core_BinaryType = Class(name="express::core::BinaryType")
express_core_ScopedId = Class(name="express::core::ScopedId")
express_core_AggregationType = Class(name="express::core::AggregationType", is_abstract=True)
express_core_ExplicitAttribute = Class(name="express::core::ExplicitAttribute")
express_core_SimpleType = Class(name="express::core::SimpleType", is_abstract=True)
express_core_CommonElement = Class(name="express::core::CommonElement", is_abstract=True)
AlgorithmScope = Class(name="AlgorithmScope")
express_core_SchemaElement = Class(name="express::core::SchemaElement", is_abstract=True)
express_core_ActualType = Class(name="express::core::ActualType", is_abstract=True)
Algorithm = Class(name="Algorithm")
express_algorithms_ActualTypeConstraint = Class(name="express::algorithms::ActualTypeConstraint")
GenericType = Class(name="GenericType")
ActualDataType = Class(name="ActualDataType")
express_algorithms_FunctionResult = Class(name="express::algorithms::FunctionResult")
express_algorithms_Function = Class(name="express::algorithms::Function")
express_core_ConcreteAggregationType = Class(name="express::core::ConcreteAggregationType", is_abstract=True)
core_AnonymousType = Class(name="core::AnonymousType")
express_core_ARRAYType = Class(name="express::core::ARRAYType")
express_algorithms_ActualStructure = Class(name="express::algorithms::ActualStructure")
algorithms_GenericElement = Class(name="algorithms::GenericElement")
core_AGGREGATEType = Class(name="core::AGGREGATEType")
express_algorithms_ActualGenericType = Class(name="express::algorithms::ActualGenericType")
ActualType = Class(name="ActualType")
express_algorithms_Statement = Class(name="express::algorithms::Statement")
StatementBlock = Class(name="StatementBlock")
SkipStatement = Class(name="SkipStatement")
EscapeStatement = Class(name="EscapeStatement")
RepeatStatement = Class(name="RepeatStatement")
express_algorithms_InParameter = Class(name="express::algorithms::InParameter")
InVariable = Class(name="InVariable")
express_algorithms_LocalVariable = Class(name="express::algorithms::LocalVariable")
express_algorithms_Procedure = Class(name="express::algorithms::Procedure")
express_algorithms_ActualARRAYType = Class(name="express::algorithms::ActualARRAYType")
ActualAggregationType = Class(name="ActualAggregationType")
express_algorithms_ActualSETType = Class(name="express::algorithms::ActualSETType")
express_algorithms_ActualAGGREGATEType = Class(name="express::algorithms::ActualAGGREGATEType")
ActualStructure = Class(name="ActualStructure")
express_algorithms_NamedVariable = Class(name="express::algorithms::NamedVariable", is_abstract=True)
express_algorithms_InVariable = Class(name="express::algorithms::InVariable")
InParameter = Class(name="InParameter")
express_algorithms_ActualStructureConstraint = Class(name="express::algorithms::ActualStructureConstraint")
AGGREGATEType = Class(name="AGGREGATEType")
express_algorithms_Algorithm = Class(name="express::algorithms::Algorithm", is_abstract=True)
express_algorithms_ActualAggregationType = Class(name="express::algorithms::ActualAggregationType", is_abstract=True)
core_ActualType = Class(name="core::ActualType")
express_algorithms_Parameter = Class(name="express::algorithms::Parameter", is_abstract=True)
express_algorithms_VARParameter = Class(name="express::algorithms::VARParameter")
algorithms_Parameter = Class(name="algorithms::Parameter")
express_algorithms_ActualDataType = Class(name="express::algorithms::ActualDataType")
core_GenericType = Class(name="core::GenericType")
express_algorithms_ActualBAGType = Class(name="express::algorithms::ActualBAGType")
express_instances_AttributeValue = Class(name="express::instances::AttributeValue")
express_instances_ARRAYValue = Class(name="express::instances::ARRAYValue")
AggregateValue = Class(name="AggregateValue")
ArrayMember = Class(name="ArrayMember")
express_instances_RoleName = Class(name="express::instances::RoleName")
express_algorithms_VARVariable = Class(name="express::algorithms::VARVariable", is_abstract=True)
express_algorithms_ActualLISTType = Class(name="express::algorithms::ActualLISTType")
express_algorithms_Variable = Class(name="express::algorithms::Variable", is_abstract=True)
express_algorithms_GenericElement = Class(name="express::algorithms::GenericElement", is_abstract=True)
express_instances_IntegerValue = Class(name="express::instances::IntegerValue")
RealValue = Class(name="RealValue")
express_instances_AggregateValue = Class(name="express::instances::AggregateValue", is_abstract=True)
ConcreteValue = Class(name="ConcreteValue")
express_instances_Constant = Class(name="express::instances::Constant")
express_instances_LogicalValue = Class(name="express::instances::LogicalValue")
express_instances_TypedInstance = Class(name="express::instances::TypedInstance", is_abstract=True)
StringValue = Class(name="StringValue")
express_instances_ListMember = Class(name="express::instances::ListMember")
express_instances_EntityInstance = Class(name="express::instances::EntityInstance")
TypedInstance = Class(name="TypedInstance")
express_instances_BagMember = Class(name="express::instances::BagMember")
EntityValue = Class(name="EntityValue")
express_instances_SingleEntityValue = Class(name="express::instances::SingleEntityValue")
express_instances_Indeterminate = Class(name="express::instances::Indeterminate")
express_instances_SingleLeafInstance = Class(name="express::instances::SingleLeafInstance")
express_instances_GenericAggregate = Class(name="express::instances::GenericAggregate")
LISTValue = Class(name="LISTValue")
express_instances_BinaryValue = Class(name="express::instances::BinaryValue")
express_instances_SpecializedValue = Class(name="express::instances::SpecializedValue")
express_instances_BAGValue = Class(name="express::instances::BAGValue")
BagMember = Class(name="BagMember")
express_instances_EnumerationItem = Class(name="express::instances::EnumerationItem")
instances_TypedInstance = Class(name="instances::TypedInstance")
instances_ConcreteValue = Class(name="instances::ConcreteValue")
express_instances_EntityValue = Class(name="express::instances::EntityValue")
express_instances_SETValue = Class(name="express::instances::SETValue")
express_instances_ArrayMember = Class(name="express::instances::ArrayMember")
express_instances_Population = Class(name="express::instances::Population")
express_instances_RealValue = Class(name="express::instances::RealValue")
express_instances_BooleanValue = Class(name="express::instances::BooleanValue")
LogicalValue = Class(name="LogicalValue")
express_instances_LISTValue = Class(name="express::instances::LISTValue")
core_Instance = Class(name="core::Instance")
instances_AggregateValue = Class(name="instances::AggregateValue")
express_instances_StringValue = Class(name="express::instances::StringValue")
express_instances_TypeName = Class(name="express::instances::TypeName")
express_instances_PartialEntityValue = Class(name="express::instances::PartialEntityValue")
SingleEntityValue = Class(name="SingleEntityValue")
express_instances_NumberValue = Class(name="express::instances::NumberValue")
express_instances_MultiLeafInstance = Class(name="express::instances::MultiLeafInstance")
express_instances_SimpleValue = Class(name="express::instances::SimpleValue", is_abstract=True)
express_instances_ConcreteValue = Class(name="express::instances::ConcreteValue", is_abstract=True)
NumberValue = Class(name="NumberValue")

# express_rules_ONEOFConstraint class attributes and methods

# SubtypeConstraint class attributes and methods

# express_rules_SupertypeRule class attributes and methods
express_rules_SupertypeRule_assertsAbstract: Property = Property(name="assertsAbstract", type=StringType)
express_rules_SupertypeRule.attributes={express_rules_SupertypeRule_assertsAbstract}

# CommonElement class attributes and methods

# EntityType class attributes and methods

# Population class attributes and methods

# GlobalRule class attributes and methods

# ScopedId class attributes and methods

# express_rules_TOTAL_OVERConstraint class attributes and methods

# express_rules_ANDConstraint class attributes and methods

# express_rules_GlobalRule class attributes and methods

# core_SchemaElement class attributes and methods

# core_AlgorithmScope class attributes and methods

# express_rules_SubtypeConstraint class attributes and methods

# Extent class attributes and methods

# Expression class attributes and methods

# SupertypeRule class attributes and methods

# express_rules_Extent class attributes and methods

# SETValue class attributes and methods

# EntityInstance class attributes and methods

# express_statements_SkipStatement class attributes and methods

# ControlStatement class attributes and methods

# express_statements_AliasStatement class attributes and methods

# algorithms_Statement class attributes and methods

# core_LocalScope class attributes and methods

# VARExpression class attributes and methods

# AliasVariable class attributes and methods

# Statement class attributes and methods

# NamedRule class attributes and methods

# express_rules_NamedRule class attributes and methods
express_rules_NamedRule_position: Property = Property(name="position", type=StringType)
express_rules_NamedRule.attributes={express_rules_NamedRule_position}

# LocalElement class attributes and methods

# express_statements_ProcedureCall class attributes and methods

# Procedure class attributes and methods

# ActualParameter class attributes and methods

# VARVariable class attributes and methods

# express_statements_NullStatement class attributes and methods

# express_statements_VARExpression class attributes and methods
express_statements_VARExpression_text: Property = Property(name="text", type=StringType)
express_statements_VARExpression.attributes={express_statements_VARExpression_text}

# express_statements_AttributeCell class attributes and methods
express_statements_AttributeCell_id: Property = Property(name="id", type=StringType)
express_statements_AttributeCell.attributes={express_statements_AttributeCell_id}

# ExplicitAttribute class attributes and methods

# express_statements_ControlVariable class attributes and methods

# NamedVariable class attributes and methods

# express_statements_AliasVariable class attributes and methods

# algorithms_NamedVariable class attributes and methods

# algorithms_VARVariable class attributes and methods

# express_statements_ControlStatement class attributes and methods

# express_statements_VARCell class attributes and methods
express_statements_VARCell_id: Property = Property(name="id", type=StringType)
express_statements_VARCell.attributes={express_statements_VARCell_id}

# express_statements_StatementBlock class attributes and methods
express_statements_StatementBlock_delimited: Property = Property(name="delimited", type=StringType)
express_statements_StatementBlock.attributes={express_statements_StatementBlock_delimited}

# express_statements_CaseAction class attributes and methods
express_statements_CaseAction_isDefault: Property = Property(name="isDefault", type=StringType)
express_statements_CaseAction.attributes={express_statements_CaseAction_isDefault}

# express_statements_MemberCell class attributes and methods

# ControlVariable class attributes and methods

# express_statements_GroupCell class attributes and methods
express_statements_GroupCell_id: Property = Property(name="id", type=StringType)
express_statements_GroupCell.attributes={express_statements_GroupCell_id}

# SingleEntityType class attributes and methods

# express_statements_VariableCell class attributes and methods
express_statements_VariableCell_id: Property = Property(name="id", type=StringType)
express_statements_VariableCell.attributes={express_statements_VariableCell_id}

# express_statements_RepeatStatement class attributes and methods

# express_statements_IfStatement class attributes and methods

# express_statements_EscapeStatement class attributes and methods

# express_statements_ReturnStatement class attributes and methods

# express_statements_Assignment class attributes and methods

# Variable class attributes and methods

# express_statements_CaseStatement class attributes and methods

# CaseAction class attributes and methods

# express_expressions_Selector class attributes and methods

# express_expressions_RepeatCount class attributes and methods

# express_expressions_EnumItemRef class attributes and methods
express_expressions_EnumItemRef_id: Property = Property(name="id", type=StringType)
express_expressions_EnumItemRef.attributes={express_expressions_EnumItemRef_id}

# Primary class attributes and methods

# EnumerationItem class attributes and methods

# express_expressions_IndeterminateRef class attributes and methods

# Indeterminate class attributes and methods

# express_expressions_SELFRef class attributes and methods

# express_expressions_IndexOperation class attributes and methods

# express_expressions_BinaryOperation class attributes and methods
express_expressions_BinaryOperation_operator: Property = Property(name="operator", type=StringType)
express_expressions_BinaryOperation.attributes={express_expressions_BinaryOperation_operator}

# Operation class attributes and methods

# express_expressions_Literal class attributes and methods

# SimpleValue class attributes and methods

# express_expressions_BinaryIndex class attributes and methods

# IndexOperation class attributes and methods

# express_expressions_PartialEntityConstructor class attributes and methods
express_expressions_PartialEntityConstructor_id: Property = Property(name="id", type=StringType)
express_expressions_PartialEntityConstructor.attributes={express_expressions_PartialEntityConstructor_id}

# PartialEntityValue class attributes and methods

# AttributeBinding class attributes and methods

# express_expressions_Coercion class attributes and methods

# express_expressions_AggregateInitializer class attributes and methods

# VariableType class attributes and methods

# GenericAggregate class attributes and methods

# express_expressions_Primary class attributes and methods

# MemberBinding class attributes and methods

# express_expressions_ActualParameter class attributes and methods
express_expressions_ActualParameter_position: Property = Property(name="position", type=StringType)
express_expressions_ActualParameter.attributes={express_expressions_ActualParameter_position}

# express_expressions_StringIndex class attributes and methods

# FunctionCall class attributes and methods

# Parameter class attributes and methods

# express_expressions_ParameterRef class attributes and methods
express_expressions_ParameterRef_id: Property = Property(name="id", type=StringType)
express_expressions_ParameterRef.attributes={express_expressions_ParameterRef_id}

# ProcedureCall class attributes and methods

# express_expressions_AttributeRef class attributes and methods
express_expressions_AttributeRef_id: Property = Property(name="id", type=StringType)
express_expressions_AttributeRef.attributes={express_expressions_AttributeRef_id}

# Selector class attributes and methods

# Attribute class attributes and methods

# express_expressions_AggregateIndex class attributes and methods

# express_expressions_GroupRef class attributes and methods
express_expressions_GroupRef_id: Property = Property(name="id", type=StringType)
express_expressions_GroupRef.attributes={express_expressions_GroupRef_id}

# express_expressions_UnaryOperation class attributes and methods
express_expressions_UnaryOperation_operator: Property = Property(name="operator", type=StringType)
express_expressions_UnaryOperation.attributes={express_expressions_UnaryOperation_operator}

# express_expressions_UsedInRef class attributes and methods

# express_expressions_ConstantRef class attributes and methods
express_expressions_ConstantRef_id: Property = Property(name="id", type=StringType)
express_expressions_ConstantRef.attributes={express_expressions_ConstantRef_id}

# Constant class attributes and methods

# express_expressions_QueryExpression class attributes and methods

# core_Expression class attributes and methods

# QueryVariable class attributes and methods

# express_expressions_QueryVariable class attributes and methods

# express_expressions_Operation class attributes and methods

# express_expressions_AttributeBinding class attributes and methods
express_expressions_AttributeBinding_position: Property = Property(name="position", type=StringType)
express_expressions_AttributeBinding.attributes={express_expressions_AttributeBinding_position}

# AttributeValue class attributes and methods

# express_expressions_FunctionCall class attributes and methods

# Function class attributes and methods

# FunctionResult class attributes and methods

# express_expressions_MemberBinding class attributes and methods
express_expressions_MemberBinding_position: Property = Property(name="position", type=StringType)
express_expressions_MemberBinding.attributes={express_expressions_MemberBinding_position}

# RepeatCount class attributes and methods

# ListMember class attributes and methods

# express_expressions_ExtentRef class attributes and methods
express_expressions_ExtentRef_id: Property = Property(name="id", type=StringType)
express_expressions_ExtentRef.attributes={express_expressions_ExtentRef_id}

# NamedType class attributes and methods

# express_expressions_VariableRef class attributes and methods
express_expressions_VariableRef_id: Property = Property(name="id", type=StringType)
express_expressions_VariableRef.attributes={express_expressions_VariableRef_id}

# express_core_TypeElement class attributes and methods

# NamedElement class attributes and methods

# express_core_SingleEntityType class attributes and methods

# PartialEntityType class attributes and methods

# express_core_AGGREGATEType class attributes and methods

# GeneralizedType class attributes and methods

# SizeConstraint class attributes and methods

# ParameterType class attributes and methods

# ActualStructureConstraint class attributes and methods

# express_core_DomainRule class attributes and methods
express_core_DomainRule_position: Property = Property(name="position", type=StringType)
express_core_DomainRule.attributes={express_core_DomainRule_position}

# core_DomainConstraint class attributes and methods

# core_TypeElement class attributes and methods

# express_core_GeneralAggregationType class attributes and methods

# core_GeneralizedType class attributes and methods

# core_AggregationType class attributes and methods

# express_core_ConcreteType class attributes and methods

# InstantiableType class attributes and methods

# express_core_Expression class attributes and methods
express_core_Expression_text: Property = Property(name="text", type=StringType)
express_core_Expression.attributes={express_core_Expression_text}

# Instance class attributes and methods

# Scope class attributes and methods

# DataType class attributes and methods

# express_core_InverseAttribute class attributes and methods
express_core_InverseAttribute_isUnique: Property = Property(name="isUnique", type=StringType)
express_core_InverseAttribute.attributes={express_core_InverseAttribute_isUnique}

# DomainRole class attributes and methods

# InvertibleAttribute class attributes and methods

# express_core_EnumerationType class attributes and methods
express_core_EnumerationType_isExtensible: Property = Property(name="isExtensible", type=StringType)
express_core_EnumerationType.attributes={express_core_EnumerationType_isExtensible}

# DefinedType class attributes and methods

# express_core_GeneralBAGType class attributes and methods

# GeneralAggregationType class attributes and methods

# EnumerationType class attributes and methods

# express_core_VariableType class attributes and methods

# core_DataType class attributes and methods

# core_AttributeType class attributes and methods

# express_core_ArrayBound class attributes and methods
express_core_ArrayBound_bound: Property = Property(name="bound", type=StringType)
express_core_ArrayBound.attributes={express_core_ArrayBound_bound}

# express_core_GeneralSETType class attributes and methods

# express_core_LISTType class attributes and methods

# ConcreteAggregationType class attributes and methods

# express_core_Redeclaration class attributes and methods
express_core_Redeclaration_position: Property = Property(name="position", type=StringType)
express_core_Redeclaration_isMandatory: Property = Property(name="isMandatory", type=StringType)
express_core_Redeclaration.attributes={express_core_Redeclaration_position, express_core_Redeclaration_isMandatory}

# AttributeType class attributes and methods

# Redeclaration class attributes and methods

# Role class attributes and methods

# express_core_EntityType class attributes and methods
express_core_EntityType_isAbstract: Property = Property(name="isAbstract", type=StringType)
express_core_EntityType.attributes={express_core_EntityType_isAbstract}

# core_NamedType class attributes and methods

# core_InstantiableType class attributes and methods

# RangeRole class attributes and methods

# UniqueRule class attributes and methods

# express_core_DataType class attributes and methods

# express_core_PartialEntityType class attributes and methods

# InterfacedElement class attributes and methods

# SchemaElement class attributes and methods

# express_core_InvertibleAttribute class attributes and methods

# InverseAttribute class attributes and methods

# Relationship class attributes and methods

# express_core_GeneralizedType class attributes and methods

# core_ParameterType class attributes and methods

# express_core_Schema class attributes and methods
express_core_Schema_name: Property = Property(name="name", type=StringType)
express_core_Schema_version: Property = Property(name="version", type=StringType)
express_core_Schema.attributes={express_core_Schema_name, express_core_Schema_version}

# Remark class attributes and methods

# express_core_InterfacedElement class attributes and methods
express_core_InterfacedElement_isUSE: Property = Property(name="isUSE", type=StringType)
express_core_InterfacedElement.attributes={express_core_InterfacedElement_isUSE}

# Schema class attributes and methods

# express_core_NumericType class attributes and methods

# SimpleType class attributes and methods

# express_core_DefinedType class attributes and methods

# core_ConcreteType class attributes and methods

# express_core_UniqueRule class attributes and methods
express_core_UniqueRule_position: Property = Property(name="position", type=StringType)
express_core_UniqueRule.attributes={express_core_UniqueRule_position}

# TypeElement class attributes and methods

# express_core_DomainRole class attributes and methods

# express_core_BAGType class attributes and methods

# express_core_RealType class attributes and methods
express_core_RealType_precision: Property = Property(name="precision", type=StringType)
express_core_RealType.attributes={express_core_RealType_precision}

# NumericType class attributes and methods

# express_core_InstantiableType class attributes and methods

# core_VariableType class attributes and methods

# express_core_GeneralLISTType class attributes and methods

# express_core_NamedElement class attributes and methods

# express_core_Attribute class attributes and methods
express_core_Attribute_isAbstract: Property = Property(name="isAbstract", type=StringType)
express_core_Attribute_position: Property = Property(name="position", type=StringType)
express_core_Attribute.attributes={express_core_Attribute_position, express_core_Attribute_isAbstract}

# express_core_DomainConstraint class attributes and methods

# express_core_AttributeType class attributes and methods

# express_core_LogicType class attributes and methods

# express_core_GenericType class attributes and methods
express_core_GenericType_isEntity: Property = Property(name="isEntity", type=StringType)
express_core_GenericType.attributes={express_core_GenericType_isEntity}

# ActualTypeConstraint class attributes and methods

# express_core_StringType class attributes and methods

# LengthConstraint class attributes and methods

# express_core_AnonymousType class attributes and methods

# AnonymousType class attributes and methods

# express_core_AlgorithmScope class attributes and methods

# LocalScope class attributes and methods

# express_core_Instance class attributes and methods

# express_core_LocalElement class attributes and methods

# DomainConstraint class attributes and methods

# express_core_DerivedAttribute class attributes and methods

# express_core_RangeRole class attributes and methods

# express_core_Role class attributes and methods

# express_core_Remark class attributes and methods
express_core_Remark_isTagged: Property = Property(name="isTagged", type=StringType)
express_core_Remark_isTail: Property = Property(name="isTail", type=StringType)
express_core_Remark_text: Property = Property(name="text", type=StringType)
express_core_Remark.attributes={express_core_Remark_isTail, express_core_Remark_isTagged, express_core_Remark_text}

# express_core_SizeConstraint class attributes and methods
express_core_SizeConstraint_bound: Property = Property(name="bound", type=StringType)
express_core_SizeConstraint.attributes={express_core_SizeConstraint_bound}

# express_core_SpecializedType class attributes and methods

# ConcreteType class attributes and methods

# express_core_SETType class attributes and methods

# express_core_GeneralARRAYType class attributes and methods
express_core_GeneralARRAYType_isOptional: Property = Property(name="isOptional", type=StringType)
express_core_GeneralARRAYType.attributes={express_core_GeneralARRAYType_isOptional}

# ArrayBound class attributes and methods

# express_core_Relationship class attributes and methods

# express_core_NamedType class attributes and methods

# core_Scope class attributes and methods

# core_CommonElement class attributes and methods

# express_core_LengthConstraint class attributes and methods
express_core_LengthConstraint_maxLength: Property = Property(name="maxLength", type=StringType)
express_core_LengthConstraint_isFixed: Property = Property(name="isFixed", type=StringType)
express_core_LengthConstraint.attributes={express_core_LengthConstraint_isFixed, express_core_LengthConstraint_maxLength}

# express_core_LocalScope class attributes and methods

# express_core_Scope class attributes and methods

# SelectType class attributes and methods

# express_core_ParameterType class attributes and methods

# express_core_SelectType class attributes and methods
express_core_SelectType_isExtensible: Property = Property(name="isExtensible", type=StringType)
express_core_SelectType_isEntity: Property = Property(name="isEntity", type=StringType)
express_core_SelectType.attributes={express_core_SelectType_isExtensible, express_core_SelectType_isEntity}

# DomainRule class attributes and methods

# express_core_BinaryType class attributes and methods

# express_core_ScopedId class attributes and methods
express_core_ScopedId_localName: Property = Property(name="localName", type=StringType)
express_core_ScopedId.attributes={express_core_ScopedId_localName}

# express_core_AggregationType class attributes and methods
express_core_AggregationType_isUnique: Property = Property(name="isUnique", type=StringType)
express_core_AggregationType_ordering: Property = Property(name="ordering", type=StringType)
express_core_AggregationType.attributes={express_core_AggregationType_ordering, express_core_AggregationType_isUnique}

# express_core_ExplicitAttribute class attributes and methods
express_core_ExplicitAttribute_isOptional: Property = Property(name="isOptional", type=StringType)
express_core_ExplicitAttribute.attributes={express_core_ExplicitAttribute_isOptional}

# express_core_SimpleType class attributes and methods
express_core_SimpleType_id: Property = Property(name="id", type=StringType)
express_core_SimpleType.attributes={express_core_SimpleType_id}

# express_core_CommonElement class attributes and methods

# AlgorithmScope class attributes and methods

# express_core_SchemaElement class attributes and methods

# express_core_ActualType class attributes and methods

# Algorithm class attributes and methods

# express_algorithms_ActualTypeConstraint class attributes and methods
express_algorithms_ActualTypeConstraint_label: Property = Property(name="label", type=StringType)
express_algorithms_ActualTypeConstraint.attributes={express_algorithms_ActualTypeConstraint_label}

# GenericType class attributes and methods

# ActualDataType class attributes and methods

# express_algorithms_FunctionResult class attributes and methods

# express_algorithms_Function class attributes and methods

# express_core_ConcreteAggregationType class attributes and methods

# core_AnonymousType class attributes and methods

# express_core_ARRAYType class attributes and methods
express_core_ARRAYType_isOptional: Property = Property(name="isOptional", type=StringType)
express_core_ARRAYType.attributes={express_core_ARRAYType_isOptional}

# express_algorithms_ActualStructure class attributes and methods

# algorithms_GenericElement class attributes and methods

# core_AGGREGATEType class attributes and methods

# express_algorithms_ActualGenericType class attributes and methods
express_algorithms_ActualGenericType_isEntity: Property = Property(name="isEntity", type=StringType)
express_algorithms_ActualGenericType_label: Property = Property(name="label", type=StringType)
express_algorithms_ActualGenericType.attributes={express_algorithms_ActualGenericType_isEntity, express_algorithms_ActualGenericType_label}

# ActualType class attributes and methods

# express_algorithms_Statement class attributes and methods
express_algorithms_Statement_text: Property = Property(name="text", type=StringType)
express_algorithms_Statement.attributes={express_algorithms_Statement_text}

# StatementBlock class attributes and methods

# SkipStatement class attributes and methods

# EscapeStatement class attributes and methods

# RepeatStatement class attributes and methods

# express_algorithms_InParameter class attributes and methods

# InVariable class attributes and methods

# express_algorithms_LocalVariable class attributes and methods

# express_algorithms_Procedure class attributes and methods

# express_algorithms_ActualARRAYType class attributes and methods
express_algorithms_ActualARRAYType_isOptional: Property = Property(name="isOptional", type=StringType)
express_algorithms_ActualARRAYType.attributes={express_algorithms_ActualARRAYType_isOptional}

# ActualAggregationType class attributes and methods

# express_algorithms_ActualSETType class attributes and methods

# express_algorithms_ActualAGGREGATEType class attributes and methods
express_algorithms_ActualAGGREGATEType_label: Property = Property(name="label", type=StringType)
express_algorithms_ActualAGGREGATEType.attributes={express_algorithms_ActualAGGREGATEType_label}

# ActualStructure class attributes and methods

# express_algorithms_NamedVariable class attributes and methods

# express_algorithms_InVariable class attributes and methods

# InParameter class attributes and methods

# express_algorithms_ActualStructureConstraint class attributes and methods
express_algorithms_ActualStructureConstraint_label: Property = Property(name="label", type=StringType)
express_algorithms_ActualStructureConstraint.attributes={express_algorithms_ActualStructureConstraint_label}

# AGGREGATEType class attributes and methods

# express_algorithms_Algorithm class attributes and methods

# express_algorithms_ActualAggregationType class attributes and methods

# core_ActualType class attributes and methods

# express_algorithms_Parameter class attributes and methods
express_algorithms_Parameter_inout: Property = Property(name="inout", type=StringType)
express_algorithms_Parameter_position: Property = Property(name="position", type=StringType)
express_algorithms_Parameter.attributes={express_algorithms_Parameter_position, express_algorithms_Parameter_inout}

# express_algorithms_VARParameter class attributes and methods

# algorithms_Parameter class attributes and methods

# express_algorithms_ActualDataType class attributes and methods

# core_GenericType class attributes and methods

# express_algorithms_ActualBAGType class attributes and methods

# express_instances_AttributeValue class attributes and methods

# express_instances_ARRAYValue class attributes and methods

# AggregateValue class attributes and methods

# ArrayMember class attributes and methods

# express_instances_RoleName class attributes and methods

# express_algorithms_VARVariable class attributes and methods

# express_algorithms_ActualLISTType class attributes and methods

# express_algorithms_Variable class attributes and methods

# express_algorithms_GenericElement class attributes and methods

# express_instances_IntegerValue class attributes and methods

# RealValue class attributes and methods

# express_instances_AggregateValue class attributes and methods

# ConcreteValue class attributes and methods

# express_instances_Constant class attributes and methods

# express_instances_LogicalValue class attributes and methods

# express_instances_TypedInstance class attributes and methods

# StringValue class attributes and methods

# express_instances_ListMember class attributes and methods
express_instances_ListMember_position: Property = Property(name="position", type=StringType)
express_instances_ListMember.attributes={express_instances_ListMember_position}

# express_instances_EntityInstance class attributes and methods
express_instances_EntityInstance_id: Property = Property(name="id", type=StringType)
express_instances_EntityInstance.attributes={express_instances_EntityInstance_id}

# TypedInstance class attributes and methods

# express_instances_BagMember class attributes and methods
express_instances_BagMember_count: Property = Property(name="count", type=StringType)
express_instances_BagMember.attributes={express_instances_BagMember_count}

# EntityValue class attributes and methods

# express_instances_SingleEntityValue class attributes and methods

# express_instances_Indeterminate class attributes and methods

# express_instances_SingleLeafInstance class attributes and methods

# express_instances_GenericAggregate class attributes and methods

# LISTValue class attributes and methods

# express_instances_BinaryValue class attributes and methods

# express_instances_SpecializedValue class attributes and methods

# express_instances_BAGValue class attributes and methods

# BagMember class attributes and methods

# express_instances_EnumerationItem class attributes and methods
express_instances_EnumerationItem_position: Property = Property(name="position", type=StringType)
express_instances_EnumerationItem.attributes={express_instances_EnumerationItem_position}

# instances_TypedInstance class attributes and methods

# instances_ConcreteValue class attributes and methods

# express_instances_EntityValue class attributes and methods

# express_instances_SETValue class attributes and methods

# express_instances_ArrayMember class attributes and methods
express_instances_ArrayMember_index: Property = Property(name="index", type=StringType)
express_instances_ArrayMember.attributes={express_instances_ArrayMember_index}

# express_instances_Population class attributes and methods

# express_instances_RealValue class attributes and methods

# express_instances_BooleanValue class attributes and methods

# LogicalValue class attributes and methods

# express_instances_LISTValue class attributes and methods

# core_Instance class attributes and methods

# instances_AggregateValue class attributes and methods

# express_instances_StringValue class attributes and methods

# express_instances_TypeName class attributes and methods

# express_instances_PartialEntityValue class attributes and methods

# SingleEntityValue class attributes and methods

# express_instances_NumberValue class attributes and methods

# express_instances_MultiLeafInstance class attributes and methods

# express_instances_SimpleValue class attributes and methods
express_instances_SimpleValue_name: Property = Property(name="name", type=StringType)
express_instances_SimpleValue.attributes={express_instances_SimpleValue_name}

# express_instances_ConcreteValue class attributes and methods

# NumberValue class attributes and methods

# Relationships
namedSupertype0: BinaryAssociation = BinaryAssociation(
    name="namedSupertype0",
    ends={
        Property(name="EntityType", type=express_rules_SupertypeRule, multiplicity=Multiplicity(1, 1)),
        Property(name="express_rules_SupertypeRule", type=EntityType, multiplicity=Multiplicity(1, 1))
    }
)
constraints1: BinaryAssociation = BinaryAssociation(
    name="constraints1",
    ends={
        Property(name="rules", type=express_rules_SupertypeRule, multiplicity=Multiplicity(1, 1)),
        Property(name="SubtypeConstraint", type=SubtypeConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
withinPopulation11: BinaryAssociation = BinaryAssociation(
    name="withinPopulation11",
    ends={
        Property(name="Population", type=express_rules_Extent, multiplicity=Multiplicity(1, 1)),
        Property(name="express_rules_Extent12", type=Population, multiplicity=Multiplicity(1, 1))
    }
)
constraintRules13: BinaryAssociation = BinaryAssociation(
    name="constraintRules13",
    ends={
        Property(name="rules14", type=express_rules_Extent, multiplicity=Multiplicity(1, 1)),
        Property(name="GlobalRule", type=GlobalRule, multiplicity=Multiplicity(0, 9999))
    }
)
forType15: BinaryAssociation = BinaryAssociation(
    name="forType15",
    ends={
        Property(name="core", type=express_rules_Extent, multiplicity=Multiplicity(1, 1)),
        Property(name="EntityType16", type=EntityType, multiplicity=Multiplicity(1, 1))
    }
)
id17: BinaryAssociation = BinaryAssociation(
    name="id17",
    ends={
        Property(name="ScopedId", type=express_rules_Extent, multiplicity=Multiplicity(1, 1)),
        Property(name="express_rules_Extent18", type=ScopedId, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
constrainedSubtypes2: BinaryAssociation = BinaryAssociation(
    name="constrainedSubtypes2",
    ends={
        Property(name="rules3", type=express_rules_SubtypeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="Extent", type=Extent, multiplicity=Multiplicity(1, 9999))
    }
)
equivalentRule4: BinaryAssociation = BinaryAssociation(
    name="equivalentRule4",
    ends={
        Property(name="Expression", type=express_rules_SubtypeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="express_rules_SubtypeConstraint", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
collection5: BinaryAssociation = BinaryAssociation(
    name="collection5",
    ends={
        Property(name="rules6", type=express_rules_SubtypeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="SupertypeRule", type=SupertypeRule, multiplicity=Multiplicity(1, 1))
    }
)
constraints7: BinaryAssociation = BinaryAssociation(
    name="constraints7",
    ends={
        Property(name="rules9", type=express_rules_Extent, multiplicity=Multiplicity(1, 1)),
        Property(name="SubtypeConstraint8", type=SubtypeConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
content10: BinaryAssociation = BinaryAssociation(
    name="content10",
    ends={
        Property(name="EntityInstance", type=express_rules_Extent, multiplicity=Multiplicity(1, 1)),
        Property(name="express_rules_Extent", type=EntityInstance, multiplicity=Multiplicity(0, 9999))
    }
)
actualParameters28: BinaryAssociation = BinaryAssociation(
    name="actualParameters28",
    ends={
        Property(name="expressions", type=express_statements_ProcedureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="ActualParameter", type=ActualParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bindsToReference29: BinaryAssociation = BinaryAssociation(
    name="bindsToReference29",
    ends={
        Property(name="VARExpression", type=express_statements_AliasStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_AliasStatement", type=VARExpression, multiplicity=Multiplicity(1, 1))
    }
)
body30: BinaryAssociation = BinaryAssociation(
    name="body30",
    ends={
        Property(name="Statement32", type=express_statements_AliasStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_AliasStatement31", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
aliasVariable33: BinaryAssociation = BinaryAssociation(
    name="aliasVariable33",
    ends={
        Property(name="AliasVariable", type=express_statements_AliasStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_AliasStatement34", type=AliasVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
supportingBody19: BinaryAssociation = BinaryAssociation(
    name="supportingBody19",
    ends={
        Property(name="Statement", type=express_rules_GlobalRule, multiplicity=Multiplicity(1, 1)),
        Property(name="express_rules_GlobalRule", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constrainedExtents20: BinaryAssociation = BinaryAssociation(
    name="constrainedExtents20",
    ends={
        Property(name="rules22", type=express_rules_GlobalRule, multiplicity=Multiplicity(1, 1)),
        Property(name="Extent21", type=Extent, multiplicity=Multiplicity(1, 9999))
    }
)
containsRules23: BinaryAssociation = BinaryAssociation(
    name="containsRules23",
    ends={
        Property(name="NamedRule", type=express_rules_GlobalRule, multiplicity=Multiplicity(1, 1)),
        Property(name="express_rules_GlobalRule24", type=NamedRule, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
assertsExpression25: BinaryAssociation = BinaryAssociation(
    name="assertsExpression25",
    ends={
        Property(name="Expression26", type=express_rules_NamedRule, multiplicity=Multiplicity(1, 1)),
        Property(name="express_rules_NamedRule", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
invokes27: BinaryAssociation = BinaryAssociation(
    name="invokes27",
    ends={
        Property(name="Procedure", type=express_statements_ProcedureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_ProcedureCall", type=Procedure, multiplicity=Multiplicity(1, 1))
    }
)
refersTo45: BinaryAssociation = BinaryAssociation(
    name="refersTo45",
    ends={
        Property(name="VARVariable", type=express_statements_VARCell, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_VARCell", type=VARVariable, multiplicity=Multiplicity(1, 1))
    }
)
refersTo46: BinaryAssociation = BinaryAssociation(
    name="refersTo46",
    ends={
        Property(name="ExplicitAttribute", type=express_statements_AttributeCell, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_AttributeCell", type=ExplicitAttribute, multiplicity=Multiplicity(1, 1))
    }
)
baseEntity47: BinaryAssociation = BinaryAssociation(
    name="baseEntity47",
    ends={
        Property(name="VARExpression49", type=express_statements_AttributeCell, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_AttributeCell48", type=VARExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
boundValue35: BinaryAssociation = BinaryAssociation(
    name="boundValue35",
    ends={
        Property(name="Expression36", type=express_statements_ControlVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_ControlVariable", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
initialValue37: BinaryAssociation = BinaryAssociation(
    name="initialValue37",
    ends={
        Property(name="Expression39", type=express_statements_ControlVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_ControlVariable38", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
increment40: BinaryAssociation = BinaryAssociation(
    name="increment40",
    ends={
        Property(name="Expression42", type=express_statements_ControlVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_ControlVariable41", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
referent43: BinaryAssociation = BinaryAssociation(
    name="referent43",
    ends={
        Property(name="VARExpression44", type=express_statements_AliasVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_AliasVariable", type=VARExpression, multiplicity=Multiplicity(0, 1))
    }
)
bodyStatements_Statement50: BinaryAssociation = BinaryAssociation(
    name="bodyStatements_Statement50",
    ends={
        Property(name="algorithms", type=express_statements_StatementBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="Statement51", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
labelValue52: BinaryAssociation = BinaryAssociation(
    name="labelValue52",
    ends={
        Property(name="Expression53", type=express_statements_CaseAction, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_CaseAction", type=Expression, multiplicity=Multiplicity(0, 9999))
    }
)
action54: BinaryAssociation = BinaryAssociation(
    name="action54",
    ends={
        Property(name="Statement56", type=express_statements_CaseAction, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_CaseAction55", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
whileExpression62: BinaryAssociation = BinaryAssociation(
    name="whileExpression62",
    ends={
        Property(name="Expression63", type=express_statements_RepeatStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_RepeatStatement", type=Expression, multiplicity=Multiplicity(0, 1))
    }
)
body64: BinaryAssociation = BinaryAssociation(
    name="body64",
    ends={
        Property(name="algorithms66", type=express_statements_RepeatStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="Statement65", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
controlVariable67: BinaryAssociation = BinaryAssociation(
    name="controlVariable67",
    ends={
        Property(name="ControlVariable", type=express_statements_RepeatStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_RepeatStatement68", type=ControlVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
untilExpression69: BinaryAssociation = BinaryAssociation(
    name="untilExpression69",
    ends={
        Property(name="Expression71", type=express_statements_RepeatStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_RepeatStatement70", type=Expression, multiplicity=Multiplicity(0, 1))
    }
)
baseEntity72: BinaryAssociation = BinaryAssociation(
    name="baseEntity72",
    ends={
        Property(name="VARExpression73", type=express_statements_GroupCell, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_GroupCell", type=VARExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
refersTo74: BinaryAssociation = BinaryAssociation(
    name="refersTo74",
    ends={
        Property(name="SingleEntityType", type=express_statements_GroupCell, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_GroupCell75", type=SingleEntityType, multiplicity=Multiplicity(1, 1))
    }
)
indexValue57: BinaryAssociation = BinaryAssociation(
    name="indexValue57",
    ends={
        Property(name="Expression58", type=express_statements_MemberCell, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_MemberCell", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
baseAggregate59: BinaryAssociation = BinaryAssociation(
    name="baseAggregate59",
    ends={
        Property(name="VARExpression61", type=express_statements_MemberCell, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_MemberCell60", type=VARExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ifCondition81: BinaryAssociation = BinaryAssociation(
    name="ifCondition81",
    ends={
        Property(name="Expression82", type=express_statements_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_IfStatement", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseActions83: BinaryAssociation = BinaryAssociation(
    name="elseActions83",
    ends={
        Property(name="Statement85", type=express_statements_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_IfStatement84", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenActions86: BinaryAssociation = BinaryAssociation(
    name="thenActions86",
    ends={
        Property(name="Statement88", type=express_statements_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_IfStatement87", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnValue89: BinaryAssociation = BinaryAssociation(
    name="returnValue89",
    ends={
        Property(name="Expression90", type=express_statements_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_ReturnStatement", type=Expression, multiplicity=Multiplicity(0, 1))
    }
)
assignedValue91: BinaryAssociation = BinaryAssociation(
    name="assignedValue91",
    ends={
        Property(name="Expression92", type=express_statements_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_Assignment", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
refersTo76: BinaryAssociation = BinaryAssociation(
    name="refersTo76",
    ends={
        Property(name="Variable", type=express_statements_VariableCell, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_VariableCell", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
cases77: BinaryAssociation = BinaryAssociation(
    name="cases77",
    ends={
        Property(name="CaseAction", type=express_statements_CaseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_CaseStatement", type=CaseAction, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
selectionExpression78: BinaryAssociation = BinaryAssociation(
    name="selectionExpression78",
    ends={
        Property(name="Expression80", type=express_statements_CaseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_CaseStatement79", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
entityInstance96: BinaryAssociation = BinaryAssociation(
    name="entityInstance96",
    ends={
        Property(name="Expression97", type=express_expressions_Selector, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_Selector", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
derivation98: BinaryAssociation = BinaryAssociation(
    name="derivation98",
    ends={
        Property(name="Expression99", type=express_expressions_RepeatCount, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_RepeatCount", type=Expression, multiplicity=Multiplicity(0, 1))
    }
)
refersTo100: BinaryAssociation = BinaryAssociation(
    name="refersTo100",
    ends={
        Property(name="EnumerationItem", type=express_expressions_EnumItemRef, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_EnumItemRef", type=EnumerationItem, multiplicity=Multiplicity(1, 1))
    }
)
variable93: BinaryAssociation = BinaryAssociation(
    name="variable93",
    ends={
        Property(name="VARExpression95", type=express_statements_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_Assignment94", type=VARExpression, multiplicity=Multiplicity(1, 1))
    }
)
lastBit104: BinaryAssociation = BinaryAssociation(
    name="lastBit104",
    ends={
        Property(name="Expression106", type=express_expressions_BinaryIndex, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_BinaryIndex105", type=Expression, multiplicity=Multiplicity(0, 1))
    }
)
refersTo107: BinaryAssociation = BinaryAssociation(
    name="refersTo107",
    ends={
        Property(name="Indeterminate", type=express_expressions_IndeterminateRef, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_IndeterminateRef", type=Indeterminate, multiplicity=Multiplicity(1, 1))
    }
)
baseValue108: BinaryAssociation = BinaryAssociation(
    name="baseValue108",
    ends={
        Property(name="Expression109", type=express_expressions_IndexOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_IndexOperation", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
leftOperand110: BinaryAssociation = BinaryAssociation(
    name="leftOperand110",
    ends={
        Property(name="Expression111", type=express_expressions_BinaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_BinaryOperation", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
rightOperand112: BinaryAssociation = BinaryAssociation(
    name="rightOperand112",
    ends={
        Property(name="Expression114", type=express_expressions_BinaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_BinaryOperation113", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
refersTo101: BinaryAssociation = BinaryAssociation(
    name="refersTo101",
    ends={
        Property(name="SimpleValue", type=express_expressions_Literal, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_Literal", type=SimpleValue, multiplicity=Multiplicity(1, 1))
    }
)
firstBit102: BinaryAssociation = BinaryAssociation(
    name="firstBit102",
    ends={
        Property(name="Expression103", type=express_expressions_BinaryIndex, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_BinaryIndex", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
firstCode118: BinaryAssociation = BinaryAssociation(
    name="firstCode118",
    ends={
        Property(name="Expression119", type=express_expressions_StringIndex, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_StringIndex", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
lastCode120: BinaryAssociation = BinaryAssociation(
    name="lastCode120",
    ends={
        Property(name="Expression122", type=express_expressions_StringIndex, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_StringIndex121", type=Expression, multiplicity=Multiplicity(0, 1))
    }
)
resultValue123: BinaryAssociation = BinaryAssociation(
    name="resultValue123",
    ends={
        Property(name="PartialEntityValue", type=express_expressions_PartialEntityConstructor, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_PartialEntityConstructor", type=PartialEntityValue, multiplicity=Multiplicity(0, 1))
    }
)
attributeGroup124: BinaryAssociation = BinaryAssociation(
    name="attributeGroup124",
    ends={
        Property(name="SingleEntityType126", type=express_expressions_PartialEntityConstructor, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_PartialEntityConstructor125", type=SingleEntityType, multiplicity=Multiplicity(1, 1))
    }
)
bindings127: BinaryAssociation = BinaryAssociation(
    name="bindings127",
    ends={
        Property(name="AttributeBinding", type=express_expressions_PartialEntityConstructor, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_PartialEntityConstructor128", type=AttributeBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operand129: BinaryAssociation = BinaryAssociation(
    name="operand129",
    ends={
        Property(name="Expression130", type=express_expressions_Coercion, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_Coercion", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
targetType131: BinaryAssociation = BinaryAssociation(
    name="targetType131",
    ends={
        Property(name="VariableType", type=express_expressions_Coercion, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_Coercion132", type=VariableType, multiplicity=Multiplicity(1, 1))
    }
)
resultValue115: BinaryAssociation = BinaryAssociation(
    name="resultValue115",
    ends={
        Property(name="GenericAggregate", type=express_expressions_AggregateInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_AggregateInitializer", type=GenericAggregate, multiplicity=Multiplicity(0, 1))
    }
)
bindings116: BinaryAssociation = BinaryAssociation(
    name="bindings116",
    ends={
        Property(name="MemberBinding", type=express_expressions_AggregateInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_AggregateInitializer117", type=MemberBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inFunctionCall134: BinaryAssociation = BinaryAssociation(
    name="inFunctionCall134",
    ends={
        Property(name="expressions135", type=express_expressions_ActualParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="FunctionCall", type=FunctionCall, multiplicity=Multiplicity(0, 1))
    }
)
formalParameter136: BinaryAssociation = BinaryAssociation(
    name="formalParameter136",
    ends={
        Property(name="Parameter", type=express_expressions_ActualParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_ActualParameter", type=Parameter_, multiplicity=Multiplicity(1, 1))
    }
)
actualReferent137: BinaryAssociation = BinaryAssociation(
    name="actualReferent137",
    ends={
        Property(name="VARExpression139", type=express_expressions_ActualParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_ActualParameter138", type=VARExpression, multiplicity=Multiplicity(0, 1))
    }
)
actualValue140: BinaryAssociation = BinaryAssociation(
    name="actualValue140",
    ends={
        Property(name="Expression142", type=express_expressions_ActualParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_ActualParameter141", type=Expression, multiplicity=Multiplicity(0, 1))
    }
)
inProcedureCall133: BinaryAssociation = BinaryAssociation(
    name="inProcedureCall133",
    ends={
        Property(name="statements", type=express_expressions_ActualParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ProcedureCall", type=ProcedureCall, multiplicity=Multiplicity(0, 1))
    }
)
refersTo145: BinaryAssociation = BinaryAssociation(
    name="refersTo145",
    ends={
        Property(name="Attribute", type=express_expressions_AttributeRef, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_AttributeRef", type=Attribute, multiplicity=Multiplicity(1, 1))
    }
)
indexValue146: BinaryAssociation = BinaryAssociation(
    name="indexValue146",
    ends={
        Property(name="Expression147", type=express_expressions_AggregateIndex, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_AggregateIndex", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
refersTo148: BinaryAssociation = BinaryAssociation(
    name="refersTo148",
    ends={
        Property(name="SingleEntityType149", type=express_expressions_GroupRef, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_GroupRef", type=SingleEntityType, multiplicity=Multiplicity(1, 1))
    }
)
unaryOperand150: BinaryAssociation = BinaryAssociation(
    name="unaryOperand150",
    ends={
        Property(name="Expression151", type=express_expressions_UnaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_UnaryOperation", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
refersTo143: BinaryAssociation = BinaryAssociation(
    name="refersTo143",
    ends={
        Property(name="Parameter144", type=express_expressions_ParameterRef, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_ParameterRef", type=Parameter_, multiplicity=Multiplicity(1, 1))
    }
)
refersTo154: BinaryAssociation = BinaryAssociation(
    name="refersTo154",
    ends={
        Property(name="Constant", type=express_expressions_ConstantRef, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_ConstantRef", type=Constant, multiplicity=Multiplicity(1, 1))
    }
)
selectCondition155: BinaryAssociation = BinaryAssociation(
    name="selectCondition155",
    ends={
        Property(name="Expression156", type=express_expressions_QueryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_QueryExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
queryVariable157: BinaryAssociation = BinaryAssociation(
    name="queryVariable157",
    ends={
        Property(name="QueryVariable", type=express_expressions_QueryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_QueryExpression158", type=QueryVariable, multiplicity=Multiplicity(1, 1))
    }
)
aggregateOperand159: BinaryAssociation = BinaryAssociation(
    name="aggregateOperand159",
    ends={
        Property(name="Expression161", type=express_expressions_QueryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_QueryExpression160", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
attributeValue162: BinaryAssociation = BinaryAssociation(
    name="attributeValue162",
    ends={
        Property(name="Expression163", type=express_expressions_AttributeBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_AttributeBinding", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
toValue164: BinaryAssociation = BinaryAssociation(
    name="toValue164",
    ends={
        Property(name="AttributeValue", type=express_expressions_AttributeBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_AttributeBinding165", type=AttributeValue, multiplicity=Multiplicity(0, 1))
    }
)
inverseOf152: BinaryAssociation = BinaryAssociation(
    name="inverseOf152",
    ends={
        Property(name="Attribute153", type=express_expressions_UsedInRef, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_UsedInRef", type=Attribute, multiplicity=Multiplicity(1, 1))
    }
)
actualParameters169: BinaryAssociation = BinaryAssociation(
    name="actualParameters169",
    ends={
        Property(name="expressions171", type=express_expressions_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="ActualParameter170", type=ActualParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
invokesFunction172: BinaryAssociation = BinaryAssociation(
    name="invokesFunction172",
    ends={
        Property(name="Function", type=express_expressions_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_FunctionCall", type=Function, multiplicity=Multiplicity(1, 1))
    }
)
returnsResult173: BinaryAssociation = BinaryAssociation(
    name="returnsResult173",
    ends={
        Property(name="FunctionResult", type=express_expressions_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_FunctionCall174", type=FunctionResult, multiplicity=Multiplicity(1, 1))
    }
)
repetition175: BinaryAssociation = BinaryAssociation(
    name="repetition175",
    ends={
        Property(name="RepeatCount", type=express_expressions_MemberBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_MemberBinding", type=RepeatCount, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
toSlot176: BinaryAssociation = BinaryAssociation(
    name="toSlot176",
    ends={
        Property(name="ListMember", type=express_expressions_MemberBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_MemberBinding177", type=ListMember, multiplicity=Multiplicity(0, 9999))
    }
)
memberValue178: BinaryAssociation = BinaryAssociation(
    name="memberValue178",
    ends={
        Property(name="Expression180", type=express_expressions_MemberBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_MemberBinding179", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
refersTo181: BinaryAssociation = BinaryAssociation(
    name="refersTo181",
    ends={
        Property(name="NamedType", type=express_expressions_ExtentRef, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_ExtentRef", type=NamedType, multiplicity=Multiplicity(1, 1))
    }
)
attribute166: BinaryAssociation = BinaryAssociation(
    name="attribute166",
    ends={
        Property(name="ExplicitAttribute168", type=express_expressions_AttributeBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_AttributeBinding167", type=ExplicitAttribute, multiplicity=Multiplicity(1, 1))
    }
)
declaresExplicitAttribute183: BinaryAssociation = BinaryAssociation(
    name="declaresExplicitAttribute183",
    ends={
        Property(name="ExplicitAttribute184", type=express_core_SingleEntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_SingleEntityType", type=ExplicitAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
declaresAttribute185: BinaryAssociation = BinaryAssociation(
    name="declaresAttribute185",
    ends={
        Property(name="core187", type=express_core_SingleEntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="Attribute186", type=Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declaredIn188: BinaryAssociation = BinaryAssociation(
    name="declaredIn188",
    ends={
        Property(name="core190", type=express_core_SingleEntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="EntityType189", type=EntityType, multiplicity=Multiplicity(1, 1))
    }
)
equivalent191: BinaryAssociation = BinaryAssociation(
    name="equivalent191",
    ends={
        Property(name="PartialEntityType", type=express_core_SingleEntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_SingleEntityType192", type=PartialEntityType, multiplicity=Multiplicity(1, 1))
    }
)
id193: BinaryAssociation = BinaryAssociation(
    name="id193",
    ends={
        Property(name="ScopedId195", type=express_core_SingleEntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_SingleEntityType194", type=ScopedId, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
upperBound196: BinaryAssociation = BinaryAssociation(
    name="upperBound196",
    ends={
        Property(name="SizeConstraint", type=express_core_AGGREGATEType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_AGGREGATEType", type=SizeConstraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
memberType197: BinaryAssociation = BinaryAssociation(
    name="memberType197",
    ends={
        Property(name="ParameterType", type=express_core_AGGREGATEType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_AGGREGATEType198", type=ParameterType, multiplicity=Multiplicity(1, 1))
    }
)
constraint199: BinaryAssociation = BinaryAssociation(
    name="constraint199",
    ends={
        Property(name="algorithms200", type=express_core_AGGREGATEType, multiplicity=Multiplicity(1, 1)),
        Property(name="ActualStructureConstraint", type=ActualStructureConstraint, multiplicity=Multiplicity(0, 1))
    }
)
lowerBound201: BinaryAssociation = BinaryAssociation(
    name="lowerBound201",
    ends={
        Property(name="SizeConstraint203", type=express_core_AGGREGATEType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_AGGREGATEType202", type=SizeConstraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
refersTo182: BinaryAssociation = BinaryAssociation(
    name="refersTo182",
    ends={
        Property(name="NamedVariable", type=express_expressions_VariableRef, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_VariableRef", type=NamedVariable, multiplicity=Multiplicity(1, 1))
    }
)
memberType204: BinaryAssociation = BinaryAssociation(
    name="memberType204",
    ends={
        Property(name="GeneralizedType", type=express_core_GeneralAggregationType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_GeneralAggregationType", type=GeneralizedType, multiplicity=Multiplicity(1, 1))
    }
)
evaluation205: BinaryAssociation = BinaryAssociation(
    name="evaluation205",
    ends={
        Property(name="Instance", type=express_core_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_Expression", type=Instance, multiplicity=Multiplicity(0, 1))
    }
)
interpretationContext206: BinaryAssociation = BinaryAssociation(
    name="interpretationContext206",
    ends={
        Property(name="Scope", type=express_core_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_Expression207", type=Scope, multiplicity=Multiplicity(0, 1))
    }
)
dataType208: BinaryAssociation = BinaryAssociation(
    name="dataType208",
    ends={
        Property(name="DataType", type=express_core_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_Expression209", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
modelsRole210: BinaryAssociation = BinaryAssociation(
    name="modelsRole210",
    ends={
        Property(name="core211", type=express_core_InverseAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="DomainRole", type=DomainRole, multiplicity=Multiplicity(1, 1))
    }
)
explicit212: BinaryAssociation = BinaryAssociation(
    name="explicit212",
    ends={
        Property(name="core213", type=express_core_InverseAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="InvertibleAttribute", type=InvertibleAttribute, multiplicity=Multiplicity(1, 1))
    }
)
values214: BinaryAssociation = BinaryAssociation(
    name="values214",
    ends={
        Property(name="EnumerationItem215", type=express_core_EnumerationType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_EnumerationType", type=EnumerationItem, multiplicity=Multiplicity(0, 9999))
    }
)
extension218: BinaryAssociation = BinaryAssociation(
    name="extension218",
    ends={
        Property(name="core219", type=express_core_EnumerationType, multiplicity=Multiplicity(1, 1)),
        Property(name="EnumerationType", type=EnumerationType, multiplicity=Multiplicity(0, 9999))
    }
)
base220: BinaryAssociation = BinaryAssociation(
    name="base220",
    ends={
        Property(name="core222", type=express_core_EnumerationType, multiplicity=Multiplicity(1, 1)),
        Property(name="EnumerationType221", type=EnumerationType, multiplicity=Multiplicity(1, 1))
    }
)
boundExpression223: BinaryAssociation = BinaryAssociation(
    name="boundExpression223",
    ends={
        Property(name="Expression224", type=express_core_ArrayBound, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_ArrayBound", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
derivation225: BinaryAssociation = BinaryAssociation(
    name="derivation225",
    ends={
        Property(name="Expression226", type=express_core_Redeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_Redeclaration", type=Expression, multiplicity=Multiplicity(0, 1))
    }
)
restrictedType227: BinaryAssociation = BinaryAssociation(
    name="restrictedType227",
    ends={
        Property(name="AttributeType", type=express_core_Redeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_Redeclaration228", type=AttributeType, multiplicity=Multiplicity(1, 1))
    }
)
refines229: BinaryAssociation = BinaryAssociation(
    name="refines229",
    ends={
        Property(name="Redeclaration", type=express_core_Redeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_Redeclaration230", type=Redeclaration, multiplicity=Multiplicity(0, 1))
    }
)
upperBound231: BinaryAssociation = BinaryAssociation(
    name="upperBound231",
    ends={
        Property(name="SizeConstraint233", type=express_core_Redeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_Redeclaration232", type=SizeConstraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
declaredItems216: BinaryAssociation = BinaryAssociation(
    name="declaredItems216",
    ends={
        Property(name="instances", type=express_core_EnumerationType, multiplicity=Multiplicity(1, 1)),
        Property(name="EnumerationItem217", type=EnumerationItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
scope237: BinaryAssociation = BinaryAssociation(
    name="scope237",
    ends={
        Property(name="core239", type=express_core_Redeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="EntityType238", type=EntityType, multiplicity=Multiplicity(1, 1))
    }
)
originalAttribute240: BinaryAssociation = BinaryAssociation(
    name="originalAttribute240",
    ends={
        Property(name="Attribute242", type=express_core_Redeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_Redeclaration241", type=Attribute, multiplicity=Multiplicity(1, 1))
    }
)
refinedRole243: BinaryAssociation = BinaryAssociation(
    name="refinedRole243",
    ends={
        Property(name="Role", type=express_core_Redeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_Redeclaration244", type=Role, multiplicity=Multiplicity(0, 1))
    }
)
alias245: BinaryAssociation = BinaryAssociation(
    name="alias245",
    ends={
        Property(name="ScopedId247", type=express_core_Redeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_Redeclaration246", type=ScopedId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
playsRole248: BinaryAssociation = BinaryAssociation(
    name="playsRole248",
    ends={
        Property(name="core250", type=express_core_EntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="Role249", type=Role, multiplicity=Multiplicity(0, 9999))
    }
)
redeclarations251: BinaryAssociation = BinaryAssociation(
    name="redeclarations251",
    ends={
        Property(name="core253", type=express_core_EntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="Redeclaration252", type=Redeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes254: BinaryAssociation = BinaryAssociation(
    name="attributes254",
    ends={
        Property(name="core256", type=express_core_EntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="Attribute255", type=Attribute, multiplicity=Multiplicity(0, 9999))
    }
)
playsRangeRole257: BinaryAssociation = BinaryAssociation(
    name="playsRangeRole257",
    ends={
        Property(name="core258", type=express_core_EntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="RangeRole", type=RangeRole, multiplicity=Multiplicity(0, 9999))
    }
)
declares259: BinaryAssociation = BinaryAssociation(
    name="declares259",
    ends={
        Property(name="core261", type=express_core_EntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="SingleEntityType260", type=SingleEntityType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
extension262: BinaryAssociation = BinaryAssociation(
    name="extension262",
    ends={
        Property(name="rules264", type=express_core_EntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="Extent263", type=Extent, multiplicity=Multiplicity(0, 9999))
    }
)
lowerBound234: BinaryAssociation = BinaryAssociation(
    name="lowerBound234",
    ends={
        Property(name="SizeConstraint236", type=express_core_Redeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_Redeclaration235", type=SizeConstraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
invertibleAttributes265: BinaryAssociation = BinaryAssociation(
    name="invertibleAttributes265",
    ends={
        Property(name="core267", type=express_core_EntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="InvertibleAttribute266", type=InvertibleAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
playsDomainRole268: BinaryAssociation = BinaryAssociation(
    name="playsDomainRole268",
    ends={
        Property(name="core270", type=express_core_EntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="DomainRole269", type=DomainRole, multiplicity=Multiplicity(0, 9999))
    }
)
uniqueRules271: BinaryAssociation = BinaryAssociation(
    name="uniqueRules271",
    ends={
        Property(name="core272", type=express_core_EntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="UniqueRule", type=UniqueRule, multiplicity=Multiplicity(0, 9999))
    }
)
usedIn273: BinaryAssociation = BinaryAssociation(
    name="usedIn273",
    ends={
        Property(name="core275", type=express_core_EntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="InvertibleAttribute274", type=InvertibleAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
subtypeOf276: BinaryAssociation = BinaryAssociation(
    name="subtypeOf276",
    ends={
        Property(name="EntityType277", type=express_core_EntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_EntityType", type=EntityType, multiplicity=Multiplicity(0, 9999))
    }
)
instances278: BinaryAssociation = BinaryAssociation(
    name="instances278",
    ends={
        Property(name="core280", type=express_core_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="Instance279", type=Instance, multiplicity=Multiplicity(0, 9999))
    }
)
components281: BinaryAssociation = BinaryAssociation(
    name="components281",
    ends={
        Property(name="SingleEntityType282", type=express_core_PartialEntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_PartialEntityType", type=SingleEntityType, multiplicity=Multiplicity(1, 9999))
    }
)
documentation283: BinaryAssociation = BinaryAssociation(
    name="documentation283",
    ends={
        Property(name="Remark", type=Remark, multiplicity=Multiplicity(0, 9999)),
        Property(name="core284", type=express_core_Schema, multiplicity=Multiplicity(1, 1))
    }
)
interfaces285: BinaryAssociation = BinaryAssociation(
    name="interfaces285",
    ends={
        Property(name="core286", type=express_core_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="InterfacedElement", type=InterfacedElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schemaElements287: BinaryAssociation = BinaryAssociation(
    name="schemaElements287",
    ends={
        Property(name="core288", type=express_core_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="SchemaElement", type=SchemaElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interfacedElements289: BinaryAssociation = BinaryAssociation(
    name="interfacedElements289",
    ends={
        Property(name="core291", type=express_core_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="SchemaElement290", type=SchemaElement, multiplicity=Multiplicity(0, 9999))
    }
)
inverse292: BinaryAssociation = BinaryAssociation(
    name="inverse292",
    ends={
        Property(name="core293", type=express_core_InvertibleAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="InverseAttribute", type=InverseAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
rangeType294: BinaryAssociation = BinaryAssociation(
    name="rangeType294",
    ends={
        Property(name="core296", type=express_core_InvertibleAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="EntityType295", type=EntityType, multiplicity=Multiplicity(1, 9999))
    }
)
createsRelationship297: BinaryAssociation = BinaryAssociation(
    name="createsRelationship297",
    ends={
        Property(name="core298", type=express_core_InvertibleAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="Relationship", type=Relationship, multiplicity=Multiplicity(1, 1))
    }
)
referencingType299: BinaryAssociation = BinaryAssociation(
    name="referencingType299",
    ends={
        Property(name="core301", type=express_core_InvertibleAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="EntityType300", type=EntityType, multiplicity=Multiplicity(1, 9999))
    }
)
modelsRole302: BinaryAssociation = BinaryAssociation(
    name="modelsRole302",
    ends={
        Property(name="core304", type=express_core_InvertibleAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="RangeRole303", type=RangeRole, multiplicity=Multiplicity(1, 1))
    }
)
interfacingSchema308: BinaryAssociation = BinaryAssociation(
    name="interfacingSchema308",
    ends={
        Property(name="core309", type=express_core_InterfacedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Schema", type=Schema, multiplicity=Multiplicity(1, 1))
    }
)
refersTo310: BinaryAssociation = BinaryAssociation(
    name="refersTo310",
    ends={
        Property(name="core312", type=express_core_InterfacedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="SchemaElement311", type=SchemaElement, multiplicity=Multiplicity(1, 1))
    }
)
interfacedId313: BinaryAssociation = BinaryAssociation(
    name="interfacedId313",
    ends={
        Property(name="ScopedId314", type=express_core_InterfacedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_InterfacedElement", type=ScopedId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
domain315: BinaryAssociation = BinaryAssociation(
    name="domain315",
    ends={
        Property(name="core317", type=express_core_UniqueRule, multiplicity=Multiplicity(1, 1)),
        Property(name="EntityType316", type=EntityType, multiplicity=Multiplicity(1, 1))
    }
)
keyComponent318: BinaryAssociation = BinaryAssociation(
    name="keyComponent318",
    ends={
        Property(name="Attribute319", type=express_core_UniqueRule, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_UniqueRule", type=Attribute, multiplicity=Multiplicity(1, 9999))
    }
)
rangeView320: BinaryAssociation = BinaryAssociation(
    name="rangeView320",
    ends={
        Property(name="core322", type=express_core_DomainRole, multiplicity=Multiplicity(1, 1)),
        Property(name="InverseAttribute321", type=InverseAttribute, multiplicity=Multiplicity(0, 1))
    }
)
domain323: BinaryAssociation = BinaryAssociation(
    name="domain323",
    ends={
        Property(name="core325", type=express_core_DomainRole, multiplicity=Multiplicity(1, 1)),
        Property(name="EntityType324", type=EntityType, multiplicity=Multiplicity(1, 1))
    }
)
occursIn305: BinaryAssociation = BinaryAssociation(
    name="occursIn305",
    ends={
        Property(name="core307", type=express_core_GeneralizedType, multiplicity=Multiplicity(1, 1)),
        Property(name="ParameterType306", type=ParameterType, multiplicity=Multiplicity(1, 9999))
    }
)
owningEntity348: BinaryAssociation = BinaryAssociation(
    name="owningEntity348",
    ends={
        Property(name="EntityType349", type=EntityType, multiplicity=Multiplicity(1, 9999)),
        Property(name="core350", type=express_core_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
domain328: BinaryAssociation = BinaryAssociation(
    name="domain328",
    ends={
        Property(name="core330", type=express_core_DomainConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="AttributeType329", type=AttributeType, multiplicity=Multiplicity(1, 1))
    }
)
asserts331: BinaryAssociation = BinaryAssociation(
    name="asserts331",
    ends={
        Property(name="Expression332", type=express_core_DomainConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_DomainConstraint", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fundamentalType333: BinaryAssociation = BinaryAssociation(
    name="fundamentalType333",
    ends={
        Property(name="InstantiableType", type=express_core_InstantiableType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_InstantiableType", type=InstantiableType, multiplicity=Multiplicity(1, 1))
    }
)
namespace334: BinaryAssociation = BinaryAssociation(
    name="namespace334",
    ends={
        Property(name="core336", type=express_core_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Scope335", type=Scope, multiplicity=Multiplicity(1, 1))
    }
)
documentation337: BinaryAssociation = BinaryAssociation(
    name="documentation337",
    ends={
        Property(name="core339", type=express_core_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Remark338", type=Remark, multiplicity=Multiplicity(0, 9999))
    }
)
id340: BinaryAssociation = BinaryAssociation(
    name="id340",
    ends={
        Property(name="ScopedId341", type=express_core_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_NamedElement", type=ScopedId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributeType342: BinaryAssociation = BinaryAssociation(
    name="attributeType342",
    ends={
        Property(name="core344", type=express_core_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="AttributeType343", type=AttributeType, multiplicity=Multiplicity(1, 1))
    }
)
ofEntity345: BinaryAssociation = BinaryAssociation(
    name="ofEntity345",
    ends={
        Property(name="core347", type=express_core_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="SingleEntityType346", type=SingleEntityType, multiplicity=Multiplicity(1, 1))
    }
)
id326: BinaryAssociation = BinaryAssociation(
    name="id326",
    ends={
        Property(name="ScopedId327", type=express_core_DomainRole, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_DomainRole", type=ScopedId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ofType362: BinaryAssociation = BinaryAssociation(
    name="ofType362",
    ends={
        Property(name="core364", type=express_core_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="DataType363", type=DataType, multiplicity=Multiplicity(1, 9999))
    }
)
role365: BinaryAssociation = BinaryAssociation(
    name="role365",
    ends={
        Property(name="core367", type=express_core_AttributeType, multiplicity=Multiplicity(1, 1)),
        Property(name="Attribute366", type=Attribute, multiplicity=Multiplicity(0, 9999))
    }
)
constraint351: BinaryAssociation = BinaryAssociation(
    name="constraint351",
    ends={
        Property(name="algorithms352", type=express_core_GenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="ActualTypeConstraint", type=ActualTypeConstraint, multiplicity=Multiplicity(0, 1))
    }
)
stringLengthConstraint353: BinaryAssociation = BinaryAssociation(
    name="stringLengthConstraint353",
    ends={
        Property(name="LengthConstraint", type=express_core_StringType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_StringType", type=LengthConstraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specializes354: BinaryAssociation = BinaryAssociation(
    name="specializes354",
    ends={
        Property(name="AnonymousType", type=express_core_AnonymousType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_AnonymousType", type=AnonymousType, multiplicity=Multiplicity(0, 9999))
    }
)
commonElements355: BinaryAssociation = BinaryAssociation(
    name="commonElements355",
    ends={
        Property(name="core356", type=express_core_AlgorithmScope, multiplicity=Multiplicity(1, 1)),
        Property(name="CommonElement", type=CommonElement, multiplicity=Multiplicity(0, 9999))
    }
)
variables357: BinaryAssociation = BinaryAssociation(
    name="variables357",
    ends={
        Property(name="Variable358", type=express_core_AlgorithmScope, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_AlgorithmScope", type=Variable, multiplicity=Multiplicity(0, 9999))
    }
)
appearsInPopulation359: BinaryAssociation = BinaryAssociation(
    name="appearsInPopulation359",
    ends={
        Property(name="instances361", type=express_core_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="Population360", type=Population, multiplicity=Multiplicity(0, 9999))
    }
)
id378: BinaryAssociation = BinaryAssociation(
    name="id378",
    ends={
        Property(name="ScopedId379", type=express_core_RangeRole, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_RangeRole", type=ScopedId, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
constraints368: BinaryAssociation = BinaryAssociation(
    name="constraints368",
    ends={
        Property(name="core369", type=express_core_AttributeType, multiplicity=Multiplicity(1, 1)),
        Property(name="DomainConstraint", type=DomainConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
derivation370: BinaryAssociation = BinaryAssociation(
    name="derivation370",
    ends={
        Property(name="Expression371", type=express_core_DerivedAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_DerivedAttribute", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
domainView372: BinaryAssociation = BinaryAssociation(
    name="domainView372",
    ends={
        Property(name="core374", type=express_core_RangeRole, multiplicity=Multiplicity(1, 1)),
        Property(name="InvertibleAttribute373", type=InvertibleAttribute, multiplicity=Multiplicity(1, 1))
    }
)
range375: BinaryAssociation = BinaryAssociation(
    name="range375",
    ends={
        Property(name="core377", type=express_core_RangeRole, multiplicity=Multiplicity(1, 1)),
        Property(name="EntityType376", type=EntityType, multiplicity=Multiplicity(1, 1))
    }
)
inRelationship388: BinaryAssociation = BinaryAssociation(
    name="inRelationship388",
    ends={
        Property(name="core390", type=express_core_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="Relationship389", type=Relationship, multiplicity=Multiplicity(1, 1))
    }
)
describesSchema380: BinaryAssociation = BinaryAssociation(
    name="describesSchema380",
    ends={
        Property(name="core382", type=express_core_Remark, multiplicity=Multiplicity(1, 1)),
        Property(name="Schema381", type=Schema, multiplicity=Multiplicity(0, 9999))
    }
)
appearsIn383: BinaryAssociation = BinaryAssociation(
    name="appearsIn383",
    ends={
        Property(name="core385", type=express_core_Remark, multiplicity=Multiplicity(1, 1)),
        Property(name="Scope384", type=Scope, multiplicity=Multiplicity(1, 1))
    }
)
describesElement386: BinaryAssociation = BinaryAssociation(
    name="describesElement386",
    ends={
        Property(name="core387", type=express_core_Remark, multiplicity=Multiplicity(1, 1)),
        Property(name="NamedElement", type=NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
underlyingType399: BinaryAssociation = BinaryAssociation(
    name="underlyingType399",
    ends={
        Property(name="ConcreteType", type=express_core_SpecializedType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_SpecializedType", type=ConcreteType, multiplicity=Multiplicity(1, 1))
    }
)
ofEntity391: BinaryAssociation = BinaryAssociation(
    name="ofEntity391",
    ends={
        Property(name="core393", type=express_core_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="EntityType392", type=EntityType, multiplicity=Multiplicity(1, 9999))
    }
)
upperBound394: BinaryAssociation = BinaryAssociation(
    name="upperBound394",
    ends={
        Property(name="SizeConstraint395", type=express_core_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_Role", type=SizeConstraint, multiplicity=Multiplicity(0, 1))
    }
)
lowerBound396: BinaryAssociation = BinaryAssociation(
    name="lowerBound396",
    ends={
        Property(name="SizeConstraint398", type=express_core_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_Role397", type=SizeConstraint, multiplicity=Multiplicity(0, 1))
    }
)
roles406: BinaryAssociation = BinaryAssociation(
    name="roles406",
    ends={
        Property(name="core408", type=express_core_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="Role407", type=Role, multiplicity=Multiplicity(2, 2))
    }
)
hiIndex400: BinaryAssociation = BinaryAssociation(
    name="hiIndex400",
    ends={
        Property(name="ArrayBound", type=express_core_GeneralARRAYType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_GeneralARRAYType", type=ArrayBound, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
loIndex401: BinaryAssociation = BinaryAssociation(
    name="loIndex401",
    ends={
        Property(name="ArrayBound403", type=express_core_GeneralARRAYType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_GeneralARRAYType402", type=ArrayBound, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
domain404: BinaryAssociation = BinaryAssociation(
    name="domain404",
    ends={
        Property(name="DomainRole405", type=express_core_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_Relationship", type=DomainRole, multiplicity=Multiplicity(1, 1))
    }
)
basedOn409: BinaryAssociation = BinaryAssociation(
    name="basedOn409",
    ends={
        Property(name="core411", type=express_core_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="InvertibleAttribute410", type=InvertibleAttribute, multiplicity=Multiplicity(1, 1))
    }
)
range412: BinaryAssociation = BinaryAssociation(
    name="range412",
    ends={
        Property(name="RangeRole414", type=express_core_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_Relationship413", type=RangeRole, multiplicity=Multiplicity(1, 1))
    }
)
localElements415: BinaryAssociation = BinaryAssociation(
    name="localElements415",
    ends={
        Property(name="LocalElement", type=express_core_LocalScope, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_LocalScope", type=LocalElement, multiplicity=Multiplicity(0, 9999))
    }
)
upperBound425: BinaryAssociation = BinaryAssociation(
    name="upperBound425",
    ends={
        Property(name="SizeConstraint427", type=express_core_AggregationType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_AggregationType426", type=SizeConstraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
namedElements428: BinaryAssociation = BinaryAssociation(
    name="namedElements428",
    ends={
        Property(name="core430", type=express_core_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="NamedElement429", type=NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
includesRemarks431: BinaryAssociation = BinaryAssociation(
    name="includesRemarks431",
    ends={
        Property(name="core433", type=express_core_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="Remark432", type=Remark, multiplicity=Multiplicity(0, 9999))
    }
)
contains434: BinaryAssociation = BinaryAssociation(
    name="contains434",
    ends={
        Property(name="core436", type=express_core_ParameterType, multiplicity=Multiplicity(1, 1)),
        Property(name="GeneralizedType435", type=GeneralizedType, multiplicity=Multiplicity(0, 9999))
    }
)
instantiates416: BinaryAssociation = BinaryAssociation(
    name="instantiates416",
    ends={
        Property(name="core417", type=express_core_NamedType, multiplicity=Multiplicity(1, 1)),
        Property(name="SelectType", type=SelectType, multiplicity=Multiplicity(0, 9999))
    }
)
domainRules418: BinaryAssociation = BinaryAssociation(
    name="domainRules418",
    ends={
        Property(name="DomainRule", type=express_core_NamedType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_NamedType", type=DomainRule, multiplicity=Multiplicity(0, 9999))
    }
)
allowedTypes437: BinaryAssociation = BinaryAssociation(
    name="allowedTypes437",
    ends={
        Property(name="core439", type=express_core_SelectType, multiplicity=Multiplicity(1, 1)),
        Property(name="NamedType438", type=NamedType, multiplicity=Multiplicity(0, 9999))
    }
)
binaryLengthConstraint419: BinaryAssociation = BinaryAssociation(
    name="binaryLengthConstraint419",
    ends={
        Property(name="LengthConstraint420", type=express_core_BinaryType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_BinaryType", type=LengthConstraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definingScope421: BinaryAssociation = BinaryAssociation(
    name="definingScope421",
    ends={
        Property(name="Scope422", type=express_core_ScopedId, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_ScopedId", type=Scope, multiplicity=Multiplicity(1, 1))
    }
)
lowerBound423: BinaryAssociation = BinaryAssociation(
    name="lowerBound423",
    ends={
        Property(name="SizeConstraint424", type=express_core_AggregationType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_AggregationType", type=SizeConstraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
scope448: BinaryAssociation = BinaryAssociation(
    name="scope448",
    ends={
        Property(name="Algorithm", type=express_core_ActualType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_ActualType", type=Algorithm, multiplicity=Multiplicity(1, 1))
    }
)
localScope449: BinaryAssociation = BinaryAssociation(
    name="localScope449",
    ends={
        Property(name="core450", type=express_core_CommonElement, multiplicity=Multiplicity(1, 1)),
        Property(name="AlgorithmScope", type=AlgorithmScope, multiplicity=Multiplicity(0, 1))
    }
)
referencedAs451: BinaryAssociation = BinaryAssociation(
    name="referencedAs451",
    ends={
        Property(name="core453", type=express_core_SchemaElement, multiplicity=Multiplicity(1, 1)),
        Property(name="InterfacedElement452", type=InterfacedElement, multiplicity=Multiplicity(0, 9999))
    }
)
referencedIn454: BinaryAssociation = BinaryAssociation(
    name="referencedIn454",
    ends={
        Property(name="core456", type=express_core_SchemaElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Schema455", type=Schema, multiplicity=Multiplicity(0, 9999))
    }
)
extension440: BinaryAssociation = BinaryAssociation(
    name="extension440",
    ends={
        Property(name="core442", type=express_core_SelectType, multiplicity=Multiplicity(1, 1)),
        Property(name="SelectType441", type=SelectType, multiplicity=Multiplicity(0, 9999))
    }
)
base443: BinaryAssociation = BinaryAssociation(
    name="base443",
    ends={
        Property(name="core445", type=express_core_SelectType, multiplicity=Multiplicity(1, 1)),
        Property(name="SelectType444", type=SelectType, multiplicity=Multiplicity(1, 1))
    }
)
selectList446: BinaryAssociation = BinaryAssociation(
    name="selectList446",
    ends={
        Property(name="NamedType447", type=express_core_SelectType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_SelectType", type=NamedType, multiplicity=Multiplicity(0, 9999))
    }
)
matchingType467: BinaryAssociation = BinaryAssociation(
    name="matchingType467",
    ends={
        Property(name="core468", type=express_algorithms_ActualTypeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="GenericType", type=GenericType, multiplicity=Multiplicity(1, 1))
    }
)
requiredType469: BinaryAssociation = BinaryAssociation(
    name="requiredType469",
    ends={
        Property(name="ActualDataType", type=express_algorithms_ActualTypeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="express_algorithms_ActualTypeConstraint", type=ActualDataType, multiplicity=Multiplicity(1, 1))
    }
)
definedIn457: BinaryAssociation = BinaryAssociation(
    name="definedIn457",
    ends={
        Property(name="core459", type=express_core_SchemaElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Schema458", type=Schema, multiplicity=Multiplicity(0, 1))
    }
)
memberType460: BinaryAssociation = BinaryAssociation(
    name="memberType460",
    ends={
        Property(name="InstantiableType461", type=express_core_ConcreteAggregationType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_ConcreteAggregationType", type=InstantiableType, multiplicity=Multiplicity(1, 1))
    }
)
loIndex462: BinaryAssociation = BinaryAssociation(
    name="loIndex462",
    ends={
        Property(name="ArrayBound463", type=express_core_ARRAYType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_ARRAYType", type=ArrayBound, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
hiIndex464: BinaryAssociation = BinaryAssociation(
    name="hiIndex464",
    ends={
        Property(name="ArrayBound466", type=express_core_ARRAYType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_ARRAYType465", type=ArrayBound, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
refersTo476: BinaryAssociation = BinaryAssociation(
    name="refersTo476",
    ends={
        Property(name="ActualDataType477", type=express_algorithms_ActualGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_algorithms_ActualGenericType", type=ActualDataType, multiplicity=Multiplicity(1, 1))
    }
)
inBlock478: BinaryAssociation = BinaryAssociation(
    name="inBlock478",
    ends={
        Property(name="statements479", type=express_algorithms_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="StatementBlock", type=StatementBlock, multiplicity=Multiplicity(0, 1))
    }
)
bodyStatementsSkipStatement480: BinaryAssociation = BinaryAssociation(
    name="bodyStatementsSkipStatement480",
    ends={
        Property(name="SkipStatement", type=express_algorithms_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="express_algorithms_Statement", type=SkipStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyStatementsEscapeStatement481: BinaryAssociation = BinaryAssociation(
    name="bodyStatementsEscapeStatement481",
    ends={
        Property(name="EscapeStatement", type=express_algorithms_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="express_algorithms_Statement482", type=EscapeStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
controlledBy483: BinaryAssociation = BinaryAssociation(
    name="controlledBy483",
    ends={
        Property(name="statements484", type=express_algorithms_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="RepeatStatement", type=RepeatStatement, multiplicity=Multiplicity(0, 1))
    }
)
result470: BinaryAssociation = BinaryAssociation(
    name="result470",
    ends={
        Property(name="FunctionResult471", type=express_algorithms_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="express_algorithms_Function", type=FunctionResult, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable472: BinaryAssociation = BinaryAssociation(
    name="variable472",
    ends={
        Property(name="algorithms473", type=express_algorithms_InParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="InVariable", type=InVariable, multiplicity=Multiplicity(1, 1))
    }
)
initialValue474: BinaryAssociation = BinaryAssociation(
    name="initialValue474",
    ends={
        Property(name="Expression475", type=express_algorithms_LocalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="express_algorithms_LocalVariable", type=Expression, multiplicity=Multiplicity(0, 1))
    }
)
hiIndex492: BinaryAssociation = BinaryAssociation(
    name="hiIndex492",
    ends={
        Property(name="ArrayBound493", type=express_algorithms_ActualARRAYType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_algorithms_ActualARRAYType", type=ArrayBound, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
loIndex494: BinaryAssociation = BinaryAssociation(
    name="loIndex494",
    ends={
        Property(name="ArrayBound496", type=express_algorithms_ActualARRAYType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_algorithms_ActualARRAYType495", type=ArrayBound, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
upperBound497: BinaryAssociation = BinaryAssociation(
    name="upperBound497",
    ends={
        Property(name="SizeConstraint498", type=express_algorithms_ActualAGGREGATEType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_algorithms_ActualAGGREGATEType", type=SizeConstraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
refersTo499: BinaryAssociation = BinaryAssociation(
    name="refersTo499",
    ends={
        Property(name="ActualStructure", type=express_algorithms_ActualAGGREGATEType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_algorithms_ActualAGGREGATEType500", type=ActualStructure, multiplicity=Multiplicity(1, 1))
    }
)
memberType501: BinaryAssociation = BinaryAssociation(
    name="memberType501",
    ends={
        Property(name="VariableType503", type=express_algorithms_ActualAGGREGATEType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_algorithms_ActualAGGREGATEType502", type=VariableType, multiplicity=Multiplicity(1, 1))
    }
)
lowerBound504: BinaryAssociation = BinaryAssociation(
    name="lowerBound504",
    ends={
        Property(name="SizeConstraint506", type=express_algorithms_ActualAGGREGATEType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_algorithms_ActualAGGREGATEType505", type=SizeConstraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
implements485: BinaryAssociation = BinaryAssociation(
    name="implements485",
    ends={
        Property(name="algorithms487", type=express_algorithms_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="Algorithm486", type=Algorithm, multiplicity=Multiplicity(0, 1))
    }
)
variableType488: BinaryAssociation = BinaryAssociation(
    name="variableType488",
    ends={
        Property(name="VariableType489", type=express_algorithms_NamedVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="express_algorithms_NamedVariable", type=VariableType, multiplicity=Multiplicity(1, 1))
    }
)
source490: BinaryAssociation = BinaryAssociation(
    name="source490",
    ends={
        Property(name="algorithms491", type=express_algorithms_InVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="InParameter", type=InParameter, multiplicity=Multiplicity(1, 1))
    }
)
matchingStructure515: BinaryAssociation = BinaryAssociation(
    name="matchingStructure515",
    ends={
        Property(name="core516", type=express_algorithms_ActualStructureConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="AGGREGATEType", type=AGGREGATEType, multiplicity=Multiplicity(1, 1))
    }
)
requiredStructure517: BinaryAssociation = BinaryAssociation(
    name="requiredStructure517",
    ends={
        Property(name="ActualStructure518", type=express_algorithms_ActualStructureConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="express_algorithms_ActualStructureConstraint", type=ActualStructure, multiplicity=Multiplicity(1, 1))
    }
)
body519: BinaryAssociation = BinaryAssociation(
    name="body519",
    ends={
        Property(name="algorithms521", type=express_algorithms_Algorithm, multiplicity=Multiplicity(1, 1)),
        Property(name="Statement520", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameters522: BinaryAssociation = BinaryAssociation(
    name="formalParameters522",
    ends={
        Property(name="Parameter523", type=express_algorithms_Algorithm, multiplicity=Multiplicity(1, 1)),
        Property(name="express_algorithms_Algorithm", type=Parameter_, multiplicity=Multiplicity(0, 9999))
    }
)
structureConstraints507: BinaryAssociation = BinaryAssociation(
    name="structureConstraints507",
    ends={
        Property(name="ActualStructureConstraint508", type=express_algorithms_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="express_algorithms_Parameter", type=ActualStructureConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeConstraints509: BinaryAssociation = BinaryAssociation(
    name="typeConstraints509",
    ends={
        Property(name="ActualTypeConstraint511", type=express_algorithms_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="express_algorithms_Parameter510", type=ActualTypeConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
formalParameterType512: BinaryAssociation = BinaryAssociation(
    name="formalParameterType512",
    ends={
        Property(name="ParameterType514", type=express_algorithms_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="express_algorithms_Parameter513", type=ParameterType, multiplicity=Multiplicity(1, 1))
    }
)
label527: BinaryAssociation = BinaryAssociation(
    name="label527",
    ends={
        Property(name="ScopedId529", type=express_algorithms_GenericElement, multiplicity=Multiplicity(1, 1)),
        Property(name="express_algorithms_GenericElement528", type=ScopedId, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
actualValue530: BinaryAssociation = BinaryAssociation(
    name="actualValue530",
    ends={
        Property(name="Instance531", type=express_instances_AttributeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_AttributeValue", type=Instance, multiplicity=Multiplicity(0, 1))
    }
)
attribute532: BinaryAssociation = BinaryAssociation(
    name="attribute532",
    ends={
        Property(name="ExplicitAttribute534", type=express_instances_AttributeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_AttributeValue533", type=ExplicitAttribute, multiplicity=Multiplicity(1, 1))
    }
)
memberSlot535: BinaryAssociation = BinaryAssociation(
    name="memberSlot535",
    ends={
        Property(name="ArrayMember", type=express_instances_ARRAYValue, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_ARRAYValue", type=ArrayMember, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
memberType524: BinaryAssociation = BinaryAssociation(
    name="memberType524",
    ends={
        Property(name="ActualType", type=express_algorithms_ActualAggregationType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_algorithms_ActualAggregationType", type=ActualType, multiplicity=Multiplicity(1, 1))
    }
)
source525: BinaryAssociation = BinaryAssociation(
    name="source525",
    ends={
        Property(name="Parameter526", type=express_algorithms_GenericElement, multiplicity=Multiplicity(1, 1)),
        Property(name="express_algorithms_GenericElement", type=Parameter_, multiplicity=Multiplicity(1, 1))
    }
)
state541: BinaryAssociation = BinaryAssociation(
    name="state541",
    ends={
        Property(name="instances542", type=express_instances_EntityInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="EntityValue", type=EntityValue, multiplicity=Multiplicity(1, 1))
    }
)
instanceOf543: BinaryAssociation = BinaryAssociation(
    name="instanceOf543",
    ends={
        Property(name="EntityType544", type=express_instances_EntityInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_EntityInstance", type=EntityType, multiplicity=Multiplicity(1, 9999))
    }
)
valueExpression545: BinaryAssociation = BinaryAssociation(
    name="valueExpression545",
    ends={
        Property(name="Expression546", type=express_instances_Constant, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_Constant", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
actualValue547: BinaryAssociation = BinaryAssociation(
    name="actualValue547",
    ends={
        Property(name="Instance549", type=express_instances_Constant, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_Constant548", type=Instance, multiplicity=Multiplicity(0, 1))
    }
)
dataType550: BinaryAssociation = BinaryAssociation(
    name="dataType550",
    ends={
        Property(name="InstantiableType552", type=express_instances_Constant, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_Constant551", type=InstantiableType, multiplicity=Multiplicity(1, 1))
    }
)
refersTo536: BinaryAssociation = BinaryAssociation(
    name="refersTo536",
    ends={
        Property(name="Attribute537", type=express_instances_RoleName, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_RoleName", type=Attribute, multiplicity=Multiplicity(1, 1))
    }
)
satisfiesType553: BinaryAssociation = BinaryAssociation(
    name="satisfiesType553",
    ends={
        Property(name="SelectType554", type=express_instances_TypedInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_TypedInstance", type=SelectType, multiplicity=Multiplicity(0, 9999))
    }
)
represents538: BinaryAssociation = BinaryAssociation(
    name="represents538",
    ends={
        Property(name="ScopedId540", type=express_instances_RoleName, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_RoleName539", type=ScopedId, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
memberValue555: BinaryAssociation = BinaryAssociation(
    name="memberValue555",
    ends={
        Property(name="Instance556", type=express_instances_ListMember, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_ListMember", type=Instance, multiplicity=Multiplicity(1, 1))
    }
)
memberValue557: BinaryAssociation = BinaryAssociation(
    name="memberValue557",
    ends={
        Property(name="Instance558", type=express_instances_BagMember, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_BagMember", type=Instance, multiplicity=Multiplicity(1, 1))
    }
)
equivalent559: BinaryAssociation = BinaryAssociation(
    name="equivalent559",
    ends={
        Property(name="PartialEntityValue560", type=express_instances_SingleEntityValue, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_SingleEntityValue", type=PartialEntityValue, multiplicity=Multiplicity(1, 1))
    }
)
ofType561: BinaryAssociation = BinaryAssociation(
    name="ofType561",
    ends={
        Property(name="SingleEntityType563", type=express_instances_SingleEntityValue, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_SingleEntityValue562", type=SingleEntityType, multiplicity=Multiplicity(1, 1))
    }
)
properties564: BinaryAssociation = BinaryAssociation(
    name="properties564",
    ends={
        Property(name="AttributeValue566", type=express_instances_SingleEntityValue, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_SingleEntityValue565", type=AttributeValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
characterizingType567: BinaryAssociation = BinaryAssociation(
    name="characterizingType567",
    ends={
        Property(name="EntityType568", type=express_instances_SingleLeafInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_SingleLeafInstance", type=EntityType, multiplicity=Multiplicity(1, 1))
    }
)
fundamentalValue569: BinaryAssociation = BinaryAssociation(
    name="fundamentalValue569",
    ends={
        Property(name="ConcreteValue", type=express_instances_SpecializedValue, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_SpecializedValue", type=ConcreteValue, multiplicity=Multiplicity(1, 1))
    }
)
memberSlot570: BinaryAssociation = BinaryAssociation(
    name="memberSlot570",
    ends={
        Property(name="BagMember", type=express_instances_BAGValue, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_BAGValue", type=BagMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declaredIn571: BinaryAssociation = BinaryAssociation(
    name="declaredIn571",
    ends={
        Property(name="core573", type=express_instances_EnumerationItem, multiplicity=Multiplicity(1, 1)),
        Property(name="EnumerationType572", type=EnumerationType, multiplicity=Multiplicity(1, 1))
    }
)
correspondsTo574: BinaryAssociation = BinaryAssociation(
    name="correspondsTo574",
    ends={
        Property(name="EntityType575", type=express_instances_EntityValue, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_EntityValue", type=EntityType, multiplicity=Multiplicity(1, 9999))
    }
)
describes576: BinaryAssociation = BinaryAssociation(
    name="describes576",
    ends={
        Property(name="instances578", type=express_instances_EntityValue, multiplicity=Multiplicity(1, 1)),
        Property(name="EntityInstance577", type=EntityInstance, multiplicity=Multiplicity(0, 9999))
    }
)
memberValue579: BinaryAssociation = BinaryAssociation(
    name="memberValue579",
    ends={
        Property(name="Instance580", type=express_instances_SETValue, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_SETValue", type=Instance, multiplicity=Multiplicity(0, 9999))
    }
)
memberValue581: BinaryAssociation = BinaryAssociation(
    name="memberValue581",
    ends={
        Property(name="Instance582", type=express_instances_ArrayMember, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_ArrayMember", type=Instance, multiplicity=Multiplicity(0, 1))
    }
)
compositionEntityInstance583: BinaryAssociation = BinaryAssociation(
    name="compositionEntityInstance583",
    ends={
        Property(name="EntityInstance584", type=express_instances_Population, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_Population", type=EntityInstance, multiplicity=Multiplicity(0, 9999))
    }
)
compositionInstance585: BinaryAssociation = BinaryAssociation(
    name="compositionInstance585",
    ends={
        Property(name="core587", type=express_instances_Population, multiplicity=Multiplicity(1, 1)),
        Property(name="Instance586", type=Instance, multiplicity=Multiplicity(0, 9999))
    }
)
governingSchema588: BinaryAssociation = BinaryAssociation(
    name="governingSchema588",
    ends={
        Property(name="Schema590", type=express_instances_Population, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_Population589", type=Schema, multiplicity=Multiplicity(0, 9999))
    }
)
memberSlot591: BinaryAssociation = BinaryAssociation(
    name="memberSlot591",
    ends={
        Property(name="ListMember592", type=express_instances_LISTValue, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_LISTValue", type=ListMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refersTo593: BinaryAssociation = BinaryAssociation(
    name="refersTo593",
    ends={
        Property(name="NamedType594", type=express_instances_TypeName, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_TypeName", type=NamedType, multiplicity=Multiplicity(1, 1))
    }
)
represents595: BinaryAssociation = BinaryAssociation(
    name="represents595",
    ends={
        Property(name="ScopedId597", type=express_instances_TypeName, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_TypeName596", type=ScopedId, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
components598: BinaryAssociation = BinaryAssociation(
    name="components598",
    ends={
        Property(name="SingleEntityValue", type=express_instances_PartialEntityValue, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_PartialEntityValue", type=SingleEntityValue, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_express_rules_ONEOFConstraint_SubtypeConstraint = Generalization(general=SubtypeConstraint, specific=express_rules_ONEOFConstraint)
gen_express_rules_SupertypeRule_CommonElement = Generalization(general=CommonElement, specific=express_rules_SupertypeRule)
gen_express_rules_TOTAL_OVERConstraint_SubtypeConstraint = Generalization(general=SubtypeConstraint, specific=express_rules_TOTAL_OVERConstraint)
gen_express_rules_ANDConstraint_SubtypeConstraint = Generalization(general=SubtypeConstraint, specific=express_rules_ANDConstraint)
gen_express_rules_GlobalRule_core_SchemaElement = Generalization(general=core_SchemaElement, specific=express_rules_GlobalRule)
gen_express_rules_GlobalRule_core_AlgorithmScope = Generalization(general=core_AlgorithmScope, specific=express_rules_GlobalRule)
gen_express_rules_Extent_SETValue = Generalization(general=SETValue, specific=express_rules_Extent)
gen_express_statements_SkipStatement_ControlStatement = Generalization(general=ControlStatement, specific=express_statements_SkipStatement)
gen_express_statements_AliasStatement_algorithms_Statement = Generalization(general=algorithms_Statement, specific=express_statements_AliasStatement)
gen_express_statements_AliasStatement_core_LocalScope = Generalization(general=core_LocalScope, specific=express_statements_AliasStatement)
gen_express_rules_NamedRule_LocalElement = Generalization(general=LocalElement, specific=express_rules_NamedRule)
gen_express_statements_ProcedureCall_Statement = Generalization(general=Statement, specific=express_statements_ProcedureCall)
gen_express_statements_NullStatement_ControlStatement = Generalization(general=ControlStatement, specific=express_statements_NullStatement)
gen_express_statements_AttributeCell_VARExpression = Generalization(general=VARExpression, specific=express_statements_AttributeCell)
gen_express_statements_ControlVariable_NamedVariable = Generalization(general=NamedVariable, specific=express_statements_ControlVariable)
gen_express_statements_AliasVariable_algorithms_NamedVariable = Generalization(general=algorithms_NamedVariable, specific=express_statements_AliasVariable)
gen_express_statements_AliasVariable_algorithms_VARVariable = Generalization(general=algorithms_VARVariable, specific=express_statements_AliasVariable)
gen_express_statements_ControlStatement_Statement = Generalization(general=Statement, specific=express_statements_ControlStatement)
gen_express_statements_VARCell_VARExpression = Generalization(general=VARExpression, specific=express_statements_VARCell)
gen_express_statements_StatementBlock_Statement = Generalization(general=Statement, specific=express_statements_StatementBlock)
gen_express_statements_MemberCell_VARExpression = Generalization(general=VARExpression, specific=express_statements_MemberCell)
gen_express_statements_RepeatStatement_algorithms_Statement = Generalization(general=algorithms_Statement, specific=express_statements_RepeatStatement)
gen_express_statements_RepeatStatement_core_LocalScope = Generalization(general=core_LocalScope, specific=express_statements_RepeatStatement)
gen_express_statements_GroupCell_VARExpression = Generalization(general=VARExpression, specific=express_statements_GroupCell)
gen_express_statements_IfStatement_Statement = Generalization(general=Statement, specific=express_statements_IfStatement)
gen_express_statements_EscapeStatement_ControlStatement = Generalization(general=ControlStatement, specific=express_statements_EscapeStatement)
gen_express_statements_ReturnStatement_ControlStatement = Generalization(general=ControlStatement, specific=express_statements_ReturnStatement)
gen_express_statements_Assignment_Statement = Generalization(general=Statement, specific=express_statements_Assignment)
gen_express_statements_VariableCell_VARExpression = Generalization(general=VARExpression, specific=express_statements_VariableCell)
gen_express_statements_CaseStatement_Statement = Generalization(general=Statement, specific=express_statements_CaseStatement)
gen_express_expressions_Selector_Expression = Generalization(general=Expression, specific=express_expressions_Selector)
gen_express_expressions_EnumItemRef_Primary = Generalization(general=Primary, specific=express_expressions_EnumItemRef)
gen_express_expressions_IndeterminateRef_Primary = Generalization(general=Primary, specific=express_expressions_IndeterminateRef)
gen_express_expressions_SELFRef_Primary = Generalization(general=Primary, specific=express_expressions_SELFRef)
gen_express_expressions_IndexOperation_Expression = Generalization(general=Expression, specific=express_expressions_IndexOperation)
gen_express_expressions_BinaryOperation_Operation = Generalization(general=Operation, specific=express_expressions_BinaryOperation)
gen_express_expressions_Literal_Primary = Generalization(general=Primary, specific=express_expressions_Literal)
gen_express_expressions_BinaryIndex_IndexOperation = Generalization(general=IndexOperation, specific=express_expressions_BinaryIndex)
gen_express_expressions_PartialEntityConstructor_Expression = Generalization(general=Expression, specific=express_expressions_PartialEntityConstructor)
gen_express_expressions_Coercion_Operation = Generalization(general=Operation, specific=express_expressions_Coercion)
gen_express_expressions_AggregateInitializer_Expression = Generalization(general=Expression, specific=express_expressions_AggregateInitializer)
gen_express_expressions_Primary_Expression = Generalization(general=Expression, specific=express_expressions_Primary)
gen_express_expressions_StringIndex_IndexOperation = Generalization(general=IndexOperation, specific=express_expressions_StringIndex)
gen_express_expressions_ParameterRef_Primary = Generalization(general=Primary, specific=express_expressions_ParameterRef)
gen_express_expressions_AttributeRef_Selector = Generalization(general=Selector, specific=express_expressions_AttributeRef)
gen_express_expressions_AggregateIndex_IndexOperation = Generalization(general=IndexOperation, specific=express_expressions_AggregateIndex)
gen_express_expressions_GroupRef_Selector = Generalization(general=Selector, specific=express_expressions_GroupRef)
gen_express_expressions_UnaryOperation_Operation = Generalization(general=Operation, specific=express_expressions_UnaryOperation)
gen_express_expressions_UsedInRef_Selector = Generalization(general=Selector, specific=express_expressions_UsedInRef)
gen_express_expressions_ConstantRef_Primary = Generalization(general=Primary, specific=express_expressions_ConstantRef)
gen_express_expressions_QueryExpression_core_LocalScope = Generalization(general=core_LocalScope, specific=express_expressions_QueryExpression)
gen_express_expressions_QueryExpression_core_Expression = Generalization(general=core_Expression, specific=express_expressions_QueryExpression)
gen_express_expressions_QueryVariable_NamedVariable = Generalization(general=NamedVariable, specific=express_expressions_QueryVariable)
gen_express_expressions_Operation_Expression = Generalization(general=Expression, specific=express_expressions_Operation)
gen_express_expressions_FunctionCall_Expression = Generalization(general=Expression, specific=express_expressions_FunctionCall)
gen_express_expressions_ExtentRef_Primary = Generalization(general=Primary, specific=express_expressions_ExtentRef)
gen_express_expressions_VariableRef_Primary = Generalization(general=Primary, specific=express_expressions_VariableRef)
gen_express_core_TypeElement_NamedElement = Generalization(general=NamedElement, specific=express_core_TypeElement)
gen_express_core_AGGREGATEType_GeneralizedType = Generalization(general=GeneralizedType, specific=express_core_AGGREGATEType)
gen_express_core_DomainRule_core_DomainConstraint = Generalization(general=core_DomainConstraint, specific=express_core_DomainRule)
gen_express_core_DomainRule_core_TypeElement = Generalization(general=core_TypeElement, specific=express_core_DomainRule)
gen_express_core_GeneralAggregationType_core_GeneralizedType = Generalization(general=core_GeneralizedType, specific=express_core_GeneralAggregationType)
gen_express_core_GeneralAggregationType_core_AggregationType = Generalization(general=core_AggregationType, specific=express_core_GeneralAggregationType)
gen_express_core_ConcreteType_InstantiableType = Generalization(general=InstantiableType, specific=express_core_ConcreteType)
gen_express_core_InverseAttribute_Attribute = Generalization(general=Attribute, specific=express_core_InverseAttribute)
gen_express_core_EnumerationType_DefinedType = Generalization(general=DefinedType, specific=express_core_EnumerationType)
gen_express_core_GeneralBAGType_GeneralAggregationType = Generalization(general=GeneralAggregationType, specific=express_core_GeneralBAGType)
gen_express_core_VariableType_core_DataType = Generalization(general=core_DataType, specific=express_core_VariableType)
gen_express_core_VariableType_core_AttributeType = Generalization(general=core_AttributeType, specific=express_core_VariableType)
gen_express_core_GeneralSETType_GeneralAggregationType = Generalization(general=GeneralAggregationType, specific=express_core_GeneralSETType)
gen_express_core_LISTType_ConcreteAggregationType = Generalization(general=ConcreteAggregationType, specific=express_core_LISTType)
gen_express_core_EntityType_core_NamedType = Generalization(general=core_NamedType, specific=express_core_EntityType)
gen_express_core_EntityType_core_InstantiableType = Generalization(general=core_InstantiableType, specific=express_core_EntityType)
gen_express_core_PartialEntityType_DataType = Generalization(general=DataType, specific=express_core_PartialEntityType)
gen_express_core_InvertibleAttribute_ExplicitAttribute = Generalization(general=ExplicitAttribute, specific=express_core_InvertibleAttribute)
gen_express_core_GeneralizedType_core_ParameterType = Generalization(general=core_ParameterType, specific=express_core_GeneralizedType)
gen_express_core_GeneralizedType_core_AttributeType = Generalization(general=core_AttributeType, specific=express_core_GeneralizedType)
gen_express_core_Schema_Scope = Generalization(general=Scope, specific=express_core_Schema)
gen_express_core_NumericType_SimpleType = Generalization(general=SimpleType, specific=express_core_NumericType)
gen_express_core_DefinedType_core_NamedType = Generalization(general=core_NamedType, specific=express_core_DefinedType)
gen_express_core_DefinedType_core_ConcreteType = Generalization(general=core_ConcreteType, specific=express_core_DefinedType)
gen_express_core_UniqueRule_TypeElement = Generalization(general=TypeElement, specific=express_core_UniqueRule)
gen_express_core_DomainRole_Role = Generalization(general=Role, specific=express_core_DomainRole)
gen_express_core_BAGType_ConcreteAggregationType = Generalization(general=ConcreteAggregationType, specific=express_core_BAGType)
gen_express_core_RealType_NumericType = Generalization(general=NumericType, specific=express_core_RealType)
gen_express_core_InstantiableType_core_ParameterType = Generalization(general=core_ParameterType, specific=express_core_InstantiableType)
gen_express_core_InstantiableType_core_VariableType = Generalization(general=core_VariableType, specific=express_core_InstantiableType)
gen_express_core_GeneralLISTType_GeneralAggregationType = Generalization(general=GeneralAggregationType, specific=express_core_GeneralLISTType)
gen_express_core_Attribute_TypeElement = Generalization(general=TypeElement, specific=express_core_Attribute)
gen_express_core_LogicType_SimpleType = Generalization(general=SimpleType, specific=express_core_LogicType)
gen_express_core_GenericType_GeneralizedType = Generalization(general=GeneralizedType, specific=express_core_GenericType)
gen_express_core_StringType_SimpleType = Generalization(general=SimpleType, specific=express_core_StringType)
gen_express_core_AnonymousType_core_ConcreteType = Generalization(general=core_ConcreteType, specific=express_core_AnonymousType)
gen_express_core_AnonymousType_core_InstantiableType = Generalization(general=core_InstantiableType, specific=express_core_AnonymousType)
gen_express_core_AlgorithmScope_LocalScope = Generalization(general=LocalScope, specific=express_core_AlgorithmScope)
gen_express_core_LocalElement_NamedElement = Generalization(general=NamedElement, specific=express_core_LocalElement)
gen_express_core_DerivedAttribute_Attribute = Generalization(general=Attribute, specific=express_core_DerivedAttribute)
gen_express_core_RangeRole_Role = Generalization(general=Role, specific=express_core_RangeRole)
gen_express_core_SizeConstraint_DomainConstraint = Generalization(general=DomainConstraint, specific=express_core_SizeConstraint)
gen_express_core_SpecializedType_DefinedType = Generalization(general=DefinedType, specific=express_core_SpecializedType)
gen_express_core_SETType_ConcreteAggregationType = Generalization(general=ConcreteAggregationType, specific=express_core_SETType)
gen_express_core_GeneralARRAYType_GeneralAggregationType = Generalization(general=GeneralAggregationType, specific=express_core_GeneralARRAYType)
gen_express_core_NamedType_core_InstantiableType = Generalization(general=core_InstantiableType, specific=express_core_NamedType)
gen_express_core_NamedType_core_Scope = Generalization(general=core_Scope, specific=express_core_NamedType)
gen_express_core_NamedType_core_CommonElement = Generalization(general=core_CommonElement, specific=express_core_NamedType)
gen_express_core_NamedType_core_AttributeType = Generalization(general=core_AttributeType, specific=express_core_NamedType)
gen_express_core_LengthConstraint_DomainConstraint = Generalization(general=DomainConstraint, specific=express_core_LengthConstraint)
gen_express_core_LocalScope_Scope = Generalization(general=Scope, specific=express_core_LocalScope)
gen_express_core_SelectType_DefinedType = Generalization(general=DefinedType, specific=express_core_SelectType)
gen_express_core_BinaryType_SimpleType = Generalization(general=SimpleType, specific=express_core_BinaryType)
gen_express_core_ExplicitAttribute_Attribute = Generalization(general=Attribute, specific=express_core_ExplicitAttribute)
gen_express_core_SimpleType_AnonymousType = Generalization(general=AnonymousType, specific=express_core_SimpleType)
gen_express_core_CommonElement_SchemaElement = Generalization(general=SchemaElement, specific=express_core_CommonElement)
gen_express_core_SchemaElement_NamedElement = Generalization(general=NamedElement, specific=express_core_SchemaElement)
gen_express_core_ActualType_VariableType = Generalization(general=VariableType, specific=express_core_ActualType)
gen_express_algorithms_FunctionResult_Variable = Generalization(general=Variable, specific=express_algorithms_FunctionResult)
gen_express_algorithms_Function_Algorithm = Generalization(general=Algorithm, specific=express_algorithms_Function)
gen_express_core_ConcreteAggregationType_core_AnonymousType = Generalization(general=core_AnonymousType, specific=express_core_ConcreteAggregationType)
gen_express_core_ConcreteAggregationType_core_AggregationType = Generalization(general=core_AggregationType, specific=express_core_ConcreteAggregationType)
gen_express_core_ARRAYType_ConcreteAggregationType = Generalization(general=ConcreteAggregationType, specific=express_core_ARRAYType)
gen_express_algorithms_ActualStructure_algorithms_GenericElement = Generalization(general=algorithms_GenericElement, specific=express_algorithms_ActualStructure)
gen_express_algorithms_ActualStructure_core_AGGREGATEType = Generalization(general=core_AGGREGATEType, specific=express_algorithms_ActualStructure)
gen_express_algorithms_ActualGenericType_ActualType = Generalization(general=ActualType, specific=express_algorithms_ActualGenericType)
gen_express_algorithms_InParameter_Parameter = Generalization(general=Parameter_, specific=express_algorithms_InParameter)
gen_express_algorithms_LocalVariable_Variable = Generalization(general=Variable, specific=express_algorithms_LocalVariable)
gen_express_algorithms_Procedure_Algorithm = Generalization(general=Algorithm, specific=express_algorithms_Procedure)
gen_express_algorithms_ActualARRAYType_ActualAggregationType = Generalization(general=ActualAggregationType, specific=express_algorithms_ActualARRAYType)
gen_express_algorithms_ActualSETType_ActualAggregationType = Generalization(general=ActualAggregationType, specific=express_algorithms_ActualSETType)
gen_express_algorithms_ActualAGGREGATEType_ActualType = Generalization(general=ActualType, specific=express_algorithms_ActualAGGREGATEType)
gen_express_algorithms_NamedVariable_LocalElement = Generalization(general=LocalElement, specific=express_algorithms_NamedVariable)
gen_express_algorithms_InVariable_Variable = Generalization(general=Variable, specific=express_algorithms_InVariable)
gen_express_algorithms_Algorithm_core_AlgorithmScope = Generalization(general=core_AlgorithmScope, specific=express_algorithms_Algorithm)
gen_express_algorithms_Algorithm_core_CommonElement = Generalization(general=core_CommonElement, specific=express_algorithms_Algorithm)
gen_express_algorithms_ActualAggregationType_core_ActualType = Generalization(general=core_ActualType, specific=express_algorithms_ActualAggregationType)
gen_express_algorithms_ActualAggregationType_core_AggregationType = Generalization(general=core_AggregationType, specific=express_algorithms_ActualAggregationType)
gen_express_algorithms_Parameter_LocalElement = Generalization(general=LocalElement, specific=express_algorithms_Parameter)
gen_express_algorithms_VARParameter_algorithms_Parameter = Generalization(general=algorithms_Parameter, specific=express_algorithms_VARParameter)
gen_express_algorithms_VARParameter_algorithms_VARVariable = Generalization(general=algorithms_VARVariable, specific=express_algorithms_VARParameter)
gen_express_algorithms_ActualDataType_core_GenericType = Generalization(general=core_GenericType, specific=express_algorithms_ActualDataType)
gen_express_algorithms_ActualDataType_algorithms_GenericElement = Generalization(general=algorithms_GenericElement, specific=express_algorithms_ActualDataType)
gen_express_algorithms_ActualBAGType_ActualAggregationType = Generalization(general=ActualAggregationType, specific=express_algorithms_ActualBAGType)
gen_express_instances_ARRAYValue_AggregateValue = Generalization(general=AggregateValue, specific=express_instances_ARRAYValue)
gen_express_algorithms_ActualLISTType_ActualAggregationType = Generalization(general=ActualAggregationType, specific=express_algorithms_ActualLISTType)
gen_express_algorithms_Variable_NamedVariable = Generalization(general=NamedVariable, specific=express_algorithms_Variable)
gen_express_algorithms_GenericElement_LocalElement = Generalization(general=LocalElement, specific=express_algorithms_GenericElement)
gen_express_instances_IntegerValue_RealValue = Generalization(general=RealValue, specific=express_instances_IntegerValue)
gen_express_instances_AggregateValue_ConcreteValue = Generalization(general=ConcreteValue, specific=express_instances_AggregateValue)
gen_express_instances_Constant_CommonElement = Generalization(general=CommonElement, specific=express_instances_Constant)
gen_express_instances_LogicalValue_SimpleValue = Generalization(general=SimpleValue, specific=express_instances_LogicalValue)
gen_express_instances_TypedInstance_Instance = Generalization(general=Instance, specific=express_instances_TypedInstance)
gen_express_instances_RoleName_StringValue = Generalization(general=StringValue, specific=express_instances_RoleName)
gen_express_instances_EntityInstance_TypedInstance = Generalization(general=TypedInstance, specific=express_instances_EntityInstance)
gen_express_instances_Indeterminate_Instance = Generalization(general=Instance, specific=express_instances_Indeterminate)
gen_express_instances_SingleLeafInstance_EntityInstance = Generalization(general=EntityInstance, specific=express_instances_SingleLeafInstance)
gen_express_instances_GenericAggregate_LISTValue = Generalization(general=LISTValue, specific=express_instances_GenericAggregate)
gen_express_instances_BinaryValue_SimpleValue = Generalization(general=SimpleValue, specific=express_instances_BinaryValue)
gen_express_instances_SpecializedValue_TypedInstance = Generalization(general=TypedInstance, specific=express_instances_SpecializedValue)
gen_express_instances_BAGValue_AggregateValue = Generalization(general=AggregateValue, specific=express_instances_BAGValue)
gen_express_instances_EnumerationItem_instances_TypedInstance = Generalization(general=instances_TypedInstance, specific=express_instances_EnumerationItem)
gen_express_instances_EnumerationItem_instances_ConcreteValue = Generalization(general=instances_ConcreteValue, specific=express_instances_EnumerationItem)
gen_express_instances_EntityValue_PartialEntityValue = Generalization(general=PartialEntityValue, specific=express_instances_EntityValue)
gen_express_instances_SETValue_AggregateValue = Generalization(general=AggregateValue, specific=express_instances_SETValue)
gen_express_instances_EnumerationItem_core_TypeElement = Generalization(general=core_TypeElement, specific=express_instances_EnumerationItem)
gen_express_instances_BooleanValue_LogicalValue = Generalization(general=LogicalValue, specific=express_instances_BooleanValue)
gen_express_instances_LISTValue_core_Instance = Generalization(general=core_Instance, specific=express_instances_LISTValue)
gen_express_instances_LISTValue_instances_AggregateValue = Generalization(general=instances_AggregateValue, specific=express_instances_LISTValue)
gen_express_instances_StringValue_SimpleValue = Generalization(general=SimpleValue, specific=express_instances_StringValue)
gen_express_instances_TypeName_StringValue = Generalization(general=StringValue, specific=express_instances_TypeName)
gen_express_instances_PartialEntityValue_Instance = Generalization(general=Instance, specific=express_instances_PartialEntityValue)
gen_express_instances_NumberValue_SimpleValue = Generalization(general=SimpleValue, specific=express_instances_NumberValue)
gen_express_instances_MultiLeafInstance_EntityInstance = Generalization(general=EntityInstance, specific=express_instances_MultiLeafInstance)
gen_express_instances_SimpleValue_ConcreteValue = Generalization(general=ConcreteValue, specific=express_instances_SimpleValue)
gen_express_instances_ConcreteValue_Instance = Generalization(general=Instance, specific=express_instances_ConcreteValue)
gen_express_instances_RealValue_NumberValue = Generalization(general=NumberValue, specific=express_instances_RealValue)

# Domain Model
domain_model = DomainModel(
    name="express",
    types={express_rules_ONEOFConstraint, SubtypeConstraint, express_rules_SupertypeRule, CommonElement, EntityType, Population, GlobalRule, ScopedId, express_rules_TOTAL_OVERConstraint, express_rules_ANDConstraint, express_rules_GlobalRule, core_SchemaElement, core_AlgorithmScope, express_rules_SubtypeConstraint, Extent, Expression, SupertypeRule, express_rules_Extent, SETValue, EntityInstance, express_statements_SkipStatement, ControlStatement, express_statements_AliasStatement, algorithms_Statement, core_LocalScope, VARExpression, AliasVariable, Statement, NamedRule, express_rules_NamedRule, LocalElement, express_statements_ProcedureCall, Procedure, ActualParameter, VARVariable, express_statements_NullStatement, express_statements_VARExpression, express_statements_AttributeCell, ExplicitAttribute, express_statements_ControlVariable, NamedVariable, express_statements_AliasVariable, algorithms_NamedVariable, algorithms_VARVariable, express_statements_ControlStatement, express_statements_VARCell, express_statements_StatementBlock, express_statements_CaseAction, express_statements_MemberCell, ControlVariable, express_statements_GroupCell, SingleEntityType, express_statements_VariableCell, express_statements_RepeatStatement, express_statements_IfStatement, express_statements_EscapeStatement, express_statements_ReturnStatement, express_statements_Assignment, Variable, express_statements_CaseStatement, CaseAction, express_expressions_Selector, express_expressions_RepeatCount, express_expressions_EnumItemRef, Primary, EnumerationItem, express_expressions_IndeterminateRef, Indeterminate, express_expressions_SELFRef, express_expressions_IndexOperation, express_expressions_BinaryOperation, Operation, express_expressions_Literal, SimpleValue, express_expressions_BinaryIndex, IndexOperation, express_expressions_PartialEntityConstructor, PartialEntityValue, AttributeBinding, express_expressions_Coercion, express_expressions_AggregateInitializer, VariableType, GenericAggregate, express_expressions_Primary, MemberBinding, express_expressions_ActualParameter, express_expressions_StringIndex, FunctionCall, Parameter_, express_expressions_ParameterRef, ProcedureCall, express_expressions_AttributeRef, Selector, Attribute, express_expressions_AggregateIndex, express_expressions_GroupRef, express_expressions_UnaryOperation, express_expressions_UsedInRef, express_expressions_ConstantRef, Constant, express_expressions_QueryExpression, core_Expression, QueryVariable, express_expressions_QueryVariable, express_expressions_Operation, express_expressions_AttributeBinding, AttributeValue, express_expressions_FunctionCall, Function, FunctionResult, express_expressions_MemberBinding, RepeatCount, ListMember, express_expressions_ExtentRef, NamedType, express_expressions_VariableRef, express_core_TypeElement, NamedElement, express_core_SingleEntityType, PartialEntityType, express_core_AGGREGATEType, GeneralizedType, SizeConstraint, ParameterType, ActualStructureConstraint, express_core_DomainRule, core_DomainConstraint, core_TypeElement, express_core_GeneralAggregationType, core_GeneralizedType, core_AggregationType, express_core_ConcreteType, InstantiableType, express_core_Expression, Instance, Scope, DataType, express_core_InverseAttribute, DomainRole, InvertibleAttribute, express_core_EnumerationType, DefinedType, express_core_GeneralBAGType, GeneralAggregationType, EnumerationType, express_core_VariableType, core_DataType, core_AttributeType, express_core_ArrayBound, express_core_GeneralSETType, express_core_LISTType, ConcreteAggregationType, express_core_Redeclaration, AttributeType, Redeclaration, Role, express_core_EntityType, core_NamedType, core_InstantiableType, RangeRole, UniqueRule, express_core_DataType, express_core_PartialEntityType, InterfacedElement, SchemaElement, express_core_InvertibleAttribute, InverseAttribute, Relationship, express_core_GeneralizedType, core_ParameterType, express_core_Schema, Remark, express_core_InterfacedElement, Schema, express_core_NumericType, SimpleType, express_core_DefinedType, core_ConcreteType, express_core_UniqueRule, TypeElement, express_core_DomainRole, express_core_BAGType, express_core_RealType, NumericType, express_core_InstantiableType, core_VariableType, express_core_GeneralLISTType, express_core_NamedElement, express_core_Attribute, express_core_DomainConstraint, express_core_AttributeType, express_core_LogicType, express_core_GenericType, ActualTypeConstraint, express_core_StringType, LengthConstraint, express_core_AnonymousType, AnonymousType, express_core_AlgorithmScope, LocalScope, express_core_Instance, express_core_LocalElement, DomainConstraint, express_core_DerivedAttribute, express_core_RangeRole, express_core_Role, express_core_Remark, express_core_SizeConstraint, express_core_SpecializedType, ConcreteType, express_core_SETType, express_core_GeneralARRAYType, ArrayBound, express_core_Relationship, express_core_NamedType, core_Scope, core_CommonElement, express_core_LengthConstraint, express_core_LocalScope, express_core_Scope, SelectType, express_core_ParameterType, express_core_SelectType, DomainRule, express_core_BinaryType, express_core_ScopedId, express_core_AggregationType, express_core_ExplicitAttribute, express_core_SimpleType, express_core_CommonElement, AlgorithmScope, express_core_SchemaElement, express_core_ActualType, Algorithm, express_algorithms_ActualTypeConstraint, GenericType, ActualDataType, express_algorithms_FunctionResult, express_algorithms_Function, express_core_ConcreteAggregationType, core_AnonymousType, express_core_ARRAYType, express_algorithms_ActualStructure, algorithms_GenericElement, core_AGGREGATEType, express_algorithms_ActualGenericType, ActualType, express_algorithms_Statement, StatementBlock, SkipStatement, EscapeStatement, RepeatStatement, express_algorithms_InParameter, InVariable, express_algorithms_LocalVariable, express_algorithms_Procedure, express_algorithms_ActualARRAYType, ActualAggregationType, express_algorithms_ActualSETType, express_algorithms_ActualAGGREGATEType, ActualStructure, express_algorithms_NamedVariable, express_algorithms_InVariable, InParameter, express_algorithms_ActualStructureConstraint, AGGREGATEType, express_algorithms_Algorithm, express_algorithms_ActualAggregationType, core_ActualType, express_algorithms_Parameter, express_algorithms_VARParameter, algorithms_Parameter, express_algorithms_ActualDataType, core_GenericType, express_algorithms_ActualBAGType, express_instances_AttributeValue, express_instances_ARRAYValue, AggregateValue, ArrayMember, express_instances_RoleName, express_algorithms_VARVariable, express_algorithms_ActualLISTType, express_algorithms_Variable, express_algorithms_GenericElement, express_instances_IntegerValue, RealValue, express_instances_AggregateValue, ConcreteValue, express_instances_Constant, express_instances_LogicalValue, express_instances_TypedInstance, StringValue, express_instances_ListMember, express_instances_EntityInstance, TypedInstance, express_instances_BagMember, EntityValue, express_instances_SingleEntityValue, express_instances_Indeterminate, express_instances_SingleLeafInstance, express_instances_GenericAggregate, LISTValue, express_instances_BinaryValue, express_instances_SpecializedValue, express_instances_BAGValue, BagMember, express_instances_EnumerationItem, instances_TypedInstance, instances_ConcreteValue, express_instances_EntityValue, express_instances_SETValue, express_instances_ArrayMember, express_instances_Population, express_instances_RealValue, express_instances_BooleanValue, LogicalValue, express_instances_LISTValue, core_Instance, instances_AggregateValue, express_instances_StringValue, express_instances_TypeName, express_instances_PartialEntityValue, SingleEntityValue, express_instances_NumberValue, express_instances_MultiLeafInstance, express_instances_SimpleValue, express_instances_ConcreteValue, NumberValue},
    associations={namedSupertype0, constraints1, withinPopulation11, constraintRules13, forType15, id17, constrainedSubtypes2, equivalentRule4, collection5, constraints7, content10, actualParameters28, bindsToReference29, body30, aliasVariable33, supportingBody19, constrainedExtents20, containsRules23, assertsExpression25, invokes27, refersTo45, refersTo46, baseEntity47, boundValue35, initialValue37, increment40, referent43, bodyStatements_Statement50, labelValue52, action54, whileExpression62, body64, controlVariable67, untilExpression69, baseEntity72, refersTo74, indexValue57, baseAggregate59, ifCondition81, elseActions83, thenActions86, returnValue89, assignedValue91, refersTo76, cases77, selectionExpression78, entityInstance96, derivation98, refersTo100, variable93, lastBit104, refersTo107, baseValue108, leftOperand110, rightOperand112, refersTo101, firstBit102, firstCode118, lastCode120, resultValue123, attributeGroup124, bindings127, operand129, targetType131, resultValue115, bindings116, inFunctionCall134, formalParameter136, actualReferent137, actualValue140, inProcedureCall133, refersTo145, indexValue146, refersTo148, unaryOperand150, refersTo143, refersTo154, selectCondition155, queryVariable157, aggregateOperand159, attributeValue162, toValue164, inverseOf152, actualParameters169, invokesFunction172, returnsResult173, repetition175, toSlot176, memberValue178, refersTo181, attribute166, declaresExplicitAttribute183, declaresAttribute185, declaredIn188, equivalent191, id193, upperBound196, memberType197, constraint199, lowerBound201, refersTo182, memberType204, evaluation205, interpretationContext206, dataType208, modelsRole210, explicit212, values214, extension218, base220, boundExpression223, derivation225, restrictedType227, refines229, upperBound231, declaredItems216, scope237, originalAttribute240, refinedRole243, alias245, playsRole248, redeclarations251, attributes254, playsRangeRole257, declares259, extension262, lowerBound234, invertibleAttributes265, playsDomainRole268, uniqueRules271, usedIn273, subtypeOf276, instances278, components281, documentation283, interfaces285, schemaElements287, interfacedElements289, inverse292, rangeType294, createsRelationship297, referencingType299, modelsRole302, interfacingSchema308, refersTo310, interfacedId313, domain315, keyComponent318, rangeView320, domain323, occursIn305, owningEntity348, domain328, asserts331, fundamentalType333, namespace334, documentation337, id340, attributeType342, ofEntity345, id326, ofType362, role365, constraint351, stringLengthConstraint353, specializes354, commonElements355, variables357, appearsInPopulation359, id378, constraints368, derivation370, domainView372, range375, inRelationship388, describesSchema380, appearsIn383, describesElement386, underlyingType399, ofEntity391, upperBound394, lowerBound396, roles406, hiIndex400, loIndex401, domain404, basedOn409, range412, localElements415, upperBound425, namedElements428, includesRemarks431, contains434, instantiates416, domainRules418, allowedTypes437, binaryLengthConstraint419, definingScope421, lowerBound423, scope448, localScope449, referencedAs451, referencedIn454, extension440, base443, selectList446, matchingType467, requiredType469, definedIn457, memberType460, loIndex462, hiIndex464, refersTo476, inBlock478, bodyStatementsSkipStatement480, bodyStatementsEscapeStatement481, controlledBy483, result470, variable472, initialValue474, hiIndex492, loIndex494, upperBound497, refersTo499, memberType501, lowerBound504, implements485, variableType488, source490, matchingStructure515, requiredStructure517, body519, formalParameters522, structureConstraints507, typeConstraints509, formalParameterType512, label527, actualValue530, attribute532, memberSlot535, memberType524, source525, state541, instanceOf543, valueExpression545, actualValue547, dataType550, refersTo536, satisfiesType553, represents538, memberValue555, memberValue557, equivalent559, ofType561, properties564, characterizingType567, fundamentalValue569, memberSlot570, declaredIn571, correspondsTo574, describes576, memberValue579, memberValue581, compositionEntityInstance583, compositionInstance585, governingSchema588, memberSlot591, refersTo593, represents595, components598},
    generalizations={gen_express_rules_ONEOFConstraint_SubtypeConstraint, gen_express_rules_SupertypeRule_CommonElement, gen_express_rules_TOTAL_OVERConstraint_SubtypeConstraint, gen_express_rules_ANDConstraint_SubtypeConstraint, gen_express_rules_GlobalRule_core_SchemaElement, gen_express_rules_GlobalRule_core_AlgorithmScope, gen_express_rules_Extent_SETValue, gen_express_statements_SkipStatement_ControlStatement, gen_express_statements_AliasStatement_algorithms_Statement, gen_express_statements_AliasStatement_core_LocalScope, gen_express_rules_NamedRule_LocalElement, gen_express_statements_ProcedureCall_Statement, gen_express_statements_NullStatement_ControlStatement, gen_express_statements_AttributeCell_VARExpression, gen_express_statements_ControlVariable_NamedVariable, gen_express_statements_AliasVariable_algorithms_NamedVariable, gen_express_statements_AliasVariable_algorithms_VARVariable, gen_express_statements_ControlStatement_Statement, gen_express_statements_VARCell_VARExpression, gen_express_statements_StatementBlock_Statement, gen_express_statements_MemberCell_VARExpression, gen_express_statements_RepeatStatement_algorithms_Statement, gen_express_statements_RepeatStatement_core_LocalScope, gen_express_statements_GroupCell_VARExpression, gen_express_statements_IfStatement_Statement, gen_express_statements_EscapeStatement_ControlStatement, gen_express_statements_ReturnStatement_ControlStatement, gen_express_statements_Assignment_Statement, gen_express_statements_VariableCell_VARExpression, gen_express_statements_CaseStatement_Statement, gen_express_expressions_Selector_Expression, gen_express_expressions_EnumItemRef_Primary, gen_express_expressions_IndeterminateRef_Primary, gen_express_expressions_SELFRef_Primary, gen_express_expressions_IndexOperation_Expression, gen_express_expressions_BinaryOperation_Operation, gen_express_expressions_Literal_Primary, gen_express_expressions_BinaryIndex_IndexOperation, gen_express_expressions_PartialEntityConstructor_Expression, gen_express_expressions_Coercion_Operation, gen_express_expressions_AggregateInitializer_Expression, gen_express_expressions_Primary_Expression, gen_express_expressions_StringIndex_IndexOperation, gen_express_expressions_ParameterRef_Primary, gen_express_expressions_AttributeRef_Selector, gen_express_expressions_AggregateIndex_IndexOperation, gen_express_expressions_GroupRef_Selector, gen_express_expressions_UnaryOperation_Operation, gen_express_expressions_UsedInRef_Selector, gen_express_expressions_ConstantRef_Primary, gen_express_expressions_QueryExpression_core_LocalScope, gen_express_expressions_QueryExpression_core_Expression, gen_express_expressions_QueryVariable_NamedVariable, gen_express_expressions_Operation_Expression, gen_express_expressions_FunctionCall_Expression, gen_express_expressions_ExtentRef_Primary, gen_express_expressions_VariableRef_Primary, gen_express_core_TypeElement_NamedElement, gen_express_core_AGGREGATEType_GeneralizedType, gen_express_core_DomainRule_core_DomainConstraint, gen_express_core_DomainRule_core_TypeElement, gen_express_core_GeneralAggregationType_core_GeneralizedType, gen_express_core_GeneralAggregationType_core_AggregationType, gen_express_core_ConcreteType_InstantiableType, gen_express_core_InverseAttribute_Attribute, gen_express_core_EnumerationType_DefinedType, gen_express_core_GeneralBAGType_GeneralAggregationType, gen_express_core_VariableType_core_DataType, gen_express_core_VariableType_core_AttributeType, gen_express_core_GeneralSETType_GeneralAggregationType, gen_express_core_LISTType_ConcreteAggregationType, gen_express_core_EntityType_core_NamedType, gen_express_core_EntityType_core_InstantiableType, gen_express_core_PartialEntityType_DataType, gen_express_core_InvertibleAttribute_ExplicitAttribute, gen_express_core_GeneralizedType_core_ParameterType, gen_express_core_GeneralizedType_core_AttributeType, gen_express_core_Schema_Scope, gen_express_core_NumericType_SimpleType, gen_express_core_DefinedType_core_NamedType, gen_express_core_DefinedType_core_ConcreteType, gen_express_core_UniqueRule_TypeElement, gen_express_core_DomainRole_Role, gen_express_core_BAGType_ConcreteAggregationType, gen_express_core_RealType_NumericType, gen_express_core_InstantiableType_core_ParameterType, gen_express_core_InstantiableType_core_VariableType, gen_express_core_GeneralLISTType_GeneralAggregationType, gen_express_core_Attribute_TypeElement, gen_express_core_LogicType_SimpleType, gen_express_core_GenericType_GeneralizedType, gen_express_core_StringType_SimpleType, gen_express_core_AnonymousType_core_ConcreteType, gen_express_core_AnonymousType_core_InstantiableType, gen_express_core_AlgorithmScope_LocalScope, gen_express_core_LocalElement_NamedElement, gen_express_core_DerivedAttribute_Attribute, gen_express_core_RangeRole_Role, gen_express_core_SizeConstraint_DomainConstraint, gen_express_core_SpecializedType_DefinedType, gen_express_core_SETType_ConcreteAggregationType, gen_express_core_GeneralARRAYType_GeneralAggregationType, gen_express_core_NamedType_core_InstantiableType, gen_express_core_NamedType_core_Scope, gen_express_core_NamedType_core_CommonElement, gen_express_core_NamedType_core_AttributeType, gen_express_core_LengthConstraint_DomainConstraint, gen_express_core_LocalScope_Scope, gen_express_core_SelectType_DefinedType, gen_express_core_BinaryType_SimpleType, gen_express_core_ExplicitAttribute_Attribute, gen_express_core_SimpleType_AnonymousType, gen_express_core_CommonElement_SchemaElement, gen_express_core_SchemaElement_NamedElement, gen_express_core_ActualType_VariableType, gen_express_algorithms_FunctionResult_Variable, gen_express_algorithms_Function_Algorithm, gen_express_core_ConcreteAggregationType_core_AnonymousType, gen_express_core_ConcreteAggregationType_core_AggregationType, gen_express_core_ARRAYType_ConcreteAggregationType, gen_express_algorithms_ActualStructure_algorithms_GenericElement, gen_express_algorithms_ActualStructure_core_AGGREGATEType, gen_express_algorithms_ActualGenericType_ActualType, gen_express_algorithms_InParameter_Parameter, gen_express_algorithms_LocalVariable_Variable, gen_express_algorithms_Procedure_Algorithm, gen_express_algorithms_ActualARRAYType_ActualAggregationType, gen_express_algorithms_ActualSETType_ActualAggregationType, gen_express_algorithms_ActualAGGREGATEType_ActualType, gen_express_algorithms_NamedVariable_LocalElement, gen_express_algorithms_InVariable_Variable, gen_express_algorithms_Algorithm_core_AlgorithmScope, gen_express_algorithms_Algorithm_core_CommonElement, gen_express_algorithms_ActualAggregationType_core_ActualType, gen_express_algorithms_ActualAggregationType_core_AggregationType, gen_express_algorithms_Parameter_LocalElement, gen_express_algorithms_VARParameter_algorithms_Parameter, gen_express_algorithms_VARParameter_algorithms_VARVariable, gen_express_algorithms_ActualDataType_core_GenericType, gen_express_algorithms_ActualDataType_algorithms_GenericElement, gen_express_algorithms_ActualBAGType_ActualAggregationType, gen_express_instances_ARRAYValue_AggregateValue, gen_express_algorithms_ActualLISTType_ActualAggregationType, gen_express_algorithms_Variable_NamedVariable, gen_express_algorithms_GenericElement_LocalElement, gen_express_instances_IntegerValue_RealValue, gen_express_instances_AggregateValue_ConcreteValue, gen_express_instances_Constant_CommonElement, gen_express_instances_LogicalValue_SimpleValue, gen_express_instances_TypedInstance_Instance, gen_express_instances_RoleName_StringValue, gen_express_instances_EntityInstance_TypedInstance, gen_express_instances_Indeterminate_Instance, gen_express_instances_SingleLeafInstance_EntityInstance, gen_express_instances_GenericAggregate_LISTValue, gen_express_instances_BinaryValue_SimpleValue, gen_express_instances_SpecializedValue_TypedInstance, gen_express_instances_BAGValue_AggregateValue, gen_express_instances_EnumerationItem_instances_TypedInstance, gen_express_instances_EnumerationItem_instances_ConcreteValue, gen_express_instances_EntityValue_PartialEntityValue, gen_express_instances_SETValue_AggregateValue, gen_express_instances_EnumerationItem_core_TypeElement, gen_express_instances_BooleanValue_LogicalValue, gen_express_instances_LISTValue_core_Instance, gen_express_instances_LISTValue_instances_AggregateValue, gen_express_instances_StringValue_SimpleValue, gen_express_instances_TypeName_StringValue, gen_express_instances_PartialEntityValue_Instance, gen_express_instances_NumberValue_SimpleValue, gen_express_instances_MultiLeafInstance_EntityInstance, gen_express_instances_SimpleValue_ConcreteValue, gen_express_instances_ConcreteValue_Instance, gen_express_instances_RealValue_NumberValue},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)