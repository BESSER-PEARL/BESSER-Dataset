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
express_rules_ONEOFConstraint = Class(name="express_rules_ONEOFConstraint")
SubtypeConstraint = Class(name="SubtypeConstraint")
express_rules_SupertypeRule = Class(name="express_rules_SupertypeRule")
CommonElement = Class(name="CommonElement")
EntityType = Class(name="EntityType")
express_statements_ProcedureCall = Class(name="express_statements_ProcedureCall")
Procedure = Class(name="Procedure")
ActualParameter = Class(name="ActualParameter")
express_rules_SubtypeConstraint = Class(name="express_rules_SubtypeConstraint")
Extent = Class(name="Extent")
Expression = Class(name="Expression")
SupertypeRule = Class(name="SupertypeRule")
express_rules_Extent = Class(name="express_rules_Extent")
SETValue = Class(name="SETValue")
EntityInstance = Class(name="EntityInstance")
Population = Class(name="Population")
GlobalRule = Class(name="GlobalRule")
ScopedId = Class(name="ScopedId")
express_rules_TOTAL_OVERConstraint = Class(name="express_rules_TOTAL_OVERConstraint")
express_rules_ANDConstraint = Class(name="express_rules_ANDConstraint")
express_rules_GlobalRule = Class(name="express_rules_GlobalRule")
core_SchemaElement = Class(name="core_SchemaElement")
core_AlgorithmScope = Class(name="core_AlgorithmScope")
Statement = Class(name="Statement")
NamedRule = Class(name="NamedRule")
express_rules_NamedRule = Class(name="express_rules_NamedRule")
LocalElement = Class(name="LocalElement")
express_statements_CaseAction = Class(name="express_statements_CaseAction")
express_statements_SkipStatement = Class(name="express_statements_SkipStatement")
ControlStatement = Class(name="ControlStatement")
express_statements_AliasStatement = Class(name="express_statements_AliasStatement")
algorithms_Statement = Class(name="algorithms_Statement")
core_LocalScope = Class(name="core_LocalScope")
VARExpression = Class(name="VARExpression")
AliasVariable = Class(name="AliasVariable")
express_statements_ControlVariable = Class(name="express_statements_ControlVariable")
NamedVariable = Class(name="NamedVariable")
express_statements_AliasVariable = Class(name="express_statements_AliasVariable")
algorithms_NamedVariable = Class(name="algorithms_NamedVariable")
algorithms_VARVariable = Class(name="algorithms_VARVariable")
express_statements_ControlStatement = Class(name="express_statements_ControlStatement", is_abstract=True)
express_statements_VARCell = Class(name="express_statements_VARCell")
VARVariable = Class(name="VARVariable")
express_statements_NullStatement = Class(name="express_statements_NullStatement")
express_statements_VARExpression = Class(name="express_statements_VARExpression", is_abstract=True)
express_statements_AttributeCell = Class(name="express_statements_AttributeCell")
ExplicitAttribute = Class(name="ExplicitAttribute")
express_statements_StatementBlock = Class(name="express_statements_StatementBlock")
express_statements_IfStatement = Class(name="express_statements_IfStatement")
express_statements_MemberCell = Class(name="express_statements_MemberCell")
express_statements_RepeatStatement = Class(name="express_statements_RepeatStatement")
ControlVariable = Class(name="ControlVariable")
express_statements_GroupCell = Class(name="express_statements_GroupCell")
SingleEntityType = Class(name="SingleEntityType")
express_statements_VariableCell = Class(name="express_statements_VariableCell")
Variable = Class(name="Variable")
express_statements_CaseStatement = Class(name="express_statements_CaseStatement")
CaseAction = Class(name="CaseAction")
Indeterminate = Class(name="Indeterminate")
express_expressions_SELFRef = Class(name="express_expressions_SELFRef")
express_expressions_IndexOperation = Class(name="express_expressions_IndexOperation", is_abstract=True)
express_statements_EscapeStatement = Class(name="express_statements_EscapeStatement")
express_statements_ReturnStatement = Class(name="express_statements_ReturnStatement")
express_statements_Assignment = Class(name="express_statements_Assignment")
express_expressions_Selector = Class(name="express_expressions_Selector", is_abstract=True)
express_expressions_RepeatCount = Class(name="express_expressions_RepeatCount")
express_expressions_EnumItemRef = Class(name="express_expressions_EnumItemRef")
Primary = Class(name="Primary")
EnumerationItem = Class(name="EnumerationItem")
express_expressions_Literal = Class(name="express_expressions_Literal")
SimpleValue = Class(name="SimpleValue")
express_expressions_BinaryIndex = Class(name="express_expressions_BinaryIndex")
IndexOperation = Class(name="IndexOperation")
express_expressions_ActualParameter = Class(name="express_expressions_ActualParameter")
express_expressions_IndeterminateRef = Class(name="express_expressions_IndeterminateRef")
ProcedureCall = Class(name="ProcedureCall")
FunctionCall = Class(name="FunctionCall")
Parameter_ = Class(name="Parameter")
express_expressions_BinaryOperation = Class(name="express_expressions_BinaryOperation")
Operation = Class(name="Operation")
express_expressions_ParameterRef = Class(name="express_expressions_ParameterRef")
express_expressions_AggregateInitializer = Class(name="express_expressions_AggregateInitializer")
GenericAggregate = Class(name="GenericAggregate")
MemberBinding = Class(name="MemberBinding")
express_expressions_StringIndex = Class(name="express_expressions_StringIndex")
express_expressions_PartialEntityConstructor = Class(name="express_expressions_PartialEntityConstructor")
PartialEntityValue = Class(name="PartialEntityValue")
AttributeBinding = Class(name="AttributeBinding")
express_expressions_Coercion = Class(name="express_expressions_Coercion")
VariableType = Class(name="VariableType")
express_expressions_Primary = Class(name="express_expressions_Primary", is_abstract=True)
QueryVariable = Class(name="QueryVariable")
express_expressions_QueryVariable = Class(name="express_expressions_QueryVariable")
express_expressions_Operation = Class(name="express_expressions_Operation", is_abstract=True)
express_expressions_AttributeBinding = Class(name="express_expressions_AttributeBinding")
AttributeValue = Class(name="AttributeValue")
express_expressions_AttributeRef = Class(name="express_expressions_AttributeRef")
Selector = Class(name="Selector")
Attribute = Class(name="Attribute")
express_expressions_AggregateIndex = Class(name="express_expressions_AggregateIndex")
express_expressions_GroupRef = Class(name="express_expressions_GroupRef")
express_expressions_UnaryOperation = Class(name="express_expressions_UnaryOperation")
express_expressions_UsedInRef = Class(name="express_expressions_UsedInRef")
express_expressions_ConstantRef = Class(name="express_expressions_ConstantRef")
Constant = Class(name="Constant")
express_expressions_QueryExpression = Class(name="express_expressions_QueryExpression")
core_Expression = Class(name="core_Expression")
express_core_TypeElement = Class(name="express_core_TypeElement", is_abstract=True)
NamedElement = Class(name="NamedElement")
express_core_SingleEntityType = Class(name="express_core_SingleEntityType")
PartialEntityType = Class(name="PartialEntityType")
express_core_AGGREGATEType = Class(name="express_core_AGGREGATEType")
GeneralizedType = Class(name="GeneralizedType")
SizeConstraint = Class(name="SizeConstraint")
express_expressions_FunctionCall = Class(name="express_expressions_FunctionCall")
Function = Class(name="Function")
FunctionResult = Class(name="FunctionResult")
express_expressions_MemberBinding = Class(name="express_expressions_MemberBinding")
RepeatCount = Class(name="RepeatCount")
ListMember = Class(name="ListMember")
express_expressions_ExtentRef = Class(name="express_expressions_ExtentRef")
NamedType = Class(name="NamedType")
express_expressions_VariableRef = Class(name="express_expressions_VariableRef")
EnumerationType = Class(name="EnumerationType")
express_core_VariableType = Class(name="express_core_VariableType", is_abstract=True)
core_DataType = Class(name="core_DataType")
core_AttributeType = Class(name="core_AttributeType")
express_core_ArrayBound = Class(name="express_core_ArrayBound")
ParameterType = Class(name="ParameterType")
ActualStructureConstraint = Class(name="ActualStructureConstraint")
express_core_GeneralBAGType = Class(name="express_core_GeneralBAGType")
GeneralAggregationType = Class(name="GeneralAggregationType")
express_core_DomainRule = Class(name="express_core_DomainRule")
core_DomainConstraint = Class(name="core_DomainConstraint")
core_TypeElement = Class(name="core_TypeElement")
express_core_GeneralAggregationType = Class(name="express_core_GeneralAggregationType", is_abstract=True)
core_GeneralizedType = Class(name="core_GeneralizedType")
core_AggregationType = Class(name="core_AggregationType")
express_core_ConcreteType = Class(name="express_core_ConcreteType", is_abstract=True)
InstantiableType = Class(name="InstantiableType")
express_core_Expression = Class(name="express_core_Expression")
Instance = Class(name="Instance")
Scope = Class(name="Scope")
DataType = Class(name="DataType")
express_core_InverseAttribute = Class(name="express_core_InverseAttribute")
DomainRole = Class(name="DomainRole")
InvertibleAttribute = Class(name="InvertibleAttribute")
express_core_EnumerationType = Class(name="express_core_EnumerationType")
DefinedType = Class(name="DefinedType")
RangeRole = Class(name="RangeRole")
UniqueRule = Class(name="UniqueRule")
express_core_GeneralSETType = Class(name="express_core_GeneralSETType")
express_core_LISTType = Class(name="express_core_LISTType")
ConcreteAggregationType = Class(name="ConcreteAggregationType")
express_core_Redeclaration = Class(name="express_core_Redeclaration")
AttributeType = Class(name="AttributeType")
Redeclaration = Class(name="Redeclaration")
Role = Class(name="Role")
express_core_EntityType = Class(name="express_core_EntityType")
core_NamedType = Class(name="core_NamedType")
core_InstantiableType = Class(name="core_InstantiableType")
express_core_GeneralizedType = Class(name="express_core_GeneralizedType", is_abstract=True)
core_ParameterType = Class(name="core_ParameterType")
express_core_InterfacedElement = Class(name="express_core_InterfacedElement")
Schema = Class(name="Schema")
express_core_DataType = Class(name="express_core_DataType", is_abstract=True)
express_core_PartialEntityType = Class(name="express_core_PartialEntityType")
express_core_Schema = Class(name="express_core_Schema")
Remark = Class(name="Remark")
InterfacedElement = Class(name="InterfacedElement")
SchemaElement = Class(name="SchemaElement")
express_core_InvertibleAttribute = Class(name="express_core_InvertibleAttribute")
InverseAttribute = Class(name="InverseAttribute")
Relationship = Class(name="Relationship")
express_core_Attribute = Class(name="express_core_Attribute", is_abstract=True)
express_core_NumericType = Class(name="express_core_NumericType")
SimpleType = Class(name="SimpleType")
express_core_DefinedType = Class(name="express_core_DefinedType", is_abstract=True)
core_ConcreteType = Class(name="core_ConcreteType")
express_core_UniqueRule = Class(name="express_core_UniqueRule")
TypeElement = Class(name="TypeElement")
express_core_DomainRole = Class(name="express_core_DomainRole")
express_core_DomainConstraint = Class(name="express_core_DomainConstraint", is_abstract=True)
express_core_InstantiableType = Class(name="express_core_InstantiableType", is_abstract=True)
core_VariableType = Class(name="core_VariableType")
express_core_GeneralLISTType = Class(name="express_core_GeneralLISTType")
express_core_NamedElement = Class(name="express_core_NamedElement", is_abstract=True)
express_core_Instance = Class(name="express_core_Instance", is_abstract=True)
express_core_AttributeType = Class(name="express_core_AttributeType", is_abstract=True)
DomainConstraint = Class(name="DomainConstraint")
express_core_DerivedAttribute = Class(name="express_core_DerivedAttribute")
express_core_BAGType = Class(name="express_core_BAGType")
express_core_RealType = Class(name="express_core_RealType")
NumericType = Class(name="NumericType")
express_core_LogicType = Class(name="express_core_LogicType")
express_core_GenericType = Class(name="express_core_GenericType")
ActualTypeConstraint = Class(name="ActualTypeConstraint")
express_core_StringType = Class(name="express_core_StringType")
LengthConstraint = Class(name="LengthConstraint")
express_core_AnonymousType = Class(name="express_core_AnonymousType", is_abstract=True)
AnonymousType = Class(name="AnonymousType")
express_core_AlgorithmScope = Class(name="express_core_AlgorithmScope", is_abstract=True)
LocalScope = Class(name="LocalScope")
express_core_SETType = Class(name="express_core_SETType")
express_core_SpecializedType = Class(name="express_core_SpecializedType")
ConcreteType = Class(name="ConcreteType")
express_core_GeneralARRAYType = Class(name="express_core_GeneralARRAYType")
ArrayBound = Class(name="ArrayBound")
express_core_RangeRole = Class(name="express_core_RangeRole")
express_core_LocalElement = Class(name="express_core_LocalElement", is_abstract=True)
express_core_Remark = Class(name="express_core_Remark")
express_core_SizeConstraint = Class(name="express_core_SizeConstraint")
express_core_Role = Class(name="express_core_Role", is_abstract=True)
express_core_Scope = Class(name="express_core_Scope", is_abstract=True)
express_core_ParameterType = Class(name="express_core_ParameterType", is_abstract=True)
express_core_SelectType = Class(name="express_core_SelectType")
express_core_Relationship = Class(name="express_core_Relationship")
express_core_LengthConstraint = Class(name="express_core_LengthConstraint")
express_core_LocalScope = Class(name="express_core_LocalScope", is_abstract=True)
express_core_NamedType = Class(name="express_core_NamedType", is_abstract=True)
core_Scope = Class(name="core_Scope")
core_CommonElement = Class(name="core_CommonElement")
SelectType = Class(name="SelectType")
DomainRule = Class(name="DomainRule")
express_core_BinaryType = Class(name="express_core_BinaryType")
express_core_ScopedId = Class(name="express_core_ScopedId")
express_core_AggregationType = Class(name="express_core_AggregationType", is_abstract=True)
express_core_ARRAYType = Class(name="express_core_ARRAYType")
express_algorithms_ActualTypeConstraint = Class(name="express_algorithms_ActualTypeConstraint")
express_core_ActualType = Class(name="express_core_ActualType", is_abstract=True)
Algorithm = Class(name="Algorithm")
express_core_ExplicitAttribute = Class(name="express_core_ExplicitAttribute")
express_core_SimpleType = Class(name="express_core_SimpleType", is_abstract=True)
express_core_CommonElement = Class(name="express_core_CommonElement", is_abstract=True)
AlgorithmScope = Class(name="AlgorithmScope")
express_core_SchemaElement = Class(name="express_core_SchemaElement", is_abstract=True)
express_core_ConcreteAggregationType = Class(name="express_core_ConcreteAggregationType", is_abstract=True)
core_AnonymousType = Class(name="core_AnonymousType")
RepeatStatement = Class(name="RepeatStatement")
express_algorithms_NamedVariable = Class(name="express_algorithms_NamedVariable", is_abstract=True)
express_algorithms_InVariable = Class(name="express_algorithms_InVariable")
InParameter = Class(name="InParameter")
express_algorithms_Procedure = Class(name="express_algorithms_Procedure")
express_algorithms_ActualARRAYType = Class(name="express_algorithms_ActualARRAYType")
ActualAggregationType = Class(name="ActualAggregationType")
GenericType = Class(name="GenericType")
ActualDataType = Class(name="ActualDataType")
express_algorithms_FunctionResult = Class(name="express_algorithms_FunctionResult")
express_algorithms_Function = Class(name="express_algorithms_Function")
express_algorithms_InParameter = Class(name="express_algorithms_InParameter")
InVariable = Class(name="InVariable")
express_algorithms_LocalVariable = Class(name="express_algorithms_LocalVariable")
express_algorithms_ActualStructure = Class(name="express_algorithms_ActualStructure")
algorithms_GenericElement = Class(name="algorithms_GenericElement")
core_AGGREGATEType = Class(name="core_AGGREGATEType")
express_algorithms_ActualGenericType = Class(name="express_algorithms_ActualGenericType")
ActualType = Class(name="ActualType")
express_algorithms_Statement = Class(name="express_algorithms_Statement")
StatementBlock = Class(name="StatementBlock")
SkipStatement = Class(name="SkipStatement")
EscapeStatement = Class(name="EscapeStatement")
express_algorithms_Algorithm = Class(name="express_algorithms_Algorithm", is_abstract=True)
express_algorithms_ActualAggregationType = Class(name="express_algorithms_ActualAggregationType", is_abstract=True)
core_ActualType = Class(name="core_ActualType")
express_algorithms_VARVariable = Class(name="express_algorithms_VARVariable", is_abstract=True)
express_algorithms_ActualSETType = Class(name="express_algorithms_ActualSETType")
express_algorithms_ActualAGGREGATEType = Class(name="express_algorithms_ActualAGGREGATEType")
ActualStructure = Class(name="ActualStructure")
express_algorithms_Parameter = Class(name="express_algorithms_Parameter", is_abstract=True)
express_algorithms_ActualStructureConstraint = Class(name="express_algorithms_ActualStructureConstraint")
AGGREGATEType = Class(name="AGGREGATEType")
express_instances_IntegerValue = Class(name="express_instances_IntegerValue")
RealValue = Class(name="RealValue")
express_instances_AggregateValue = Class(name="express_instances_AggregateValue", is_abstract=True)
ConcreteValue = Class(name="ConcreteValue")
express_instances_Constant = Class(name="express_instances_Constant")
express_instances_LogicalValue = Class(name="express_instances_LogicalValue")
express_instances_TypedInstance = Class(name="express_instances_TypedInstance", is_abstract=True)
express_algorithms_ActualLISTType = Class(name="express_algorithms_ActualLISTType")
express_algorithms_Variable = Class(name="express_algorithms_Variable", is_abstract=True)
express_algorithms_GenericElement = Class(name="express_algorithms_GenericElement", is_abstract=True)
express_algorithms_VARParameter = Class(name="express_algorithms_VARParameter")
algorithms_Parameter = Class(name="algorithms_Parameter")
express_algorithms_ActualDataType = Class(name="express_algorithms_ActualDataType")
core_GenericType = Class(name="core_GenericType")
express_algorithms_ActualBAGType = Class(name="express_algorithms_ActualBAGType")
express_instances_AttributeValue = Class(name="express_instances_AttributeValue")
express_instances_ARRAYValue = Class(name="express_instances_ARRAYValue")
AggregateValue = Class(name="AggregateValue")
ArrayMember = Class(name="ArrayMember")
express_instances_RoleName = Class(name="express_instances_RoleName")
StringValue = Class(name="StringValue")
express_instances_EntityInstance = Class(name="express_instances_EntityInstance")
TypedInstance = Class(name="TypedInstance")
EntityValue = Class(name="EntityValue")
express_instances_EntityValue = Class(name="express_instances_EntityValue")
express_instances_SETValue = Class(name="express_instances_SETValue")
express_instances_ListMember = Class(name="express_instances_ListMember")
express_instances_BagMember = Class(name="express_instances_BagMember")
express_instances_SingleEntityValue = Class(name="express_instances_SingleEntityValue")
express_instances_Indeterminate = Class(name="express_instances_Indeterminate")
express_instances_SingleLeafInstance = Class(name="express_instances_SingleLeafInstance")
express_instances_GenericAggregate = Class(name="express_instances_GenericAggregate")
LISTValue = Class(name="LISTValue")
express_instances_BinaryValue = Class(name="express_instances_BinaryValue")
express_instances_SpecializedValue = Class(name="express_instances_SpecializedValue")
express_instances_BAGValue = Class(name="express_instances_BAGValue")
BagMember = Class(name="BagMember")
express_instances_EnumerationItem = Class(name="express_instances_EnumerationItem")
instances_TypedInstance = Class(name="instances_TypedInstance")
instances_ConcreteValue = Class(name="instances_ConcreteValue")
express_instances_ArrayMember = Class(name="express_instances_ArrayMember")
express_instances_Population = Class(name="express_instances_Population")
express_instances_RealValue = Class(name="express_instances_RealValue")
NumberValue = Class(name="NumberValue")
express_instances_NumberValue = Class(name="express_instances_NumberValue")
express_instances_BooleanValue = Class(name="express_instances_BooleanValue")
LogicalValue = Class(name="LogicalValue")
express_instances_MultiLeafInstance = Class(name="express_instances_MultiLeafInstance")
express_instances_LISTValue = Class(name="express_instances_LISTValue")
express_instances_SimpleValue = Class(name="express_instances_SimpleValue", is_abstract=True)
core_Instance = Class(name="core_Instance")
instances_AggregateValue = Class(name="instances_AggregateValue")
express_instances_ConcreteValue = Class(name="express_instances_ConcreteValue", is_abstract=True)
express_instances_StringValue = Class(name="express_instances_StringValue")
express_instances_TypeName = Class(name="express_instances_TypeName")
express_instances_PartialEntityValue = Class(name="express_instances_PartialEntityValue")
SingleEntityValue = Class(name="SingleEntityValue")

# express_rules_ONEOFConstraint class attributes and methods

# SubtypeConstraint class attributes and methods

# express_rules_SupertypeRule class attributes and methods
express_rules_SupertypeRule_assertsAbstract: Property = Property(name="assertsAbstract", type=StringType)
express_rules_SupertypeRule.attributes={express_rules_SupertypeRule_assertsAbstract}

# CommonElement class attributes and methods

# EntityType class attributes and methods

# express_statements_ProcedureCall class attributes and methods

# Procedure class attributes and methods

# ActualParameter class attributes and methods

# express_rules_SubtypeConstraint class attributes and methods

# Extent class attributes and methods

# Expression class attributes and methods

# SupertypeRule class attributes and methods

# express_rules_Extent class attributes and methods

# SETValue class attributes and methods

# EntityInstance class attributes and methods

# Population class attributes and methods

# GlobalRule class attributes and methods

# ScopedId class attributes and methods

# express_rules_TOTAL_OVERConstraint class attributes and methods

# express_rules_ANDConstraint class attributes and methods

# express_rules_GlobalRule class attributes and methods

# core_SchemaElement class attributes and methods

# core_AlgorithmScope class attributes and methods

# Statement class attributes and methods

# NamedRule class attributes and methods

# express_rules_NamedRule class attributes and methods
express_rules_NamedRule_position: Property = Property(name="position", type=StringType)
express_rules_NamedRule.attributes={express_rules_NamedRule_position}

# LocalElement class attributes and methods

# express_statements_CaseAction class attributes and methods
express_statements_CaseAction_isDefault: Property = Property(name="isDefault", type=StringType)
express_statements_CaseAction.attributes={express_statements_CaseAction_isDefault}

# express_statements_SkipStatement class attributes and methods

# ControlStatement class attributes and methods

# express_statements_AliasStatement class attributes and methods

# algorithms_Statement class attributes and methods

# core_LocalScope class attributes and methods

# VARExpression class attributes and methods

# AliasVariable class attributes and methods

# express_statements_ControlVariable class attributes and methods

# NamedVariable class attributes and methods

# express_statements_AliasVariable class attributes and methods

# algorithms_NamedVariable class attributes and methods

# algorithms_VARVariable class attributes and methods

# express_statements_ControlStatement class attributes and methods

# express_statements_VARCell class attributes and methods
express_statements_VARCell_id: Property = Property(name="id", type=StringType)
express_statements_VARCell.attributes={express_statements_VARCell_id}

# VARVariable class attributes and methods

# express_statements_NullStatement class attributes and methods

# express_statements_VARExpression class attributes and methods
express_statements_VARExpression_text: Property = Property(name="text", type=StringType)
express_statements_VARExpression.attributes={express_statements_VARExpression_text}

# express_statements_AttributeCell class attributes and methods
express_statements_AttributeCell_id: Property = Property(name="id", type=StringType)
express_statements_AttributeCell.attributes={express_statements_AttributeCell_id}

# ExplicitAttribute class attributes and methods

# express_statements_StatementBlock class attributes and methods
express_statements_StatementBlock_delimited: Property = Property(name="delimited", type=StringType)
express_statements_StatementBlock.attributes={express_statements_StatementBlock_delimited}

# express_statements_IfStatement class attributes and methods

# express_statements_MemberCell class attributes and methods

# express_statements_RepeatStatement class attributes and methods

# ControlVariable class attributes and methods

# express_statements_GroupCell class attributes and methods
express_statements_GroupCell_id: Property = Property(name="id", type=StringType)
express_statements_GroupCell.attributes={express_statements_GroupCell_id}

# SingleEntityType class attributes and methods

# express_statements_VariableCell class attributes and methods
express_statements_VariableCell_id: Property = Property(name="id", type=StringType)
express_statements_VariableCell.attributes={express_statements_VariableCell_id}

# Variable class attributes and methods

# express_statements_CaseStatement class attributes and methods

# CaseAction class attributes and methods

# Indeterminate class attributes and methods

# express_expressions_SELFRef class attributes and methods

# express_expressions_IndexOperation class attributes and methods

# express_statements_EscapeStatement class attributes and methods

# express_statements_ReturnStatement class attributes and methods

# express_statements_Assignment class attributes and methods

# express_expressions_Selector class attributes and methods

# express_expressions_RepeatCount class attributes and methods

# express_expressions_EnumItemRef class attributes and methods
express_expressions_EnumItemRef_id: Property = Property(name="id", type=StringType)
express_expressions_EnumItemRef.attributes={express_expressions_EnumItemRef_id}

# Primary class attributes and methods

# EnumerationItem class attributes and methods

# express_expressions_Literal class attributes and methods

# SimpleValue class attributes and methods

# express_expressions_BinaryIndex class attributes and methods

# IndexOperation class attributes and methods

# express_expressions_ActualParameter class attributes and methods
express_expressions_ActualParameter_position: Property = Property(name="position", type=StringType)
express_expressions_ActualParameter.attributes={express_expressions_ActualParameter_position}

# express_expressions_IndeterminateRef class attributes and methods

# ProcedureCall class attributes and methods

# FunctionCall class attributes and methods

# Parameter class attributes and methods

# express_expressions_BinaryOperation class attributes and methods
express_expressions_BinaryOperation_operator: Property = Property(name="operator", type=StringType)
express_expressions_BinaryOperation.attributes={express_expressions_BinaryOperation_operator}

# Operation class attributes and methods

# express_expressions_ParameterRef class attributes and methods
express_expressions_ParameterRef_id: Property = Property(name="id", type=StringType)
express_expressions_ParameterRef.attributes={express_expressions_ParameterRef_id}

# express_expressions_AggregateInitializer class attributes and methods

# GenericAggregate class attributes and methods

# MemberBinding class attributes and methods

# express_expressions_StringIndex class attributes and methods

# express_expressions_PartialEntityConstructor class attributes and methods
express_expressions_PartialEntityConstructor_id: Property = Property(name="id", type=StringType)
express_expressions_PartialEntityConstructor.attributes={express_expressions_PartialEntityConstructor_id}

# PartialEntityValue class attributes and methods

# AttributeBinding class attributes and methods

# express_expressions_Coercion class attributes and methods

# VariableType class attributes and methods

# express_expressions_Primary class attributes and methods

# QueryVariable class attributes and methods

# express_expressions_QueryVariable class attributes and methods

# express_expressions_Operation class attributes and methods

# express_expressions_AttributeBinding class attributes and methods
express_expressions_AttributeBinding_position: Property = Property(name="position", type=StringType)
express_expressions_AttributeBinding.attributes={express_expressions_AttributeBinding_position}

# AttributeValue class attributes and methods

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

# express_core_TypeElement class attributes and methods

# NamedElement class attributes and methods

# express_core_SingleEntityType class attributes and methods

# PartialEntityType class attributes and methods

# express_core_AGGREGATEType class attributes and methods

# GeneralizedType class attributes and methods

# SizeConstraint class attributes and methods

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

# EnumerationType class attributes and methods

# express_core_VariableType class attributes and methods

# core_DataType class attributes and methods

# core_AttributeType class attributes and methods

# express_core_ArrayBound class attributes and methods
express_core_ArrayBound_bound: Property = Property(name="bound", type=StringType)
express_core_ArrayBound.attributes={express_core_ArrayBound_bound}

# ParameterType class attributes and methods

# ActualStructureConstraint class attributes and methods

# express_core_GeneralBAGType class attributes and methods

# GeneralAggregationType class attributes and methods

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

# RangeRole class attributes and methods

# UniqueRule class attributes and methods

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

# express_core_GeneralizedType class attributes and methods

# core_ParameterType class attributes and methods

# express_core_InterfacedElement class attributes and methods
express_core_InterfacedElement_isUSE: Property = Property(name="isUSE", type=StringType)
express_core_InterfacedElement.attributes={express_core_InterfacedElement_isUSE}

# Schema class attributes and methods

# express_core_DataType class attributes and methods

# express_core_PartialEntityType class attributes and methods

# express_core_Schema class attributes and methods
express_core_Schema_name: Property = Property(name="name", type=StringType)
express_core_Schema_version: Property = Property(name="version", type=StringType)
express_core_Schema.attributes={express_core_Schema_version, express_core_Schema_name}

# Remark class attributes and methods

# InterfacedElement class attributes and methods

# SchemaElement class attributes and methods

# express_core_InvertibleAttribute class attributes and methods

# InverseAttribute class attributes and methods

# Relationship class attributes and methods

# express_core_Attribute class attributes and methods
express_core_Attribute_isAbstract: Property = Property(name="isAbstract", type=StringType)
express_core_Attribute_position: Property = Property(name="position", type=StringType)
express_core_Attribute.attributes={express_core_Attribute_position, express_core_Attribute_isAbstract}

# express_core_NumericType class attributes and methods

# SimpleType class attributes and methods

# express_core_DefinedType class attributes and methods

# core_ConcreteType class attributes and methods

# express_core_UniqueRule class attributes and methods
express_core_UniqueRule_position: Property = Property(name="position", type=StringType)
express_core_UniqueRule.attributes={express_core_UniqueRule_position}

# TypeElement class attributes and methods

# express_core_DomainRole class attributes and methods

# express_core_DomainConstraint class attributes and methods

# express_core_InstantiableType class attributes and methods

# core_VariableType class attributes and methods

# express_core_GeneralLISTType class attributes and methods

# express_core_NamedElement class attributes and methods

# express_core_Instance class attributes and methods

# express_core_AttributeType class attributes and methods

# DomainConstraint class attributes and methods

# express_core_DerivedAttribute class attributes and methods

# express_core_BAGType class attributes and methods

# express_core_RealType class attributes and methods
express_core_RealType_precision: Property = Property(name="precision", type=StringType)
express_core_RealType.attributes={express_core_RealType_precision}

# NumericType class attributes and methods

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

# express_core_SETType class attributes and methods

# express_core_SpecializedType class attributes and methods

# ConcreteType class attributes and methods

# express_core_GeneralARRAYType class attributes and methods
express_core_GeneralARRAYType_isOptional: Property = Property(name="isOptional", type=StringType)
express_core_GeneralARRAYType.attributes={express_core_GeneralARRAYType_isOptional}

# ArrayBound class attributes and methods

# express_core_RangeRole class attributes and methods

# express_core_LocalElement class attributes and methods

# express_core_Remark class attributes and methods
express_core_Remark_isTagged: Property = Property(name="isTagged", type=StringType)
express_core_Remark_isTail: Property = Property(name="isTail", type=StringType)
express_core_Remark_text: Property = Property(name="text", type=StringType)
express_core_Remark.attributes={express_core_Remark_isTagged, express_core_Remark_text, express_core_Remark_isTail}

# express_core_SizeConstraint class attributes and methods
express_core_SizeConstraint_bound: Property = Property(name="bound", type=StringType)
express_core_SizeConstraint.attributes={express_core_SizeConstraint_bound}

# express_core_Role class attributes and methods

# express_core_Scope class attributes and methods

# express_core_ParameterType class attributes and methods

# express_core_SelectType class attributes and methods
express_core_SelectType_isExtensible: Property = Property(name="isExtensible", type=StringType)
express_core_SelectType_isEntity: Property = Property(name="isEntity", type=StringType)
express_core_SelectType.attributes={express_core_SelectType_isEntity, express_core_SelectType_isExtensible}

# express_core_Relationship class attributes and methods

# express_core_LengthConstraint class attributes and methods
express_core_LengthConstraint_maxLength: Property = Property(name="maxLength", type=StringType)
express_core_LengthConstraint_isFixed: Property = Property(name="isFixed", type=StringType)
express_core_LengthConstraint.attributes={express_core_LengthConstraint_isFixed, express_core_LengthConstraint_maxLength}

# express_core_LocalScope class attributes and methods

# express_core_NamedType class attributes and methods

# core_Scope class attributes and methods

# core_CommonElement class attributes and methods

# SelectType class attributes and methods

# DomainRule class attributes and methods

# express_core_BinaryType class attributes and methods

# express_core_ScopedId class attributes and methods
express_core_ScopedId_localName: Property = Property(name="localName", type=StringType)
express_core_ScopedId.attributes={express_core_ScopedId_localName}

# express_core_AggregationType class attributes and methods
express_core_AggregationType_isUnique: Property = Property(name="isUnique", type=StringType)
express_core_AggregationType_ordering: Property = Property(name="ordering", type=StringType)
express_core_AggregationType.attributes={express_core_AggregationType_ordering, express_core_AggregationType_isUnique}

# express_core_ARRAYType class attributes and methods
express_core_ARRAYType_isOptional: Property = Property(name="isOptional", type=StringType)
express_core_ARRAYType.attributes={express_core_ARRAYType_isOptional}

# express_algorithms_ActualTypeConstraint class attributes and methods
express_algorithms_ActualTypeConstraint_label: Property = Property(name="label", type=StringType)
express_algorithms_ActualTypeConstraint.attributes={express_algorithms_ActualTypeConstraint_label}

# express_core_ActualType class attributes and methods

# Algorithm class attributes and methods

# express_core_ExplicitAttribute class attributes and methods
express_core_ExplicitAttribute_isOptional: Property = Property(name="isOptional", type=StringType)
express_core_ExplicitAttribute.attributes={express_core_ExplicitAttribute_isOptional}

# express_core_SimpleType class attributes and methods
express_core_SimpleType_id: Property = Property(name="id", type=StringType)
express_core_SimpleType.attributes={express_core_SimpleType_id}

# express_core_CommonElement class attributes and methods

# AlgorithmScope class attributes and methods

# express_core_SchemaElement class attributes and methods

# express_core_ConcreteAggregationType class attributes and methods

# core_AnonymousType class attributes and methods

# RepeatStatement class attributes and methods

# express_algorithms_NamedVariable class attributes and methods

# express_algorithms_InVariable class attributes and methods

# InParameter class attributes and methods

# express_algorithms_Procedure class attributes and methods

# express_algorithms_ActualARRAYType class attributes and methods
express_algorithms_ActualARRAYType_isOptional: Property = Property(name="isOptional", type=StringType)
express_algorithms_ActualARRAYType.attributes={express_algorithms_ActualARRAYType_isOptional}

# ActualAggregationType class attributes and methods

# GenericType class attributes and methods

# ActualDataType class attributes and methods

# express_algorithms_FunctionResult class attributes and methods

# express_algorithms_Function class attributes and methods

# express_algorithms_InParameter class attributes and methods

# InVariable class attributes and methods

# express_algorithms_LocalVariable class attributes and methods

# express_algorithms_ActualStructure class attributes and methods

# algorithms_GenericElement class attributes and methods

# core_AGGREGATEType class attributes and methods

# express_algorithms_ActualGenericType class attributes and methods
express_algorithms_ActualGenericType_isEntity: Property = Property(name="isEntity", type=StringType)
express_algorithms_ActualGenericType_label: Property = Property(name="label", type=StringType)
express_algorithms_ActualGenericType.attributes={express_algorithms_ActualGenericType_label, express_algorithms_ActualGenericType_isEntity}

# ActualType class attributes and methods

# express_algorithms_Statement class attributes and methods
express_algorithms_Statement_text: Property = Property(name="text", type=StringType)
express_algorithms_Statement.attributes={express_algorithms_Statement_text}

# StatementBlock class attributes and methods

# SkipStatement class attributes and methods

# EscapeStatement class attributes and methods

# express_algorithms_Algorithm class attributes and methods

# express_algorithms_ActualAggregationType class attributes and methods

# core_ActualType class attributes and methods

# express_algorithms_VARVariable class attributes and methods

# express_algorithms_ActualSETType class attributes and methods

# express_algorithms_ActualAGGREGATEType class attributes and methods
express_algorithms_ActualAGGREGATEType_label: Property = Property(name="label", type=StringType)
express_algorithms_ActualAGGREGATEType.attributes={express_algorithms_ActualAGGREGATEType_label}

# ActualStructure class attributes and methods

# express_algorithms_Parameter class attributes and methods
express_algorithms_Parameter_inout: Property = Property(name="inout", type=StringType)
express_algorithms_Parameter_position: Property = Property(name="position", type=StringType)
express_algorithms_Parameter.attributes={express_algorithms_Parameter_position, express_algorithms_Parameter_inout}

# express_algorithms_ActualStructureConstraint class attributes and methods
express_algorithms_ActualStructureConstraint_label: Property = Property(name="label", type=StringType)
express_algorithms_ActualStructureConstraint.attributes={express_algorithms_ActualStructureConstraint_label}

# AGGREGATEType class attributes and methods

# express_instances_IntegerValue class attributes and methods

# RealValue class attributes and methods

# express_instances_AggregateValue class attributes and methods

# ConcreteValue class attributes and methods

# express_instances_Constant class attributes and methods

# express_instances_LogicalValue class attributes and methods

# express_instances_TypedInstance class attributes and methods

# express_algorithms_ActualLISTType class attributes and methods

# express_algorithms_Variable class attributes and methods

# express_algorithms_GenericElement class attributes and methods

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

# StringValue class attributes and methods

# express_instances_EntityInstance class attributes and methods
express_instances_EntityInstance_id: Property = Property(name="id", type=StringType)
express_instances_EntityInstance.attributes={express_instances_EntityInstance_id}

# TypedInstance class attributes and methods

# EntityValue class attributes and methods

# express_instances_EntityValue class attributes and methods

# express_instances_SETValue class attributes and methods

# express_instances_ListMember class attributes and methods
express_instances_ListMember_position: Property = Property(name="position", type=StringType)
express_instances_ListMember.attributes={express_instances_ListMember_position}

# express_instances_BagMember class attributes and methods
express_instances_BagMember_count: Property = Property(name="count", type=StringType)
express_instances_BagMember.attributes={express_instances_BagMember_count}

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

# express_instances_ArrayMember class attributes and methods
express_instances_ArrayMember_index: Property = Property(name="index", type=StringType)
express_instances_ArrayMember.attributes={express_instances_ArrayMember_index}

# express_instances_Population class attributes and methods

# express_instances_RealValue class attributes and methods

# NumberValue class attributes and methods

# express_instances_NumberValue class attributes and methods

# express_instances_BooleanValue class attributes and methods

# LogicalValue class attributes and methods

# express_instances_MultiLeafInstance class attributes and methods

# express_instances_LISTValue class attributes and methods

# express_instances_SimpleValue class attributes and methods
express_instances_SimpleValue_name: Property = Property(name="name", type=StringType)
express_instances_SimpleValue.attributes={express_instances_SimpleValue_name}

# core_Instance class attributes and methods

# instances_AggregateValue class attributes and methods

# express_instances_ConcreteValue class attributes and methods

# express_instances_StringValue class attributes and methods

# express_instances_TypeName class attributes and methods

# express_instances_PartialEntityValue class attributes and methods

# SingleEntityValue class attributes and methods

# Relationships
assertsExpression21: BinaryAssociation = BinaryAssociation(
    name="assertsExpression21",
    ends={
        Property(name="Expression22", type=express_rules_NamedRule, multiplicity=Multiplicity(1, 1)),
        Property(name="express_rules_NamedRule", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
invokes23: BinaryAssociation = BinaryAssociation(
    name="invokes23",
    ends={
        Property(name="Procedure", type=express_statements_ProcedureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_ProcedureCall", type=Procedure, multiplicity=Multiplicity(1, 1))
    }
)
actualParameters24: BinaryAssociation = BinaryAssociation(
    name="actualParameters24",
    ends={
        Property(name="ActualParameter", type=express_statements_ProcedureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="inProcedureCall", type=ActualParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
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
        Property(name="SubtypeConstraint", type=express_rules_SupertypeRule, multiplicity=Multiplicity(1, 1)),
        Property(name="collection", type=SubtypeConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constrainedSubtypes2: BinaryAssociation = BinaryAssociation(
    name="constrainedSubtypes2",
    ends={
        Property(name="Extent", type=express_rules_SubtypeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="constraints", type=Extent, multiplicity=Multiplicity(1, 9999))
    }
)
equivalentRule3: BinaryAssociation = BinaryAssociation(
    name="equivalentRule3",
    ends={
        Property(name="Expression", type=express_rules_SubtypeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="express_rules_SubtypeConstraint", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
collection4: BinaryAssociation = BinaryAssociation(
    name="collection4",
    ends={
        Property(name="SupertypeRule", type=express_rules_SubtypeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="constraints5", type=SupertypeRule, multiplicity=Multiplicity(1, 1))
    }
)
constraints6: BinaryAssociation = BinaryAssociation(
    name="constraints6",
    ends={
        Property(name="SubtypeConstraint7", type=express_rules_Extent, multiplicity=Multiplicity(1, 1)),
        Property(name="constrainedSubtypes", type=SubtypeConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
content8: BinaryAssociation = BinaryAssociation(
    name="content8",
    ends={
        Property(name="EntityInstance", type=express_rules_Extent, multiplicity=Multiplicity(1, 1)),
        Property(name="express_rules_Extent", type=EntityInstance, multiplicity=Multiplicity(0, 9999))
    }
)
withinPopulation9: BinaryAssociation = BinaryAssociation(
    name="withinPopulation9",
    ends={
        Property(name="Population", type=express_rules_Extent, multiplicity=Multiplicity(1, 1)),
        Property(name="express_rules_Extent10", type=Population, multiplicity=Multiplicity(1, 1))
    }
)
constraintRules11: BinaryAssociation = BinaryAssociation(
    name="constraintRules11",
    ends={
        Property(name="GlobalRule", type=express_rules_Extent, multiplicity=Multiplicity(1, 1)),
        Property(name="constrainedExtents", type=GlobalRule, multiplicity=Multiplicity(0, 9999))
    }
)
forType12: BinaryAssociation = BinaryAssociation(
    name="forType12",
    ends={
        Property(name="EntityType13", type=express_rules_Extent, multiplicity=Multiplicity(1, 1)),
        Property(name="extension", type=EntityType, multiplicity=Multiplicity(1, 1))
    }
)
id14: BinaryAssociation = BinaryAssociation(
    name="id14",
    ends={
        Property(name="ScopedId", type=express_rules_Extent, multiplicity=Multiplicity(1, 1)),
        Property(name="express_rules_Extent15", type=ScopedId, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
supportingBody16: BinaryAssociation = BinaryAssociation(
    name="supportingBody16",
    ends={
        Property(name="Statement", type=express_rules_GlobalRule, multiplicity=Multiplicity(1, 1)),
        Property(name="express_rules_GlobalRule", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constrainedExtents17: BinaryAssociation = BinaryAssociation(
    name="constrainedExtents17",
    ends={
        Property(name="Extent18", type=express_rules_GlobalRule, multiplicity=Multiplicity(1, 1)),
        Property(name="constraintRules", type=Extent, multiplicity=Multiplicity(1, 9999))
    }
)
containsRules19: BinaryAssociation = BinaryAssociation(
    name="containsRules19",
    ends={
        Property(name="NamedRule", type=express_rules_GlobalRule, multiplicity=Multiplicity(1, 1)),
        Property(name="express_rules_GlobalRule20", type=NamedRule, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
bodyStatements_Statement46: BinaryAssociation = BinaryAssociation(
    name="bodyStatements_Statement46",
    ends={
        Property(name="Statement47", type=express_statements_StatementBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="inBlock", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
labelValue48: BinaryAssociation = BinaryAssociation(
    name="labelValue48",
    ends={
        Property(name="Expression49", type=express_statements_CaseAction, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_CaseAction", type=Expression, multiplicity=Multiplicity(0, 9999))
    }
)
action50: BinaryAssociation = BinaryAssociation(
    name="action50",
    ends={
        Property(name="Statement52", type=express_statements_CaseAction, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_CaseAction51", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bindsToReference25: BinaryAssociation = BinaryAssociation(
    name="bindsToReference25",
    ends={
        Property(name="VARExpression", type=express_statements_AliasStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_AliasStatement", type=VARExpression, multiplicity=Multiplicity(1, 1))
    }
)
body26: BinaryAssociation = BinaryAssociation(
    name="body26",
    ends={
        Property(name="Statement28", type=express_statements_AliasStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_AliasStatement27", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
aliasVariable29: BinaryAssociation = BinaryAssociation(
    name="aliasVariable29",
    ends={
        Property(name="AliasVariable", type=express_statements_AliasStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_AliasStatement30", type=AliasVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
boundValue31: BinaryAssociation = BinaryAssociation(
    name="boundValue31",
    ends={
        Property(name="Expression32", type=express_statements_ControlVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_ControlVariable", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
initialValue33: BinaryAssociation = BinaryAssociation(
    name="initialValue33",
    ends={
        Property(name="Expression35", type=express_statements_ControlVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_ControlVariable34", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
increment36: BinaryAssociation = BinaryAssociation(
    name="increment36",
    ends={
        Property(name="Expression38", type=express_statements_ControlVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_ControlVariable37", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
referent39: BinaryAssociation = BinaryAssociation(
    name="referent39",
    ends={
        Property(name="VARExpression40", type=express_statements_AliasVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_AliasVariable", type=VARExpression, multiplicity=Multiplicity(0, 1))
    }
)
refersTo41: BinaryAssociation = BinaryAssociation(
    name="refersTo41",
    ends={
        Property(name="VARVariable", type=express_statements_VARCell, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_VARCell", type=VARVariable, multiplicity=Multiplicity(1, 1))
    }
)
refersTo42: BinaryAssociation = BinaryAssociation(
    name="refersTo42",
    ends={
        Property(name="ExplicitAttribute", type=express_statements_AttributeCell, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_AttributeCell", type=ExplicitAttribute, multiplicity=Multiplicity(1, 1))
    }
)
baseEntity43: BinaryAssociation = BinaryAssociation(
    name="baseEntity43",
    ends={
        Property(name="VARExpression45", type=express_statements_AttributeCell, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_AttributeCell44", type=VARExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ifCondition76: BinaryAssociation = BinaryAssociation(
    name="ifCondition76",
    ends={
        Property(name="Expression77", type=express_statements_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_IfStatement", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseActions78: BinaryAssociation = BinaryAssociation(
    name="elseActions78",
    ends={
        Property(name="Statement80", type=express_statements_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_IfStatement79", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenActions81: BinaryAssociation = BinaryAssociation(
    name="thenActions81",
    ends={
        Property(name="Statement83", type=express_statements_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_IfStatement82", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
indexValue53: BinaryAssociation = BinaryAssociation(
    name="indexValue53",
    ends={
        Property(name="Expression54", type=express_statements_MemberCell, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_MemberCell", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
baseAggregate55: BinaryAssociation = BinaryAssociation(
    name="baseAggregate55",
    ends={
        Property(name="VARExpression57", type=express_statements_MemberCell, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_MemberCell56", type=VARExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
whileExpression58: BinaryAssociation = BinaryAssociation(
    name="whileExpression58",
    ends={
        Property(name="Expression59", type=express_statements_RepeatStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_RepeatStatement", type=Expression, multiplicity=Multiplicity(0, 1))
    }
)
body60: BinaryAssociation = BinaryAssociation(
    name="body60",
    ends={
        Property(name="Statement61", type=express_statements_RepeatStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="controlledBy", type=Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
controlVariable62: BinaryAssociation = BinaryAssociation(
    name="controlVariable62",
    ends={
        Property(name="ControlVariable", type=express_statements_RepeatStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_RepeatStatement63", type=ControlVariable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
untilExpression64: BinaryAssociation = BinaryAssociation(
    name="untilExpression64",
    ends={
        Property(name="Expression66", type=express_statements_RepeatStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_RepeatStatement65", type=Expression, multiplicity=Multiplicity(0, 1))
    }
)
baseEntity67: BinaryAssociation = BinaryAssociation(
    name="baseEntity67",
    ends={
        Property(name="VARExpression68", type=express_statements_GroupCell, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_GroupCell", type=VARExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
refersTo69: BinaryAssociation = BinaryAssociation(
    name="refersTo69",
    ends={
        Property(name="SingleEntityType", type=express_statements_GroupCell, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_GroupCell70", type=SingleEntityType, multiplicity=Multiplicity(1, 1))
    }
)
refersTo71: BinaryAssociation = BinaryAssociation(
    name="refersTo71",
    ends={
        Property(name="Variable", type=express_statements_VariableCell, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_VariableCell", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
cases72: BinaryAssociation = BinaryAssociation(
    name="cases72",
    ends={
        Property(name="CaseAction", type=express_statements_CaseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_CaseStatement", type=CaseAction, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
selectionExpression73: BinaryAssociation = BinaryAssociation(
    name="selectionExpression73",
    ends={
        Property(name="Expression75", type=express_statements_CaseStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_CaseStatement74", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
refersTo102: BinaryAssociation = BinaryAssociation(
    name="refersTo102",
    ends={
        Property(name="Indeterminate", type=express_expressions_IndeterminateRef, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_IndeterminateRef", type=Indeterminate, multiplicity=Multiplicity(1, 1))
    }
)
baseValue103: BinaryAssociation = BinaryAssociation(
    name="baseValue103",
    ends={
        Property(name="Expression104", type=express_expressions_IndexOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_IndexOperation", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
returnValue84: BinaryAssociation = BinaryAssociation(
    name="returnValue84",
    ends={
        Property(name="Expression85", type=express_statements_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_ReturnStatement", type=Expression, multiplicity=Multiplicity(0, 1))
    }
)
assignedValue86: BinaryAssociation = BinaryAssociation(
    name="assignedValue86",
    ends={
        Property(name="Expression87", type=express_statements_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_Assignment", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
variable88: BinaryAssociation = BinaryAssociation(
    name="variable88",
    ends={
        Property(name="VARExpression90", type=express_statements_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="express_statements_Assignment89", type=VARExpression, multiplicity=Multiplicity(1, 1))
    }
)
entityInstance91: BinaryAssociation = BinaryAssociation(
    name="entityInstance91",
    ends={
        Property(name="Expression92", type=express_expressions_Selector, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_Selector", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
derivation93: BinaryAssociation = BinaryAssociation(
    name="derivation93",
    ends={
        Property(name="Expression94", type=express_expressions_RepeatCount, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_RepeatCount", type=Expression, multiplicity=Multiplicity(0, 1))
    }
)
refersTo95: BinaryAssociation = BinaryAssociation(
    name="refersTo95",
    ends={
        Property(name="EnumerationItem", type=express_expressions_EnumItemRef, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_EnumItemRef", type=EnumerationItem, multiplicity=Multiplicity(1, 1))
    }
)
refersTo96: BinaryAssociation = BinaryAssociation(
    name="refersTo96",
    ends={
        Property(name="SimpleValue", type=express_expressions_Literal, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_Literal", type=SimpleValue, multiplicity=Multiplicity(1, 1))
    }
)
firstBit97: BinaryAssociation = BinaryAssociation(
    name="firstBit97",
    ends={
        Property(name="Expression98", type=express_expressions_BinaryIndex, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_BinaryIndex", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
lastBit99: BinaryAssociation = BinaryAssociation(
    name="lastBit99",
    ends={
        Property(name="Expression101", type=express_expressions_BinaryIndex, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_BinaryIndex100", type=Expression, multiplicity=Multiplicity(0, 1))
    }
)
inProcedureCall128: BinaryAssociation = BinaryAssociation(
    name="inProcedureCall128",
    ends={
        Property(name="ProcedureCall", type=express_expressions_ActualParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="actualParameters", type=ProcedureCall, multiplicity=Multiplicity(0, 1))
    }
)
inFunctionCall129: BinaryAssociation = BinaryAssociation(
    name="inFunctionCall129",
    ends={
        Property(name="FunctionCall", type=express_expressions_ActualParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="actualParameters130", type=FunctionCall, multiplicity=Multiplicity(0, 1))
    }
)
formalParameter131: BinaryAssociation = BinaryAssociation(
    name="formalParameter131",
    ends={
        Property(name="Parameter", type=express_expressions_ActualParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_ActualParameter", type=Parameter_, multiplicity=Multiplicity(1, 1))
    }
)
actualReferent132: BinaryAssociation = BinaryAssociation(
    name="actualReferent132",
    ends={
        Property(name="VARExpression134", type=express_expressions_ActualParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_ActualParameter133", type=VARExpression, multiplicity=Multiplicity(0, 1))
    }
)
actualValue135: BinaryAssociation = BinaryAssociation(
    name="actualValue135",
    ends={
        Property(name="Expression137", type=express_expressions_ActualParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_ActualParameter136", type=Expression, multiplicity=Multiplicity(0, 1))
    }
)
leftOperand105: BinaryAssociation = BinaryAssociation(
    name="leftOperand105",
    ends={
        Property(name="Expression106", type=express_expressions_BinaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_BinaryOperation", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
rightOperand107: BinaryAssociation = BinaryAssociation(
    name="rightOperand107",
    ends={
        Property(name="Expression109", type=express_expressions_BinaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_BinaryOperation108", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
resultValue110: BinaryAssociation = BinaryAssociation(
    name="resultValue110",
    ends={
        Property(name="GenericAggregate", type=express_expressions_AggregateInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_AggregateInitializer", type=GenericAggregate, multiplicity=Multiplicity(0, 1))
    }
)
bindings111: BinaryAssociation = BinaryAssociation(
    name="bindings111",
    ends={
        Property(name="MemberBinding", type=express_expressions_AggregateInitializer, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_AggregateInitializer112", type=MemberBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
firstCode113: BinaryAssociation = BinaryAssociation(
    name="firstCode113",
    ends={
        Property(name="Expression114", type=express_expressions_StringIndex, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_StringIndex", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
lastCode115: BinaryAssociation = BinaryAssociation(
    name="lastCode115",
    ends={
        Property(name="Expression117", type=express_expressions_StringIndex, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_StringIndex116", type=Expression, multiplicity=Multiplicity(0, 1))
    }
)
resultValue118: BinaryAssociation = BinaryAssociation(
    name="resultValue118",
    ends={
        Property(name="PartialEntityValue", type=express_expressions_PartialEntityConstructor, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_PartialEntityConstructor", type=PartialEntityValue, multiplicity=Multiplicity(0, 1))
    }
)
attributeGroup119: BinaryAssociation = BinaryAssociation(
    name="attributeGroup119",
    ends={
        Property(name="SingleEntityType121", type=express_expressions_PartialEntityConstructor, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_PartialEntityConstructor120", type=SingleEntityType, multiplicity=Multiplicity(1, 1))
    }
)
bindings122: BinaryAssociation = BinaryAssociation(
    name="bindings122",
    ends={
        Property(name="AttributeBinding", type=express_expressions_PartialEntityConstructor, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_PartialEntityConstructor123", type=AttributeBinding, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operand124: BinaryAssociation = BinaryAssociation(
    name="operand124",
    ends={
        Property(name="Expression125", type=express_expressions_Coercion, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_Coercion", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
targetType126: BinaryAssociation = BinaryAssociation(
    name="targetType126",
    ends={
        Property(name="VariableType", type=express_expressions_Coercion, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_Coercion127", type=VariableType, multiplicity=Multiplicity(1, 1))
    }
)
queryVariable152: BinaryAssociation = BinaryAssociation(
    name="queryVariable152",
    ends={
        Property(name="QueryVariable", type=express_expressions_QueryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_QueryExpression153", type=QueryVariable, multiplicity=Multiplicity(1, 1))
    }
)
aggregateOperand154: BinaryAssociation = BinaryAssociation(
    name="aggregateOperand154",
    ends={
        Property(name="Expression156", type=express_expressions_QueryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_QueryExpression155", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
attributeValue157: BinaryAssociation = BinaryAssociation(
    name="attributeValue157",
    ends={
        Property(name="Expression158", type=express_expressions_AttributeBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_AttributeBinding", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
toValue159: BinaryAssociation = BinaryAssociation(
    name="toValue159",
    ends={
        Property(name="AttributeValue", type=express_expressions_AttributeBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_AttributeBinding160", type=AttributeValue, multiplicity=Multiplicity(0, 1))
    }
)
refersTo138: BinaryAssociation = BinaryAssociation(
    name="refersTo138",
    ends={
        Property(name="Parameter139", type=express_expressions_ParameterRef, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_ParameterRef", type=Parameter_, multiplicity=Multiplicity(1, 1))
    }
)
refersTo140: BinaryAssociation = BinaryAssociation(
    name="refersTo140",
    ends={
        Property(name="Attribute", type=express_expressions_AttributeRef, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_AttributeRef", type=Attribute, multiplicity=Multiplicity(1, 1))
    }
)
indexValue141: BinaryAssociation = BinaryAssociation(
    name="indexValue141",
    ends={
        Property(name="Expression142", type=express_expressions_AggregateIndex, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_AggregateIndex", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
refersTo143: BinaryAssociation = BinaryAssociation(
    name="refersTo143",
    ends={
        Property(name="SingleEntityType144", type=express_expressions_GroupRef, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_GroupRef", type=SingleEntityType, multiplicity=Multiplicity(1, 1))
    }
)
unaryOperand145: BinaryAssociation = BinaryAssociation(
    name="unaryOperand145",
    ends={
        Property(name="Expression146", type=express_expressions_UnaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_UnaryOperation", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
inverseOf147: BinaryAssociation = BinaryAssociation(
    name="inverseOf147",
    ends={
        Property(name="Attribute148", type=express_expressions_UsedInRef, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_UsedInRef", type=Attribute, multiplicity=Multiplicity(1, 1))
    }
)
refersTo149: BinaryAssociation = BinaryAssociation(
    name="refersTo149",
    ends={
        Property(name="Constant", type=express_expressions_ConstantRef, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_ConstantRef", type=Constant, multiplicity=Multiplicity(1, 1))
    }
)
selectCondition150: BinaryAssociation = BinaryAssociation(
    name="selectCondition150",
    ends={
        Property(name="Expression151", type=express_expressions_QueryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_QueryExpression", type=Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
declaresExplicitAttribute177: BinaryAssociation = BinaryAssociation(
    name="declaresExplicitAttribute177",
    ends={
        Property(name="ExplicitAttribute178", type=express_core_SingleEntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_SingleEntityType", type=ExplicitAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
declaresAttribute179: BinaryAssociation = BinaryAssociation(
    name="declaresAttribute179",
    ends={
        Property(name="Attribute180", type=express_core_SingleEntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="ofEntity", type=Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
declaredIn181: BinaryAssociation = BinaryAssociation(
    name="declaredIn181",
    ends={
        Property(name="EntityType182", type=express_core_SingleEntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="declares", type=EntityType, multiplicity=Multiplicity(1, 1))
    }
)
equivalent183: BinaryAssociation = BinaryAssociation(
    name="equivalent183",
    ends={
        Property(name="PartialEntityType", type=express_core_SingleEntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_SingleEntityType184", type=PartialEntityType, multiplicity=Multiplicity(1, 1))
    }
)
id185: BinaryAssociation = BinaryAssociation(
    name="id185",
    ends={
        Property(name="ScopedId187", type=express_core_SingleEntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_SingleEntityType186", type=ScopedId, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
attribute161: BinaryAssociation = BinaryAssociation(
    name="attribute161",
    ends={
        Property(name="ExplicitAttribute163", type=express_expressions_AttributeBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_AttributeBinding162", type=ExplicitAttribute, multiplicity=Multiplicity(1, 1))
    }
)
actualParameters164: BinaryAssociation = BinaryAssociation(
    name="actualParameters164",
    ends={
        Property(name="ActualParameter165", type=express_expressions_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="inFunctionCall", type=ActualParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
invokesFunction166: BinaryAssociation = BinaryAssociation(
    name="invokesFunction166",
    ends={
        Property(name="Function", type=express_expressions_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_FunctionCall", type=Function, multiplicity=Multiplicity(1, 1))
    }
)
returnsResult167: BinaryAssociation = BinaryAssociation(
    name="returnsResult167",
    ends={
        Property(name="FunctionResult", type=express_expressions_FunctionCall, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_FunctionCall168", type=FunctionResult, multiplicity=Multiplicity(1, 1))
    }
)
repetition169: BinaryAssociation = BinaryAssociation(
    name="repetition169",
    ends={
        Property(name="RepeatCount", type=express_expressions_MemberBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_MemberBinding", type=RepeatCount, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
toSlot170: BinaryAssociation = BinaryAssociation(
    name="toSlot170",
    ends={
        Property(name="ListMember", type=express_expressions_MemberBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_MemberBinding171", type=ListMember, multiplicity=Multiplicity(0, 9999))
    }
)
memberValue172: BinaryAssociation = BinaryAssociation(
    name="memberValue172",
    ends={
        Property(name="Expression174", type=express_expressions_MemberBinding, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_MemberBinding173", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
refersTo175: BinaryAssociation = BinaryAssociation(
    name="refersTo175",
    ends={
        Property(name="NamedType", type=express_expressions_ExtentRef, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_ExtentRef", type=NamedType, multiplicity=Multiplicity(1, 1))
    }
)
refersTo176: BinaryAssociation = BinaryAssociation(
    name="refersTo176",
    ends={
        Property(name="NamedVariable", type=express_expressions_VariableRef, multiplicity=Multiplicity(1, 1)),
        Property(name="express_expressions_VariableRef", type=NamedVariable, multiplicity=Multiplicity(1, 1))
    }
)
values203: BinaryAssociation = BinaryAssociation(
    name="values203",
    ends={
        Property(name="EnumerationItem204", type=express_core_EnumerationType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_EnumerationType", type=EnumerationItem, multiplicity=Multiplicity(0, 9999))
    }
)
declaredItems205: BinaryAssociation = BinaryAssociation(
    name="declaredItems205",
    ends={
        Property(name="EnumerationItem206", type=express_core_EnumerationType, multiplicity=Multiplicity(1, 1)),
        Property(name="declaredIn", type=EnumerationItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extension207: BinaryAssociation = BinaryAssociation(
    name="extension207",
    ends={
        Property(name="EnumerationType", type=express_core_EnumerationType, multiplicity=Multiplicity(1, 1)),
        Property(name="base", type=EnumerationType, multiplicity=Multiplicity(0, 9999))
    }
)
base208: BinaryAssociation = BinaryAssociation(
    name="base208",
    ends={
        Property(name="EnumerationType210", type=express_core_EnumerationType, multiplicity=Multiplicity(1, 1)),
        Property(name="extension209", type=EnumerationType, multiplicity=Multiplicity(1, 1))
    }
)
boundExpression211: BinaryAssociation = BinaryAssociation(
    name="boundExpression211",
    ends={
        Property(name="Expression212", type=express_core_ArrayBound, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_ArrayBound", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
upperBound188: BinaryAssociation = BinaryAssociation(
    name="upperBound188",
    ends={
        Property(name="SizeConstraint", type=express_core_AGGREGATEType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_AGGREGATEType", type=SizeConstraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
memberType189: BinaryAssociation = BinaryAssociation(
    name="memberType189",
    ends={
        Property(name="ParameterType", type=express_core_AGGREGATEType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_AGGREGATEType190", type=ParameterType, multiplicity=Multiplicity(1, 1))
    }
)
constraint191: BinaryAssociation = BinaryAssociation(
    name="constraint191",
    ends={
        Property(name="ActualStructureConstraint", type=express_core_AGGREGATEType, multiplicity=Multiplicity(1, 1)),
        Property(name="matchingStructure", type=ActualStructureConstraint, multiplicity=Multiplicity(0, 1))
    }
)
lowerBound192: BinaryAssociation = BinaryAssociation(
    name="lowerBound192",
    ends={
        Property(name="SizeConstraint194", type=express_core_AGGREGATEType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_AGGREGATEType193", type=SizeConstraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
memberType195: BinaryAssociation = BinaryAssociation(
    name="memberType195",
    ends={
        Property(name="GeneralizedType", type=express_core_GeneralAggregationType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_GeneralAggregationType", type=GeneralizedType, multiplicity=Multiplicity(1, 1))
    }
)
evaluation196: BinaryAssociation = BinaryAssociation(
    name="evaluation196",
    ends={
        Property(name="Instance", type=express_core_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_Expression", type=Instance, multiplicity=Multiplicity(0, 1))
    }
)
interpretationContext197: BinaryAssociation = BinaryAssociation(
    name="interpretationContext197",
    ends={
        Property(name="Scope", type=express_core_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_Expression198", type=Scope, multiplicity=Multiplicity(0, 1))
    }
)
dataType199: BinaryAssociation = BinaryAssociation(
    name="dataType199",
    ends={
        Property(name="DataType", type=express_core_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_Expression200", type=DataType, multiplicity=Multiplicity(0, 1))
    }
)
modelsRole201: BinaryAssociation = BinaryAssociation(
    name="modelsRole201",
    ends={
        Property(name="DomainRole", type=express_core_InverseAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="rangeView", type=DomainRole, multiplicity=Multiplicity(1, 1))
    }
)
explicit202: BinaryAssociation = BinaryAssociation(
    name="explicit202",
    ends={
        Property(name="InvertibleAttribute", type=express_core_InverseAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="inverse", type=InvertibleAttribute, multiplicity=Multiplicity(1, 1))
    }
)
attributes240: BinaryAssociation = BinaryAssociation(
    name="attributes240",
    ends={
        Property(name="Attribute241", type=express_core_EntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="owningEntity", type=Attribute, multiplicity=Multiplicity(0, 9999))
    }
)
playsRangeRole242: BinaryAssociation = BinaryAssociation(
    name="playsRangeRole242",
    ends={
        Property(name="RangeRole", type=express_core_EntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="range", type=RangeRole, multiplicity=Multiplicity(0, 9999))
    }
)
declares243: BinaryAssociation = BinaryAssociation(
    name="declares243",
    ends={
        Property(name="SingleEntityType245", type=express_core_EntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="declaredIn244", type=SingleEntityType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
extension246: BinaryAssociation = BinaryAssociation(
    name="extension246",
    ends={
        Property(name="Extent247", type=express_core_EntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="forType", type=Extent, multiplicity=Multiplicity(0, 9999))
    }
)
invertibleAttributes248: BinaryAssociation = BinaryAssociation(
    name="invertibleAttributes248",
    ends={
        Property(name="InvertibleAttribute249", type=express_core_EntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="referencingType", type=InvertibleAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
playsDomainRole250: BinaryAssociation = BinaryAssociation(
    name="playsDomainRole250",
    ends={
        Property(name="DomainRole251", type=express_core_EntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="domain", type=DomainRole, multiplicity=Multiplicity(0, 9999))
    }
)
derivation213: BinaryAssociation = BinaryAssociation(
    name="derivation213",
    ends={
        Property(name="Expression214", type=express_core_Redeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_Redeclaration", type=Expression, multiplicity=Multiplicity(0, 1))
    }
)
restrictedType215: BinaryAssociation = BinaryAssociation(
    name="restrictedType215",
    ends={
        Property(name="AttributeType", type=express_core_Redeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_Redeclaration216", type=AttributeType, multiplicity=Multiplicity(1, 1))
    }
)
refines217: BinaryAssociation = BinaryAssociation(
    name="refines217",
    ends={
        Property(name="Redeclaration", type=express_core_Redeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_Redeclaration218", type=Redeclaration, multiplicity=Multiplicity(0, 1))
    }
)
upperBound219: BinaryAssociation = BinaryAssociation(
    name="upperBound219",
    ends={
        Property(name="SizeConstraint221", type=express_core_Redeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_Redeclaration220", type=SizeConstraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
lowerBound222: BinaryAssociation = BinaryAssociation(
    name="lowerBound222",
    ends={
        Property(name="SizeConstraint224", type=express_core_Redeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_Redeclaration223", type=SizeConstraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
scope225: BinaryAssociation = BinaryAssociation(
    name="scope225",
    ends={
        Property(name="EntityType226", type=express_core_Redeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="redeclarations", type=EntityType, multiplicity=Multiplicity(1, 1))
    }
)
originalAttribute227: BinaryAssociation = BinaryAssociation(
    name="originalAttribute227",
    ends={
        Property(name="Attribute229", type=express_core_Redeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_Redeclaration228", type=Attribute, multiplicity=Multiplicity(1, 1))
    }
)
refinedRole230: BinaryAssociation = BinaryAssociation(
    name="refinedRole230",
    ends={
        Property(name="Role", type=express_core_Redeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_Redeclaration231", type=Role, multiplicity=Multiplicity(0, 1))
    }
)
alias232: BinaryAssociation = BinaryAssociation(
    name="alias232",
    ends={
        Property(name="ScopedId234", type=express_core_Redeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_Redeclaration233", type=ScopedId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
playsRole235: BinaryAssociation = BinaryAssociation(
    name="playsRole235",
    ends={
        Property(name="Role237", type=express_core_EntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="ofEntity236", type=Role, multiplicity=Multiplicity(0, 9999))
    }
)
redeclarations238: BinaryAssociation = BinaryAssociation(
    name="redeclarations238",
    ends={
        Property(name="Redeclaration239", type=express_core_EntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="scope", type=Redeclaration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referencingType271: BinaryAssociation = BinaryAssociation(
    name="referencingType271",
    ends={
        Property(name="EntityType272", type=express_core_InvertibleAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="invertibleAttributes", type=EntityType, multiplicity=Multiplicity(1, 9999))
    }
)
modelsRole273: BinaryAssociation = BinaryAssociation(
    name="modelsRole273",
    ends={
        Property(name="RangeRole274", type=express_core_InvertibleAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="domainView", type=RangeRole, multiplicity=Multiplicity(1, 1))
    }
)
occursIn275: BinaryAssociation = BinaryAssociation(
    name="occursIn275",
    ends={
        Property(name="ParameterType276", type=express_core_GeneralizedType, multiplicity=Multiplicity(1, 1)),
        Property(name="contains", type=ParameterType, multiplicity=Multiplicity(1, 9999))
    }
)
interfacingSchema277: BinaryAssociation = BinaryAssociation(
    name="interfacingSchema277",
    ends={
        Property(name="Schema", type=express_core_InterfacedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="interfaces", type=Schema, multiplicity=Multiplicity(1, 1))
    }
)
refersTo278: BinaryAssociation = BinaryAssociation(
    name="refersTo278",
    ends={
        Property(name="SchemaElement279", type=express_core_InterfacedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="referencedAs", type=SchemaElement, multiplicity=Multiplicity(1, 1))
    }
)
uniqueRules252: BinaryAssociation = BinaryAssociation(
    name="uniqueRules252",
    ends={
        Property(name="UniqueRule", type=express_core_EntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="domain253", type=UniqueRule, multiplicity=Multiplicity(0, 9999))
    }
)
usedIn254: BinaryAssociation = BinaryAssociation(
    name="usedIn254",
    ends={
        Property(name="InvertibleAttribute255", type=express_core_EntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="rangeType", type=InvertibleAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
subtypeOf256: BinaryAssociation = BinaryAssociation(
    name="subtypeOf256",
    ends={
        Property(name="EntityType257", type=express_core_EntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_EntityType", type=EntityType, multiplicity=Multiplicity(0, 9999))
    }
)
instances258: BinaryAssociation = BinaryAssociation(
    name="instances258",
    ends={
        Property(name="Instance259", type=express_core_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="ofType", type=Instance, multiplicity=Multiplicity(0, 9999))
    }
)
components260: BinaryAssociation = BinaryAssociation(
    name="components260",
    ends={
        Property(name="SingleEntityType261", type=express_core_PartialEntityType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_PartialEntityType", type=SingleEntityType, multiplicity=Multiplicity(1, 9999))
    }
)
documentation262: BinaryAssociation = BinaryAssociation(
    name="documentation262",
    ends={
        Property(name="Remark", type=express_core_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="describesSchema", type=Remark, multiplicity=Multiplicity(0, 9999))
    }
)
interfaces263: BinaryAssociation = BinaryAssociation(
    name="interfaces263",
    ends={
        Property(name="InterfacedElement", type=express_core_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="interfacingSchema", type=InterfacedElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schemaElements264: BinaryAssociation = BinaryAssociation(
    name="schemaElements264",
    ends={
        Property(name="SchemaElement", type=express_core_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="definedIn", type=SchemaElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interfacedElements265: BinaryAssociation = BinaryAssociation(
    name="interfacedElements265",
    ends={
        Property(name="SchemaElement266", type=express_core_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="referencedIn", type=SchemaElement, multiplicity=Multiplicity(0, 9999))
    }
)
inverse267: BinaryAssociation = BinaryAssociation(
    name="inverse267",
    ends={
        Property(name="InverseAttribute", type=express_core_InvertibleAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="explicit", type=InverseAttribute, multiplicity=Multiplicity(0, 9999))
    }
)
rangeType268: BinaryAssociation = BinaryAssociation(
    name="rangeType268",
    ends={
        Property(name="EntityType269", type=express_core_InvertibleAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="usedIn", type=EntityType, multiplicity=Multiplicity(1, 9999))
    }
)
createsRelationship270: BinaryAssociation = BinaryAssociation(
    name="createsRelationship270",
    ends={
        Property(name="Relationship", type=express_core_InvertibleAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="basedOn", type=Relationship, multiplicity=Multiplicity(1, 1))
    }
)
namespace298: BinaryAssociation = BinaryAssociation(
    name="namespace298",
    ends={
        Property(name="Scope299", type=express_core_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="namedElements", type=Scope, multiplicity=Multiplicity(1, 1))
    }
)
documentation300: BinaryAssociation = BinaryAssociation(
    name="documentation300",
    ends={
        Property(name="Remark301", type=express_core_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="describesElement", type=Remark, multiplicity=Multiplicity(0, 9999))
    }
)
id302: BinaryAssociation = BinaryAssociation(
    name="id302",
    ends={
        Property(name="ScopedId303", type=express_core_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_NamedElement", type=ScopedId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributeType304: BinaryAssociation = BinaryAssociation(
    name="attributeType304",
    ends={
        Property(name="AttributeType305", type=express_core_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="role", type=AttributeType, multiplicity=Multiplicity(1, 1))
    }
)
ofEntity306: BinaryAssociation = BinaryAssociation(
    name="ofEntity306",
    ends={
        Property(name="SingleEntityType307", type=express_core_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="declaresAttribute", type=SingleEntityType, multiplicity=Multiplicity(1, 1))
    }
)
interfacedId280: BinaryAssociation = BinaryAssociation(
    name="interfacedId280",
    ends={
        Property(name="ScopedId281", type=express_core_InterfacedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_InterfacedElement", type=ScopedId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
domain282: BinaryAssociation = BinaryAssociation(
    name="domain282",
    ends={
        Property(name="EntityType283", type=express_core_UniqueRule, multiplicity=Multiplicity(1, 1)),
        Property(name="uniqueRules", type=EntityType, multiplicity=Multiplicity(1, 1))
    }
)
keyComponent284: BinaryAssociation = BinaryAssociation(
    name="keyComponent284",
    ends={
        Property(name="Attribute285", type=express_core_UniqueRule, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_UniqueRule", type=Attribute, multiplicity=Multiplicity(1, 9999))
    }
)
rangeView286: BinaryAssociation = BinaryAssociation(
    name="rangeView286",
    ends={
        Property(name="InverseAttribute287", type=express_core_DomainRole, multiplicity=Multiplicity(1, 1)),
        Property(name="modelsRole", type=InverseAttribute, multiplicity=Multiplicity(0, 1))
    }
)
domain288: BinaryAssociation = BinaryAssociation(
    name="domain288",
    ends={
        Property(name="EntityType289", type=express_core_DomainRole, multiplicity=Multiplicity(1, 1)),
        Property(name="playsDomainRole", type=EntityType, multiplicity=Multiplicity(1, 1))
    }
)
id290: BinaryAssociation = BinaryAssociation(
    name="id290",
    ends={
        Property(name="ScopedId291", type=express_core_DomainRole, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_DomainRole", type=ScopedId, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
domain292: BinaryAssociation = BinaryAssociation(
    name="domain292",
    ends={
        Property(name="AttributeType294", type=express_core_DomainConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="constraints293", type=AttributeType, multiplicity=Multiplicity(1, 1))
    }
)
asserts295: BinaryAssociation = BinaryAssociation(
    name="asserts295",
    ends={
        Property(name="Expression296", type=express_core_DomainConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_DomainConstraint", type=Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
fundamentalType297: BinaryAssociation = BinaryAssociation(
    name="fundamentalType297",
    ends={
        Property(name="InstantiableType", type=express_core_InstantiableType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_InstantiableType", type=InstantiableType, multiplicity=Multiplicity(1, 1))
    }
)
variables314: BinaryAssociation = BinaryAssociation(
    name="variables314",
    ends={
        Property(name="express_core_AlgorithmScope", type=Variable, multiplicity=Multiplicity(0, 9999)),
        Property(name="Variable315", type=express_core_AlgorithmScope, multiplicity=Multiplicity(1, 1))
    }
)
appearsInPopulation316: BinaryAssociation = BinaryAssociation(
    name="appearsInPopulation316",
    ends={
        Property(name="Population317", type=express_core_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="compositionInstance", type=Population, multiplicity=Multiplicity(0, 9999))
    }
)
ofType318: BinaryAssociation = BinaryAssociation(
    name="ofType318",
    ends={
        Property(name="DataType319", type=express_core_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="instances", type=DataType, multiplicity=Multiplicity(1, 9999))
    }
)
role320: BinaryAssociation = BinaryAssociation(
    name="role320",
    ends={
        Property(name="Attribute321", type=express_core_AttributeType, multiplicity=Multiplicity(1, 1)),
        Property(name="attributeType", type=Attribute, multiplicity=Multiplicity(0, 9999))
    }
)
constraints322: BinaryAssociation = BinaryAssociation(
    name="constraints322",
    ends={
        Property(name="DomainConstraint", type=express_core_AttributeType, multiplicity=Multiplicity(1, 1)),
        Property(name="domain323", type=DomainConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
owningEntity308: BinaryAssociation = BinaryAssociation(
    name="owningEntity308",
    ends={
        Property(name="EntityType309", type=express_core_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attributes", type=EntityType, multiplicity=Multiplicity(1, 9999))
    }
)
constraint310: BinaryAssociation = BinaryAssociation(
    name="constraint310",
    ends={
        Property(name="ActualTypeConstraint", type=express_core_GenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="matchingType", type=ActualTypeConstraint, multiplicity=Multiplicity(0, 1))
    }
)
stringLengthConstraint311: BinaryAssociation = BinaryAssociation(
    name="stringLengthConstraint311",
    ends={
        Property(name="LengthConstraint", type=express_core_StringType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_StringType", type=LengthConstraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
specializes312: BinaryAssociation = BinaryAssociation(
    name="specializes312",
    ends={
        Property(name="AnonymousType", type=express_core_AnonymousType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_AnonymousType", type=AnonymousType, multiplicity=Multiplicity(0, 9999))
    }
)
commonElements313: BinaryAssociation = BinaryAssociation(
    name="commonElements313",
    ends={
        Property(name="CommonElement", type=express_core_AlgorithmScope, multiplicity=Multiplicity(1, 1)),
        Property(name="localScope", type=CommonElement, multiplicity=Multiplicity(0, 9999))
    }
)
upperBound343: BinaryAssociation = BinaryAssociation(
    name="upperBound343",
    ends={
        Property(name="SizeConstraint344", type=express_core_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_Role", type=SizeConstraint, multiplicity=Multiplicity(0, 1))
    }
)
lowerBound345: BinaryAssociation = BinaryAssociation(
    name="lowerBound345",
    ends={
        Property(name="SizeConstraint347", type=express_core_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_Role346", type=SizeConstraint, multiplicity=Multiplicity(0, 1))
    }
)
underlyingType348: BinaryAssociation = BinaryAssociation(
    name="underlyingType348",
    ends={
        Property(name="ConcreteType", type=express_core_SpecializedType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_SpecializedType", type=ConcreteType, multiplicity=Multiplicity(1, 1))
    }
)
hiIndex349: BinaryAssociation = BinaryAssociation(
    name="hiIndex349",
    ends={
        Property(name="ArrayBound", type=express_core_GeneralARRAYType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_GeneralARRAYType", type=ArrayBound, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
loIndex350: BinaryAssociation = BinaryAssociation(
    name="loIndex350",
    ends={
        Property(name="ArrayBound352", type=express_core_GeneralARRAYType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_GeneralARRAYType351", type=ArrayBound, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
derivation324: BinaryAssociation = BinaryAssociation(
    name="derivation324",
    ends={
        Property(name="Expression325", type=express_core_DerivedAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_DerivedAttribute", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
domainView326: BinaryAssociation = BinaryAssociation(
    name="domainView326",
    ends={
        Property(name="InvertibleAttribute328", type=express_core_RangeRole, multiplicity=Multiplicity(1, 1)),
        Property(name="modelsRole327", type=InvertibleAttribute, multiplicity=Multiplicity(1, 1))
    }
)
range329: BinaryAssociation = BinaryAssociation(
    name="range329",
    ends={
        Property(name="EntityType330", type=express_core_RangeRole, multiplicity=Multiplicity(1, 1)),
        Property(name="playsRangeRole", type=EntityType, multiplicity=Multiplicity(1, 1))
    }
)
id331: BinaryAssociation = BinaryAssociation(
    name="id331",
    ends={
        Property(name="ScopedId332", type=express_core_RangeRole, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_RangeRole", type=ScopedId, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
describesSchema333: BinaryAssociation = BinaryAssociation(
    name="describesSchema333",
    ends={
        Property(name="Schema334", type=express_core_Remark, multiplicity=Multiplicity(1, 1)),
        Property(name="documentation", type=Schema, multiplicity=Multiplicity(0, 9999))
    }
)
appearsIn335: BinaryAssociation = BinaryAssociation(
    name="appearsIn335",
    ends={
        Property(name="Scope336", type=express_core_Remark, multiplicity=Multiplicity(1, 1)),
        Property(name="includesRemarks", type=Scope, multiplicity=Multiplicity(1, 1))
    }
)
describesElement337: BinaryAssociation = BinaryAssociation(
    name="describesElement337",
    ends={
        Property(name="NamedElement", type=express_core_Remark, multiplicity=Multiplicity(1, 1)),
        Property(name="documentation338", type=NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
inRelationship339: BinaryAssociation = BinaryAssociation(
    name="inRelationship339",
    ends={
        Property(name="Relationship340", type=express_core_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="roles", type=Relationship, multiplicity=Multiplicity(1, 1))
    }
)
ofEntity341: BinaryAssociation = BinaryAssociation(
    name="ofEntity341",
    ends={
        Property(name="EntityType342", type=express_core_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="playsRole", type=EntityType, multiplicity=Multiplicity(1, 9999))
    }
)
upperBound371: BinaryAssociation = BinaryAssociation(
    name="upperBound371",
    ends={
        Property(name="SizeConstraint373", type=express_core_AggregationType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_AggregationType372", type=SizeConstraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
namedElements374: BinaryAssociation = BinaryAssociation(
    name="namedElements374",
    ends={
        Property(name="NamedElement375", type=express_core_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="namespace", type=NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
includesRemarks376: BinaryAssociation = BinaryAssociation(
    name="includesRemarks376",
    ends={
        Property(name="Remark377", type=express_core_Scope, multiplicity=Multiplicity(1, 1)),
        Property(name="appearsIn", type=Remark, multiplicity=Multiplicity(0, 9999))
    }
)
contains378: BinaryAssociation = BinaryAssociation(
    name="contains378",
    ends={
        Property(name="GeneralizedType379", type=express_core_ParameterType, multiplicity=Multiplicity(1, 1)),
        Property(name="occursIn", type=GeneralizedType, multiplicity=Multiplicity(0, 9999))
    }
)
domain353: BinaryAssociation = BinaryAssociation(
    name="domain353",
    ends={
        Property(name="DomainRole354", type=express_core_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_Relationship", type=DomainRole, multiplicity=Multiplicity(1, 1))
    }
)
roles355: BinaryAssociation = BinaryAssociation(
    name="roles355",
    ends={
        Property(name="Role356", type=express_core_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="inRelationship", type=Role, multiplicity=Multiplicity(2, 2))
    }
)
basedOn357: BinaryAssociation = BinaryAssociation(
    name="basedOn357",
    ends={
        Property(name="InvertibleAttribute358", type=express_core_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="createsRelationship", type=InvertibleAttribute, multiplicity=Multiplicity(1, 1))
    }
)
range359: BinaryAssociation = BinaryAssociation(
    name="range359",
    ends={
        Property(name="RangeRole361", type=express_core_Relationship, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_Relationship360", type=RangeRole, multiplicity=Multiplicity(1, 1))
    }
)
localElements362: BinaryAssociation = BinaryAssociation(
    name="localElements362",
    ends={
        Property(name="LocalElement", type=express_core_LocalScope, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_LocalScope", type=LocalElement, multiplicity=Multiplicity(0, 9999))
    }
)
instantiates363: BinaryAssociation = BinaryAssociation(
    name="instantiates363",
    ends={
        Property(name="SelectType", type=express_core_NamedType, multiplicity=Multiplicity(1, 1)),
        Property(name="allowedTypes", type=SelectType, multiplicity=Multiplicity(0, 9999))
    }
)
domainRules364: BinaryAssociation = BinaryAssociation(
    name="domainRules364",
    ends={
        Property(name="DomainRule", type=express_core_NamedType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_NamedType", type=DomainRule, multiplicity=Multiplicity(0, 9999))
    }
)
binaryLengthConstraint365: BinaryAssociation = BinaryAssociation(
    name="binaryLengthConstraint365",
    ends={
        Property(name="LengthConstraint366", type=express_core_BinaryType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_BinaryType", type=LengthConstraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definingScope367: BinaryAssociation = BinaryAssociation(
    name="definingScope367",
    ends={
        Property(name="Scope368", type=express_core_ScopedId, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_ScopedId", type=Scope, multiplicity=Multiplicity(1, 1))
    }
)
lowerBound369: BinaryAssociation = BinaryAssociation(
    name="lowerBound369",
    ends={
        Property(name="SizeConstraint370", type=express_core_AggregationType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_AggregationType", type=SizeConstraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
memberType398: BinaryAssociation = BinaryAssociation(
    name="memberType398",
    ends={
        Property(name="InstantiableType399", type=express_core_ConcreteAggregationType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_ConcreteAggregationType", type=InstantiableType, multiplicity=Multiplicity(1, 1))
    }
)
loIndex400: BinaryAssociation = BinaryAssociation(
    name="loIndex400",
    ends={
        Property(name="ArrayBound401", type=express_core_ARRAYType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_ARRAYType", type=ArrayBound, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
hiIndex402: BinaryAssociation = BinaryAssociation(
    name="hiIndex402",
    ends={
        Property(name="ArrayBound404", type=express_core_ARRAYType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_ARRAYType403", type=ArrayBound, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
allowedTypes380: BinaryAssociation = BinaryAssociation(
    name="allowedTypes380",
    ends={
        Property(name="NamedType381", type=express_core_SelectType, multiplicity=Multiplicity(1, 1)),
        Property(name="instantiates", type=NamedType, multiplicity=Multiplicity(0, 9999))
    }
)
extension382: BinaryAssociation = BinaryAssociation(
    name="extension382",
    ends={
        Property(name="SelectType384", type=express_core_SelectType, multiplicity=Multiplicity(1, 1)),
        Property(name="base383", type=SelectType, multiplicity=Multiplicity(0, 9999))
    }
)
base385: BinaryAssociation = BinaryAssociation(
    name="base385",
    ends={
        Property(name="SelectType387", type=express_core_SelectType, multiplicity=Multiplicity(1, 1)),
        Property(name="extension386", type=SelectType, multiplicity=Multiplicity(1, 1))
    }
)
selectList388: BinaryAssociation = BinaryAssociation(
    name="selectList388",
    ends={
        Property(name="NamedType389", type=express_core_SelectType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_SelectType", type=NamedType, multiplicity=Multiplicity(0, 9999))
    }
)
scope390: BinaryAssociation = BinaryAssociation(
    name="scope390",
    ends={
        Property(name="Algorithm", type=express_core_ActualType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_core_ActualType", type=Algorithm, multiplicity=Multiplicity(1, 1))
    }
)
localScope391: BinaryAssociation = BinaryAssociation(
    name="localScope391",
    ends={
        Property(name="AlgorithmScope", type=express_core_CommonElement, multiplicity=Multiplicity(1, 1)),
        Property(name="commonElements", type=AlgorithmScope, multiplicity=Multiplicity(0, 1))
    }
)
referencedAs392: BinaryAssociation = BinaryAssociation(
    name="referencedAs392",
    ends={
        Property(name="InterfacedElement393", type=express_core_SchemaElement, multiplicity=Multiplicity(1, 1)),
        Property(name="refersTo", type=InterfacedElement, multiplicity=Multiplicity(0, 9999))
    }
)
referencedIn394: BinaryAssociation = BinaryAssociation(
    name="referencedIn394",
    ends={
        Property(name="Schema395", type=express_core_SchemaElement, multiplicity=Multiplicity(1, 1)),
        Property(name="interfacedElements", type=Schema, multiplicity=Multiplicity(0, 9999))
    }
)
definedIn396: BinaryAssociation = BinaryAssociation(
    name="definedIn396",
    ends={
        Property(name="Schema397", type=express_core_SchemaElement, multiplicity=Multiplicity(1, 1)),
        Property(name="schemaElements", type=Schema, multiplicity=Multiplicity(0, 1))
    }
)
controlledBy418: BinaryAssociation = BinaryAssociation(
    name="controlledBy418",
    ends={
        Property(name="RepeatStatement", type=express_algorithms_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="body", type=RepeatStatement, multiplicity=Multiplicity(0, 1))
    }
)
implements419: BinaryAssociation = BinaryAssociation(
    name="implements419",
    ends={
        Property(name="Algorithm421", type=express_algorithms_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="body420", type=Algorithm, multiplicity=Multiplicity(0, 1))
    }
)
variableType422: BinaryAssociation = BinaryAssociation(
    name="variableType422",
    ends={
        Property(name="VariableType423", type=express_algorithms_NamedVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="express_algorithms_NamedVariable", type=VariableType, multiplicity=Multiplicity(1, 1))
    }
)
source424: BinaryAssociation = BinaryAssociation(
    name="source424",
    ends={
        Property(name="InParameter", type=express_algorithms_InVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="variable", type=InParameter, multiplicity=Multiplicity(1, 1))
    }
)
matchingType405: BinaryAssociation = BinaryAssociation(
    name="matchingType405",
    ends={
        Property(name="GenericType", type=express_algorithms_ActualTypeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="constraint", type=GenericType, multiplicity=Multiplicity(1, 1))
    }
)
requiredType406: BinaryAssociation = BinaryAssociation(
    name="requiredType406",
    ends={
        Property(name="ActualDataType", type=express_algorithms_ActualTypeConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="express_algorithms_ActualTypeConstraint", type=ActualDataType, multiplicity=Multiplicity(1, 1))
    }
)
result407: BinaryAssociation = BinaryAssociation(
    name="result407",
    ends={
        Property(name="FunctionResult408", type=express_algorithms_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="express_algorithms_Function", type=FunctionResult, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable409: BinaryAssociation = BinaryAssociation(
    name="variable409",
    ends={
        Property(name="InVariable", type=express_algorithms_InParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=InVariable, multiplicity=Multiplicity(1, 1))
    }
)
initialValue410: BinaryAssociation = BinaryAssociation(
    name="initialValue410",
    ends={
        Property(name="Expression411", type=express_algorithms_LocalVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="express_algorithms_LocalVariable", type=Expression, multiplicity=Multiplicity(0, 1))
    }
)
refersTo412: BinaryAssociation = BinaryAssociation(
    name="refersTo412",
    ends={
        Property(name="ActualDataType413", type=express_algorithms_ActualGenericType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_algorithms_ActualGenericType", type=ActualDataType, multiplicity=Multiplicity(1, 1))
    }
)
inBlock414: BinaryAssociation = BinaryAssociation(
    name="inBlock414",
    ends={
        Property(name="StatementBlock", type=express_algorithms_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="bodyStatements_Statement", type=StatementBlock, multiplicity=Multiplicity(0, 1))
    }
)
bodyStatementsSkipStatement415: BinaryAssociation = BinaryAssociation(
    name="bodyStatementsSkipStatement415",
    ends={
        Property(name="SkipStatement", type=express_algorithms_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="express_algorithms_Statement", type=SkipStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyStatementsEscapeStatement416: BinaryAssociation = BinaryAssociation(
    name="bodyStatementsEscapeStatement416",
    ends={
        Property(name="EscapeStatement", type=express_algorithms_Statement, multiplicity=Multiplicity(1, 1)),
        Property(name="express_algorithms_Statement417", type=EscapeStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiredStructure450: BinaryAssociation = BinaryAssociation(
    name="requiredStructure450",
    ends={
        Property(name="ActualStructure451", type=express_algorithms_ActualStructureConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="express_algorithms_ActualStructureConstraint", type=ActualStructure, multiplicity=Multiplicity(1, 1))
    }
)
body452: BinaryAssociation = BinaryAssociation(
    name="body452",
    ends={
        Property(name="Statement453", type=express_algorithms_Algorithm, multiplicity=Multiplicity(1, 1)),
        Property(name="implements", type=Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
formalParameters454: BinaryAssociation = BinaryAssociation(
    name="formalParameters454",
    ends={
        Property(name="Parameter455", type=express_algorithms_Algorithm, multiplicity=Multiplicity(1, 1)),
        Property(name="express_algorithms_Algorithm", type=Parameter_, multiplicity=Multiplicity(0, 9999))
    }
)
memberType456: BinaryAssociation = BinaryAssociation(
    name="memberType456",
    ends={
        Property(name="ActualType", type=express_algorithms_ActualAggregationType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_algorithms_ActualAggregationType", type=ActualType, multiplicity=Multiplicity(1, 1))
    }
)
hiIndex425: BinaryAssociation = BinaryAssociation(
    name="hiIndex425",
    ends={
        Property(name="ArrayBound426", type=express_algorithms_ActualARRAYType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_algorithms_ActualARRAYType", type=ArrayBound, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
loIndex427: BinaryAssociation = BinaryAssociation(
    name="loIndex427",
    ends={
        Property(name="ArrayBound429", type=express_algorithms_ActualARRAYType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_algorithms_ActualARRAYType428", type=ArrayBound, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
upperBound430: BinaryAssociation = BinaryAssociation(
    name="upperBound430",
    ends={
        Property(name="SizeConstraint431", type=express_algorithms_ActualAGGREGATEType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_algorithms_ActualAGGREGATEType", type=SizeConstraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
refersTo432: BinaryAssociation = BinaryAssociation(
    name="refersTo432",
    ends={
        Property(name="ActualStructure", type=express_algorithms_ActualAGGREGATEType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_algorithms_ActualAGGREGATEType433", type=ActualStructure, multiplicity=Multiplicity(1, 1))
    }
)
memberType434: BinaryAssociation = BinaryAssociation(
    name="memberType434",
    ends={
        Property(name="VariableType436", type=express_algorithms_ActualAGGREGATEType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_algorithms_ActualAGGREGATEType435", type=VariableType, multiplicity=Multiplicity(1, 1))
    }
)
lowerBound437: BinaryAssociation = BinaryAssociation(
    name="lowerBound437",
    ends={
        Property(name="SizeConstraint439", type=express_algorithms_ActualAGGREGATEType, multiplicity=Multiplicity(1, 1)),
        Property(name="express_algorithms_ActualAGGREGATEType438", type=SizeConstraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
structureConstraints440: BinaryAssociation = BinaryAssociation(
    name="structureConstraints440",
    ends={
        Property(name="ActualStructureConstraint441", type=express_algorithms_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="express_algorithms_Parameter", type=ActualStructureConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
typeConstraints442: BinaryAssociation = BinaryAssociation(
    name="typeConstraints442",
    ends={
        Property(name="ActualTypeConstraint444", type=express_algorithms_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="express_algorithms_Parameter443", type=ActualTypeConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
formalParameterType445: BinaryAssociation = BinaryAssociation(
    name="formalParameterType445",
    ends={
        Property(name="ParameterType447", type=express_algorithms_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="express_algorithms_Parameter446", type=ParameterType, multiplicity=Multiplicity(1, 1))
    }
)
matchingStructure448: BinaryAssociation = BinaryAssociation(
    name="matchingStructure448",
    ends={
        Property(name="AGGREGATEType", type=express_algorithms_ActualStructureConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="constraint449", type=AGGREGATEType, multiplicity=Multiplicity(1, 1))
    }
)
valueExpression476: BinaryAssociation = BinaryAssociation(
    name="valueExpression476",
    ends={
        Property(name="Expression477", type=express_instances_Constant, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_Constant", type=Expression, multiplicity=Multiplicity(1, 1))
    }
)
actualValue478: BinaryAssociation = BinaryAssociation(
    name="actualValue478",
    ends={
        Property(name="Instance480", type=express_instances_Constant, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_Constant479", type=Instance, multiplicity=Multiplicity(0, 1))
    }
)
dataType481: BinaryAssociation = BinaryAssociation(
    name="dataType481",
    ends={
        Property(name="InstantiableType483", type=express_instances_Constant, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_Constant482", type=InstantiableType, multiplicity=Multiplicity(1, 1))
    }
)
source457: BinaryAssociation = BinaryAssociation(
    name="source457",
    ends={
        Property(name="Parameter458", type=express_algorithms_GenericElement, multiplicity=Multiplicity(1, 1)),
        Property(name="express_algorithms_GenericElement", type=Parameter_, multiplicity=Multiplicity(1, 1))
    }
)
label459: BinaryAssociation = BinaryAssociation(
    name="label459",
    ends={
        Property(name="ScopedId461", type=express_algorithms_GenericElement, multiplicity=Multiplicity(1, 1)),
        Property(name="express_algorithms_GenericElement460", type=ScopedId, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
actualValue462: BinaryAssociation = BinaryAssociation(
    name="actualValue462",
    ends={
        Property(name="Instance463", type=express_instances_AttributeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_AttributeValue", type=Instance, multiplicity=Multiplicity(0, 1))
    }
)
attribute464: BinaryAssociation = BinaryAssociation(
    name="attribute464",
    ends={
        Property(name="ExplicitAttribute466", type=express_instances_AttributeValue, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_AttributeValue465", type=ExplicitAttribute, multiplicity=Multiplicity(1, 1))
    }
)
memberSlot467: BinaryAssociation = BinaryAssociation(
    name="memberSlot467",
    ends={
        Property(name="ArrayMember", type=express_instances_ARRAYValue, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_ARRAYValue", type=ArrayMember, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
refersTo468: BinaryAssociation = BinaryAssociation(
    name="refersTo468",
    ends={
        Property(name="Attribute469", type=express_instances_RoleName, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_RoleName", type=Attribute, multiplicity=Multiplicity(1, 1))
    }
)
represents470: BinaryAssociation = BinaryAssociation(
    name="represents470",
    ends={
        Property(name="ScopedId472", type=express_instances_RoleName, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_RoleName471", type=ScopedId, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
state473: BinaryAssociation = BinaryAssociation(
    name="state473",
    ends={
        Property(name="EntityValue", type=express_instances_EntityInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="describes", type=EntityValue, multiplicity=Multiplicity(1, 1))
    }
)
instanceOf474: BinaryAssociation = BinaryAssociation(
    name="instanceOf474",
    ends={
        Property(name="EntityType475", type=express_instances_EntityInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_EntityInstance", type=EntityType, multiplicity=Multiplicity(1, 9999))
    }
)
declaredIn502: BinaryAssociation = BinaryAssociation(
    name="declaredIn502",
    ends={
        Property(name="declaredItems", type=EnumerationType, multiplicity=Multiplicity(1, 1)),
        Property(name="EnumerationType503", type=express_instances_EnumerationItem, multiplicity=Multiplicity(1, 1))
    }
)
correspondsTo504: BinaryAssociation = BinaryAssociation(
    name="correspondsTo504",
    ends={
        Property(name="EntityType505", type=express_instances_EntityValue, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_EntityValue", type=EntityType, multiplicity=Multiplicity(1, 9999))
    }
)
describes506: BinaryAssociation = BinaryAssociation(
    name="describes506",
    ends={
        Property(name="EntityInstance507", type=express_instances_EntityValue, multiplicity=Multiplicity(1, 1)),
        Property(name="state", type=EntityInstance, multiplicity=Multiplicity(0, 9999))
    }
)
memberValue508: BinaryAssociation = BinaryAssociation(
    name="memberValue508",
    ends={
        Property(name="Instance509", type=express_instances_SETValue, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_SETValue", type=Instance, multiplicity=Multiplicity(0, 9999))
    }
)
satisfiesType484: BinaryAssociation = BinaryAssociation(
    name="satisfiesType484",
    ends={
        Property(name="SelectType485", type=express_instances_TypedInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_TypedInstance", type=SelectType, multiplicity=Multiplicity(0, 9999))
    }
)
memberValue486: BinaryAssociation = BinaryAssociation(
    name="memberValue486",
    ends={
        Property(name="Instance487", type=express_instances_ListMember, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_ListMember", type=Instance, multiplicity=Multiplicity(1, 1))
    }
)
memberValue488: BinaryAssociation = BinaryAssociation(
    name="memberValue488",
    ends={
        Property(name="Instance489", type=express_instances_BagMember, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_BagMember", type=Instance, multiplicity=Multiplicity(1, 1))
    }
)
equivalent490: BinaryAssociation = BinaryAssociation(
    name="equivalent490",
    ends={
        Property(name="PartialEntityValue491", type=express_instances_SingleEntityValue, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_SingleEntityValue", type=PartialEntityValue, multiplicity=Multiplicity(1, 1))
    }
)
ofType492: BinaryAssociation = BinaryAssociation(
    name="ofType492",
    ends={
        Property(name="SingleEntityType494", type=express_instances_SingleEntityValue, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_SingleEntityValue493", type=SingleEntityType, multiplicity=Multiplicity(1, 1))
    }
)
properties495: BinaryAssociation = BinaryAssociation(
    name="properties495",
    ends={
        Property(name="AttributeValue497", type=express_instances_SingleEntityValue, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_SingleEntityValue496", type=AttributeValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
characterizingType498: BinaryAssociation = BinaryAssociation(
    name="characterizingType498",
    ends={
        Property(name="EntityType499", type=express_instances_SingleLeafInstance, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_SingleLeafInstance", type=EntityType, multiplicity=Multiplicity(1, 1))
    }
)
fundamentalValue500: BinaryAssociation = BinaryAssociation(
    name="fundamentalValue500",
    ends={
        Property(name="ConcreteValue", type=express_instances_SpecializedValue, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_SpecializedValue", type=ConcreteValue, multiplicity=Multiplicity(1, 1))
    }
)
memberSlot501: BinaryAssociation = BinaryAssociation(
    name="memberSlot501",
    ends={
        Property(name="BagMember", type=express_instances_BAGValue, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_BAGValue", type=BagMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
memberValue510: BinaryAssociation = BinaryAssociation(
    name="memberValue510",
    ends={
        Property(name="Instance511", type=express_instances_ArrayMember, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_ArrayMember", type=Instance, multiplicity=Multiplicity(0, 1))
    }
)
compositionEntityInstance512: BinaryAssociation = BinaryAssociation(
    name="compositionEntityInstance512",
    ends={
        Property(name="EntityInstance513", type=express_instances_Population, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_Population", type=EntityInstance, multiplicity=Multiplicity(0, 9999))
    }
)
compositionInstance514: BinaryAssociation = BinaryAssociation(
    name="compositionInstance514",
    ends={
        Property(name="Instance515", type=express_instances_Population, multiplicity=Multiplicity(1, 1)),
        Property(name="appearsInPopulation", type=Instance, multiplicity=Multiplicity(0, 9999))
    }
)
governingSchema516: BinaryAssociation = BinaryAssociation(
    name="governingSchema516",
    ends={
        Property(name="Schema518", type=express_instances_Population, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_Population517", type=Schema, multiplicity=Multiplicity(0, 9999))
    }
)
memberSlot519: BinaryAssociation = BinaryAssociation(
    name="memberSlot519",
    ends={
        Property(name="ListMember520", type=express_instances_LISTValue, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_LISTValue", type=ListMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refersTo521: BinaryAssociation = BinaryAssociation(
    name="refersTo521",
    ends={
        Property(name="NamedType522", type=express_instances_TypeName, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_TypeName", type=NamedType, multiplicity=Multiplicity(1, 1))
    }
)
represents523: BinaryAssociation = BinaryAssociation(
    name="represents523",
    ends={
        Property(name="ScopedId525", type=express_instances_TypeName, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_TypeName524", type=ScopedId, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
components526: BinaryAssociation = BinaryAssociation(
    name="components526",
    ends={
        Property(name="SingleEntityValue", type=express_instances_PartialEntityValue, multiplicity=Multiplicity(1, 1)),
        Property(name="express_instances_PartialEntityValue", type=SingleEntityValue, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_express_rules_ONEOFConstraint_SubtypeConstraint = Generalization(general=SubtypeConstraint, specific=express_rules_ONEOFConstraint)
gen_express_rules_SupertypeRule_CommonElement = Generalization(general=CommonElement, specific=express_rules_SupertypeRule)
gen_express_statements_ProcedureCall_Statement = Generalization(general=Statement, specific=express_statements_ProcedureCall)
gen_express_rules_Extent_SETValue = Generalization(general=SETValue, specific=express_rules_Extent)
gen_express_rules_TOTAL_OVERConstraint_SubtypeConstraint = Generalization(general=SubtypeConstraint, specific=express_rules_TOTAL_OVERConstraint)
gen_express_rules_ANDConstraint_SubtypeConstraint = Generalization(general=SubtypeConstraint, specific=express_rules_ANDConstraint)
gen_express_rules_GlobalRule_core_SchemaElement = Generalization(general=core_SchemaElement, specific=express_rules_GlobalRule)
gen_express_rules_GlobalRule_core_AlgorithmScope = Generalization(general=core_AlgorithmScope, specific=express_rules_GlobalRule)
gen_express_rules_NamedRule_LocalElement = Generalization(general=LocalElement, specific=express_rules_NamedRule)
gen_express_statements_SkipStatement_ControlStatement = Generalization(general=ControlStatement, specific=express_statements_SkipStatement)
gen_express_statements_AliasStatement_algorithms_Statement = Generalization(general=algorithms_Statement, specific=express_statements_AliasStatement)
gen_express_statements_AliasStatement_core_LocalScope = Generalization(general=core_LocalScope, specific=express_statements_AliasStatement)
gen_express_statements_ControlVariable_NamedVariable = Generalization(general=NamedVariable, specific=express_statements_ControlVariable)
gen_express_statements_AliasVariable_algorithms_NamedVariable = Generalization(general=algorithms_NamedVariable, specific=express_statements_AliasVariable)
gen_express_statements_AliasVariable_algorithms_VARVariable = Generalization(general=algorithms_VARVariable, specific=express_statements_AliasVariable)
gen_express_statements_ControlStatement_Statement = Generalization(general=Statement, specific=express_statements_ControlStatement)
gen_express_statements_VARCell_VARExpression = Generalization(general=VARExpression, specific=express_statements_VARCell)
gen_express_statements_NullStatement_ControlStatement = Generalization(general=ControlStatement, specific=express_statements_NullStatement)
gen_express_statements_AttributeCell_VARExpression = Generalization(general=VARExpression, specific=express_statements_AttributeCell)
gen_express_statements_StatementBlock_Statement = Generalization(general=Statement, specific=express_statements_StatementBlock)
gen_express_statements_IfStatement_Statement = Generalization(general=Statement, specific=express_statements_IfStatement)
gen_express_statements_MemberCell_VARExpression = Generalization(general=VARExpression, specific=express_statements_MemberCell)
gen_express_statements_RepeatStatement_algorithms_Statement = Generalization(general=algorithms_Statement, specific=express_statements_RepeatStatement)
gen_express_statements_RepeatStatement_core_LocalScope = Generalization(general=core_LocalScope, specific=express_statements_RepeatStatement)
gen_express_statements_GroupCell_VARExpression = Generalization(general=VARExpression, specific=express_statements_GroupCell)
gen_express_statements_VariableCell_VARExpression = Generalization(general=VARExpression, specific=express_statements_VariableCell)
gen_express_statements_CaseStatement_Statement = Generalization(general=Statement, specific=express_statements_CaseStatement)
gen_express_expressions_IndeterminateRef_Primary = Generalization(general=Primary, specific=express_expressions_IndeterminateRef)
gen_express_expressions_SELFRef_Primary = Generalization(general=Primary, specific=express_expressions_SELFRef)
gen_express_expressions_IndexOperation_Expression = Generalization(general=Expression, specific=express_expressions_IndexOperation)
gen_express_statements_EscapeStatement_ControlStatement = Generalization(general=ControlStatement, specific=express_statements_EscapeStatement)
gen_express_statements_ReturnStatement_ControlStatement = Generalization(general=ControlStatement, specific=express_statements_ReturnStatement)
gen_express_statements_Assignment_Statement = Generalization(general=Statement, specific=express_statements_Assignment)
gen_express_expressions_Selector_Expression = Generalization(general=Expression, specific=express_expressions_Selector)
gen_express_expressions_EnumItemRef_Primary = Generalization(general=Primary, specific=express_expressions_EnumItemRef)
gen_express_expressions_Literal_Primary = Generalization(general=Primary, specific=express_expressions_Literal)
gen_express_expressions_BinaryIndex_IndexOperation = Generalization(general=IndexOperation, specific=express_expressions_BinaryIndex)
gen_express_expressions_BinaryOperation_Operation = Generalization(general=Operation, specific=express_expressions_BinaryOperation)
gen_express_expressions_ParameterRef_Primary = Generalization(general=Primary, specific=express_expressions_ParameterRef)
gen_express_expressions_AggregateInitializer_Expression = Generalization(general=Expression, specific=express_expressions_AggregateInitializer)
gen_express_expressions_StringIndex_IndexOperation = Generalization(general=IndexOperation, specific=express_expressions_StringIndex)
gen_express_expressions_PartialEntityConstructor_Expression = Generalization(general=Expression, specific=express_expressions_PartialEntityConstructor)
gen_express_expressions_Coercion_Operation = Generalization(general=Operation, specific=express_expressions_Coercion)
gen_express_expressions_Primary_Expression = Generalization(general=Expression, specific=express_expressions_Primary)
gen_express_expressions_QueryVariable_NamedVariable = Generalization(general=NamedVariable, specific=express_expressions_QueryVariable)
gen_express_expressions_Operation_Expression = Generalization(general=Expression, specific=express_expressions_Operation)
gen_express_expressions_AttributeRef_Selector = Generalization(general=Selector, specific=express_expressions_AttributeRef)
gen_express_expressions_AggregateIndex_IndexOperation = Generalization(general=IndexOperation, specific=express_expressions_AggregateIndex)
gen_express_expressions_GroupRef_Selector = Generalization(general=Selector, specific=express_expressions_GroupRef)
gen_express_expressions_UnaryOperation_Operation = Generalization(general=Operation, specific=express_expressions_UnaryOperation)
gen_express_expressions_UsedInRef_Selector = Generalization(general=Selector, specific=express_expressions_UsedInRef)
gen_express_expressions_ConstantRef_Primary = Generalization(general=Primary, specific=express_expressions_ConstantRef)
gen_express_expressions_QueryExpression_core_LocalScope = Generalization(general=core_LocalScope, specific=express_expressions_QueryExpression)
gen_express_expressions_QueryExpression_core_Expression = Generalization(general=core_Expression, specific=express_expressions_QueryExpression)
gen_express_core_TypeElement_NamedElement = Generalization(general=NamedElement, specific=express_core_TypeElement)
gen_express_core_AGGREGATEType_GeneralizedType = Generalization(general=GeneralizedType, specific=express_core_AGGREGATEType)
gen_express_expressions_FunctionCall_Expression = Generalization(general=Expression, specific=express_expressions_FunctionCall)
gen_express_expressions_ExtentRef_Primary = Generalization(general=Primary, specific=express_expressions_ExtentRef)
gen_express_expressions_VariableRef_Primary = Generalization(general=Primary, specific=express_expressions_VariableRef)
gen_express_core_VariableType_core_DataType = Generalization(general=core_DataType, specific=express_core_VariableType)
gen_express_core_VariableType_core_AttributeType = Generalization(general=core_AttributeType, specific=express_core_VariableType)
gen_express_core_GeneralBAGType_GeneralAggregationType = Generalization(general=GeneralAggregationType, specific=express_core_GeneralBAGType)
gen_express_core_DomainRule_core_DomainConstraint = Generalization(general=core_DomainConstraint, specific=express_core_DomainRule)
gen_express_core_DomainRule_core_TypeElement = Generalization(general=core_TypeElement, specific=express_core_DomainRule)
gen_express_core_GeneralAggregationType_core_GeneralizedType = Generalization(general=core_GeneralizedType, specific=express_core_GeneralAggregationType)
gen_express_core_GeneralAggregationType_core_AggregationType = Generalization(general=core_AggregationType, specific=express_core_GeneralAggregationType)
gen_express_core_ConcreteType_InstantiableType = Generalization(general=InstantiableType, specific=express_core_ConcreteType)
gen_express_core_InverseAttribute_Attribute = Generalization(general=Attribute, specific=express_core_InverseAttribute)
gen_express_core_EnumerationType_DefinedType = Generalization(general=DefinedType, specific=express_core_EnumerationType)
gen_express_core_GeneralSETType_GeneralAggregationType = Generalization(general=GeneralAggregationType, specific=express_core_GeneralSETType)
gen_express_core_LISTType_ConcreteAggregationType = Generalization(general=ConcreteAggregationType, specific=express_core_LISTType)
gen_express_core_EntityType_core_NamedType = Generalization(general=core_NamedType, specific=express_core_EntityType)
gen_express_core_EntityType_core_InstantiableType = Generalization(general=core_InstantiableType, specific=express_core_EntityType)
gen_express_core_GeneralizedType_core_ParameterType = Generalization(general=core_ParameterType, specific=express_core_GeneralizedType)
gen_express_core_GeneralizedType_core_AttributeType = Generalization(general=core_AttributeType, specific=express_core_GeneralizedType)
gen_express_core_PartialEntityType_DataType = Generalization(general=DataType, specific=express_core_PartialEntityType)
gen_express_core_Schema_Scope = Generalization(general=Scope, specific=express_core_Schema)
gen_express_core_InvertibleAttribute_ExplicitAttribute = Generalization(general=ExplicitAttribute, specific=express_core_InvertibleAttribute)
gen_express_core_Attribute_TypeElement = Generalization(general=TypeElement, specific=express_core_Attribute)
gen_express_core_NumericType_SimpleType = Generalization(general=SimpleType, specific=express_core_NumericType)
gen_express_core_DefinedType_core_NamedType = Generalization(general=core_NamedType, specific=express_core_DefinedType)
gen_express_core_DefinedType_core_ConcreteType = Generalization(general=core_ConcreteType, specific=express_core_DefinedType)
gen_express_core_UniqueRule_TypeElement = Generalization(general=TypeElement, specific=express_core_UniqueRule)
gen_express_core_DomainRole_Role = Generalization(general=Role, specific=express_core_DomainRole)
gen_express_core_InstantiableType_core_ParameterType = Generalization(general=core_ParameterType, specific=express_core_InstantiableType)
gen_express_core_InstantiableType_core_VariableType = Generalization(general=core_VariableType, specific=express_core_InstantiableType)
gen_express_core_GeneralLISTType_GeneralAggregationType = Generalization(general=GeneralAggregationType, specific=express_core_GeneralLISTType)
gen_express_core_DerivedAttribute_Attribute = Generalization(general=Attribute, specific=express_core_DerivedAttribute)
gen_express_core_BAGType_ConcreteAggregationType = Generalization(general=ConcreteAggregationType, specific=express_core_BAGType)
gen_express_core_RealType_NumericType = Generalization(general=NumericType, specific=express_core_RealType)
gen_express_core_LogicType_SimpleType = Generalization(general=SimpleType, specific=express_core_LogicType)
gen_express_core_GenericType_GeneralizedType = Generalization(general=GeneralizedType, specific=express_core_GenericType)
gen_express_core_StringType_SimpleType = Generalization(general=SimpleType, specific=express_core_StringType)
gen_express_core_AnonymousType_core_ConcreteType = Generalization(general=core_ConcreteType, specific=express_core_AnonymousType)
gen_express_core_AnonymousType_core_InstantiableType = Generalization(general=core_InstantiableType, specific=express_core_AnonymousType)
gen_express_core_AlgorithmScope_LocalScope = Generalization(general=LocalScope, specific=express_core_AlgorithmScope)
gen_express_core_SETType_ConcreteAggregationType = Generalization(general=ConcreteAggregationType, specific=express_core_SETType)
gen_express_core_SpecializedType_DefinedType = Generalization(general=DefinedType, specific=express_core_SpecializedType)
gen_express_core_GeneralARRAYType_GeneralAggregationType = Generalization(general=GeneralAggregationType, specific=express_core_GeneralARRAYType)
gen_express_core_RangeRole_Role = Generalization(general=Role, specific=express_core_RangeRole)
gen_express_core_LocalElement_NamedElement = Generalization(general=NamedElement, specific=express_core_LocalElement)
gen_express_core_SizeConstraint_DomainConstraint = Generalization(general=DomainConstraint, specific=express_core_SizeConstraint)
gen_express_core_SelectType_DefinedType = Generalization(general=DefinedType, specific=express_core_SelectType)
gen_express_core_LengthConstraint_DomainConstraint = Generalization(general=DomainConstraint, specific=express_core_LengthConstraint)
gen_express_core_LocalScope_Scope = Generalization(general=Scope, specific=express_core_LocalScope)
gen_express_core_NamedType_core_InstantiableType = Generalization(general=core_InstantiableType, specific=express_core_NamedType)
gen_express_core_NamedType_core_Scope = Generalization(general=core_Scope, specific=express_core_NamedType)
gen_express_core_NamedType_core_CommonElement = Generalization(general=core_CommonElement, specific=express_core_NamedType)
gen_express_core_NamedType_core_AttributeType = Generalization(general=core_AttributeType, specific=express_core_NamedType)
gen_express_core_BinaryType_SimpleType = Generalization(general=SimpleType, specific=express_core_BinaryType)
gen_express_core_ARRAYType_ConcreteAggregationType = Generalization(general=ConcreteAggregationType, specific=express_core_ARRAYType)
gen_express_core_ActualType_VariableType = Generalization(general=VariableType, specific=express_core_ActualType)
gen_express_core_ExplicitAttribute_Attribute = Generalization(general=Attribute, specific=express_core_ExplicitAttribute)
gen_express_core_SimpleType_AnonymousType = Generalization(general=AnonymousType, specific=express_core_SimpleType)
gen_express_core_CommonElement_SchemaElement = Generalization(general=SchemaElement, specific=express_core_CommonElement)
gen_express_core_SchemaElement_NamedElement = Generalization(general=NamedElement, specific=express_core_SchemaElement)
gen_express_core_ConcreteAggregationType_core_AnonymousType = Generalization(general=core_AnonymousType, specific=express_core_ConcreteAggregationType)
gen_express_core_ConcreteAggregationType_core_AggregationType = Generalization(general=core_AggregationType, specific=express_core_ConcreteAggregationType)
gen_express_algorithms_NamedVariable_LocalElement = Generalization(general=LocalElement, specific=express_algorithms_NamedVariable)
gen_express_algorithms_InVariable_Variable = Generalization(general=Variable, specific=express_algorithms_InVariable)
gen_express_algorithms_Procedure_Algorithm = Generalization(general=Algorithm, specific=express_algorithms_Procedure)
gen_express_algorithms_ActualARRAYType_ActualAggregationType = Generalization(general=ActualAggregationType, specific=express_algorithms_ActualARRAYType)
gen_express_algorithms_FunctionResult_Variable = Generalization(general=Variable, specific=express_algorithms_FunctionResult)
gen_express_algorithms_Function_Algorithm = Generalization(general=Algorithm, specific=express_algorithms_Function)
gen_express_algorithms_InParameter_Parameter = Generalization(general=Parameter_, specific=express_algorithms_InParameter)
gen_express_algorithms_LocalVariable_Variable = Generalization(general=Variable, specific=express_algorithms_LocalVariable)
gen_express_algorithms_ActualStructure_algorithms_GenericElement = Generalization(general=algorithms_GenericElement, specific=express_algorithms_ActualStructure)
gen_express_algorithms_ActualStructure_core_AGGREGATEType = Generalization(general=core_AGGREGATEType, specific=express_algorithms_ActualStructure)
gen_express_algorithms_ActualGenericType_ActualType = Generalization(general=ActualType, specific=express_algorithms_ActualGenericType)
gen_express_algorithms_Algorithm_core_AlgorithmScope = Generalization(general=core_AlgorithmScope, specific=express_algorithms_Algorithm)
gen_express_algorithms_Algorithm_core_CommonElement = Generalization(general=core_CommonElement, specific=express_algorithms_Algorithm)
gen_express_algorithms_ActualAggregationType_core_ActualType = Generalization(general=core_ActualType, specific=express_algorithms_ActualAggregationType)
gen_express_algorithms_ActualAggregationType_core_AggregationType = Generalization(general=core_AggregationType, specific=express_algorithms_ActualAggregationType)
gen_express_algorithms_ActualSETType_ActualAggregationType = Generalization(general=ActualAggregationType, specific=express_algorithms_ActualSETType)
gen_express_algorithms_ActualAGGREGATEType_ActualType = Generalization(general=ActualType, specific=express_algorithms_ActualAGGREGATEType)
gen_express_algorithms_Parameter_LocalElement = Generalization(general=LocalElement, specific=express_algorithms_Parameter)
gen_express_instances_IntegerValue_RealValue = Generalization(general=RealValue, specific=express_instances_IntegerValue)
gen_express_instances_AggregateValue_ConcreteValue = Generalization(general=ConcreteValue, specific=express_instances_AggregateValue)
gen_express_instances_Constant_CommonElement = Generalization(general=CommonElement, specific=express_instances_Constant)
gen_express_instances_LogicalValue_SimpleValue = Generalization(general=SimpleValue, specific=express_instances_LogicalValue)
gen_express_instances_TypedInstance_Instance = Generalization(general=Instance, specific=express_instances_TypedInstance)
gen_express_algorithms_ActualLISTType_ActualAggregationType = Generalization(general=ActualAggregationType, specific=express_algorithms_ActualLISTType)
gen_express_algorithms_Variable_NamedVariable = Generalization(general=NamedVariable, specific=express_algorithms_Variable)
gen_express_algorithms_GenericElement_LocalElement = Generalization(general=LocalElement, specific=express_algorithms_GenericElement)
gen_express_algorithms_VARParameter_algorithms_Parameter = Generalization(general=algorithms_Parameter, specific=express_algorithms_VARParameter)
gen_express_algorithms_VARParameter_algorithms_VARVariable = Generalization(general=algorithms_VARVariable, specific=express_algorithms_VARParameter)
gen_express_algorithms_ActualDataType_core_GenericType = Generalization(general=core_GenericType, specific=express_algorithms_ActualDataType)
gen_express_algorithms_ActualDataType_algorithms_GenericElement = Generalization(general=algorithms_GenericElement, specific=express_algorithms_ActualDataType)
gen_express_algorithms_ActualBAGType_ActualAggregationType = Generalization(general=ActualAggregationType, specific=express_algorithms_ActualBAGType)
gen_express_instances_ARRAYValue_AggregateValue = Generalization(general=AggregateValue, specific=express_instances_ARRAYValue)
gen_express_instances_RoleName_StringValue = Generalization(general=StringValue, specific=express_instances_RoleName)
gen_express_instances_EntityInstance_TypedInstance = Generalization(general=TypedInstance, specific=express_instances_EntityInstance)
gen_express_instances_EntityValue_PartialEntityValue = Generalization(general=PartialEntityValue, specific=express_instances_EntityValue)
gen_express_instances_SETValue_AggregateValue = Generalization(general=AggregateValue, specific=express_instances_SETValue)
gen_express_instances_Indeterminate_Instance = Generalization(general=Instance, specific=express_instances_Indeterminate)
gen_express_instances_SingleLeafInstance_EntityInstance = Generalization(general=EntityInstance, specific=express_instances_SingleLeafInstance)
gen_express_instances_GenericAggregate_LISTValue = Generalization(general=LISTValue, specific=express_instances_GenericAggregate)
gen_express_instances_BinaryValue_SimpleValue = Generalization(general=SimpleValue, specific=express_instances_BinaryValue)
gen_express_instances_SpecializedValue_TypedInstance = Generalization(general=TypedInstance, specific=express_instances_SpecializedValue)
gen_express_instances_BAGValue_AggregateValue = Generalization(general=AggregateValue, specific=express_instances_BAGValue)
gen_express_instances_EnumerationItem_core_TypeElement = Generalization(general=core_TypeElement, specific=express_instances_EnumerationItem)
gen_express_instances_EnumerationItem_instances_TypedInstance = Generalization(general=instances_TypedInstance, specific=express_instances_EnumerationItem)
gen_express_instances_EnumerationItem_instances_ConcreteValue = Generalization(general=instances_ConcreteValue, specific=express_instances_EnumerationItem)
gen_express_instances_RealValue_NumberValue = Generalization(general=NumberValue, specific=express_instances_RealValue)
gen_express_instances_NumberValue_SimpleValue = Generalization(general=SimpleValue, specific=express_instances_NumberValue)
gen_express_instances_BooleanValue_LogicalValue = Generalization(general=LogicalValue, specific=express_instances_BooleanValue)
gen_express_instances_MultiLeafInstance_EntityInstance = Generalization(general=EntityInstance, specific=express_instances_MultiLeafInstance)
gen_express_instances_SimpleValue_ConcreteValue = Generalization(general=ConcreteValue, specific=express_instances_SimpleValue)
gen_express_instances_LISTValue_core_Instance = Generalization(general=core_Instance, specific=express_instances_LISTValue)
gen_express_instances_LISTValue_instances_AggregateValue = Generalization(general=instances_AggregateValue, specific=express_instances_LISTValue)
gen_express_instances_ConcreteValue_Instance = Generalization(general=Instance, specific=express_instances_ConcreteValue)
gen_express_instances_StringValue_SimpleValue = Generalization(general=SimpleValue, specific=express_instances_StringValue)
gen_express_instances_TypeName_StringValue = Generalization(general=StringValue, specific=express_instances_TypeName)
gen_express_instances_PartialEntityValue_Instance = Generalization(general=Instance, specific=express_instances_PartialEntityValue)

# Domain Model
domain_model = DomainModel(
    name="express",
    types={express_rules_ONEOFConstraint, SubtypeConstraint, express_rules_SupertypeRule, CommonElement, EntityType, express_statements_ProcedureCall, Procedure, ActualParameter, express_rules_SubtypeConstraint, Extent, Expression, SupertypeRule, express_rules_Extent, SETValue, EntityInstance, Population, GlobalRule, ScopedId, express_rules_TOTAL_OVERConstraint, express_rules_ANDConstraint, express_rules_GlobalRule, core_SchemaElement, core_AlgorithmScope, Statement, NamedRule, express_rules_NamedRule, LocalElement, express_statements_CaseAction, express_statements_SkipStatement, ControlStatement, express_statements_AliasStatement, algorithms_Statement, core_LocalScope, VARExpression, AliasVariable, express_statements_ControlVariable, NamedVariable, express_statements_AliasVariable, algorithms_NamedVariable, algorithms_VARVariable, express_statements_ControlStatement, express_statements_VARCell, VARVariable, express_statements_NullStatement, express_statements_VARExpression, express_statements_AttributeCell, ExplicitAttribute, express_statements_StatementBlock, express_statements_IfStatement, express_statements_MemberCell, express_statements_RepeatStatement, ControlVariable, express_statements_GroupCell, SingleEntityType, express_statements_VariableCell, Variable, express_statements_CaseStatement, CaseAction, Indeterminate, express_expressions_SELFRef, express_expressions_IndexOperation, express_statements_EscapeStatement, express_statements_ReturnStatement, express_statements_Assignment, express_expressions_Selector, express_expressions_RepeatCount, express_expressions_EnumItemRef, Primary, EnumerationItem, express_expressions_Literal, SimpleValue, express_expressions_BinaryIndex, IndexOperation, express_expressions_ActualParameter, express_expressions_IndeterminateRef, ProcedureCall, FunctionCall, Parameter_, express_expressions_BinaryOperation, Operation, express_expressions_ParameterRef, express_expressions_AggregateInitializer, GenericAggregate, MemberBinding, express_expressions_StringIndex, express_expressions_PartialEntityConstructor, PartialEntityValue, AttributeBinding, express_expressions_Coercion, VariableType, express_expressions_Primary, QueryVariable, express_expressions_QueryVariable, express_expressions_Operation, express_expressions_AttributeBinding, AttributeValue, express_expressions_AttributeRef, Selector, Attribute, express_expressions_AggregateIndex, express_expressions_GroupRef, express_expressions_UnaryOperation, express_expressions_UsedInRef, express_expressions_ConstantRef, Constant, express_expressions_QueryExpression, core_Expression, express_core_TypeElement, NamedElement, express_core_SingleEntityType, PartialEntityType, express_core_AGGREGATEType, GeneralizedType, SizeConstraint, express_expressions_FunctionCall, Function, FunctionResult, express_expressions_MemberBinding, RepeatCount, ListMember, express_expressions_ExtentRef, NamedType, express_expressions_VariableRef, EnumerationType, express_core_VariableType, core_DataType, core_AttributeType, express_core_ArrayBound, ParameterType, ActualStructureConstraint, express_core_GeneralBAGType, GeneralAggregationType, express_core_DomainRule, core_DomainConstraint, core_TypeElement, express_core_GeneralAggregationType, core_GeneralizedType, core_AggregationType, express_core_ConcreteType, InstantiableType, express_core_Expression, Instance, Scope, DataType, express_core_InverseAttribute, DomainRole, InvertibleAttribute, express_core_EnumerationType, DefinedType, RangeRole, UniqueRule, express_core_GeneralSETType, express_core_LISTType, ConcreteAggregationType, express_core_Redeclaration, AttributeType, Redeclaration, Role, express_core_EntityType, core_NamedType, core_InstantiableType, express_core_GeneralizedType, core_ParameterType, express_core_InterfacedElement, Schema, express_core_DataType, express_core_PartialEntityType, express_core_Schema, Remark, InterfacedElement, SchemaElement, express_core_InvertibleAttribute, InverseAttribute, Relationship, express_core_Attribute, express_core_NumericType, SimpleType, express_core_DefinedType, core_ConcreteType, express_core_UniqueRule, TypeElement, express_core_DomainRole, express_core_DomainConstraint, express_core_InstantiableType, core_VariableType, express_core_GeneralLISTType, express_core_NamedElement, express_core_Instance, express_core_AttributeType, DomainConstraint, express_core_DerivedAttribute, express_core_BAGType, express_core_RealType, NumericType, express_core_LogicType, express_core_GenericType, ActualTypeConstraint, express_core_StringType, LengthConstraint, express_core_AnonymousType, AnonymousType, express_core_AlgorithmScope, LocalScope, express_core_SETType, express_core_SpecializedType, ConcreteType, express_core_GeneralARRAYType, ArrayBound, express_core_RangeRole, express_core_LocalElement, express_core_Remark, express_core_SizeConstraint, express_core_Role, express_core_Scope, express_core_ParameterType, express_core_SelectType, express_core_Relationship, express_core_LengthConstraint, express_core_LocalScope, express_core_NamedType, core_Scope, core_CommonElement, SelectType, DomainRule, express_core_BinaryType, express_core_ScopedId, express_core_AggregationType, express_core_ARRAYType, express_algorithms_ActualTypeConstraint, express_core_ActualType, Algorithm, express_core_ExplicitAttribute, express_core_SimpleType, express_core_CommonElement, AlgorithmScope, express_core_SchemaElement, express_core_ConcreteAggregationType, core_AnonymousType, RepeatStatement, express_algorithms_NamedVariable, express_algorithms_InVariable, InParameter, express_algorithms_Procedure, express_algorithms_ActualARRAYType, ActualAggregationType, GenericType, ActualDataType, express_algorithms_FunctionResult, express_algorithms_Function, express_algorithms_InParameter, InVariable, express_algorithms_LocalVariable, express_algorithms_ActualStructure, algorithms_GenericElement, core_AGGREGATEType, express_algorithms_ActualGenericType, ActualType, express_algorithms_Statement, StatementBlock, SkipStatement, EscapeStatement, express_algorithms_Algorithm, express_algorithms_ActualAggregationType, core_ActualType, express_algorithms_VARVariable, express_algorithms_ActualSETType, express_algorithms_ActualAGGREGATEType, ActualStructure, express_algorithms_Parameter, express_algorithms_ActualStructureConstraint, AGGREGATEType, express_instances_IntegerValue, RealValue, express_instances_AggregateValue, ConcreteValue, express_instances_Constant, express_instances_LogicalValue, express_instances_TypedInstance, express_algorithms_ActualLISTType, express_algorithms_Variable, express_algorithms_GenericElement, express_algorithms_VARParameter, algorithms_Parameter, express_algorithms_ActualDataType, core_GenericType, express_algorithms_ActualBAGType, express_instances_AttributeValue, express_instances_ARRAYValue, AggregateValue, ArrayMember, express_instances_RoleName, StringValue, express_instances_EntityInstance, TypedInstance, EntityValue, express_instances_EntityValue, express_instances_SETValue, express_instances_ListMember, express_instances_BagMember, express_instances_SingleEntityValue, express_instances_Indeterminate, express_instances_SingleLeafInstance, express_instances_GenericAggregate, LISTValue, express_instances_BinaryValue, express_instances_SpecializedValue, express_instances_BAGValue, BagMember, express_instances_EnumerationItem, instances_TypedInstance, instances_ConcreteValue, express_instances_ArrayMember, express_instances_Population, express_instances_RealValue, NumberValue, express_instances_NumberValue, express_instances_BooleanValue, LogicalValue, express_instances_MultiLeafInstance, express_instances_LISTValue, express_instances_SimpleValue, core_Instance, instances_AggregateValue, express_instances_ConcreteValue, express_instances_StringValue, express_instances_TypeName, express_instances_PartialEntityValue, SingleEntityValue},
    associations={assertsExpression21, invokes23, actualParameters24, namedSupertype0, constraints1, constrainedSubtypes2, equivalentRule3, collection4, constraints6, content8, withinPopulation9, constraintRules11, forType12, id14, supportingBody16, constrainedExtents17, containsRules19, bodyStatements_Statement46, labelValue48, action50, bindsToReference25, body26, aliasVariable29, boundValue31, initialValue33, increment36, referent39, refersTo41, refersTo42, baseEntity43, ifCondition76, elseActions78, thenActions81, indexValue53, baseAggregate55, whileExpression58, body60, controlVariable62, untilExpression64, baseEntity67, refersTo69, refersTo71, cases72, selectionExpression73, refersTo102, baseValue103, returnValue84, assignedValue86, variable88, entityInstance91, derivation93, refersTo95, refersTo96, firstBit97, lastBit99, inProcedureCall128, inFunctionCall129, formalParameter131, actualReferent132, actualValue135, leftOperand105, rightOperand107, resultValue110, bindings111, firstCode113, lastCode115, resultValue118, attributeGroup119, bindings122, operand124, targetType126, queryVariable152, aggregateOperand154, attributeValue157, toValue159, refersTo138, refersTo140, indexValue141, refersTo143, unaryOperand145, inverseOf147, refersTo149, selectCondition150, declaresExplicitAttribute177, declaresAttribute179, declaredIn181, equivalent183, id185, attribute161, actualParameters164, invokesFunction166, returnsResult167, repetition169, toSlot170, memberValue172, refersTo175, refersTo176, values203, declaredItems205, extension207, base208, boundExpression211, upperBound188, memberType189, constraint191, lowerBound192, memberType195, evaluation196, interpretationContext197, dataType199, modelsRole201, explicit202, attributes240, playsRangeRole242, declares243, extension246, invertibleAttributes248, playsDomainRole250, derivation213, restrictedType215, refines217, upperBound219, lowerBound222, scope225, originalAttribute227, refinedRole230, alias232, playsRole235, redeclarations238, referencingType271, modelsRole273, occursIn275, interfacingSchema277, refersTo278, uniqueRules252, usedIn254, subtypeOf256, instances258, components260, documentation262, interfaces263, schemaElements264, interfacedElements265, inverse267, rangeType268, createsRelationship270, namespace298, documentation300, id302, attributeType304, ofEntity306, interfacedId280, domain282, keyComponent284, rangeView286, domain288, id290, domain292, asserts295, fundamentalType297, variables314, appearsInPopulation316, ofType318, role320, constraints322, owningEntity308, constraint310, stringLengthConstraint311, specializes312, commonElements313, upperBound343, lowerBound345, underlyingType348, hiIndex349, loIndex350, derivation324, domainView326, range329, id331, describesSchema333, appearsIn335, describesElement337, inRelationship339, ofEntity341, upperBound371, namedElements374, includesRemarks376, contains378, domain353, roles355, basedOn357, range359, localElements362, instantiates363, domainRules364, binaryLengthConstraint365, definingScope367, lowerBound369, memberType398, loIndex400, hiIndex402, allowedTypes380, extension382, base385, selectList388, scope390, localScope391, referencedAs392, referencedIn394, definedIn396, controlledBy418, implements419, variableType422, source424, matchingType405, requiredType406, result407, variable409, initialValue410, refersTo412, inBlock414, bodyStatementsSkipStatement415, bodyStatementsEscapeStatement416, requiredStructure450, body452, formalParameters454, memberType456, hiIndex425, loIndex427, upperBound430, refersTo432, memberType434, lowerBound437, structureConstraints440, typeConstraints442, formalParameterType445, matchingStructure448, valueExpression476, actualValue478, dataType481, source457, label459, actualValue462, attribute464, memberSlot467, refersTo468, represents470, state473, instanceOf474, declaredIn502, correspondsTo504, describes506, memberValue508, satisfiesType484, memberValue486, memberValue488, equivalent490, ofType492, properties495, characterizingType498, fundamentalValue500, memberSlot501, memberValue510, compositionEntityInstance512, compositionInstance514, governingSchema516, memberSlot519, refersTo521, represents523, components526},
    generalizations={gen_express_rules_ONEOFConstraint_SubtypeConstraint, gen_express_rules_SupertypeRule_CommonElement, gen_express_statements_ProcedureCall_Statement, gen_express_rules_Extent_SETValue, gen_express_rules_TOTAL_OVERConstraint_SubtypeConstraint, gen_express_rules_ANDConstraint_SubtypeConstraint, gen_express_rules_GlobalRule_core_SchemaElement, gen_express_rules_GlobalRule_core_AlgorithmScope, gen_express_rules_NamedRule_LocalElement, gen_express_statements_SkipStatement_ControlStatement, gen_express_statements_AliasStatement_algorithms_Statement, gen_express_statements_AliasStatement_core_LocalScope, gen_express_statements_ControlVariable_NamedVariable, gen_express_statements_AliasVariable_algorithms_NamedVariable, gen_express_statements_AliasVariable_algorithms_VARVariable, gen_express_statements_ControlStatement_Statement, gen_express_statements_VARCell_VARExpression, gen_express_statements_NullStatement_ControlStatement, gen_express_statements_AttributeCell_VARExpression, gen_express_statements_StatementBlock_Statement, gen_express_statements_IfStatement_Statement, gen_express_statements_MemberCell_VARExpression, gen_express_statements_RepeatStatement_algorithms_Statement, gen_express_statements_RepeatStatement_core_LocalScope, gen_express_statements_GroupCell_VARExpression, gen_express_statements_VariableCell_VARExpression, gen_express_statements_CaseStatement_Statement, gen_express_expressions_IndeterminateRef_Primary, gen_express_expressions_SELFRef_Primary, gen_express_expressions_IndexOperation_Expression, gen_express_statements_EscapeStatement_ControlStatement, gen_express_statements_ReturnStatement_ControlStatement, gen_express_statements_Assignment_Statement, gen_express_expressions_Selector_Expression, gen_express_expressions_EnumItemRef_Primary, gen_express_expressions_Literal_Primary, gen_express_expressions_BinaryIndex_IndexOperation, gen_express_expressions_BinaryOperation_Operation, gen_express_expressions_ParameterRef_Primary, gen_express_expressions_AggregateInitializer_Expression, gen_express_expressions_StringIndex_IndexOperation, gen_express_expressions_PartialEntityConstructor_Expression, gen_express_expressions_Coercion_Operation, gen_express_expressions_Primary_Expression, gen_express_expressions_QueryVariable_NamedVariable, gen_express_expressions_Operation_Expression, gen_express_expressions_AttributeRef_Selector, gen_express_expressions_AggregateIndex_IndexOperation, gen_express_expressions_GroupRef_Selector, gen_express_expressions_UnaryOperation_Operation, gen_express_expressions_UsedInRef_Selector, gen_express_expressions_ConstantRef_Primary, gen_express_expressions_QueryExpression_core_LocalScope, gen_express_expressions_QueryExpression_core_Expression, gen_express_core_TypeElement_NamedElement, gen_express_core_AGGREGATEType_GeneralizedType, gen_express_expressions_FunctionCall_Expression, gen_express_expressions_ExtentRef_Primary, gen_express_expressions_VariableRef_Primary, gen_express_core_VariableType_core_DataType, gen_express_core_VariableType_core_AttributeType, gen_express_core_GeneralBAGType_GeneralAggregationType, gen_express_core_DomainRule_core_DomainConstraint, gen_express_core_DomainRule_core_TypeElement, gen_express_core_GeneralAggregationType_core_GeneralizedType, gen_express_core_GeneralAggregationType_core_AggregationType, gen_express_core_ConcreteType_InstantiableType, gen_express_core_InverseAttribute_Attribute, gen_express_core_EnumerationType_DefinedType, gen_express_core_GeneralSETType_GeneralAggregationType, gen_express_core_LISTType_ConcreteAggregationType, gen_express_core_EntityType_core_NamedType, gen_express_core_EntityType_core_InstantiableType, gen_express_core_GeneralizedType_core_ParameterType, gen_express_core_GeneralizedType_core_AttributeType, gen_express_core_PartialEntityType_DataType, gen_express_core_Schema_Scope, gen_express_core_InvertibleAttribute_ExplicitAttribute, gen_express_core_Attribute_TypeElement, gen_express_core_NumericType_SimpleType, gen_express_core_DefinedType_core_NamedType, gen_express_core_DefinedType_core_ConcreteType, gen_express_core_UniqueRule_TypeElement, gen_express_core_DomainRole_Role, gen_express_core_InstantiableType_core_ParameterType, gen_express_core_InstantiableType_core_VariableType, gen_express_core_GeneralLISTType_GeneralAggregationType, gen_express_core_DerivedAttribute_Attribute, gen_express_core_BAGType_ConcreteAggregationType, gen_express_core_RealType_NumericType, gen_express_core_LogicType_SimpleType, gen_express_core_GenericType_GeneralizedType, gen_express_core_StringType_SimpleType, gen_express_core_AnonymousType_core_ConcreteType, gen_express_core_AnonymousType_core_InstantiableType, gen_express_core_AlgorithmScope_LocalScope, gen_express_core_SETType_ConcreteAggregationType, gen_express_core_SpecializedType_DefinedType, gen_express_core_GeneralARRAYType_GeneralAggregationType, gen_express_core_RangeRole_Role, gen_express_core_LocalElement_NamedElement, gen_express_core_SizeConstraint_DomainConstraint, gen_express_core_SelectType_DefinedType, gen_express_core_LengthConstraint_DomainConstraint, gen_express_core_LocalScope_Scope, gen_express_core_NamedType_core_InstantiableType, gen_express_core_NamedType_core_Scope, gen_express_core_NamedType_core_CommonElement, gen_express_core_NamedType_core_AttributeType, gen_express_core_BinaryType_SimpleType, gen_express_core_ARRAYType_ConcreteAggregationType, gen_express_core_ActualType_VariableType, gen_express_core_ExplicitAttribute_Attribute, gen_express_core_SimpleType_AnonymousType, gen_express_core_CommonElement_SchemaElement, gen_express_core_SchemaElement_NamedElement, gen_express_core_ConcreteAggregationType_core_AnonymousType, gen_express_core_ConcreteAggregationType_core_AggregationType, gen_express_algorithms_NamedVariable_LocalElement, gen_express_algorithms_InVariable_Variable, gen_express_algorithms_Procedure_Algorithm, gen_express_algorithms_ActualARRAYType_ActualAggregationType, gen_express_algorithms_FunctionResult_Variable, gen_express_algorithms_Function_Algorithm, gen_express_algorithms_InParameter_Parameter, gen_express_algorithms_LocalVariable_Variable, gen_express_algorithms_ActualStructure_algorithms_GenericElement, gen_express_algorithms_ActualStructure_core_AGGREGATEType, gen_express_algorithms_ActualGenericType_ActualType, gen_express_algorithms_Algorithm_core_AlgorithmScope, gen_express_algorithms_Algorithm_core_CommonElement, gen_express_algorithms_ActualAggregationType_core_ActualType, gen_express_algorithms_ActualAggregationType_core_AggregationType, gen_express_algorithms_ActualSETType_ActualAggregationType, gen_express_algorithms_ActualAGGREGATEType_ActualType, gen_express_algorithms_Parameter_LocalElement, gen_express_instances_IntegerValue_RealValue, gen_express_instances_AggregateValue_ConcreteValue, gen_express_instances_Constant_CommonElement, gen_express_instances_LogicalValue_SimpleValue, gen_express_instances_TypedInstance_Instance, gen_express_algorithms_ActualLISTType_ActualAggregationType, gen_express_algorithms_Variable_NamedVariable, gen_express_algorithms_GenericElement_LocalElement, gen_express_algorithms_VARParameter_algorithms_Parameter, gen_express_algorithms_VARParameter_algorithms_VARVariable, gen_express_algorithms_ActualDataType_core_GenericType, gen_express_algorithms_ActualDataType_algorithms_GenericElement, gen_express_algorithms_ActualBAGType_ActualAggregationType, gen_express_instances_ARRAYValue_AggregateValue, gen_express_instances_RoleName_StringValue, gen_express_instances_EntityInstance_TypedInstance, gen_express_instances_EntityValue_PartialEntityValue, gen_express_instances_SETValue_AggregateValue, gen_express_instances_Indeterminate_Instance, gen_express_instances_SingleLeafInstance_EntityInstance, gen_express_instances_GenericAggregate_LISTValue, gen_express_instances_BinaryValue_SimpleValue, gen_express_instances_SpecializedValue_TypedInstance, gen_express_instances_BAGValue_AggregateValue, gen_express_instances_EnumerationItem_core_TypeElement, gen_express_instances_EnumerationItem_instances_TypedInstance, gen_express_instances_EnumerationItem_instances_ConcreteValue, gen_express_instances_RealValue_NumberValue, gen_express_instances_NumberValue_SimpleValue, gen_express_instances_BooleanValue_LogicalValue, gen_express_instances_MultiLeafInstance_EntityInstance, gen_express_instances_SimpleValue_ConcreteValue, gen_express_instances_LISTValue_core_Instance, gen_express_instances_LISTValue_instances_AggregateValue, gen_express_instances_ConcreteValue_Instance, gen_express_instances_StringValue_SimpleValue, gen_express_instances_TypeName_StringValue, gen_express_instances_PartialEntityValue_Instance},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)