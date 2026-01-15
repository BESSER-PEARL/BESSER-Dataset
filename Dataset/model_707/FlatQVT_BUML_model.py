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
CollectionKind: Enumeration = Enumeration(
    name="CollectionKind",
    literals={
            EnumerationLiteral(name="Set"),
			EnumerationLiteral(name="OrderedSet"),
			EnumerationLiteral(name="Bag"),
			EnumerationLiteral(name="Sequence"),
			EnumerationLiteral(name="Collection")
    }
)

DirectionKind: Enumeration = Enumeration(
    name="DirectionKind",
    literals={
            EnumerationLiteral(name="in"),
			EnumerationLiteral(name="inout"),
			EnumerationLiteral(name="out")
    }
)

EnforcementMode: Enumeration = Enumeration(
    name="EnforcementMode",
    literals={
            EnumerationLiteral(name="Creation"),
			EnumerationLiteral(name="Deletion")
    }
)

ImportKind: Enumeration = Enumeration(
    name="ImportKind",
    literals={
            EnumerationLiteral(name="extension"),
			EnumerationLiteral(name="access")
    }
)

SeverityKind: Enumeration = Enumeration(
    name="SeverityKind",
    literals={
            EnumerationLiteral(name="error"),
			EnumerationLiteral(name="warning"),
			EnumerationLiteral(name="fatal")
    }
)

# Classes
FlatQVT_AltExp = Class(name="FlatQVT::AltExp")
ImperativeExpression = Class(name="ImperativeExpression")
OclExpression = Class(name="OclExpression")
FlatQVT_Area = Class(name="FlatQVT::Area", is_abstract=True)
BottomPattern = Class(name="BottomPattern")
GuardPattern = Class(name="GuardPattern")
FlatQVT_AssertExp = Class(name="FlatQVT::AssertExp")
FlatQVT_AnyType = Class(name="FlatQVT::AnyType")
Type = Class(name="Type")
FlatQVT_Assignment = Class(name="FlatQVT::Assignment", is_abstract=True)
Element = Class(name="Element")
LogExp = Class(name="LogExp")
FlatQVT_AssignExp = Class(name="FlatQVT::AssignExp")
FlatQVT_BagType = Class(name="FlatQVT::BagType")
CollectionType = Class(name="CollectionType")
FlatQVT_BlockExp = Class(name="FlatQVT::BlockExp")
FlatQVT_BooleanLiteralExp = Class(name="FlatQVT::BooleanLiteralExp")
PrimitiveLiteralExp = Class(name="PrimitiveLiteralExp")
FlatQVT_BottomPattern = Class(name="FlatQVT::BottomPattern")
CorePattern = Class(name="CorePattern")
RealizedVariable = Class(name="RealizedVariable")
FlatQVT_BreakExp = Class(name="FlatQVT::BreakExp")
FlatQVT_CallExp = Class(name="FlatQVT::CallExp", is_abstract=True)
Area = Class(name="Area")
Assignment = Class(name="Assignment")
EnforcementOperation = Class(name="EnforcementOperation")
FlatQVT_Class = Class(name="FlatQVT::Class")
Property_ = Class(name="Property")
Operation = Class(name="Operation")
Class_ = Class(name="Class")
FlatQVT_CatchExp = Class(name="FlatQVT::CatchExp")
FlatQVT_CollectionLiteralExp = Class(name="FlatQVT::CollectionLiteralExp")
LiteralExp = Class(name="LiteralExp")
FlatQVT_CollectionItem = Class(name="FlatQVT::CollectionItem")
CollectionLiteralPart = Class(name="CollectionLiteralPart")
CollectionLiteralExp = Class(name="CollectionLiteralExp")
FlatQVT_CollectionRange = Class(name="FlatQVT::CollectionRange")
FlatQVT_CollectionLiteralPart = Class(name="FlatQVT::CollectionLiteralPart", is_abstract=True)
TypedElement = Class(name="TypedElement")
Variable = Class(name="Variable")
FlatQVT_CollectionTemplateExp = Class(name="FlatQVT::CollectionTemplateExp")
TemplateExp = Class(name="TemplateExp")
NamedElement = Class(name="NamedElement")
FlatQVT_ComputeExp = Class(name="FlatQVT::ComputeExp")
FlatQVT_CollectionType = Class(name="FlatQVT::CollectionType")
DataType = Class(name="DataType")
FlatQVT_Comment = Class(name="FlatQVT::Comment")
FlatQVT_ConstructorBody = Class(name="FlatQVT::ConstructorBody")
OperationBody = Class(name="OperationBody")
FlatQVT_ContextualProperty = Class(name="FlatQVT::ContextualProperty")
FlatQVT_Constructor = Class(name="FlatQVT::Constructor")
ImperativeOperation = Class(name="ImperativeOperation")
FlatQVT_CoreDomain = Class(name="FlatQVT::CoreDomain")
Domain = Class(name="Domain")
FlatQVT_CorePattern = Class(name="FlatQVT::CorePattern")
Pattern = Class(name="Pattern")
FlatQVT_DataType = Class(name="FlatQVT::DataType")
FlatQVT_DictLiteralExp = Class(name="FlatQVT::DictLiteralExp")
FlatQVT_ContinueExp = Class(name="FlatQVT::ContinueExp")
FlatQVT_DictLiteralPart = Class(name="FlatQVT::DictLiteralPart")
DictLiteralPart = Class(name="DictLiteralPart")
FlatQVT_DictionaryType = Class(name="FlatQVT::DictionaryType")
FlatQVT_Domain = Class(name="FlatQVT::Domain", is_abstract=True)
Rule = Class(name="Rule")
TypedModel = Class(name="TypedModel")
FlatQVT_DomainPattern = Class(name="FlatQVT::DomainPattern")
FlatQVT_Element = Class(name="FlatQVT::Element", is_abstract=True)
Object = Class(name="Object")
Comment = Class(name="Comment")
FlatQVT_EnforcementOperation = Class(name="FlatQVT::EnforcementOperation")
OperationCallExp = Class(name="OperationCallExp")
FlatQVT_EntryOperation = Class(name="FlatQVT::EntryOperation")
FlatQVT_EnumLiteralExp = Class(name="FlatQVT::EnumLiteralExp")
EnumerationLiteral = Class(name="EnumerationLiteral")
FlatQVT_Enumeration = Class(name="FlatQVT::Enumeration")
FlatQVT_EnumerationLiteral = Class(name="FlatQVT::EnumerationLiteral")
Enumeration_ = Class(name="Enumeration")
FlatQVT_ExpressionInOcl = Class(name="FlatQVT::ExpressionInOcl")
FlatQVT_Extent = Class(name="FlatQVT::Extent")
FlatQVT_Factory = Class(name="FlatQVT::Factory")
Package = Class(name="Package")
FlatQVT_FeatureCallExp = Class(name="FlatQVT::FeatureCallExp", is_abstract=True)
CallExp = Class(name="CallExp")
FlatQVT_ForExp = Class(name="FlatQVT::ForExp")
ImperativeLoopExp = Class(name="ImperativeLoopExp")
FlatQVT_Function = Class(name="FlatQVT::Function")
FlatQVT_FunctionParameter = Class(name="FlatQVT::FunctionParameter")
Parameter_ = Class(name="Parameter")
FlatQVT_GuardPattern = Class(name="FlatQVT::GuardPattern")
FlatQVT_ImperativeCallExp = Class(name="FlatQVT::ImperativeCallExp")
FlatQVT_ImperativeExpression = Class(name="FlatQVT::ImperativeExpression", is_abstract=True)
FlatQVT_Helper = Class(name="FlatQVT::Helper")
FlatQVT_IfExp = Class(name="FlatQVT::IfExp")
FlatQVT_ImperativeOperation = Class(name="FlatQVT::ImperativeOperation")
VarParameter = Class(name="VarParameter")
FlatQVT_ImperativeIterateExp = Class(name="FlatQVT::ImperativeIterateExp")
FlatQVT_ImperativeLoopExp = Class(name="FlatQVT::ImperativeLoopExp", is_abstract=True)
LoopExp = Class(name="LoopExp")
FlatQVT_IntegerLiteralExp = Class(name="FlatQVT::IntegerLiteralExp")
NumericLiteralExp = Class(name="NumericLiteralExp")
FlatQVT_InvalidLiteralExp = Class(name="FlatQVT::InvalidLiteralExp")
FlatQVT_InvalidType = Class(name="FlatQVT::InvalidType")
FlatQVT_IterateExp = Class(name="FlatQVT::IterateExp")
FlatQVT_InstantiationExp = Class(name="FlatQVT::InstantiationExp")
FlatQVT_Key = Class(name="FlatQVT::Key")
RelationalTransformation = Class(name="RelationalTransformation")
FlatQVT_LetExp = Class(name="FlatQVT::LetExp")
FlatQVT_IteratorExp = Class(name="FlatQVT::IteratorExp")
Module = Class(name="Module")
FlatQVT_ListLiteralExp = Class(name="FlatQVT::ListLiteralExp")
FlatQVT_ListType = Class(name="FlatQVT::ListType")
FlatQVT_LiteralExp = Class(name="FlatQVT::LiteralExp", is_abstract=True)
FlatQVT_LogExp = Class(name="FlatQVT::LogExp")
FlatQVT_LoopExp = Class(name="FlatQVT::LoopExp", is_abstract=True)
FlatQVT_Library = Class(name="FlatQVT::Library")
FlatQVT_Mapping = Class(name="FlatQVT::Mapping")
Mapping = Class(name="Mapping")
FlatQVT_MappingBody = Class(name="FlatQVT::MappingBody")
FlatQVT_MappingCallExp = Class(name="FlatQVT::MappingCallExp")
ImperativeCallExp = Class(name="ImperativeCallExp")
FlatQVT_MappingOperation = Class(name="FlatQVT::MappingOperation")
MappingOperation = Class(name="MappingOperation")
FlatQVT_MappingParameter = Class(name="FlatQVT::MappingParameter")
ModelParameter = Class(name="ModelParameter")
RelationDomain = Class(name="RelationDomain")
FlatQVT_ModelParameter = Class(name="FlatQVT::ModelParameter")
FlatQVT_ModelType = Class(name="FlatQVT::ModelType")
Relation = Class(name="Relation")
FlatQVT_Module = Class(name="FlatQVT::Module")
EntryOperation = Class(name="EntryOperation")
ModuleImport = Class(name="ModuleImport")
Tag = Class(name="Tag")
ModelType = Class(name="ModelType")
FlatQVT_ModuleImport = Class(name="FlatQVT::ModuleImport")
FlatQVT_MultiplicityElement = Class(name="FlatQVT::MultiplicityElement", is_abstract=True)
FlatQVT_NamedElement = Class(name="FlatQVT::NamedElement", is_abstract=True)
FlatQVT_NumericLiteralExp = Class(name="FlatQVT::NumericLiteralExp", is_abstract=True)
FlatQVT_Object = Class(name="FlatQVT::Object")
FlatQVT_ObjectExp = Class(name="FlatQVT::ObjectExp")
InstantiationExp = Class(name="InstantiationExp")
ConstructorBody = Class(name="ConstructorBody")
FlatQVT_ObjectTemplateExp = Class(name="FlatQVT::ObjectTemplateExp")
PropertyTemplateItem = Class(name="PropertyTemplateItem")
FlatQVT_OclExpression = Class(name="FlatQVT::OclExpression", is_abstract=True)
FlatQVT_Operation = Class(name="FlatQVT::Operation")
MultiplicityElement = Class(name="MultiplicityElement")
FlatQVT_NavigationCallExp = Class(name="FlatQVT::NavigationCallExp")
FeatureCallExp = Class(name="FeatureCallExp")
FlatQVT_NullLiteralExp = Class(name="FlatQVT::NullLiteralExp")
FlatQVT_OperationBody = Class(name="FlatQVT::OperationBody")
FlatQVT_OperationCallExp = Class(name="FlatQVT::OperationCallExp")
FlatQVT_OperationalTransformation = Class(name="FlatQVT::OperationalTransformation")
FlatQVT_OppositePropertyCallExp = Class(name="FlatQVT::OppositePropertyCallExp")
PropertyCallExp = Class(name="PropertyCallExp")
FlatQVT_OrderedSetType = Class(name="FlatQVT::OrderedSetType")
FlatQVT_OrderedTupleLiteralExp = Class(name="FlatQVT::OrderedTupleLiteralExp")
OrderedTupleLiteralPart = Class(name="OrderedTupleLiteralPart")
FlatQVT_OrderedTupleLiteralPart = Class(name="FlatQVT::OrderedTupleLiteralPart")
FlatQVT_Package = Class(name="FlatQVT::Package")
FlatQVT_Parameter = Class(name="FlatQVT::Parameter")
FlatQVT_Pattern = Class(name="FlatQVT::Pattern")
Predicate = Class(name="Predicate")
FlatQVT_Predicate = Class(name="FlatQVT::Predicate")
FlatQVT_PrimitiveLiteralExp = Class(name="FlatQVT::PrimitiveLiteralExp", is_abstract=True)
FlatQVT_PrimitiveType = Class(name="FlatQVT::PrimitiveType")
FlatQVT_Property = Class(name="FlatQVT::Property")
FlatQVT_OrderedTupleType = Class(name="FlatQVT::OrderedTupleType")
FlatQVT_PropertyAssignment = Class(name="FlatQVT::PropertyAssignment")
FlatQVT_PropertyCallExp = Class(name="FlatQVT::PropertyCallExp")
NavigationCallExp = Class(name="NavigationCallExp")
FlatQVT_PropertyTemplateItem = Class(name="FlatQVT::PropertyTemplateItem")
FlatQVT_RaiseExp = Class(name="FlatQVT::RaiseExp")
ObjectTemplateExp = Class(name="ObjectTemplateExp")
FlatQVT_RealizedVariable = Class(name="FlatQVT::RealizedVariable")
FlatQVT_ReflectiveCollection = Class(name="FlatQVT::ReflectiveCollection")
FlatQVT_ReflectiveSequence = Class(name="FlatQVT::ReflectiveSequence")
ReflectiveCollection = Class(name="ReflectiveCollection")
FlatQVT_RealLiteralExp = Class(name="FlatQVT::RealLiteralExp")
FlatQVT_Relation = Class(name="FlatQVT::Relation")
RelationImplementation = Class(name="RelationImplementation")
FlatQVT_RelationDomain = Class(name="FlatQVT::RelationDomain")
RelationDomainAssignment = Class(name="RelationDomainAssignment")
DomainPattern = Class(name="DomainPattern")
FlatQVT_RelationCallExp = Class(name="FlatQVT::RelationCallExp")
FlatQVT_RelationImplementation = Class(name="FlatQVT::RelationImplementation")
FlatQVT_RelationDomainAssignment = Class(name="FlatQVT::RelationDomainAssignment")
FlatQVT_RelationalTransformation = Class(name="FlatQVT::RelationalTransformation")
Transformation = Class(name="Transformation")
FlatQVT_ReturnExp = Class(name="FlatQVT::ReturnExp")
Key = Class(name="Key")
FlatQVT_ResolveExp = Class(name="FlatQVT::ResolveExp")
FlatQVT_Rule = Class(name="FlatQVT::Rule", is_abstract=True)
FlatQVT_ResolveInExp = Class(name="FlatQVT::ResolveInExp")
ResolveExp = Class(name="ResolveExp")
FlatQVT_StringLiteralExp = Class(name="FlatQVT::StringLiteralExp")
FlatQVT_SwitchExp = Class(name="FlatQVT::SwitchExp")
AltExp = Class(name="AltExp")
FlatQVT_SequenceType = Class(name="FlatQVT::SequenceType")
FlatQVT_SetType = Class(name="FlatQVT::SetType")
FlatQVT_TemplateExp = Class(name="FlatQVT::TemplateExp", is_abstract=True)
FlatQVT_Tag = Class(name="FlatQVT::Tag")
FlatQVT_TryExp = Class(name="FlatQVT::TryExp")
CatchExp = Class(name="CatchExp")
FlatQVT_TemplateParameterType = Class(name="FlatQVT::TemplateParameterType")
FlatQVT_Transformation = Class(name="FlatQVT::Transformation")
FlatQVT_TupleLiteralExp = Class(name="FlatQVT::TupleLiteralExp")
TupleLiteralPart = Class(name="TupleLiteralPart")
FlatQVT_TupleLiteralPart = Class(name="FlatQVT::TupleLiteralPart")
TupleLiteralExp = Class(name="TupleLiteralExp")
FlatQVT_TypeExp = Class(name="FlatQVT::TypeExp")
FlatQVT_TupleType = Class(name="FlatQVT::TupleType")
FlatQVT_Type = Class(name="FlatQVT::Type", is_abstract=True)
FlatQVT_TypedModel = Class(name="FlatQVT::TypedModel")
FlatQVT_TypedElement = Class(name="FlatQVT::TypedElement", is_abstract=True)
FlatQVT_Typedef = Class(name="FlatQVT::Typedef")
FlatQVT_UnlimitedNaturalExp = Class(name="FlatQVT::UnlimitedNaturalExp")
FlatQVT_UnlinkExp = Class(name="FlatQVT::UnlinkExp")
FlatQVT_URIExtent = Class(name="FlatQVT::URIExtent")
Extent = Class(name="Extent")
FlatQVT_UnpackExp = Class(name="FlatQVT::UnpackExp")
FlatQVT_VarParameter = Class(name="FlatQVT::VarParameter")
LetExp = Class(name="LetExp")
FlatQVT_Variable = Class(name="FlatQVT::Variable")
FlatQVT_VariableExp = Class(name="FlatQVT::VariableExp")
FlatQVT_VariableInitExp = Class(name="FlatQVT::VariableInitExp")
FlatQVT_VariableAssignment = Class(name="FlatQVT::VariableAssignment")
FlatQVT_WhileExp = Class(name="FlatQVT::WhileExp")
FlatQVT_VoidType = Class(name="FlatQVT::VoidType")

# FlatQVT_AltExp class attributes and methods

# ImperativeExpression class attributes and methods

# OclExpression class attributes and methods

# FlatQVT_Area class attributes and methods

# BottomPattern class attributes and methods

# GuardPattern class attributes and methods

# FlatQVT_AssertExp class attributes and methods
FlatQVT_AssertExp_severity: Property = Property(name="severity", type=StringType)
FlatQVT_AssertExp.attributes={FlatQVT_AssertExp_severity}

# FlatQVT_AnyType class attributes and methods

# Type class attributes and methods

# FlatQVT_Assignment class attributes and methods
FlatQVT_Assignment_isDefault: Property = Property(name="isDefault", type=StringType)
FlatQVT_Assignment.attributes={FlatQVT_Assignment_isDefault}

# Element class attributes and methods

# LogExp class attributes and methods

# FlatQVT_AssignExp class attributes and methods
FlatQVT_AssignExp_isReset: Property = Property(name="isReset", type=StringType)
FlatQVT_AssignExp.attributes={FlatQVT_AssignExp_isReset}

# FlatQVT_BagType class attributes and methods

# CollectionType class attributes and methods

# FlatQVT_BlockExp class attributes and methods

# FlatQVT_BooleanLiteralExp class attributes and methods
FlatQVT_BooleanLiteralExp_booleanSymbol: Property = Property(name="booleanSymbol", type=StringType)
FlatQVT_BooleanLiteralExp.attributes={FlatQVT_BooleanLiteralExp_booleanSymbol}

# PrimitiveLiteralExp class attributes and methods

# FlatQVT_BottomPattern class attributes and methods

# CorePattern class attributes and methods

# RealizedVariable class attributes and methods

# FlatQVT_BreakExp class attributes and methods

# FlatQVT_CallExp class attributes and methods

# Area class attributes and methods

# Assignment class attributes and methods

# EnforcementOperation class attributes and methods

# FlatQVT_Class class attributes and methods
FlatQVT_Class_isAbstract: Property = Property(name="isAbstract", type=StringType)
FlatQVT_Class.attributes={FlatQVT_Class_isAbstract}

# Property class attributes and methods

# Operation class attributes and methods

# Class class attributes and methods

# FlatQVT_CatchExp class attributes and methods

# FlatQVT_CollectionLiteralExp class attributes and methods
FlatQVT_CollectionLiteralExp_kind: Property = Property(name="kind", type=StringType)
FlatQVT_CollectionLiteralExp.attributes={FlatQVT_CollectionLiteralExp_kind}

# LiteralExp class attributes and methods

# FlatQVT_CollectionItem class attributes and methods

# CollectionLiteralPart class attributes and methods

# CollectionLiteralExp class attributes and methods

# FlatQVT_CollectionRange class attributes and methods

# FlatQVT_CollectionLiteralPart class attributes and methods

# TypedElement class attributes and methods

# Variable class attributes and methods

# FlatQVT_CollectionTemplateExp class attributes and methods

# TemplateExp class attributes and methods

# NamedElement class attributes and methods

# FlatQVT_ComputeExp class attributes and methods

# FlatQVT_CollectionType class attributes and methods

# DataType class attributes and methods

# FlatQVT_Comment class attributes and methods
FlatQVT_Comment_body: Property = Property(name="body", type=StringType)
FlatQVT_Comment.attributes={FlatQVT_Comment_body}

# FlatQVT_ConstructorBody class attributes and methods

# OperationBody class attributes and methods

# FlatQVT_ContextualProperty class attributes and methods

# FlatQVT_Constructor class attributes and methods

# ImperativeOperation class attributes and methods

# FlatQVT_CoreDomain class attributes and methods

# Domain class attributes and methods

# FlatQVT_CorePattern class attributes and methods

# Pattern class attributes and methods

# FlatQVT_DataType class attributes and methods

# FlatQVT_DictLiteralExp class attributes and methods

# FlatQVT_ContinueExp class attributes and methods

# FlatQVT_DictLiteralPart class attributes and methods

# DictLiteralPart class attributes and methods

# FlatQVT_DictionaryType class attributes and methods

# FlatQVT_Domain class attributes and methods
FlatQVT_Domain_isCheckable: Property = Property(name="isCheckable", type=StringType)
FlatQVT_Domain_isEnforceable: Property = Property(name="isEnforceable", type=StringType)
FlatQVT_Domain.attributes={FlatQVT_Domain_isEnforceable, FlatQVT_Domain_isCheckable}

# Rule class attributes and methods

# TypedModel class attributes and methods

# FlatQVT_DomainPattern class attributes and methods

# FlatQVT_Element class attributes and methods
FlatQVT_Element_m_container: Method = Method(name="container", parameters={}, type=StringType)
FlatQVT_Element_m_unset: Method = Method(name="unset", parameters={Parameter(name='property')})
FlatQVT_Element_m_equals: Method = Method(name="equals", parameters={Parameter(name='object')}, type=StringType)
FlatQVT_Element_m_get: Method = Method(name="get", parameters={Parameter(name='property')}, type=StringType)
FlatQVT_Element_m_getMetaClass: Method = Method(name="getMetaClass", parameters={}, type=StringType)
FlatQVT_Element_m_isSet: Method = Method(name="isSet", parameters={Parameter(name='property')}, type=StringType)
FlatQVT_Element_m_set: Method = Method(name="set", parameters={Parameter(name='object'), Parameter(name='property')})
FlatQVT_Element.methods={FlatQVT_Element_m_set, FlatQVT_Element_m_getMetaClass, FlatQVT_Element_m_isSet, FlatQVT_Element_m_container, FlatQVT_Element_m_unset, FlatQVT_Element_m_equals, FlatQVT_Element_m_get}

# Object class attributes and methods

# Comment class attributes and methods

# FlatQVT_EnforcementOperation class attributes and methods
FlatQVT_EnforcementOperation_enforcementMode: Property = Property(name="enforcementMode", type=StringType)
FlatQVT_EnforcementOperation.attributes={FlatQVT_EnforcementOperation_enforcementMode}

# OperationCallExp class attributes and methods

# FlatQVT_EntryOperation class attributes and methods

# FlatQVT_EnumLiteralExp class attributes and methods

# EnumerationLiteral class attributes and methods

# FlatQVT_Enumeration class attributes and methods

# FlatQVT_EnumerationLiteral class attributes and methods

# Enumeration class attributes and methods

# FlatQVT_ExpressionInOcl class attributes and methods

# FlatQVT_Extent class attributes and methods
FlatQVT_Extent_m_elements: Method = Method(name="elements", parameters={}, type=StringType)
FlatQVT_Extent_m_useContainment: Method = Method(name="useContainment", parameters={}, type=StringType)
FlatQVT_Extent.methods={FlatQVT_Extent_m_elements, FlatQVT_Extent_m_useContainment}

# FlatQVT_Factory class attributes and methods
FlatQVT_Factory_m_convertToString: Method = Method(name="convertToString", parameters={Parameter(name='dataType'), Parameter(name='object')}, type=StringType)
FlatQVT_Factory_m_create: Method = Method(name="create", parameters={Parameter(name='metaClass')}, type=StringType)
FlatQVT_Factory_m_createFromString: Method = Method(name="createFromString", parameters={Parameter(name='string'), Parameter(name='dataType')}, type=StringType)
FlatQVT_Factory.methods={FlatQVT_Factory_m_create, FlatQVT_Factory_m_convertToString, FlatQVT_Factory_m_createFromString}

# Package class attributes and methods

# FlatQVT_FeatureCallExp class attributes and methods

# CallExp class attributes and methods

# FlatQVT_ForExp class attributes and methods

# ImperativeLoopExp class attributes and methods

# FlatQVT_Function class attributes and methods

# FlatQVT_FunctionParameter class attributes and methods

# Parameter class attributes and methods

# FlatQVT_GuardPattern class attributes and methods

# FlatQVT_ImperativeCallExp class attributes and methods
FlatQVT_ImperativeCallExp_isVirtual: Property = Property(name="isVirtual", type=StringType)
FlatQVT_ImperativeCallExp.attributes={FlatQVT_ImperativeCallExp_isVirtual}

# FlatQVT_ImperativeExpression class attributes and methods

# FlatQVT_Helper class attributes and methods
FlatQVT_Helper_isQuery: Property = Property(name="isQuery", type=StringType)
FlatQVT_Helper.attributes={FlatQVT_Helper_isQuery}

# FlatQVT_IfExp class attributes and methods

# FlatQVT_ImperativeOperation class attributes and methods
FlatQVT_ImperativeOperation_isBlackbox: Property = Property(name="isBlackbox", type=StringType)
FlatQVT_ImperativeOperation.attributes={FlatQVT_ImperativeOperation_isBlackbox}

# VarParameter class attributes and methods

# FlatQVT_ImperativeIterateExp class attributes and methods

# FlatQVT_ImperativeLoopExp class attributes and methods

# LoopExp class attributes and methods

# FlatQVT_IntegerLiteralExp class attributes and methods
FlatQVT_IntegerLiteralExp_integerSymbol: Property = Property(name="integerSymbol", type=StringType)
FlatQVT_IntegerLiteralExp.attributes={FlatQVT_IntegerLiteralExp_integerSymbol}

# NumericLiteralExp class attributes and methods

# FlatQVT_InvalidLiteralExp class attributes and methods

# FlatQVT_InvalidType class attributes and methods

# FlatQVT_IterateExp class attributes and methods

# FlatQVT_InstantiationExp class attributes and methods

# FlatQVT_Key class attributes and methods

# RelationalTransformation class attributes and methods

# FlatQVT_LetExp class attributes and methods

# FlatQVT_IteratorExp class attributes and methods

# Module class attributes and methods

# FlatQVT_ListLiteralExp class attributes and methods

# FlatQVT_ListType class attributes and methods

# FlatQVT_LiteralExp class attributes and methods

# FlatQVT_LogExp class attributes and methods

# FlatQVT_LoopExp class attributes and methods

# FlatQVT_Library class attributes and methods

# FlatQVT_Mapping class attributes and methods

# Mapping class attributes and methods

# FlatQVT_MappingBody class attributes and methods

# FlatQVT_MappingCallExp class attributes and methods
FlatQVT_MappingCallExp_isStrict: Property = Property(name="isStrict", type=StringType)
FlatQVT_MappingCallExp.attributes={FlatQVT_MappingCallExp_isStrict}

# ImperativeCallExp class attributes and methods

# FlatQVT_MappingOperation class attributes and methods

# MappingOperation class attributes and methods

# FlatQVT_MappingParameter class attributes and methods

# ModelParameter class attributes and methods

# RelationDomain class attributes and methods

# FlatQVT_ModelParameter class attributes and methods

# FlatQVT_ModelType class attributes and methods
FlatQVT_ModelType_conformanceKind: Property = Property(name="conformanceKind", type=StringType)
FlatQVT_ModelType.attributes={FlatQVT_ModelType_conformanceKind}

# Relation class attributes and methods

# FlatQVT_Module class attributes and methods
FlatQVT_Module_isBlackbox: Property = Property(name="isBlackbox", type=StringType)
FlatQVT_Module.attributes={FlatQVT_Module_isBlackbox}

# EntryOperation class attributes and methods

# ModuleImport class attributes and methods

# Tag class attributes and methods

# ModelType class attributes and methods

# FlatQVT_ModuleImport class attributes and methods
FlatQVT_ModuleImport_kind: Property = Property(name="kind", type=StringType)
FlatQVT_ModuleImport.attributes={FlatQVT_ModuleImport_kind}

# FlatQVT_MultiplicityElement class attributes and methods
FlatQVT_MultiplicityElement_isOrdered: Property = Property(name="isOrdered", type=StringType)
FlatQVT_MultiplicityElement_isUnique: Property = Property(name="isUnique", type=StringType)
FlatQVT_MultiplicityElement_lower: Property = Property(name="lower", type=StringType)
FlatQVT_MultiplicityElement_upper: Property = Property(name="upper", type=StringType)
FlatQVT_MultiplicityElement.attributes={FlatQVT_MultiplicityElement_isOrdered, FlatQVT_MultiplicityElement_isUnique, FlatQVT_MultiplicityElement_upper, FlatQVT_MultiplicityElement_lower}

# FlatQVT_NamedElement class attributes and methods
FlatQVT_NamedElement_name: Property = Property(name="name", type=StringType)
FlatQVT_NamedElement.attributes={FlatQVT_NamedElement_name}

# FlatQVT_NumericLiteralExp class attributes and methods

# FlatQVT_Object class attributes and methods

# FlatQVT_ObjectExp class attributes and methods

# InstantiationExp class attributes and methods

# ConstructorBody class attributes and methods

# FlatQVT_ObjectTemplateExp class attributes and methods

# PropertyTemplateItem class attributes and methods

# FlatQVT_OclExpression class attributes and methods

# FlatQVT_Operation class attributes and methods

# MultiplicityElement class attributes and methods

# FlatQVT_NavigationCallExp class attributes and methods

# FeatureCallExp class attributes and methods

# FlatQVT_NullLiteralExp class attributes and methods

# FlatQVT_OperationBody class attributes and methods

# FlatQVT_OperationCallExp class attributes and methods

# FlatQVT_OperationalTransformation class attributes and methods

# FlatQVT_OppositePropertyCallExp class attributes and methods

# PropertyCallExp class attributes and methods

# FlatQVT_OrderedSetType class attributes and methods

# FlatQVT_OrderedTupleLiteralExp class attributes and methods

# OrderedTupleLiteralPart class attributes and methods

# FlatQVT_OrderedTupleLiteralPart class attributes and methods

# FlatQVT_Package class attributes and methods
FlatQVT_Package_uri: Property = Property(name="uri", type=StringType)
FlatQVT_Package.attributes={FlatQVT_Package_uri}

# FlatQVT_Parameter class attributes and methods

# FlatQVT_Pattern class attributes and methods

# Predicate class attributes and methods

# FlatQVT_Predicate class attributes and methods

# FlatQVT_PrimitiveLiteralExp class attributes and methods

# FlatQVT_PrimitiveType class attributes and methods

# FlatQVT_Property class attributes and methods
FlatQVT_Property_default: Property = Property(name="default", type=StringType)
FlatQVT_Property_isComposite: Property = Property(name="isComposite", type=StringType)
FlatQVT_Property_isDerived: Property = Property(name="isDerived", type=StringType)
FlatQVT_Property_isID: Property = Property(name="isID", type=StringType)
FlatQVT_Property_isReadOnly: Property = Property(name="isReadOnly", type=StringType)
FlatQVT_Property.attributes={FlatQVT_Property_default, FlatQVT_Property_isReadOnly, FlatQVT_Property_isDerived, FlatQVT_Property_isID, FlatQVT_Property_isComposite}

# FlatQVT_OrderedTupleType class attributes and methods

# FlatQVT_PropertyAssignment class attributes and methods

# FlatQVT_PropertyCallExp class attributes and methods

# NavigationCallExp class attributes and methods

# FlatQVT_PropertyTemplateItem class attributes and methods
FlatQVT_PropertyTemplateItem_isOpposite: Property = Property(name="isOpposite", type=StringType)
FlatQVT_PropertyTemplateItem.attributes={FlatQVT_PropertyTemplateItem_isOpposite}

# FlatQVT_RaiseExp class attributes and methods

# ObjectTemplateExp class attributes and methods

# FlatQVT_RealizedVariable class attributes and methods

# FlatQVT_ReflectiveCollection class attributes and methods
FlatQVT_ReflectiveCollection_m_add: Method = Method(name="add", parameters={Parameter(name='object')}, type=StringType)
FlatQVT_ReflectiveCollection_m_addAll: Method = Method(name="addAll", parameters={Parameter(name='objects')}, type=StringType)
FlatQVT_ReflectiveCollection_m_clear: Method = Method(name="clear", parameters={})
FlatQVT_ReflectiveCollection_m_remove: Method = Method(name="remove", parameters={Parameter(name='object')}, type=StringType)
FlatQVT_ReflectiveCollection_m_size: Method = Method(name="size", parameters={}, type=StringType)
FlatQVT_ReflectiveCollection.methods={FlatQVT_ReflectiveCollection_m_remove, FlatQVT_ReflectiveCollection_m_size, FlatQVT_ReflectiveCollection_m_add, FlatQVT_ReflectiveCollection_m_addAll, FlatQVT_ReflectiveCollection_m_clear}

# FlatQVT_ReflectiveSequence class attributes and methods
FlatQVT_ReflectiveSequence_m_add: Method = Method(name="add", parameters={Parameter(name='object'), Parameter(name='index')})
FlatQVT_ReflectiveSequence_m_get: Method = Method(name="get", parameters={Parameter(name='index')}, type=StringType)
FlatQVT_ReflectiveSequence_m_remove: Method = Method(name="remove", parameters={Parameter(name='index')}, type=StringType)
FlatQVT_ReflectiveSequence_m_set: Method = Method(name="set", parameters={Parameter(name='index'), Parameter(name='object')}, type=StringType)
FlatQVT_ReflectiveSequence.methods={FlatQVT_ReflectiveSequence_m_set, FlatQVT_ReflectiveSequence_m_remove, FlatQVT_ReflectiveSequence_m_get, FlatQVT_ReflectiveSequence_m_add}

# ReflectiveCollection class attributes and methods

# FlatQVT_RealLiteralExp class attributes and methods
FlatQVT_RealLiteralExp_realSymbol: Property = Property(name="realSymbol", type=StringType)
FlatQVT_RealLiteralExp.attributes={FlatQVT_RealLiteralExp_realSymbol}

# FlatQVT_Relation class attributes and methods
FlatQVT_Relation_isTopLevel: Property = Property(name="isTopLevel", type=StringType)
FlatQVT_Relation.attributes={FlatQVT_Relation_isTopLevel}

# RelationImplementation class attributes and methods

# FlatQVT_RelationDomain class attributes and methods

# RelationDomainAssignment class attributes and methods

# DomainPattern class attributes and methods

# FlatQVT_RelationCallExp class attributes and methods

# FlatQVT_RelationImplementation class attributes and methods

# FlatQVT_RelationDomainAssignment class attributes and methods

# FlatQVT_RelationalTransformation class attributes and methods

# Transformation class attributes and methods

# FlatQVT_ReturnExp class attributes and methods

# Key class attributes and methods

# FlatQVT_ResolveExp class attributes and methods
FlatQVT_ResolveExp_isDeferred: Property = Property(name="isDeferred", type=StringType)
FlatQVT_ResolveExp_isInverse: Property = Property(name="isInverse", type=StringType)
FlatQVT_ResolveExp_one: Property = Property(name="one", type=StringType)
FlatQVT_ResolveExp.attributes={FlatQVT_ResolveExp_isDeferred, FlatQVT_ResolveExp_one, FlatQVT_ResolveExp_isInverse}

# FlatQVT_Rule class attributes and methods

# FlatQVT_ResolveInExp class attributes and methods

# ResolveExp class attributes and methods

# FlatQVT_StringLiteralExp class attributes and methods
FlatQVT_StringLiteralExp_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
FlatQVT_StringLiteralExp.attributes={FlatQVT_StringLiteralExp_stringSymbol}

# FlatQVT_SwitchExp class attributes and methods

# AltExp class attributes and methods

# FlatQVT_SequenceType class attributes and methods

# FlatQVT_SetType class attributes and methods

# FlatQVT_TemplateExp class attributes and methods

# FlatQVT_Tag class attributes and methods
FlatQVT_Tag_name: Property = Property(name="name", type=StringType)
FlatQVT_Tag_value: Property = Property(name="value", type=StringType)
FlatQVT_Tag.attributes={FlatQVT_Tag_name, FlatQVT_Tag_value}

# FlatQVT_TryExp class attributes and methods

# CatchExp class attributes and methods

# FlatQVT_TemplateParameterType class attributes and methods
FlatQVT_TemplateParameterType_specification: Property = Property(name="specification", type=StringType)
FlatQVT_TemplateParameterType.attributes={FlatQVT_TemplateParameterType_specification}

# FlatQVT_Transformation class attributes and methods

# FlatQVT_TupleLiteralExp class attributes and methods

# TupleLiteralPart class attributes and methods

# FlatQVT_TupleLiteralPart class attributes and methods

# TupleLiteralExp class attributes and methods

# FlatQVT_TypeExp class attributes and methods

# FlatQVT_TupleType class attributes and methods

# FlatQVT_Type class attributes and methods
FlatQVT_Type_m_isInstance: Method = Method(name="isInstance", parameters={Parameter(name='object')}, type=StringType)
FlatQVT_Type.methods={FlatQVT_Type_m_isInstance}

# FlatQVT_TypedModel class attributes and methods

# FlatQVT_TypedElement class attributes and methods

# FlatQVT_Typedef class attributes and methods

# FlatQVT_UnlimitedNaturalExp class attributes and methods
FlatQVT_UnlimitedNaturalExp_symbol: Property = Property(name="symbol", type=StringType)
FlatQVT_UnlimitedNaturalExp.attributes={FlatQVT_UnlimitedNaturalExp_symbol}

# FlatQVT_UnlinkExp class attributes and methods

# FlatQVT_URIExtent class attributes and methods
FlatQVT_URIExtent_m_uri: Method = Method(name="uri", parameters={Parameter(name='element')}, type=StringType)
FlatQVT_URIExtent_m_contextURI: Method = Method(name="contextURI", parameters={}, type=StringType)
FlatQVT_URIExtent_m_element: Method = Method(name="element", parameters={Parameter(name='uri')}, type=StringType)
FlatQVT_URIExtent.methods={FlatQVT_URIExtent_m_element, FlatQVT_URIExtent_m_contextURI, FlatQVT_URIExtent_m_uri}

# Extent class attributes and methods

# FlatQVT_UnpackExp class attributes and methods

# FlatQVT_VarParameter class attributes and methods
FlatQVT_VarParameter_kind: Property = Property(name="kind", type=StringType)
FlatQVT_VarParameter.attributes={FlatQVT_VarParameter_kind}

# LetExp class attributes and methods

# FlatQVT_Variable class attributes and methods

# FlatQVT_VariableExp class attributes and methods

# FlatQVT_VariableInitExp class attributes and methods
FlatQVT_VariableInitExp_withResult: Property = Property(name="withResult", type=StringType)
FlatQVT_VariableInitExp.attributes={FlatQVT_VariableInitExp_withResult}

# FlatQVT_VariableAssignment class attributes and methods

# FlatQVT_WhileExp class attributes and methods

# FlatQVT_VoidType class attributes and methods

# Relationships
body0: BinaryAssociation = BinaryAssociation(
    name="body0",
    ends={
        Property(name="OclExpression", type=FlatQVT_AltExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_AltExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bottomPattern4: BinaryAssociation = BinaryAssociation(
    name="bottomPattern4",
    ends={
        Property(name="BottomPattern", type=FlatQVT_Area, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Area", type=BottomPattern, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
guardPattern5: BinaryAssociation = BinaryAssociation(
    name="guardPattern5",
    ends={
        Property(name="GuardPattern", type=FlatQVT_Area, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Area6", type=GuardPattern, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
assertion7: BinaryAssociation = BinaryAssociation(
    name="assertion7",
    ends={
        Property(name="OclExpression8", type=FlatQVT_AssertExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_AssertExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition1: BinaryAssociation = BinaryAssociation(
    name="condition1",
    ends={
        Property(name="OclExpression3", type=FlatQVT_AltExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_AltExp2", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left13: BinaryAssociation = BinaryAssociation(
    name="left13",
    ends={
        Property(name="OclExpression15", type=FlatQVT_AssignExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_AssignExp14", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value16: BinaryAssociation = BinaryAssociation(
    name="value16",
    ends={
        Property(name="OclExpression18", type=FlatQVT_AssignExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_AssignExp17", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
log9: BinaryAssociation = BinaryAssociation(
    name="log9",
    ends={
        Property(name="LogExp", type=FlatQVT_AssertExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_AssertExp10", type=LogExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultValue11: BinaryAssociation = BinaryAssociation(
    name="defaultValue11",
    ends={
        Property(name="OclExpression12", type=FlatQVT_AssignExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_AssignExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body24: BinaryAssociation = BinaryAssociation(
    name="body24",
    ends={
        Property(name="OclExpression25", type=FlatQVT_BlockExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_BlockExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bottomPattern19: BinaryAssociation = BinaryAssociation(
    name="bottomPattern19",
    ends={
        Property(name="BottomPattern20", type=FlatQVT_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Assignment", type=BottomPattern, multiplicity=Multiplicity(1, 1))
    }
)
value21: BinaryAssociation = BinaryAssociation(
    name="value21",
    ends={
        Property(name="OclExpression23", type=FlatQVT_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Assignment22", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
enforcementOperation29: BinaryAssociation = BinaryAssociation(
    name="enforcementOperation29",
    ends={
        Property(name="EnforcementOperation", type=FlatQVT_BottomPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_BottomPattern30", type=EnforcementOperation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
realizedVariable31: BinaryAssociation = BinaryAssociation(
    name="realizedVariable31",
    ends={
        Property(name="RealizedVariable", type=FlatQVT_BottomPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_BottomPattern32", type=RealizedVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source33: BinaryAssociation = BinaryAssociation(
    name="source33",
    ends={
        Property(name="OclExpression34", type=FlatQVT_CallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_CallExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
area26: BinaryAssociation = BinaryAssociation(
    name="area26",
    ends={
        Property(name="Area", type=FlatQVT_BottomPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_BottomPattern", type=Area, multiplicity=Multiplicity(1, 1))
    }
)
assignment27: BinaryAssociation = BinaryAssociation(
    name="assignment27",
    ends={
        Property(name="Assignment", type=FlatQVT_BottomPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_BottomPattern28", type=Assignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAttribute39: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute39",
    ends={
        Property(name="Property", type=FlatQVT_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Class", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation40: BinaryAssociation = BinaryAssociation(
    name="ownedOperation40",
    ends={
        Property(name="Operation", type=FlatQVT_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Class41", type=Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body35: BinaryAssociation = BinaryAssociation(
    name="body35",
    ends={
        Property(name="OclExpression36", type=FlatQVT_CatchExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_CatchExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exception37: BinaryAssociation = BinaryAssociation(
    name="exception37",
    ends={
        Property(name="Type", type=FlatQVT_CatchExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_CatchExp38", type=Type, multiplicity=Multiplicity(0, 9999))
    }
)
superClass42: BinaryAssociation = BinaryAssociation(
    name="superClass42",
    ends={
        Property(name="Class", type=FlatQVT_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Class43", type=Class_, multiplicity=Multiplicity(0, 9999))
    }
)
item44: BinaryAssociation = BinaryAssociation(
    name="item44",
    ends={
        Property(name="OclExpression45", type=FlatQVT_CollectionItem, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_CollectionItem", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
collectionLiteralExp47: BinaryAssociation = BinaryAssociation(
    name="collectionLiteralExp47",
    ends={
        Property(name="CollectionLiteralExp", type=FlatQVT_CollectionLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_CollectionLiteralPart", type=CollectionLiteralExp, multiplicity=Multiplicity(1, 1))
    }
)
first48: BinaryAssociation = BinaryAssociation(
    name="first48",
    ends={
        Property(name="OclExpression49", type=FlatQVT_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_CollectionRange", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
part46: BinaryAssociation = BinaryAssociation(
    name="part46",
    ends={
        Property(name="CollectionLiteralPart", type=FlatQVT_CollectionLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_CollectionLiteralExp", type=CollectionLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
member53: BinaryAssociation = BinaryAssociation(
    name="member53",
    ends={
        Property(name="OclExpression54", type=FlatQVT_CollectionTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_CollectionTemplateExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredCollectionType55: BinaryAssociation = BinaryAssociation(
    name="referredCollectionType55",
    ends={
        Property(name="CollectionType", type=FlatQVT_CollectionTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_CollectionTemplateExp56", type=CollectionType, multiplicity=Multiplicity(1, 1))
    }
)
rest57: BinaryAssociation = BinaryAssociation(
    name="rest57",
    ends={
        Property(name="Variable", type=FlatQVT_CollectionTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_CollectionTemplateExp58", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
last50: BinaryAssociation = BinaryAssociation(
    name="last50",
    ends={
        Property(name="OclExpression52", type=FlatQVT_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_CollectionRange51", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
annotatedElement61: BinaryAssociation = BinaryAssociation(
    name="annotatedElement61",
    ends={
        Property(name="NamedElement", type=FlatQVT_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Comment", type=NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
body62: BinaryAssociation = BinaryAssociation(
    name="body62",
    ends={
        Property(name="OclExpression63", type=FlatQVT_ComputeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_ComputeExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elementType59: BinaryAssociation = BinaryAssociation(
    name="elementType59",
    ends={
        Property(name="Type60", type=FlatQVT_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_CollectionType", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
context67: BinaryAssociation = BinaryAssociation(
    name="context67",
    ends={
        Property(name="Class68", type=FlatQVT_ContextualProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_ContextualProperty", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
initExpression69: BinaryAssociation = BinaryAssociation(
    name="initExpression69",
    ends={
        Property(name="OclExpression71", type=FlatQVT_ContextualProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_ContextualProperty70", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnedElement64: BinaryAssociation = BinaryAssociation(
    name="returnedElement64",
    ends={
        Property(name="Variable66", type=FlatQVT_ComputeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_ComputeExp65", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable75: BinaryAssociation = BinaryAssociation(
    name="variable75",
    ends={
        Property(name="Variable76", type=FlatQVT_CorePattern, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_CorePattern", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
overridden72: BinaryAssociation = BinaryAssociation(
    name="overridden72",
    ends={
        Property(name="Property74", type=FlatQVT_ContextualProperty, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_ContextualProperty73", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
key78: BinaryAssociation = BinaryAssociation(
    name="key78",
    ends={
        Property(name="OclExpression79", type=FlatQVT_DictLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_DictLiteralPart", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value80: BinaryAssociation = BinaryAssociation(
    name="value80",
    ends={
        Property(name="OclExpression82", type=FlatQVT_DictLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_DictLiteralPart81", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
part77: BinaryAssociation = BinaryAssociation(
    name="part77",
    ends={
        Property(name="DictLiteralPart", type=FlatQVT_DictLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_DictLiteralExp", type=DictLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keyType83: BinaryAssociation = BinaryAssociation(
    name="keyType83",
    ends={
        Property(name="Type84", type=FlatQVT_DictionaryType, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_DictionaryType", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
rule85: BinaryAssociation = BinaryAssociation(
    name="rule85",
    ends={
        Property(name="Rule", type=FlatQVT_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Domain", type=Rule, multiplicity=Multiplicity(1, 1))
    }
)
typedModel86: BinaryAssociation = BinaryAssociation(
    name="typedModel86",
    ends={
        Property(name="TypedModel", type=FlatQVT_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Domain87", type=TypedModel, multiplicity=Multiplicity(0, 1))
    }
)
templateExpression88: BinaryAssociation = BinaryAssociation(
    name="templateExpression88",
    ends={
        Property(name="TemplateExp", type=FlatQVT_DomainPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_DomainPattern", type=TemplateExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedComment89: BinaryAssociation = BinaryAssociation(
    name="ownedComment89",
    ends={
        Property(name="Comment", type=FlatQVT_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Element", type=Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bottomPattern90: BinaryAssociation = BinaryAssociation(
    name="bottomPattern90",
    ends={
        Property(name="BottomPattern91", type=FlatQVT_EnforcementOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_EnforcementOperation", type=BottomPattern, multiplicity=Multiplicity(0, 1))
    }
)
operationCallExp92: BinaryAssociation = BinaryAssociation(
    name="operationCallExp92",
    ends={
        Property(name="OperationCallExp", type=FlatQVT_EnforcementOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_EnforcementOperation93", type=OperationCallExp, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referredEnumLiteral94: BinaryAssociation = BinaryAssociation(
    name="referredEnumLiteral94",
    ends={
        Property(name="EnumerationLiteral", type=FlatQVT_EnumLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_EnumLiteralExp", type=EnumerationLiteral, multiplicity=Multiplicity(0, 1))
    }
)
ownedLiteral95: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral95",
    ends={
        Property(name="EnumerationLiteral96", type=FlatQVT_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Enumeration", type=EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enumeration97: BinaryAssociation = BinaryAssociation(
    name="enumeration97",
    ends={
        Property(name="Enumeration", type=FlatQVT_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_EnumerationLiteral", type=Enumeration_, multiplicity=Multiplicity(0, 1))
    }
)
bodyExpression98: BinaryAssociation = BinaryAssociation(
    name="bodyExpression98",
    ends={
        Property(name="OclExpression99", type=FlatQVT_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_ExpressionInOcl", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameterVariable106: BinaryAssociation = BinaryAssociation(
    name="parameterVariable106",
    ends={
        Property(name="Variable108", type=FlatQVT_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_ExpressionInOcl107", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resultVariable109: BinaryAssociation = BinaryAssociation(
    name="resultVariable109",
    ends={
        Property(name="Variable111", type=FlatQVT_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_ExpressionInOcl110", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
package112: BinaryAssociation = BinaryAssociation(
    name="package112",
    ends={
        Property(name="Package", type=FlatQVT_Factory, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Factory", type=Package, multiplicity=Multiplicity(1, 1))
    }
)
queryExpression113: BinaryAssociation = BinaryAssociation(
    name="queryExpression113",
    ends={
        Property(name="OclExpression114", type=FlatQVT_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Function", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contextVariable100: BinaryAssociation = BinaryAssociation(
    name="contextVariable100",
    ends={
        Property(name="Variable102", type=FlatQVT_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_ExpressionInOcl101", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
generatedType103: BinaryAssociation = BinaryAssociation(
    name="generatedType103",
    ends={
        Property(name="Type105", type=FlatQVT_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_ExpressionInOcl104", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition117: BinaryAssociation = BinaryAssociation(
    name="condition117",
    ends={
        Property(name="OclExpression118", type=FlatQVT_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_IfExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression119: BinaryAssociation = BinaryAssociation(
    name="elseExpression119",
    ends={
        Property(name="OclExpression121", type=FlatQVT_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_IfExp120", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression122: BinaryAssociation = BinaryAssociation(
    name="thenExpression122",
    ends={
        Property(name="OclExpression124", type=FlatQVT_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_IfExp123", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
area115: BinaryAssociation = BinaryAssociation(
    name="area115",
    ends={
        Property(name="Area116", type=FlatQVT_GuardPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_GuardPattern", type=Area, multiplicity=Multiplicity(1, 1))
    }
)
condition127: BinaryAssociation = BinaryAssociation(
    name="condition127",
    ends={
        Property(name="OclExpression128", type=FlatQVT_ImperativeLoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_ImperativeLoopExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body129: BinaryAssociation = BinaryAssociation(
    name="body129",
    ends={
        Property(name="OperationBody", type=FlatQVT_ImperativeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_ImperativeOperation", type=OperationBody, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
context130: BinaryAssociation = BinaryAssociation(
    name="context130",
    ends={
        Property(name="VarParameter", type=FlatQVT_ImperativeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_ImperativeOperation131", type=VarParameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
overridden132: BinaryAssociation = BinaryAssociation(
    name="overridden132",
    ends={
        Property(name="ImperativeOperation", type=FlatQVT_ImperativeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_ImperativeOperation133", type=ImperativeOperation, multiplicity=Multiplicity(0, 1))
    }
)
result134: BinaryAssociation = BinaryAssociation(
    name="result134",
    ends={
        Property(name="VarParameter136", type=FlatQVT_ImperativeOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_ImperativeOperation135", type=VarParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target125: BinaryAssociation = BinaryAssociation(
    name="target125",
    ends={
        Property(name="Variable126", type=FlatQVT_ImperativeIterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_ImperativeIterateExp", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extent139: BinaryAssociation = BinaryAssociation(
    name="extent139",
    ends={
        Property(name="Variable141", type=FlatQVT_InstantiationExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_InstantiationExp140", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
instantiatedClass142: BinaryAssociation = BinaryAssociation(
    name="instantiatedClass142",
    ends={
        Property(name="Class144", type=FlatQVT_InstantiationExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_InstantiationExp143", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
argument137: BinaryAssociation = BinaryAssociation(
    name="argument137",
    ends={
        Property(name="OclExpression138", type=FlatQVT_InstantiationExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_InstantiationExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
identifies147: BinaryAssociation = BinaryAssociation(
    name="identifies147",
    ends={
        Property(name="Class148", type=FlatQVT_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Key", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
oppositePart149: BinaryAssociation = BinaryAssociation(
    name="oppositePart149",
    ends={
        Property(name="Property151", type=FlatQVT_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Key150", type=Property_, multiplicity=Multiplicity(0, 9999))
    }
)
part152: BinaryAssociation = BinaryAssociation(
    name="part152",
    ends={
        Property(name="Property154", type=FlatQVT_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Key153", type=Property_, multiplicity=Multiplicity(0, 9999))
    }
)
transformation155: BinaryAssociation = BinaryAssociation(
    name="transformation155",
    ends={
        Property(name="RelationalTransformation", type=FlatQVT_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Key156", type=RelationalTransformation, multiplicity=Multiplicity(0, 1))
    }
)
in157: BinaryAssociation = BinaryAssociation(
    name="in157",
    ends={
        Property(name="OclExpression158", type=FlatQVT_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_LetExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result145: BinaryAssociation = BinaryAssociation(
    name="result145",
    ends={
        Property(name="Variable146", type=FlatQVT_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_IterateExp", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
element162: BinaryAssociation = BinaryAssociation(
    name="element162",
    ends={
        Property(name="OclExpression163", type=FlatQVT_ListLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_ListLiteralExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition164: BinaryAssociation = BinaryAssociation(
    name="condition164",
    ends={
        Property(name="OclExpression165", type=FlatQVT_LogExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_LogExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable159: BinaryAssociation = BinaryAssociation(
    name="variable159",
    ends={
        Property(name="Variable161", type=FlatQVT_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_LetExp160", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterator168: BinaryAssociation = BinaryAssociation(
    name="iterator168",
    ends={
        Property(name="Variable170", type=FlatQVT_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_LoopExp169", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
context171: BinaryAssociation = BinaryAssociation(
    name="context171",
    ends={
        Property(name="Mapping", type=FlatQVT_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Mapping", type=Mapping, multiplicity=Multiplicity(0, 1))
    }
)
local172: BinaryAssociation = BinaryAssociation(
    name="local172",
    ends={
        Property(name="Mapping174", type=FlatQVT_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Mapping173", type=Mapping, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refinement175: BinaryAssociation = BinaryAssociation(
    name="refinement175",
    ends={
        Property(name="Mapping177", type=FlatQVT_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Mapping176", type=Mapping, multiplicity=Multiplicity(0, 9999))
    }
)
specification178: BinaryAssociation = BinaryAssociation(
    name="specification178",
    ends={
        Property(name="Mapping180", type=FlatQVT_Mapping, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Mapping179", type=Mapping, multiplicity=Multiplicity(0, 9999))
    }
)
body166: BinaryAssociation = BinaryAssociation(
    name="body166",
    ends={
        Property(name="OclExpression167", type=FlatQVT_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_LoopExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initSection183: BinaryAssociation = BinaryAssociation(
    name="initSection183",
    ends={
        Property(name="OclExpression185", type=FlatQVT_MappingBody, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_MappingBody184", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
disjunct186: BinaryAssociation = BinaryAssociation(
    name="disjunct186",
    ends={
        Property(name="MappingOperation", type=FlatQVT_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_MappingOperation", type=MappingOperation, multiplicity=Multiplicity(0, 9999))
    }
)
inherited187: BinaryAssociation = BinaryAssociation(
    name="inherited187",
    ends={
        Property(name="MappingOperation189", type=FlatQVT_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_MappingOperation188", type=MappingOperation, multiplicity=Multiplicity(0, 9999))
    }
)
merged190: BinaryAssociation = BinaryAssociation(
    name="merged190",
    ends={
        Property(name="MappingOperation192", type=FlatQVT_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_MappingOperation191", type=MappingOperation, multiplicity=Multiplicity(0, 9999))
    }
)
endSection181: BinaryAssociation = BinaryAssociation(
    name="endSection181",
    ends={
        Property(name="OclExpression182", type=FlatQVT_MappingBody, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_MappingBody", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
when195: BinaryAssociation = BinaryAssociation(
    name="when195",
    ends={
        Property(name="OclExpression197", type=FlatQVT_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_MappingOperation196", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
where198: BinaryAssociation = BinaryAssociation(
    name="where198",
    ends={
        Property(name="OclExpression200", type=FlatQVT_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_MappingOperation199", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extent201: BinaryAssociation = BinaryAssociation(
    name="extent201",
    ends={
        Property(name="ModelParameter", type=FlatQVT_MappingParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_MappingParameter", type=ModelParameter, multiplicity=Multiplicity(0, 1))
    }
)
referredDomain202: BinaryAssociation = BinaryAssociation(
    name="referredDomain202",
    ends={
        Property(name="RelationDomain", type=FlatQVT_MappingParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_MappingParameter203", type=RelationDomain, multiplicity=Multiplicity(0, 1))
    }
)
additionalCondition204: BinaryAssociation = BinaryAssociation(
    name="additionalCondition204",
    ends={
        Property(name="OclExpression205", type=FlatQVT_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_ModelType", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refinedRelation193: BinaryAssociation = BinaryAssociation(
    name="refinedRelation193",
    ends={
        Property(name="Relation", type=FlatQVT_MappingOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_MappingOperation194", type=Relation, multiplicity=Multiplicity(0, 1))
    }
)
metamodel206: BinaryAssociation = BinaryAssociation(
    name="metamodel206",
    ends={
        Property(name="Package208", type=FlatQVT_ModelType, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_ModelType207", type=Package, multiplicity=Multiplicity(1, 9999))
    }
)
configProperty209: BinaryAssociation = BinaryAssociation(
    name="configProperty209",
    ends={
        Property(name="Property210", type=FlatQVT_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Module", type=Property_, multiplicity=Multiplicity(0, 9999))
    }
)
entry211: BinaryAssociation = BinaryAssociation(
    name="entry211",
    ends={
        Property(name="EntryOperation", type=FlatQVT_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Module212", type=EntryOperation, multiplicity=Multiplicity(0, 1))
    }
)
moduleImport213: BinaryAssociation = BinaryAssociation(
    name="moduleImport213",
    ends={
        Property(name="ModuleImport", type=FlatQVT_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Module214", type=ModuleImport, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedTag215: BinaryAssociation = BinaryAssociation(
    name="ownedTag215",
    ends={
        Property(name="Tag", type=FlatQVT_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Module216", type=Tag, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedVariable217: BinaryAssociation = BinaryAssociation(
    name="ownedVariable217",
    ends={
        Property(name="Variable219", type=FlatQVT_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Module218", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
usedModelType220: BinaryAssociation = BinaryAssociation(
    name="usedModelType220",
    ends={
        Property(name="ModelType", type=FlatQVT_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Module221", type=ModelType, multiplicity=Multiplicity(0, 9999))
    }
)
binding222: BinaryAssociation = BinaryAssociation(
    name="binding222",
    ends={
        Property(name="ModelType223", type=FlatQVT_ModuleImport, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_ModuleImport", type=ModelType, multiplicity=Multiplicity(0, 9999))
    }
)
importedModule224: BinaryAssociation = BinaryAssociation(
    name="importedModule224",
    ends={
        Property(name="Module", type=FlatQVT_ModuleImport, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_ModuleImport225", type=Module, multiplicity=Multiplicity(1, 1))
    }
)
module226: BinaryAssociation = BinaryAssociation(
    name="module226",
    ends={
        Property(name="Module228", type=FlatQVT_ModuleImport, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_ModuleImport227", type=Module, multiplicity=Multiplicity(0, 1))
    }
)
body229: BinaryAssociation = BinaryAssociation(
    name="body229",
    ends={
        Property(name="ConstructorBody", type=FlatQVT_ObjectExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_ObjectExp", type=ConstructorBody, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referredObject230: BinaryAssociation = BinaryAssociation(
    name="referredObject230",
    ends={
        Property(name="Variable232", type=FlatQVT_ObjectExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_ObjectExp231", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
part233: BinaryAssociation = BinaryAssociation(
    name="part233",
    ends={
        Property(name="PropertyTemplateItem", type=FlatQVT_ObjectTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_ObjectTemplateExp", type=PropertyTemplateItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredClass234: BinaryAssociation = BinaryAssociation(
    name="referredClass234",
    ends={
        Property(name="Class236", type=FlatQVT_ObjectTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_ObjectTemplateExp235", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
ownedParameter239: BinaryAssociation = BinaryAssociation(
    name="ownedParameter239",
    ends={
        Property(name="Parameter", type=FlatQVT_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Operation240", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
raisedException241: BinaryAssociation = BinaryAssociation(
    name="raisedException241",
    ends={
        Property(name="Type243", type=FlatQVT_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Operation242", type=Type, multiplicity=Multiplicity(0, 9999))
    }
)
content244: BinaryAssociation = BinaryAssociation(
    name="content244",
    ends={
        Property(name="OclExpression245", type=FlatQVT_OperationBody, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_OperationBody", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operation246: BinaryAssociation = BinaryAssociation(
    name="operation246",
    ends={
        Property(name="ImperativeOperation248", type=FlatQVT_OperationBody, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_OperationBody247", type=ImperativeOperation, multiplicity=Multiplicity(0, 1))
    }
)
variable249: BinaryAssociation = BinaryAssociation(
    name="variable249",
    ends={
        Property(name="Variable251", type=FlatQVT_OperationBody, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_OperationBody250", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument252: BinaryAssociation = BinaryAssociation(
    name="argument252",
    ends={
        Property(name="OclExpression253", type=FlatQVT_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_OperationCallExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
class237: BinaryAssociation = BinaryAssociation(
    name="class237",
    ends={
        Property(name="Class238", type=FlatQVT_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Operation", type=Class_, multiplicity=Multiplicity(0, 1))
    }
)
referredOperation254: BinaryAssociation = BinaryAssociation(
    name="referredOperation254",
    ends={
        Property(name="Operation256", type=FlatQVT_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_OperationCallExp255", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
intermediateClass257: BinaryAssociation = BinaryAssociation(
    name="intermediateClass257",
    ends={
        Property(name="Class258", type=FlatQVT_OperationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_OperationalTransformation", type=Class_, multiplicity=Multiplicity(0, 9999))
    }
)
intermediateProperty259: BinaryAssociation = BinaryAssociation(
    name="intermediateProperty259",
    ends={
        Property(name="Property261", type=FlatQVT_OperationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_OperationalTransformation260", type=Property_, multiplicity=Multiplicity(0, 9999))
    }
)
refined265: BinaryAssociation = BinaryAssociation(
    name="refined265",
    ends={
        Property(name="RelationalTransformation267", type=FlatQVT_OperationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_OperationalTransformation266", type=RelationalTransformation, multiplicity=Multiplicity(0, 1))
    }
)
relation268: BinaryAssociation = BinaryAssociation(
    name="relation268",
    ends={
        Property(name="Relation270", type=FlatQVT_OperationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_OperationalTransformation269", type=Relation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
part271: BinaryAssociation = BinaryAssociation(
    name="part271",
    ends={
        Property(name="OrderedTupleLiteralPart", type=FlatQVT_OrderedTupleLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_OrderedTupleLiteralExp", type=OrderedTupleLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value272: BinaryAssociation = BinaryAssociation(
    name="value272",
    ends={
        Property(name="OclExpression273", type=FlatQVT_OrderedTupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_OrderedTupleLiteralPart", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
modelParameter262: BinaryAssociation = BinaryAssociation(
    name="modelParameter262",
    ends={
        Property(name="ModelParameter264", type=FlatQVT_OperationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_OperationalTransformation263", type=ModelParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elementType274: BinaryAssociation = BinaryAssociation(
    name="elementType274",
    ends={
        Property(name="Type275", type=FlatQVT_OrderedTupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_OrderedTupleType", type=Type, multiplicity=Multiplicity(0, 9999))
    }
)
nestedPackage276: BinaryAssociation = BinaryAssociation(
    name="nestedPackage276",
    ends={
        Property(name="Package277", type=FlatQVT_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Package", type=Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestingPackage278: BinaryAssociation = BinaryAssociation(
    name="nestingPackage278",
    ends={
        Property(name="Package280", type=FlatQVT_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Package279", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
ownedType281: BinaryAssociation = BinaryAssociation(
    name="ownedType281",
    ends={
        Property(name="Type283", type=FlatQVT_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Package282", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
operation284: BinaryAssociation = BinaryAssociation(
    name="operation284",
    ends={
        Property(name="Operation285", type=FlatQVT_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Parameter", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
bindsTo286: BinaryAssociation = BinaryAssociation(
    name="bindsTo286",
    ends={
        Property(name="Variable287", type=FlatQVT_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Pattern", type=Variable, multiplicity=Multiplicity(0, 9999))
    }
)
predicate288: BinaryAssociation = BinaryAssociation(
    name="predicate288",
    ends={
        Property(name="Predicate", type=FlatQVT_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Pattern289", type=Predicate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
conditionExpression290: BinaryAssociation = BinaryAssociation(
    name="conditionExpression290",
    ends={
        Property(name="OclExpression291", type=FlatQVT_Predicate, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Predicate", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
pattern292: BinaryAssociation = BinaryAssociation(
    name="pattern292",
    ends={
        Property(name="Pattern", type=FlatQVT_Predicate, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Predicate293", type=Pattern, multiplicity=Multiplicity(1, 1))
    }
)
opposite296: BinaryAssociation = BinaryAssociation(
    name="opposite296",
    ends={
        Property(name="Property298", type=FlatQVT_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Property297", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
slotExpression299: BinaryAssociation = BinaryAssociation(
    name="slotExpression299",
    ends={
        Property(name="OclExpression300", type=FlatQVT_PropertyAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_PropertyAssignment", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
targetProperty301: BinaryAssociation = BinaryAssociation(
    name="targetProperty301",
    ends={
        Property(name="Property303", type=FlatQVT_PropertyAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_PropertyAssignment302", type=Property_, multiplicity=Multiplicity(1, 1))
    }
)
referredProperty304: BinaryAssociation = BinaryAssociation(
    name="referredProperty304",
    ends={
        Property(name="Property305", type=FlatQVT_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_PropertyCallExp", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
class294: BinaryAssociation = BinaryAssociation(
    name="class294",
    ends={
        Property(name="Class295", type=FlatQVT_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Property", type=Class_, multiplicity=Multiplicity(0, 1))
    }
)
referredProperty307: BinaryAssociation = BinaryAssociation(
    name="referredProperty307",
    ends={
        Property(name="Property309", type=FlatQVT_PropertyTemplateItem, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_PropertyTemplateItem308", type=Property_, multiplicity=Multiplicity(1, 1))
    }
)
value310: BinaryAssociation = BinaryAssociation(
    name="value310",
    ends={
        Property(name="OclExpression312", type=FlatQVT_PropertyTemplateItem, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_PropertyTemplateItem311", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
argument313: BinaryAssociation = BinaryAssociation(
    name="argument313",
    ends={
        Property(name="OclExpression314", type=FlatQVT_RaiseExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_RaiseExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exception315: BinaryAssociation = BinaryAssociation(
    name="exception315",
    ends={
        Property(name="Type317", type=FlatQVT_RaiseExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_RaiseExp316", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
objContainer306: BinaryAssociation = BinaryAssociation(
    name="objContainer306",
    ends={
        Property(name="ObjectTemplateExp", type=FlatQVT_PropertyTemplateItem, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_PropertyTemplateItem", type=ObjectTemplateExp, multiplicity=Multiplicity(1, 1))
    }
)
operationalImpl318: BinaryAssociation = BinaryAssociation(
    name="operationalImpl318",
    ends={
        Property(name="RelationImplementation", type=FlatQVT_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Relation", type=RelationImplementation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable319: BinaryAssociation = BinaryAssociation(
    name="variable319",
    ends={
        Property(name="Variable321", type=FlatQVT_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Relation320", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
when322: BinaryAssociation = BinaryAssociation(
    name="when322",
    ends={
        Property(name="Pattern324", type=FlatQVT_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Relation323", type=Pattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
where325: BinaryAssociation = BinaryAssociation(
    name="where325",
    ends={
        Property(name="Pattern327", type=FlatQVT_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Relation326", type=Pattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
argument328: BinaryAssociation = BinaryAssociation(
    name="argument328",
    ends={
        Property(name="OclExpression329", type=FlatQVT_RelationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_RelationCallExp", type=OclExpression, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
referredRelation330: BinaryAssociation = BinaryAssociation(
    name="referredRelation330",
    ends={
        Property(name="Relation332", type=FlatQVT_RelationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_RelationCallExp331", type=Relation, multiplicity=Multiplicity(1, 1))
    }
)
defaultAssignment333: BinaryAssociation = BinaryAssociation(
    name="defaultAssignment333",
    ends={
        Property(name="RelationDomainAssignment", type=FlatQVT_RelationDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_RelationDomain", type=RelationDomainAssignment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pattern334: BinaryAssociation = BinaryAssociation(
    name="pattern334",
    ends={
        Property(name="DomainPattern", type=FlatQVT_RelationDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_RelationDomain335", type=DomainPattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rootVariable336: BinaryAssociation = BinaryAssociation(
    name="rootVariable336",
    ends={
        Property(name="Variable338", type=FlatQVT_RelationDomain, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_RelationDomain337", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
valueExp339: BinaryAssociation = BinaryAssociation(
    name="valueExp339",
    ends={
        Property(name="OclExpression340", type=FlatQVT_RelationDomainAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_RelationDomainAssignment", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable341: BinaryAssociation = BinaryAssociation(
    name="variable341",
    ends={
        Property(name="Variable343", type=FlatQVT_RelationDomainAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_RelationDomainAssignment342", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
impl344: BinaryAssociation = BinaryAssociation(
    name="impl344",
    ends={
        Property(name="Operation345", type=FlatQVT_RelationImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_RelationImplementation", type=Operation, multiplicity=Multiplicity(1, 1))
    }
)
inDirectionOf346: BinaryAssociation = BinaryAssociation(
    name="inDirectionOf346",
    ends={
        Property(name="TypedModel348", type=FlatQVT_RelationImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_RelationImplementation347", type=TypedModel, multiplicity=Multiplicity(1, 1))
    }
)
ownedKey352: BinaryAssociation = BinaryAssociation(
    name="ownedKey352",
    ends={
        Property(name="Key", type=FlatQVT_RelationalTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_RelationalTransformation", type=Key, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value360: BinaryAssociation = BinaryAssociation(
    name="value360",
    ends={
        Property(name="OclExpression361", type=FlatQVT_ReturnExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_ReturnExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition353: BinaryAssociation = BinaryAssociation(
    name="condition353",
    ends={
        Property(name="OclExpression354", type=FlatQVT_ResolveExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_ResolveExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
domain362: BinaryAssociation = BinaryAssociation(
    name="domain362",
    ends={
        Property(name="Domain", type=FlatQVT_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Rule", type=Domain, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target355: BinaryAssociation = BinaryAssociation(
    name="target355",
    ends={
        Property(name="Variable357", type=FlatQVT_ResolveExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_ResolveExp356", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
relation349: BinaryAssociation = BinaryAssociation(
    name="relation349",
    ends={
        Property(name="Relation351", type=FlatQVT_RelationImplementation, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_RelationImplementation350", type=Relation, multiplicity=Multiplicity(0, 1))
    }
)
inMapping358: BinaryAssociation = BinaryAssociation(
    name="inMapping358",
    ends={
        Property(name="MappingOperation359", type=FlatQVT_ResolveInExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_ResolveInExp", type=MappingOperation, multiplicity=Multiplicity(0, 1))
    }
)
alternativePart368: BinaryAssociation = BinaryAssociation(
    name="alternativePart368",
    ends={
        Property(name="AltExp", type=FlatQVT_SwitchExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_SwitchExp", type=AltExp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
overrides363: BinaryAssociation = BinaryAssociation(
    name="overrides363",
    ends={
        Property(name="Rule365", type=FlatQVT_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Rule364", type=Rule, multiplicity=Multiplicity(0, 1))
    }
)
elsePart369: BinaryAssociation = BinaryAssociation(
    name="elsePart369",
    ends={
        Property(name="OclExpression371", type=FlatQVT_SwitchExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_SwitchExp370", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transformation366: BinaryAssociation = BinaryAssociation(
    name="transformation366",
    ends={
        Property(name="Transformation", type=FlatQVT_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Rule367", type=Transformation, multiplicity=Multiplicity(0, 1))
    }
)
element372: BinaryAssociation = BinaryAssociation(
    name="element372",
    ends={
        Property(name="FlatQVT_Tag", type=Element, multiplicity=Multiplicity(0, 9999)),
        Property(name="Element", type=FlatQVT_Tag, multiplicity=Multiplicity(1, 1))
    }
)
bindsTo373: BinaryAssociation = BinaryAssociation(
    name="bindsTo373",
    ends={
        Property(name="Variable374", type=FlatQVT_TemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_TemplateExp", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
where375: BinaryAssociation = BinaryAssociation(
    name="where375",
    ends={
        Property(name="OclExpression377", type=FlatQVT_TemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_TemplateExp376", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
extends378: BinaryAssociation = BinaryAssociation(
    name="extends378",
    ends={
        Property(name="Transformation379", type=FlatQVT_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Transformation", type=Transformation, multiplicity=Multiplicity(0, 1))
    }
)
modelParameter380: BinaryAssociation = BinaryAssociation(
    name="modelParameter380",
    ends={
        Property(name="TypedModel382", type=FlatQVT_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Transformation381", type=TypedModel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedTag383: BinaryAssociation = BinaryAssociation(
    name="ownedTag383",
    ends={
        Property(name="Tag385", type=FlatQVT_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Transformation384", type=Tag, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rule386: BinaryAssociation = BinaryAssociation(
    name="rule386",
    ends={
        Property(name="Rule388", type=FlatQVT_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Transformation387", type=Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
part393: BinaryAssociation = BinaryAssociation(
    name="part393",
    ends={
        Property(name="TupleLiteralPart", type=FlatQVT_TupleLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_TupleLiteralExp", type=TupleLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute394: BinaryAssociation = BinaryAssociation(
    name="attribute394",
    ends={
        Property(name="Property395", type=FlatQVT_TupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_TupleLiteralPart", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
tupleLiteralExp396: BinaryAssociation = BinaryAssociation(
    name="tupleLiteralExp396",
    ends={
        Property(name="TupleLiteralExp", type=FlatQVT_TupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_TupleLiteralPart397", type=TupleLiteralExp, multiplicity=Multiplicity(0, 1))
    }
)
value398: BinaryAssociation = BinaryAssociation(
    name="value398",
    ends={
        Property(name="OclExpression400", type=FlatQVT_TupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_TupleLiteralPart399", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exceptClause389: BinaryAssociation = BinaryAssociation(
    name="exceptClause389",
    ends={
        Property(name="CatchExp", type=FlatQVT_TryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_TryExp", type=CatchExp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tryBody390: BinaryAssociation = BinaryAssociation(
    name="tryBody390",
    ends={
        Property(name="OclExpression392", type=FlatQVT_TryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_TryExp391", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredType403: BinaryAssociation = BinaryAssociation(
    name="referredType403",
    ends={
        Property(name="Type404", type=FlatQVT_TypeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_TypeExp", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
package401: BinaryAssociation = BinaryAssociation(
    name="package401",
    ends={
        Property(name="Package402", type=FlatQVT_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Type", type=Package, multiplicity=Multiplicity(0, 1))
    }
)
type405: BinaryAssociation = BinaryAssociation(
    name="type405",
    ends={
        Property(name="FlatQVT_TypedElement", type=Type, multiplicity=Multiplicity(0, 1)),
        Property(name="Type406", type=FlatQVT_TypedElement, multiplicity=Multiplicity(1, 1))
    }
)
dependsOn407: BinaryAssociation = BinaryAssociation(
    name="dependsOn407",
    ends={
        Property(name="TypedModel408", type=FlatQVT_TypedModel, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_TypedModel", type=TypedModel, multiplicity=Multiplicity(0, 9999))
    }
)
transformation409: BinaryAssociation = BinaryAssociation(
    name="transformation409",
    ends={
        Property(name="Transformation411", type=FlatQVT_TypedModel, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_TypedModel410", type=Transformation, multiplicity=Multiplicity(1, 1))
    }
)
base415: BinaryAssociation = BinaryAssociation(
    name="base415",
    ends={
        Property(name="Type416", type=FlatQVT_Typedef, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Typedef", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
condition417: BinaryAssociation = BinaryAssociation(
    name="condition417",
    ends={
        Property(name="OclExpression419", type=FlatQVT_Typedef, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Typedef418", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
usedPackage412: BinaryAssociation = BinaryAssociation(
    name="usedPackage412",
    ends={
        Property(name="Package414", type=FlatQVT_TypedModel, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_TypedModel413", type=Package, multiplicity=Multiplicity(1, 9999))
    }
)
item420: BinaryAssociation = BinaryAssociation(
    name="item420",
    ends={
        Property(name="OclExpression421", type=FlatQVT_UnlinkExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_UnlinkExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target422: BinaryAssociation = BinaryAssociation(
    name="target422",
    ends={
        Property(name="OclExpression424", type=FlatQVT_UnlinkExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_UnlinkExp423", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source425: BinaryAssociation = BinaryAssociation(
    name="source425",
    ends={
        Property(name="OclExpression426", type=FlatQVT_UnpackExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_UnpackExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ctxOwner430: BinaryAssociation = BinaryAssociation(
    name="ctxOwner430",
    ends={
        Property(name="ImperativeOperation431", type=FlatQVT_VarParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_VarParameter", type=ImperativeOperation, multiplicity=Multiplicity(0, 1))
    }
)
targetVariable427: BinaryAssociation = BinaryAssociation(
    name="targetVariable427",
    ends={
        Property(name="Variable429", type=FlatQVT_UnpackExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_UnpackExp428", type=Variable, multiplicity=Multiplicity(1, 9999))
    }
)
initExpression435: BinaryAssociation = BinaryAssociation(
    name="initExpression435",
    ends={
        Property(name="OclExpression436", type=FlatQVT_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Variable", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
letExp437: BinaryAssociation = BinaryAssociation(
    name="letExp437",
    ends={
        Property(name="LetExp", type=FlatQVT_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Variable438", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
representedParameter439: BinaryAssociation = BinaryAssociation(
    name="representedParameter439",
    ends={
        Property(name="Parameter441", type=FlatQVT_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_Variable440", type=Parameter_, multiplicity=Multiplicity(0, 1))
    }
)
resOwner432: BinaryAssociation = BinaryAssociation(
    name="resOwner432",
    ends={
        Property(name="ImperativeOperation434", type=FlatQVT_VarParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_VarParameter433", type=ImperativeOperation, multiplicity=Multiplicity(0, 1))
    }
)
referredVariable444: BinaryAssociation = BinaryAssociation(
    name="referredVariable444",
    ends={
        Property(name="Variable445", type=FlatQVT_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_VariableExp", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
referredVariable446: BinaryAssociation = BinaryAssociation(
    name="referredVariable446",
    ends={
        Property(name="Variable447", type=FlatQVT_VariableInitExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_VariableInitExp", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
targetVariable442: BinaryAssociation = BinaryAssociation(
    name="targetVariable442",
    ends={
        Property(name="Variable443", type=FlatQVT_VariableAssignment, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_VariableAssignment", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
body448: BinaryAssociation = BinaryAssociation(
    name="body448",
    ends={
        Property(name="OclExpression449", type=FlatQVT_WhileExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_WhileExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition450: BinaryAssociation = BinaryAssociation(
    name="condition450",
    ends={
        Property(name="OclExpression452", type=FlatQVT_WhileExp, multiplicity=Multiplicity(1, 1)),
        Property(name="FlatQVT_WhileExp451", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_FlatQVT_AltExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=FlatQVT_AltExp)
gen_FlatQVT_AssertExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=FlatQVT_AssertExp)
gen_FlatQVT_AnyType_Type = Generalization(general=Type, specific=FlatQVT_AnyType)
gen_FlatQVT_Assignment_Element = Generalization(general=Element, specific=FlatQVT_Assignment)
gen_FlatQVT_AssignExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=FlatQVT_AssignExp)
gen_FlatQVT_BagType_CollectionType = Generalization(general=CollectionType, specific=FlatQVT_BagType)
gen_FlatQVT_BlockExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=FlatQVT_BlockExp)
gen_FlatQVT_BooleanLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=FlatQVT_BooleanLiteralExp)
gen_FlatQVT_BottomPattern_CorePattern = Generalization(general=CorePattern, specific=FlatQVT_BottomPattern)
gen_FlatQVT_BreakExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=FlatQVT_BreakExp)
gen_FlatQVT_CallExp_OclExpression = Generalization(general=OclExpression, specific=FlatQVT_CallExp)
gen_FlatQVT_Class_Type = Generalization(general=Type, specific=FlatQVT_Class)
gen_FlatQVT_CatchExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=FlatQVT_CatchExp)
gen_FlatQVT_CollectionLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=FlatQVT_CollectionLiteralExp)
gen_FlatQVT_CollectionItem_CollectionLiteralPart = Generalization(general=CollectionLiteralPart, specific=FlatQVT_CollectionItem)
gen_FlatQVT_CollectionRange_CollectionLiteralPart = Generalization(general=CollectionLiteralPart, specific=FlatQVT_CollectionRange)
gen_FlatQVT_CollectionLiteralPart_TypedElement = Generalization(general=TypedElement, specific=FlatQVT_CollectionLiteralPart)
gen_FlatQVT_CollectionTemplateExp_TemplateExp = Generalization(general=TemplateExp, specific=FlatQVT_CollectionTemplateExp)
gen_FlatQVT_ComputeExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=FlatQVT_ComputeExp)
gen_FlatQVT_CollectionType_DataType = Generalization(general=DataType, specific=FlatQVT_CollectionType)
gen_FlatQVT_Comment_Element = Generalization(general=Element, specific=FlatQVT_Comment)
gen_FlatQVT_Constructor_ImperativeOperation = Generalization(general=ImperativeOperation, specific=FlatQVT_Constructor)
gen_FlatQVT_ConstructorBody_OperationBody = Generalization(general=OperationBody, specific=FlatQVT_ConstructorBody)
gen_FlatQVT_ContextualProperty_Property = Generalization(general=Property_, specific=FlatQVT_ContextualProperty)
gen_FlatQVT_CoreDomain_Domain = Generalization(general=Domain, specific=FlatQVT_CoreDomain)
gen_FlatQVT_CoreDomain_Area = Generalization(general=Area, specific=FlatQVT_CoreDomain)
gen_FlatQVT_CorePattern_Pattern = Generalization(general=Pattern, specific=FlatQVT_CorePattern)
gen_FlatQVT_DataType_Type = Generalization(general=Type, specific=FlatQVT_DataType)
gen_FlatQVT_DictLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=FlatQVT_DictLiteralExp)
gen_FlatQVT_ContinueExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=FlatQVT_ContinueExp)
gen_FlatQVT_DictLiteralPart_Element = Generalization(general=Element, specific=FlatQVT_DictLiteralPart)
gen_FlatQVT_DictionaryType_CollectionType = Generalization(general=CollectionType, specific=FlatQVT_DictionaryType)
gen_FlatQVT_Domain_NamedElement = Generalization(general=NamedElement, specific=FlatQVT_Domain)
gen_FlatQVT_DomainPattern_Pattern = Generalization(general=Pattern, specific=FlatQVT_DomainPattern)
gen_FlatQVT_Element_Object = Generalization(general=Object, specific=FlatQVT_Element)
gen_FlatQVT_EnforcementOperation_Element = Generalization(general=Element, specific=FlatQVT_EnforcementOperation)
gen_FlatQVT_EntryOperation_ImperativeOperation = Generalization(general=ImperativeOperation, specific=FlatQVT_EntryOperation)
gen_FlatQVT_EnumLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=FlatQVT_EnumLiteralExp)
gen_FlatQVT_Enumeration_DataType = Generalization(general=DataType, specific=FlatQVT_Enumeration)
gen_FlatQVT_EnumerationLiteral_NamedElement = Generalization(general=NamedElement, specific=FlatQVT_EnumerationLiteral)
gen_FlatQVT_ExpressionInOcl_TypedElement = Generalization(general=TypedElement, specific=FlatQVT_ExpressionInOcl)
gen_FlatQVT_Extent_Object = Generalization(general=Object, specific=FlatQVT_Extent)
gen_FlatQVT_Factory_Element = Generalization(general=Element, specific=FlatQVT_Factory)
gen_FlatQVT_FeatureCallExp_CallExp = Generalization(general=CallExp, specific=FlatQVT_FeatureCallExp)
gen_FlatQVT_ForExp_ImperativeLoopExp = Generalization(general=ImperativeLoopExp, specific=FlatQVT_ForExp)
gen_FlatQVT_Function_Operation = Generalization(general=Operation, specific=FlatQVT_Function)
gen_FlatQVT_FunctionParameter_Variable = Generalization(general=Variable, specific=FlatQVT_FunctionParameter)
gen_FlatQVT_FunctionParameter_Parameter = Generalization(general=Parameter_, specific=FlatQVT_FunctionParameter)
gen_FlatQVT_GuardPattern_CorePattern = Generalization(general=CorePattern, specific=FlatQVT_GuardPattern)
gen_FlatQVT_ImperativeCallExp_OperationCallExp = Generalization(general=OperationCallExp, specific=FlatQVT_ImperativeCallExp)
gen_FlatQVT_ImperativeCallExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=FlatQVT_ImperativeCallExp)
gen_FlatQVT_ImperativeExpression_OclExpression = Generalization(general=OclExpression, specific=FlatQVT_ImperativeExpression)
gen_FlatQVT_Helper_ImperativeOperation = Generalization(general=ImperativeOperation, specific=FlatQVT_Helper)
gen_FlatQVT_IfExp_OclExpression = Generalization(general=OclExpression, specific=FlatQVT_IfExp)
gen_FlatQVT_ImperativeLoopExp_LoopExp = Generalization(general=LoopExp, specific=FlatQVT_ImperativeLoopExp)
gen_FlatQVT_ImperativeLoopExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=FlatQVT_ImperativeLoopExp)
gen_FlatQVT_ImperativeOperation_Operation = Generalization(general=Operation, specific=FlatQVT_ImperativeOperation)
gen_FlatQVT_ImperativeIterateExp_ImperativeLoopExp = Generalization(general=ImperativeLoopExp, specific=FlatQVT_ImperativeIterateExp)
gen_FlatQVT_IntegerLiteralExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=FlatQVT_IntegerLiteralExp)
gen_FlatQVT_InvalidLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=FlatQVT_InvalidLiteralExp)
gen_FlatQVT_InvalidType_Type = Generalization(general=Type, specific=FlatQVT_InvalidType)
gen_FlatQVT_InstantiationExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=FlatQVT_InstantiationExp)
gen_FlatQVT_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=FlatQVT_IteratorExp)
gen_FlatQVT_Key_Element = Generalization(general=Element, specific=FlatQVT_Key)
gen_FlatQVT_LetExp_OclExpression = Generalization(general=OclExpression, specific=FlatQVT_LetExp)
gen_FlatQVT_IterateExp_LoopExp = Generalization(general=LoopExp, specific=FlatQVT_IterateExp)
gen_FlatQVT_Library_Module = Generalization(general=Module, specific=FlatQVT_Library)
gen_FlatQVT_ListLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=FlatQVT_ListLiteralExp)
gen_FlatQVT_ListType_CollectionType = Generalization(general=CollectionType, specific=FlatQVT_ListType)
gen_FlatQVT_LiteralExp_OclExpression = Generalization(general=OclExpression, specific=FlatQVT_LiteralExp)
gen_FlatQVT_LogExp_OperationCallExp = Generalization(general=OperationCallExp, specific=FlatQVT_LogExp)
gen_FlatQVT_LogExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=FlatQVT_LogExp)
gen_FlatQVT_LoopExp_CallExp = Generalization(general=CallExp, specific=FlatQVT_LoopExp)
gen_FlatQVT_LoopExp_OclExpression = Generalization(general=OclExpression, specific=FlatQVT_LoopExp)
gen_FlatQVT_Mapping_Rule = Generalization(general=Rule, specific=FlatQVT_Mapping)
gen_FlatQVT_Mapping_Area = Generalization(general=Area, specific=FlatQVT_Mapping)
gen_FlatQVT_MappingBody_OperationBody = Generalization(general=OperationBody, specific=FlatQVT_MappingBody)
gen_FlatQVT_MappingCallExp_ImperativeCallExp = Generalization(general=ImperativeCallExp, specific=FlatQVT_MappingCallExp)
gen_FlatQVT_MappingOperation_ImperativeOperation = Generalization(general=ImperativeOperation, specific=FlatQVT_MappingOperation)
gen_FlatQVT_MappingParameter_VarParameter = Generalization(general=VarParameter, specific=FlatQVT_MappingParameter)
gen_FlatQVT_ModelParameter_VarParameter = Generalization(general=VarParameter, specific=FlatQVT_ModelParameter)
gen_FlatQVT_ModelType_Class = Generalization(general=Class_, specific=FlatQVT_ModelType)
gen_FlatQVT_Module_Class = Generalization(general=Class_, specific=FlatQVT_Module)
gen_FlatQVT_Module_Package = Generalization(general=Package, specific=FlatQVT_Module)
gen_FlatQVT_ModuleImport_Element = Generalization(general=Element, specific=FlatQVT_ModuleImport)
gen_FlatQVT_NamedElement_Element = Generalization(general=Element, specific=FlatQVT_NamedElement)
gen_FlatQVT_NumericLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=FlatQVT_NumericLiteralExp)
gen_FlatQVT_ObjectExp_InstantiationExp = Generalization(general=InstantiationExp, specific=FlatQVT_ObjectExp)
gen_FlatQVT_ObjectTemplateExp_TemplateExp = Generalization(general=TemplateExp, specific=FlatQVT_ObjectTemplateExp)
gen_FlatQVT_OclExpression_TypedElement = Generalization(general=TypedElement, specific=FlatQVT_OclExpression)
gen_FlatQVT_Operation_TypedElement = Generalization(general=TypedElement, specific=FlatQVT_Operation)
gen_FlatQVT_Operation_MultiplicityElement = Generalization(general=MultiplicityElement, specific=FlatQVT_Operation)
gen_FlatQVT_NavigationCallExp_FeatureCallExp = Generalization(general=FeatureCallExp, specific=FlatQVT_NavigationCallExp)
gen_FlatQVT_NullLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=FlatQVT_NullLiteralExp)
gen_FlatQVT_OperationBody_Element = Generalization(general=Element, specific=FlatQVT_OperationBody)
gen_FlatQVT_OperationCallExp_FeatureCallExp = Generalization(general=FeatureCallExp, specific=FlatQVT_OperationCallExp)
gen_FlatQVT_OperationalTransformation_Module = Generalization(general=Module, specific=FlatQVT_OperationalTransformation)
gen_FlatQVT_OppositePropertyCallExp_PropertyCallExp = Generalization(general=PropertyCallExp, specific=FlatQVT_OppositePropertyCallExp)
gen_FlatQVT_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=FlatQVT_OrderedSetType)
gen_FlatQVT_OrderedTupleLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=FlatQVT_OrderedTupleLiteralExp)
gen_FlatQVT_OrderedTupleLiteralPart_Element = Generalization(general=Element, specific=FlatQVT_OrderedTupleLiteralPart)
gen_FlatQVT_Package_NamedElement = Generalization(general=NamedElement, specific=FlatQVT_Package)
gen_FlatQVT_Parameter_TypedElement = Generalization(general=TypedElement, specific=FlatQVT_Parameter)
gen_FlatQVT_Parameter_MultiplicityElement = Generalization(general=MultiplicityElement, specific=FlatQVT_Parameter)
gen_FlatQVT_Pattern_Element = Generalization(general=Element, specific=FlatQVT_Pattern)
gen_FlatQVT_Predicate_Element = Generalization(general=Element, specific=FlatQVT_Predicate)
gen_FlatQVT_PrimitiveLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=FlatQVT_PrimitiveLiteralExp)
gen_FlatQVT_PrimitiveType_DataType = Generalization(general=DataType, specific=FlatQVT_PrimitiveType)
gen_FlatQVT_Property_TypedElement = Generalization(general=TypedElement, specific=FlatQVT_Property)
gen_FlatQVT_Property_MultiplicityElement = Generalization(general=MultiplicityElement, specific=FlatQVT_Property)
gen_FlatQVT_OrderedTupleType_Class = Generalization(general=Class_, specific=FlatQVT_OrderedTupleType)
gen_FlatQVT_PropertyAssignment_Assignment = Generalization(general=Assignment, specific=FlatQVT_PropertyAssignment)
gen_FlatQVT_PropertyCallExp_NavigationCallExp = Generalization(general=NavigationCallExp, specific=FlatQVT_PropertyCallExp)
gen_FlatQVT_PropertyTemplateItem_Element = Generalization(general=Element, specific=FlatQVT_PropertyTemplateItem)
gen_FlatQVT_RaiseExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=FlatQVT_RaiseExp)
gen_FlatQVT_RealizedVariable_Variable = Generalization(general=Variable, specific=FlatQVT_RealizedVariable)
gen_FlatQVT_ReflectiveCollection_Object = Generalization(general=Object, specific=FlatQVT_ReflectiveCollection)
gen_FlatQVT_ReflectiveSequence_ReflectiveCollection = Generalization(general=ReflectiveCollection, specific=FlatQVT_ReflectiveSequence)
gen_FlatQVT_RealLiteralExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=FlatQVT_RealLiteralExp)
gen_FlatQVT_Relation_Rule = Generalization(general=Rule, specific=FlatQVT_Relation)
gen_FlatQVT_RelationDomain_Domain = Generalization(general=Domain, specific=FlatQVT_RelationDomain)
gen_FlatQVT_RelationCallExp_OclExpression = Generalization(general=OclExpression, specific=FlatQVT_RelationCallExp)
gen_FlatQVT_RelationImplementation_Element = Generalization(general=Element, specific=FlatQVT_RelationImplementation)
gen_FlatQVT_RelationDomainAssignment_Element = Generalization(general=Element, specific=FlatQVT_RelationDomainAssignment)
gen_FlatQVT_RelationalTransformation_Transformation = Generalization(general=Transformation, specific=FlatQVT_RelationalTransformation)
gen_FlatQVT_ReturnExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=FlatQVT_ReturnExp)
gen_FlatQVT_ResolveExp_CallExp = Generalization(general=CallExp, specific=FlatQVT_ResolveExp)
gen_FlatQVT_ResolveExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=FlatQVT_ResolveExp)
gen_FlatQVT_Rule_NamedElement = Generalization(general=NamedElement, specific=FlatQVT_Rule)
gen_FlatQVT_ResolveInExp_ResolveExp = Generalization(general=ResolveExp, specific=FlatQVT_ResolveInExp)
gen_FlatQVT_StringLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=FlatQVT_StringLiteralExp)
gen_FlatQVT_SwitchExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=FlatQVT_SwitchExp)
gen_FlatQVT_SequenceType_CollectionType = Generalization(general=CollectionType, specific=FlatQVT_SequenceType)
gen_FlatQVT_SetType_CollectionType = Generalization(general=CollectionType, specific=FlatQVT_SetType)
gen_FlatQVT_TemplateExp_LiteralExp = Generalization(general=LiteralExp, specific=FlatQVT_TemplateExp)
gen_FlatQVT_Tag_Element = Generalization(general=Element, specific=FlatQVT_Tag)
gen_FlatQVT_TryExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=FlatQVT_TryExp)
gen_FlatQVT_TemplateParameterType_Type = Generalization(general=Type, specific=FlatQVT_TemplateParameterType)
gen_FlatQVT_Transformation_Class = Generalization(general=Class_, specific=FlatQVT_Transformation)
gen_FlatQVT_Transformation_Package = Generalization(general=Package, specific=FlatQVT_Transformation)
gen_FlatQVT_TupleLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=FlatQVT_TupleLiteralExp)
gen_FlatQVT_TupleLiteralPart_TypedElement = Generalization(general=TypedElement, specific=FlatQVT_TupleLiteralPart)
gen_FlatQVT_TypeExp_OclExpression = Generalization(general=OclExpression, specific=FlatQVT_TypeExp)
gen_FlatQVT_TupleType_Class = Generalization(general=Class_, specific=FlatQVT_TupleType)
gen_FlatQVT_TupleType_DataType = Generalization(general=DataType, specific=FlatQVT_TupleType)
gen_FlatQVT_Type_NamedElement = Generalization(general=NamedElement, specific=FlatQVT_Type)
gen_FlatQVT_TypedModel_NamedElement = Generalization(general=NamedElement, specific=FlatQVT_TypedModel)
gen_FlatQVT_TypedElement_NamedElement = Generalization(general=NamedElement, specific=FlatQVT_TypedElement)
gen_FlatQVT_Typedef_Class = Generalization(general=Class_, specific=FlatQVT_Typedef)
gen_FlatQVT_UnlimitedNaturalExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=FlatQVT_UnlimitedNaturalExp)
gen_FlatQVT_UnlinkExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=FlatQVT_UnlinkExp)
gen_FlatQVT_URIExtent_Extent = Generalization(general=Extent, specific=FlatQVT_URIExtent)
gen_FlatQVT_UnpackExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=FlatQVT_UnpackExp)
gen_FlatQVT_VarParameter_Variable = Generalization(general=Variable, specific=FlatQVT_VarParameter)
gen_FlatQVT_VarParameter_Parameter = Generalization(general=Parameter_, specific=FlatQVT_VarParameter)
gen_FlatQVT_Variable_TypedElement = Generalization(general=TypedElement, specific=FlatQVT_Variable)
gen_FlatQVT_VariableExp_OclExpression = Generalization(general=OclExpression, specific=FlatQVT_VariableExp)
gen_FlatQVT_VariableInitExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=FlatQVT_VariableInitExp)
gen_FlatQVT_VariableAssignment_Assignment = Generalization(general=Assignment, specific=FlatQVT_VariableAssignment)
gen_FlatQVT_WhileExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=FlatQVT_WhileExp)
gen_FlatQVT_VoidType_Type = Generalization(general=Type, specific=FlatQVT_VoidType)

# Domain Model
domain_model = DomainModel(
    name="FlatQVT",
    types={FlatQVT_AltExp, ImperativeExpression, OclExpression, FlatQVT_Area, BottomPattern, GuardPattern, FlatQVT_AssertExp, FlatQVT_AnyType, Type, FlatQVT_Assignment, Element, LogExp, FlatQVT_AssignExp, FlatQVT_BagType, CollectionType, FlatQVT_BlockExp, FlatQVT_BooleanLiteralExp, PrimitiveLiteralExp, FlatQVT_BottomPattern, CorePattern, RealizedVariable, FlatQVT_BreakExp, FlatQVT_CallExp, Area, Assignment, EnforcementOperation, FlatQVT_Class, Property_, Operation, Class_, FlatQVT_CatchExp, FlatQVT_CollectionLiteralExp, LiteralExp, FlatQVT_CollectionItem, CollectionLiteralPart, CollectionLiteralExp, FlatQVT_CollectionRange, FlatQVT_CollectionLiteralPart, TypedElement, Variable, FlatQVT_CollectionTemplateExp, TemplateExp, NamedElement, FlatQVT_ComputeExp, FlatQVT_CollectionType, DataType, FlatQVT_Comment, FlatQVT_ConstructorBody, OperationBody, FlatQVT_ContextualProperty, FlatQVT_Constructor, ImperativeOperation, FlatQVT_CoreDomain, Domain, FlatQVT_CorePattern, Pattern, FlatQVT_DataType, FlatQVT_DictLiteralExp, FlatQVT_ContinueExp, FlatQVT_DictLiteralPart, DictLiteralPart, FlatQVT_DictionaryType, FlatQVT_Domain, Rule, TypedModel, FlatQVT_DomainPattern, FlatQVT_Element, Object, Comment, FlatQVT_EnforcementOperation, OperationCallExp, FlatQVT_EntryOperation, FlatQVT_EnumLiteralExp, EnumerationLiteral, FlatQVT_Enumeration, FlatQVT_EnumerationLiteral, Enumeration_, FlatQVT_ExpressionInOcl, FlatQVT_Extent, FlatQVT_Factory, Package, FlatQVT_FeatureCallExp, CallExp, FlatQVT_ForExp, ImperativeLoopExp, FlatQVT_Function, FlatQVT_FunctionParameter, Parameter_, FlatQVT_GuardPattern, FlatQVT_ImperativeCallExp, FlatQVT_ImperativeExpression, FlatQVT_Helper, FlatQVT_IfExp, FlatQVT_ImperativeOperation, VarParameter, FlatQVT_ImperativeIterateExp, FlatQVT_ImperativeLoopExp, LoopExp, FlatQVT_IntegerLiteralExp, NumericLiteralExp, FlatQVT_InvalidLiteralExp, FlatQVT_InvalidType, FlatQVT_IterateExp, FlatQVT_InstantiationExp, FlatQVT_Key, RelationalTransformation, FlatQVT_LetExp, FlatQVT_IteratorExp, Module, FlatQVT_ListLiteralExp, FlatQVT_ListType, FlatQVT_LiteralExp, FlatQVT_LogExp, FlatQVT_LoopExp, FlatQVT_Library, FlatQVT_Mapping, Mapping, FlatQVT_MappingBody, FlatQVT_MappingCallExp, ImperativeCallExp, FlatQVT_MappingOperation, MappingOperation, FlatQVT_MappingParameter, ModelParameter, RelationDomain, FlatQVT_ModelParameter, FlatQVT_ModelType, Relation, FlatQVT_Module, EntryOperation, ModuleImport, Tag, ModelType, FlatQVT_ModuleImport, FlatQVT_MultiplicityElement, FlatQVT_NamedElement, FlatQVT_NumericLiteralExp, FlatQVT_Object, FlatQVT_ObjectExp, InstantiationExp, ConstructorBody, FlatQVT_ObjectTemplateExp, PropertyTemplateItem, FlatQVT_OclExpression, FlatQVT_Operation, MultiplicityElement, FlatQVT_NavigationCallExp, FeatureCallExp, FlatQVT_NullLiteralExp, FlatQVT_OperationBody, FlatQVT_OperationCallExp, FlatQVT_OperationalTransformation, FlatQVT_OppositePropertyCallExp, PropertyCallExp, FlatQVT_OrderedSetType, FlatQVT_OrderedTupleLiteralExp, OrderedTupleLiteralPart, FlatQVT_OrderedTupleLiteralPart, FlatQVT_Package, FlatQVT_Parameter, FlatQVT_Pattern, Predicate, FlatQVT_Predicate, FlatQVT_PrimitiveLiteralExp, FlatQVT_PrimitiveType, FlatQVT_Property, FlatQVT_OrderedTupleType, FlatQVT_PropertyAssignment, FlatQVT_PropertyCallExp, NavigationCallExp, FlatQVT_PropertyTemplateItem, FlatQVT_RaiseExp, ObjectTemplateExp, FlatQVT_RealizedVariable, FlatQVT_ReflectiveCollection, FlatQVT_ReflectiveSequence, ReflectiveCollection, FlatQVT_RealLiteralExp, FlatQVT_Relation, RelationImplementation, FlatQVT_RelationDomain, RelationDomainAssignment, DomainPattern, FlatQVT_RelationCallExp, FlatQVT_RelationImplementation, FlatQVT_RelationDomainAssignment, FlatQVT_RelationalTransformation, Transformation, FlatQVT_ReturnExp, Key, FlatQVT_ResolveExp, FlatQVT_Rule, FlatQVT_ResolveInExp, ResolveExp, FlatQVT_StringLiteralExp, FlatQVT_SwitchExp, AltExp, FlatQVT_SequenceType, FlatQVT_SetType, FlatQVT_TemplateExp, FlatQVT_Tag, FlatQVT_TryExp, CatchExp, FlatQVT_TemplateParameterType, FlatQVT_Transformation, FlatQVT_TupleLiteralExp, TupleLiteralPart, FlatQVT_TupleLiteralPart, TupleLiteralExp, FlatQVT_TypeExp, FlatQVT_TupleType, FlatQVT_Type, FlatQVT_TypedModel, FlatQVT_TypedElement, FlatQVT_Typedef, FlatQVT_UnlimitedNaturalExp, FlatQVT_UnlinkExp, FlatQVT_URIExtent, Extent, FlatQVT_UnpackExp, FlatQVT_VarParameter, LetExp, FlatQVT_Variable, FlatQVT_VariableExp, FlatQVT_VariableInitExp, FlatQVT_VariableAssignment, FlatQVT_WhileExp, FlatQVT_VoidType, CollectionKind, DirectionKind, EnforcementMode, ImportKind, SeverityKind},
    associations={body0, bottomPattern4, guardPattern5, assertion7, condition1, left13, value16, log9, defaultValue11, body24, bottomPattern19, value21, enforcementOperation29, realizedVariable31, source33, area26, assignment27, ownedAttribute39, ownedOperation40, body35, exception37, superClass42, item44, collectionLiteralExp47, first48, part46, member53, referredCollectionType55, rest57, last50, annotatedElement61, body62, elementType59, context67, initExpression69, returnedElement64, variable75, overridden72, key78, value80, part77, keyType83, rule85, typedModel86, templateExpression88, ownedComment89, bottomPattern90, operationCallExp92, referredEnumLiteral94, ownedLiteral95, enumeration97, bodyExpression98, parameterVariable106, resultVariable109, package112, queryExpression113, contextVariable100, generatedType103, condition117, elseExpression119, thenExpression122, area115, condition127, body129, context130, overridden132, result134, target125, extent139, instantiatedClass142, argument137, identifies147, oppositePart149, part152, transformation155, in157, result145, element162, condition164, variable159, iterator168, context171, local172, refinement175, specification178, body166, initSection183, disjunct186, inherited187, merged190, endSection181, when195, where198, extent201, referredDomain202, additionalCondition204, refinedRelation193, metamodel206, configProperty209, entry211, moduleImport213, ownedTag215, ownedVariable217, usedModelType220, binding222, importedModule224, module226, body229, referredObject230, part233, referredClass234, ownedParameter239, raisedException241, content244, operation246, variable249, argument252, class237, referredOperation254, intermediateClass257, intermediateProperty259, refined265, relation268, part271, value272, modelParameter262, elementType274, nestedPackage276, nestingPackage278, ownedType281, operation284, bindsTo286, predicate288, conditionExpression290, pattern292, opposite296, slotExpression299, targetProperty301, referredProperty304, class294, referredProperty307, value310, argument313, exception315, objContainer306, operationalImpl318, variable319, when322, where325, argument328, referredRelation330, defaultAssignment333, pattern334, rootVariable336, valueExp339, variable341, impl344, inDirectionOf346, ownedKey352, value360, condition353, domain362, target355, relation349, inMapping358, alternativePart368, overrides363, elsePart369, transformation366, element372, bindsTo373, where375, extends378, modelParameter380, ownedTag383, rule386, part393, attribute394, tupleLiteralExp396, value398, exceptClause389, tryBody390, referredType403, package401, type405, dependsOn407, transformation409, base415, condition417, usedPackage412, item420, target422, source425, ctxOwner430, targetVariable427, initExpression435, letExp437, representedParameter439, resOwner432, referredVariable444, referredVariable446, targetVariable442, body448, condition450},
    generalizations={gen_FlatQVT_AltExp_ImperativeExpression, gen_FlatQVT_AssertExp_ImperativeExpression, gen_FlatQVT_AnyType_Type, gen_FlatQVT_Assignment_Element, gen_FlatQVT_AssignExp_ImperativeExpression, gen_FlatQVT_BagType_CollectionType, gen_FlatQVT_BlockExp_ImperativeExpression, gen_FlatQVT_BooleanLiteralExp_PrimitiveLiteralExp, gen_FlatQVT_BottomPattern_CorePattern, gen_FlatQVT_BreakExp_ImperativeExpression, gen_FlatQVT_CallExp_OclExpression, gen_FlatQVT_Class_Type, gen_FlatQVT_CatchExp_ImperativeExpression, gen_FlatQVT_CollectionLiteralExp_LiteralExp, gen_FlatQVT_CollectionItem_CollectionLiteralPart, gen_FlatQVT_CollectionRange_CollectionLiteralPart, gen_FlatQVT_CollectionLiteralPart_TypedElement, gen_FlatQVT_CollectionTemplateExp_TemplateExp, gen_FlatQVT_ComputeExp_ImperativeExpression, gen_FlatQVT_CollectionType_DataType, gen_FlatQVT_Comment_Element, gen_FlatQVT_Constructor_ImperativeOperation, gen_FlatQVT_ConstructorBody_OperationBody, gen_FlatQVT_ContextualProperty_Property, gen_FlatQVT_CoreDomain_Domain, gen_FlatQVT_CoreDomain_Area, gen_FlatQVT_CorePattern_Pattern, gen_FlatQVT_DataType_Type, gen_FlatQVT_DictLiteralExp_LiteralExp, gen_FlatQVT_ContinueExp_ImperativeExpression, gen_FlatQVT_DictLiteralPart_Element, gen_FlatQVT_DictionaryType_CollectionType, gen_FlatQVT_Domain_NamedElement, gen_FlatQVT_DomainPattern_Pattern, gen_FlatQVT_Element_Object, gen_FlatQVT_EnforcementOperation_Element, gen_FlatQVT_EntryOperation_ImperativeOperation, gen_FlatQVT_EnumLiteralExp_LiteralExp, gen_FlatQVT_Enumeration_DataType, gen_FlatQVT_EnumerationLiteral_NamedElement, gen_FlatQVT_ExpressionInOcl_TypedElement, gen_FlatQVT_Extent_Object, gen_FlatQVT_Factory_Element, gen_FlatQVT_FeatureCallExp_CallExp, gen_FlatQVT_ForExp_ImperativeLoopExp, gen_FlatQVT_Function_Operation, gen_FlatQVT_FunctionParameter_Variable, gen_FlatQVT_FunctionParameter_Parameter, gen_FlatQVT_GuardPattern_CorePattern, gen_FlatQVT_ImperativeCallExp_OperationCallExp, gen_FlatQVT_ImperativeCallExp_ImperativeExpression, gen_FlatQVT_ImperativeExpression_OclExpression, gen_FlatQVT_Helper_ImperativeOperation, gen_FlatQVT_IfExp_OclExpression, gen_FlatQVT_ImperativeLoopExp_LoopExp, gen_FlatQVT_ImperativeLoopExp_ImperativeExpression, gen_FlatQVT_ImperativeOperation_Operation, gen_FlatQVT_ImperativeIterateExp_ImperativeLoopExp, gen_FlatQVT_IntegerLiteralExp_NumericLiteralExp, gen_FlatQVT_InvalidLiteralExp_LiteralExp, gen_FlatQVT_InvalidType_Type, gen_FlatQVT_InstantiationExp_ImperativeExpression, gen_FlatQVT_IteratorExp_LoopExp, gen_FlatQVT_Key_Element, gen_FlatQVT_LetExp_OclExpression, gen_FlatQVT_IterateExp_LoopExp, gen_FlatQVT_Library_Module, gen_FlatQVT_ListLiteralExp_LiteralExp, gen_FlatQVT_ListType_CollectionType, gen_FlatQVT_LiteralExp_OclExpression, gen_FlatQVT_LogExp_OperationCallExp, gen_FlatQVT_LogExp_ImperativeExpression, gen_FlatQVT_LoopExp_CallExp, gen_FlatQVT_LoopExp_OclExpression, gen_FlatQVT_Mapping_Rule, gen_FlatQVT_Mapping_Area, gen_FlatQVT_MappingBody_OperationBody, gen_FlatQVT_MappingCallExp_ImperativeCallExp, gen_FlatQVT_MappingOperation_ImperativeOperation, gen_FlatQVT_MappingParameter_VarParameter, gen_FlatQVT_ModelParameter_VarParameter, gen_FlatQVT_ModelType_Class, gen_FlatQVT_Module_Class, gen_FlatQVT_Module_Package, gen_FlatQVT_ModuleImport_Element, gen_FlatQVT_NamedElement_Element, gen_FlatQVT_NumericLiteralExp_PrimitiveLiteralExp, gen_FlatQVT_ObjectExp_InstantiationExp, gen_FlatQVT_ObjectTemplateExp_TemplateExp, gen_FlatQVT_OclExpression_TypedElement, gen_FlatQVT_Operation_TypedElement, gen_FlatQVT_Operation_MultiplicityElement, gen_FlatQVT_NavigationCallExp_FeatureCallExp, gen_FlatQVT_NullLiteralExp_LiteralExp, gen_FlatQVT_OperationBody_Element, gen_FlatQVT_OperationCallExp_FeatureCallExp, gen_FlatQVT_OperationalTransformation_Module, gen_FlatQVT_OppositePropertyCallExp_PropertyCallExp, gen_FlatQVT_OrderedSetType_CollectionType, gen_FlatQVT_OrderedTupleLiteralExp_LiteralExp, gen_FlatQVT_OrderedTupleLiteralPart_Element, gen_FlatQVT_Package_NamedElement, gen_FlatQVT_Parameter_TypedElement, gen_FlatQVT_Parameter_MultiplicityElement, gen_FlatQVT_Pattern_Element, gen_FlatQVT_Predicate_Element, gen_FlatQVT_PrimitiveLiteralExp_LiteralExp, gen_FlatQVT_PrimitiveType_DataType, gen_FlatQVT_Property_TypedElement, gen_FlatQVT_Property_MultiplicityElement, gen_FlatQVT_OrderedTupleType_Class, gen_FlatQVT_PropertyAssignment_Assignment, gen_FlatQVT_PropertyCallExp_NavigationCallExp, gen_FlatQVT_PropertyTemplateItem_Element, gen_FlatQVT_RaiseExp_ImperativeExpression, gen_FlatQVT_RealizedVariable_Variable, gen_FlatQVT_ReflectiveCollection_Object, gen_FlatQVT_ReflectiveSequence_ReflectiveCollection, gen_FlatQVT_RealLiteralExp_NumericLiteralExp, gen_FlatQVT_Relation_Rule, gen_FlatQVT_RelationDomain_Domain, gen_FlatQVT_RelationCallExp_OclExpression, gen_FlatQVT_RelationImplementation_Element, gen_FlatQVT_RelationDomainAssignment_Element, gen_FlatQVT_RelationalTransformation_Transformation, gen_FlatQVT_ReturnExp_ImperativeExpression, gen_FlatQVT_ResolveExp_CallExp, gen_FlatQVT_ResolveExp_ImperativeExpression, gen_FlatQVT_Rule_NamedElement, gen_FlatQVT_ResolveInExp_ResolveExp, gen_FlatQVT_StringLiteralExp_PrimitiveLiteralExp, gen_FlatQVT_SwitchExp_ImperativeExpression, gen_FlatQVT_SequenceType_CollectionType, gen_FlatQVT_SetType_CollectionType, gen_FlatQVT_TemplateExp_LiteralExp, gen_FlatQVT_Tag_Element, gen_FlatQVT_TryExp_ImperativeExpression, gen_FlatQVT_TemplateParameterType_Type, gen_FlatQVT_Transformation_Class, gen_FlatQVT_Transformation_Package, gen_FlatQVT_TupleLiteralExp_LiteralExp, gen_FlatQVT_TupleLiteralPart_TypedElement, gen_FlatQVT_TypeExp_OclExpression, gen_FlatQVT_TupleType_Class, gen_FlatQVT_TupleType_DataType, gen_FlatQVT_Type_NamedElement, gen_FlatQVT_TypedModel_NamedElement, gen_FlatQVT_TypedElement_NamedElement, gen_FlatQVT_Typedef_Class, gen_FlatQVT_UnlimitedNaturalExp_NumericLiteralExp, gen_FlatQVT_UnlinkExp_ImperativeExpression, gen_FlatQVT_URIExtent_Extent, gen_FlatQVT_UnpackExp_ImperativeExpression, gen_FlatQVT_VarParameter_Variable, gen_FlatQVT_VarParameter_Parameter, gen_FlatQVT_Variable_TypedElement, gen_FlatQVT_VariableExp_OclExpression, gen_FlatQVT_VariableInitExp_ImperativeExpression, gen_FlatQVT_VariableAssignment_Assignment, gen_FlatQVT_WhileExp_ImperativeExpression, gen_FlatQVT_VoidType_Type},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)