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
SeverityKind: Enumeration = Enumeration(
    name="SeverityKind",
    literals={
            EnumerationLiteral(name="error"),
			EnumerationLiteral(name="fatal"),
			EnumerationLiteral(name="warning")
    }
)

DirectionKind: Enumeration = Enumeration(
    name="DirectionKind",
    literals={
            EnumerationLiteral(name="in_"),
			EnumerationLiteral(name="inout"),
			EnumerationLiteral(name="out")
    }
)

ImportKind: Enumeration = Enumeration(
    name="ImportKind",
    literals={
            EnumerationLiteral(name="extension"),
			EnumerationLiteral(name="access")
    }
)

EnforcementMode: Enumeration = Enumeration(
    name="EnforcementMode",
    literals={
            EnumerationLiteral(name="Deletion"),
			EnumerationLiteral(name="Creation")
    }
)

CollectionKind: Enumeration = Enumeration(
    name="CollectionKind",
    literals={
            EnumerationLiteral(name="OrderedSet"),
			EnumerationLiteral(name="Set"),
			EnumerationLiteral(name="Bag"),
			EnumerationLiteral(name="Sequence")
    }
)

# Classes
qvttemplate_TemplateExp = Class(name="qvttemplate_TemplateExp", is_abstract=True)
LiteralExp = Class(name="LiteralExp")
Variable = Class(name="Variable")
OclExpression = Class(name="OclExpression")
qvttemplate_ObjectTemplateExp = Class(name="qvttemplate_ObjectTemplateExp")
TemplateExp = Class(name="TemplateExp")
PropertyTemplateItem = Class(name="PropertyTemplateItem")
Class_ = Class(name="Class")
qvttemplate_CollectionTemplateExp = Class(name="qvttemplate_CollectionTemplateExp")
qvttemplate_PropertyTemplateItem = Class(name="qvttemplate_PropertyTemplateItem")
Element = Class(name="Element")
ObjectTemplateExp = Class(name="ObjectTemplateExp")
Property_ = Class(name="Property")
imperativeocl_ImperativeIterateExp = Class(name="imperativeocl_ImperativeIterateExp")
ImperativeLoopExp = Class(name="ImperativeLoopExp")
imperativeocl_AssignExp = Class(name="imperativeocl_AssignExp")
ImperativeExpression = Class(name="ImperativeExpression")
imperativeocl_BlockExp = Class(name="imperativeocl_BlockExp")
imperativeocl_SwitchExp = Class(name="imperativeocl_SwitchExp")
CallExp = Class(name="CallExp")
AltExp = Class(name="AltExp")
imperativeocl_VariableInitExp = Class(name="imperativeocl_VariableInitExp")
CollectionType = Class(name="CollectionType")
imperativeocl_ComputeExp = Class(name="imperativeocl_ComputeExp")
imperativeocl_AltExp = Class(name="imperativeocl_AltExp")
imperativeocl_UnlinkExp = Class(name="imperativeocl_UnlinkExp")
imperativeocl_ReturnExp = Class(name="imperativeocl_ReturnExp")
imperativeocl_BreakExp = Class(name="imperativeocl_BreakExp")
imperativeocl_TryExp = Class(name="imperativeocl_TryExp")
Type = Class(name="Type")
imperativeocl_RaiseExp = Class(name="imperativeocl_RaiseExp")
imperativeocl_WhileExp = Class(name="imperativeocl_WhileExp")
imperativeocl_Typedef = Class(name="imperativeocl_Typedef")
imperativeocl_InstantiationExp = Class(name="imperativeocl_InstantiationExp")
imperativeocl_DictionaryType = Class(name="imperativeocl_DictionaryType")
imperativeocl_DictLiteralExp = Class(name="imperativeocl_DictLiteralExp")
DictLiteralPart = Class(name="DictLiteralPart")
imperativeocl_DictLiteralPart = Class(name="imperativeocl_DictLiteralPart")
imperativeocl_TemplateParameterType = Class(name="imperativeocl_TemplateParameterType")
imperativeocl_LogExp = Class(name="imperativeocl_LogExp")
imperativeocl_ContinueExp = Class(name="imperativeocl_ContinueExp")
imperativeocl_ForExp = Class(name="imperativeocl_ForExp")
imperativeocl_TupleExp = Class(name="imperativeocl_TupleExp")
imperativeocl_AssertExp = Class(name="imperativeocl_AssertExp")
LogExp = Class(name="LogExp")
imperativeocl_ImperativeLoopExp = Class(name="imperativeocl_ImperativeLoopExp", is_abstract=True)
LoopExp = Class(name="LoopExp")
imperativeocl_CollectorExp = Class(name="imperativeocl_CollectorExp")
imperativeocl_ImperativeExpression = Class(name="imperativeocl_ImperativeExpression", is_abstract=True)
imperativeocl_UnpackExp = Class(name="imperativeocl_UnpackExp")
imperativeocl_AnonymousTupleType = Class(name="imperativeocl_AnonymousTupleType")
imperativeocl_AnonymousTupleLiteralExp = Class(name="imperativeocl_AnonymousTupleLiteralExp")
AnonymousTupleLiteralPart = Class(name="AnonymousTupleLiteralPart")
imperativeocl_AnonymousTupleLiteralPart = Class(name="imperativeocl_AnonymousTupleLiteralPart")
Operation = Class(name="Operation")
emof_DataType = Class(name="emof_DataType", is_abstract=True)
emof_Element = Class(name="emof_Element", is_abstract=True)
Object = Class(name="Object")
Tag = Class(name="Tag")
Comment = Class(name="Comment")
emof_Tag = Class(name="emof_Tag")
Transformation = Class(name="Transformation")
Module = Class(name="Module")
emof_Enumeration = Class(name="emof_Enumeration")
DataType = Class(name="DataType")
EnumerationLiteral = Class(name="EnumerationLiteral")
emof_NamedElement = Class(name="emof_NamedElement", is_abstract=True)
emof_Extent = Class(name="emof_Extent")
emof_Object = Class(name="emof_Object")
emof_Operation = Class(name="emof_Operation")
MultiplicityElement = Class(name="MultiplicityElement")
TypedElement = Class(name="TypedElement")
imperativeocl_ListType = Class(name="imperativeocl_ListType")
emof_Class = Class(name="emof_Class")
emof_MultiplicityElement = Class(name="emof_MultiplicityElement", is_abstract=True)
emof_Package = Class(name="emof_Package")
NamedElement = Class(name="NamedElement")
Package = Class(name="Package")
emof_Type = Class(name="emof_Type", is_abstract=True)
emof_Parameter = Class(name="emof_Parameter")
emof_EnumerationLiteral = Class(name="emof_EnumerationLiteral")
Enumeration_ = Class(name="Enumeration")
emof_Property = Class(name="emof_Property")
Parameter_ = Class(name="Parameter")
emof_PrimitiveType = Class(name="emof_PrimitiveType")
emof_URIExtent = Class(name="emof_URIExtent")
Extent = Class(name="Extent")
emof_Comment = Class(name="emof_Comment")
qvtoperational_MappingBody = Class(name="qvtoperational_MappingBody")
OperationBody = Class(name="OperationBody")
qvtoperational_Helper = Class(name="qvtoperational_Helper")
ImperativeOperation = Class(name="ImperativeOperation")
qvtoperational_ResolveExp = Class(name="qvtoperational_ResolveExp")
qvtoperational_ResolveInExp = Class(name="qvtoperational_ResolveInExp")
ResolveExp = Class(name="ResolveExp")
MappingOperation = Class(name="MappingOperation")
qvtoperational_OperationalTransformation = Class(name="qvtoperational_OperationalTransformation")
emof_TypedElement = Class(name="emof_TypedElement", is_abstract=True)
Relation = Class(name="Relation")
qvtoperational_MappingParameter = Class(name="qvtoperational_MappingParameter")
VarParameter = Class(name="VarParameter")
RelationDomain = Class(name="RelationDomain")
qvtoperational_MappingOperation = Class(name="qvtoperational_MappingOperation")
qvtoperational_MappingCallExp = Class(name="qvtoperational_MappingCallExp")
ImperativeCallExp = Class(name="ImperativeCallExp")
qvtoperational_Constructor = Class(name="qvtoperational_Constructor")
qvtoperational_ContextualProperty = Class(name="qvtoperational_ContextualProperty")
qvtoperational_EntryOperation = Class(name="qvtoperational_EntryOperation")
ModelParameter = Class(name="ModelParameter")
EntryOperation = Class(name="EntryOperation")
qvtoperational_Library = Class(name="qvtoperational_Library")
qvtoperational_ModelParameter = Class(name="qvtoperational_ModelParameter")
qvtoperational_ModelType = Class(name="qvtoperational_ModelType")
URIExtent = Class(name="URIExtent")
qvtoperational_Module = Class(name="qvtoperational_Module")
ModuleImport = Class(name="ModuleImport")
ModelType = Class(name="ModelType")
qvtoperational_ImperativeCallExp = Class(name="qvtoperational_ImperativeCallExp")
OperationCallExp = Class(name="OperationCallExp")
qvtoperational_ImperativeOperation = Class(name="qvtoperational_ImperativeOperation")
qvtoperational_VarParameter = Class(name="qvtoperational_VarParameter")
qvtoperational_OperationBody = Class(name="qvtoperational_OperationBody")
qvtoperational_ConstructorBody = Class(name="qvtoperational_ConstructorBody")
qvtoperational_ObjectExp = Class(name="qvtoperational_ObjectExp")
InstantiationExp = Class(name="InstantiationExp")
ConstructorBody = Class(name="ConstructorBody")
qvtcore_Area = Class(name="qvtcore_Area", is_abstract=True)
GuardPattern = Class(name="GuardPattern")
qvtoperational_ModuleImport = Class(name="qvtoperational_ModuleImport")
qvtcore_BottomPattern = Class(name="qvtcore_BottomPattern")
CorePattern = Class(name="CorePattern")
Area = Class(name="Area")
Assignment = Class(name="Assignment")
RealizedVariable = Class(name="RealizedVariable")
EnforcementOperation = Class(name="EnforcementOperation")
qvtcore_GuardPattern = Class(name="qvtcore_GuardPattern")
qvtcore_Mapping = Class(name="qvtcore_Mapping")
Rule = Class(name="Rule")
Mapping = Class(name="Mapping")
qvtcore_RealizedVariable = Class(name="qvtcore_RealizedVariable")
qvtcore_CoreDomain = Class(name="qvtcore_CoreDomain")
Domain = Class(name="Domain")
qvtcore_CorePattern = Class(name="qvtcore_CorePattern")
Pattern = Class(name="Pattern")
BottomPattern = Class(name="BottomPattern")
qvtcore_Assignment = Class(name="qvtcore_Assignment")
qvtbase_Domain = Class(name="qvtbase_Domain")
TypedModel = Class(name="TypedModel")
qvtbase_Transformation = Class(name="qvtbase_Transformation")
qvtbase_TypedModel = Class(name="qvtbase_TypedModel")
qvtbase_Rule = Class(name="qvtbase_Rule")
qvtcore_EnforcementOperation = Class(name="qvtcore_EnforcementOperation")
Predicate = Class(name="Predicate")
qvtbase_Predicate = Class(name="qvtbase_Predicate")
qvtbase_Function = Class(name="qvtbase_Function")
qvtbase_FunctionParameter = Class(name="qvtbase_FunctionParameter")
qvtrelation_RelationalTransformation = Class(name="qvtrelation_RelationalTransformation")
Key = Class(name="Key")
qvtrelation_Relation = Class(name="qvtrelation_Relation")
RelationImplementation = Class(name="RelationImplementation")
qvtbase_Pattern = Class(name="qvtbase_Pattern")
qvtrelation_RelationDomain = Class(name="qvtrelation_RelationDomain")
DomainPattern = Class(name="DomainPattern")
qvtrelation_DomainPattern = Class(name="qvtrelation_DomainPattern")
qvtrelation_RelationImplementation = Class(name="qvtrelation_RelationImplementation")
qvtrelation_Key = Class(name="qvtrelation_Key")
RelationalTransformation = Class(name="RelationalTransformation")
essentialocl_OclExpression = Class(name="essentialocl_OclExpression", is_abstract=True)
TryExp = Class(name="TryExp")
essentialocl_UnlimitedNaturalExp = Class(name="essentialocl_UnlimitedNaturalExp")
NumericLiteralExp = Class(name="NumericLiteralExp")
essentialocl_IfExp = Class(name="essentialocl_IfExp")
essentialocl_LetExp = Class(name="essentialocl_LetExp")
essentialocl_BooleanLiteralExp = Class(name="essentialocl_BooleanLiteralExp")
PrimitiveLiteralExp = Class(name="PrimitiveLiteralExp")
essentialocl_CallExp = Class(name="essentialocl_CallExp", is_abstract=True)
LetExp = Class(name="LetExp")
ComputeExp = Class(name="ComputeExp")
essentialocl_PropertyCallExp = Class(name="essentialocl_PropertyCallExp")
FeaturePropertyCall = Class(name="FeaturePropertyCall")
essentialocl_VariableExp = Class(name="essentialocl_VariableExp")
essentialocl_TypeExp = Class(name="essentialocl_TypeExp")
essentialocl_LoopExp = Class(name="essentialocl_LoopExp", is_abstract=True)
essentialocl_Variable = Class(name="essentialocl_Variable")
essentialocl_IntegerLiteralExp = Class(name="essentialocl_IntegerLiteralExp")
essentialocl_OperationCallExp = Class(name="essentialocl_OperationCallExp")
essentialocl_RealLiteralExp = Class(name="essentialocl_RealLiteralExp")
essentialocl_LiteralExp = Class(name="essentialocl_LiteralExp", is_abstract=True)
essentialocl_IterateExp = Class(name="essentialocl_IterateExp")
essentialocl_PrimitiveLiteralExp = Class(name="essentialocl_PrimitiveLiteralExp", is_abstract=True)
essentialocl_NumericLiteralExp = Class(name="essentialocl_NumericLiteralExp", is_abstract=True)
essentialocl_CollectionLiteralExp = Class(name="essentialocl_CollectionLiteralExp")
CollectionLiteralPart = Class(name="CollectionLiteralPart")
essentialocl_CollectionLiteralPart = Class(name="essentialocl_CollectionLiteralPart", is_abstract=True)
CollectionLiteralExp = Class(name="CollectionLiteralExp")
essentialocl_CollectionItem = Class(name="essentialocl_CollectionItem")
essentialocl_IteratorExp = Class(name="essentialocl_IteratorExp")
essentialocl_TupleLiteralExp = Class(name="essentialocl_TupleLiteralExp")
essentialocl_StringLiteralExp = Class(name="essentialocl_StringLiteralExp")
TupleLiteralPart = Class(name="TupleLiteralPart")
essentialocl_NullLiteralExp = Class(name="essentialocl_NullLiteralExp")
essentialocl_ExpressionInOcl = Class(name="essentialocl_ExpressionInOcl")
OpaqueExpression = Class(name="OpaqueExpression")
essentialocl_OpaqueExpression = Class(name="essentialocl_OpaqueExpression")
essentialocl_InvalidLiteralExp = Class(name="essentialocl_InvalidLiteralExp")
essentialocl_FeaturePropertyCall = Class(name="essentialocl_FeaturePropertyCall", is_abstract=True)
essentialocl_TupleLiteralPart = Class(name="essentialocl_TupleLiteralPart")
TupleLiteralExp = Class(name="TupleLiteralExp")
essentialocl_BagType = Class(name="essentialocl_BagType")
essentialocl_CollectionType = Class(name="essentialocl_CollectionType", is_abstract=True)
essentialocl_EnumLiteralExp = Class(name="essentialocl_EnumLiteralExp")
essentialocl_InvalidType = Class(name="essentialocl_InvalidType")
essentialocl_CollectionRange = Class(name="essentialocl_CollectionRange")
essentialocl_OrderedSetType = Class(name="essentialocl_OrderedSetType")
essentialocl_SequenceType = Class(name="essentialocl_SequenceType")
essentialocl_VoidType = Class(name="essentialocl_VoidType")
essentialocl_AnyType = Class(name="essentialocl_AnyType")
essentialocl_SetType = Class(name="essentialocl_SetType")
essentialocl_TupleType = Class(name="essentialocl_TupleType")

# qvttemplate_TemplateExp class attributes and methods

# LiteralExp class attributes and methods

# Variable class attributes and methods

# OclExpression class attributes and methods

# qvttemplate_ObjectTemplateExp class attributes and methods

# TemplateExp class attributes and methods

# PropertyTemplateItem class attributes and methods

# Class class attributes and methods

# qvttemplate_CollectionTemplateExp class attributes and methods
qvttemplate_CollectionTemplateExp_kind: Property = Property(name="kind", type=StringType)
qvttemplate_CollectionTemplateExp.attributes={qvttemplate_CollectionTemplateExp_kind}

# qvttemplate_PropertyTemplateItem class attributes and methods

# Element class attributes and methods

# ObjectTemplateExp class attributes and methods

# Property class attributes and methods

# imperativeocl_ImperativeIterateExp class attributes and methods

# ImperativeLoopExp class attributes and methods

# imperativeocl_AssignExp class attributes and methods
imperativeocl_AssignExp_isReset: Property = Property(name="isReset", type=StringType)
imperativeocl_AssignExp.attributes={imperativeocl_AssignExp_isReset}

# ImperativeExpression class attributes and methods

# imperativeocl_BlockExp class attributes and methods

# imperativeocl_SwitchExp class attributes and methods

# CallExp class attributes and methods

# AltExp class attributes and methods

# imperativeocl_VariableInitExp class attributes and methods
imperativeocl_VariableInitExp_withResult: Property = Property(name="withResult", type=StringType)
imperativeocl_VariableInitExp.attributes={imperativeocl_VariableInitExp_withResult}

# CollectionType class attributes and methods

# imperativeocl_ComputeExp class attributes and methods

# imperativeocl_AltExp class attributes and methods

# imperativeocl_UnlinkExp class attributes and methods

# imperativeocl_ReturnExp class attributes and methods

# imperativeocl_BreakExp class attributes and methods

# imperativeocl_TryExp class attributes and methods

# Type class attributes and methods

# imperativeocl_RaiseExp class attributes and methods

# imperativeocl_WhileExp class attributes and methods

# imperativeocl_Typedef class attributes and methods

# imperativeocl_InstantiationExp class attributes and methods

# imperativeocl_DictionaryType class attributes and methods

# imperativeocl_DictLiteralExp class attributes and methods

# DictLiteralPart class attributes and methods

# imperativeocl_DictLiteralPart class attributes and methods

# imperativeocl_TemplateParameterType class attributes and methods
imperativeocl_TemplateParameterType_specification: Property = Property(name="specification", type=StringType)
imperativeocl_TemplateParameterType.attributes={imperativeocl_TemplateParameterType_specification}

# imperativeocl_LogExp class attributes and methods
imperativeocl_LogExp_text: Property = Property(name="text", type=StringType)
imperativeocl_LogExp_level: Property = Property(name="level", type=StringType)
imperativeocl_LogExp.attributes={imperativeocl_LogExp_text, imperativeocl_LogExp_level}

# imperativeocl_ContinueExp class attributes and methods

# imperativeocl_ForExp class attributes and methods

# imperativeocl_TupleExp class attributes and methods

# imperativeocl_AssertExp class attributes and methods
imperativeocl_AssertExp_severity: Property = Property(name="severity", type=StringType)
imperativeocl_AssertExp.attributes={imperativeocl_AssertExp_severity}

# LogExp class attributes and methods

# imperativeocl_ImperativeLoopExp class attributes and methods

# LoopExp class attributes and methods

# imperativeocl_CollectorExp class attributes and methods

# imperativeocl_ImperativeExpression class attributes and methods

# imperativeocl_UnpackExp class attributes and methods

# imperativeocl_AnonymousTupleType class attributes and methods

# imperativeocl_AnonymousTupleLiteralExp class attributes and methods

# AnonymousTupleLiteralPart class attributes and methods

# imperativeocl_AnonymousTupleLiteralPart class attributes and methods

# Operation class attributes and methods

# emof_DataType class attributes and methods

# emof_Element class attributes and methods

# Object class attributes and methods

# Tag class attributes and methods

# Comment class attributes and methods

# emof_Tag class attributes and methods
emof_Tag_value: Property = Property(name="value", type=StringType)
emof_Tag_name: Property = Property(name="name", type=StringType)
emof_Tag.attributes={emof_Tag_value, emof_Tag_name}

# Transformation class attributes and methods

# Module class attributes and methods

# emof_Enumeration class attributes and methods

# DataType class attributes and methods

# EnumerationLiteral class attributes and methods

# emof_NamedElement class attributes and methods
emof_NamedElement_name: Property = Property(name="name", type=StringType)
emof_NamedElement.attributes={emof_NamedElement_name}

# emof_Extent class attributes and methods

# emof_Object class attributes and methods

# emof_Operation class attributes and methods

# MultiplicityElement class attributes and methods

# TypedElement class attributes and methods

# imperativeocl_ListType class attributes and methods

# emof_Class class attributes and methods
emof_Class_isAbstract: Property = Property(name="isAbstract", type=StringType)
emof_Class.attributes={emof_Class_isAbstract}

# emof_MultiplicityElement class attributes and methods
emof_MultiplicityElement_isOrdered: Property = Property(name="isOrdered", type=StringType)
emof_MultiplicityElement_isUnique: Property = Property(name="isUnique", type=StringType)
emof_MultiplicityElement_lower: Property = Property(name="lower", type=StringType)
emof_MultiplicityElement_upper: Property = Property(name="upper", type=StringType)
emof_MultiplicityElement.attributes={emof_MultiplicityElement_isOrdered, emof_MultiplicityElement_isUnique, emof_MultiplicityElement_lower, emof_MultiplicityElement_upper}

# emof_Package class attributes and methods
emof_Package_uri: Property = Property(name="uri", type=StringType)
emof_Package.attributes={emof_Package_uri}

# NamedElement class attributes and methods

# Package class attributes and methods

# emof_Type class attributes and methods

# emof_Parameter class attributes and methods

# emof_EnumerationLiteral class attributes and methods

# Enumeration class attributes and methods

# emof_Property class attributes and methods
emof_Property_isReadOnly: Property = Property(name="isReadOnly", type=StringType)
emof_Property_isDerived: Property = Property(name="isDerived", type=StringType)
emof_Property_isComposite: Property = Property(name="isComposite", type=StringType)
emof_Property_isId: Property = Property(name="isId", type=StringType)
emof_Property_default: Property = Property(name="default", type=StringType)
emof_Property.attributes={emof_Property_isComposite, emof_Property_isDerived, emof_Property_isId, emof_Property_default, emof_Property_isReadOnly}

# Parameter class attributes and methods

# emof_PrimitiveType class attributes and methods

# emof_URIExtent class attributes and methods

# Extent class attributes and methods

# emof_Comment class attributes and methods

# qvtoperational_MappingBody class attributes and methods

# OperationBody class attributes and methods

# qvtoperational_Helper class attributes and methods
qvtoperational_Helper_isQuery: Property = Property(name="isQuery", type=StringType)
qvtoperational_Helper.attributes={qvtoperational_Helper_isQuery}

# ImperativeOperation class attributes and methods

# qvtoperational_ResolveExp class attributes and methods
qvtoperational_ResolveExp_one: Property = Property(name="one", type=StringType)
qvtoperational_ResolveExp_isInverse: Property = Property(name="isInverse", type=StringType)
qvtoperational_ResolveExp_isDeferred: Property = Property(name="isDeferred", type=StringType)
qvtoperational_ResolveExp.attributes={qvtoperational_ResolveExp_one, qvtoperational_ResolveExp_isInverse, qvtoperational_ResolveExp_isDeferred}

# qvtoperational_ResolveInExp class attributes and methods

# ResolveExp class attributes and methods

# MappingOperation class attributes and methods

# qvtoperational_OperationalTransformation class attributes and methods

# emof_TypedElement class attributes and methods

# Relation class attributes and methods

# qvtoperational_MappingParameter class attributes and methods

# VarParameter class attributes and methods

# RelationDomain class attributes and methods

# qvtoperational_MappingOperation class attributes and methods

# qvtoperational_MappingCallExp class attributes and methods
qvtoperational_MappingCallExp_isStrict: Property = Property(name="isStrict", type=StringType)
qvtoperational_MappingCallExp.attributes={qvtoperational_MappingCallExp_isStrict}

# ImperativeCallExp class attributes and methods

# qvtoperational_Constructor class attributes and methods

# qvtoperational_ContextualProperty class attributes and methods

# qvtoperational_EntryOperation class attributes and methods

# ModelParameter class attributes and methods

# EntryOperation class attributes and methods

# qvtoperational_Library class attributes and methods

# qvtoperational_ModelParameter class attributes and methods

# qvtoperational_ModelType class attributes and methods
qvtoperational_ModelType_conformanceKind: Property = Property(name="conformanceKind", type=StringType)
qvtoperational_ModelType.attributes={qvtoperational_ModelType_conformanceKind}

# URIExtent class attributes and methods

# qvtoperational_Module class attributes and methods
qvtoperational_Module_isBlackbox: Property = Property(name="isBlackbox", type=StringType)
qvtoperational_Module.attributes={qvtoperational_Module_isBlackbox}

# ModuleImport class attributes and methods

# ModelType class attributes and methods

# qvtoperational_ImperativeCallExp class attributes and methods
qvtoperational_ImperativeCallExp_isVirtual: Property = Property(name="isVirtual", type=StringType)
qvtoperational_ImperativeCallExp.attributes={qvtoperational_ImperativeCallExp_isVirtual}

# OperationCallExp class attributes and methods

# qvtoperational_ImperativeOperation class attributes and methods
qvtoperational_ImperativeOperation_isBlackbox: Property = Property(name="isBlackbox", type=StringType)
qvtoperational_ImperativeOperation.attributes={qvtoperational_ImperativeOperation_isBlackbox}

# qvtoperational_VarParameter class attributes and methods
qvtoperational_VarParameter_kind: Property = Property(name="kind", type=StringType)
qvtoperational_VarParameter.attributes={qvtoperational_VarParameter_kind}

# qvtoperational_OperationBody class attributes and methods

# qvtoperational_ConstructorBody class attributes and methods

# qvtoperational_ObjectExp class attributes and methods

# InstantiationExp class attributes and methods

# ConstructorBody class attributes and methods

# qvtcore_Area class attributes and methods

# GuardPattern class attributes and methods

# qvtoperational_ModuleImport class attributes and methods
qvtoperational_ModuleImport_kind: Property = Property(name="kind", type=StringType)
qvtoperational_ModuleImport.attributes={qvtoperational_ModuleImport_kind}

# qvtcore_BottomPattern class attributes and methods

# CorePattern class attributes and methods

# Area class attributes and methods

# Assignment class attributes and methods

# RealizedVariable class attributes and methods

# EnforcementOperation class attributes and methods

# qvtcore_GuardPattern class attributes and methods

# qvtcore_Mapping class attributes and methods

# Rule class attributes and methods

# Mapping class attributes and methods

# qvtcore_RealizedVariable class attributes and methods

# qvtcore_CoreDomain class attributes and methods

# Domain class attributes and methods

# qvtcore_CorePattern class attributes and methods

# Pattern class attributes and methods

# BottomPattern class attributes and methods

# qvtcore_Assignment class attributes and methods
qvtcore_Assignment_isDefault: Property = Property(name="isDefault", type=StringType)
qvtcore_Assignment.attributes={qvtcore_Assignment_isDefault}

# qvtbase_Domain class attributes and methods
qvtbase_Domain_isCheckable: Property = Property(name="isCheckable", type=StringType)
qvtbase_Domain_isEnforceable: Property = Property(name="isEnforceable", type=StringType)
qvtbase_Domain.attributes={qvtbase_Domain_isEnforceable, qvtbase_Domain_isCheckable}

# TypedModel class attributes and methods

# qvtbase_Transformation class attributes and methods

# qvtbase_TypedModel class attributes and methods

# qvtbase_Rule class attributes and methods

# qvtcore_EnforcementOperation class attributes and methods
qvtcore_EnforcementOperation_enforcementMode: Property = Property(name="enforcementMode", type=StringType)
qvtcore_EnforcementOperation.attributes={qvtcore_EnforcementOperation_enforcementMode}

# Predicate class attributes and methods

# qvtbase_Predicate class attributes and methods

# qvtbase_Function class attributes and methods

# qvtbase_FunctionParameter class attributes and methods

# qvtrelation_RelationalTransformation class attributes and methods

# Key class attributes and methods

# qvtrelation_Relation class attributes and methods
qvtrelation_Relation_isTopLevel: Property = Property(name="isTopLevel", type=StringType)
qvtrelation_Relation.attributes={qvtrelation_Relation_isTopLevel}

# RelationImplementation class attributes and methods

# qvtbase_Pattern class attributes and methods

# qvtrelation_RelationDomain class attributes and methods

# DomainPattern class attributes and methods

# qvtrelation_DomainPattern class attributes and methods

# qvtrelation_RelationImplementation class attributes and methods

# qvtrelation_Key class attributes and methods

# RelationalTransformation class attributes and methods

# essentialocl_OclExpression class attributes and methods

# TryExp class attributes and methods

# essentialocl_UnlimitedNaturalExp class attributes and methods
essentialocl_UnlimitedNaturalExp_symbol: Property = Property(name="symbol", type=StringType)
essentialocl_UnlimitedNaturalExp.attributes={essentialocl_UnlimitedNaturalExp_symbol}

# NumericLiteralExp class attributes and methods

# essentialocl_IfExp class attributes and methods

# essentialocl_LetExp class attributes and methods

# essentialocl_BooleanLiteralExp class attributes and methods
essentialocl_BooleanLiteralExp_booleanSymbol: Property = Property(name="booleanSymbol", type=StringType)
essentialocl_BooleanLiteralExp.attributes={essentialocl_BooleanLiteralExp_booleanSymbol}

# PrimitiveLiteralExp class attributes and methods

# essentialocl_CallExp class attributes and methods

# LetExp class attributes and methods

# ComputeExp class attributes and methods

# essentialocl_PropertyCallExp class attributes and methods

# FeaturePropertyCall class attributes and methods

# essentialocl_VariableExp class attributes and methods

# essentialocl_TypeExp class attributes and methods

# essentialocl_LoopExp class attributes and methods

# essentialocl_Variable class attributes and methods

# essentialocl_IntegerLiteralExp class attributes and methods
essentialocl_IntegerLiteralExp_integerSymbol: Property = Property(name="integerSymbol", type=StringType)
essentialocl_IntegerLiteralExp.attributes={essentialocl_IntegerLiteralExp_integerSymbol}

# essentialocl_OperationCallExp class attributes and methods

# essentialocl_RealLiteralExp class attributes and methods
essentialocl_RealLiteralExp_realSymbol: Property = Property(name="realSymbol", type=StringType)
essentialocl_RealLiteralExp.attributes={essentialocl_RealLiteralExp_realSymbol}

# essentialocl_LiteralExp class attributes and methods

# essentialocl_IterateExp class attributes and methods

# essentialocl_PrimitiveLiteralExp class attributes and methods

# essentialocl_NumericLiteralExp class attributes and methods

# essentialocl_CollectionLiteralExp class attributes and methods
essentialocl_CollectionLiteralExp_kind: Property = Property(name="kind", type=StringType)
essentialocl_CollectionLiteralExp.attributes={essentialocl_CollectionLiteralExp_kind}

# CollectionLiteralPart class attributes and methods

# essentialocl_CollectionLiteralPart class attributes and methods

# CollectionLiteralExp class attributes and methods

# essentialocl_CollectionItem class attributes and methods

# essentialocl_IteratorExp class attributes and methods

# essentialocl_TupleLiteralExp class attributes and methods

# essentialocl_StringLiteralExp class attributes and methods
essentialocl_StringLiteralExp_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
essentialocl_StringLiteralExp.attributes={essentialocl_StringLiteralExp_stringSymbol}

# TupleLiteralPart class attributes and methods

# essentialocl_NullLiteralExp class attributes and methods

# essentialocl_ExpressionInOcl class attributes and methods

# OpaqueExpression class attributes and methods

# essentialocl_OpaqueExpression class attributes and methods

# essentialocl_InvalidLiteralExp class attributes and methods

# essentialocl_FeaturePropertyCall class attributes and methods

# essentialocl_TupleLiteralPart class attributes and methods

# TupleLiteralExp class attributes and methods

# essentialocl_BagType class attributes and methods

# essentialocl_CollectionType class attributes and methods

# essentialocl_EnumLiteralExp class attributes and methods

# essentialocl_InvalidType class attributes and methods

# essentialocl_CollectionRange class attributes and methods

# essentialocl_OrderedSetType class attributes and methods

# essentialocl_SequenceType class attributes and methods

# essentialocl_VoidType class attributes and methods

# essentialocl_AnyType class attributes and methods

# essentialocl_SetType class attributes and methods

# essentialocl_TupleType class attributes and methods

# Relationships
bindsTo0: BinaryAssociation = BinaryAssociation(
    name="bindsTo0",
    ends={
        Property(name="Variable", type=qvttemplate_TemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="qvttemplate_TemplateExp", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
where1: BinaryAssociation = BinaryAssociation(
    name="where1",
    ends={
        Property(name="OclExpression", type=qvttemplate_TemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="qvttemplate_TemplateExp2", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
part3: BinaryAssociation = BinaryAssociation(
    name="part3",
    ends={
        Property(name="PropertyTemplateItem", type=qvttemplate_ObjectTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="objContainer", type=PropertyTemplateItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredClass4: BinaryAssociation = BinaryAssociation(
    name="referredClass4",
    ends={
        Property(name="Class", type=qvttemplate_ObjectTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="qvttemplate_ObjectTemplateExp", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
match9: BinaryAssociation = BinaryAssociation(
    name="match9",
    ends={
        Property(name="OclExpression11", type=qvttemplate_CollectionTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="qvttemplate_CollectionTemplateExp10", type=OclExpression, multiplicity=Multiplicity(0, 1))
    }
)
objContainer12: BinaryAssociation = BinaryAssociation(
    name="objContainer12",
    ends={
        Property(name="ObjectTemplateExp", type=qvttemplate_PropertyTemplateItem, multiplicity=Multiplicity(1, 1)),
        Property(name="part", type=ObjectTemplateExp, multiplicity=Multiplicity(1, 1))
    }
)
value13: BinaryAssociation = BinaryAssociation(
    name="value13",
    ends={
        Property(name="OclExpression14", type=qvttemplate_PropertyTemplateItem, multiplicity=Multiplicity(1, 1)),
        Property(name="qvttemplate_PropertyTemplateItem", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referredProperty15: BinaryAssociation = BinaryAssociation(
    name="referredProperty15",
    ends={
        Property(name="Property", type=qvttemplate_PropertyTemplateItem, multiplicity=Multiplicity(1, 1)),
        Property(name="qvttemplate_PropertyTemplateItem16", type=Property_, multiplicity=Multiplicity(1, 1))
    }
)
target17: BinaryAssociation = BinaryAssociation(
    name="target17",
    ends={
        Property(name="Variable18", type=imperativeocl_ImperativeIterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_ImperativeIterateExp", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value19: BinaryAssociation = BinaryAssociation(
    name="value19",
    ends={
        Property(name="OclExpression20", type=imperativeocl_AssignExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_AssignExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left21: BinaryAssociation = BinaryAssociation(
    name="left21",
    ends={
        Property(name="OclExpression23", type=imperativeocl_AssignExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_AssignExp22", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
defaultValue24: BinaryAssociation = BinaryAssociation(
    name="defaultValue24",
    ends={
        Property(name="OclExpression26", type=imperativeocl_AssignExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_AssignExp25", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body27: BinaryAssociation = BinaryAssociation(
    name="body27",
    ends={
        Property(name="OclExpression28", type=imperativeocl_BlockExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_BlockExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
alternativePart29: BinaryAssociation = BinaryAssociation(
    name="alternativePart29",
    ends={
        Property(name="AltExp", type=imperativeocl_SwitchExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_SwitchExp", type=AltExp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elsePart30: BinaryAssociation = BinaryAssociation(
    name="elsePart30",
    ends={
        Property(name="OclExpression32", type=imperativeocl_SwitchExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_SwitchExp31", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
part5: BinaryAssociation = BinaryAssociation(
    name="part5",
    ends={
        Property(name="OclExpression6", type=qvttemplate_CollectionTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="qvttemplate_CollectionTemplateExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredCollectionType7: BinaryAssociation = BinaryAssociation(
    name="referredCollectionType7",
    ends={
        Property(name="CollectionType", type=qvttemplate_CollectionTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="qvttemplate_CollectionTemplateExp8", type=CollectionType, multiplicity=Multiplicity(0, 1))
    }
)
body37: BinaryAssociation = BinaryAssociation(
    name="body37",
    ends={
        Property(name="OclExpression39", type=imperativeocl_WhileExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_WhileExp38", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnedElement40: BinaryAssociation = BinaryAssociation(
    name="returnedElement40",
    ends={
        Property(name="Variable41", type=imperativeocl_ComputeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="computeOwner", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body42: BinaryAssociation = BinaryAssociation(
    name="body42",
    ends={
        Property(name="OclExpression43", type=imperativeocl_ComputeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_ComputeExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition44: BinaryAssociation = BinaryAssociation(
    name="condition44",
    ends={
        Property(name="OclExpression45", type=imperativeocl_AltExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_AltExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body46: BinaryAssociation = BinaryAssociation(
    name="body46",
    ends={
        Property(name="OclExpression48", type=imperativeocl_AltExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_AltExp47", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target49: BinaryAssociation = BinaryAssociation(
    name="target49",
    ends={
        Property(name="OclExpression50", type=imperativeocl_UnlinkExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_UnlinkExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
item51: BinaryAssociation = BinaryAssociation(
    name="item51",
    ends={
        Property(name="OclExpression53", type=imperativeocl_UnlinkExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_UnlinkExp52", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value54: BinaryAssociation = BinaryAssociation(
    name="value54",
    ends={
        Property(name="OclExpression55", type=imperativeocl_ReturnExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_ReturnExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tryBody56: BinaryAssociation = BinaryAssociation(
    name="tryBody56",
    ends={
        Property(name="OclExpression57", type=imperativeocl_TryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="tryBodyOwner", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exception58: BinaryAssociation = BinaryAssociation(
    name="exception58",
    ends={
        Property(name="Type", type=imperativeocl_TryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_TryExp", type=Type, multiplicity=Multiplicity(0, 9999))
    }
)
exceptBody59: BinaryAssociation = BinaryAssociation(
    name="exceptBody59",
    ends={
        Property(name="OclExpression61", type=imperativeocl_TryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_TryExp60", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referredVariable33: BinaryAssociation = BinaryAssociation(
    name="referredVariable33",
    ends={
        Property(name="Variable34", type=imperativeocl_VariableInitExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_VariableInitExp", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition35: BinaryAssociation = BinaryAssociation(
    name="condition35",
    ends={
        Property(name="OclExpression36", type=imperativeocl_WhileExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_WhileExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
element64: BinaryAssociation = BinaryAssociation(
    name="element64",
    ends={
        Property(name="OclExpression65", type=imperativeocl_TupleExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_TupleExp", type=OclExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
base66: BinaryAssociation = BinaryAssociation(
    name="base66",
    ends={
        Property(name="Type67", type=imperativeocl_Typedef, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_Typedef", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
condition68: BinaryAssociation = BinaryAssociation(
    name="condition68",
    ends={
        Property(name="OclExpression70", type=imperativeocl_Typedef, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_Typedef69", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
instantiatedClass71: BinaryAssociation = BinaryAssociation(
    name="instantiatedClass71",
    ends={
        Property(name="Class72", type=imperativeocl_InstantiationExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_InstantiationExp", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
extent73: BinaryAssociation = BinaryAssociation(
    name="extent73",
    ends={
        Property(name="Variable75", type=imperativeocl_InstantiationExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_InstantiationExp74", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
argument76: BinaryAssociation = BinaryAssociation(
    name="argument76",
    ends={
        Property(name="OclExpression78", type=imperativeocl_InstantiationExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_InstantiationExp77", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keyType79: BinaryAssociation = BinaryAssociation(
    name="keyType79",
    ends={
        Property(name="Type80", type=imperativeocl_DictionaryType, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_DictionaryType", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
part81: BinaryAssociation = BinaryAssociation(
    name="part81",
    ends={
        Property(name="DictLiteralPart", type=imperativeocl_DictLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_DictLiteralExp", type=DictLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key82: BinaryAssociation = BinaryAssociation(
    name="key82",
    ends={
        Property(name="OclExpression83", type=imperativeocl_DictLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_DictLiteralPart", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value84: BinaryAssociation = BinaryAssociation(
    name="value84",
    ends={
        Property(name="OclExpression86", type=imperativeocl_DictLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_DictLiteralPart85", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exception62: BinaryAssociation = BinaryAssociation(
    name="exception62",
    ends={
        Property(name="Type63", type=imperativeocl_RaiseExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_RaiseExp", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
log91: BinaryAssociation = BinaryAssociation(
    name="log91",
    ends={
        Property(name="LogExp", type=imperativeocl_AssertExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_AssertExp", type=LogExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assertion92: BinaryAssociation = BinaryAssociation(
    name="assertion92",
    ends={
        Property(name="OclExpression94", type=imperativeocl_AssertExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_AssertExp93", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition95: BinaryAssociation = BinaryAssociation(
    name="condition95",
    ends={
        Property(name="OclExpression96", type=imperativeocl_ImperativeLoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_ImperativeLoopExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target97: BinaryAssociation = BinaryAssociation(
    name="target97",
    ends={
        Property(name="Variable98", type=imperativeocl_CollectorExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_CollectorExp", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable99: BinaryAssociation = BinaryAssociation(
    name="variable99",
    ends={
        Property(name="Variable100", type=imperativeocl_UnpackExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_UnpackExp", type=Variable, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
elementType101: BinaryAssociation = BinaryAssociation(
    name="elementType101",
    ends={
        Property(name="Type102", type=imperativeocl_AnonymousTupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_AnonymousTupleType", type=Type, multiplicity=Multiplicity(0, 9999))
    }
)
part103: BinaryAssociation = BinaryAssociation(
    name="part103",
    ends={
        Property(name="AnonymousTupleLiteralPart", type=imperativeocl_AnonymousTupleLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_AnonymousTupleLiteralExp", type=AnonymousTupleLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value104: BinaryAssociation = BinaryAssociation(
    name="value104",
    ends={
        Property(name="OclExpression105", type=imperativeocl_AnonymousTupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_AnonymousTupleLiteralPart", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition87: BinaryAssociation = BinaryAssociation(
    name="condition87",
    ends={
        Property(name="OclExpression88", type=imperativeocl_LogExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_LogExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
element89: BinaryAssociation = BinaryAssociation(
    name="element89",
    ends={
        Property(name="Element", type=imperativeocl_LogExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_LogExp90", type=Element, multiplicity=Multiplicity(0, 1))
    }
)
ownedAttribute106: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute106",
    ends={
        Property(name="Property107", type=emof_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="emof_Class", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation108: BinaryAssociation = BinaryAssociation(
    name="ownedOperation108",
    ends={
        Property(name="Operation", type=emof_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="class_", type=Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass109: BinaryAssociation = BinaryAssociation(
    name="superClass109",
    ends={
        Property(name="Class111", type=emof_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="emof_Class110", type=Class_, multiplicity=Multiplicity(0, 9999))
    }
)
tag112: BinaryAssociation = BinaryAssociation(
    name="tag112",
    ends={
        Property(name="Tag", type=emof_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="element", type=Tag, multiplicity=Multiplicity(0, 9999))
    }
)
ownedComment113: BinaryAssociation = BinaryAssociation(
    name="ownedComment113",
    ends={
        Property(name="Comment", type=emof_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="emof_Element", type=Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element114: BinaryAssociation = BinaryAssociation(
    name="element114",
    ends={
        Property(name="Element115", type=emof_Tag, multiplicity=Multiplicity(1, 1)),
        Property(name="tag", type=Element, multiplicity=Multiplicity(0, 9999))
    }
)
transformation116: BinaryAssociation = BinaryAssociation(
    name="transformation116",
    ends={
        Property(name="Transformation", type=emof_Tag, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedTag", type=Transformation, multiplicity=Multiplicity(0, 1))
    }
)
owner117: BinaryAssociation = BinaryAssociation(
    name="owner117",
    ends={
        Property(name="Module", type=emof_Tag, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedTag118", type=Module, multiplicity=Multiplicity(0, 1))
    }
)
ownedLiteral119: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral119",
    ends={
        Property(name="EnumerationLiteral", type=emof_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="enumeration", type=EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedType125: BinaryAssociation = BinaryAssociation(
    name="ownedType125",
    ends={
        Property(name="Type126", type=emof_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedPackage127: BinaryAssociation = BinaryAssociation(
    name="nestedPackage127",
    ends={
        Property(name="Package", type=emof_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="emof_Package", type=Package, multiplicity=Multiplicity(0, 9999))
    }
)
package128: BinaryAssociation = BinaryAssociation(
    name="package128",
    ends={
        Property(name="Package129", type=emof_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedType", type=Package, multiplicity=Multiplicity(1, 1))
    }
)
operation130: BinaryAssociation = BinaryAssociation(
    name="operation130",
    ends={
        Property(name="Operation131", type=emof_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedParameter", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
enumeration132: BinaryAssociation = BinaryAssociation(
    name="enumeration132",
    ends={
        Property(name="Enumeration", type=emof_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedLiteral", type=Enumeration_, multiplicity=Multiplicity(0, 1))
    }
)
class_133: BinaryAssociation = BinaryAssociation(
    name="class_133",
    ends={
        Property(name="Class134", type=emof_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="emof_Property", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
opposite135: BinaryAssociation = BinaryAssociation(
    name="opposite135",
    ends={
        Property(name="Property137", type=emof_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="emof_Property136", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
module138: BinaryAssociation = BinaryAssociation(
    name="module138",
    ends={
        Property(name="Module139", type=emof_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="configProperty", type=Module, multiplicity=Multiplicity(0, 1))
    }
)
class_120: BinaryAssociation = BinaryAssociation(
    name="class_120",
    ends={
        Property(name="Class121", type=emof_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedOperation", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
ownedParameter122: BinaryAssociation = BinaryAssociation(
    name="ownedParameter122",
    ends={
        Property(name="Parameter", type=emof_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
raisedException123: BinaryAssociation = BinaryAssociation(
    name="raisedException123",
    ends={
        Property(name="Type124", type=emof_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="emof_Operation", type=Type, multiplicity=Multiplicity(0, 9999))
    }
)
annotatedElement142: BinaryAssociation = BinaryAssociation(
    name="annotatedElement142",
    ends={
        Property(name="NamedElement", type=emof_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="emof_Comment", type=NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
initSection143: BinaryAssociation = BinaryAssociation(
    name="initSection143",
    ends={
        Property(name="OclExpression144", type=qvtoperational_MappingBody, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_MappingBody", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
endSection145: BinaryAssociation = BinaryAssociation(
    name="endSection145",
    ends={
        Property(name="OclExpression147", type=qvtoperational_MappingBody, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_MappingBody146", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition148: BinaryAssociation = BinaryAssociation(
    name="condition148",
    ends={
        Property(name="OclExpression149", type=qvtoperational_ResolveExp, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_ResolveExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inMapping150: BinaryAssociation = BinaryAssociation(
    name="inMapping150",
    ends={
        Property(name="MappingOperation", type=qvtoperational_ResolveInExp, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_ResolveInExp", type=MappingOperation, multiplicity=Multiplicity(0, 1))
    }
)
intermediateClass151: BinaryAssociation = BinaryAssociation(
    name="intermediateClass151",
    ends={
        Property(name="Class152", type=qvtoperational_OperationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_OperationalTransformation", type=Class_, multiplicity=Multiplicity(0, 9999))
    }
)
type140: BinaryAssociation = BinaryAssociation(
    name="type140",
    ends={
        Property(name="Type141", type=emof_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="emof_TypedElement", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
entry161: BinaryAssociation = BinaryAssociation(
    name="entry161",
    ends={
        Property(name="EntryOperation", type=qvtoperational_OperationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_OperationalTransformation162", type=EntryOperation, multiplicity=Multiplicity(0, 1))
    }
)
relation163: BinaryAssociation = BinaryAssociation(
    name="relation163",
    ends={
        Property(name="Relation", type=qvtoperational_OperationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_OperationalTransformation164", type=Relation, multiplicity=Multiplicity(0, 9999))
    }
)
refinedDomain165: BinaryAssociation = BinaryAssociation(
    name="refinedDomain165",
    ends={
        Property(name="RelationDomain", type=qvtoperational_MappingParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_MappingParameter", type=RelationDomain, multiplicity=Multiplicity(0, 1))
    }
)
extent166: BinaryAssociation = BinaryAssociation(
    name="extent166",
    ends={
        Property(name="ModelParameter168", type=qvtoperational_MappingParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_MappingParameter167", type=ModelParameter, multiplicity=Multiplicity(0, 1))
    }
)
disjunct169: BinaryAssociation = BinaryAssociation(
    name="disjunct169",
    ends={
        Property(name="MappingOperation170", type=qvtoperational_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_MappingOperation", type=MappingOperation, multiplicity=Multiplicity(0, 9999))
    }
)
refinedRelation171: BinaryAssociation = BinaryAssociation(
    name="refinedRelation171",
    ends={
        Property(name="Relation173", type=qvtoperational_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_MappingOperation172", type=Relation, multiplicity=Multiplicity(1, 1))
    }
)
merged174: BinaryAssociation = BinaryAssociation(
    name="merged174",
    ends={
        Property(name="MappingOperation176", type=qvtoperational_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_MappingOperation175", type=MappingOperation, multiplicity=Multiplicity(0, 9999))
    }
)
inherited177: BinaryAssociation = BinaryAssociation(
    name="inherited177",
    ends={
        Property(name="MappingOperation179", type=qvtoperational_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_MappingOperation178", type=MappingOperation, multiplicity=Multiplicity(0, 9999))
    }
)
when180: BinaryAssociation = BinaryAssociation(
    name="when180",
    ends={
        Property(name="OclExpression182", type=qvtoperational_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_MappingOperation181", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
context183: BinaryAssociation = BinaryAssociation(
    name="context183",
    ends={
        Property(name="Class184", type=qvtoperational_ContextualProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_ContextualProperty", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
overridden185: BinaryAssociation = BinaryAssociation(
    name="overridden185",
    ends={
        Property(name="Property187", type=qvtoperational_ContextualProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_ContextualProperty186", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
refined153: BinaryAssociation = BinaryAssociation(
    name="refined153",
    ends={
        Property(name="Transformation155", type=qvtoperational_OperationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_OperationalTransformation154", type=Transformation, multiplicity=Multiplicity(0, 1))
    }
)
intermediateProperty156: BinaryAssociation = BinaryAssociation(
    name="intermediateProperty156",
    ends={
        Property(name="Property158", type=qvtoperational_OperationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_OperationalTransformation157", type=Property_, multiplicity=Multiplicity(0, 9999))
    }
)
modelParameter159: BinaryAssociation = BinaryAssociation(
    name="modelParameter159",
    ends={
        Property(name="ModelParameter", type=qvtoperational_OperationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_OperationalTransformation160", type=ModelParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
result189: BinaryAssociation = BinaryAssociation(
    name="result189",
    ends={
        Property(name="VarParameter190", type=qvtoperational_ImperativeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="resOwner", type=VarParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
overridden191: BinaryAssociation = BinaryAssociation(
    name="overridden191",
    ends={
        Property(name="ImperativeOperation", type=qvtoperational_ImperativeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_ImperativeOperation", type=ImperativeOperation, multiplicity=Multiplicity(0, 1))
    }
)
body192: BinaryAssociation = BinaryAssociation(
    name="body192",
    ends={
        Property(name="OperationBody", type=qvtoperational_ImperativeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation193", type=OperationBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
metamodel194: BinaryAssociation = BinaryAssociation(
    name="metamodel194",
    ends={
        Property(name="Package195", type=qvtoperational_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_ModelType", type=Package, multiplicity=Multiplicity(0, 9999))
    }
)
additionalCondition196: BinaryAssociation = BinaryAssociation(
    name="additionalCondition196",
    ends={
        Property(name="OclExpression198", type=qvtoperational_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_ModelType197", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedTag199: BinaryAssociation = BinaryAssociation(
    name="ownedTag199",
    ends={
        Property(name="Tag200", type=qvtoperational_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=Tag, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
configProperty201: BinaryAssociation = BinaryAssociation(
    name="configProperty201",
    ends={
        Property(name="Property202", type=qvtoperational_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="module", type=Property_, multiplicity=Multiplicity(0, 9999))
    }
)
moduleImport203: BinaryAssociation = BinaryAssociation(
    name="moduleImport203",
    ends={
        Property(name="ModuleImport", type=qvtoperational_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="module204", type=ModuleImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usedModelType205: BinaryAssociation = BinaryAssociation(
    name="usedModelType205",
    ends={
        Property(name="ModelType", type=qvtoperational_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_Module", type=ModelType, multiplicity=Multiplicity(0, 9999))
    }
)
context188: BinaryAssociation = BinaryAssociation(
    name="context188",
    ends={
        Property(name="VarParameter", type=qvtoperational_ImperativeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="ctxOwner", type=VarParameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
module208: BinaryAssociation = BinaryAssociation(
    name="module208",
    ends={
        Property(name="Module209", type=qvtoperational_ModuleImport, multiplicity=Multiplicity(1, 1)),
        Property(name="moduleImport", type=Module, multiplicity=Multiplicity(0, 1))
    }
)
importedModule210: BinaryAssociation = BinaryAssociation(
    name="importedModule210",
    ends={
        Property(name="Module212", type=qvtoperational_ModuleImport, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_ModuleImport211", type=Module, multiplicity=Multiplicity(1, 1))
    }
)
ctxOwner213: BinaryAssociation = BinaryAssociation(
    name="ctxOwner213",
    ends={
        Property(name="ImperativeOperation214", type=qvtoperational_VarParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="context", type=ImperativeOperation, multiplicity=Multiplicity(0, 1))
    }
)
resOwner215: BinaryAssociation = BinaryAssociation(
    name="resOwner215",
    ends={
        Property(name="ImperativeOperation216", type=qvtoperational_VarParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="result", type=ImperativeOperation, multiplicity=Multiplicity(0, 1))
    }
)
operation217: BinaryAssociation = BinaryAssociation(
    name="operation217",
    ends={
        Property(name="ImperativeOperation218", type=qvtoperational_OperationBody, multiplicity=Multiplicity(1, 1)),
        Property(name="body", type=ImperativeOperation, multiplicity=Multiplicity(0, 1))
    }
)
content219: BinaryAssociation = BinaryAssociation(
    name="content219",
    ends={
        Property(name="OclExpression220", type=qvtoperational_OperationBody, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_OperationBody", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredObject221: BinaryAssociation = BinaryAssociation(
    name="referredObject221",
    ends={
        Property(name="Variable222", type=qvtoperational_ObjectExp, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_ObjectExp", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
body223: BinaryAssociation = BinaryAssociation(
    name="body223",
    ends={
        Property(name="ConstructorBody", type=qvtoperational_ObjectExp, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_ObjectExp224", type=ConstructorBody, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
guardPattern225: BinaryAssociation = BinaryAssociation(
    name="guardPattern225",
    ends={
        Property(name="GuardPattern", type=qvtcore_Area, multiplicity=Multiplicity(1, 1)),
        Property(name="area", type=GuardPattern, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
binding206: BinaryAssociation = BinaryAssociation(
    name="binding206",
    ends={
        Property(name="ModelType207", type=qvtoperational_ModuleImport, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_ModuleImport", type=ModelType, multiplicity=Multiplicity(0, 9999))
    }
)
value232: BinaryAssociation = BinaryAssociation(
    name="value232",
    ends={
        Property(name="OclExpression234", type=qvtcore_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcore_Assignment233", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
targetProperty235: BinaryAssociation = BinaryAssociation(
    name="targetProperty235",
    ends={
        Property(name="Property237", type=qvtcore_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcore_Assignment236", type=Property_, multiplicity=Multiplicity(1, 1))
    }
)
area238: BinaryAssociation = BinaryAssociation(
    name="area238",
    ends={
        Property(name="Area", type=qvtcore_BottomPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="bottomPattern", type=Area, multiplicity=Multiplicity(1, 1))
    }
)
assignment239: BinaryAssociation = BinaryAssociation(
    name="assignment239",
    ends={
        Property(name="Assignment", type=qvtcore_BottomPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="bottomPattern240", type=Assignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
realizedVariable241: BinaryAssociation = BinaryAssociation(
    name="realizedVariable241",
    ends={
        Property(name="RealizedVariable", type=qvtcore_BottomPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcore_BottomPattern", type=RealizedVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enforcementOperation242: BinaryAssociation = BinaryAssociation(
    name="enforcementOperation242",
    ends={
        Property(name="EnforcementOperation", type=qvtcore_BottomPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="bottomPattern243", type=EnforcementOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
area244: BinaryAssociation = BinaryAssociation(
    name="area244",
    ends={
        Property(name="Area245", type=qvtcore_GuardPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="guardPattern", type=Area, multiplicity=Multiplicity(1, 1))
    }
)
specification246: BinaryAssociation = BinaryAssociation(
    name="specification246",
    ends={
        Property(name="Mapping", type=qvtcore_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcore_Mapping", type=Mapping, multiplicity=Multiplicity(0, 9999))
    }
)
local247: BinaryAssociation = BinaryAssociation(
    name="local247",
    ends={
        Property(name="Mapping249", type=qvtcore_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="context248", type=Mapping, multiplicity=Multiplicity(0, 9999))
    }
)
context250: BinaryAssociation = BinaryAssociation(
    name="context250",
    ends={
        Property(name="Mapping251", type=qvtcore_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="local", type=Mapping, multiplicity=Multiplicity(0, 1))
    }
)
bottomPattern226: BinaryAssociation = BinaryAssociation(
    name="bottomPattern226",
    ends={
        Property(name="BottomPattern", type=qvtcore_Area, multiplicity=Multiplicity(1, 1)),
        Property(name="area227", type=BottomPattern, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bottomPattern228: BinaryAssociation = BinaryAssociation(
    name="bottomPattern228",
    ends={
        Property(name="BottomPattern229", type=qvtcore_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="assignment", type=BottomPattern, multiplicity=Multiplicity(1, 1))
    }
)
slotExpression230: BinaryAssociation = BinaryAssociation(
    name="slotExpression230",
    ends={
        Property(name="OclExpression231", type=qvtcore_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcore_Assignment", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rule255: BinaryAssociation = BinaryAssociation(
    name="rule255",
    ends={
        Property(name="Rule", type=qvtbase_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="domain", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
typedModel256: BinaryAssociation = BinaryAssociation(
    name="typedModel256",
    ends={
        Property(name="TypedModel", type=qvtbase_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtbase_Domain", type=TypedModel, multiplicity=Multiplicity(1, 1))
    }
)
ownedTag257: BinaryAssociation = BinaryAssociation(
    name="ownedTag257",
    ends={
        Property(name="Tag258", type=qvtbase_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation", type=Tag, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modelParameter259: BinaryAssociation = BinaryAssociation(
    name="modelParameter259",
    ends={
        Property(name="TypedModel261", type=qvtbase_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation260", type=TypedModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rule262: BinaryAssociation = BinaryAssociation(
    name="rule262",
    ends={
        Property(name="Rule264", type=qvtbase_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation263", type=Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extends265: BinaryAssociation = BinaryAssociation(
    name="extends265",
    ends={
        Property(name="Transformation266", type=qvtbase_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtbase_Transformation", type=Transformation, multiplicity=Multiplicity(0, 1))
    }
)
transformation267: BinaryAssociation = BinaryAssociation(
    name="transformation267",
    ends={
        Property(name="Transformation268", type=qvtbase_TypedModel, multiplicity=Multiplicity(1, 1)),
        Property(name="modelParameter", type=Transformation, multiplicity=Multiplicity(1, 1))
    }
)
usedPackage269: BinaryAssociation = BinaryAssociation(
    name="usedPackage269",
    ends={
        Property(name="Package270", type=qvtbase_TypedModel, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtbase_TypedModel", type=Package, multiplicity=Multiplicity(1, 9999))
    }
)
dependsOn271: BinaryAssociation = BinaryAssociation(
    name="dependsOn271",
    ends={
        Property(name="TypedModel273", type=qvtbase_TypedModel, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtbase_TypedModel272", type=TypedModel, multiplicity=Multiplicity(0, 9999))
    }
)
domain274: BinaryAssociation = BinaryAssociation(
    name="domain274",
    ends={
        Property(name="Domain", type=qvtbase_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="rule", type=Domain, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bottomPattern252: BinaryAssociation = BinaryAssociation(
    name="bottomPattern252",
    ends={
        Property(name="BottomPattern253", type=qvtcore_EnforcementOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="enforcementOperation", type=BottomPattern, multiplicity=Multiplicity(0, 1))
    }
)
operationCallExp254: BinaryAssociation = BinaryAssociation(
    name="operationCallExp254",
    ends={
        Property(name="OperationCallExp", type=qvtcore_EnforcementOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcore_EnforcementOperation", type=OperationCallExp, multiplicity=Multiplicity(1, 1))
    }
)
predicate280: BinaryAssociation = BinaryAssociation(
    name="predicate280",
    ends={
        Property(name="Predicate", type=qvtbase_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="pattern", type=Predicate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bindsTo281: BinaryAssociation = BinaryAssociation(
    name="bindsTo281",
    ends={
        Property(name="Variable282", type=qvtbase_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtbase_Pattern", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
whenOwner283: BinaryAssociation = BinaryAssociation(
    name="whenOwner283",
    ends={
        Property(name="Relation284", type=qvtbase_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="where", type=Relation, multiplicity=Multiplicity(0, 1))
    }
)
whereOwner285: BinaryAssociation = BinaryAssociation(
    name="whereOwner285",
    ends={
        Property(name="Relation286", type=qvtbase_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="when", type=Relation, multiplicity=Multiplicity(0, 1))
    }
)
conditionExpression287: BinaryAssociation = BinaryAssociation(
    name="conditionExpression287",
    ends={
        Property(name="OclExpression288", type=qvtbase_Predicate, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtbase_Predicate", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
pattern289: BinaryAssociation = BinaryAssociation(
    name="pattern289",
    ends={
        Property(name="Pattern", type=qvtbase_Predicate, multiplicity=Multiplicity(1, 1)),
        Property(name="predicate", type=Pattern, multiplicity=Multiplicity(1, 1))
    }
)
queryExpression290: BinaryAssociation = BinaryAssociation(
    name="queryExpression290",
    ends={
        Property(name="OclExpression291", type=qvtbase_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtbase_Function", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedKey292: BinaryAssociation = BinaryAssociation(
    name="ownedKey292",
    ends={
        Property(name="Key", type=qvtrelation_RelationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation293", type=Key, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable294: BinaryAssociation = BinaryAssociation(
    name="variable294",
    ends={
        Property(name="Variable295", type=qvtrelation_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_Relation", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transformation275: BinaryAssociation = BinaryAssociation(
    name="transformation275",
    ends={
        Property(name="Transformation277", type=qvtbase_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="rule276", type=Transformation, multiplicity=Multiplicity(1, 1))
    }
)
overrides278: BinaryAssociation = BinaryAssociation(
    name="overrides278",
    ends={
        Property(name="Rule279", type=qvtbase_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtbase_Rule", type=Rule, multiplicity=Multiplicity(0, 1))
    }
)
when299: BinaryAssociation = BinaryAssociation(
    name="when299",
    ends={
        Property(name="Pattern300", type=qvtrelation_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="whereOwner", type=Pattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pattern301: BinaryAssociation = BinaryAssociation(
    name="pattern301",
    ends={
        Property(name="DomainPattern", type=qvtrelation_RelationDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_RelationDomain", type=DomainPattern, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rootVariable302: BinaryAssociation = BinaryAssociation(
    name="rootVariable302",
    ends={
        Property(name="Variable304", type=qvtrelation_RelationDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_RelationDomain303", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
templateExpression305: BinaryAssociation = BinaryAssociation(
    name="templateExpression305",
    ends={
        Property(name="TemplateExp", type=qvtrelation_DomainPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_DomainPattern", type=TemplateExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
relation306: BinaryAssociation = BinaryAssociation(
    name="relation306",
    ends={
        Property(name="Relation307", type=qvtrelation_RelationImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="operationalImpl", type=Relation, multiplicity=Multiplicity(0, 1))
    }
)
impl308: BinaryAssociation = BinaryAssociation(
    name="impl308",
    ends={
        Property(name="Operation309", type=qvtrelation_RelationImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_RelationImplementation", type=Operation, multiplicity=Multiplicity(1, 1))
    }
)
inDirectionOf310: BinaryAssociation = BinaryAssociation(
    name="inDirectionOf310",
    ends={
        Property(name="TypedModel312", type=qvtrelation_RelationImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_RelationImplementation311", type=TypedModel, multiplicity=Multiplicity(1, 1))
    }
)
identifies313: BinaryAssociation = BinaryAssociation(
    name="identifies313",
    ends={
        Property(name="Class314", type=qvtrelation_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_Key", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
part315: BinaryAssociation = BinaryAssociation(
    name="part315",
    ends={
        Property(name="Property317", type=qvtrelation_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_Key316", type=Property_, multiplicity=Multiplicity(1, 9999))
    }
)
transformation318: BinaryAssociation = BinaryAssociation(
    name="transformation318",
    ends={
        Property(name="RelationalTransformation", type=qvtrelation_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedKey", type=RelationalTransformation, multiplicity=Multiplicity(0, 1))
    }
)
operationalImpl296: BinaryAssociation = BinaryAssociation(
    name="operationalImpl296",
    ends={
        Property(name="RelationImplementation", type=qvtrelation_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="relation", type=RelationImplementation, multiplicity=Multiplicity(0, 9999))
    }
)
where297: BinaryAssociation = BinaryAssociation(
    name="where297",
    ends={
        Property(name="Pattern298", type=qvtrelation_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="whenOwner", type=Pattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tryBodyOwner321: BinaryAssociation = BinaryAssociation(
    name="tryBodyOwner321",
    ends={
        Property(name="TryExp", type=essentialocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="tryBody", type=TryExp, multiplicity=Multiplicity(0, 1))
    }
)
condition322: BinaryAssociation = BinaryAssociation(
    name="condition322",
    ends={
        Property(name="OclExpression323", type=essentialocl_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_IfExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression324: BinaryAssociation = BinaryAssociation(
    name="thenExpression324",
    ends={
        Property(name="OclExpression326", type=essentialocl_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_IfExp325", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression327: BinaryAssociation = BinaryAssociation(
    name="elseExpression327",
    ends={
        Property(name="OclExpression329", type=essentialocl_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_IfExp328", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
in_330: BinaryAssociation = BinaryAssociation(
    name="in_330",
    ends={
        Property(name="OclExpression331", type=essentialocl_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_LetExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source319: BinaryAssociation = BinaryAssociation(
    name="source319",
    ends={
        Property(name="OclExpression320", type=essentialocl_CallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_CallExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initExpression334: BinaryAssociation = BinaryAssociation(
    name="initExpression334",
    ends={
        Property(name="OclExpression335", type=essentialocl_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_Variable", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
LetExp336: BinaryAssociation = BinaryAssociation(
    name="LetExp336",
    ends={
        Property(name="LetExp337", type=essentialocl_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="variable", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
computeOwner338: BinaryAssociation = BinaryAssociation(
    name="computeOwner338",
    ends={
        Property(name="ComputeExp", type=essentialocl_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="returnedElement", type=ComputeExp, multiplicity=Multiplicity(0, 1))
    }
)
bindParameter339: BinaryAssociation = BinaryAssociation(
    name="bindParameter339",
    ends={
        Property(name="Parameter341", type=essentialocl_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_Variable340", type=Parameter_, multiplicity=Multiplicity(0, 1))
    }
)
referredProperty342: BinaryAssociation = BinaryAssociation(
    name="referredProperty342",
    ends={
        Property(name="Property343", type=essentialocl_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_PropertyCallExp", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
referredVariable344: BinaryAssociation = BinaryAssociation(
    name="referredVariable344",
    ends={
        Property(name="Variable345", type=essentialocl_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_VariableExp", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
referredType346: BinaryAssociation = BinaryAssociation(
    name="referredType346",
    ends={
        Property(name="Type347", type=essentialocl_TypeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_TypeExp", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
body348: BinaryAssociation = BinaryAssociation(
    name="body348",
    ends={
        Property(name="OclExpression349", type=essentialocl_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_LoopExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable332: BinaryAssociation = BinaryAssociation(
    name="variable332",
    ends={
        Property(name="Variable333", type=essentialocl_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="LetExp", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterator350: BinaryAssociation = BinaryAssociation(
    name="iterator350",
    ends={
        Property(name="Variable352", type=essentialocl_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_LoopExp351", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument353: BinaryAssociation = BinaryAssociation(
    name="argument353",
    ends={
        Property(name="OclExpression354", type=essentialocl_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_OperationCallExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredOperation355: BinaryAssociation = BinaryAssociation(
    name="referredOperation355",
    ends={
        Property(name="Operation357", type=essentialocl_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_OperationCallExp356", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
result358: BinaryAssociation = BinaryAssociation(
    name="result358",
    ends={
        Property(name="Variable359", type=essentialocl_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_IterateExp", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
part360: BinaryAssociation = BinaryAssociation(
    name="part360",
    ends={
        Property(name="CollectionLiteralPart", type=essentialocl_CollectionLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="CollectionLiteralExp", type=CollectionLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
CollectionLiteralExp361: BinaryAssociation = BinaryAssociation(
    name="CollectionLiteralExp361",
    ends={
        Property(name="CollectionLiteralExp363", type=essentialocl_CollectionLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="part362", type=CollectionLiteralExp, multiplicity=Multiplicity(1, 1))
    }
)
item364: BinaryAssociation = BinaryAssociation(
    name="item364",
    ends={
        Property(name="OclExpression365", type=essentialocl_CollectionItem, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_CollectionItem", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
last368: BinaryAssociation = BinaryAssociation(
    name="last368",
    ends={
        Property(name="OclExpression370", type=essentialocl_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_CollectionRange369", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
part371: BinaryAssociation = BinaryAssociation(
    name="part371",
    ends={
        Property(name="TupleLiteralPart", type=essentialocl_TupleLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="TupleLiteralExp", type=TupleLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyExpression372: BinaryAssociation = BinaryAssociation(
    name="bodyExpression372",
    ends={
        Property(name="OclExpression373", type=essentialocl_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_ExpressionInOcl", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context374: BinaryAssociation = BinaryAssociation(
    name="context374",
    ends={
        Property(name="Variable376", type=essentialocl_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_ExpressionInOcl375", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resultVariable377: BinaryAssociation = BinaryAssociation(
    name="resultVariable377",
    ends={
        Property(name="Variable379", type=essentialocl_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_ExpressionInOcl378", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterVariable380: BinaryAssociation = BinaryAssociation(
    name="parameterVariable380",
    ends={
        Property(name="Variable382", type=essentialocl_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_ExpressionInOcl381", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TupleLiteralExp383: BinaryAssociation = BinaryAssociation(
    name="TupleLiteralExp383",
    ends={
        Property(name="TupleLiteralExp385", type=essentialocl_TupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="part384", type=TupleLiteralExp, multiplicity=Multiplicity(0, 1))
    }
)
attribute386: BinaryAssociation = BinaryAssociation(
    name="attribute386",
    ends={
        Property(name="Property387", type=essentialocl_TupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_TupleLiteralPart", type=Property_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elementType388: BinaryAssociation = BinaryAssociation(
    name="elementType388",
    ends={
        Property(name="Type389", type=essentialocl_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_CollectionType", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
referredEnumLiteral390: BinaryAssociation = BinaryAssociation(
    name="referredEnumLiteral390",
    ends={
        Property(name="EnumerationLiteral391", type=essentialocl_EnumLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_EnumLiteralExp", type=EnumerationLiteral, multiplicity=Multiplicity(0, 1))
    }
)
first366: BinaryAssociation = BinaryAssociation(
    name="first366",
    ends={
        Property(name="OclExpression367", type=essentialocl_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_CollectionRange", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_qvttemplate_TemplateExp_LiteralExp = Generalization(general=LiteralExp, specific=qvttemplate_TemplateExp)
gen_qvttemplate_ObjectTemplateExp_TemplateExp = Generalization(general=TemplateExp, specific=qvttemplate_ObjectTemplateExp)
gen_qvttemplate_CollectionTemplateExp_TemplateExp = Generalization(general=TemplateExp, specific=qvttemplate_CollectionTemplateExp)
gen_qvttemplate_PropertyTemplateItem_Element = Generalization(general=Element, specific=qvttemplate_PropertyTemplateItem)
gen_imperativeocl_ImperativeIterateExp_ImperativeLoopExp = Generalization(general=ImperativeLoopExp, specific=imperativeocl_ImperativeIterateExp)
gen_imperativeocl_AssignExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_AssignExp)
gen_imperativeocl_BlockExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_BlockExp)
gen_imperativeocl_SwitchExp_CallExp = Generalization(general=CallExp, specific=imperativeocl_SwitchExp)
gen_imperativeocl_SwitchExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_SwitchExp)
gen_imperativeocl_VariableInitExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_VariableInitExp)
gen_imperativeocl_ComputeExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_ComputeExp)
gen_imperativeocl_AltExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_AltExp)
gen_imperativeocl_UnlinkExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_UnlinkExp)
gen_imperativeocl_ReturnExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_ReturnExp)
gen_imperativeocl_BreakExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_BreakExp)
gen_imperativeocl_TryExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_TryExp)
gen_imperativeocl_RaiseExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_RaiseExp)
gen_imperativeocl_WhileExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_WhileExp)
gen_imperativeocl_Typedef_Class = Generalization(general=Class_, specific=imperativeocl_Typedef)
gen_imperativeocl_InstantiationExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_InstantiationExp)
gen_imperativeocl_DictionaryType_CollectionType = Generalization(general=CollectionType, specific=imperativeocl_DictionaryType)
gen_imperativeocl_DictLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=imperativeocl_DictLiteralExp)
gen_imperativeocl_DictLiteralPart_Element = Generalization(general=Element, specific=imperativeocl_DictLiteralPart)
gen_imperativeocl_TemplateParameterType_Type = Generalization(general=Type, specific=imperativeocl_TemplateParameterType)
gen_imperativeocl_LogExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_LogExp)
gen_imperativeocl_ContinueExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_ContinueExp)
gen_imperativeocl_ForExp_ImperativeLoopExp = Generalization(general=ImperativeLoopExp, specific=imperativeocl_ForExp)
gen_imperativeocl_TupleExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_TupleExp)
gen_imperativeocl_AssertExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_AssertExp)
gen_imperativeocl_ImperativeLoopExp_LoopExp = Generalization(general=LoopExp, specific=imperativeocl_ImperativeLoopExp)
gen_imperativeocl_ImperativeLoopExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_ImperativeLoopExp)
gen_imperativeocl_CollectorExp_ImperativeLoopExp = Generalization(general=ImperativeLoopExp, specific=imperativeocl_CollectorExp)
gen_imperativeocl_ImperativeExpression_OclExpression = Generalization(general=OclExpression, specific=imperativeocl_ImperativeExpression)
gen_imperativeocl_UnpackExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_UnpackExp)
gen_imperativeocl_AnonymousTupleType_Class = Generalization(general=Class_, specific=imperativeocl_AnonymousTupleType)
gen_imperativeocl_AnonymousTupleLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=imperativeocl_AnonymousTupleLiteralExp)
gen_imperativeocl_AnonymousTupleLiteralPart_Element = Generalization(general=Element, specific=imperativeocl_AnonymousTupleLiteralPart)
gen_emof_DataType_Type = Generalization(general=Type, specific=emof_DataType)
gen_emof_Element_Object = Generalization(general=Object, specific=emof_Element)
gen_emof_Tag_Element = Generalization(general=Element, specific=emof_Tag)
gen_emof_Enumeration_DataType = Generalization(general=DataType, specific=emof_Enumeration)
gen_emof_NamedElement_Element = Generalization(general=Element, specific=emof_NamedElement)
gen_emof_Extent_Object = Generalization(general=Object, specific=emof_Extent)
gen_emof_Operation_MultiplicityElement = Generalization(general=MultiplicityElement, specific=emof_Operation)
gen_imperativeocl_ListType_CollectionType = Generalization(general=CollectionType, specific=imperativeocl_ListType)
gen_emof_Class_Type = Generalization(general=Type, specific=emof_Class)
gen_emof_Package_NamedElement = Generalization(general=NamedElement, specific=emof_Package)
gen_emof_Type_NamedElement = Generalization(general=NamedElement, specific=emof_Type)
gen_emof_Parameter_MultiplicityElement = Generalization(general=MultiplicityElement, specific=emof_Parameter)
gen_emof_Parameter_TypedElement = Generalization(general=TypedElement, specific=emof_Parameter)
gen_emof_EnumerationLiteral_NamedElement = Generalization(general=NamedElement, specific=emof_EnumerationLiteral)
gen_emof_Property_MultiplicityElement = Generalization(general=MultiplicityElement, specific=emof_Property)
gen_emof_Property_TypedElement = Generalization(general=TypedElement, specific=emof_Property)
gen_emof_Operation_TypedElement = Generalization(general=TypedElement, specific=emof_Operation)
gen_emof_PrimitiveType_DataType = Generalization(general=DataType, specific=emof_PrimitiveType)
gen_emof_URIExtent_Extent = Generalization(general=Extent, specific=emof_URIExtent)
gen_emof_Comment_Element = Generalization(general=Element, specific=emof_Comment)
gen_qvtoperational_MappingBody_OperationBody = Generalization(general=OperationBody, specific=qvtoperational_MappingBody)
gen_qvtoperational_Helper_ImperativeOperation = Generalization(general=ImperativeOperation, specific=qvtoperational_Helper)
gen_qvtoperational_ResolveExp_CallExp = Generalization(general=CallExp, specific=qvtoperational_ResolveExp)
gen_qvtoperational_ResolveInExp_ResolveExp = Generalization(general=ResolveExp, specific=qvtoperational_ResolveInExp)
gen_qvtoperational_OperationalTransformation_Module = Generalization(general=Module, specific=qvtoperational_OperationalTransformation)
gen_emof_TypedElement_NamedElement = Generalization(general=NamedElement, specific=emof_TypedElement)
gen_qvtoperational_MappingParameter_VarParameter = Generalization(general=VarParameter, specific=qvtoperational_MappingParameter)
gen_qvtoperational_MappingOperation_ImperativeOperation = Generalization(general=ImperativeOperation, specific=qvtoperational_MappingOperation)
gen_qvtoperational_MappingOperation_Operation = Generalization(general=Operation, specific=qvtoperational_MappingOperation)
gen_qvtoperational_MappingOperation_NamedElement = Generalization(general=NamedElement, specific=qvtoperational_MappingOperation)
gen_qvtoperational_MappingCallExp_ImperativeCallExp = Generalization(general=ImperativeCallExp, specific=qvtoperational_MappingCallExp)
gen_qvtoperational_Constructor_ImperativeOperation = Generalization(general=ImperativeOperation, specific=qvtoperational_Constructor)
gen_qvtoperational_ContextualProperty_Property = Generalization(general=Property_, specific=qvtoperational_ContextualProperty)
gen_qvtoperational_EntryOperation_ImperativeOperation = Generalization(general=ImperativeOperation, specific=qvtoperational_EntryOperation)
gen_qvtoperational_Library_Module = Generalization(general=Module, specific=qvtoperational_Library)
gen_qvtoperational_ModelParameter_VarParameter = Generalization(general=VarParameter, specific=qvtoperational_ModelParameter)
gen_qvtoperational_ModelType_Class = Generalization(general=Class_, specific=qvtoperational_ModelType)
gen_qvtoperational_ModelType_URIExtent = Generalization(general=URIExtent, specific=qvtoperational_ModelType)
gen_qvtoperational_Module_Class = Generalization(general=Class_, specific=qvtoperational_Module)
gen_qvtoperational_Module_Package = Generalization(general=Package, specific=qvtoperational_Module)
gen_qvtoperational_ImperativeCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=qvtoperational_ImperativeCallExp)
gen_qvtoperational_ImperativeOperation_Operation = Generalization(general=Operation, specific=qvtoperational_ImperativeOperation)
gen_qvtoperational_VarParameter_Parameter = Generalization(general=Parameter_, specific=qvtoperational_VarParameter)
gen_qvtoperational_VarParameter_Variable = Generalization(general=Variable, specific=qvtoperational_VarParameter)
gen_qvtoperational_OperationBody_Element = Generalization(general=Element, specific=qvtoperational_OperationBody)
gen_qvtoperational_ConstructorBody_OperationBody = Generalization(general=OperationBody, specific=qvtoperational_ConstructorBody)
gen_qvtoperational_ObjectExp_InstantiationExp = Generalization(general=InstantiationExp, specific=qvtoperational_ObjectExp)
gen_qvtoperational_ModuleImport_Element = Generalization(general=Element, specific=qvtoperational_ModuleImport)
gen_qvtcore_BottomPattern_CorePattern = Generalization(general=CorePattern, specific=qvtcore_BottomPattern)
gen_qvtcore_GuardPattern_CorePattern = Generalization(general=CorePattern, specific=qvtcore_GuardPattern)
gen_qvtcore_Mapping_Rule = Generalization(general=Rule, specific=qvtcore_Mapping)
gen_qvtcore_Mapping_Area = Generalization(general=Area, specific=qvtcore_Mapping)
gen_qvtcore_RealizedVariable_Variable = Generalization(general=Variable, specific=qvtcore_RealizedVariable)
gen_qvtcore_CoreDomain_Domain = Generalization(general=Domain, specific=qvtcore_CoreDomain)
gen_qvtcore_CoreDomain_Area = Generalization(general=Area, specific=qvtcore_CoreDomain)
gen_qvtcore_CorePattern_Pattern = Generalization(general=Pattern, specific=qvtcore_CorePattern)
gen_qvtbase_Domain_NamedElement = Generalization(general=NamedElement, specific=qvtbase_Domain)
gen_qvtbase_Transformation_Class = Generalization(general=Class_, specific=qvtbase_Transformation)
gen_qvtbase_Transformation_Package = Generalization(general=Package, specific=qvtbase_Transformation)
gen_qvtbase_TypedModel_NamedElement = Generalization(general=NamedElement, specific=qvtbase_TypedModel)
gen_qvtbase_Rule_NamedElement = Generalization(general=NamedElement, specific=qvtbase_Rule)
gen_qvtbase_Predicate_Element = Generalization(general=Element, specific=qvtbase_Predicate)
gen_qvtbase_Function_Operation = Generalization(general=Operation, specific=qvtbase_Function)
gen_qvtbase_FunctionParameter_Parameter = Generalization(general=Parameter_, specific=qvtbase_FunctionParameter)
gen_qvtbase_FunctionParameter_Variable = Generalization(general=Variable, specific=qvtbase_FunctionParameter)
gen_qvtrelation_RelationalTransformation_Transformation = Generalization(general=Transformation, specific=qvtrelation_RelationalTransformation)
gen_qvtrelation_Relation_Rule = Generalization(general=Rule, specific=qvtrelation_Relation)
gen_qvtbase_Pattern_Element = Generalization(general=Element, specific=qvtbase_Pattern)
gen_qvtrelation_RelationDomain_Domain = Generalization(general=Domain, specific=qvtrelation_RelationDomain)
gen_qvtrelation_DomainPattern_Pattern = Generalization(general=Pattern, specific=qvtrelation_DomainPattern)
gen_qvtrelation_RelationImplementation_Element = Generalization(general=Element, specific=qvtrelation_RelationImplementation)
gen_qvtrelation_Key_Element = Generalization(general=Element, specific=qvtrelation_Key)
gen_essentialocl_OclExpression_TypedElement = Generalization(general=TypedElement, specific=essentialocl_OclExpression)
gen_essentialocl_UnlimitedNaturalExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=essentialocl_UnlimitedNaturalExp)
gen_essentialocl_IfExp_OclExpression = Generalization(general=OclExpression, specific=essentialocl_IfExp)
gen_essentialocl_LetExp_OclExpression = Generalization(general=OclExpression, specific=essentialocl_LetExp)
gen_essentialocl_BooleanLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=essentialocl_BooleanLiteralExp)
gen_essentialocl_CallExp_OclExpression = Generalization(general=OclExpression, specific=essentialocl_CallExp)
gen_essentialocl_PropertyCallExp_FeaturePropertyCall = Generalization(general=FeaturePropertyCall, specific=essentialocl_PropertyCallExp)
gen_essentialocl_VariableExp_OclExpression = Generalization(general=OclExpression, specific=essentialocl_VariableExp)
gen_essentialocl_TypeExp_OclExpression = Generalization(general=OclExpression, specific=essentialocl_TypeExp)
gen_essentialocl_LoopExp_CallExp = Generalization(general=CallExp, specific=essentialocl_LoopExp)
gen_essentialocl_LoopExp_OclExpression = Generalization(general=OclExpression, specific=essentialocl_LoopExp)
gen_essentialocl_Variable_TypedElement = Generalization(general=TypedElement, specific=essentialocl_Variable)
gen_essentialocl_IntegerLiteralExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=essentialocl_IntegerLiteralExp)
gen_essentialocl_OperationCallExp_FeaturePropertyCall = Generalization(general=FeaturePropertyCall, specific=essentialocl_OperationCallExp)
gen_essentialocl_RealLiteralExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=essentialocl_RealLiteralExp)
gen_essentialocl_LiteralExp_OclExpression = Generalization(general=OclExpression, specific=essentialocl_LiteralExp)
gen_essentialocl_IterateExp_LoopExp = Generalization(general=LoopExp, specific=essentialocl_IterateExp)
gen_essentialocl_PrimitiveLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=essentialocl_PrimitiveLiteralExp)
gen_essentialocl_NumericLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=essentialocl_NumericLiteralExp)
gen_essentialocl_CollectionLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=essentialocl_CollectionLiteralExp)
gen_essentialocl_CollectionLiteralPart_TypedElement = Generalization(general=TypedElement, specific=essentialocl_CollectionLiteralPart)
gen_essentialocl_CollectionItem_CollectionLiteralPart = Generalization(general=CollectionLiteralPart, specific=essentialocl_CollectionItem)
gen_essentialocl_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=essentialocl_IteratorExp)
gen_essentialocl_TupleLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=essentialocl_TupleLiteralExp)
gen_essentialocl_StringLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=essentialocl_StringLiteralExp)
gen_essentialocl_NullLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=essentialocl_NullLiteralExp)
gen_essentialocl_ExpressionInOcl_OpaqueExpression = Generalization(general=OpaqueExpression, specific=essentialocl_ExpressionInOcl)
gen_essentialocl_InvalidLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=essentialocl_InvalidLiteralExp)
gen_essentialocl_FeaturePropertyCall_CallExp = Generalization(general=CallExp, specific=essentialocl_FeaturePropertyCall)
gen_essentialocl_TupleLiteralPart_TypedElement = Generalization(general=TypedElement, specific=essentialocl_TupleLiteralPart)
gen_essentialocl_BagType_CollectionType = Generalization(general=CollectionType, specific=essentialocl_BagType)
gen_essentialocl_CollectionType_DataType = Generalization(general=DataType, specific=essentialocl_CollectionType)
gen_essentialocl_EnumLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=essentialocl_EnumLiteralExp)
gen_essentialocl_InvalidType_Type = Generalization(general=Type, specific=essentialocl_InvalidType)
gen_essentialocl_CollectionRange_CollectionLiteralPart = Generalization(general=CollectionLiteralPart, specific=essentialocl_CollectionRange)
gen_essentialocl_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=essentialocl_OrderedSetType)
gen_essentialocl_SequenceType_CollectionType = Generalization(general=CollectionType, specific=essentialocl_SequenceType)
gen_essentialocl_VoidType_Type = Generalization(general=Type, specific=essentialocl_VoidType)
gen_essentialocl_AnyType_Class = Generalization(general=Class_, specific=essentialocl_AnyType)
gen_essentialocl_AnyType_Type = Generalization(general=Type, specific=essentialocl_AnyType)
gen_essentialocl_SetType_CollectionType = Generalization(general=CollectionType, specific=essentialocl_SetType)
gen_essentialocl_TupleType_Class = Generalization(general=Class_, specific=essentialocl_TupleType)
gen_essentialocl_TupleType_DataType = Generalization(general=DataType, specific=essentialocl_TupleType)

# Domain Model
domain_model = DomainModel(
    name="essentialocl",
    types={qvttemplate_TemplateExp, LiteralExp, Variable, OclExpression, qvttemplate_ObjectTemplateExp, TemplateExp, PropertyTemplateItem, Class_, qvttemplate_CollectionTemplateExp, qvttemplate_PropertyTemplateItem, Element, ObjectTemplateExp, Property_, imperativeocl_ImperativeIterateExp, ImperativeLoopExp, imperativeocl_AssignExp, ImperativeExpression, imperativeocl_BlockExp, imperativeocl_SwitchExp, CallExp, AltExp, imperativeocl_VariableInitExp, CollectionType, imperativeocl_ComputeExp, imperativeocl_AltExp, imperativeocl_UnlinkExp, imperativeocl_ReturnExp, imperativeocl_BreakExp, imperativeocl_TryExp, Type, imperativeocl_RaiseExp, imperativeocl_WhileExp, imperativeocl_Typedef, imperativeocl_InstantiationExp, imperativeocl_DictionaryType, imperativeocl_DictLiteralExp, DictLiteralPart, imperativeocl_DictLiteralPart, imperativeocl_TemplateParameterType, imperativeocl_LogExp, imperativeocl_ContinueExp, imperativeocl_ForExp, imperativeocl_TupleExp, imperativeocl_AssertExp, LogExp, imperativeocl_ImperativeLoopExp, LoopExp, imperativeocl_CollectorExp, imperativeocl_ImperativeExpression, imperativeocl_UnpackExp, imperativeocl_AnonymousTupleType, imperativeocl_AnonymousTupleLiteralExp, AnonymousTupleLiteralPart, imperativeocl_AnonymousTupleLiteralPart, Operation, emof_DataType, emof_Element, Object, Tag, Comment, emof_Tag, Transformation, Module, emof_Enumeration, DataType, EnumerationLiteral, emof_NamedElement, emof_Extent, emof_Object, emof_Operation, MultiplicityElement, TypedElement, imperativeocl_ListType, emof_Class, emof_MultiplicityElement, emof_Package, NamedElement, Package, emof_Type, emof_Parameter, emof_EnumerationLiteral, Enumeration_, emof_Property, Parameter_, emof_PrimitiveType, emof_URIExtent, Extent, emof_Comment, qvtoperational_MappingBody, OperationBody, qvtoperational_Helper, ImperativeOperation, qvtoperational_ResolveExp, qvtoperational_ResolveInExp, ResolveExp, MappingOperation, qvtoperational_OperationalTransformation, emof_TypedElement, Relation, qvtoperational_MappingParameter, VarParameter, RelationDomain, qvtoperational_MappingOperation, qvtoperational_MappingCallExp, ImperativeCallExp, qvtoperational_Constructor, qvtoperational_ContextualProperty, qvtoperational_EntryOperation, ModelParameter, EntryOperation, qvtoperational_Library, qvtoperational_ModelParameter, qvtoperational_ModelType, URIExtent, qvtoperational_Module, ModuleImport, ModelType, qvtoperational_ImperativeCallExp, OperationCallExp, qvtoperational_ImperativeOperation, qvtoperational_VarParameter, qvtoperational_OperationBody, qvtoperational_ConstructorBody, qvtoperational_ObjectExp, InstantiationExp, ConstructorBody, qvtcore_Area, GuardPattern, qvtoperational_ModuleImport, qvtcore_BottomPattern, CorePattern, Area, Assignment, RealizedVariable, EnforcementOperation, qvtcore_GuardPattern, qvtcore_Mapping, Rule, Mapping, qvtcore_RealizedVariable, qvtcore_CoreDomain, Domain, qvtcore_CorePattern, Pattern, BottomPattern, qvtcore_Assignment, qvtbase_Domain, TypedModel, qvtbase_Transformation, qvtbase_TypedModel, qvtbase_Rule, qvtcore_EnforcementOperation, Predicate, qvtbase_Predicate, qvtbase_Function, qvtbase_FunctionParameter, qvtrelation_RelationalTransformation, Key, qvtrelation_Relation, RelationImplementation, qvtbase_Pattern, qvtrelation_RelationDomain, DomainPattern, qvtrelation_DomainPattern, qvtrelation_RelationImplementation, qvtrelation_Key, RelationalTransformation, essentialocl_OclExpression, TryExp, essentialocl_UnlimitedNaturalExp, NumericLiteralExp, essentialocl_IfExp, essentialocl_LetExp, essentialocl_BooleanLiteralExp, PrimitiveLiteralExp, essentialocl_CallExp, LetExp, ComputeExp, essentialocl_PropertyCallExp, FeaturePropertyCall, essentialocl_VariableExp, essentialocl_TypeExp, essentialocl_LoopExp, essentialocl_Variable, essentialocl_IntegerLiteralExp, essentialocl_OperationCallExp, essentialocl_RealLiteralExp, essentialocl_LiteralExp, essentialocl_IterateExp, essentialocl_PrimitiveLiteralExp, essentialocl_NumericLiteralExp, essentialocl_CollectionLiteralExp, CollectionLiteralPart, essentialocl_CollectionLiteralPart, CollectionLiteralExp, essentialocl_CollectionItem, essentialocl_IteratorExp, essentialocl_TupleLiteralExp, essentialocl_StringLiteralExp, TupleLiteralPart, essentialocl_NullLiteralExp, essentialocl_ExpressionInOcl, OpaqueExpression, essentialocl_OpaqueExpression, essentialocl_InvalidLiteralExp, essentialocl_FeaturePropertyCall, essentialocl_TupleLiteralPart, TupleLiteralExp, essentialocl_BagType, essentialocl_CollectionType, essentialocl_EnumLiteralExp, essentialocl_InvalidType, essentialocl_CollectionRange, essentialocl_OrderedSetType, essentialocl_SequenceType, essentialocl_VoidType, essentialocl_AnyType, essentialocl_SetType, essentialocl_TupleType, SeverityKind, DirectionKind, ImportKind, EnforcementMode, CollectionKind},
    associations={bindsTo0, where1, part3, referredClass4, match9, objContainer12, value13, referredProperty15, target17, value19, left21, defaultValue24, body27, alternativePart29, elsePart30, part5, referredCollectionType7, body37, returnedElement40, body42, condition44, body46, target49, item51, value54, tryBody56, exception58, exceptBody59, referredVariable33, condition35, element64, base66, condition68, instantiatedClass71, extent73, argument76, keyType79, part81, key82, value84, exception62, log91, assertion92, condition95, target97, variable99, elementType101, part103, value104, condition87, element89, ownedAttribute106, ownedOperation108, superClass109, tag112, ownedComment113, element114, transformation116, owner117, ownedLiteral119, ownedType125, nestedPackage127, package128, operation130, enumeration132, class_133, opposite135, module138, class_120, ownedParameter122, raisedException123, annotatedElement142, initSection143, endSection145, condition148, inMapping150, intermediateClass151, type140, entry161, relation163, refinedDomain165, extent166, disjunct169, refinedRelation171, merged174, inherited177, when180, context183, overridden185, refined153, intermediateProperty156, modelParameter159, result189, overridden191, body192, metamodel194, additionalCondition196, ownedTag199, configProperty201, moduleImport203, usedModelType205, context188, module208, importedModule210, ctxOwner213, resOwner215, operation217, content219, referredObject221, body223, guardPattern225, binding206, value232, targetProperty235, area238, assignment239, realizedVariable241, enforcementOperation242, area244, specification246, local247, context250, bottomPattern226, bottomPattern228, slotExpression230, rule255, typedModel256, ownedTag257, modelParameter259, rule262, extends265, transformation267, usedPackage269, dependsOn271, domain274, bottomPattern252, operationCallExp254, predicate280, bindsTo281, whenOwner283, whereOwner285, conditionExpression287, pattern289, queryExpression290, ownedKey292, variable294, transformation275, overrides278, when299, pattern301, rootVariable302, templateExpression305, relation306, impl308, inDirectionOf310, identifies313, part315, transformation318, operationalImpl296, where297, tryBodyOwner321, condition322, thenExpression324, elseExpression327, in_330, source319, initExpression334, LetExp336, computeOwner338, bindParameter339, referredProperty342, referredVariable344, referredType346, body348, variable332, iterator350, argument353, referredOperation355, result358, part360, CollectionLiteralExp361, item364, last368, part371, bodyExpression372, context374, resultVariable377, parameterVariable380, TupleLiteralExp383, attribute386, elementType388, referredEnumLiteral390, first366},
    generalizations={gen_qvttemplate_TemplateExp_LiteralExp, gen_qvttemplate_ObjectTemplateExp_TemplateExp, gen_qvttemplate_CollectionTemplateExp_TemplateExp, gen_qvttemplate_PropertyTemplateItem_Element, gen_imperativeocl_ImperativeIterateExp_ImperativeLoopExp, gen_imperativeocl_AssignExp_ImperativeExpression, gen_imperativeocl_BlockExp_ImperativeExpression, gen_imperativeocl_SwitchExp_CallExp, gen_imperativeocl_SwitchExp_ImperativeExpression, gen_imperativeocl_VariableInitExp_ImperativeExpression, gen_imperativeocl_ComputeExp_ImperativeExpression, gen_imperativeocl_AltExp_ImperativeExpression, gen_imperativeocl_UnlinkExp_ImperativeExpression, gen_imperativeocl_ReturnExp_ImperativeExpression, gen_imperativeocl_BreakExp_ImperativeExpression, gen_imperativeocl_TryExp_ImperativeExpression, gen_imperativeocl_RaiseExp_ImperativeExpression, gen_imperativeocl_WhileExp_ImperativeExpression, gen_imperativeocl_Typedef_Class, gen_imperativeocl_InstantiationExp_ImperativeExpression, gen_imperativeocl_DictionaryType_CollectionType, gen_imperativeocl_DictLiteralExp_LiteralExp, gen_imperativeocl_DictLiteralPart_Element, gen_imperativeocl_TemplateParameterType_Type, gen_imperativeocl_LogExp_ImperativeExpression, gen_imperativeocl_ContinueExp_ImperativeExpression, gen_imperativeocl_ForExp_ImperativeLoopExp, gen_imperativeocl_TupleExp_ImperativeExpression, gen_imperativeocl_AssertExp_ImperativeExpression, gen_imperativeocl_ImperativeLoopExp_LoopExp, gen_imperativeocl_ImperativeLoopExp_ImperativeExpression, gen_imperativeocl_CollectorExp_ImperativeLoopExp, gen_imperativeocl_ImperativeExpression_OclExpression, gen_imperativeocl_UnpackExp_ImperativeExpression, gen_imperativeocl_AnonymousTupleType_Class, gen_imperativeocl_AnonymousTupleLiteralExp_LiteralExp, gen_imperativeocl_AnonymousTupleLiteralPart_Element, gen_emof_DataType_Type, gen_emof_Element_Object, gen_emof_Tag_Element, gen_emof_Enumeration_DataType, gen_emof_NamedElement_Element, gen_emof_Extent_Object, gen_emof_Operation_MultiplicityElement, gen_imperativeocl_ListType_CollectionType, gen_emof_Class_Type, gen_emof_Package_NamedElement, gen_emof_Type_NamedElement, gen_emof_Parameter_MultiplicityElement, gen_emof_Parameter_TypedElement, gen_emof_EnumerationLiteral_NamedElement, gen_emof_Property_MultiplicityElement, gen_emof_Property_TypedElement, gen_emof_Operation_TypedElement, gen_emof_PrimitiveType_DataType, gen_emof_URIExtent_Extent, gen_emof_Comment_Element, gen_qvtoperational_MappingBody_OperationBody, gen_qvtoperational_Helper_ImperativeOperation, gen_qvtoperational_ResolveExp_CallExp, gen_qvtoperational_ResolveInExp_ResolveExp, gen_qvtoperational_OperationalTransformation_Module, gen_emof_TypedElement_NamedElement, gen_qvtoperational_MappingParameter_VarParameter, gen_qvtoperational_MappingOperation_ImperativeOperation, gen_qvtoperational_MappingOperation_Operation, gen_qvtoperational_MappingOperation_NamedElement, gen_qvtoperational_MappingCallExp_ImperativeCallExp, gen_qvtoperational_Constructor_ImperativeOperation, gen_qvtoperational_ContextualProperty_Property, gen_qvtoperational_EntryOperation_ImperativeOperation, gen_qvtoperational_Library_Module, gen_qvtoperational_ModelParameter_VarParameter, gen_qvtoperational_ModelType_Class, gen_qvtoperational_ModelType_URIExtent, gen_qvtoperational_Module_Class, gen_qvtoperational_Module_Package, gen_qvtoperational_ImperativeCallExp_OperationCallExp, gen_qvtoperational_ImperativeOperation_Operation, gen_qvtoperational_VarParameter_Parameter, gen_qvtoperational_VarParameter_Variable, gen_qvtoperational_OperationBody_Element, gen_qvtoperational_ConstructorBody_OperationBody, gen_qvtoperational_ObjectExp_InstantiationExp, gen_qvtoperational_ModuleImport_Element, gen_qvtcore_BottomPattern_CorePattern, gen_qvtcore_GuardPattern_CorePattern, gen_qvtcore_Mapping_Rule, gen_qvtcore_Mapping_Area, gen_qvtcore_RealizedVariable_Variable, gen_qvtcore_CoreDomain_Domain, gen_qvtcore_CoreDomain_Area, gen_qvtcore_CorePattern_Pattern, gen_qvtbase_Domain_NamedElement, gen_qvtbase_Transformation_Class, gen_qvtbase_Transformation_Package, gen_qvtbase_TypedModel_NamedElement, gen_qvtbase_Rule_NamedElement, gen_qvtbase_Predicate_Element, gen_qvtbase_Function_Operation, gen_qvtbase_FunctionParameter_Parameter, gen_qvtbase_FunctionParameter_Variable, gen_qvtrelation_RelationalTransformation_Transformation, gen_qvtrelation_Relation_Rule, gen_qvtbase_Pattern_Element, gen_qvtrelation_RelationDomain_Domain, gen_qvtrelation_DomainPattern_Pattern, gen_qvtrelation_RelationImplementation_Element, gen_qvtrelation_Key_Element, gen_essentialocl_OclExpression_TypedElement, gen_essentialocl_UnlimitedNaturalExp_NumericLiteralExp, gen_essentialocl_IfExp_OclExpression, gen_essentialocl_LetExp_OclExpression, gen_essentialocl_BooleanLiteralExp_PrimitiveLiteralExp, gen_essentialocl_CallExp_OclExpression, gen_essentialocl_PropertyCallExp_FeaturePropertyCall, gen_essentialocl_VariableExp_OclExpression, gen_essentialocl_TypeExp_OclExpression, gen_essentialocl_LoopExp_CallExp, gen_essentialocl_LoopExp_OclExpression, gen_essentialocl_Variable_TypedElement, gen_essentialocl_IntegerLiteralExp_NumericLiteralExp, gen_essentialocl_OperationCallExp_FeaturePropertyCall, gen_essentialocl_RealLiteralExp_NumericLiteralExp, gen_essentialocl_LiteralExp_OclExpression, gen_essentialocl_IterateExp_LoopExp, gen_essentialocl_PrimitiveLiteralExp_LiteralExp, gen_essentialocl_NumericLiteralExp_PrimitiveLiteralExp, gen_essentialocl_CollectionLiteralExp_LiteralExp, gen_essentialocl_CollectionLiteralPart_TypedElement, gen_essentialocl_CollectionItem_CollectionLiteralPart, gen_essentialocl_IteratorExp_LoopExp, gen_essentialocl_TupleLiteralExp_LiteralExp, gen_essentialocl_StringLiteralExp_PrimitiveLiteralExp, gen_essentialocl_NullLiteralExp_LiteralExp, gen_essentialocl_ExpressionInOcl_OpaqueExpression, gen_essentialocl_InvalidLiteralExp_LiteralExp, gen_essentialocl_FeaturePropertyCall_CallExp, gen_essentialocl_TupleLiteralPart_TypedElement, gen_essentialocl_BagType_CollectionType, gen_essentialocl_CollectionType_DataType, gen_essentialocl_EnumLiteralExp_LiteralExp, gen_essentialocl_InvalidType_Type, gen_essentialocl_CollectionRange_CollectionLiteralPart, gen_essentialocl_OrderedSetType_CollectionType, gen_essentialocl_SequenceType_CollectionType, gen_essentialocl_VoidType_Type, gen_essentialocl_AnyType_Class, gen_essentialocl_AnyType_Type, gen_essentialocl_SetType_CollectionType, gen_essentialocl_TupleType_Class, gen_essentialocl_TupleType_DataType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)