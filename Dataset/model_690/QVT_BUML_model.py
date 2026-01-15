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
            EnumerationLiteral(name="out"),
			EnumerationLiteral(name="in"),
			EnumerationLiteral(name="inout")
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
Variable = Class(name="Variable")
OclExpression = Class(name="OclExpression")
qvttemplate_TemplateExp = Class(name="qvttemplate::TemplateExp", is_abstract=True)
LiteralExp = Class(name="LiteralExp")
qvttemplate_PropertyTemplateItem = Class(name="qvttemplate::PropertyTemplateItem")
Element = Class(name="Element")
ObjectTemplateExp = Class(name="ObjectTemplateExp")
qvttemplate_ObjectTemplateExp = Class(name="qvttemplate::ObjectTemplateExp")
TemplateExp = Class(name="TemplateExp")
PropertyTemplateItem = Class(name="PropertyTemplateItem")
Class_ = Class(name="Class")
qvttemplate_CollectionTemplateExp = Class(name="qvttemplate::CollectionTemplateExp")
CollectionType = Class(name="CollectionType")
imperativeocl_BlockExp = Class(name="imperativeocl::BlockExp")
Property_ = Class(name="Property")
imperativeocl_ImperativeIterateExp = Class(name="imperativeocl::ImperativeIterateExp")
ImperativeLoopExp = Class(name="ImperativeLoopExp")
imperativeocl_AssignExp = Class(name="imperativeocl::AssignExp")
ImperativeExpression = Class(name="ImperativeExpression")
imperativeocl_ComputeExp = Class(name="imperativeocl::ComputeExp")
imperativeocl_SwitchExp = Class(name="imperativeocl::SwitchExp")
CallExp = Class(name="CallExp")
AltExp = Class(name="AltExp")
imperativeocl_VariableInitExp = Class(name="imperativeocl::VariableInitExp")
imperativeocl_WhileExp = Class(name="imperativeocl::WhileExp")
imperativeocl_ReturnExp = Class(name="imperativeocl::ReturnExp")
imperativeocl_AltExp = Class(name="imperativeocl::AltExp")
imperativeocl_UnlinkExp = Class(name="imperativeocl::UnlinkExp")
imperativeocl_TupleExp = Class(name="imperativeocl::TupleExp")
imperativeocl_Typedef = Class(name="imperativeocl::Typedef")
imperativeocl_BreakExp = Class(name="imperativeocl::BreakExp")
imperativeocl_TryExp = Class(name="imperativeocl::TryExp")
Type = Class(name="Type")
imperativeocl_RaiseExp = Class(name="imperativeocl::RaiseExp")
imperativeocl_ContinueExp = Class(name="imperativeocl::ContinueExp")
imperativeocl_ForExp = Class(name="imperativeocl::ForExp")
imperativeocl_DictionaryType = Class(name="imperativeocl::DictionaryType")
imperativeocl_InstantiationExp = Class(name="imperativeocl::InstantiationExp")
imperativeocl_DictLiteralExp = Class(name="imperativeocl::DictLiteralExp")
DictLiteralPart = Class(name="DictLiteralPart")
imperativeocl_DictLiteralPart = Class(name="imperativeocl::DictLiteralPart")
imperativeocl_AssertExp = Class(name="imperativeocl::AssertExp")
LogExp = Class(name="LogExp")
imperativeocl_TemplateParameterType = Class(name="imperativeocl::TemplateParameterType")
imperativeocl_LogExp = Class(name="imperativeocl::LogExp")
imperativeocl_CollectorExp = Class(name="imperativeocl::CollectorExp")
imperativeocl_ImperativeExpression = Class(name="imperativeocl::ImperativeExpression", is_abstract=True)
imperativeocl_UnpackExp = Class(name="imperativeocl::UnpackExp")
imperativeocl_AnonymousTupleType = Class(name="imperativeocl::AnonymousTupleType")
imperativeocl_AnonymousTupleLiteralExp = Class(name="imperativeocl::AnonymousTupleLiteralExp")
AnonymousTupleLiteralPart = Class(name="AnonymousTupleLiteralPart")
imperativeocl_ImperativeLoopExp = Class(name="imperativeocl::ImperativeLoopExp", is_abstract=True)
LoopExp = Class(name="LoopExp")
imperativeocl_ListType = Class(name="imperativeocl::ListType")
emof_Class = Class(name="emof::Class")
Operation = Class(name="Operation")
imperativeocl_AnonymousTupleLiteralPart = Class(name="imperativeocl::AnonymousTupleLiteralPart")
emof_DataType = Class(name="emof::DataType", is_abstract=True)
emof_Element = Class(name="emof::Element", is_abstract=True)
Object = Class(name="Object")
Tag = Class(name="Tag")
emof_Tag = Class(name="emof::Tag")
Transformation = Class(name="Transformation")
Module = Class(name="Module")
Comment = Class(name="Comment")
emof_Enumeration = Class(name="emof::Enumeration")
DataType = Class(name="DataType")
EnumerationLiteral = Class(name="EnumerationLiteral")
emof_NamedElement = Class(name="emof::NamedElement", is_abstract=True)
emof_Extent = Class(name="emof::Extent")
emof_Object = Class(name="emof::Object")
emof_Operation = Class(name="emof::Operation")
MultiplicityElement = Class(name="MultiplicityElement")
TypedElement = Class(name="TypedElement")
Parameter_ = Class(name="Parameter")
emof_MultiplicityElement = Class(name="emof::MultiplicityElement", is_abstract=True)
emof_EnumerationLiteral = Class(name="emof::EnumerationLiteral")
emof_Package = Class(name="emof::Package")
NamedElement = Class(name="NamedElement")
Package = Class(name="Package")
emof_Type = Class(name="emof::Type", is_abstract=True)
emof_Parameter = Class(name="emof::Parameter")
Extent = Class(name="Extent")
Enumeration_ = Class(name="Enumeration")
emof_Property = Class(name="emof::Property")
emof_TypedElement = Class(name="emof::TypedElement", is_abstract=True)
emof_PrimitiveType = Class(name="emof::PrimitiveType")
emof_URIExtent = Class(name="emof::URIExtent")
emof_Comment = Class(name="emof::Comment")
qvtoperational_MappingBody = Class(name="qvtoperational::MappingBody")
OperationBody = Class(name="OperationBody")
qvtoperational_Helper = Class(name="qvtoperational::Helper")
ImperativeOperation = Class(name="ImperativeOperation")
qvtoperational_ResolveExp = Class(name="qvtoperational::ResolveExp")
qvtoperational_ResolveInExp = Class(name="qvtoperational::ResolveInExp")
ResolveExp = Class(name="ResolveExp")
MappingOperation = Class(name="MappingOperation")
qvtoperational_OperationalTransformation = Class(name="qvtoperational::OperationalTransformation")
ModelParameter = Class(name="ModelParameter")
EntryOperation = Class(name="EntryOperation")
Relation = Class(name="Relation")
qvtoperational_MappingParameter = Class(name="qvtoperational::MappingParameter")
VarParameter = Class(name="VarParameter")
RelationDomain = Class(name="RelationDomain")
qvtoperational_MappingOperation = Class(name="qvtoperational::MappingOperation")
qvtoperational_MappingCallExp = Class(name="qvtoperational::MappingCallExp")
ImperativeCallExp = Class(name="ImperativeCallExp")
qvtoperational_Constructor = Class(name="qvtoperational::Constructor")
qvtoperational_ContextualProperty = Class(name="qvtoperational::ContextualProperty")
qvtoperational_Library = Class(name="qvtoperational::Library")
qvtoperational_EntryOperation = Class(name="qvtoperational::EntryOperation")
qvtoperational_ImperativeCallExp = Class(name="qvtoperational::ImperativeCallExp")
OperationCallExp = Class(name="OperationCallExp")
qvtoperational_ImperativeOperation = Class(name="qvtoperational::ImperativeOperation")
ModelType = Class(name="ModelType")
qvtoperational_ModelParameter = Class(name="qvtoperational::ModelParameter")
qvtoperational_ModelType = Class(name="qvtoperational::ModelType")
URIExtent = Class(name="URIExtent")
qvtoperational_Module = Class(name="qvtoperational::Module")
ModuleImport = Class(name="ModuleImport")
qvtoperational_ModuleImport = Class(name="qvtoperational::ModuleImport")
qvtoperational_VarParameter = Class(name="qvtoperational::VarParameter")
qvtoperational_OperationBody = Class(name="qvtoperational::OperationBody")
qvtoperational_ConstructorBody = Class(name="qvtoperational::ConstructorBody")
qvtoperational_ObjectExp = Class(name="qvtoperational::ObjectExp")
InstantiationExp = Class(name="InstantiationExp")
ConstructorBody = Class(name="ConstructorBody")
qvtcore_Area = Class(name="qvtcore::Area", is_abstract=True)
GuardPattern = Class(name="GuardPattern")
BottomPattern = Class(name="BottomPattern")
qvtcore_Assignment = Class(name="qvtcore::Assignment")
qvtcore_BottomPattern = Class(name="qvtcore::BottomPattern")
CorePattern = Class(name="CorePattern")
Area = Class(name="Area")
Assignment = Class(name="Assignment")
RealizedVariable = Class(name="RealizedVariable")
EnforcementOperation = Class(name="EnforcementOperation")
qvtcore_GuardPattern = Class(name="qvtcore::GuardPattern")
qvtcore_Mapping = Class(name="qvtcore::Mapping")
Rule = Class(name="Rule")
Mapping = Class(name="Mapping")
qvtcore_RealizedVariable = Class(name="qvtcore::RealizedVariable")
qvtcore_CoreDomain = Class(name="qvtcore::CoreDomain")
Domain = Class(name="Domain")
qvtcore_CorePattern = Class(name="qvtcore::CorePattern")
Pattern = Class(name="Pattern")
qvtcore_EnforcementOperation = Class(name="qvtcore::EnforcementOperation")
qvtbase_Domain = Class(name="qvtbase::Domain")
TypedModel = Class(name="TypedModel")
qvtbase_Transformation = Class(name="qvtbase::Transformation")
qvtbase_TypedModel = Class(name="qvtbase::TypedModel")
qvtbase_Rule = Class(name="qvtbase::Rule")
qvtbase_Pattern = Class(name="qvtbase::Pattern")
Predicate = Class(name="Predicate")
qvtbase_Predicate = Class(name="qvtbase::Predicate")
qvtbase_Function = Class(name="qvtbase::Function")
qvtbase_FunctionParameter = Class(name="qvtbase::FunctionParameter")
qvtrelation_RelationalTransformation = Class(name="qvtrelation::RelationalTransformation")
Key = Class(name="Key")
qvtrelation_Relation = Class(name="qvtrelation::Relation")
RelationImplementation = Class(name="RelationImplementation")
qvtrelation_RelationDomain = Class(name="qvtrelation::RelationDomain")
DomainPattern = Class(name="DomainPattern")
qvtrelation_DomainPattern = Class(name="qvtrelation::DomainPattern")
qvtrelation_RelationImplementation = Class(name="qvtrelation::RelationImplementation")
qvtrelation_Key = Class(name="qvtrelation::Key")
RelationalTransformation = Class(name="RelationalTransformation")
essentialocl_BooleanLiteralExp = Class(name="essentialocl::BooleanLiteralExp")
PrimitiveLiteralExp = Class(name="PrimitiveLiteralExp")
essentialocl_CallExp = Class(name="essentialocl::CallExp", is_abstract=True)
essentialocl_OclExpression = Class(name="essentialocl::OclExpression", is_abstract=True)
TryExp = Class(name="TryExp")
essentialocl_UnlimitedNaturalExp = Class(name="essentialocl::UnlimitedNaturalExp")
NumericLiteralExp = Class(name="NumericLiteralExp")
essentialocl_IfExp = Class(name="essentialocl::IfExp")
essentialocl_LetExp = Class(name="essentialocl::LetExp")
essentialocl_Variable = Class(name="essentialocl::Variable")
LetExp = Class(name="LetExp")
ComputeExp = Class(name="ComputeExp")
essentialocl_PropertyCallExp = Class(name="essentialocl::PropertyCallExp")
FeaturePropertyCall = Class(name="FeaturePropertyCall")
essentialocl_VariableExp = Class(name="essentialocl::VariableExp")
essentialocl_TypeExp = Class(name="essentialocl::TypeExp")
essentialocl_IntegerLiteralExp = Class(name="essentialocl::IntegerLiteralExp")
essentialocl_LoopExp = Class(name="essentialocl::LoopExp", is_abstract=True)
essentialocl_IteratorExp = Class(name="essentialocl::IteratorExp")
essentialocl_StringLiteralExp = Class(name="essentialocl::StringLiteralExp")
essentialocl_OperationCallExp = Class(name="essentialocl::OperationCallExp")
essentialocl_RealLiteralExp = Class(name="essentialocl::RealLiteralExp")
essentialocl_LiteralExp = Class(name="essentialocl::LiteralExp", is_abstract=True)
essentialocl_IterateExp = Class(name="essentialocl::IterateExp")
essentialocl_PrimitiveLiteralExp = Class(name="essentialocl::PrimitiveLiteralExp", is_abstract=True)
essentialocl_NumericLiteralExp = Class(name="essentialocl::NumericLiteralExp", is_abstract=True)
essentialocl_CollectionLiteralExp = Class(name="essentialocl::CollectionLiteralExp")
CollectionLiteralPart = Class(name="CollectionLiteralPart")
essentialocl_CollectionLiteralPart = Class(name="essentialocl::CollectionLiteralPart", is_abstract=True)
CollectionLiteralExp = Class(name="CollectionLiteralExp")
essentialocl_CollectionItem = Class(name="essentialocl::CollectionItem")
essentialocl_CollectionRange = Class(name="essentialocl::CollectionRange")
essentialocl_TupleLiteralExp = Class(name="essentialocl::TupleLiteralExp")
TupleLiteralPart = Class(name="TupleLiteralPart")
essentialocl_NullLiteralExp = Class(name="essentialocl::NullLiteralExp")
essentialocl_ExpressionInOcl = Class(name="essentialocl::ExpressionInOcl")
OpaqueExpression = Class(name="OpaqueExpression")
essentialocl_BagType = Class(name="essentialocl::BagType")
essentialocl_CollectionType = Class(name="essentialocl::CollectionType", is_abstract=True)
essentialocl_OpaqueExpression = Class(name="essentialocl::OpaqueExpression")
essentialocl_InvalidLiteralExp = Class(name="essentialocl::InvalidLiteralExp")
essentialocl_FeaturePropertyCall = Class(name="essentialocl::FeaturePropertyCall", is_abstract=True)
essentialocl_TupleLiteralPart = Class(name="essentialocl::TupleLiteralPart")
TupleLiteralExp = Class(name="TupleLiteralExp")
essentialocl_EnumLiteralExp = Class(name="essentialocl::EnumLiteralExp")
essentialocl_InvalidType = Class(name="essentialocl::InvalidType")
essentialocl_OrderedSetType = Class(name="essentialocl::OrderedSetType")
essentialocl_SequenceType = Class(name="essentialocl::SequenceType")
essentialocl_SetType = Class(name="essentialocl::SetType")
essentialocl_TupleType = Class(name="essentialocl::TupleType")
essentialocl_VoidType = Class(name="essentialocl::VoidType")
essentialocl_AnyType = Class(name="essentialocl::AnyType")

# Variable class attributes and methods

# OclExpression class attributes and methods

# qvttemplate_TemplateExp class attributes and methods

# LiteralExp class attributes and methods

# qvttemplate_PropertyTemplateItem class attributes and methods

# Element class attributes and methods

# ObjectTemplateExp class attributes and methods

# qvttemplate_ObjectTemplateExp class attributes and methods

# TemplateExp class attributes and methods

# PropertyTemplateItem class attributes and methods

# Class class attributes and methods

# qvttemplate_CollectionTemplateExp class attributes and methods
qvttemplate_CollectionTemplateExp_kind: Property = Property(name="kind", type=StringType)
qvttemplate_CollectionTemplateExp.attributes={qvttemplate_CollectionTemplateExp_kind}

# CollectionType class attributes and methods

# imperativeocl_BlockExp class attributes and methods

# Property class attributes and methods

# imperativeocl_ImperativeIterateExp class attributes and methods

# ImperativeLoopExp class attributes and methods

# imperativeocl_AssignExp class attributes and methods
imperativeocl_AssignExp_isReset: Property = Property(name="isReset", type=StringType)
imperativeocl_AssignExp.attributes={imperativeocl_AssignExp_isReset}

# ImperativeExpression class attributes and methods

# imperativeocl_ComputeExp class attributes and methods

# imperativeocl_SwitchExp class attributes and methods

# CallExp class attributes and methods

# AltExp class attributes and methods

# imperativeocl_VariableInitExp class attributes and methods
imperativeocl_VariableInitExp_withResult: Property = Property(name="withResult", type=StringType)
imperativeocl_VariableInitExp.attributes={imperativeocl_VariableInitExp_withResult}

# imperativeocl_WhileExp class attributes and methods

# imperativeocl_ReturnExp class attributes and methods

# imperativeocl_AltExp class attributes and methods

# imperativeocl_UnlinkExp class attributes and methods

# imperativeocl_TupleExp class attributes and methods

# imperativeocl_Typedef class attributes and methods

# imperativeocl_BreakExp class attributes and methods

# imperativeocl_TryExp class attributes and methods

# Type class attributes and methods

# imperativeocl_RaiseExp class attributes and methods

# imperativeocl_ContinueExp class attributes and methods

# imperativeocl_ForExp class attributes and methods

# imperativeocl_DictionaryType class attributes and methods

# imperativeocl_InstantiationExp class attributes and methods

# imperativeocl_DictLiteralExp class attributes and methods

# DictLiteralPart class attributes and methods

# imperativeocl_DictLiteralPart class attributes and methods

# imperativeocl_AssertExp class attributes and methods
imperativeocl_AssertExp_severity: Property = Property(name="severity", type=StringType)
imperativeocl_AssertExp.attributes={imperativeocl_AssertExp_severity}

# LogExp class attributes and methods

# imperativeocl_TemplateParameterType class attributes and methods
imperativeocl_TemplateParameterType_specification: Property = Property(name="specification", type=StringType)
imperativeocl_TemplateParameterType.attributes={imperativeocl_TemplateParameterType_specification}

# imperativeocl_LogExp class attributes and methods
imperativeocl_LogExp_text: Property = Property(name="text", type=StringType)
imperativeocl_LogExp_level: Property = Property(name="level", type=StringType)
imperativeocl_LogExp.attributes={imperativeocl_LogExp_level, imperativeocl_LogExp_text}

# imperativeocl_CollectorExp class attributes and methods

# imperativeocl_ImperativeExpression class attributes and methods

# imperativeocl_UnpackExp class attributes and methods

# imperativeocl_AnonymousTupleType class attributes and methods

# imperativeocl_AnonymousTupleLiteralExp class attributes and methods

# AnonymousTupleLiteralPart class attributes and methods

# imperativeocl_ImperativeLoopExp class attributes and methods

# LoopExp class attributes and methods

# imperativeocl_ListType class attributes and methods

# emof_Class class attributes and methods
emof_Class_isAbstract: Property = Property(name="isAbstract", type=StringType)
emof_Class.attributes={emof_Class_isAbstract}

# Operation class attributes and methods

# imperativeocl_AnonymousTupleLiteralPart class attributes and methods

# emof_DataType class attributes and methods

# emof_Element class attributes and methods

# Object class attributes and methods

# Tag class attributes and methods

# emof_Tag class attributes and methods
emof_Tag_value: Property = Property(name="value", type=StringType)
emof_Tag_name: Property = Property(name="name", type=StringType)
emof_Tag.attributes={emof_Tag_value, emof_Tag_name}

# Transformation class attributes and methods

# Module class attributes and methods

# Comment class attributes and methods

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

# Parameter class attributes and methods

# emof_MultiplicityElement class attributes and methods
emof_MultiplicityElement_isUnique: Property = Property(name="isUnique", type=StringType)
emof_MultiplicityElement_isOrdered: Property = Property(name="isOrdered", type=StringType)
emof_MultiplicityElement_lower: Property = Property(name="lower", type=StringType)
emof_MultiplicityElement_upper: Property = Property(name="upper", type=StringType)
emof_MultiplicityElement.attributes={emof_MultiplicityElement_isUnique, emof_MultiplicityElement_upper, emof_MultiplicityElement_lower, emof_MultiplicityElement_isOrdered}

# emof_EnumerationLiteral class attributes and methods

# emof_Package class attributes and methods
emof_Package_uri: Property = Property(name="uri", type=StringType)
emof_Package.attributes={emof_Package_uri}

# NamedElement class attributes and methods

# Package class attributes and methods

# emof_Type class attributes and methods

# emof_Parameter class attributes and methods

# Extent class attributes and methods

# Enumeration class attributes and methods

# emof_Property class attributes and methods
emof_Property_isReadOnly: Property = Property(name="isReadOnly", type=StringType)
emof_Property_isDerived: Property = Property(name="isDerived", type=StringType)
emof_Property_isComposite: Property = Property(name="isComposite", type=StringType)
emof_Property_isId: Property = Property(name="isId", type=StringType)
emof_Property_default: Property = Property(name="default", type=StringType)
emof_Property.attributes={emof_Property_isId, emof_Property_isComposite, emof_Property_isReadOnly, emof_Property_isDerived, emof_Property_default}

# emof_TypedElement class attributes and methods

# emof_PrimitiveType class attributes and methods

# emof_URIExtent class attributes and methods

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
qvtoperational_ResolveExp.attributes={qvtoperational_ResolveExp_isDeferred, qvtoperational_ResolveExp_one, qvtoperational_ResolveExp_isInverse}

# qvtoperational_ResolveInExp class attributes and methods

# ResolveExp class attributes and methods

# MappingOperation class attributes and methods

# qvtoperational_OperationalTransformation class attributes and methods

# ModelParameter class attributes and methods

# EntryOperation class attributes and methods

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

# qvtoperational_Library class attributes and methods

# qvtoperational_EntryOperation class attributes and methods

# qvtoperational_ImperativeCallExp class attributes and methods
qvtoperational_ImperativeCallExp_isVirtual: Property = Property(name="isVirtual", type=StringType)
qvtoperational_ImperativeCallExp.attributes={qvtoperational_ImperativeCallExp_isVirtual}

# OperationCallExp class attributes and methods

# qvtoperational_ImperativeOperation class attributes and methods
qvtoperational_ImperativeOperation_isBlackbox: Property = Property(name="isBlackbox", type=StringType)
qvtoperational_ImperativeOperation.attributes={qvtoperational_ImperativeOperation_isBlackbox}

# ModelType class attributes and methods

# qvtoperational_ModelParameter class attributes and methods

# qvtoperational_ModelType class attributes and methods
qvtoperational_ModelType_conformanceKind: Property = Property(name="conformanceKind", type=StringType)
qvtoperational_ModelType.attributes={qvtoperational_ModelType_conformanceKind}

# URIExtent class attributes and methods

# qvtoperational_Module class attributes and methods
qvtoperational_Module_isBlackbox: Property = Property(name="isBlackbox", type=StringType)
qvtoperational_Module.attributes={qvtoperational_Module_isBlackbox}

# ModuleImport class attributes and methods

# qvtoperational_ModuleImport class attributes and methods
qvtoperational_ModuleImport_kind: Property = Property(name="kind", type=StringType)
qvtoperational_ModuleImport.attributes={qvtoperational_ModuleImport_kind}

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

# BottomPattern class attributes and methods

# qvtcore_Assignment class attributes and methods
qvtcore_Assignment_isDefault: Property = Property(name="isDefault", type=StringType)
qvtcore_Assignment.attributes={qvtcore_Assignment_isDefault}

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

# qvtcore_EnforcementOperation class attributes and methods
qvtcore_EnforcementOperation_enforcementMode: Property = Property(name="enforcementMode", type=StringType)
qvtcore_EnforcementOperation.attributes={qvtcore_EnforcementOperation_enforcementMode}

# qvtbase_Domain class attributes and methods
qvtbase_Domain_isCheckable: Property = Property(name="isCheckable", type=StringType)
qvtbase_Domain_isEnforceable: Property = Property(name="isEnforceable", type=StringType)
qvtbase_Domain.attributes={qvtbase_Domain_isCheckable, qvtbase_Domain_isEnforceable}

# TypedModel class attributes and methods

# qvtbase_Transformation class attributes and methods

# qvtbase_TypedModel class attributes and methods

# qvtbase_Rule class attributes and methods

# qvtbase_Pattern class attributes and methods

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

# qvtrelation_RelationDomain class attributes and methods

# DomainPattern class attributes and methods

# qvtrelation_DomainPattern class attributes and methods

# qvtrelation_RelationImplementation class attributes and methods

# qvtrelation_Key class attributes and methods

# RelationalTransformation class attributes and methods

# essentialocl_BooleanLiteralExp class attributes and methods
essentialocl_BooleanLiteralExp_booleanSymbol: Property = Property(name="booleanSymbol", type=StringType)
essentialocl_BooleanLiteralExp.attributes={essentialocl_BooleanLiteralExp_booleanSymbol}

# PrimitiveLiteralExp class attributes and methods

# essentialocl_CallExp class attributes and methods

# essentialocl_OclExpression class attributes and methods

# TryExp class attributes and methods

# essentialocl_UnlimitedNaturalExp class attributes and methods
essentialocl_UnlimitedNaturalExp_symbol: Property = Property(name="symbol", type=StringType)
essentialocl_UnlimitedNaturalExp.attributes={essentialocl_UnlimitedNaturalExp_symbol}

# NumericLiteralExp class attributes and methods

# essentialocl_IfExp class attributes and methods

# essentialocl_LetExp class attributes and methods

# essentialocl_Variable class attributes and methods

# LetExp class attributes and methods

# ComputeExp class attributes and methods

# essentialocl_PropertyCallExp class attributes and methods

# FeaturePropertyCall class attributes and methods

# essentialocl_VariableExp class attributes and methods

# essentialocl_TypeExp class attributes and methods

# essentialocl_IntegerLiteralExp class attributes and methods
essentialocl_IntegerLiteralExp_integerSymbol: Property = Property(name="integerSymbol", type=StringType)
essentialocl_IntegerLiteralExp.attributes={essentialocl_IntegerLiteralExp_integerSymbol}

# essentialocl_LoopExp class attributes and methods

# essentialocl_IteratorExp class attributes and methods

# essentialocl_StringLiteralExp class attributes and methods
essentialocl_StringLiteralExp_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
essentialocl_StringLiteralExp.attributes={essentialocl_StringLiteralExp_stringSymbol}

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

# essentialocl_CollectionRange class attributes and methods

# essentialocl_TupleLiteralExp class attributes and methods

# TupleLiteralPart class attributes and methods

# essentialocl_NullLiteralExp class attributes and methods

# essentialocl_ExpressionInOcl class attributes and methods

# OpaqueExpression class attributes and methods

# essentialocl_BagType class attributes and methods

# essentialocl_CollectionType class attributes and methods

# essentialocl_OpaqueExpression class attributes and methods

# essentialocl_InvalidLiteralExp class attributes and methods

# essentialocl_FeaturePropertyCall class attributes and methods

# essentialocl_TupleLiteralPart class attributes and methods

# TupleLiteralExp class attributes and methods

# essentialocl_EnumLiteralExp class attributes and methods

# essentialocl_InvalidType class attributes and methods

# essentialocl_OrderedSetType class attributes and methods

# essentialocl_SequenceType class attributes and methods

# essentialocl_SetType class attributes and methods

# essentialocl_TupleType class attributes and methods

# essentialocl_VoidType class attributes and methods

# essentialocl_AnyType class attributes and methods

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
        Property(name="#14", type=qvttemplate_PropertyTemplateItem, multiplicity=Multiplicity(1, 1)),
        Property(name="013", type=ObjectTemplateExp, multiplicity=Multiplicity(1, 1))
    }
)
part3: BinaryAssociation = BinaryAssociation(
    name="part3",
    ends={
        Property(name="#", type=qvttemplate_ObjectTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="0", type=PropertyTemplateItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredClass4: BinaryAssociation = BinaryAssociation(
    name="referredClass4",
    ends={
        Property(name="Class", type=qvttemplate_ObjectTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="qvttemplate_ObjectTemplateExp", type=Class_, multiplicity=Multiplicity(1, 1))
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
defaultValue26: BinaryAssociation = BinaryAssociation(
    name="defaultValue26",
    ends={
        Property(name="OclExpression28", type=imperativeocl_AssignExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_AssignExp27", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value15: BinaryAssociation = BinaryAssociation(
    name="value15",
    ends={
        Property(name="OclExpression16", type=qvttemplate_PropertyTemplateItem, multiplicity=Multiplicity(1, 1)),
        Property(name="qvttemplate_PropertyTemplateItem", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referredProperty17: BinaryAssociation = BinaryAssociation(
    name="referredProperty17",
    ends={
        Property(name="Property", type=qvttemplate_PropertyTemplateItem, multiplicity=Multiplicity(1, 1)),
        Property(name="qvttemplate_PropertyTemplateItem18", type=Property_, multiplicity=Multiplicity(1, 1))
    }
)
target19: BinaryAssociation = BinaryAssociation(
    name="target19",
    ends={
        Property(name="Variable20", type=imperativeocl_ImperativeIterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_ImperativeIterateExp", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value21: BinaryAssociation = BinaryAssociation(
    name="value21",
    ends={
        Property(name="OclExpression22", type=imperativeocl_AssignExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_AssignExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left23: BinaryAssociation = BinaryAssociation(
    name="left23",
    ends={
        Property(name="OclExpression25", type=imperativeocl_AssignExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_AssignExp24", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body39: BinaryAssociation = BinaryAssociation(
    name="body39",
    ends={
        Property(name="OclExpression41", type=imperativeocl_WhileExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_WhileExp40", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body29: BinaryAssociation = BinaryAssociation(
    name="body29",
    ends={
        Property(name="OclExpression30", type=imperativeocl_BlockExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_BlockExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
alternativePart31: BinaryAssociation = BinaryAssociation(
    name="alternativePart31",
    ends={
        Property(name="AltExp", type=imperativeocl_SwitchExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_SwitchExp", type=AltExp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elsePart32: BinaryAssociation = BinaryAssociation(
    name="elsePart32",
    ends={
        Property(name="OclExpression34", type=imperativeocl_SwitchExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_SwitchExp33", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referredVariable35: BinaryAssociation = BinaryAssociation(
    name="referredVariable35",
    ends={
        Property(name="Variable36", type=imperativeocl_VariableInitExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_VariableInitExp", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition37: BinaryAssociation = BinaryAssociation(
    name="condition37",
    ends={
        Property(name="OclExpression38", type=imperativeocl_WhileExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_WhileExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value56: BinaryAssociation = BinaryAssociation(
    name="value56",
    ends={
        Property(name="OclExpression57", type=imperativeocl_ReturnExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_ReturnExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnedElement42: BinaryAssociation = BinaryAssociation(
    name="returnedElement42",
    ends={
        Property(name="#43", type=imperativeocl_ComputeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="7", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body44: BinaryAssociation = BinaryAssociation(
    name="body44",
    ends={
        Property(name="OclExpression45", type=imperativeocl_ComputeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_ComputeExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition46: BinaryAssociation = BinaryAssociation(
    name="condition46",
    ends={
        Property(name="OclExpression47", type=imperativeocl_AltExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_AltExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body48: BinaryAssociation = BinaryAssociation(
    name="body48",
    ends={
        Property(name="OclExpression50", type=imperativeocl_AltExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_AltExp49", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target51: BinaryAssociation = BinaryAssociation(
    name="target51",
    ends={
        Property(name="OclExpression52", type=imperativeocl_UnlinkExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_UnlinkExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
item53: BinaryAssociation = BinaryAssociation(
    name="item53",
    ends={
        Property(name="OclExpression55", type=imperativeocl_UnlinkExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_UnlinkExp54", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
element67: BinaryAssociation = BinaryAssociation(
    name="element67",
    ends={
        Property(name="OclExpression68", type=imperativeocl_TupleExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_TupleExp", type=OclExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
tryBody58: BinaryAssociation = BinaryAssociation(
    name="tryBody58",
    ends={
        Property(name="#60", type=imperativeocl_TryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="759", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exception61: BinaryAssociation = BinaryAssociation(
    name="exception61",
    ends={
        Property(name="Type", type=imperativeocl_TryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_TryExp", type=Type, multiplicity=Multiplicity(0, 9999))
    }
)
exceptBody62: BinaryAssociation = BinaryAssociation(
    name="exceptBody62",
    ends={
        Property(name="OclExpression64", type=imperativeocl_TryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_TryExp63", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exception65: BinaryAssociation = BinaryAssociation(
    name="exception65",
    ends={
        Property(name="Type66", type=imperativeocl_RaiseExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_RaiseExp", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
argument79: BinaryAssociation = BinaryAssociation(
    name="argument79",
    ends={
        Property(name="imperativeocl_InstantiationExp80", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="OclExpression81", type=imperativeocl_InstantiationExp, multiplicity=Multiplicity(1, 1))
    }
)
keyType82: BinaryAssociation = BinaryAssociation(
    name="keyType82",
    ends={
        Property(name="Type83", type=imperativeocl_DictionaryType, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_DictionaryType", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
base69: BinaryAssociation = BinaryAssociation(
    name="base69",
    ends={
        Property(name="Type70", type=imperativeocl_Typedef, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_Typedef", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
condition71: BinaryAssociation = BinaryAssociation(
    name="condition71",
    ends={
        Property(name="OclExpression73", type=imperativeocl_Typedef, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_Typedef72", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
instantiatedClass74: BinaryAssociation = BinaryAssociation(
    name="instantiatedClass74",
    ends={
        Property(name="Class75", type=imperativeocl_InstantiationExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_InstantiationExp", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
extent76: BinaryAssociation = BinaryAssociation(
    name="extent76",
    ends={
        Property(name="Variable78", type=imperativeocl_InstantiationExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_InstantiationExp77", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
part84: BinaryAssociation = BinaryAssociation(
    name="part84",
    ends={
        Property(name="DictLiteralPart", type=imperativeocl_DictLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_DictLiteralExp", type=DictLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key85: BinaryAssociation = BinaryAssociation(
    name="key85",
    ends={
        Property(name="OclExpression86", type=imperativeocl_DictLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_DictLiteralPart", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition90: BinaryAssociation = BinaryAssociation(
    name="condition90",
    ends={
        Property(name="OclExpression91", type=imperativeocl_LogExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_LogExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value87: BinaryAssociation = BinaryAssociation(
    name="value87",
    ends={
        Property(name="OclExpression89", type=imperativeocl_DictLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_DictLiteralPart88", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
element92: BinaryAssociation = BinaryAssociation(
    name="element92",
    ends={
        Property(name="Element", type=imperativeocl_LogExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_LogExp93", type=Element, multiplicity=Multiplicity(0, 1))
    }
)
log94: BinaryAssociation = BinaryAssociation(
    name="log94",
    ends={
        Property(name="LogExp", type=imperativeocl_AssertExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_AssertExp", type=LogExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assertion95: BinaryAssociation = BinaryAssociation(
    name="assertion95",
    ends={
        Property(name="OclExpression97", type=imperativeocl_AssertExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_AssertExp96", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target100: BinaryAssociation = BinaryAssociation(
    name="target100",
    ends={
        Property(name="Variable101", type=imperativeocl_CollectorExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_CollectorExp", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable102: BinaryAssociation = BinaryAssociation(
    name="variable102",
    ends={
        Property(name="Variable103", type=imperativeocl_UnpackExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_UnpackExp", type=Variable, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
elementType104: BinaryAssociation = BinaryAssociation(
    name="elementType104",
    ends={
        Property(name="Type105", type=imperativeocl_AnonymousTupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_AnonymousTupleType", type=Type, multiplicity=Multiplicity(0, 9999))
    }
)
condition98: BinaryAssociation = BinaryAssociation(
    name="condition98",
    ends={
        Property(name="OclExpression99", type=imperativeocl_ImperativeLoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_ImperativeLoopExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedAttribute109: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute109",
    ends={
        Property(name="Property110", type=emof_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="emof_Class", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation111: BinaryAssociation = BinaryAssociation(
    name="ownedOperation111",
    ends={
        Property(name="#112", type=emof_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="2", type=Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
part106: BinaryAssociation = BinaryAssociation(
    name="part106",
    ends={
        Property(name="AnonymousTupleLiteralPart", type=imperativeocl_AnonymousTupleLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_AnonymousTupleLiteralExp", type=AnonymousTupleLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value107: BinaryAssociation = BinaryAssociation(
    name="value107",
    ends={
        Property(name="OclExpression108", type=imperativeocl_AnonymousTupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="imperativeocl_AnonymousTupleLiteralPart", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass113: BinaryAssociation = BinaryAssociation(
    name="superClass113",
    ends={
        Property(name="Class115", type=emof_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="emof_Class114", type=Class_, multiplicity=Multiplicity(0, 9999))
    }
)
ownedComment119: BinaryAssociation = BinaryAssociation(
    name="ownedComment119",
    ends={
        Property(name="emof_Element", type=Comment, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="Comment", type=emof_Element, multiplicity=Multiplicity(1, 1))
    }
)
element120: BinaryAssociation = BinaryAssociation(
    name="element120",
    ends={
        Property(name="#122", type=emof_Tag, multiplicity=Multiplicity(1, 1)),
        Property(name="2121", type=Element, multiplicity=Multiplicity(0, 9999))
    }
)
transformation123: BinaryAssociation = BinaryAssociation(
    name="transformation123",
    ends={
        Property(name="#124", type=emof_Tag, multiplicity=Multiplicity(1, 1)),
        Property(name="5", type=Transformation, multiplicity=Multiplicity(0, 1))
    }
)
tag116: BinaryAssociation = BinaryAssociation(
    name="tag116",
    ends={
        Property(name="#118", type=emof_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="2117", type=Tag, multiplicity=Multiplicity(0, 9999))
    }
)
ownedLiteral127: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral127",
    ends={
        Property(name="#129", type=emof_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="2128", type=EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner125: BinaryAssociation = BinaryAssociation(
    name="owner125",
    ends={
        Property(name="#126", type=emof_Tag, multiplicity=Multiplicity(1, 1)),
        Property(name="3", type=Module, multiplicity=Multiplicity(0, 1))
    }
)
class130: BinaryAssociation = BinaryAssociation(
    name="class130",
    ends={
        Property(name="2131", type=Class_, multiplicity=Multiplicity(1, 1)),
        Property(name="#132", type=emof_Operation, multiplicity=Multiplicity(1, 1))
    }
)
ownedParameter133: BinaryAssociation = BinaryAssociation(
    name="ownedParameter133",
    ends={
        Property(name="#135", type=emof_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="2134", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
raisedException136: BinaryAssociation = BinaryAssociation(
    name="raisedException136",
    ends={
        Property(name="Type137", type=emof_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="emof_Operation", type=Type, multiplicity=Multiplicity(0, 9999))
    }
)
ownedType138: BinaryAssociation = BinaryAssociation(
    name="ownedType138",
    ends={
        Property(name="#140", type=emof_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="2139", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedPackage141: BinaryAssociation = BinaryAssociation(
    name="nestedPackage141",
    ends={
        Property(name="Package", type=emof_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="emof_Package", type=Package, multiplicity=Multiplicity(0, 9999))
    }
)
package142: BinaryAssociation = BinaryAssociation(
    name="package142",
    ends={
        Property(name="#144", type=emof_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="2143", type=Package, multiplicity=Multiplicity(1, 1))
    }
)
operation145: BinaryAssociation = BinaryAssociation(
    name="operation145",
    ends={
        Property(name="#147", type=emof_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="2146", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
enumeration148: BinaryAssociation = BinaryAssociation(
    name="enumeration148",
    ends={
        Property(name="#150", type=emof_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="2149", type=Enumeration_, multiplicity=Multiplicity(0, 1))
    }
)
class151: BinaryAssociation = BinaryAssociation(
    name="class151",
    ends={
        Property(name="Class152", type=emof_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="emof_Property", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
opposite153: BinaryAssociation = BinaryAssociation(
    name="opposite153",
    ends={
        Property(name="Property155", type=emof_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="emof_Property154", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
module156: BinaryAssociation = BinaryAssociation(
    name="module156",
    ends={
        Property(name="#158", type=emof_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="3157", type=Module, multiplicity=Multiplicity(0, 1))
    }
)
type159: BinaryAssociation = BinaryAssociation(
    name="type159",
    ends={
        Property(name="Type160", type=emof_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="emof_TypedElement", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
intermediateClass170: BinaryAssociation = BinaryAssociation(
    name="intermediateClass170",
    ends={
        Property(name="Class171", type=qvtoperational_OperationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_OperationalTransformation", type=Class_, multiplicity=Multiplicity(0, 9999))
    }
)
annotatedElement161: BinaryAssociation = BinaryAssociation(
    name="annotatedElement161",
    ends={
        Property(name="NamedElement", type=emof_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="emof_Comment", type=NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
initSection162: BinaryAssociation = BinaryAssociation(
    name="initSection162",
    ends={
        Property(name="OclExpression163", type=qvtoperational_MappingBody, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_MappingBody", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
endSection164: BinaryAssociation = BinaryAssociation(
    name="endSection164",
    ends={
        Property(name="OclExpression166", type=qvtoperational_MappingBody, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_MappingBody165", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition167: BinaryAssociation = BinaryAssociation(
    name="condition167",
    ends={
        Property(name="OclExpression168", type=qvtoperational_ResolveExp, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_ResolveExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inMapping169: BinaryAssociation = BinaryAssociation(
    name="inMapping169",
    ends={
        Property(name="MappingOperation", type=qvtoperational_ResolveInExp, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_ResolveInExp", type=MappingOperation, multiplicity=Multiplicity(0, 1))
    }
)
disjunct187: BinaryAssociation = BinaryAssociation(
    name="disjunct187",
    ends={
        Property(name="MappingOperation188", type=qvtoperational_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_MappingOperation", type=MappingOperation, multiplicity=Multiplicity(0, 9999))
    }
)
refined172: BinaryAssociation = BinaryAssociation(
    name="refined172",
    ends={
        Property(name="Transformation", type=qvtoperational_OperationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_OperationalTransformation173", type=Transformation, multiplicity=Multiplicity(0, 1))
    }
)
intermediateProperty174: BinaryAssociation = BinaryAssociation(
    name="intermediateProperty174",
    ends={
        Property(name="Property176", type=qvtoperational_OperationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_OperationalTransformation175", type=Property_, multiplicity=Multiplicity(0, 9999))
    }
)
modelParameter177: BinaryAssociation = BinaryAssociation(
    name="modelParameter177",
    ends={
        Property(name="ModelParameter", type=qvtoperational_OperationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_OperationalTransformation178", type=ModelParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entry179: BinaryAssociation = BinaryAssociation(
    name="entry179",
    ends={
        Property(name="EntryOperation", type=qvtoperational_OperationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_OperationalTransformation180", type=EntryOperation, multiplicity=Multiplicity(0, 1))
    }
)
relation181: BinaryAssociation = BinaryAssociation(
    name="relation181",
    ends={
        Property(name="Relation", type=qvtoperational_OperationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_OperationalTransformation182", type=Relation, multiplicity=Multiplicity(0, 9999))
    }
)
refinedDomain183: BinaryAssociation = BinaryAssociation(
    name="refinedDomain183",
    ends={
        Property(name="RelationDomain", type=qvtoperational_MappingParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_MappingParameter", type=RelationDomain, multiplicity=Multiplicity(0, 1))
    }
)
extent184: BinaryAssociation = BinaryAssociation(
    name="extent184",
    ends={
        Property(name="ModelParameter186", type=qvtoperational_MappingParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_MappingParameter185", type=ModelParameter, multiplicity=Multiplicity(0, 1))
    }
)
overridden203: BinaryAssociation = BinaryAssociation(
    name="overridden203",
    ends={
        Property(name="Property205", type=qvtoperational_ContextualProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_ContextualProperty204", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
refinedRelation189: BinaryAssociation = BinaryAssociation(
    name="refinedRelation189",
    ends={
        Property(name="Relation191", type=qvtoperational_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_MappingOperation190", type=Relation, multiplicity=Multiplicity(1, 1))
    }
)
merged192: BinaryAssociation = BinaryAssociation(
    name="merged192",
    ends={
        Property(name="MappingOperation194", type=qvtoperational_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_MappingOperation193", type=MappingOperation, multiplicity=Multiplicity(0, 9999))
    }
)
inherited195: BinaryAssociation = BinaryAssociation(
    name="inherited195",
    ends={
        Property(name="MappingOperation197", type=qvtoperational_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_MappingOperation196", type=MappingOperation, multiplicity=Multiplicity(0, 9999))
    }
)
when198: BinaryAssociation = BinaryAssociation(
    name="when198",
    ends={
        Property(name="OclExpression200", type=qvtoperational_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_MappingOperation199", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
context201: BinaryAssociation = BinaryAssociation(
    name="context201",
    ends={
        Property(name="Class202", type=qvtoperational_ContextualProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_ContextualProperty", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
context206: BinaryAssociation = BinaryAssociation(
    name="context206",
    ends={
        Property(name="#208", type=qvtoperational_ImperativeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="3207", type=VarParameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result209: BinaryAssociation = BinaryAssociation(
    name="result209",
    ends={
        Property(name="#211", type=qvtoperational_ImperativeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="3210", type=VarParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
overridden212: BinaryAssociation = BinaryAssociation(
    name="overridden212",
    ends={
        Property(name="ImperativeOperation", type=qvtoperational_ImperativeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_ImperativeOperation", type=ImperativeOperation, multiplicity=Multiplicity(0, 1))
    }
)
body213: BinaryAssociation = BinaryAssociation(
    name="body213",
    ends={
        Property(name="#215", type=qvtoperational_ImperativeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="3214", type=OperationBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
metamodel216: BinaryAssociation = BinaryAssociation(
    name="metamodel216",
    ends={
        Property(name="Package217", type=qvtoperational_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_ModelType", type=Package, multiplicity=Multiplicity(0, 9999))
    }
)
additionalCondition218: BinaryAssociation = BinaryAssociation(
    name="additionalCondition218",
    ends={
        Property(name="OclExpression220", type=qvtoperational_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_ModelType219", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedTag221: BinaryAssociation = BinaryAssociation(
    name="ownedTag221",
    ends={
        Property(name="#223", type=qvtoperational_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="2222", type=Tag, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
configProperty224: BinaryAssociation = BinaryAssociation(
    name="configProperty224",
    ends={
        Property(name="#226", type=qvtoperational_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="2225", type=Property_, multiplicity=Multiplicity(0, 9999))
    }
)
moduleImport227: BinaryAssociation = BinaryAssociation(
    name="moduleImport227",
    ends={
        Property(name="#229", type=qvtoperational_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="3228", type=ModuleImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usedModelType230: BinaryAssociation = BinaryAssociation(
    name="usedModelType230",
    ends={
        Property(name="ModelType", type=qvtoperational_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_Module", type=ModelType, multiplicity=Multiplicity(0, 9999))
    }
)
binding231: BinaryAssociation = BinaryAssociation(
    name="binding231",
    ends={
        Property(name="ModelType232", type=qvtoperational_ModuleImport, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_ModuleImport", type=ModelType, multiplicity=Multiplicity(0, 9999))
    }
)
module233: BinaryAssociation = BinaryAssociation(
    name="module233",
    ends={
        Property(name="#235", type=qvtoperational_ModuleImport, multiplicity=Multiplicity(1, 1)),
        Property(name="3234", type=Module, multiplicity=Multiplicity(0, 1))
    }
)
importedModule236: BinaryAssociation = BinaryAssociation(
    name="importedModule236",
    ends={
        Property(name="Module", type=qvtoperational_ModuleImport, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_ModuleImport237", type=Module, multiplicity=Multiplicity(1, 1))
    }
)
content247: BinaryAssociation = BinaryAssociation(
    name="content247",
    ends={
        Property(name="OclExpression248", type=qvtoperational_OperationBody, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_OperationBody", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ctxOwner238: BinaryAssociation = BinaryAssociation(
    name="ctxOwner238",
    ends={
        Property(name="#240", type=qvtoperational_VarParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="3239", type=ImperativeOperation, multiplicity=Multiplicity(0, 1))
    }
)
resOwner241: BinaryAssociation = BinaryAssociation(
    name="resOwner241",
    ends={
        Property(name="#243", type=qvtoperational_VarParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="3242", type=ImperativeOperation, multiplicity=Multiplicity(0, 1))
    }
)
operation244: BinaryAssociation = BinaryAssociation(
    name="operation244",
    ends={
        Property(name="#246", type=qvtoperational_OperationBody, multiplicity=Multiplicity(1, 1)),
        Property(name="3245", type=ImperativeOperation, multiplicity=Multiplicity(0, 1))
    }
)
slotExpression261: BinaryAssociation = BinaryAssociation(
    name="slotExpression261",
    ends={
        Property(name="OclExpression262", type=qvtcore_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcore_Assignment", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referredObject249: BinaryAssociation = BinaryAssociation(
    name="referredObject249",
    ends={
        Property(name="Variable250", type=qvtoperational_ObjectExp, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_ObjectExp", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
body251: BinaryAssociation = BinaryAssociation(
    name="body251",
    ends={
        Property(name="ConstructorBody", type=qvtoperational_ObjectExp, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtoperational_ObjectExp252", type=ConstructorBody, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
guardPattern253: BinaryAssociation = BinaryAssociation(
    name="guardPattern253",
    ends={
        Property(name="#254", type=qvtcore_Area, multiplicity=Multiplicity(1, 1)),
        Property(name="4", type=GuardPattern, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bottomPattern255: BinaryAssociation = BinaryAssociation(
    name="bottomPattern255",
    ends={
        Property(name="#257", type=qvtcore_Area, multiplicity=Multiplicity(1, 1)),
        Property(name="4256", type=BottomPattern, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bottomPattern258: BinaryAssociation = BinaryAssociation(
    name="bottomPattern258",
    ends={
        Property(name="#260", type=qvtcore_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="4259", type=BottomPattern, multiplicity=Multiplicity(1, 1))
    }
)
area279: BinaryAssociation = BinaryAssociation(
    name="area279",
    ends={
        Property(name="#281", type=qvtcore_GuardPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="4280", type=Area, multiplicity=Multiplicity(1, 1))
    }
)
value263: BinaryAssociation = BinaryAssociation(
    name="value263",
    ends={
        Property(name="OclExpression265", type=qvtcore_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcore_Assignment264", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
targetProperty266: BinaryAssociation = BinaryAssociation(
    name="targetProperty266",
    ends={
        Property(name="Property268", type=qvtcore_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcore_Assignment267", type=Property_, multiplicity=Multiplicity(1, 1))
    }
)
area269: BinaryAssociation = BinaryAssociation(
    name="area269",
    ends={
        Property(name="#271", type=qvtcore_BottomPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="4270", type=Area, multiplicity=Multiplicity(1, 1))
    }
)
assignment272: BinaryAssociation = BinaryAssociation(
    name="assignment272",
    ends={
        Property(name="#274", type=qvtcore_BottomPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="4273", type=Assignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
realizedVariable275: BinaryAssociation = BinaryAssociation(
    name="realizedVariable275",
    ends={
        Property(name="RealizedVariable", type=qvtcore_BottomPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcore_BottomPattern", type=RealizedVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enforcementOperation276: BinaryAssociation = BinaryAssociation(
    name="enforcementOperation276",
    ends={
        Property(name="#278", type=qvtcore_BottomPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="4277", type=EnforcementOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bottomPattern289: BinaryAssociation = BinaryAssociation(
    name="bottomPattern289",
    ends={
        Property(name="#291", type=qvtcore_EnforcementOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="4290", type=BottomPattern, multiplicity=Multiplicity(0, 1))
    }
)
specification282: BinaryAssociation = BinaryAssociation(
    name="specification282",
    ends={
        Property(name="Mapping", type=qvtcore_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcore_Mapping", type=Mapping, multiplicity=Multiplicity(0, 9999))
    }
)
local283: BinaryAssociation = BinaryAssociation(
    name="local283",
    ends={
        Property(name="#285", type=qvtcore_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="4284", type=Mapping, multiplicity=Multiplicity(0, 9999))
    }
)
context286: BinaryAssociation = BinaryAssociation(
    name="context286",
    ends={
        Property(name="#288", type=qvtcore_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="4287", type=Mapping, multiplicity=Multiplicity(0, 1))
    }
)
ownedTag297: BinaryAssociation = BinaryAssociation(
    name="ownedTag297",
    ends={
        Property(name="#299", type=qvtbase_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="2298", type=Tag, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operationCallExp292: BinaryAssociation = BinaryAssociation(
    name="operationCallExp292",
    ends={
        Property(name="OperationCallExp", type=qvtcore_EnforcementOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtcore_EnforcementOperation", type=OperationCallExp, multiplicity=Multiplicity(1, 1))
    }
)
rule293: BinaryAssociation = BinaryAssociation(
    name="rule293",
    ends={
        Property(name="#295", type=qvtbase_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="5294", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
typedModel296: BinaryAssociation = BinaryAssociation(
    name="typedModel296",
    ends={
        Property(name="TypedModel", type=qvtbase_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtbase_Domain", type=TypedModel, multiplicity=Multiplicity(1, 1))
    }
)
modelParameter300: BinaryAssociation = BinaryAssociation(
    name="modelParameter300",
    ends={
        Property(name="#302", type=qvtbase_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="5301", type=TypedModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rule303: BinaryAssociation = BinaryAssociation(
    name="rule303",
    ends={
        Property(name="#305", type=qvtbase_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="5304", type=Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extends306: BinaryAssociation = BinaryAssociation(
    name="extends306",
    ends={
        Property(name="Transformation307", type=qvtbase_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtbase_Transformation", type=Transformation, multiplicity=Multiplicity(0, 1))
    }
)
transformation308: BinaryAssociation = BinaryAssociation(
    name="transformation308",
    ends={
        Property(name="#310", type=qvtbase_TypedModel, multiplicity=Multiplicity(1, 1)),
        Property(name="5309", type=Transformation, multiplicity=Multiplicity(1, 1))
    }
)
usedPackage311: BinaryAssociation = BinaryAssociation(
    name="usedPackage311",
    ends={
        Property(name="Package312", type=qvtbase_TypedModel, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtbase_TypedModel", type=Package, multiplicity=Multiplicity(1, 9999))
    }
)
dependsOn313: BinaryAssociation = BinaryAssociation(
    name="dependsOn313",
    ends={
        Property(name="TypedModel315", type=qvtbase_TypedModel, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtbase_TypedModel314", type=TypedModel, multiplicity=Multiplicity(0, 9999))
    }
)
domain316: BinaryAssociation = BinaryAssociation(
    name="domain316",
    ends={
        Property(name="#318", type=qvtbase_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="5317", type=Domain, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bindsTo326: BinaryAssociation = BinaryAssociation(
    name="bindsTo326",
    ends={
        Property(name="qvtbase_Pattern", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="Variable327", type=qvtbase_Pattern, multiplicity=Multiplicity(1, 1))
    }
)
transformation319: BinaryAssociation = BinaryAssociation(
    name="transformation319",
    ends={
        Property(name="#321", type=qvtbase_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="5320", type=Transformation, multiplicity=Multiplicity(1, 1))
    }
)
overrides322: BinaryAssociation = BinaryAssociation(
    name="overrides322",
    ends={
        Property(name="Rule", type=qvtbase_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtbase_Rule", type=Rule, multiplicity=Multiplicity(0, 1))
    }
)
predicate323: BinaryAssociation = BinaryAssociation(
    name="predicate323",
    ends={
        Property(name="#325", type=qvtbase_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="5324", type=Predicate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pattern335: BinaryAssociation = BinaryAssociation(
    name="pattern335",
    ends={
        Property(name="#337", type=qvtbase_Predicate, multiplicity=Multiplicity(1, 1)),
        Property(name="5336", type=Pattern, multiplicity=Multiplicity(1, 1))
    }
)
whenOwner328: BinaryAssociation = BinaryAssociation(
    name="whenOwner328",
    ends={
        Property(name="#329", type=qvtbase_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="6", type=Relation, multiplicity=Multiplicity(0, 1))
    }
)
whereOwner330: BinaryAssociation = BinaryAssociation(
    name="whereOwner330",
    ends={
        Property(name="#332", type=qvtbase_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="6331", type=Relation, multiplicity=Multiplicity(0, 1))
    }
)
conditionExpression333: BinaryAssociation = BinaryAssociation(
    name="conditionExpression333",
    ends={
        Property(name="OclExpression334", type=qvtbase_Predicate, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtbase_Predicate", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
operationalImpl345: BinaryAssociation = BinaryAssociation(
    name="operationalImpl345",
    ends={
        Property(name="#347", type=qvtrelation_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="6346", type=RelationImplementation, multiplicity=Multiplicity(0, 9999))
    }
)
queryExpression338: BinaryAssociation = BinaryAssociation(
    name="queryExpression338",
    ends={
        Property(name="OclExpression339", type=qvtbase_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtbase_Function", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedKey340: BinaryAssociation = BinaryAssociation(
    name="ownedKey340",
    ends={
        Property(name="#342", type=qvtrelation_RelationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="6341", type=Key, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable343: BinaryAssociation = BinaryAssociation(
    name="variable343",
    ends={
        Property(name="Variable344", type=qvtrelation_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_Relation", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
impl362: BinaryAssociation = BinaryAssociation(
    name="impl362",
    ends={
        Property(name="Operation", type=qvtrelation_RelationImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_RelationImplementation", type=Operation, multiplicity=Multiplicity(1, 1))
    }
)
where348: BinaryAssociation = BinaryAssociation(
    name="where348",
    ends={
        Property(name="#350", type=qvtrelation_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="5349", type=Pattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
when351: BinaryAssociation = BinaryAssociation(
    name="when351",
    ends={
        Property(name="#353", type=qvtrelation_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="5352", type=Pattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pattern354: BinaryAssociation = BinaryAssociation(
    name="pattern354",
    ends={
        Property(name="DomainPattern", type=qvtrelation_RelationDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_RelationDomain", type=DomainPattern, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rootVariable355: BinaryAssociation = BinaryAssociation(
    name="rootVariable355",
    ends={
        Property(name="Variable357", type=qvtrelation_RelationDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_RelationDomain356", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
templateExpression358: BinaryAssociation = BinaryAssociation(
    name="templateExpression358",
    ends={
        Property(name="TemplateExp", type=qvtrelation_DomainPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_DomainPattern", type=TemplateExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
relation359: BinaryAssociation = BinaryAssociation(
    name="relation359",
    ends={
        Property(name="#361", type=qvtrelation_RelationImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="6360", type=Relation, multiplicity=Multiplicity(0, 1))
    }
)
inDirectionOf363: BinaryAssociation = BinaryAssociation(
    name="inDirectionOf363",
    ends={
        Property(name="TypedModel365", type=qvtrelation_RelationImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_RelationImplementation364", type=TypedModel, multiplicity=Multiplicity(1, 1))
    }
)
identifies366: BinaryAssociation = BinaryAssociation(
    name="identifies366",
    ends={
        Property(name="Class367", type=qvtrelation_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_Key", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
part368: BinaryAssociation = BinaryAssociation(
    name="part368",
    ends={
        Property(name="Property370", type=qvtrelation_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="qvtrelation_Key369", type=Property_, multiplicity=Multiplicity(1, 9999))
    }
)
transformation371: BinaryAssociation = BinaryAssociation(
    name="transformation371",
    ends={
        Property(name="#373", type=qvtrelation_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="6372", type=RelationalTransformation, multiplicity=Multiplicity(0, 1))
    }
)
source374: BinaryAssociation = BinaryAssociation(
    name="source374",
    ends={
        Property(name="OclExpression375", type=essentialocl_CallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_CallExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tryBodyOwner376: BinaryAssociation = BinaryAssociation(
    name="tryBodyOwner376",
    ends={
        Property(name="#377", type=essentialocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="1", type=TryExp, multiplicity=Multiplicity(0, 1))
    }
)
condition378: BinaryAssociation = BinaryAssociation(
    name="condition378",
    ends={
        Property(name="OclExpression379", type=essentialocl_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_IfExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression380: BinaryAssociation = BinaryAssociation(
    name="thenExpression380",
    ends={
        Property(name="OclExpression382", type=essentialocl_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_IfExp381", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initExpression391: BinaryAssociation = BinaryAssociation(
    name="initExpression391",
    ends={
        Property(name="OclExpression392", type=essentialocl_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_Variable", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseExpression383: BinaryAssociation = BinaryAssociation(
    name="elseExpression383",
    ends={
        Property(name="OclExpression385", type=essentialocl_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_IfExp384", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
in386: BinaryAssociation = BinaryAssociation(
    name="in386",
    ends={
        Property(name="OclExpression387", type=essentialocl_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_LetExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable388: BinaryAssociation = BinaryAssociation(
    name="variable388",
    ends={
        Property(name="#390", type=essentialocl_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="7389", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referredType405: BinaryAssociation = BinaryAssociation(
    name="referredType405",
    ends={
        Property(name="Type406", type=essentialocl_TypeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_TypeExp", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
LetExp393: BinaryAssociation = BinaryAssociation(
    name="LetExp393",
    ends={
        Property(name="#395", type=essentialocl_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="7394", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
computeOwner396: BinaryAssociation = BinaryAssociation(
    name="computeOwner396",
    ends={
        Property(name="#398", type=essentialocl_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="1397", type=ComputeExp, multiplicity=Multiplicity(0, 1))
    }
)
bindParameter399: BinaryAssociation = BinaryAssociation(
    name="bindParameter399",
    ends={
        Property(name="Parameter", type=essentialocl_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_Variable400", type=Parameter_, multiplicity=Multiplicity(0, 1))
    }
)
referredProperty401: BinaryAssociation = BinaryAssociation(
    name="referredProperty401",
    ends={
        Property(name="Property402", type=essentialocl_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_PropertyCallExp", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
referredVariable403: BinaryAssociation = BinaryAssociation(
    name="referredVariable403",
    ends={
        Property(name="Variable404", type=essentialocl_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_VariableExp", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
body407: BinaryAssociation = BinaryAssociation(
    name="body407",
    ends={
        Property(name="OclExpression408", type=essentialocl_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_LoopExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterator409: BinaryAssociation = BinaryAssociation(
    name="iterator409",
    ends={
        Property(name="Variable411", type=essentialocl_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_LoopExp410", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
result417: BinaryAssociation = BinaryAssociation(
    name="result417",
    ends={
        Property(name="Variable418", type=essentialocl_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_IterateExp", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
argument412: BinaryAssociation = BinaryAssociation(
    name="argument412",
    ends={
        Property(name="OclExpression413", type=essentialocl_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_OperationCallExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredOperation414: BinaryAssociation = BinaryAssociation(
    name="referredOperation414",
    ends={
        Property(name="Operation416", type=essentialocl_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_OperationCallExp415", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
part419: BinaryAssociation = BinaryAssociation(
    name="part419",
    ends={
        Property(name="#421", type=essentialocl_CollectionLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="7420", type=CollectionLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
CollectionLiteralExp422: BinaryAssociation = BinaryAssociation(
    name="CollectionLiteralExp422",
    ends={
        Property(name="#424", type=essentialocl_CollectionLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="7423", type=CollectionLiteralExp, multiplicity=Multiplicity(1, 1))
    }
)
item425: BinaryAssociation = BinaryAssociation(
    name="item425",
    ends={
        Property(name="OclExpression426", type=essentialocl_CollectionItem, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_CollectionItem", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
first427: BinaryAssociation = BinaryAssociation(
    name="first427",
    ends={
        Property(name="OclExpression428", type=essentialocl_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_CollectionRange", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
last429: BinaryAssociation = BinaryAssociation(
    name="last429",
    ends={
        Property(name="OclExpression431", type=essentialocl_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_CollectionRange430", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
part432: BinaryAssociation = BinaryAssociation(
    name="part432",
    ends={
        Property(name="#434", type=essentialocl_TupleLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="7433", type=TupleLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyExpression435: BinaryAssociation = BinaryAssociation(
    name="bodyExpression435",
    ends={
        Property(name="OclExpression436", type=essentialocl_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_ExpressionInOcl", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context437: BinaryAssociation = BinaryAssociation(
    name="context437",
    ends={
        Property(name="Variable439", type=essentialocl_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_ExpressionInOcl438", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resultVariable440: BinaryAssociation = BinaryAssociation(
    name="resultVariable440",
    ends={
        Property(name="Variable442", type=essentialocl_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_ExpressionInOcl441", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterVariable443: BinaryAssociation = BinaryAssociation(
    name="parameterVariable443",
    ends={
        Property(name="Variable445", type=essentialocl_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_ExpressionInOcl444", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TupleLiteralExp446: BinaryAssociation = BinaryAssociation(
    name="TupleLiteralExp446",
    ends={
        Property(name="#448", type=essentialocl_TupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="7447", type=TupleLiteralExp, multiplicity=Multiplicity(0, 1))
    }
)
attribute449: BinaryAssociation = BinaryAssociation(
    name="attribute449",
    ends={
        Property(name="Property450", type=essentialocl_TupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_TupleLiteralPart", type=Property_, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elementType451: BinaryAssociation = BinaryAssociation(
    name="elementType451",
    ends={
        Property(name="Type452", type=essentialocl_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_CollectionType", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
referredEnumLiteral453: BinaryAssociation = BinaryAssociation(
    name="referredEnumLiteral453",
    ends={
        Property(name="EnumerationLiteral", type=essentialocl_EnumLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="essentialocl_EnumLiteralExp", type=EnumerationLiteral, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_qvttemplate_TemplateExp_LiteralExp = Generalization(general=LiteralExp, specific=qvttemplate_TemplateExp)
gen_qvttemplate_PropertyTemplateItem_Element = Generalization(general=Element, specific=qvttemplate_PropertyTemplateItem)
gen_qvttemplate_ObjectTemplateExp_TemplateExp = Generalization(general=TemplateExp, specific=qvttemplate_ObjectTemplateExp)
gen_qvttemplate_CollectionTemplateExp_TemplateExp = Generalization(general=TemplateExp, specific=qvttemplate_CollectionTemplateExp)
gen_imperativeocl_BlockExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_BlockExp)
gen_imperativeocl_ImperativeIterateExp_ImperativeLoopExp = Generalization(general=ImperativeLoopExp, specific=imperativeocl_ImperativeIterateExp)
gen_imperativeocl_AssignExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_AssignExp)
gen_imperativeocl_ComputeExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_ComputeExp)
gen_imperativeocl_SwitchExp_CallExp = Generalization(general=CallExp, specific=imperativeocl_SwitchExp)
gen_imperativeocl_SwitchExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_SwitchExp)
gen_imperativeocl_VariableInitExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_VariableInitExp)
gen_imperativeocl_WhileExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_WhileExp)
gen_imperativeocl_ReturnExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_ReturnExp)
gen_imperativeocl_AltExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_AltExp)
gen_imperativeocl_UnlinkExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_UnlinkExp)
gen_imperativeocl_TupleExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_TupleExp)
gen_imperativeocl_Typedef_Class = Generalization(general=Class_, specific=imperativeocl_Typedef)
gen_imperativeocl_BreakExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_BreakExp)
gen_imperativeocl_TryExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_TryExp)
gen_imperativeocl_RaiseExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_RaiseExp)
gen_imperativeocl_ContinueExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_ContinueExp)
gen_imperativeocl_ForExp_ImperativeLoopExp = Generalization(general=ImperativeLoopExp, specific=imperativeocl_ForExp)
gen_imperativeocl_DictionaryType_CollectionType = Generalization(general=CollectionType, specific=imperativeocl_DictionaryType)
gen_imperativeocl_InstantiationExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_InstantiationExp)
gen_imperativeocl_DictLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=imperativeocl_DictLiteralExp)
gen_imperativeocl_DictLiteralPart_Element = Generalization(general=Element, specific=imperativeocl_DictLiteralPart)
gen_imperativeocl_AssertExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_AssertExp)
gen_imperativeocl_TemplateParameterType_Type = Generalization(general=Type, specific=imperativeocl_TemplateParameterType)
gen_imperativeocl_LogExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_LogExp)
gen_imperativeocl_CollectorExp_ImperativeLoopExp = Generalization(general=ImperativeLoopExp, specific=imperativeocl_CollectorExp)
gen_imperativeocl_ImperativeExpression_OclExpression = Generalization(general=OclExpression, specific=imperativeocl_ImperativeExpression)
gen_imperativeocl_UnpackExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_UnpackExp)
gen_imperativeocl_AnonymousTupleType_Class = Generalization(general=Class_, specific=imperativeocl_AnonymousTupleType)
gen_imperativeocl_AnonymousTupleLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=imperativeocl_AnonymousTupleLiteralExp)
gen_imperativeocl_ImperativeLoopExp_LoopExp = Generalization(general=LoopExp, specific=imperativeocl_ImperativeLoopExp)
gen_imperativeocl_ImperativeLoopExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=imperativeocl_ImperativeLoopExp)
gen_imperativeocl_ListType_CollectionType = Generalization(general=CollectionType, specific=imperativeocl_ListType)
gen_emof_Class_Type = Generalization(general=Type, specific=emof_Class)
gen_imperativeocl_AnonymousTupleLiteralPart_Element = Generalization(general=Element, specific=imperativeocl_AnonymousTupleLiteralPart)
gen_emof_DataType_Type = Generalization(general=Type, specific=emof_DataType)
gen_emof_Element_Object = Generalization(general=Object, specific=emof_Element)
gen_emof_Tag_Element = Generalization(general=Element, specific=emof_Tag)
gen_emof_Enumeration_DataType = Generalization(general=DataType, specific=emof_Enumeration)
gen_emof_NamedElement_Element = Generalization(general=Element, specific=emof_NamedElement)
gen_emof_Extent_Object = Generalization(general=Object, specific=emof_Extent)
gen_emof_Operation_MultiplicityElement = Generalization(general=MultiplicityElement, specific=emof_Operation)
gen_emof_Operation_TypedElement = Generalization(general=TypedElement, specific=emof_Operation)
gen_emof_EnumerationLiteral_NamedElement = Generalization(general=NamedElement, specific=emof_EnumerationLiteral)
gen_emof_Package_NamedElement = Generalization(general=NamedElement, specific=emof_Package)
gen_emof_Type_NamedElement = Generalization(general=NamedElement, specific=emof_Type)
gen_emof_Parameter_MultiplicityElement = Generalization(general=MultiplicityElement, specific=emof_Parameter)
gen_emof_Parameter_TypedElement = Generalization(general=TypedElement, specific=emof_Parameter)
gen_emof_URIExtent_Extent = Generalization(general=Extent, specific=emof_URIExtent)
gen_emof_Property_MultiplicityElement = Generalization(general=MultiplicityElement, specific=emof_Property)
gen_emof_Property_TypedElement = Generalization(general=TypedElement, specific=emof_Property)
gen_emof_TypedElement_NamedElement = Generalization(general=NamedElement, specific=emof_TypedElement)
gen_emof_PrimitiveType_DataType = Generalization(general=DataType, specific=emof_PrimitiveType)
gen_qvtoperational_OperationalTransformation_Module = Generalization(general=Module, specific=qvtoperational_OperationalTransformation)
gen_emof_Comment_Element = Generalization(general=Element, specific=emof_Comment)
gen_qvtoperational_MappingBody_OperationBody = Generalization(general=OperationBody, specific=qvtoperational_MappingBody)
gen_qvtoperational_Helper_ImperativeOperation = Generalization(general=ImperativeOperation, specific=qvtoperational_Helper)
gen_qvtoperational_ResolveExp_CallExp = Generalization(general=CallExp, specific=qvtoperational_ResolveExp)
gen_qvtoperational_ResolveInExp_ResolveExp = Generalization(general=ResolveExp, specific=qvtoperational_ResolveInExp)
gen_qvtoperational_MappingOperation_NamedElement = Generalization(general=NamedElement, specific=qvtoperational_MappingOperation)
gen_qvtoperational_MappingParameter_VarParameter = Generalization(general=VarParameter, specific=qvtoperational_MappingParameter)
gen_qvtoperational_MappingOperation_ImperativeOperation = Generalization(general=ImperativeOperation, specific=qvtoperational_MappingOperation)
gen_qvtoperational_MappingOperation_Operation = Generalization(general=Operation, specific=qvtoperational_MappingOperation)
gen_qvtoperational_MappingCallExp_ImperativeCallExp = Generalization(general=ImperativeCallExp, specific=qvtoperational_MappingCallExp)
gen_qvtoperational_Constructor_ImperativeOperation = Generalization(general=ImperativeOperation, specific=qvtoperational_Constructor)
gen_qvtoperational_ContextualProperty_Property = Generalization(general=Property_, specific=qvtoperational_ContextualProperty)
gen_qvtoperational_Library_Module = Generalization(general=Module, specific=qvtoperational_Library)
gen_qvtoperational_EntryOperation_ImperativeOperation = Generalization(general=ImperativeOperation, specific=qvtoperational_EntryOperation)
gen_qvtoperational_ImperativeCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=qvtoperational_ImperativeCallExp)
gen_qvtoperational_ImperativeOperation_Operation = Generalization(general=Operation, specific=qvtoperational_ImperativeOperation)
gen_qvtoperational_ModelParameter_VarParameter = Generalization(general=VarParameter, specific=qvtoperational_ModelParameter)
gen_qvtoperational_ModelType_Class = Generalization(general=Class_, specific=qvtoperational_ModelType)
gen_qvtoperational_ModelType_URIExtent = Generalization(general=URIExtent, specific=qvtoperational_ModelType)
gen_qvtoperational_Module_Class = Generalization(general=Class_, specific=qvtoperational_Module)
gen_qvtoperational_Module_Package = Generalization(general=Package, specific=qvtoperational_Module)
gen_qvtoperational_ModuleImport_Element = Generalization(general=Element, specific=qvtoperational_ModuleImport)
gen_qvtoperational_VarParameter_Parameter = Generalization(general=Parameter_, specific=qvtoperational_VarParameter)
gen_qvtoperational_VarParameter_Variable = Generalization(general=Variable, specific=qvtoperational_VarParameter)
gen_qvtoperational_OperationBody_Element = Generalization(general=Element, specific=qvtoperational_OperationBody)
gen_qvtoperational_ConstructorBody_OperationBody = Generalization(general=OperationBody, specific=qvtoperational_ConstructorBody)
gen_qvtoperational_ObjectExp_InstantiationExp = Generalization(general=InstantiationExp, specific=qvtoperational_ObjectExp)
gen_qvtcore_GuardPattern_CorePattern = Generalization(general=CorePattern, specific=qvtcore_GuardPattern)
gen_qvtcore_BottomPattern_CorePattern = Generalization(general=CorePattern, specific=qvtcore_BottomPattern)
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
gen_qvtbase_Pattern_Element = Generalization(general=Element, specific=qvtbase_Pattern)
gen_qvtbase_Predicate_Element = Generalization(general=Element, specific=qvtbase_Predicate)
gen_qvtbase_Function_Operation = Generalization(general=Operation, specific=qvtbase_Function)
gen_qvtbase_FunctionParameter_Parameter = Generalization(general=Parameter_, specific=qvtbase_FunctionParameter)
gen_qvtbase_FunctionParameter_Variable = Generalization(general=Variable, specific=qvtbase_FunctionParameter)
gen_qvtrelation_RelationalTransformation_Transformation = Generalization(general=Transformation, specific=qvtrelation_RelationalTransformation)
gen_qvtrelation_Relation_Rule = Generalization(general=Rule, specific=qvtrelation_Relation)
gen_qvtrelation_RelationDomain_Domain = Generalization(general=Domain, specific=qvtrelation_RelationDomain)
gen_qvtrelation_DomainPattern_Pattern = Generalization(general=Pattern, specific=qvtrelation_DomainPattern)
gen_qvtrelation_RelationImplementation_Element = Generalization(general=Element, specific=qvtrelation_RelationImplementation)
gen_qvtrelation_Key_Element = Generalization(general=Element, specific=qvtrelation_Key)
gen_essentialocl_BooleanLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=essentialocl_BooleanLiteralExp)
gen_essentialocl_CallExp_OclExpression = Generalization(general=OclExpression, specific=essentialocl_CallExp)
gen_essentialocl_OclExpression_TypedElement = Generalization(general=TypedElement, specific=essentialocl_OclExpression)
gen_essentialocl_UnlimitedNaturalExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=essentialocl_UnlimitedNaturalExp)
gen_essentialocl_IfExp_OclExpression = Generalization(general=OclExpression, specific=essentialocl_IfExp)
gen_essentialocl_LetExp_OclExpression = Generalization(general=OclExpression, specific=essentialocl_LetExp)
gen_essentialocl_Variable_TypedElement = Generalization(general=TypedElement, specific=essentialocl_Variable)
gen_essentialocl_PropertyCallExp_FeaturePropertyCall = Generalization(general=FeaturePropertyCall, specific=essentialocl_PropertyCallExp)
gen_essentialocl_VariableExp_OclExpression = Generalization(general=OclExpression, specific=essentialocl_VariableExp)
gen_essentialocl_TypeExp_OclExpression = Generalization(general=OclExpression, specific=essentialocl_TypeExp)
gen_essentialocl_IntegerLiteralExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=essentialocl_IntegerLiteralExp)
gen_essentialocl_LoopExp_CallExp = Generalization(general=CallExp, specific=essentialocl_LoopExp)
gen_essentialocl_LoopExp_OclExpression = Generalization(general=OclExpression, specific=essentialocl_LoopExp)
gen_essentialocl_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=essentialocl_IteratorExp)
gen_essentialocl_StringLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=essentialocl_StringLiteralExp)
gen_essentialocl_OperationCallExp_FeaturePropertyCall = Generalization(general=FeaturePropertyCall, specific=essentialocl_OperationCallExp)
gen_essentialocl_RealLiteralExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=essentialocl_RealLiteralExp)
gen_essentialocl_LiteralExp_OclExpression = Generalization(general=OclExpression, specific=essentialocl_LiteralExp)
gen_essentialocl_IterateExp_LoopExp = Generalization(general=LoopExp, specific=essentialocl_IterateExp)
gen_essentialocl_PrimitiveLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=essentialocl_PrimitiveLiteralExp)
gen_essentialocl_NumericLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=essentialocl_NumericLiteralExp)
gen_essentialocl_CollectionLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=essentialocl_CollectionLiteralExp)
gen_essentialocl_CollectionLiteralPart_TypedElement = Generalization(general=TypedElement, specific=essentialocl_CollectionLiteralPart)
gen_essentialocl_CollectionItem_CollectionLiteralPart = Generalization(general=CollectionLiteralPart, specific=essentialocl_CollectionItem)
gen_essentialocl_CollectionRange_CollectionLiteralPart = Generalization(general=CollectionLiteralPart, specific=essentialocl_CollectionRange)
gen_essentialocl_TupleLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=essentialocl_TupleLiteralExp)
gen_essentialocl_NullLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=essentialocl_NullLiteralExp)
gen_essentialocl_ExpressionInOcl_OpaqueExpression = Generalization(general=OpaqueExpression, specific=essentialocl_ExpressionInOcl)
gen_essentialocl_BagType_CollectionType = Generalization(general=CollectionType, specific=essentialocl_BagType)
gen_essentialocl_CollectionType_DataType = Generalization(general=DataType, specific=essentialocl_CollectionType)
gen_essentialocl_InvalidLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=essentialocl_InvalidLiteralExp)
gen_essentialocl_FeaturePropertyCall_CallExp = Generalization(general=CallExp, specific=essentialocl_FeaturePropertyCall)
gen_essentialocl_TupleLiteralPart_TypedElement = Generalization(general=TypedElement, specific=essentialocl_TupleLiteralPart)
gen_essentialocl_EnumLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=essentialocl_EnumLiteralExp)
gen_essentialocl_InvalidType_Type = Generalization(general=Type, specific=essentialocl_InvalidType)
gen_essentialocl_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=essentialocl_OrderedSetType)
gen_essentialocl_SequenceType_CollectionType = Generalization(general=CollectionType, specific=essentialocl_SequenceType)
gen_essentialocl_SetType_CollectionType = Generalization(general=CollectionType, specific=essentialocl_SetType)
gen_essentialocl_TupleType_Class = Generalization(general=Class_, specific=essentialocl_TupleType)
gen_essentialocl_TupleType_DataType = Generalization(general=DataType, specific=essentialocl_TupleType)
gen_essentialocl_VoidType_Type = Generalization(general=Type, specific=essentialocl_VoidType)
gen_essentialocl_AnyType_Class = Generalization(general=Class_, specific=essentialocl_AnyType)
gen_essentialocl_AnyType_Type = Generalization(general=Type, specific=essentialocl_AnyType)

# Domain Model
domain_model = DomainModel(
    name="essentialocl",
    types={Variable, OclExpression, qvttemplate_TemplateExp, LiteralExp, qvttemplate_PropertyTemplateItem, Element, ObjectTemplateExp, qvttemplate_ObjectTemplateExp, TemplateExp, PropertyTemplateItem, Class_, qvttemplate_CollectionTemplateExp, CollectionType, imperativeocl_BlockExp, Property_, imperativeocl_ImperativeIterateExp, ImperativeLoopExp, imperativeocl_AssignExp, ImperativeExpression, imperativeocl_ComputeExp, imperativeocl_SwitchExp, CallExp, AltExp, imperativeocl_VariableInitExp, imperativeocl_WhileExp, imperativeocl_ReturnExp, imperativeocl_AltExp, imperativeocl_UnlinkExp, imperativeocl_TupleExp, imperativeocl_Typedef, imperativeocl_BreakExp, imperativeocl_TryExp, Type, imperativeocl_RaiseExp, imperativeocl_ContinueExp, imperativeocl_ForExp, imperativeocl_DictionaryType, imperativeocl_InstantiationExp, imperativeocl_DictLiteralExp, DictLiteralPart, imperativeocl_DictLiteralPart, imperativeocl_AssertExp, LogExp, imperativeocl_TemplateParameterType, imperativeocl_LogExp, imperativeocl_CollectorExp, imperativeocl_ImperativeExpression, imperativeocl_UnpackExp, imperativeocl_AnonymousTupleType, imperativeocl_AnonymousTupleLiteralExp, AnonymousTupleLiteralPart, imperativeocl_ImperativeLoopExp, LoopExp, imperativeocl_ListType, emof_Class, Operation, imperativeocl_AnonymousTupleLiteralPart, emof_DataType, emof_Element, Object, Tag, emof_Tag, Transformation, Module, Comment, emof_Enumeration, DataType, EnumerationLiteral, emof_NamedElement, emof_Extent, emof_Object, emof_Operation, MultiplicityElement, TypedElement, Parameter_, emof_MultiplicityElement, emof_EnumerationLiteral, emof_Package, NamedElement, Package, emof_Type, emof_Parameter, Extent, Enumeration_, emof_Property, emof_TypedElement, emof_PrimitiveType, emof_URIExtent, emof_Comment, qvtoperational_MappingBody, OperationBody, qvtoperational_Helper, ImperativeOperation, qvtoperational_ResolveExp, qvtoperational_ResolveInExp, ResolveExp, MappingOperation, qvtoperational_OperationalTransformation, ModelParameter, EntryOperation, Relation, qvtoperational_MappingParameter, VarParameter, RelationDomain, qvtoperational_MappingOperation, qvtoperational_MappingCallExp, ImperativeCallExp, qvtoperational_Constructor, qvtoperational_ContextualProperty, qvtoperational_Library, qvtoperational_EntryOperation, qvtoperational_ImperativeCallExp, OperationCallExp, qvtoperational_ImperativeOperation, ModelType, qvtoperational_ModelParameter, qvtoperational_ModelType, URIExtent, qvtoperational_Module, ModuleImport, qvtoperational_ModuleImport, qvtoperational_VarParameter, qvtoperational_OperationBody, qvtoperational_ConstructorBody, qvtoperational_ObjectExp, InstantiationExp, ConstructorBody, qvtcore_Area, GuardPattern, BottomPattern, qvtcore_Assignment, qvtcore_BottomPattern, CorePattern, Area, Assignment, RealizedVariable, EnforcementOperation, qvtcore_GuardPattern, qvtcore_Mapping, Rule, Mapping, qvtcore_RealizedVariable, qvtcore_CoreDomain, Domain, qvtcore_CorePattern, Pattern, qvtcore_EnforcementOperation, qvtbase_Domain, TypedModel, qvtbase_Transformation, qvtbase_TypedModel, qvtbase_Rule, qvtbase_Pattern, Predicate, qvtbase_Predicate, qvtbase_Function, qvtbase_FunctionParameter, qvtrelation_RelationalTransformation, Key, qvtrelation_Relation, RelationImplementation, qvtrelation_RelationDomain, DomainPattern, qvtrelation_DomainPattern, qvtrelation_RelationImplementation, qvtrelation_Key, RelationalTransformation, essentialocl_BooleanLiteralExp, PrimitiveLiteralExp, essentialocl_CallExp, essentialocl_OclExpression, TryExp, essentialocl_UnlimitedNaturalExp, NumericLiteralExp, essentialocl_IfExp, essentialocl_LetExp, essentialocl_Variable, LetExp, ComputeExp, essentialocl_PropertyCallExp, FeaturePropertyCall, essentialocl_VariableExp, essentialocl_TypeExp, essentialocl_IntegerLiteralExp, essentialocl_LoopExp, essentialocl_IteratorExp, essentialocl_StringLiteralExp, essentialocl_OperationCallExp, essentialocl_RealLiteralExp, essentialocl_LiteralExp, essentialocl_IterateExp, essentialocl_PrimitiveLiteralExp, essentialocl_NumericLiteralExp, essentialocl_CollectionLiteralExp, CollectionLiteralPart, essentialocl_CollectionLiteralPart, CollectionLiteralExp, essentialocl_CollectionItem, essentialocl_CollectionRange, essentialocl_TupleLiteralExp, TupleLiteralPart, essentialocl_NullLiteralExp, essentialocl_ExpressionInOcl, OpaqueExpression, essentialocl_BagType, essentialocl_CollectionType, essentialocl_OpaqueExpression, essentialocl_InvalidLiteralExp, essentialocl_FeaturePropertyCall, essentialocl_TupleLiteralPart, TupleLiteralExp, essentialocl_EnumLiteralExp, essentialocl_InvalidType, essentialocl_OrderedSetType, essentialocl_SequenceType, essentialocl_SetType, essentialocl_TupleType, essentialocl_VoidType, essentialocl_AnyType, SeverityKind, DirectionKind, ImportKind, EnforcementMode, CollectionKind},
    associations={bindsTo0, where1, match9, objContainer12, part3, referredClass4, part5, referredCollectionType7, defaultValue26, value15, referredProperty17, target19, value21, left23, body39, body29, alternativePart31, elsePart32, referredVariable35, condition37, value56, returnedElement42, body44, condition46, body48, target51, item53, element67, tryBody58, exception61, exceptBody62, exception65, argument79, keyType82, base69, condition71, instantiatedClass74, extent76, part84, key85, condition90, value87, element92, log94, assertion95, target100, variable102, elementType104, condition98, ownedAttribute109, ownedOperation111, part106, value107, superClass113, ownedComment119, element120, transformation123, tag116, ownedLiteral127, owner125, class130, ownedParameter133, raisedException136, ownedType138, nestedPackage141, package142, operation145, enumeration148, class151, opposite153, module156, type159, intermediateClass170, annotatedElement161, initSection162, endSection164, condition167, inMapping169, disjunct187, refined172, intermediateProperty174, modelParameter177, entry179, relation181, refinedDomain183, extent184, overridden203, refinedRelation189, merged192, inherited195, when198, context201, context206, result209, overridden212, body213, metamodel216, additionalCondition218, ownedTag221, configProperty224, moduleImport227, usedModelType230, binding231, module233, importedModule236, content247, ctxOwner238, resOwner241, operation244, slotExpression261, referredObject249, body251, guardPattern253, bottomPattern255, bottomPattern258, area279, value263, targetProperty266, area269, assignment272, realizedVariable275, enforcementOperation276, bottomPattern289, specification282, local283, context286, ownedTag297, operationCallExp292, rule293, typedModel296, modelParameter300, rule303, extends306, transformation308, usedPackage311, dependsOn313, domain316, bindsTo326, transformation319, overrides322, predicate323, pattern335, whenOwner328, whereOwner330, conditionExpression333, operationalImpl345, queryExpression338, ownedKey340, variable343, impl362, where348, when351, pattern354, rootVariable355, templateExpression358, relation359, inDirectionOf363, identifies366, part368, transformation371, source374, tryBodyOwner376, condition378, thenExpression380, initExpression391, elseExpression383, in386, variable388, referredType405, LetExp393, computeOwner396, bindParameter399, referredProperty401, referredVariable403, body407, iterator409, result417, argument412, referredOperation414, part419, CollectionLiteralExp422, item425, first427, last429, part432, bodyExpression435, context437, resultVariable440, parameterVariable443, TupleLiteralExp446, attribute449, elementType451, referredEnumLiteral453},
    generalizations={gen_qvttemplate_TemplateExp_LiteralExp, gen_qvttemplate_PropertyTemplateItem_Element, gen_qvttemplate_ObjectTemplateExp_TemplateExp, gen_qvttemplate_CollectionTemplateExp_TemplateExp, gen_imperativeocl_BlockExp_ImperativeExpression, gen_imperativeocl_ImperativeIterateExp_ImperativeLoopExp, gen_imperativeocl_AssignExp_ImperativeExpression, gen_imperativeocl_ComputeExp_ImperativeExpression, gen_imperativeocl_SwitchExp_CallExp, gen_imperativeocl_SwitchExp_ImperativeExpression, gen_imperativeocl_VariableInitExp_ImperativeExpression, gen_imperativeocl_WhileExp_ImperativeExpression, gen_imperativeocl_ReturnExp_ImperativeExpression, gen_imperativeocl_AltExp_ImperativeExpression, gen_imperativeocl_UnlinkExp_ImperativeExpression, gen_imperativeocl_TupleExp_ImperativeExpression, gen_imperativeocl_Typedef_Class, gen_imperativeocl_BreakExp_ImperativeExpression, gen_imperativeocl_TryExp_ImperativeExpression, gen_imperativeocl_RaiseExp_ImperativeExpression, gen_imperativeocl_ContinueExp_ImperativeExpression, gen_imperativeocl_ForExp_ImperativeLoopExp, gen_imperativeocl_DictionaryType_CollectionType, gen_imperativeocl_InstantiationExp_ImperativeExpression, gen_imperativeocl_DictLiteralExp_LiteralExp, gen_imperativeocl_DictLiteralPart_Element, gen_imperativeocl_AssertExp_ImperativeExpression, gen_imperativeocl_TemplateParameterType_Type, gen_imperativeocl_LogExp_ImperativeExpression, gen_imperativeocl_CollectorExp_ImperativeLoopExp, gen_imperativeocl_ImperativeExpression_OclExpression, gen_imperativeocl_UnpackExp_ImperativeExpression, gen_imperativeocl_AnonymousTupleType_Class, gen_imperativeocl_AnonymousTupleLiteralExp_LiteralExp, gen_imperativeocl_ImperativeLoopExp_LoopExp, gen_imperativeocl_ImperativeLoopExp_ImperativeExpression, gen_imperativeocl_ListType_CollectionType, gen_emof_Class_Type, gen_imperativeocl_AnonymousTupleLiteralPart_Element, gen_emof_DataType_Type, gen_emof_Element_Object, gen_emof_Tag_Element, gen_emof_Enumeration_DataType, gen_emof_NamedElement_Element, gen_emof_Extent_Object, gen_emof_Operation_MultiplicityElement, gen_emof_Operation_TypedElement, gen_emof_EnumerationLiteral_NamedElement, gen_emof_Package_NamedElement, gen_emof_Type_NamedElement, gen_emof_Parameter_MultiplicityElement, gen_emof_Parameter_TypedElement, gen_emof_URIExtent_Extent, gen_emof_Property_MultiplicityElement, gen_emof_Property_TypedElement, gen_emof_TypedElement_NamedElement, gen_emof_PrimitiveType_DataType, gen_qvtoperational_OperationalTransformation_Module, gen_emof_Comment_Element, gen_qvtoperational_MappingBody_OperationBody, gen_qvtoperational_Helper_ImperativeOperation, gen_qvtoperational_ResolveExp_CallExp, gen_qvtoperational_ResolveInExp_ResolveExp, gen_qvtoperational_MappingOperation_NamedElement, gen_qvtoperational_MappingParameter_VarParameter, gen_qvtoperational_MappingOperation_ImperativeOperation, gen_qvtoperational_MappingOperation_Operation, gen_qvtoperational_MappingCallExp_ImperativeCallExp, gen_qvtoperational_Constructor_ImperativeOperation, gen_qvtoperational_ContextualProperty_Property, gen_qvtoperational_Library_Module, gen_qvtoperational_EntryOperation_ImperativeOperation, gen_qvtoperational_ImperativeCallExp_OperationCallExp, gen_qvtoperational_ImperativeOperation_Operation, gen_qvtoperational_ModelParameter_VarParameter, gen_qvtoperational_ModelType_Class, gen_qvtoperational_ModelType_URIExtent, gen_qvtoperational_Module_Class, gen_qvtoperational_Module_Package, gen_qvtoperational_ModuleImport_Element, gen_qvtoperational_VarParameter_Parameter, gen_qvtoperational_VarParameter_Variable, gen_qvtoperational_OperationBody_Element, gen_qvtoperational_ConstructorBody_OperationBody, gen_qvtoperational_ObjectExp_InstantiationExp, gen_qvtcore_GuardPattern_CorePattern, gen_qvtcore_BottomPattern_CorePattern, gen_qvtcore_Mapping_Rule, gen_qvtcore_Mapping_Area, gen_qvtcore_RealizedVariable_Variable, gen_qvtcore_CoreDomain_Domain, gen_qvtcore_CoreDomain_Area, gen_qvtcore_CorePattern_Pattern, gen_qvtbase_Domain_NamedElement, gen_qvtbase_Transformation_Class, gen_qvtbase_Transformation_Package, gen_qvtbase_TypedModel_NamedElement, gen_qvtbase_Rule_NamedElement, gen_qvtbase_Pattern_Element, gen_qvtbase_Predicate_Element, gen_qvtbase_Function_Operation, gen_qvtbase_FunctionParameter_Parameter, gen_qvtbase_FunctionParameter_Variable, gen_qvtrelation_RelationalTransformation_Transformation, gen_qvtrelation_Relation_Rule, gen_qvtrelation_RelationDomain_Domain, gen_qvtrelation_DomainPattern_Pattern, gen_qvtrelation_RelationImplementation_Element, gen_qvtrelation_Key_Element, gen_essentialocl_BooleanLiteralExp_PrimitiveLiteralExp, gen_essentialocl_CallExp_OclExpression, gen_essentialocl_OclExpression_TypedElement, gen_essentialocl_UnlimitedNaturalExp_NumericLiteralExp, gen_essentialocl_IfExp_OclExpression, gen_essentialocl_LetExp_OclExpression, gen_essentialocl_Variable_TypedElement, gen_essentialocl_PropertyCallExp_FeaturePropertyCall, gen_essentialocl_VariableExp_OclExpression, gen_essentialocl_TypeExp_OclExpression, gen_essentialocl_IntegerLiteralExp_NumericLiteralExp, gen_essentialocl_LoopExp_CallExp, gen_essentialocl_LoopExp_OclExpression, gen_essentialocl_IteratorExp_LoopExp, gen_essentialocl_StringLiteralExp_PrimitiveLiteralExp, gen_essentialocl_OperationCallExp_FeaturePropertyCall, gen_essentialocl_RealLiteralExp_NumericLiteralExp, gen_essentialocl_LiteralExp_OclExpression, gen_essentialocl_IterateExp_LoopExp, gen_essentialocl_PrimitiveLiteralExp_LiteralExp, gen_essentialocl_NumericLiteralExp_PrimitiveLiteralExp, gen_essentialocl_CollectionLiteralExp_LiteralExp, gen_essentialocl_CollectionLiteralPart_TypedElement, gen_essentialocl_CollectionItem_CollectionLiteralPart, gen_essentialocl_CollectionRange_CollectionLiteralPart, gen_essentialocl_TupleLiteralExp_LiteralExp, gen_essentialocl_NullLiteralExp_LiteralExp, gen_essentialocl_ExpressionInOcl_OpaqueExpression, gen_essentialocl_BagType_CollectionType, gen_essentialocl_CollectionType_DataType, gen_essentialocl_InvalidLiteralExp_LiteralExp, gen_essentialocl_FeaturePropertyCall_CallExp, gen_essentialocl_TupleLiteralPart_TypedElement, gen_essentialocl_EnumLiteralExp_LiteralExp, gen_essentialocl_InvalidType_Type, gen_essentialocl_OrderedSetType_CollectionType, gen_essentialocl_SequenceType_CollectionType, gen_essentialocl_SetType_CollectionType, gen_essentialocl_TupleType_Class, gen_essentialocl_TupleType_DataType, gen_essentialocl_VoidType_Type, gen_essentialocl_AnyType_Class, gen_essentialocl_AnyType_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)