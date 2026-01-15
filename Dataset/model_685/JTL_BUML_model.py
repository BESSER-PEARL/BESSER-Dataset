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
            EnumerationLiteral(name="OrderedSet"),
			EnumerationLiteral(name="Set"),
			EnumerationLiteral(name="Bag"),
			EnumerationLiteral(name="Sequence")
    }
)

SeverityKind: Enumeration = Enumeration(
    name="SeverityKind",
    literals={
            EnumerationLiteral(name="error"),
			EnumerationLiteral(name="fatal"),
			EnumerationLiteral(name="warning")
    }
)

# Classes
JTL_emof_Class = Class(name="JTL::emof::Class")
Type = Class(name="Type")
Property_ = Class(name="Property")
Class_ = Class(name="Class")
JTL_emof_DataType = Class(name="JTL::emof::DataType", is_abstract=True)
JTL_emof_Element = Class(name="JTL::emof::Element", is_abstract=True)
Object = Class(name="Object")
Tag = Class(name="Tag")
Comment = Class(name="Comment")
JTL_emof_Tag = Class(name="JTL::emof::Tag")
Element = Class(name="Element")
Operation = Class(name="Operation")
JTL_emof_Enumeration = Class(name="JTL::emof::Enumeration")
DataType = Class(name="DataType")
EnumerationLiteral = Class(name="EnumerationLiteral")
JTL_emof_NamedElement = Class(name="JTL::emof::NamedElement", is_abstract=True)
JTL_emof_Extent = Class(name="JTL::emof::Extent")
JTL_emof_Object = Class(name="JTL::emof::Object")
JTL_emof_Operation = Class(name="JTL::emof::Operation")
emof_MultiplicityElement = Class(name="emof::MultiplicityElement")
emof_TypedElement = Class(name="emof::TypedElement")
Parameter_ = Class(name="Parameter")
JTL_emof_MultiplicityElement = Class(name="JTL::emof::MultiplicityElement", is_abstract=True)
JTL_emof_Package = Class(name="JTL::emof::Package")
NamedElement = Class(name="NamedElement")
JTL_emof_Type = Class(name="JTL::emof::Type", is_abstract=True)
JTL_emof_Parameter = Class(name="JTL::emof::Parameter")
JTL_emof_EnumerationLiteral = Class(name="JTL::emof::EnumerationLiteral")
Enumeration_ = Class(name="Enumeration")
Package = Class(name="Package")
JTL_emof_TypedElement = Class(name="JTL::emof::TypedElement", is_abstract=True)
JTL_emof_PrimitiveType = Class(name="JTL::emof::PrimitiveType")
JTL_emof_URIExtent = Class(name="JTL::emof::URIExtent")
JTL_emof_Property = Class(name="JTL::emof::Property")
JTL_emof_Comment = Class(name="JTL::emof::Comment")
JTL_JTL_Transformation = Class(name="JTL::JTL::Transformation")
emof_Class = Class(name="emof::Class")
emof_Package = Class(name="emof::Package")
Model = Class(name="Model")
Relation = Class(name="Relation")
Extent = Class(name="Extent")
Domain = Class(name="Domain")
Where = Class(name="Where")
When = Class(name="When")
Variable = Class(name="Variable")
JTL_JTL_Domain = Class(name="JTL::JTL::Domain")
JTL_JTL_Relation = Class(name="JTL::JTL::Relation")
Transformation = Class(name="Transformation")
Pattern = Class(name="Pattern")
JTL_JTL_Model = Class(name="JTL::JTL::Model")
Predicate = Class(name="Predicate")
JTL_JTL_Where = Class(name="JTL::JTL::Where")
TemplateExp = Class(name="TemplateExp")
JTL_JTL_Predicate = Class(name="JTL::JTL::Predicate")
OclExpression = Class(name="OclExpression")
JTL_JTL_When = Class(name="JTL::JTL::When")
JTL_JTL_Pattern = Class(name="JTL::JTL::Pattern")
JTL_essentialocl_OclExpression = Class(name="JTL::essentialocl::OclExpression", is_abstract=True)
TypedElement = Class(name="TypedElement")
TryExp = Class(name="TryExp")
JTL_essentialocl_BooleanLiteralExp = Class(name="JTL::essentialocl::BooleanLiteralExp")
PrimitiveLiteralExp = Class(name="PrimitiveLiteralExp")
JTL_essentialocl_CallExp = Class(name="JTL::essentialocl::CallExp", is_abstract=True)
JTL_essentialocl_LetExp = Class(name="JTL::essentialocl::LetExp")
JTL_essentialocl_UnlimitedNaturalExp = Class(name="JTL::essentialocl::UnlimitedNaturalExp")
NumericLiteralExp = Class(name="NumericLiteralExp")
JTL_essentialocl_IfExp = Class(name="JTL::essentialocl::IfExp")
ComputeExp = Class(name="ComputeExp")
JTL_essentialocl_PropertyCallExp = Class(name="JTL::essentialocl::PropertyCallExp")
FeaturePropertyCall = Class(name="FeaturePropertyCall")
JTL_essentialocl_Variable = Class(name="JTL::essentialocl::Variable")
LetExp = Class(name="LetExp")
JTL_essentialocl_LoopExp = Class(name="JTL::essentialocl::LoopExp", is_abstract=True)
essentialocl_CallExp = Class(name="essentialocl::CallExp")
essentialocl_OclExpression = Class(name="essentialocl::OclExpression")
JTL_essentialocl_IteratorExp = Class(name="JTL::essentialocl::IteratorExp")
LoopExp = Class(name="LoopExp")
JTL_essentialocl_VariableExp = Class(name="JTL::essentialocl::VariableExp")
JTL_essentialocl_TypeExp = Class(name="JTL::essentialocl::TypeExp")
JTL_essentialocl_RealLiteralExp = Class(name="JTL::essentialocl::RealLiteralExp")
JTL_essentialocl_LiteralExp = Class(name="JTL::essentialocl::LiteralExp", is_abstract=True)
JTL_essentialocl_StringLiteralExp = Class(name="JTL::essentialocl::StringLiteralExp")
JTL_essentialocl_IntegerLiteralExp = Class(name="JTL::essentialocl::IntegerLiteralExp")
JTL_essentialocl_OperationCallExp = Class(name="JTL::essentialocl::OperationCallExp")
CollectionLiteralPart = Class(name="CollectionLiteralPart")
JTL_essentialocl_CollectionLiteralPart = Class(name="JTL::essentialocl::CollectionLiteralPart", is_abstract=True)
CollectionLiteralExp = Class(name="CollectionLiteralExp")
JTL_essentialocl_CollectionItem = Class(name="JTL::essentialocl::CollectionItem")
JTL_essentialocl_IterateExp = Class(name="JTL::essentialocl::IterateExp")
JTL_essentialocl_PrimitiveLiteralExp = Class(name="JTL::essentialocl::PrimitiveLiteralExp", is_abstract=True)
LiteralExp = Class(name="LiteralExp")
JTL_essentialocl_NumericLiteralExp = Class(name="JTL::essentialocl::NumericLiteralExp", is_abstract=True)
JTL_essentialocl_CollectionLiteralExp = Class(name="JTL::essentialocl::CollectionLiteralExp")
JTL_essentialocl_TupleLiteralExp = Class(name="JTL::essentialocl::TupleLiteralExp")
TupleLiteralPart = Class(name="TupleLiteralPart")
JTL_essentialocl_NullLiteralExp = Class(name="JTL::essentialocl::NullLiteralExp")
JTL_essentialocl_CollectionRange = Class(name="JTL::essentialocl::CollectionRange")
JTL_essentialocl_OpaqueExpression = Class(name="JTL::essentialocl::OpaqueExpression")
JTL_essentialocl_InvalidLiteralExp = Class(name="JTL::essentialocl::InvalidLiteralExp")
JTL_essentialocl_FeaturePropertyCall = Class(name="JTL::essentialocl::FeaturePropertyCall", is_abstract=True)
CallExp = Class(name="CallExp")
JTL_essentialocl_TupleLiteralPart = Class(name="JTL::essentialocl::TupleLiteralPart")
JTL_essentialocl_ExpressionInOcl = Class(name="JTL::essentialocl::ExpressionInOcl")
OpaqueExpression = Class(name="OpaqueExpression")
JTL_essentialocl_EnumLiteralExp = Class(name="JTL::essentialocl::EnumLiteralExp")
JTL_essentialocl_InvalidType = Class(name="JTL::essentialocl::InvalidType")
JTL_essentialocl_OrderedSetType = Class(name="JTL::essentialocl::OrderedSetType")
JTL_essentialocl_SequenceType = Class(name="JTL::essentialocl::SequenceType")
JTL_essentialocl_SetType = Class(name="JTL::essentialocl::SetType")
TupleLiteralExp = Class(name="TupleLiteralExp")
JTL_essentialocl_BagType = Class(name="JTL::essentialocl::BagType")
CollectionType = Class(name="CollectionType")
JTL_essentialocl_CollectionType = Class(name="JTL::essentialocl::CollectionType", is_abstract=True)
JTL_template_TemplateExp = Class(name="JTL::template::TemplateExp", is_abstract=True)
JTL_essentialocl_TupleType = Class(name="JTL::essentialocl::TupleType")
emof_DataType = Class(name="emof::DataType")
JTL_essentialocl_VoidType = Class(name="JTL::essentialocl::VoidType")
JTL_essentialocl_AnyType = Class(name="JTL::essentialocl::AnyType")
emof_Type = Class(name="emof::Type")
JTL_template_CollectionTemplateExp = Class(name="JTL::template::CollectionTemplateExp")
JTL_template_ObjectTemplateExp = Class(name="JTL::template::ObjectTemplateExp")
PropertyTemplateItem = Class(name="PropertyTemplateItem")
AssignExp = Class(name="AssignExp")
JTL_imperativeocl_ImperativeIterateExp = Class(name="JTL::imperativeocl::ImperativeIterateExp")
ImperativeLoopExp = Class(name="ImperativeLoopExp")
JTL_template_PropertyTemplateItem = Class(name="JTL::template::PropertyTemplateItem")
ObjectTemplateExp = Class(name="ObjectTemplateExp")
JTL_imperativeocl_BlockExp = Class(name="JTL::imperativeocl::BlockExp")
JTL_imperativeocl_AssignExp = Class(name="JTL::imperativeocl::AssignExp")
ImperativeExpression = Class(name="ImperativeExpression")
JTL_imperativeocl_VariableInitExp = Class(name="JTL::imperativeocl::VariableInitExp")
JTL_imperativeocl_SwitchExp = Class(name="JTL::imperativeocl::SwitchExp")
imperativeocl_ImperativeExpression = Class(name="imperativeocl::ImperativeExpression")
AltExp = Class(name="AltExp")
JTL_imperativeocl_ComputeExp = Class(name="JTL::imperativeocl::ComputeExp")
JTL_imperativeocl_WhileExp = Class(name="JTL::imperativeocl::WhileExp")
JTL_imperativeocl_UnlinkExp = Class(name="JTL::imperativeocl::UnlinkExp")
JTL_imperativeocl_AltExp = Class(name="JTL::imperativeocl::AltExp")
JTL_imperativeocl_ReturnExp = Class(name="JTL::imperativeocl::ReturnExp")
JTL_imperativeocl_BreakExp = Class(name="JTL::imperativeocl::BreakExp")
JTL_imperativeocl_TryExp = Class(name="JTL::imperativeocl::TryExp")
JTL_imperativeocl_Typedef = Class(name="JTL::imperativeocl::Typedef")
JTL_imperativeocl_RaiseExp = Class(name="JTL::imperativeocl::RaiseExp")
JTL_imperativeocl_ContinueExp = Class(name="JTL::imperativeocl::ContinueExp")
JTL_imperativeocl_ForExp = Class(name="JTL::imperativeocl::ForExp")
JTL_imperativeocl_TupleExp = Class(name="JTL::imperativeocl::TupleExp")
JTL_imperativeocl_DictionaryType = Class(name="JTL::imperativeocl::DictionaryType")
JTL_imperativeocl_InstantiationExp = Class(name="JTL::imperativeocl::InstantiationExp")
JTL_imperativeocl_TemplateParameterType = Class(name="JTL::imperativeocl::TemplateParameterType")
JTL_imperativeocl_LogExp = Class(name="JTL::imperativeocl::LogExp")
JTL_imperativeocl_DictLiteralExp = Class(name="JTL::imperativeocl::DictLiteralExp")
DictLiteralPart = Class(name="DictLiteralPart")
JTL_imperativeocl_DictLiteralPart = Class(name="JTL::imperativeocl::DictLiteralPart")
JTL_imperativeocl_AssertExp = Class(name="JTL::imperativeocl::AssertExp")
LogExp = Class(name="LogExp")
JTL_imperativeocl_CollectorExp = Class(name="JTL::imperativeocl::CollectorExp")
JTL_imperativeocl_ImperativeExpression = Class(name="JTL::imperativeocl::ImperativeExpression", is_abstract=True)
JTL_imperativeocl_ImperativeLoopExp = Class(name="JTL::imperativeocl::ImperativeLoopExp", is_abstract=True)
essentialocl_LoopExp = Class(name="essentialocl::LoopExp")
JTL_imperativeocl_AnonymousTupleLiteralExp = Class(name="JTL::imperativeocl::AnonymousTupleLiteralExp")
AnonymousTupleLiteralPart = Class(name="AnonymousTupleLiteralPart")
JTL_imperativeocl_AnonymousTupleLiteralPart = Class(name="JTL::imperativeocl::AnonymousTupleLiteralPart")
JTL_imperativeocl_UnpackExp = Class(name="JTL::imperativeocl::UnpackExp")
JTL_imperativeocl_AnonymousTupleType = Class(name="JTL::imperativeocl::AnonymousTupleType")
JTL_imperativeocl_ListType = Class(name="JTL::imperativeocl::ListType")

# JTL_emof_Class class attributes and methods
JTL_emof_Class_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
JTL_emof_Class.attributes={JTL_emof_Class_isAbstract}

# Type class attributes and methods

# Property class attributes and methods

# Class class attributes and methods

# JTL_emof_DataType class attributes and methods

# JTL_emof_Element class attributes and methods

# Object class attributes and methods

# Tag class attributes and methods

# Comment class attributes and methods

# JTL_emof_Tag class attributes and methods
JTL_emof_Tag_value: Property = Property(name="value", type=StringType)
JTL_emof_Tag_name: Property = Property(name="name", type=StringType)
JTL_emof_Tag.attributes={JTL_emof_Tag_value, JTL_emof_Tag_name}

# Element class attributes and methods

# Operation class attributes and methods

# JTL_emof_Enumeration class attributes and methods

# DataType class attributes and methods

# EnumerationLiteral class attributes and methods

# JTL_emof_NamedElement class attributes and methods
JTL_emof_NamedElement_name: Property = Property(name="name", type=StringType)
JTL_emof_NamedElement.attributes={JTL_emof_NamedElement_name}

# JTL_emof_Extent class attributes and methods

# JTL_emof_Object class attributes and methods

# JTL_emof_Operation class attributes and methods

# emof_MultiplicityElement class attributes and methods

# emof_TypedElement class attributes and methods

# Parameter class attributes and methods

# JTL_emof_MultiplicityElement class attributes and methods
JTL_emof_MultiplicityElement_isOrdered: Property = Property(name="isOrdered", type=StringType)
JTL_emof_MultiplicityElement_isUnique: Property = Property(name="isUnique", type=StringType)
JTL_emof_MultiplicityElement_lower: Property = Property(name="lower", type=IntegerType)
JTL_emof_MultiplicityElement_upper: Property = Property(name="upper", type=StringType)
JTL_emof_MultiplicityElement.attributes={JTL_emof_MultiplicityElement_isUnique, JTL_emof_MultiplicityElement_lower, JTL_emof_MultiplicityElement_isOrdered, JTL_emof_MultiplicityElement_upper}

# JTL_emof_Package class attributes and methods
JTL_emof_Package_uri: Property = Property(name="uri", type=StringType)
JTL_emof_Package.attributes={JTL_emof_Package_uri}

# NamedElement class attributes and methods

# JTL_emof_Type class attributes and methods

# JTL_emof_Parameter class attributes and methods

# JTL_emof_EnumerationLiteral class attributes and methods

# Enumeration class attributes and methods

# Package class attributes and methods

# JTL_emof_TypedElement class attributes and methods
JTL_emof_TypedElement_type: Property = Property(name="type", type=StringType)
JTL_emof_TypedElement.attributes={JTL_emof_TypedElement_type}

# JTL_emof_PrimitiveType class attributes and methods

# JTL_emof_URIExtent class attributes and methods

# JTL_emof_Property class attributes and methods
JTL_emof_Property_isReadOnly: Property = Property(name="isReadOnly", type=BooleanType)
JTL_emof_Property_isDerived: Property = Property(name="isDerived", type=BooleanType)
JTL_emof_Property_isComposite: Property = Property(name="isComposite", type=BooleanType)
JTL_emof_Property_isId: Property = Property(name="isId", type=BooleanType)
JTL_emof_Property_default: Property = Property(name="default", type=StringType)
JTL_emof_Property.attributes={JTL_emof_Property_isComposite, JTL_emof_Property_isId, JTL_emof_Property_isDerived, JTL_emof_Property_default, JTL_emof_Property_isReadOnly}

# JTL_emof_Comment class attributes and methods

# JTL_JTL_Transformation class attributes and methods

# emof_Class class attributes and methods

# emof_Package class attributes and methods

# Model class attributes and methods

# Relation class attributes and methods

# Extent class attributes and methods

# Domain class attributes and methods

# Where class attributes and methods

# When class attributes and methods

# Variable class attributes and methods

# JTL_JTL_Domain class attributes and methods
JTL_JTL_Domain_isCheckable: Property = Property(name="isCheckable", type=BooleanType)
JTL_JTL_Domain_isEnforceable: Property = Property(name="isEnforceable", type=BooleanType)
JTL_JTL_Domain.attributes={JTL_JTL_Domain_isEnforceable, JTL_JTL_Domain_isCheckable}

# JTL_JTL_Relation class attributes and methods
JTL_JTL_Relation_isTopLevel: Property = Property(name="isTopLevel", type=BooleanType)
JTL_JTL_Relation.attributes={JTL_JTL_Relation_isTopLevel}

# Transformation class attributes and methods

# Pattern class attributes and methods

# JTL_JTL_Model class attributes and methods
JTL_JTL_Model_usedPackage: Property = Property(name="usedPackage", type=StringType)
JTL_JTL_Model.attributes={JTL_JTL_Model_usedPackage}

# Predicate class attributes and methods

# JTL_JTL_Where class attributes and methods

# TemplateExp class attributes and methods

# JTL_JTL_Predicate class attributes and methods

# OclExpression class attributes and methods

# JTL_JTL_When class attributes and methods

# JTL_JTL_Pattern class attributes and methods

# JTL_essentialocl_OclExpression class attributes and methods

# TypedElement class attributes and methods

# TryExp class attributes and methods

# JTL_essentialocl_BooleanLiteralExp class attributes and methods
JTL_essentialocl_BooleanLiteralExp_booleanSymbol: Property = Property(name="booleanSymbol", type=BooleanType)
JTL_essentialocl_BooleanLiteralExp.attributes={JTL_essentialocl_BooleanLiteralExp_booleanSymbol}

# PrimitiveLiteralExp class attributes and methods

# JTL_essentialocl_CallExp class attributes and methods

# JTL_essentialocl_LetExp class attributes and methods

# JTL_essentialocl_UnlimitedNaturalExp class attributes and methods
JTL_essentialocl_UnlimitedNaturalExp_symbol: Property = Property(name="symbol", type=StringType)
JTL_essentialocl_UnlimitedNaturalExp.attributes={JTL_essentialocl_UnlimitedNaturalExp_symbol}

# NumericLiteralExp class attributes and methods

# JTL_essentialocl_IfExp class attributes and methods

# ComputeExp class attributes and methods

# JTL_essentialocl_PropertyCallExp class attributes and methods

# FeaturePropertyCall class attributes and methods

# JTL_essentialocl_Variable class attributes and methods

# LetExp class attributes and methods

# JTL_essentialocl_LoopExp class attributes and methods

# essentialocl_CallExp class attributes and methods

# essentialocl_OclExpression class attributes and methods

# JTL_essentialocl_IteratorExp class attributes and methods

# LoopExp class attributes and methods

# JTL_essentialocl_VariableExp class attributes and methods

# JTL_essentialocl_TypeExp class attributes and methods

# JTL_essentialocl_RealLiteralExp class attributes and methods
JTL_essentialocl_RealLiteralExp_realSymbol: Property = Property(name="realSymbol", type=FloatType)
JTL_essentialocl_RealLiteralExp.attributes={JTL_essentialocl_RealLiteralExp_realSymbol}

# JTL_essentialocl_LiteralExp class attributes and methods

# JTL_essentialocl_StringLiteralExp class attributes and methods
JTL_essentialocl_StringLiteralExp_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
JTL_essentialocl_StringLiteralExp.attributes={JTL_essentialocl_StringLiteralExp_stringSymbol}

# JTL_essentialocl_IntegerLiteralExp class attributes and methods
JTL_essentialocl_IntegerLiteralExp_integerSymbol: Property = Property(name="integerSymbol", type=IntegerType)
JTL_essentialocl_IntegerLiteralExp.attributes={JTL_essentialocl_IntegerLiteralExp_integerSymbol}

# JTL_essentialocl_OperationCallExp class attributes and methods

# CollectionLiteralPart class attributes and methods

# JTL_essentialocl_CollectionLiteralPart class attributes and methods

# CollectionLiteralExp class attributes and methods

# JTL_essentialocl_CollectionItem class attributes and methods

# JTL_essentialocl_IterateExp class attributes and methods

# JTL_essentialocl_PrimitiveLiteralExp class attributes and methods

# LiteralExp class attributes and methods

# JTL_essentialocl_NumericLiteralExp class attributes and methods

# JTL_essentialocl_CollectionLiteralExp class attributes and methods
JTL_essentialocl_CollectionLiteralExp_kind: Property = Property(name="kind", type=StringType)
JTL_essentialocl_CollectionLiteralExp.attributes={JTL_essentialocl_CollectionLiteralExp_kind}

# JTL_essentialocl_TupleLiteralExp class attributes and methods

# TupleLiteralPart class attributes and methods

# JTL_essentialocl_NullLiteralExp class attributes and methods

# JTL_essentialocl_CollectionRange class attributes and methods

# JTL_essentialocl_OpaqueExpression class attributes and methods

# JTL_essentialocl_InvalidLiteralExp class attributes and methods

# JTL_essentialocl_FeaturePropertyCall class attributes and methods

# CallExp class attributes and methods

# JTL_essentialocl_TupleLiteralPart class attributes and methods

# JTL_essentialocl_ExpressionInOcl class attributes and methods

# OpaqueExpression class attributes and methods

# JTL_essentialocl_EnumLiteralExp class attributes and methods

# JTL_essentialocl_InvalidType class attributes and methods

# JTL_essentialocl_OrderedSetType class attributes and methods

# JTL_essentialocl_SequenceType class attributes and methods

# JTL_essentialocl_SetType class attributes and methods

# TupleLiteralExp class attributes and methods

# JTL_essentialocl_BagType class attributes and methods

# CollectionType class attributes and methods

# JTL_essentialocl_CollectionType class attributes and methods

# JTL_template_TemplateExp class attributes and methods

# JTL_essentialocl_TupleType class attributes and methods

# emof_DataType class attributes and methods

# JTL_essentialocl_VoidType class attributes and methods

# JTL_essentialocl_AnyType class attributes and methods

# emof_Type class attributes and methods

# JTL_template_CollectionTemplateExp class attributes and methods
JTL_template_CollectionTemplateExp_kind: Property = Property(name="kind", type=StringType)
JTL_template_CollectionTemplateExp.attributes={JTL_template_CollectionTemplateExp_kind}

# JTL_template_ObjectTemplateExp class attributes and methods
JTL_template_ObjectTemplateExp_referredClass: Property = Property(name="referredClass", type=StringType)
JTL_template_ObjectTemplateExp.attributes={JTL_template_ObjectTemplateExp_referredClass}

# PropertyTemplateItem class attributes and methods

# AssignExp class attributes and methods

# JTL_imperativeocl_ImperativeIterateExp class attributes and methods

# ImperativeLoopExp class attributes and methods

# JTL_template_PropertyTemplateItem class attributes and methods

# ObjectTemplateExp class attributes and methods

# JTL_imperativeocl_BlockExp class attributes and methods

# JTL_imperativeocl_AssignExp class attributes and methods
JTL_imperativeocl_AssignExp_isReset: Property = Property(name="isReset", type=BooleanType)
JTL_imperativeocl_AssignExp.attributes={JTL_imperativeocl_AssignExp_isReset}

# ImperativeExpression class attributes and methods

# JTL_imperativeocl_VariableInitExp class attributes and methods
JTL_imperativeocl_VariableInitExp_withResult: Property = Property(name="withResult", type=BooleanType)
JTL_imperativeocl_VariableInitExp.attributes={JTL_imperativeocl_VariableInitExp_withResult}

# JTL_imperativeocl_SwitchExp class attributes and methods

# imperativeocl_ImperativeExpression class attributes and methods

# AltExp class attributes and methods

# JTL_imperativeocl_ComputeExp class attributes and methods

# JTL_imperativeocl_WhileExp class attributes and methods

# JTL_imperativeocl_UnlinkExp class attributes and methods

# JTL_imperativeocl_AltExp class attributes and methods

# JTL_imperativeocl_ReturnExp class attributes and methods

# JTL_imperativeocl_BreakExp class attributes and methods

# JTL_imperativeocl_TryExp class attributes and methods

# JTL_imperativeocl_Typedef class attributes and methods

# JTL_imperativeocl_RaiseExp class attributes and methods

# JTL_imperativeocl_ContinueExp class attributes and methods

# JTL_imperativeocl_ForExp class attributes and methods

# JTL_imperativeocl_TupleExp class attributes and methods

# JTL_imperativeocl_DictionaryType class attributes and methods

# JTL_imperativeocl_InstantiationExp class attributes and methods

# JTL_imperativeocl_TemplateParameterType class attributes and methods
JTL_imperativeocl_TemplateParameterType_specification: Property = Property(name="specification", type=StringType)
JTL_imperativeocl_TemplateParameterType.attributes={JTL_imperativeocl_TemplateParameterType_specification}

# JTL_imperativeocl_LogExp class attributes and methods
JTL_imperativeocl_LogExp_text: Property = Property(name="text", type=StringType)
JTL_imperativeocl_LogExp_level: Property = Property(name="level", type=IntegerType)
JTL_imperativeocl_LogExp.attributes={JTL_imperativeocl_LogExp_level, JTL_imperativeocl_LogExp_text}

# JTL_imperativeocl_DictLiteralExp class attributes and methods

# DictLiteralPart class attributes and methods

# JTL_imperativeocl_DictLiteralPart class attributes and methods

# JTL_imperativeocl_AssertExp class attributes and methods
JTL_imperativeocl_AssertExp_severity: Property = Property(name="severity", type=StringType)
JTL_imperativeocl_AssertExp.attributes={JTL_imperativeocl_AssertExp_severity}

# LogExp class attributes and methods

# JTL_imperativeocl_CollectorExp class attributes and methods

# JTL_imperativeocl_ImperativeExpression class attributes and methods

# JTL_imperativeocl_ImperativeLoopExp class attributes and methods

# essentialocl_LoopExp class attributes and methods

# JTL_imperativeocl_AnonymousTupleLiteralExp class attributes and methods

# AnonymousTupleLiteralPart class attributes and methods

# JTL_imperativeocl_AnonymousTupleLiteralPart class attributes and methods

# JTL_imperativeocl_UnpackExp class attributes and methods

# JTL_imperativeocl_AnonymousTupleType class attributes and methods

# JTL_imperativeocl_ListType class attributes and methods

# Relationships
ownedAttribute0: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute0",
    ends={
        Property(name="emof", type=JTL_emof_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Property", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass3: BinaryAssociation = BinaryAssociation(
    name="superClass3",
    ends={
        Property(name="Class", type=JTL_emof_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_emof_Class", type=Class_, multiplicity=Multiplicity(0, 9999))
    }
)
tag4: BinaryAssociation = BinaryAssociation(
    name="tag4",
    ends={
        Property(name="emof5", type=JTL_emof_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="Tag", type=Tag, multiplicity=Multiplicity(0, 9999))
    }
)
ownedComment6: BinaryAssociation = BinaryAssociation(
    name="ownedComment6",
    ends={
        Property(name="Comment", type=JTL_emof_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_emof_Element", type=Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation1: BinaryAssociation = BinaryAssociation(
    name="ownedOperation1",
    ends={
        Property(name="emof2", type=JTL_emof_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Operation", type=Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedLiteral9: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral9",
    ends={
        Property(name="emof10", type=JTL_emof_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="EnumerationLiteral", type=EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element7: BinaryAssociation = BinaryAssociation(
    name="element7",
    ends={
        Property(name="emof8", type=JTL_emof_Tag, multiplicity=Multiplicity(1, 1)),
        Property(name="Element", type=Element, multiplicity=Multiplicity(0, 9999))
    }
)
ownedParameter14: BinaryAssociation = BinaryAssociation(
    name="ownedParameter14",
    ends={
        Property(name="emof15", type=JTL_emof_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="Parameter", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
raisedException16: BinaryAssociation = BinaryAssociation(
    name="raisedException16",
    ends={
        Property(name="Type", type=JTL_emof_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_emof_Operation", type=Type, multiplicity=Multiplicity(0, 9999))
    }
)
ownedType17: BinaryAssociation = BinaryAssociation(
    name="ownedType17",
    ends={
        Property(name="emof19", type=JTL_emof_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="Type18", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
class11: BinaryAssociation = BinaryAssociation(
    name="class11",
    ends={
        Property(name="emof13", type=JTL_emof_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="Class12", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
package21: BinaryAssociation = BinaryAssociation(
    name="package21",
    ends={
        Property(name="emof23", type=JTL_emof_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="Package22", type=Package, multiplicity=Multiplicity(1, 1))
    }
)
operation24: BinaryAssociation = BinaryAssociation(
    name="operation24",
    ends={
        Property(name="emof26", type=JTL_emof_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="Operation25", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
enumeration27: BinaryAssociation = BinaryAssociation(
    name="enumeration27",
    ends={
        Property(name="emof28", type=JTL_emof_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="Enumeration", type=Enumeration_, multiplicity=Multiplicity(0, 1))
    }
)
nestedPackage20: BinaryAssociation = BinaryAssociation(
    name="nestedPackage20",
    ends={
        Property(name="Package", type=JTL_emof_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_emof_Package", type=Package, multiplicity=Multiplicity(0, 9999))
    }
)
Class29: BinaryAssociation = BinaryAssociation(
    name="Class29",
    ends={
        Property(name="emof31", type=JTL_emof_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="Class30", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
opposite32: BinaryAssociation = BinaryAssociation(
    name="opposite32",
    ends={
        Property(name="Property33", type=JTL_emof_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_emof_Property", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
annotatedElement34: BinaryAssociation = BinaryAssociation(
    name="annotatedElement34",
    ends={
        Property(name="NamedElement", type=JTL_emof_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_emof_Comment", type=NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
modelParameter35: BinaryAssociation = BinaryAssociation(
    name="modelParameter35",
    ends={
        Property(name="JTL", type=JTL_JTL_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="Model", type=Model, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relation36: BinaryAssociation = BinaryAssociation(
    name="relation36",
    ends={
        Property(name="JTL37", type=JTL_JTL_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="Relation", type=Relation, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
domain40: BinaryAssociation = BinaryAssociation(
    name="domain40",
    ends={
        Property(name="JTL41", type=JTL_JTL_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="Domain", type=Domain, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
where42: BinaryAssociation = BinaryAssociation(
    name="where42",
    ends={
        Property(name="JTL43", type=JTL_JTL_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="Where", type=Where, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
when44: BinaryAssociation = BinaryAssociation(
    name="when44",
    ends={
        Property(name="JTL45", type=JTL_JTL_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="When", type=When, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable46: BinaryAssociation = BinaryAssociation(
    name="variable46",
    ends={
        Property(name="Variable", type=JTL_JTL_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_JTL_Relation", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transformation38: BinaryAssociation = BinaryAssociation(
    name="transformation38",
    ends={
        Property(name="JTL39", type=JTL_JTL_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="Transformation", type=Transformation, multiplicity=Multiplicity(1, 1))
    }
)
relation47: BinaryAssociation = BinaryAssociation(
    name="relation47",
    ends={
        Property(name="JTL49", type=JTL_JTL_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="Relation48", type=Relation, multiplicity=Multiplicity(1, 1))
    }
)
pattern50: BinaryAssociation = BinaryAssociation(
    name="pattern50",
    ends={
        Property(name="Pattern", type=JTL_JTL_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_JTL_Domain", type=Pattern, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
model51: BinaryAssociation = BinaryAssociation(
    name="model51",
    ends={
        Property(name="Model53", type=JTL_JTL_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_JTL_Domain52", type=Model, multiplicity=Multiplicity(1, 1))
    }
)
rootVariable54: BinaryAssociation = BinaryAssociation(
    name="rootVariable54",
    ends={
        Property(name="Variable56", type=JTL_JTL_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_JTL_Domain55", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
transformation57: BinaryAssociation = BinaryAssociation(
    name="transformation57",
    ends={
        Property(name="JTL59", type=JTL_JTL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="Transformation58", type=Transformation, multiplicity=Multiplicity(1, 1))
    }
)
dependsOn60: BinaryAssociation = BinaryAssociation(
    name="dependsOn60",
    ends={
        Property(name="Model61", type=JTL_JTL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_JTL_Model", type=Model, multiplicity=Multiplicity(0, 9999))
    }
)
whenOwner75: BinaryAssociation = BinaryAssociation(
    name="whenOwner75",
    ends={
        Property(name="JTL77", type=JTL_JTL_When, multiplicity=Multiplicity(1, 1)),
        Property(name="Relation76", type=Relation, multiplicity=Multiplicity(0, 1))
    }
)
predicate62: BinaryAssociation = BinaryAssociation(
    name="predicate62",
    ends={
        Property(name="JTL63", type=JTL_JTL_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="Predicate", type=Predicate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bindsTo64: BinaryAssociation = BinaryAssociation(
    name="bindsTo64",
    ends={
        Property(name="Variable65", type=JTL_JTL_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_JTL_Pattern", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
templateExpression66: BinaryAssociation = BinaryAssociation(
    name="templateExpression66",
    ends={
        Property(name="TemplateExp", type=JTL_JTL_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_JTL_Pattern67", type=TemplateExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
domain68: BinaryAssociation = BinaryAssociation(
    name="domain68",
    ends={
        Property(name="Domain70", type=JTL_JTL_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_JTL_Pattern69", type=Domain, multiplicity=Multiplicity(1, 1))
    }
)
pattern71: BinaryAssociation = BinaryAssociation(
    name="pattern71",
    ends={
        Property(name="JTL73", type=JTL_JTL_Predicate, multiplicity=Multiplicity(1, 1)),
        Property(name="Pattern72", type=Pattern, multiplicity=Multiplicity(1, 1))
    }
)
conditionExpression74: BinaryAssociation = BinaryAssociation(
    name="conditionExpression74",
    ends={
        Property(name="OclExpression", type=JTL_JTL_Predicate, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_JTL_Predicate", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
whereOwner78: BinaryAssociation = BinaryAssociation(
    name="whereOwner78",
    ends={
        Property(name="JTL80", type=JTL_JTL_Where, multiplicity=Multiplicity(1, 1)),
        Property(name="Relation79", type=Relation, multiplicity=Multiplicity(0, 1))
    }
)
tryBodyOwner83: BinaryAssociation = BinaryAssociation(
    name="tryBodyOwner83",
    ends={
        Property(name="imperativeocl", type=JTL_essentialocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="TryExp", type=TryExp, multiplicity=Multiplicity(0, 1))
    }
)
source81: BinaryAssociation = BinaryAssociation(
    name="source81",
    ends={
        Property(name="OclExpression82", type=JTL_essentialocl_CallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_CallExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseExpression89: BinaryAssociation = BinaryAssociation(
    name="elseExpression89",
    ends={
        Property(name="OclExpression91", type=JTL_essentialocl_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_IfExp90", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
in92: BinaryAssociation = BinaryAssociation(
    name="in92",
    ends={
        Property(name="OclExpression93", type=JTL_essentialocl_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_LetExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition84: BinaryAssociation = BinaryAssociation(
    name="condition84",
    ends={
        Property(name="OclExpression85", type=JTL_essentialocl_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_IfExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression86: BinaryAssociation = BinaryAssociation(
    name="thenExpression86",
    ends={
        Property(name="OclExpression88", type=JTL_essentialocl_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_IfExp87", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bindParameter100: BinaryAssociation = BinaryAssociation(
    name="bindParameter100",
    ends={
        Property(name="Parameter102", type=JTL_essentialocl_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_Variable101", type=Parameter_, multiplicity=Multiplicity(0, 1))
    }
)
computeOwner103: BinaryAssociation = BinaryAssociation(
    name="computeOwner103",
    ends={
        Property(name="imperativeocl104", type=JTL_essentialocl_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="ComputeExp", type=ComputeExp, multiplicity=Multiplicity(0, 1))
    }
)
referredProperty105: BinaryAssociation = BinaryAssociation(
    name="referredProperty105",
    ends={
        Property(name="Property106", type=JTL_essentialocl_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_PropertyCallExp", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
variable94: BinaryAssociation = BinaryAssociation(
    name="variable94",
    ends={
        Property(name="essentialocl", type=JTL_essentialocl_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Variable95", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initExpression96: BinaryAssociation = BinaryAssociation(
    name="initExpression96",
    ends={
        Property(name="OclExpression97", type=JTL_essentialocl_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_Variable", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
LetExp98: BinaryAssociation = BinaryAssociation(
    name="LetExp98",
    ends={
        Property(name="essentialocl99", type=JTL_essentialocl_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="LetExp", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
body111: BinaryAssociation = BinaryAssociation(
    name="body111",
    ends={
        Property(name="OclExpression112", type=JTL_essentialocl_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_LoopExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterator113: BinaryAssociation = BinaryAssociation(
    name="iterator113",
    ends={
        Property(name="Variable115", type=JTL_essentialocl_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_LoopExp114", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredVariable107: BinaryAssociation = BinaryAssociation(
    name="referredVariable107",
    ends={
        Property(name="Variable108", type=JTL_essentialocl_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_VariableExp", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
referredType109: BinaryAssociation = BinaryAssociation(
    name="referredType109",
    ends={
        Property(name="Type110", type=JTL_essentialocl_TypeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_TypeExp", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
argument116: BinaryAssociation = BinaryAssociation(
    name="argument116",
    ends={
        Property(name="JTL_essentialocl_OperationCallExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="OclExpression117", type=JTL_essentialocl_OperationCallExp, multiplicity=Multiplicity(1, 1))
    }
)
referredOperation118: BinaryAssociation = BinaryAssociation(
    name="referredOperation118",
    ends={
        Property(name="Relation120", type=JTL_essentialocl_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_OperationCallExp119", type=Relation, multiplicity=Multiplicity(0, 1))
    }
)
part123: BinaryAssociation = BinaryAssociation(
    name="part123",
    ends={
        Property(name="essentialocl124", type=JTL_essentialocl_CollectionLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="CollectionLiteralPart", type=CollectionLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
CollectionLiteralExp125: BinaryAssociation = BinaryAssociation(
    name="CollectionLiteralExp125",
    ends={
        Property(name="essentialocl126", type=JTL_essentialocl_CollectionLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="CollectionLiteralExp", type=CollectionLiteralExp, multiplicity=Multiplicity(1, 1))
    }
)
result121: BinaryAssociation = BinaryAssociation(
    name="result121",
    ends={
        Property(name="Variable122", type=JTL_essentialocl_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_IterateExp", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
last131: BinaryAssociation = BinaryAssociation(
    name="last131",
    ends={
        Property(name="OclExpression133", type=JTL_essentialocl_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_CollectionRange132", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
part134: BinaryAssociation = BinaryAssociation(
    name="part134",
    ends={
        Property(name="essentialocl135", type=JTL_essentialocl_TupleLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="TupleLiteralPart", type=TupleLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
item127: BinaryAssociation = BinaryAssociation(
    name="item127",
    ends={
        Property(name="OclExpression128", type=JTL_essentialocl_CollectionItem, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_CollectionItem", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
first129: BinaryAssociation = BinaryAssociation(
    name="first129",
    ends={
        Property(name="OclExpression130", type=JTL_essentialocl_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_CollectionRange", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameterVariable144: BinaryAssociation = BinaryAssociation(
    name="parameterVariable144",
    ends={
        Property(name="Variable146", type=JTL_essentialocl_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_ExpressionInOcl145", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bodyExpression136: BinaryAssociation = BinaryAssociation(
    name="bodyExpression136",
    ends={
        Property(name="OclExpression137", type=JTL_essentialocl_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_ExpressionInOcl", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context138: BinaryAssociation = BinaryAssociation(
    name="context138",
    ends={
        Property(name="Variable140", type=JTL_essentialocl_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_ExpressionInOcl139", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resultVariable141: BinaryAssociation = BinaryAssociation(
    name="resultVariable141",
    ends={
        Property(name="Variable143", type=JTL_essentialocl_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_ExpressionInOcl142", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referredEnumLiteral151: BinaryAssociation = BinaryAssociation(
    name="referredEnumLiteral151",
    ends={
        Property(name="EnumerationLiteral152", type=JTL_essentialocl_EnumLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_EnumLiteralExp", type=EnumerationLiteral, multiplicity=Multiplicity(0, 1))
    }
)
TupleLiteralExp147: BinaryAssociation = BinaryAssociation(
    name="TupleLiteralExp147",
    ends={
        Property(name="essentialocl148", type=JTL_essentialocl_TupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="TupleLiteralExp", type=TupleLiteralExp, multiplicity=Multiplicity(0, 1))
    }
)
elementType149: BinaryAssociation = BinaryAssociation(
    name="elementType149",
    ends={
        Property(name="Type150", type=JTL_essentialocl_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_CollectionType", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
bindsTo153: BinaryAssociation = BinaryAssociation(
    name="bindsTo153",
    ends={
        Property(name="Variable154", type=JTL_template_TemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_template_TemplateExp", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
where155: BinaryAssociation = BinaryAssociation(
    name="where155",
    ends={
        Property(name="OclExpression157", type=JTL_template_TemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_template_TemplateExp156", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
part160: BinaryAssociation = BinaryAssociation(
    name="part160",
    ends={
        Property(name="OclExpression161", type=JTL_template_CollectionTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_template_CollectionTemplateExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredCollectionType162: BinaryAssociation = BinaryAssociation(
    name="referredCollectionType162",
    ends={
        Property(name="CollectionType", type=JTL_template_CollectionTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_template_CollectionTemplateExp163", type=CollectionType, multiplicity=Multiplicity(0, 1))
    }
)
part158: BinaryAssociation = BinaryAssociation(
    name="part158",
    ends={
        Property(name="template", type=JTL_template_ObjectTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="PropertyTemplateItem", type=PropertyTemplateItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inside159: BinaryAssociation = BinaryAssociation(
    name="inside159",
    ends={
        Property(name="AssignExp", type=JTL_template_ObjectTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_template_ObjectTemplateExp", type=AssignExp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value169: BinaryAssociation = BinaryAssociation(
    name="value169",
    ends={
        Property(name="OclExpression170", type=JTL_template_PropertyTemplateItem, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_template_PropertyTemplateItem", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referredProperty171: BinaryAssociation = BinaryAssociation(
    name="referredProperty171",
    ends={
        Property(name="Property173", type=JTL_template_PropertyTemplateItem, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_template_PropertyTemplateItem172", type=Property_, multiplicity=Multiplicity(1, 1))
    }
)
match164: BinaryAssociation = BinaryAssociation(
    name="match164",
    ends={
        Property(name="OclExpression166", type=JTL_template_CollectionTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_template_CollectionTemplateExp165", type=OclExpression, multiplicity=Multiplicity(0, 1))
    }
)
objContainer167: BinaryAssociation = BinaryAssociation(
    name="objContainer167",
    ends={
        Property(name="template168", type=JTL_template_PropertyTemplateItem, multiplicity=Multiplicity(1, 1)),
        Property(name="ObjectTemplateExp", type=ObjectTemplateExp, multiplicity=Multiplicity(1, 1))
    }
)
left178: BinaryAssociation = BinaryAssociation(
    name="left178",
    ends={
        Property(name="JTL_imperativeocl_AssignExp179", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True),
        Property(name="OclExpression180", type=JTL_imperativeocl_AssignExp, multiplicity=Multiplicity(1, 1))
    }
)
defaultValue181: BinaryAssociation = BinaryAssociation(
    name="defaultValue181",
    ends={
        Property(name="OclExpression183", type=JTL_imperativeocl_AssignExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_AssignExp182", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target174: BinaryAssociation = BinaryAssociation(
    name="target174",
    ends={
        Property(name="Variable175", type=JTL_imperativeocl_ImperativeIterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_ImperativeIterateExp", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value176: BinaryAssociation = BinaryAssociation(
    name="value176",
    ends={
        Property(name="OclExpression177", type=JTL_imperativeocl_AssignExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_AssignExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elsePart187: BinaryAssociation = BinaryAssociation(
    name="elsePart187",
    ends={
        Property(name="OclExpression189", type=JTL_imperativeocl_SwitchExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_SwitchExp188", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referredVariable190: BinaryAssociation = BinaryAssociation(
    name="referredVariable190",
    ends={
        Property(name="Variable191", type=JTL_imperativeocl_VariableInitExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_VariableInitExp", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body184: BinaryAssociation = BinaryAssociation(
    name="body184",
    ends={
        Property(name="OclExpression185", type=JTL_imperativeocl_BlockExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_BlockExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
alternativePart186: BinaryAssociation = BinaryAssociation(
    name="alternativePart186",
    ends={
        Property(name="AltExp", type=JTL_imperativeocl_SwitchExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_SwitchExp", type=AltExp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnedElement197: BinaryAssociation = BinaryAssociation(
    name="returnedElement197",
    ends={
        Property(name="essentialocl199", type=JTL_imperativeocl_ComputeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Variable198", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body200: BinaryAssociation = BinaryAssociation(
    name="body200",
    ends={
        Property(name="OclExpression201", type=JTL_imperativeocl_ComputeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_ComputeExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition192: BinaryAssociation = BinaryAssociation(
    name="condition192",
    ends={
        Property(name="OclExpression193", type=JTL_imperativeocl_WhileExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_WhileExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body194: BinaryAssociation = BinaryAssociation(
    name="body194",
    ends={
        Property(name="OclExpression196", type=JTL_imperativeocl_WhileExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_WhileExp195", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target207: BinaryAssociation = BinaryAssociation(
    name="target207",
    ends={
        Property(name="OclExpression208", type=JTL_imperativeocl_UnlinkExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_UnlinkExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
item209: BinaryAssociation = BinaryAssociation(
    name="item209",
    ends={
        Property(name="OclExpression211", type=JTL_imperativeocl_UnlinkExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_UnlinkExp210", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition202: BinaryAssociation = BinaryAssociation(
    name="condition202",
    ends={
        Property(name="OclExpression203", type=JTL_imperativeocl_AltExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_AltExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body204: BinaryAssociation = BinaryAssociation(
    name="body204",
    ends={
        Property(name="OclExpression206", type=JTL_imperativeocl_AltExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_AltExp205", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tryBody214: BinaryAssociation = BinaryAssociation(
    name="tryBody214",
    ends={
        Property(name="essentialocl216", type=JTL_imperativeocl_TryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression215", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exception217: BinaryAssociation = BinaryAssociation(
    name="exception217",
    ends={
        Property(name="Type218", type=JTL_imperativeocl_TryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_TryExp", type=Type, multiplicity=Multiplicity(0, 9999))
    }
)
exceptBody219: BinaryAssociation = BinaryAssociation(
    name="exceptBody219",
    ends={
        Property(name="OclExpression221", type=JTL_imperativeocl_TryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_TryExp220", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
value212: BinaryAssociation = BinaryAssociation(
    name="value212",
    ends={
        Property(name="OclExpression213", type=JTL_imperativeocl_ReturnExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_ReturnExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
element224: BinaryAssociation = BinaryAssociation(
    name="element224",
    ends={
        Property(name="OclExpression225", type=JTL_imperativeocl_TupleExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_TupleExp", type=OclExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
base226: BinaryAssociation = BinaryAssociation(
    name="base226",
    ends={
        Property(name="Type227", type=JTL_imperativeocl_Typedef, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_Typedef", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
exception222: BinaryAssociation = BinaryAssociation(
    name="exception222",
    ends={
        Property(name="Type223", type=JTL_imperativeocl_RaiseExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_RaiseExp", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
argument236: BinaryAssociation = BinaryAssociation(
    name="argument236",
    ends={
        Property(name="OclExpression238", type=JTL_imperativeocl_InstantiationExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_InstantiationExp237", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keyType239: BinaryAssociation = BinaryAssociation(
    name="keyType239",
    ends={
        Property(name="Type240", type=JTL_imperativeocl_DictionaryType, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_DictionaryType", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
condition228: BinaryAssociation = BinaryAssociation(
    name="condition228",
    ends={
        Property(name="OclExpression230", type=JTL_imperativeocl_Typedef, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_Typedef229", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
instantiatedClass231: BinaryAssociation = BinaryAssociation(
    name="instantiatedClass231",
    ends={
        Property(name="Class232", type=JTL_imperativeocl_InstantiationExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_InstantiationExp", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
extent233: BinaryAssociation = BinaryAssociation(
    name="extent233",
    ends={
        Property(name="Variable235", type=JTL_imperativeocl_InstantiationExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_InstantiationExp234", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
value244: BinaryAssociation = BinaryAssociation(
    name="value244",
    ends={
        Property(name="OclExpression246", type=JTL_imperativeocl_DictLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_DictLiteralPart245", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
part241: BinaryAssociation = BinaryAssociation(
    name="part241",
    ends={
        Property(name="DictLiteralPart", type=JTL_imperativeocl_DictLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_DictLiteralExp", type=DictLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key242: BinaryAssociation = BinaryAssociation(
    name="key242",
    ends={
        Property(name="OclExpression243", type=JTL_imperativeocl_DictLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_DictLiteralPart", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
log252: BinaryAssociation = BinaryAssociation(
    name="log252",
    ends={
        Property(name="LogExp", type=JTL_imperativeocl_AssertExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_AssertExp", type=LogExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assertion253: BinaryAssociation = BinaryAssociation(
    name="assertion253",
    ends={
        Property(name="OclExpression255", type=JTL_imperativeocl_AssertExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_AssertExp254", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition247: BinaryAssociation = BinaryAssociation(
    name="condition247",
    ends={
        Property(name="OclExpression248", type=JTL_imperativeocl_LogExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_LogExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
element249: BinaryAssociation = BinaryAssociation(
    name="element249",
    ends={
        Property(name="Element251", type=JTL_imperativeocl_LogExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_LogExp250", type=Element, multiplicity=Multiplicity(0, 1))
    }
)
condition256: BinaryAssociation = BinaryAssociation(
    name="condition256",
    ends={
        Property(name="OclExpression257", type=JTL_imperativeocl_ImperativeLoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_ImperativeLoopExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target258: BinaryAssociation = BinaryAssociation(
    name="target258",
    ends={
        Property(name="Variable259", type=JTL_imperativeocl_CollectorExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_CollectorExp", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elementType262: BinaryAssociation = BinaryAssociation(
    name="elementType262",
    ends={
        Property(name="JTL_imperativeocl_AnonymousTupleType", type=Type, multiplicity=Multiplicity(0, 9999)),
        Property(name="Type263", type=JTL_imperativeocl_AnonymousTupleType, multiplicity=Multiplicity(1, 1))
    }
)
part264: BinaryAssociation = BinaryAssociation(
    name="part264",
    ends={
        Property(name="AnonymousTupleLiteralPart", type=JTL_imperativeocl_AnonymousTupleLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_AnonymousTupleLiteralExp", type=AnonymousTupleLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value265: BinaryAssociation = BinaryAssociation(
    name="value265",
    ends={
        Property(name="OclExpression266", type=JTL_imperativeocl_AnonymousTupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_AnonymousTupleLiteralPart", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable260: BinaryAssociation = BinaryAssociation(
    name="variable260",
    ends={
        Property(name="Variable261", type=JTL_imperativeocl_UnpackExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_UnpackExp", type=Variable, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_JTL_emof_Class_Type = Generalization(general=Type, specific=JTL_emof_Class)
gen_JTL_emof_DataType_Type = Generalization(general=Type, specific=JTL_emof_DataType)
gen_JTL_emof_Element_Object = Generalization(general=Object, specific=JTL_emof_Element)
gen_JTL_emof_Tag_Element = Generalization(general=Element, specific=JTL_emof_Tag)
gen_JTL_emof_Enumeration_DataType = Generalization(general=DataType, specific=JTL_emof_Enumeration)
gen_JTL_emof_NamedElement_Element = Generalization(general=Element, specific=JTL_emof_NamedElement)
gen_JTL_emof_Extent_Object = Generalization(general=Object, specific=JTL_emof_Extent)
gen_JTL_emof_Operation_emof_MultiplicityElement = Generalization(general=emof_MultiplicityElement, specific=JTL_emof_Operation)
gen_JTL_emof_Operation_emof_TypedElement = Generalization(general=emof_TypedElement, specific=JTL_emof_Operation)
gen_JTL_emof_Package_NamedElement = Generalization(general=NamedElement, specific=JTL_emof_Package)
gen_JTL_emof_Type_NamedElement = Generalization(general=NamedElement, specific=JTL_emof_Type)
gen_JTL_emof_Parameter_emof_MultiplicityElement = Generalization(general=emof_MultiplicityElement, specific=JTL_emof_Parameter)
gen_JTL_emof_Parameter_emof_TypedElement = Generalization(general=emof_TypedElement, specific=JTL_emof_Parameter)
gen_JTL_emof_EnumerationLiteral_NamedElement = Generalization(general=NamedElement, specific=JTL_emof_EnumerationLiteral)
gen_JTL_emof_TypedElement_NamedElement = Generalization(general=NamedElement, specific=JTL_emof_TypedElement)
gen_JTL_emof_PrimitiveType_DataType = Generalization(general=DataType, specific=JTL_emof_PrimitiveType)
gen_JTL_emof_Property_emof_MultiplicityElement = Generalization(general=emof_MultiplicityElement, specific=JTL_emof_Property)
gen_JTL_emof_Property_emof_TypedElement = Generalization(general=emof_TypedElement, specific=JTL_emof_Property)
gen_JTL_emof_Comment_Element = Generalization(general=Element, specific=JTL_emof_Comment)
gen_JTL_JTL_Transformation_emof_Class = Generalization(general=emof_Class, specific=JTL_JTL_Transformation)
gen_JTL_JTL_Transformation_emof_Package = Generalization(general=emof_Package, specific=JTL_JTL_Transformation)
gen_JTL_emof_URIExtent_Extent = Generalization(general=Extent, specific=JTL_emof_URIExtent)
gen_JTL_JTL_Domain_NamedElement = Generalization(general=NamedElement, specific=JTL_JTL_Domain)
gen_JTL_JTL_Relation_NamedElement = Generalization(general=NamedElement, specific=JTL_JTL_Relation)
gen_JTL_JTL_Model_NamedElement = Generalization(general=NamedElement, specific=JTL_JTL_Model)
gen_JTL_JTL_Where_Pattern = Generalization(general=Pattern, specific=JTL_JTL_Where)
gen_JTL_JTL_Predicate_Element = Generalization(general=Element, specific=JTL_JTL_Predicate)
gen_JTL_JTL_When_Pattern = Generalization(general=Pattern, specific=JTL_JTL_When)
gen_JTL_JTL_Pattern_Element = Generalization(general=Element, specific=JTL_JTL_Pattern)
gen_JTL_essentialocl_OclExpression_TypedElement = Generalization(general=TypedElement, specific=JTL_essentialocl_OclExpression)
gen_JTL_essentialocl_BooleanLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=JTL_essentialocl_BooleanLiteralExp)
gen_JTL_essentialocl_CallExp_OclExpression = Generalization(general=OclExpression, specific=JTL_essentialocl_CallExp)
gen_JTL_essentialocl_LetExp_OclExpression = Generalization(general=OclExpression, specific=JTL_essentialocl_LetExp)
gen_JTL_essentialocl_UnlimitedNaturalExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=JTL_essentialocl_UnlimitedNaturalExp)
gen_JTL_essentialocl_IfExp_OclExpression = Generalization(general=OclExpression, specific=JTL_essentialocl_IfExp)
gen_JTL_essentialocl_PropertyCallExp_FeaturePropertyCall = Generalization(general=FeaturePropertyCall, specific=JTL_essentialocl_PropertyCallExp)
gen_JTL_essentialocl_Variable_TypedElement = Generalization(general=TypedElement, specific=JTL_essentialocl_Variable)
gen_JTL_essentialocl_LoopExp_essentialocl_CallExp = Generalization(general=essentialocl_CallExp, specific=JTL_essentialocl_LoopExp)
gen_JTL_essentialocl_LoopExp_essentialocl_OclExpression = Generalization(general=essentialocl_OclExpression, specific=JTL_essentialocl_LoopExp)
gen_JTL_essentialocl_VariableExp_OclExpression = Generalization(general=OclExpression, specific=JTL_essentialocl_VariableExp)
gen_JTL_essentialocl_TypeExp_OclExpression = Generalization(general=OclExpression, specific=JTL_essentialocl_TypeExp)
gen_JTL_essentialocl_RealLiteralExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=JTL_essentialocl_RealLiteralExp)
gen_JTL_essentialocl_LiteralExp_OclExpression = Generalization(general=OclExpression, specific=JTL_essentialocl_LiteralExp)
gen_JTL_essentialocl_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=JTL_essentialocl_IteratorExp)
gen_JTL_essentialocl_StringLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=JTL_essentialocl_StringLiteralExp)
gen_JTL_essentialocl_IntegerLiteralExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=JTL_essentialocl_IntegerLiteralExp)
gen_JTL_essentialocl_OperationCallExp_FeaturePropertyCall = Generalization(general=FeaturePropertyCall, specific=JTL_essentialocl_OperationCallExp)
gen_JTL_essentialocl_CollectionLiteralPart_TypedElement = Generalization(general=TypedElement, specific=JTL_essentialocl_CollectionLiteralPart)
gen_JTL_essentialocl_CollectionItem_CollectionLiteralPart = Generalization(general=CollectionLiteralPart, specific=JTL_essentialocl_CollectionItem)
gen_JTL_essentialocl_IterateExp_LoopExp = Generalization(general=LoopExp, specific=JTL_essentialocl_IterateExp)
gen_JTL_essentialocl_PrimitiveLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=JTL_essentialocl_PrimitiveLiteralExp)
gen_JTL_essentialocl_NumericLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=JTL_essentialocl_NumericLiteralExp)
gen_JTL_essentialocl_CollectionLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=JTL_essentialocl_CollectionLiteralExp)
gen_JTL_essentialocl_TupleLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=JTL_essentialocl_TupleLiteralExp)
gen_JTL_essentialocl_NullLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=JTL_essentialocl_NullLiteralExp)
gen_JTL_essentialocl_CollectionRange_CollectionLiteralPart = Generalization(general=CollectionLiteralPart, specific=JTL_essentialocl_CollectionRange)
gen_JTL_essentialocl_InvalidLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=JTL_essentialocl_InvalidLiteralExp)
gen_JTL_essentialocl_FeaturePropertyCall_CallExp = Generalization(general=CallExp, specific=JTL_essentialocl_FeaturePropertyCall)
gen_JTL_essentialocl_TupleLiteralPart_TypedElement = Generalization(general=TypedElement, specific=JTL_essentialocl_TupleLiteralPart)
gen_JTL_essentialocl_ExpressionInOcl_OpaqueExpression = Generalization(general=OpaqueExpression, specific=JTL_essentialocl_ExpressionInOcl)
gen_JTL_essentialocl_EnumLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=JTL_essentialocl_EnumLiteralExp)
gen_JTL_essentialocl_InvalidType_Type = Generalization(general=Type, specific=JTL_essentialocl_InvalidType)
gen_JTL_essentialocl_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=JTL_essentialocl_OrderedSetType)
gen_JTL_essentialocl_SequenceType_CollectionType = Generalization(general=CollectionType, specific=JTL_essentialocl_SequenceType)
gen_JTL_essentialocl_SetType_CollectionType = Generalization(general=CollectionType, specific=JTL_essentialocl_SetType)
gen_JTL_essentialocl_BagType_CollectionType = Generalization(general=CollectionType, specific=JTL_essentialocl_BagType)
gen_JTL_essentialocl_CollectionType_DataType = Generalization(general=DataType, specific=JTL_essentialocl_CollectionType)
gen_JTL_template_TemplateExp_LiteralExp = Generalization(general=LiteralExp, specific=JTL_template_TemplateExp)
gen_JTL_essentialocl_TupleType_emof_Class = Generalization(general=emof_Class, specific=JTL_essentialocl_TupleType)
gen_JTL_essentialocl_TupleType_emof_DataType = Generalization(general=emof_DataType, specific=JTL_essentialocl_TupleType)
gen_JTL_essentialocl_VoidType_Type = Generalization(general=Type, specific=JTL_essentialocl_VoidType)
gen_JTL_essentialocl_AnyType_emof_Class = Generalization(general=emof_Class, specific=JTL_essentialocl_AnyType)
gen_JTL_essentialocl_AnyType_emof_Type = Generalization(general=emof_Type, specific=JTL_essentialocl_AnyType)
gen_JTL_template_CollectionTemplateExp_TemplateExp = Generalization(general=TemplateExp, specific=JTL_template_CollectionTemplateExp)
gen_JTL_template_ObjectTemplateExp_TemplateExp = Generalization(general=TemplateExp, specific=JTL_template_ObjectTemplateExp)
gen_JTL_imperativeocl_ImperativeIterateExp_ImperativeLoopExp = Generalization(general=ImperativeLoopExp, specific=JTL_imperativeocl_ImperativeIterateExp)
gen_JTL_template_PropertyTemplateItem_Element = Generalization(general=Element, specific=JTL_template_PropertyTemplateItem)
gen_JTL_imperativeocl_BlockExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTL_imperativeocl_BlockExp)
gen_JTL_imperativeocl_AssignExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTL_imperativeocl_AssignExp)
gen_JTL_imperativeocl_VariableInitExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTL_imperativeocl_VariableInitExp)
gen_JTL_imperativeocl_SwitchExp_essentialocl_CallExp = Generalization(general=essentialocl_CallExp, specific=JTL_imperativeocl_SwitchExp)
gen_JTL_imperativeocl_SwitchExp_imperativeocl_ImperativeExpression = Generalization(general=imperativeocl_ImperativeExpression, specific=JTL_imperativeocl_SwitchExp)
gen_JTL_imperativeocl_ComputeExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTL_imperativeocl_ComputeExp)
gen_JTL_imperativeocl_WhileExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTL_imperativeocl_WhileExp)
gen_JTL_imperativeocl_UnlinkExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTL_imperativeocl_UnlinkExp)
gen_JTL_imperativeocl_AltExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTL_imperativeocl_AltExp)
gen_JTL_imperativeocl_ReturnExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTL_imperativeocl_ReturnExp)
gen_JTL_imperativeocl_BreakExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTL_imperativeocl_BreakExp)
gen_JTL_imperativeocl_TryExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTL_imperativeocl_TryExp)
gen_JTL_imperativeocl_Typedef_Class = Generalization(general=Class_, specific=JTL_imperativeocl_Typedef)
gen_JTL_imperativeocl_RaiseExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTL_imperativeocl_RaiseExp)
gen_JTL_imperativeocl_ContinueExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTL_imperativeocl_ContinueExp)
gen_JTL_imperativeocl_ForExp_ImperativeLoopExp = Generalization(general=ImperativeLoopExp, specific=JTL_imperativeocl_ForExp)
gen_JTL_imperativeocl_TupleExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTL_imperativeocl_TupleExp)
gen_JTL_imperativeocl_DictionaryType_CollectionType = Generalization(general=CollectionType, specific=JTL_imperativeocl_DictionaryType)
gen_JTL_imperativeocl_InstantiationExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTL_imperativeocl_InstantiationExp)
gen_JTL_imperativeocl_TemplateParameterType_Type = Generalization(general=Type, specific=JTL_imperativeocl_TemplateParameterType)
gen_JTL_imperativeocl_LogExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTL_imperativeocl_LogExp)
gen_JTL_imperativeocl_DictLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=JTL_imperativeocl_DictLiteralExp)
gen_JTL_imperativeocl_DictLiteralPart_Element = Generalization(general=Element, specific=JTL_imperativeocl_DictLiteralPart)
gen_JTL_imperativeocl_AssertExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTL_imperativeocl_AssertExp)
gen_JTL_imperativeocl_CollectorExp_ImperativeLoopExp = Generalization(general=ImperativeLoopExp, specific=JTL_imperativeocl_CollectorExp)
gen_JTL_imperativeocl_ImperativeExpression_OclExpression = Generalization(general=OclExpression, specific=JTL_imperativeocl_ImperativeExpression)
gen_JTL_imperativeocl_ImperativeLoopExp_essentialocl_LoopExp = Generalization(general=essentialocl_LoopExp, specific=JTL_imperativeocl_ImperativeLoopExp)
gen_JTL_imperativeocl_ImperativeLoopExp_imperativeocl_ImperativeExpression = Generalization(general=imperativeocl_ImperativeExpression, specific=JTL_imperativeocl_ImperativeLoopExp)
gen_JTL_imperativeocl_AnonymousTupleLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=JTL_imperativeocl_AnonymousTupleLiteralExp)
gen_JTL_imperativeocl_AnonymousTupleLiteralPart_Element = Generalization(general=Element, specific=JTL_imperativeocl_AnonymousTupleLiteralPart)
gen_JTL_imperativeocl_UnpackExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTL_imperativeocl_UnpackExp)
gen_JTL_imperativeocl_AnonymousTupleType_Class = Generalization(general=Class_, specific=JTL_imperativeocl_AnonymousTupleType)
gen_JTL_imperativeocl_ListType_CollectionType = Generalization(general=CollectionType, specific=JTL_imperativeocl_ListType)

# Domain Model
domain_model = DomainModel(
    name="JTL",
    types={JTL_emof_Class, Type, Property_, Class_, JTL_emof_DataType, JTL_emof_Element, Object, Tag, Comment, JTL_emof_Tag, Element, Operation, JTL_emof_Enumeration, DataType, EnumerationLiteral, JTL_emof_NamedElement, JTL_emof_Extent, JTL_emof_Object, JTL_emof_Operation, emof_MultiplicityElement, emof_TypedElement, Parameter_, JTL_emof_MultiplicityElement, JTL_emof_Package, NamedElement, JTL_emof_Type, JTL_emof_Parameter, JTL_emof_EnumerationLiteral, Enumeration_, Package, JTL_emof_TypedElement, JTL_emof_PrimitiveType, JTL_emof_URIExtent, JTL_emof_Property, JTL_emof_Comment, JTL_JTL_Transformation, emof_Class, emof_Package, Model, Relation, Extent, Domain, Where, When, Variable, JTL_JTL_Domain, JTL_JTL_Relation, Transformation, Pattern, JTL_JTL_Model, Predicate, JTL_JTL_Where, TemplateExp, JTL_JTL_Predicate, OclExpression, JTL_JTL_When, JTL_JTL_Pattern, JTL_essentialocl_OclExpression, TypedElement, TryExp, JTL_essentialocl_BooleanLiteralExp, PrimitiveLiteralExp, JTL_essentialocl_CallExp, JTL_essentialocl_LetExp, JTL_essentialocl_UnlimitedNaturalExp, NumericLiteralExp, JTL_essentialocl_IfExp, ComputeExp, JTL_essentialocl_PropertyCallExp, FeaturePropertyCall, JTL_essentialocl_Variable, LetExp, JTL_essentialocl_LoopExp, essentialocl_CallExp, essentialocl_OclExpression, JTL_essentialocl_IteratorExp, LoopExp, JTL_essentialocl_VariableExp, JTL_essentialocl_TypeExp, JTL_essentialocl_RealLiteralExp, JTL_essentialocl_LiteralExp, JTL_essentialocl_StringLiteralExp, JTL_essentialocl_IntegerLiteralExp, JTL_essentialocl_OperationCallExp, CollectionLiteralPart, JTL_essentialocl_CollectionLiteralPart, CollectionLiteralExp, JTL_essentialocl_CollectionItem, JTL_essentialocl_IterateExp, JTL_essentialocl_PrimitiveLiteralExp, LiteralExp, JTL_essentialocl_NumericLiteralExp, JTL_essentialocl_CollectionLiteralExp, JTL_essentialocl_TupleLiteralExp, TupleLiteralPart, JTL_essentialocl_NullLiteralExp, JTL_essentialocl_CollectionRange, JTL_essentialocl_OpaqueExpression, JTL_essentialocl_InvalidLiteralExp, JTL_essentialocl_FeaturePropertyCall, CallExp, JTL_essentialocl_TupleLiteralPart, JTL_essentialocl_ExpressionInOcl, OpaqueExpression, JTL_essentialocl_EnumLiteralExp, JTL_essentialocl_InvalidType, JTL_essentialocl_OrderedSetType, JTL_essentialocl_SequenceType, JTL_essentialocl_SetType, TupleLiteralExp, JTL_essentialocl_BagType, CollectionType, JTL_essentialocl_CollectionType, JTL_template_TemplateExp, JTL_essentialocl_TupleType, emof_DataType, JTL_essentialocl_VoidType, JTL_essentialocl_AnyType, emof_Type, JTL_template_CollectionTemplateExp, JTL_template_ObjectTemplateExp, PropertyTemplateItem, AssignExp, JTL_imperativeocl_ImperativeIterateExp, ImperativeLoopExp, JTL_template_PropertyTemplateItem, ObjectTemplateExp, JTL_imperativeocl_BlockExp, JTL_imperativeocl_AssignExp, ImperativeExpression, JTL_imperativeocl_VariableInitExp, JTL_imperativeocl_SwitchExp, imperativeocl_ImperativeExpression, AltExp, JTL_imperativeocl_ComputeExp, JTL_imperativeocl_WhileExp, JTL_imperativeocl_UnlinkExp, JTL_imperativeocl_AltExp, JTL_imperativeocl_ReturnExp, JTL_imperativeocl_BreakExp, JTL_imperativeocl_TryExp, JTL_imperativeocl_Typedef, JTL_imperativeocl_RaiseExp, JTL_imperativeocl_ContinueExp, JTL_imperativeocl_ForExp, JTL_imperativeocl_TupleExp, JTL_imperativeocl_DictionaryType, JTL_imperativeocl_InstantiationExp, JTL_imperativeocl_TemplateParameterType, JTL_imperativeocl_LogExp, JTL_imperativeocl_DictLiteralExp, DictLiteralPart, JTL_imperativeocl_DictLiteralPart, JTL_imperativeocl_AssertExp, LogExp, JTL_imperativeocl_CollectorExp, JTL_imperativeocl_ImperativeExpression, JTL_imperativeocl_ImperativeLoopExp, essentialocl_LoopExp, JTL_imperativeocl_AnonymousTupleLiteralExp, AnonymousTupleLiteralPart, JTL_imperativeocl_AnonymousTupleLiteralPart, JTL_imperativeocl_UnpackExp, JTL_imperativeocl_AnonymousTupleType, JTL_imperativeocl_ListType, CollectionKind, SeverityKind},
    associations={ownedAttribute0, superClass3, tag4, ownedComment6, ownedOperation1, ownedLiteral9, element7, ownedParameter14, raisedException16, ownedType17, class11, package21, operation24, enumeration27, nestedPackage20, Class29, opposite32, annotatedElement34, modelParameter35, relation36, domain40, where42, when44, variable46, transformation38, relation47, pattern50, model51, rootVariable54, transformation57, dependsOn60, whenOwner75, predicate62, bindsTo64, templateExpression66, domain68, pattern71, conditionExpression74, whereOwner78, tryBodyOwner83, source81, elseExpression89, in92, condition84, thenExpression86, bindParameter100, computeOwner103, referredProperty105, variable94, initExpression96, LetExp98, body111, iterator113, referredVariable107, referredType109, argument116, referredOperation118, part123, CollectionLiteralExp125, result121, last131, part134, item127, first129, parameterVariable144, bodyExpression136, context138, resultVariable141, referredEnumLiteral151, TupleLiteralExp147, elementType149, bindsTo153, where155, part160, referredCollectionType162, part158, inside159, value169, referredProperty171, match164, objContainer167, left178, defaultValue181, target174, value176, elsePart187, referredVariable190, body184, alternativePart186, returnedElement197, body200, condition192, body194, target207, item209, condition202, body204, tryBody214, exception217, exceptBody219, value212, element224, base226, exception222, argument236, keyType239, condition228, instantiatedClass231, extent233, value244, part241, key242, log252, assertion253, condition247, element249, condition256, target258, elementType262, part264, value265, variable260},
    generalizations={gen_JTL_emof_Class_Type, gen_JTL_emof_DataType_Type, gen_JTL_emof_Element_Object, gen_JTL_emof_Tag_Element, gen_JTL_emof_Enumeration_DataType, gen_JTL_emof_NamedElement_Element, gen_JTL_emof_Extent_Object, gen_JTL_emof_Operation_emof_MultiplicityElement, gen_JTL_emof_Operation_emof_TypedElement, gen_JTL_emof_Package_NamedElement, gen_JTL_emof_Type_NamedElement, gen_JTL_emof_Parameter_emof_MultiplicityElement, gen_JTL_emof_Parameter_emof_TypedElement, gen_JTL_emof_EnumerationLiteral_NamedElement, gen_JTL_emof_TypedElement_NamedElement, gen_JTL_emof_PrimitiveType_DataType, gen_JTL_emof_Property_emof_MultiplicityElement, gen_JTL_emof_Property_emof_TypedElement, gen_JTL_emof_Comment_Element, gen_JTL_JTL_Transformation_emof_Class, gen_JTL_JTL_Transformation_emof_Package, gen_JTL_emof_URIExtent_Extent, gen_JTL_JTL_Domain_NamedElement, gen_JTL_JTL_Relation_NamedElement, gen_JTL_JTL_Model_NamedElement, gen_JTL_JTL_Where_Pattern, gen_JTL_JTL_Predicate_Element, gen_JTL_JTL_When_Pattern, gen_JTL_JTL_Pattern_Element, gen_JTL_essentialocl_OclExpression_TypedElement, gen_JTL_essentialocl_BooleanLiteralExp_PrimitiveLiteralExp, gen_JTL_essentialocl_CallExp_OclExpression, gen_JTL_essentialocl_LetExp_OclExpression, gen_JTL_essentialocl_UnlimitedNaturalExp_NumericLiteralExp, gen_JTL_essentialocl_IfExp_OclExpression, gen_JTL_essentialocl_PropertyCallExp_FeaturePropertyCall, gen_JTL_essentialocl_Variable_TypedElement, gen_JTL_essentialocl_LoopExp_essentialocl_CallExp, gen_JTL_essentialocl_LoopExp_essentialocl_OclExpression, gen_JTL_essentialocl_VariableExp_OclExpression, gen_JTL_essentialocl_TypeExp_OclExpression, gen_JTL_essentialocl_RealLiteralExp_NumericLiteralExp, gen_JTL_essentialocl_LiteralExp_OclExpression, gen_JTL_essentialocl_IteratorExp_LoopExp, gen_JTL_essentialocl_StringLiteralExp_PrimitiveLiteralExp, gen_JTL_essentialocl_IntegerLiteralExp_NumericLiteralExp, gen_JTL_essentialocl_OperationCallExp_FeaturePropertyCall, gen_JTL_essentialocl_CollectionLiteralPart_TypedElement, gen_JTL_essentialocl_CollectionItem_CollectionLiteralPart, gen_JTL_essentialocl_IterateExp_LoopExp, gen_JTL_essentialocl_PrimitiveLiteralExp_LiteralExp, gen_JTL_essentialocl_NumericLiteralExp_PrimitiveLiteralExp, gen_JTL_essentialocl_CollectionLiteralExp_LiteralExp, gen_JTL_essentialocl_TupleLiteralExp_LiteralExp, gen_JTL_essentialocl_NullLiteralExp_LiteralExp, gen_JTL_essentialocl_CollectionRange_CollectionLiteralPart, gen_JTL_essentialocl_InvalidLiteralExp_LiteralExp, gen_JTL_essentialocl_FeaturePropertyCall_CallExp, gen_JTL_essentialocl_TupleLiteralPart_TypedElement, gen_JTL_essentialocl_ExpressionInOcl_OpaqueExpression, gen_JTL_essentialocl_EnumLiteralExp_LiteralExp, gen_JTL_essentialocl_InvalidType_Type, gen_JTL_essentialocl_OrderedSetType_CollectionType, gen_JTL_essentialocl_SequenceType_CollectionType, gen_JTL_essentialocl_SetType_CollectionType, gen_JTL_essentialocl_BagType_CollectionType, gen_JTL_essentialocl_CollectionType_DataType, gen_JTL_template_TemplateExp_LiteralExp, gen_JTL_essentialocl_TupleType_emof_Class, gen_JTL_essentialocl_TupleType_emof_DataType, gen_JTL_essentialocl_VoidType_Type, gen_JTL_essentialocl_AnyType_emof_Class, gen_JTL_essentialocl_AnyType_emof_Type, gen_JTL_template_CollectionTemplateExp_TemplateExp, gen_JTL_template_ObjectTemplateExp_TemplateExp, gen_JTL_imperativeocl_ImperativeIterateExp_ImperativeLoopExp, gen_JTL_template_PropertyTemplateItem_Element, gen_JTL_imperativeocl_BlockExp_ImperativeExpression, gen_JTL_imperativeocl_AssignExp_ImperativeExpression, gen_JTL_imperativeocl_VariableInitExp_ImperativeExpression, gen_JTL_imperativeocl_SwitchExp_essentialocl_CallExp, gen_JTL_imperativeocl_SwitchExp_imperativeocl_ImperativeExpression, gen_JTL_imperativeocl_ComputeExp_ImperativeExpression, gen_JTL_imperativeocl_WhileExp_ImperativeExpression, gen_JTL_imperativeocl_UnlinkExp_ImperativeExpression, gen_JTL_imperativeocl_AltExp_ImperativeExpression, gen_JTL_imperativeocl_ReturnExp_ImperativeExpression, gen_JTL_imperativeocl_BreakExp_ImperativeExpression, gen_JTL_imperativeocl_TryExp_ImperativeExpression, gen_JTL_imperativeocl_Typedef_Class, gen_JTL_imperativeocl_RaiseExp_ImperativeExpression, gen_JTL_imperativeocl_ContinueExp_ImperativeExpression, gen_JTL_imperativeocl_ForExp_ImperativeLoopExp, gen_JTL_imperativeocl_TupleExp_ImperativeExpression, gen_JTL_imperativeocl_DictionaryType_CollectionType, gen_JTL_imperativeocl_InstantiationExp_ImperativeExpression, gen_JTL_imperativeocl_TemplateParameterType_Type, gen_JTL_imperativeocl_LogExp_ImperativeExpression, gen_JTL_imperativeocl_DictLiteralExp_LiteralExp, gen_JTL_imperativeocl_DictLiteralPart_Element, gen_JTL_imperativeocl_AssertExp_ImperativeExpression, gen_JTL_imperativeocl_CollectorExp_ImperativeLoopExp, gen_JTL_imperativeocl_ImperativeExpression_OclExpression, gen_JTL_imperativeocl_ImperativeLoopExp_essentialocl_LoopExp, gen_JTL_imperativeocl_ImperativeLoopExp_imperativeocl_ImperativeExpression, gen_JTL_imperativeocl_AnonymousTupleLiteralExp_LiteralExp, gen_JTL_imperativeocl_AnonymousTupleLiteralPart_Element, gen_JTL_imperativeocl_UnpackExp_ImperativeExpression, gen_JTL_imperativeocl_AnonymousTupleType_Class, gen_JTL_imperativeocl_ListType_CollectionType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)