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
Operation = Class(name="Operation")
Janus_emof_Class = Class(name="Janus::emof::Class")
Type = Class(name="Type")
Property_ = Class(name="Property")
Janus_emof_Enumeration = Class(name="Janus::emof::Enumeration")
DataType = Class(name="DataType")
Class_ = Class(name="Class")
Janus_emof_DataType = Class(name="Janus::emof::DataType", is_abstract=True)
Janus_emof_Element = Class(name="Janus::emof::Element", is_abstract=True)
Object = Class(name="Object")
Tag = Class(name="Tag")
Comment = Class(name="Comment")
Janus_emof_Tag = Class(name="Janus::emof::Tag")
Element = Class(name="Element")
Janus_emof_MultiplicityElement = Class(name="Janus::emof::MultiplicityElement", is_abstract=True)
EnumerationLiteral = Class(name="EnumerationLiteral")
Janus_emof_NamedElement = Class(name="Janus::emof::NamedElement", is_abstract=True)
Janus_emof_Extent = Class(name="Janus::emof::Extent")
Janus_emof_Object = Class(name="Janus::emof::Object")
Janus_emof_Operation = Class(name="Janus::emof::Operation")
emof_MultiplicityElement = Class(name="emof::MultiplicityElement")
emof_TypedElement = Class(name="emof::TypedElement")
Parameter_ = Class(name="Parameter")
Janus_emof_EnumerationLiteral = Class(name="Janus::emof::EnumerationLiteral")
Enumeration_ = Class(name="Enumeration")
Janus_emof_Package = Class(name="Janus::emof::Package")
NamedElement = Class(name="NamedElement")
Package = Class(name="Package")
Janus_emof_Type = Class(name="Janus::emof::Type", is_abstract=True)
Janus_emof_Parameter = Class(name="Janus::emof::Parameter")
Janus_emof_Property = Class(name="Janus::emof::Property")
Janus_emof_TypedElement = Class(name="Janus::emof::TypedElement", is_abstract=True)
Janus_emof_PrimitiveType = Class(name="Janus::emof::PrimitiveType")
Janus_emof_URIExtent = Class(name="Janus::emof::URIExtent")
Extent = Class(name="Extent")
Janus_emof_Comment = Class(name="Janus::emof::Comment")
Janus_JTL_Transformation = Class(name="Janus::JTL::Transformation")
emof_Class = Class(name="emof::Class")
emof_Package = Class(name="emof::Package")
Model = Class(name="Model")
Pattern = Class(name="Pattern")
Relation = Class(name="Relation")
Janus_JTL_Relation = Class(name="Janus::JTL::Relation")
Transformation = Class(name="Transformation")
Domain = Class(name="Domain")
Variable = Class(name="Variable")
Janus_JTL_Domain = Class(name="Janus::JTL::Domain")
Janus_JTL_Model = Class(name="Janus::JTL::Model")
Janus_JTL_Pattern = Class(name="Janus::JTL::Pattern")
Janus_JTL_Predicate = Class(name="Janus::JTL::Predicate")
Predicate = Class(name="Predicate")
TemplateExp = Class(name="TemplateExp")
Janus_essentialocl_CallExp = Class(name="Janus::essentialocl::CallExp", is_abstract=True)
OclExpression = Class(name="OclExpression")
Janus_essentialocl_BooleanLiteralExp = Class(name="Janus::essentialocl::BooleanLiteralExp")
PrimitiveLiteralExp = Class(name="PrimitiveLiteralExp")
TryExp = Class(name="TryExp")
Janus_essentialocl_OclExpression = Class(name="Janus::essentialocl::OclExpression", is_abstract=True)
TypedElement = Class(name="TypedElement")
Janus_essentialocl_UnlimitedNaturalExp = Class(name="Janus::essentialocl::UnlimitedNaturalExp")
NumericLiteralExp = Class(name="NumericLiteralExp")
Janus_essentialocl_IfExp = Class(name="Janus::essentialocl::IfExp")
Janus_essentialocl_Variable = Class(name="Janus::essentialocl::Variable")
Janus_essentialocl_LetExp = Class(name="Janus::essentialocl::LetExp")
Janus_essentialocl_PropertyCallExp = Class(name="Janus::essentialocl::PropertyCallExp")
FeaturePropertyCall = Class(name="FeaturePropertyCall")
LetExp = Class(name="LetExp")
ComputeExp = Class(name="ComputeExp")
Janus_essentialocl_LoopExp = Class(name="Janus::essentialocl::LoopExp", is_abstract=True)
Janus_essentialocl_VariableExp = Class(name="Janus::essentialocl::VariableExp")
Janus_essentialocl_TypeExp = Class(name="Janus::essentialocl::TypeExp")
Janus_essentialocl_StringLiteralExp = Class(name="Janus::essentialocl::StringLiteralExp")
essentialocl_CallExp = Class(name="essentialocl::CallExp")
essentialocl_OclExpression = Class(name="essentialocl::OclExpression")
Janus_essentialocl_IteratorExp = Class(name="Janus::essentialocl::IteratorExp")
LoopExp = Class(name="LoopExp")
Janus_essentialocl_IntegerLiteralExp = Class(name="Janus::essentialocl::IntegerLiteralExp")
Janus_essentialocl_OperationCallExp = Class(name="Janus::essentialocl::OperationCallExp")
Janus_essentialocl_RealLiteralExp = Class(name="Janus::essentialocl::RealLiteralExp")
Janus_essentialocl_LiteralExp = Class(name="Janus::essentialocl::LiteralExp", is_abstract=True)
Janus_essentialocl_IterateExp = Class(name="Janus::essentialocl::IterateExp")
CollectionLiteralExp = Class(name="CollectionLiteralExp")
Janus_essentialocl_PrimitiveLiteralExp = Class(name="Janus::essentialocl::PrimitiveLiteralExp", is_abstract=True)
LiteralExp = Class(name="LiteralExp")
Janus_essentialocl_NumericLiteralExp = Class(name="Janus::essentialocl::NumericLiteralExp", is_abstract=True)
Janus_essentialocl_CollectionLiteralExp = Class(name="Janus::essentialocl::CollectionLiteralExp")
CollectionLiteralPart = Class(name="CollectionLiteralPart")
Janus_essentialocl_CollectionLiteralPart = Class(name="Janus::essentialocl::CollectionLiteralPart", is_abstract=True)
Janus_essentialocl_CollectionItem = Class(name="Janus::essentialocl::CollectionItem")
Janus_essentialocl_CollectionRange = Class(name="Janus::essentialocl::CollectionRange")
Janus_essentialocl_NullLiteralExp = Class(name="Janus::essentialocl::NullLiteralExp")
Janus_essentialocl_ExpressionInOcl = Class(name="Janus::essentialocl::ExpressionInOcl")
OpaqueExpression = Class(name="OpaqueExpression")
Janus_essentialocl_TupleLiteralExp = Class(name="Janus::essentialocl::TupleLiteralExp")
TupleLiteralPart = Class(name="TupleLiteralPart")
TupleLiteralExp = Class(name="TupleLiteralExp")
Janus_essentialocl_BagType = Class(name="Janus::essentialocl::BagType")
Janus_essentialocl_OpaqueExpression = Class(name="Janus::essentialocl::OpaqueExpression")
Janus_essentialocl_InvalidLiteralExp = Class(name="Janus::essentialocl::InvalidLiteralExp")
Janus_essentialocl_FeaturePropertyCall = Class(name="Janus::essentialocl::FeaturePropertyCall", is_abstract=True)
CallExp = Class(name="CallExp")
Janus_essentialocl_TupleLiteralPart = Class(name="Janus::essentialocl::TupleLiteralPart")
Janus_essentialocl_SetType = Class(name="Janus::essentialocl::SetType")
Janus_essentialocl_TupleType = Class(name="Janus::essentialocl::TupleType")
emof_DataType = Class(name="emof::DataType")
Janus_essentialocl_VoidType = Class(name="Janus::essentialocl::VoidType")
Janus_essentialocl_AnyType = Class(name="Janus::essentialocl::AnyType")
emof_Type = Class(name="emof::Type")
Janus_template_TemplateExp = Class(name="Janus::template::TemplateExp", is_abstract=True)
CollectionType = Class(name="CollectionType")
Janus_essentialocl_CollectionType = Class(name="Janus::essentialocl::CollectionType", is_abstract=True)
Janus_essentialocl_EnumLiteralExp = Class(name="Janus::essentialocl::EnumLiteralExp")
Janus_essentialocl_InvalidType = Class(name="Janus::essentialocl::InvalidType")
Janus_essentialocl_OrderedSetType = Class(name="Janus::essentialocl::OrderedSetType")
Janus_essentialocl_SequenceType = Class(name="Janus::essentialocl::SequenceType")
Janus_template_ObjectTemplateExp = Class(name="Janus::template::ObjectTemplateExp")
PropertyTemplateItem = Class(name="PropertyTemplateItem")
Janus_template_CollectionTemplateExp = Class(name="Janus::template::CollectionTemplateExp")
Janus_imperativeocl_AssignExp = Class(name="Janus::imperativeocl::AssignExp")
ImperativeExpression = Class(name="ImperativeExpression")
Janus_template_PropertyTemplateItem = Class(name="Janus::template::PropertyTemplateItem")
ObjectTemplateExp = Class(name="ObjectTemplateExp")
Janus_imperativeocl_ImperativeIterateExp = Class(name="Janus::imperativeocl::ImperativeIterateExp")
ImperativeLoopExp = Class(name="ImperativeLoopExp")
Janus_imperativeocl_BlockExp = Class(name="Janus::imperativeocl::BlockExp")
Janus_imperativeocl_VariableInitExp = Class(name="Janus::imperativeocl::VariableInitExp")
Janus_imperativeocl_SwitchExp = Class(name="Janus::imperativeocl::SwitchExp")
imperativeocl_ImperativeExpression = Class(name="imperativeocl::ImperativeExpression")
AltExp = Class(name="AltExp")
Janus_imperativeocl_WhileExp = Class(name="Janus::imperativeocl::WhileExp")
Janus_imperativeocl_AltExp = Class(name="Janus::imperativeocl::AltExp")
Janus_imperativeocl_ComputeExp = Class(name="Janus::imperativeocl::ComputeExp")
Janus_imperativeocl_UnlinkExp = Class(name="Janus::imperativeocl::UnlinkExp")
Janus_imperativeocl_BreakExp = Class(name="Janus::imperativeocl::BreakExp")
Janus_imperativeocl_TryExp = Class(name="Janus::imperativeocl::TryExp")
Janus_imperativeocl_ReturnExp = Class(name="Janus::imperativeocl::ReturnExp")
Janus_imperativeocl_RaiseExp = Class(name="Janus::imperativeocl::RaiseExp")
Janus_imperativeocl_ContinueExp = Class(name="Janus::imperativeocl::ContinueExp")
Janus_imperativeocl_ForExp = Class(name="Janus::imperativeocl::ForExp")
Janus_imperativeocl_TupleExp = Class(name="Janus::imperativeocl::TupleExp")
Janus_imperativeocl_Typedef = Class(name="Janus::imperativeocl::Typedef")
Janus_imperativeocl_InstantiationExp = Class(name="Janus::imperativeocl::InstantiationExp")
Janus_imperativeocl_DictionaryType = Class(name="Janus::imperativeocl::DictionaryType")
Janus_imperativeocl_DictLiteralExp = Class(name="Janus::imperativeocl::DictLiteralExp")
Janus_imperativeocl_LogExp = Class(name="Janus::imperativeocl::LogExp")
DictLiteralPart = Class(name="DictLiteralPart")
Janus_imperativeocl_DictLiteralPart = Class(name="Janus::imperativeocl::DictLiteralPart")
Janus_imperativeocl_TemplateParameterType = Class(name="Janus::imperativeocl::TemplateParameterType")
Janus_imperativeocl_ImperativeLoopExp = Class(name="Janus::imperativeocl::ImperativeLoopExp", is_abstract=True)
essentialocl_LoopExp = Class(name="essentialocl::LoopExp")
Janus_imperativeocl_AssertExp = Class(name="Janus::imperativeocl::AssertExp")
LogExp = Class(name="LogExp")
Janus_imperativeocl_AnonymousTupleType = Class(name="Janus::imperativeocl::AnonymousTupleType")
Janus_imperativeocl_AnonymousTupleLiteralExp = Class(name="Janus::imperativeocl::AnonymousTupleLiteralExp")
AnonymousTupleLiteralPart = Class(name="AnonymousTupleLiteralPart")
Janus_imperativeocl_CollectorExp = Class(name="Janus::imperativeocl::CollectorExp")
Janus_imperativeocl_ImperativeExpression = Class(name="Janus::imperativeocl::ImperativeExpression", is_abstract=True)
Janus_imperativeocl_UnpackExp = Class(name="Janus::imperativeocl::UnpackExp")
Janus_imperativeocl_AnonymousTupleLiteralPart = Class(name="Janus::imperativeocl::AnonymousTupleLiteralPart")
Janus_imperativeocl_ListType = Class(name="Janus::imperativeocl::ListType")

# Operation class attributes and methods

# Janus_emof_Class class attributes and methods
Janus_emof_Class_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
Janus_emof_Class.attributes={Janus_emof_Class_isAbstract}

# Type class attributes and methods

# Property class attributes and methods

# Janus_emof_Enumeration class attributes and methods

# DataType class attributes and methods

# Class class attributes and methods

# Janus_emof_DataType class attributes and methods

# Janus_emof_Element class attributes and methods

# Object class attributes and methods

# Tag class attributes and methods

# Comment class attributes and methods

# Janus_emof_Tag class attributes and methods
Janus_emof_Tag_name: Property = Property(name="name", type=StringType)
Janus_emof_Tag_value: Property = Property(name="value", type=StringType)
Janus_emof_Tag.attributes={Janus_emof_Tag_name, Janus_emof_Tag_value}

# Element class attributes and methods

# Janus_emof_MultiplicityElement class attributes and methods
Janus_emof_MultiplicityElement_isOrdered: Property = Property(name="isOrdered", type=StringType)
Janus_emof_MultiplicityElement_isUnique: Property = Property(name="isUnique", type=StringType)
Janus_emof_MultiplicityElement_lower: Property = Property(name="lower", type=IntegerType)
Janus_emof_MultiplicityElement_upper: Property = Property(name="upper", type=StringType)
Janus_emof_MultiplicityElement.attributes={Janus_emof_MultiplicityElement_isOrdered, Janus_emof_MultiplicityElement_lower, Janus_emof_MultiplicityElement_upper, Janus_emof_MultiplicityElement_isUnique}

# EnumerationLiteral class attributes and methods

# Janus_emof_NamedElement class attributes and methods
Janus_emof_NamedElement_name: Property = Property(name="name", type=StringType)
Janus_emof_NamedElement.attributes={Janus_emof_NamedElement_name}

# Janus_emof_Extent class attributes and methods

# Janus_emof_Object class attributes and methods

# Janus_emof_Operation class attributes and methods

# emof_MultiplicityElement class attributes and methods

# emof_TypedElement class attributes and methods

# Parameter class attributes and methods

# Janus_emof_EnumerationLiteral class attributes and methods

# Enumeration class attributes and methods

# Janus_emof_Package class attributes and methods
Janus_emof_Package_uri: Property = Property(name="uri", type=StringType)
Janus_emof_Package.attributes={Janus_emof_Package_uri}

# NamedElement class attributes and methods

# Package class attributes and methods

# Janus_emof_Type class attributes and methods

# Janus_emof_Parameter class attributes and methods

# Janus_emof_Property class attributes and methods
Janus_emof_Property_isReadOnly: Property = Property(name="isReadOnly", type=BooleanType)
Janus_emof_Property_isDerived: Property = Property(name="isDerived", type=BooleanType)
Janus_emof_Property_isComposite: Property = Property(name="isComposite", type=BooleanType)
Janus_emof_Property_isId: Property = Property(name="isId", type=BooleanType)
Janus_emof_Property_default: Property = Property(name="default", type=StringType)
Janus_emof_Property.attributes={Janus_emof_Property_isId, Janus_emof_Property_isDerived, Janus_emof_Property_default, Janus_emof_Property_isComposite, Janus_emof_Property_isReadOnly}

# Janus_emof_TypedElement class attributes and methods

# Janus_emof_PrimitiveType class attributes and methods

# Janus_emof_URIExtent class attributes and methods

# Extent class attributes and methods

# Janus_emof_Comment class attributes and methods

# Janus_JTL_Transformation class attributes and methods

# emof_Class class attributes and methods

# emof_Package class attributes and methods

# Model class attributes and methods

# Pattern class attributes and methods

# Relation class attributes and methods

# Janus_JTL_Relation class attributes and methods
Janus_JTL_Relation_isTopLevel: Property = Property(name="isTopLevel", type=BooleanType)
Janus_JTL_Relation.attributes={Janus_JTL_Relation_isTopLevel}

# Transformation class attributes and methods

# Domain class attributes and methods

# Variable class attributes and methods

# Janus_JTL_Domain class attributes and methods
Janus_JTL_Domain_isEnforceable: Property = Property(name="isEnforceable", type=BooleanType)
Janus_JTL_Domain_isCheckable: Property = Property(name="isCheckable", type=BooleanType)
Janus_JTL_Domain.attributes={Janus_JTL_Domain_isEnforceable, Janus_JTL_Domain_isCheckable}

# Janus_JTL_Model class attributes and methods

# Janus_JTL_Pattern class attributes and methods

# Janus_JTL_Predicate class attributes and methods

# Predicate class attributes and methods

# TemplateExp class attributes and methods

# Janus_essentialocl_CallExp class attributes and methods

# OclExpression class attributes and methods

# Janus_essentialocl_BooleanLiteralExp class attributes and methods
Janus_essentialocl_BooleanLiteralExp_booleanSymbol: Property = Property(name="booleanSymbol", type=BooleanType)
Janus_essentialocl_BooleanLiteralExp.attributes={Janus_essentialocl_BooleanLiteralExp_booleanSymbol}

# PrimitiveLiteralExp class attributes and methods

# TryExp class attributes and methods

# Janus_essentialocl_OclExpression class attributes and methods

# TypedElement class attributes and methods

# Janus_essentialocl_UnlimitedNaturalExp class attributes and methods
Janus_essentialocl_UnlimitedNaturalExp_symbol: Property = Property(name="symbol", type=StringType)
Janus_essentialocl_UnlimitedNaturalExp.attributes={Janus_essentialocl_UnlimitedNaturalExp_symbol}

# NumericLiteralExp class attributes and methods

# Janus_essentialocl_IfExp class attributes and methods

# Janus_essentialocl_Variable class attributes and methods

# Janus_essentialocl_LetExp class attributes and methods

# Janus_essentialocl_PropertyCallExp class attributes and methods

# FeaturePropertyCall class attributes and methods

# LetExp class attributes and methods

# ComputeExp class attributes and methods

# Janus_essentialocl_LoopExp class attributes and methods

# Janus_essentialocl_VariableExp class attributes and methods

# Janus_essentialocl_TypeExp class attributes and methods

# Janus_essentialocl_StringLiteralExp class attributes and methods
Janus_essentialocl_StringLiteralExp_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
Janus_essentialocl_StringLiteralExp.attributes={Janus_essentialocl_StringLiteralExp_stringSymbol}

# essentialocl_CallExp class attributes and methods

# essentialocl_OclExpression class attributes and methods

# Janus_essentialocl_IteratorExp class attributes and methods

# LoopExp class attributes and methods

# Janus_essentialocl_IntegerLiteralExp class attributes and methods
Janus_essentialocl_IntegerLiteralExp_integerSymbol: Property = Property(name="integerSymbol", type=IntegerType)
Janus_essentialocl_IntegerLiteralExp.attributes={Janus_essentialocl_IntegerLiteralExp_integerSymbol}

# Janus_essentialocl_OperationCallExp class attributes and methods

# Janus_essentialocl_RealLiteralExp class attributes and methods
Janus_essentialocl_RealLiteralExp_realSymbol: Property = Property(name="realSymbol", type=FloatType)
Janus_essentialocl_RealLiteralExp.attributes={Janus_essentialocl_RealLiteralExp_realSymbol}

# Janus_essentialocl_LiteralExp class attributes and methods

# Janus_essentialocl_IterateExp class attributes and methods

# CollectionLiteralExp class attributes and methods

# Janus_essentialocl_PrimitiveLiteralExp class attributes and methods

# LiteralExp class attributes and methods

# Janus_essentialocl_NumericLiteralExp class attributes and methods

# Janus_essentialocl_CollectionLiteralExp class attributes and methods
Janus_essentialocl_CollectionLiteralExp_kind: Property = Property(name="kind", type=StringType)
Janus_essentialocl_CollectionLiteralExp.attributes={Janus_essentialocl_CollectionLiteralExp_kind}

# CollectionLiteralPart class attributes and methods

# Janus_essentialocl_CollectionLiteralPart class attributes and methods

# Janus_essentialocl_CollectionItem class attributes and methods

# Janus_essentialocl_CollectionRange class attributes and methods

# Janus_essentialocl_NullLiteralExp class attributes and methods

# Janus_essentialocl_ExpressionInOcl class attributes and methods

# OpaqueExpression class attributes and methods

# Janus_essentialocl_TupleLiteralExp class attributes and methods

# TupleLiteralPart class attributes and methods

# TupleLiteralExp class attributes and methods

# Janus_essentialocl_BagType class attributes and methods

# Janus_essentialocl_OpaqueExpression class attributes and methods

# Janus_essentialocl_InvalidLiteralExp class attributes and methods

# Janus_essentialocl_FeaturePropertyCall class attributes and methods

# CallExp class attributes and methods

# Janus_essentialocl_TupleLiteralPart class attributes and methods

# Janus_essentialocl_SetType class attributes and methods

# Janus_essentialocl_TupleType class attributes and methods

# emof_DataType class attributes and methods

# Janus_essentialocl_VoidType class attributes and methods

# Janus_essentialocl_AnyType class attributes and methods

# emof_Type class attributes and methods

# Janus_template_TemplateExp class attributes and methods

# CollectionType class attributes and methods

# Janus_essentialocl_CollectionType class attributes and methods

# Janus_essentialocl_EnumLiteralExp class attributes and methods

# Janus_essentialocl_InvalidType class attributes and methods

# Janus_essentialocl_OrderedSetType class attributes and methods

# Janus_essentialocl_SequenceType class attributes and methods

# Janus_template_ObjectTemplateExp class attributes and methods
Janus_template_ObjectTemplateExp_referredClass: Property = Property(name="referredClass", type=StringType)
Janus_template_ObjectTemplateExp.attributes={Janus_template_ObjectTemplateExp_referredClass}

# PropertyTemplateItem class attributes and methods

# Janus_template_CollectionTemplateExp class attributes and methods
Janus_template_CollectionTemplateExp_kind: Property = Property(name="kind", type=StringType)
Janus_template_CollectionTemplateExp.attributes={Janus_template_CollectionTemplateExp_kind}

# Janus_imperativeocl_AssignExp class attributes and methods
Janus_imperativeocl_AssignExp_isReset: Property = Property(name="isReset", type=BooleanType)
Janus_imperativeocl_AssignExp.attributes={Janus_imperativeocl_AssignExp_isReset}

# ImperativeExpression class attributes and methods

# Janus_template_PropertyTemplateItem class attributes and methods

# ObjectTemplateExp class attributes and methods

# Janus_imperativeocl_ImperativeIterateExp class attributes and methods

# ImperativeLoopExp class attributes and methods

# Janus_imperativeocl_BlockExp class attributes and methods

# Janus_imperativeocl_VariableInitExp class attributes and methods
Janus_imperativeocl_VariableInitExp_withResult: Property = Property(name="withResult", type=BooleanType)
Janus_imperativeocl_VariableInitExp.attributes={Janus_imperativeocl_VariableInitExp_withResult}

# Janus_imperativeocl_SwitchExp class attributes and methods

# imperativeocl_ImperativeExpression class attributes and methods

# AltExp class attributes and methods

# Janus_imperativeocl_WhileExp class attributes and methods

# Janus_imperativeocl_AltExp class attributes and methods

# Janus_imperativeocl_ComputeExp class attributes and methods

# Janus_imperativeocl_UnlinkExp class attributes and methods

# Janus_imperativeocl_BreakExp class attributes and methods

# Janus_imperativeocl_TryExp class attributes and methods

# Janus_imperativeocl_ReturnExp class attributes and methods

# Janus_imperativeocl_RaiseExp class attributes and methods

# Janus_imperativeocl_ContinueExp class attributes and methods

# Janus_imperativeocl_ForExp class attributes and methods

# Janus_imperativeocl_TupleExp class attributes and methods

# Janus_imperativeocl_Typedef class attributes and methods

# Janus_imperativeocl_InstantiationExp class attributes and methods

# Janus_imperativeocl_DictionaryType class attributes and methods

# Janus_imperativeocl_DictLiteralExp class attributes and methods

# Janus_imperativeocl_LogExp class attributes and methods
Janus_imperativeocl_LogExp_text: Property = Property(name="text", type=StringType)
Janus_imperativeocl_LogExp_level: Property = Property(name="level", type=IntegerType)
Janus_imperativeocl_LogExp.attributes={Janus_imperativeocl_LogExp_text, Janus_imperativeocl_LogExp_level}

# DictLiteralPart class attributes and methods

# Janus_imperativeocl_DictLiteralPart class attributes and methods

# Janus_imperativeocl_TemplateParameterType class attributes and methods
Janus_imperativeocl_TemplateParameterType_specification: Property = Property(name="specification", type=StringType)
Janus_imperativeocl_TemplateParameterType.attributes={Janus_imperativeocl_TemplateParameterType_specification}

# Janus_imperativeocl_ImperativeLoopExp class attributes and methods

# essentialocl_LoopExp class attributes and methods

# Janus_imperativeocl_AssertExp class attributes and methods
Janus_imperativeocl_AssertExp_severity: Property = Property(name="severity", type=StringType)
Janus_imperativeocl_AssertExp.attributes={Janus_imperativeocl_AssertExp_severity}

# LogExp class attributes and methods

# Janus_imperativeocl_AnonymousTupleType class attributes and methods

# Janus_imperativeocl_AnonymousTupleLiteralExp class attributes and methods

# AnonymousTupleLiteralPart class attributes and methods

# Janus_imperativeocl_CollectorExp class attributes and methods

# Janus_imperativeocl_ImperativeExpression class attributes and methods

# Janus_imperativeocl_UnpackExp class attributes and methods

# Janus_imperativeocl_AnonymousTupleLiteralPart class attributes and methods

# Janus_imperativeocl_ListType class attributes and methods

# Relationships
ownedOperation1: BinaryAssociation = BinaryAssociation(
    name="ownedOperation1",
    ends={
        Property(name="emof2", type=Janus_emof_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Operation", type=Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAttribute0: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute0",
    ends={
        Property(name="emof", type=Janus_emof_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Property", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass3: BinaryAssociation = BinaryAssociation(
    name="superClass3",
    ends={
        Property(name="Class", type=Janus_emof_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_emof_Class", type=Class_, multiplicity=Multiplicity(0, 9999))
    }
)
tag4: BinaryAssociation = BinaryAssociation(
    name="tag4",
    ends={
        Property(name="emof5", type=Janus_emof_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="Tag", type=Tag, multiplicity=Multiplicity(0, 9999))
    }
)
ownedComment6: BinaryAssociation = BinaryAssociation(
    name="ownedComment6",
    ends={
        Property(name="Comment", type=Janus_emof_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_emof_Element", type=Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element7: BinaryAssociation = BinaryAssociation(
    name="element7",
    ends={
        Property(name="emof8", type=Janus_emof_Tag, multiplicity=Multiplicity(1, 1)),
        Property(name="Element", type=Element, multiplicity=Multiplicity(0, 9999))
    }
)
ownedLiteral9: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral9",
    ends={
        Property(name="emof10", type=Janus_emof_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="EnumerationLiteral", type=EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
class11: BinaryAssociation = BinaryAssociation(
    name="class11",
    ends={
        Property(name="emof13", type=Janus_emof_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="Class12", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
ownedParameter14: BinaryAssociation = BinaryAssociation(
    name="ownedParameter14",
    ends={
        Property(name="emof15", type=Janus_emof_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="Parameter", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
raisedException16: BinaryAssociation = BinaryAssociation(
    name="raisedException16",
    ends={
        Property(name="Type", type=Janus_emof_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_emof_Operation", type=Type, multiplicity=Multiplicity(0, 9999))
    }
)
enumeration27: BinaryAssociation = BinaryAssociation(
    name="enumeration27",
    ends={
        Property(name="emof28", type=Janus_emof_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="Enumeration", type=Enumeration_, multiplicity=Multiplicity(0, 1))
    }
)
ownedType17: BinaryAssociation = BinaryAssociation(
    name="ownedType17",
    ends={
        Property(name="emof19", type=Janus_emof_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="Type18", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedPackage20: BinaryAssociation = BinaryAssociation(
    name="nestedPackage20",
    ends={
        Property(name="Package", type=Janus_emof_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_emof_Package", type=Package, multiplicity=Multiplicity(0, 9999))
    }
)
package21: BinaryAssociation = BinaryAssociation(
    name="package21",
    ends={
        Property(name="emof23", type=Janus_emof_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="Package22", type=Package, multiplicity=Multiplicity(1, 1))
    }
)
operation24: BinaryAssociation = BinaryAssociation(
    name="operation24",
    ends={
        Property(name="emof26", type=Janus_emof_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="Operation25", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
Class29: BinaryAssociation = BinaryAssociation(
    name="Class29",
    ends={
        Property(name="emof31", type=Janus_emof_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="Class30", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
opposite32: BinaryAssociation = BinaryAssociation(
    name="opposite32",
    ends={
        Property(name="Property33", type=Janus_emof_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_emof_Property", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
type34: BinaryAssociation = BinaryAssociation(
    name="type34",
    ends={
        Property(name="Type35", type=Janus_emof_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_emof_TypedElement", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
modelParameter37: BinaryAssociation = BinaryAssociation(
    name="modelParameter37",
    ends={
        Property(name="JTL", type=Janus_JTL_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="Model", type=Model, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotatedElement36: BinaryAssociation = BinaryAssociation(
    name="annotatedElement36",
    ends={
        Property(name="NamedElement", type=Janus_emof_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_emof_Comment", type=NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
where44: BinaryAssociation = BinaryAssociation(
    name="where44",
    ends={
        Property(name="JTL45", type=Janus_JTL_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="Pattern", type=Pattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
relation38: BinaryAssociation = BinaryAssociation(
    name="relation38",
    ends={
        Property(name="JTL39", type=Janus_JTL_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="Relation", type=Relation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transformation40: BinaryAssociation = BinaryAssociation(
    name="transformation40",
    ends={
        Property(name="JTL41", type=Janus_JTL_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="Transformation", type=Transformation, multiplicity=Multiplicity(1, 1))
    }
)
domain42: BinaryAssociation = BinaryAssociation(
    name="domain42",
    ends={
        Property(name="JTL43", type=Janus_JTL_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="Domain", type=Domain, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relation50: BinaryAssociation = BinaryAssociation(
    name="relation50",
    ends={
        Property(name="JTL52", type=Janus_JTL_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="Relation51", type=Relation, multiplicity=Multiplicity(1, 1))
    }
)
when46: BinaryAssociation = BinaryAssociation(
    name="when46",
    ends={
        Property(name="JTL48", type=Janus_JTL_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="Pattern47", type=Pattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable49: BinaryAssociation = BinaryAssociation(
    name="variable49",
    ends={
        Property(name="Variable", type=Janus_JTL_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_JTL_Relation", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transformation61: BinaryAssociation = BinaryAssociation(
    name="transformation61",
    ends={
        Property(name="JTL63", type=Janus_JTL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="Transformation62", type=Transformation, multiplicity=Multiplicity(1, 1))
    }
)
pattern53: BinaryAssociation = BinaryAssociation(
    name="pattern53",
    ends={
        Property(name="Pattern54", type=Janus_JTL_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_JTL_Domain", type=Pattern, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
model55: BinaryAssociation = BinaryAssociation(
    name="model55",
    ends={
        Property(name="Model57", type=Janus_JTL_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_JTL_Domain56", type=Model, multiplicity=Multiplicity(1, 1))
    }
)
rootVariable58: BinaryAssociation = BinaryAssociation(
    name="rootVariable58",
    ends={
        Property(name="Variable60", type=Janus_JTL_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_JTL_Domain59", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
whenOwner72: BinaryAssociation = BinaryAssociation(
    name="whenOwner72",
    ends={
        Property(name="JTL74", type=Janus_JTL_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="Relation73", type=Relation, multiplicity=Multiplicity(0, 1))
    }
)
usedPackage64: BinaryAssociation = BinaryAssociation(
    name="usedPackage64",
    ends={
        Property(name="Package65", type=Janus_JTL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_JTL_Model", type=Package, multiplicity=Multiplicity(0, 9999))
    }
)
dependsOn66: BinaryAssociation = BinaryAssociation(
    name="dependsOn66",
    ends={
        Property(name="Model68", type=Janus_JTL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_JTL_Model67", type=Model, multiplicity=Multiplicity(0, 9999))
    }
)
whereOwner69: BinaryAssociation = BinaryAssociation(
    name="whereOwner69",
    ends={
        Property(name="JTL71", type=Janus_JTL_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="Relation70", type=Relation, multiplicity=Multiplicity(0, 1))
    }
)
domain81: BinaryAssociation = BinaryAssociation(
    name="domain81",
    ends={
        Property(name="Janus_JTL_Pattern82", type=Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="Domain83", type=Janus_JTL_Pattern, multiplicity=Multiplicity(1, 1))
    }
)
predicate75: BinaryAssociation = BinaryAssociation(
    name="predicate75",
    ends={
        Property(name="JTL76", type=Janus_JTL_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="Predicate", type=Predicate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bindsTo77: BinaryAssociation = BinaryAssociation(
    name="bindsTo77",
    ends={
        Property(name="Variable78", type=Janus_JTL_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_JTL_Pattern", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
templateExpression79: BinaryAssociation = BinaryAssociation(
    name="templateExpression79",
    ends={
        Property(name="TemplateExp", type=Janus_JTL_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_JTL_Pattern80", type=TemplateExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pattern84: BinaryAssociation = BinaryAssociation(
    name="pattern84",
    ends={
        Property(name="JTL86", type=Janus_JTL_Predicate, multiplicity=Multiplicity(1, 1)),
        Property(name="Pattern85", type=Pattern, multiplicity=Multiplicity(1, 1))
    }
)
conditionExpression87: BinaryAssociation = BinaryAssociation(
    name="conditionExpression87",
    ends={
        Property(name="OclExpression", type=Janus_JTL_Predicate, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_JTL_Predicate", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tryBodyOwner90: BinaryAssociation = BinaryAssociation(
    name="tryBodyOwner90",
    ends={
        Property(name="imperativeocl", type=Janus_essentialocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="TryExp", type=TryExp, multiplicity=Multiplicity(0, 1))
    }
)
source88: BinaryAssociation = BinaryAssociation(
    name="source88",
    ends={
        Property(name="OclExpression89", type=Janus_essentialocl_CallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_CallExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition91: BinaryAssociation = BinaryAssociation(
    name="condition91",
    ends={
        Property(name="OclExpression92", type=Janus_essentialocl_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_IfExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression93: BinaryAssociation = BinaryAssociation(
    name="thenExpression93",
    ends={
        Property(name="OclExpression95", type=Janus_essentialocl_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_IfExp94", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression96: BinaryAssociation = BinaryAssociation(
    name="elseExpression96",
    ends={
        Property(name="OclExpression98", type=Janus_essentialocl_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_IfExp97", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
in99: BinaryAssociation = BinaryAssociation(
    name="in99",
    ends={
        Property(name="OclExpression100", type=Janus_essentialocl_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_LetExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable101: BinaryAssociation = BinaryAssociation(
    name="variable101",
    ends={
        Property(name="essentialocl", type=Janus_essentialocl_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Variable102", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initExpression103: BinaryAssociation = BinaryAssociation(
    name="initExpression103",
    ends={
        Property(name="OclExpression104", type=Janus_essentialocl_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_Variable", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
LetExp105: BinaryAssociation = BinaryAssociation(
    name="LetExp105",
    ends={
        Property(name="essentialocl106", type=Janus_essentialocl_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="LetExp", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
bindParameter107: BinaryAssociation = BinaryAssociation(
    name="bindParameter107",
    ends={
        Property(name="Parameter109", type=Janus_essentialocl_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_Variable108", type=Parameter_, multiplicity=Multiplicity(0, 1))
    }
)
computeOwner110: BinaryAssociation = BinaryAssociation(
    name="computeOwner110",
    ends={
        Property(name="imperativeocl111", type=Janus_essentialocl_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="ComputeExp", type=ComputeExp, multiplicity=Multiplicity(0, 1))
    }
)
referredProperty112: BinaryAssociation = BinaryAssociation(
    name="referredProperty112",
    ends={
        Property(name="Property113", type=Janus_essentialocl_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_PropertyCallExp", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
referredVariable114: BinaryAssociation = BinaryAssociation(
    name="referredVariable114",
    ends={
        Property(name="Variable115", type=Janus_essentialocl_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_VariableExp", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
referredType116: BinaryAssociation = BinaryAssociation(
    name="referredType116",
    ends={
        Property(name="Type117", type=Janus_essentialocl_TypeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_TypeExp", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
body118: BinaryAssociation = BinaryAssociation(
    name="body118",
    ends={
        Property(name="OclExpression119", type=Janus_essentialocl_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_LoopExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterator120: BinaryAssociation = BinaryAssociation(
    name="iterator120",
    ends={
        Property(name="Variable122", type=Janus_essentialocl_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_LoopExp121", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredOperation125: BinaryAssociation = BinaryAssociation(
    name="referredOperation125",
    ends={
        Property(name="Relation127", type=Janus_essentialocl_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_OperationCallExp126", type=Relation, multiplicity=Multiplicity(0, 1))
    }
)
argument123: BinaryAssociation = BinaryAssociation(
    name="argument123",
    ends={
        Property(name="OclExpression124", type=Janus_essentialocl_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_OperationCallExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
result128: BinaryAssociation = BinaryAssociation(
    name="result128",
    ends={
        Property(name="Variable129", type=Janus_essentialocl_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_IterateExp", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
CollectionLiteralExp132: BinaryAssociation = BinaryAssociation(
    name="CollectionLiteralExp132",
    ends={
        Property(name="essentialocl133", type=Janus_essentialocl_CollectionLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="CollectionLiteralExp", type=CollectionLiteralExp, multiplicity=Multiplicity(1, 1))
    }
)
part130: BinaryAssociation = BinaryAssociation(
    name="part130",
    ends={
        Property(name="essentialocl131", type=Janus_essentialocl_CollectionLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="CollectionLiteralPart", type=CollectionLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
last138: BinaryAssociation = BinaryAssociation(
    name="last138",
    ends={
        Property(name="OclExpression140", type=Janus_essentialocl_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_CollectionRange139", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
item134: BinaryAssociation = BinaryAssociation(
    name="item134",
    ends={
        Property(name="OclExpression135", type=Janus_essentialocl_CollectionItem, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_CollectionItem", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
first136: BinaryAssociation = BinaryAssociation(
    name="first136",
    ends={
        Property(name="OclExpression137", type=Janus_essentialocl_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_CollectionRange", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
part141: BinaryAssociation = BinaryAssociation(
    name="part141",
    ends={
        Property(name="essentialocl142", type=Janus_essentialocl_TupleLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="TupleLiteralPart", type=TupleLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resultVariable148: BinaryAssociation = BinaryAssociation(
    name="resultVariable148",
    ends={
        Property(name="Variable150", type=Janus_essentialocl_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_ExpressionInOcl149", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterVariable151: BinaryAssociation = BinaryAssociation(
    name="parameterVariable151",
    ends={
        Property(name="Variable153", type=Janus_essentialocl_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_ExpressionInOcl152", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bodyExpression143: BinaryAssociation = BinaryAssociation(
    name="bodyExpression143",
    ends={
        Property(name="OclExpression144", type=Janus_essentialocl_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_ExpressionInOcl", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context145: BinaryAssociation = BinaryAssociation(
    name="context145",
    ends={
        Property(name="Variable147", type=Janus_essentialocl_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_ExpressionInOcl146", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TupleLiteralExp154: BinaryAssociation = BinaryAssociation(
    name="TupleLiteralExp154",
    ends={
        Property(name="essentialocl155", type=Janus_essentialocl_TupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="TupleLiteralExp", type=TupleLiteralExp, multiplicity=Multiplicity(0, 1))
    }
)
attribute156: BinaryAssociation = BinaryAssociation(
    name="attribute156",
    ends={
        Property(name="Property157", type=Janus_essentialocl_TupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_TupleLiteralPart", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
elementType158: BinaryAssociation = BinaryAssociation(
    name="elementType158",
    ends={
        Property(name="Type159", type=Janus_essentialocl_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_CollectionType", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
referredEnumLiteral160: BinaryAssociation = BinaryAssociation(
    name="referredEnumLiteral160",
    ends={
        Property(name="EnumerationLiteral161", type=Janus_essentialocl_EnumLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_EnumLiteralExp", type=EnumerationLiteral, multiplicity=Multiplicity(0, 1))
    }
)
part168: BinaryAssociation = BinaryAssociation(
    name="part168",
    ends={
        Property(name="OclExpression169", type=Janus_template_CollectionTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_template_CollectionTemplateExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredCollectionType170: BinaryAssociation = BinaryAssociation(
    name="referredCollectionType170",
    ends={
        Property(name="CollectionType", type=Janus_template_CollectionTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_template_CollectionTemplateExp171", type=CollectionType, multiplicity=Multiplicity(0, 1))
    }
)
match172: BinaryAssociation = BinaryAssociation(
    name="match172",
    ends={
        Property(name="OclExpression174", type=Janus_template_CollectionTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_template_CollectionTemplateExp173", type=OclExpression, multiplicity=Multiplicity(0, 1))
    }
)
bindsTo162: BinaryAssociation = BinaryAssociation(
    name="bindsTo162",
    ends={
        Property(name="Variable163", type=Janus_template_TemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_template_TemplateExp", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
where164: BinaryAssociation = BinaryAssociation(
    name="where164",
    ends={
        Property(name="OclExpression166", type=Janus_template_TemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_template_TemplateExp165", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
part167: BinaryAssociation = BinaryAssociation(
    name="part167",
    ends={
        Property(name="template", type=Janus_template_ObjectTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="PropertyTemplateItem", type=PropertyTemplateItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target182: BinaryAssociation = BinaryAssociation(
    name="target182",
    ends={
        Property(name="Variable183", type=Janus_imperativeocl_ImperativeIterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_ImperativeIterateExp", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value184: BinaryAssociation = BinaryAssociation(
    name="value184",
    ends={
        Property(name="OclExpression185", type=Janus_imperativeocl_AssignExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_AssignExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
objContainer175: BinaryAssociation = BinaryAssociation(
    name="objContainer175",
    ends={
        Property(name="template176", type=Janus_template_PropertyTemplateItem, multiplicity=Multiplicity(1, 1)),
        Property(name="ObjectTemplateExp", type=ObjectTemplateExp, multiplicity=Multiplicity(1, 1))
    }
)
value177: BinaryAssociation = BinaryAssociation(
    name="value177",
    ends={
        Property(name="OclExpression178", type=Janus_template_PropertyTemplateItem, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_template_PropertyTemplateItem", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referredProperty179: BinaryAssociation = BinaryAssociation(
    name="referredProperty179",
    ends={
        Property(name="Property181", type=Janus_template_PropertyTemplateItem, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_template_PropertyTemplateItem180", type=Property_, multiplicity=Multiplicity(1, 1))
    }
)
left186: BinaryAssociation = BinaryAssociation(
    name="left186",
    ends={
        Property(name="OclExpression188", type=Janus_imperativeocl_AssignExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_AssignExp187", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
defaultValue189: BinaryAssociation = BinaryAssociation(
    name="defaultValue189",
    ends={
        Property(name="OclExpression191", type=Janus_imperativeocl_AssignExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_AssignExp190", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elsePart195: BinaryAssociation = BinaryAssociation(
    name="elsePart195",
    ends={
        Property(name="OclExpression197", type=Janus_imperativeocl_SwitchExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_SwitchExp196", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body192: BinaryAssociation = BinaryAssociation(
    name="body192",
    ends={
        Property(name="OclExpression193", type=Janus_imperativeocl_BlockExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_BlockExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
alternativePart194: BinaryAssociation = BinaryAssociation(
    name="alternativePart194",
    ends={
        Property(name="AltExp", type=Janus_imperativeocl_SwitchExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_SwitchExp", type=AltExp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition200: BinaryAssociation = BinaryAssociation(
    name="condition200",
    ends={
        Property(name="OclExpression201", type=Janus_imperativeocl_WhileExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_WhileExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body202: BinaryAssociation = BinaryAssociation(
    name="body202",
    ends={
        Property(name="OclExpression204", type=Janus_imperativeocl_WhileExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_WhileExp203", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referredVariable198: BinaryAssociation = BinaryAssociation(
    name="referredVariable198",
    ends={
        Property(name="Variable199", type=Janus_imperativeocl_VariableInitExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_VariableInitExp", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body208: BinaryAssociation = BinaryAssociation(
    name="body208",
    ends={
        Property(name="OclExpression209", type=Janus_imperativeocl_ComputeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_ComputeExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnedElement205: BinaryAssociation = BinaryAssociation(
    name="returnedElement205",
    ends={
        Property(name="essentialocl207", type=Janus_imperativeocl_ComputeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Variable206", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target215: BinaryAssociation = BinaryAssociation(
    name="target215",
    ends={
        Property(name="OclExpression216", type=Janus_imperativeocl_UnlinkExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_UnlinkExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition210: BinaryAssociation = BinaryAssociation(
    name="condition210",
    ends={
        Property(name="OclExpression211", type=Janus_imperativeocl_AltExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_AltExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body212: BinaryAssociation = BinaryAssociation(
    name="body212",
    ends={
        Property(name="OclExpression214", type=Janus_imperativeocl_AltExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_AltExp213", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value220: BinaryAssociation = BinaryAssociation(
    name="value220",
    ends={
        Property(name="OclExpression221", type=Janus_imperativeocl_ReturnExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_ReturnExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tryBody222: BinaryAssociation = BinaryAssociation(
    name="tryBody222",
    ends={
        Property(name="essentialocl224", type=Janus_imperativeocl_TryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression223", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exception225: BinaryAssociation = BinaryAssociation(
    name="exception225",
    ends={
        Property(name="Type226", type=Janus_imperativeocl_TryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_TryExp", type=Type, multiplicity=Multiplicity(0, 9999))
    }
)
exceptBody227: BinaryAssociation = BinaryAssociation(
    name="exceptBody227",
    ends={
        Property(name="OclExpression229", type=Janus_imperativeocl_TryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_TryExp228", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
item217: BinaryAssociation = BinaryAssociation(
    name="item217",
    ends={
        Property(name="OclExpression219", type=Janus_imperativeocl_UnlinkExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_UnlinkExp218", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
instantiatedClass239: BinaryAssociation = BinaryAssociation(
    name="instantiatedClass239",
    ends={
        Property(name="Class240", type=Janus_imperativeocl_InstantiationExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_InstantiationExp", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
exception230: BinaryAssociation = BinaryAssociation(
    name="exception230",
    ends={
        Property(name="Type231", type=Janus_imperativeocl_RaiseExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_RaiseExp", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
element232: BinaryAssociation = BinaryAssociation(
    name="element232",
    ends={
        Property(name="OclExpression233", type=Janus_imperativeocl_TupleExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_TupleExp", type=OclExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
base234: BinaryAssociation = BinaryAssociation(
    name="base234",
    ends={
        Property(name="Type235", type=Janus_imperativeocl_Typedef, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_Typedef", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
condition236: BinaryAssociation = BinaryAssociation(
    name="condition236",
    ends={
        Property(name="OclExpression238", type=Janus_imperativeocl_Typedef, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_Typedef237", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
keyType247: BinaryAssociation = BinaryAssociation(
    name="keyType247",
    ends={
        Property(name="Type248", type=Janus_imperativeocl_DictionaryType, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_DictionaryType", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
extent241: BinaryAssociation = BinaryAssociation(
    name="extent241",
    ends={
        Property(name="Variable243", type=Janus_imperativeocl_InstantiationExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_InstantiationExp242", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
argument244: BinaryAssociation = BinaryAssociation(
    name="argument244",
    ends={
        Property(name="OclExpression246", type=Janus_imperativeocl_InstantiationExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_InstantiationExp245", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition255: BinaryAssociation = BinaryAssociation(
    name="condition255",
    ends={
        Property(name="OclExpression256", type=Janus_imperativeocl_LogExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_LogExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
part249: BinaryAssociation = BinaryAssociation(
    name="part249",
    ends={
        Property(name="DictLiteralPart", type=Janus_imperativeocl_DictLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_DictLiteralExp", type=DictLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key250: BinaryAssociation = BinaryAssociation(
    name="key250",
    ends={
        Property(name="OclExpression251", type=Janus_imperativeocl_DictLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_DictLiteralPart", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value252: BinaryAssociation = BinaryAssociation(
    name="value252",
    ends={
        Property(name="OclExpression254", type=Janus_imperativeocl_DictLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_DictLiteralPart253", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition264: BinaryAssociation = BinaryAssociation(
    name="condition264",
    ends={
        Property(name="OclExpression265", type=Janus_imperativeocl_ImperativeLoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_ImperativeLoopExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
element257: BinaryAssociation = BinaryAssociation(
    name="element257",
    ends={
        Property(name="Element259", type=Janus_imperativeocl_LogExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_LogExp258", type=Element, multiplicity=Multiplicity(0, 1))
    }
)
log260: BinaryAssociation = BinaryAssociation(
    name="log260",
    ends={
        Property(name="LogExp", type=Janus_imperativeocl_AssertExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_AssertExp", type=LogExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assertion261: BinaryAssociation = BinaryAssociation(
    name="assertion261",
    ends={
        Property(name="OclExpression263", type=Janus_imperativeocl_AssertExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_AssertExp262", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elementType270: BinaryAssociation = BinaryAssociation(
    name="elementType270",
    ends={
        Property(name="Type271", type=Janus_imperativeocl_AnonymousTupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_AnonymousTupleType", type=Type, multiplicity=Multiplicity(0, 9999))
    }
)
target266: BinaryAssociation = BinaryAssociation(
    name="target266",
    ends={
        Property(name="Variable267", type=Janus_imperativeocl_CollectorExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_CollectorExp", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable268: BinaryAssociation = BinaryAssociation(
    name="variable268",
    ends={
        Property(name="Variable269", type=Janus_imperativeocl_UnpackExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_UnpackExp", type=Variable, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
part272: BinaryAssociation = BinaryAssociation(
    name="part272",
    ends={
        Property(name="AnonymousTupleLiteralPart", type=Janus_imperativeocl_AnonymousTupleLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_AnonymousTupleLiteralExp", type=AnonymousTupleLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value273: BinaryAssociation = BinaryAssociation(
    name="value273",
    ends={
        Property(name="OclExpression274", type=Janus_imperativeocl_AnonymousTupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_AnonymousTupleLiteralPart", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_Janus_emof_Class_Type = Generalization(general=Type, specific=Janus_emof_Class)
gen_Janus_emof_Enumeration_DataType = Generalization(general=DataType, specific=Janus_emof_Enumeration)
gen_Janus_emof_DataType_Type = Generalization(general=Type, specific=Janus_emof_DataType)
gen_Janus_emof_Element_Object = Generalization(general=Object, specific=Janus_emof_Element)
gen_Janus_emof_Tag_Element = Generalization(general=Element, specific=Janus_emof_Tag)
gen_Janus_emof_NamedElement_Element = Generalization(general=Element, specific=Janus_emof_NamedElement)
gen_Janus_emof_Extent_Object = Generalization(general=Object, specific=Janus_emof_Extent)
gen_Janus_emof_Operation_emof_MultiplicityElement = Generalization(general=emof_MultiplicityElement, specific=Janus_emof_Operation)
gen_Janus_emof_Operation_emof_TypedElement = Generalization(general=emof_TypedElement, specific=Janus_emof_Operation)
gen_Janus_emof_EnumerationLiteral_NamedElement = Generalization(general=NamedElement, specific=Janus_emof_EnumerationLiteral)
gen_Janus_emof_Package_NamedElement = Generalization(general=NamedElement, specific=Janus_emof_Package)
gen_Janus_emof_Type_NamedElement = Generalization(general=NamedElement, specific=Janus_emof_Type)
gen_Janus_emof_Parameter_emof_MultiplicityElement = Generalization(general=emof_MultiplicityElement, specific=Janus_emof_Parameter)
gen_Janus_emof_Parameter_emof_TypedElement = Generalization(general=emof_TypedElement, specific=Janus_emof_Parameter)
gen_Janus_emof_URIExtent_Extent = Generalization(general=Extent, specific=Janus_emof_URIExtent)
gen_Janus_emof_Property_emof_MultiplicityElement = Generalization(general=emof_MultiplicityElement, specific=Janus_emof_Property)
gen_Janus_emof_Property_emof_TypedElement = Generalization(general=emof_TypedElement, specific=Janus_emof_Property)
gen_Janus_emof_TypedElement_NamedElement = Generalization(general=NamedElement, specific=Janus_emof_TypedElement)
gen_Janus_emof_PrimitiveType_DataType = Generalization(general=DataType, specific=Janus_emof_PrimitiveType)
gen_Janus_emof_Comment_Element = Generalization(general=Element, specific=Janus_emof_Comment)
gen_Janus_JTL_Transformation_emof_Class = Generalization(general=emof_Class, specific=Janus_JTL_Transformation)
gen_Janus_JTL_Transformation_emof_Package = Generalization(general=emof_Package, specific=Janus_JTL_Transformation)
gen_Janus_JTL_Relation_NamedElement = Generalization(general=NamedElement, specific=Janus_JTL_Relation)
gen_Janus_JTL_Domain_NamedElement = Generalization(general=NamedElement, specific=Janus_JTL_Domain)
gen_Janus_JTL_Model_NamedElement = Generalization(general=NamedElement, specific=Janus_JTL_Model)
gen_Janus_JTL_Pattern_Element = Generalization(general=Element, specific=Janus_JTL_Pattern)
gen_Janus_JTL_Predicate_Element = Generalization(general=Element, specific=Janus_JTL_Predicate)
gen_Janus_essentialocl_CallExp_OclExpression = Generalization(general=OclExpression, specific=Janus_essentialocl_CallExp)
gen_Janus_essentialocl_BooleanLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=Janus_essentialocl_BooleanLiteralExp)
gen_Janus_essentialocl_OclExpression_TypedElement = Generalization(general=TypedElement, specific=Janus_essentialocl_OclExpression)
gen_Janus_essentialocl_UnlimitedNaturalExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=Janus_essentialocl_UnlimitedNaturalExp)
gen_Janus_essentialocl_IfExp_OclExpression = Generalization(general=OclExpression, specific=Janus_essentialocl_IfExp)
gen_Janus_essentialocl_Variable_TypedElement = Generalization(general=TypedElement, specific=Janus_essentialocl_Variable)
gen_Janus_essentialocl_LetExp_OclExpression = Generalization(general=OclExpression, specific=Janus_essentialocl_LetExp)
gen_Janus_essentialocl_PropertyCallExp_FeaturePropertyCall = Generalization(general=FeaturePropertyCall, specific=Janus_essentialocl_PropertyCallExp)
gen_Janus_essentialocl_VariableExp_OclExpression = Generalization(general=OclExpression, specific=Janus_essentialocl_VariableExp)
gen_Janus_essentialocl_TypeExp_OclExpression = Generalization(general=OclExpression, specific=Janus_essentialocl_TypeExp)
gen_Janus_essentialocl_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=Janus_essentialocl_IteratorExp)
gen_Janus_essentialocl_StringLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=Janus_essentialocl_StringLiteralExp)
gen_Janus_essentialocl_LoopExp_essentialocl_CallExp = Generalization(general=essentialocl_CallExp, specific=Janus_essentialocl_LoopExp)
gen_Janus_essentialocl_LoopExp_essentialocl_OclExpression = Generalization(general=essentialocl_OclExpression, specific=Janus_essentialocl_LoopExp)
gen_Janus_essentialocl_IntegerLiteralExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=Janus_essentialocl_IntegerLiteralExp)
gen_Janus_essentialocl_OperationCallExp_FeaturePropertyCall = Generalization(general=FeaturePropertyCall, specific=Janus_essentialocl_OperationCallExp)
gen_Janus_essentialocl_RealLiteralExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=Janus_essentialocl_RealLiteralExp)
gen_Janus_essentialocl_LiteralExp_OclExpression = Generalization(general=OclExpression, specific=Janus_essentialocl_LiteralExp)
gen_Janus_essentialocl_IterateExp_LoopExp = Generalization(general=LoopExp, specific=Janus_essentialocl_IterateExp)
gen_Janus_essentialocl_PrimitiveLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=Janus_essentialocl_PrimitiveLiteralExp)
gen_Janus_essentialocl_NumericLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=Janus_essentialocl_NumericLiteralExp)
gen_Janus_essentialocl_CollectionLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=Janus_essentialocl_CollectionLiteralExp)
gen_Janus_essentialocl_CollectionLiteralPart_TypedElement = Generalization(general=TypedElement, specific=Janus_essentialocl_CollectionLiteralPart)
gen_Janus_essentialocl_CollectionItem_CollectionLiteralPart = Generalization(general=CollectionLiteralPart, specific=Janus_essentialocl_CollectionItem)
gen_Janus_essentialocl_CollectionRange_CollectionLiteralPart = Generalization(general=CollectionLiteralPart, specific=Janus_essentialocl_CollectionRange)
gen_Janus_essentialocl_NullLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=Janus_essentialocl_NullLiteralExp)
gen_Janus_essentialocl_ExpressionInOcl_OpaqueExpression = Generalization(general=OpaqueExpression, specific=Janus_essentialocl_ExpressionInOcl)
gen_Janus_essentialocl_TupleLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=Janus_essentialocl_TupleLiteralExp)
gen_Janus_essentialocl_InvalidLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=Janus_essentialocl_InvalidLiteralExp)
gen_Janus_essentialocl_FeaturePropertyCall_CallExp = Generalization(general=CallExp, specific=Janus_essentialocl_FeaturePropertyCall)
gen_Janus_essentialocl_TupleLiteralPart_TypedElement = Generalization(general=TypedElement, specific=Janus_essentialocl_TupleLiteralPart)
gen_Janus_essentialocl_SetType_CollectionType = Generalization(general=CollectionType, specific=Janus_essentialocl_SetType)
gen_Janus_essentialocl_TupleType_emof_Class = Generalization(general=emof_Class, specific=Janus_essentialocl_TupleType)
gen_Janus_essentialocl_TupleType_emof_DataType = Generalization(general=emof_DataType, specific=Janus_essentialocl_TupleType)
gen_Janus_essentialocl_VoidType_Type = Generalization(general=Type, specific=Janus_essentialocl_VoidType)
gen_Janus_essentialocl_AnyType_emof_Class = Generalization(general=emof_Class, specific=Janus_essentialocl_AnyType)
gen_Janus_essentialocl_AnyType_emof_Type = Generalization(general=emof_Type, specific=Janus_essentialocl_AnyType)
gen_Janus_template_TemplateExp_LiteralExp = Generalization(general=LiteralExp, specific=Janus_template_TemplateExp)
gen_Janus_essentialocl_BagType_CollectionType = Generalization(general=CollectionType, specific=Janus_essentialocl_BagType)
gen_Janus_essentialocl_CollectionType_DataType = Generalization(general=DataType, specific=Janus_essentialocl_CollectionType)
gen_Janus_essentialocl_EnumLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=Janus_essentialocl_EnumLiteralExp)
gen_Janus_essentialocl_InvalidType_Type = Generalization(general=Type, specific=Janus_essentialocl_InvalidType)
gen_Janus_essentialocl_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=Janus_essentialocl_OrderedSetType)
gen_Janus_essentialocl_SequenceType_CollectionType = Generalization(general=CollectionType, specific=Janus_essentialocl_SequenceType)
gen_Janus_template_ObjectTemplateExp_TemplateExp = Generalization(general=TemplateExp, specific=Janus_template_ObjectTemplateExp)
gen_Janus_template_CollectionTemplateExp_TemplateExp = Generalization(general=TemplateExp, specific=Janus_template_CollectionTemplateExp)
gen_Janus_imperativeocl_AssignExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=Janus_imperativeocl_AssignExp)
gen_Janus_template_PropertyTemplateItem_Element = Generalization(general=Element, specific=Janus_template_PropertyTemplateItem)
gen_Janus_imperativeocl_ImperativeIterateExp_ImperativeLoopExp = Generalization(general=ImperativeLoopExp, specific=Janus_imperativeocl_ImperativeIterateExp)
gen_Janus_imperativeocl_BlockExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=Janus_imperativeocl_BlockExp)
gen_Janus_imperativeocl_SwitchExp_essentialocl_CallExp = Generalization(general=essentialocl_CallExp, specific=Janus_imperativeocl_SwitchExp)
gen_Janus_imperativeocl_SwitchExp_imperativeocl_ImperativeExpression = Generalization(general=imperativeocl_ImperativeExpression, specific=Janus_imperativeocl_SwitchExp)
gen_Janus_imperativeocl_VariableInitExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=Janus_imperativeocl_VariableInitExp)
gen_Janus_imperativeocl_WhileExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=Janus_imperativeocl_WhileExp)
gen_Janus_imperativeocl_AltExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=Janus_imperativeocl_AltExp)
gen_Janus_imperativeocl_ComputeExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=Janus_imperativeocl_ComputeExp)
gen_Janus_imperativeocl_UnlinkExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=Janus_imperativeocl_UnlinkExp)
gen_Janus_imperativeocl_BreakExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=Janus_imperativeocl_BreakExp)
gen_Janus_imperativeocl_TryExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=Janus_imperativeocl_TryExp)
gen_Janus_imperativeocl_ReturnExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=Janus_imperativeocl_ReturnExp)
gen_Janus_imperativeocl_InstantiationExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=Janus_imperativeocl_InstantiationExp)
gen_Janus_imperativeocl_RaiseExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=Janus_imperativeocl_RaiseExp)
gen_Janus_imperativeocl_ContinueExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=Janus_imperativeocl_ContinueExp)
gen_Janus_imperativeocl_ForExp_ImperativeLoopExp = Generalization(general=ImperativeLoopExp, specific=Janus_imperativeocl_ForExp)
gen_Janus_imperativeocl_TupleExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=Janus_imperativeocl_TupleExp)
gen_Janus_imperativeocl_Typedef_Class = Generalization(general=Class_, specific=Janus_imperativeocl_Typedef)
gen_Janus_imperativeocl_DictionaryType_CollectionType = Generalization(general=CollectionType, specific=Janus_imperativeocl_DictionaryType)
gen_Janus_imperativeocl_DictLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=Janus_imperativeocl_DictLiteralExp)
gen_Janus_imperativeocl_LogExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=Janus_imperativeocl_LogExp)
gen_Janus_imperativeocl_DictLiteralPart_Element = Generalization(general=Element, specific=Janus_imperativeocl_DictLiteralPart)
gen_Janus_imperativeocl_TemplateParameterType_Type = Generalization(general=Type, specific=Janus_imperativeocl_TemplateParameterType)
gen_Janus_imperativeocl_ImperativeLoopExp_essentialocl_LoopExp = Generalization(general=essentialocl_LoopExp, specific=Janus_imperativeocl_ImperativeLoopExp)
gen_Janus_imperativeocl_ImperativeLoopExp_imperativeocl_ImperativeExpression = Generalization(general=imperativeocl_ImperativeExpression, specific=Janus_imperativeocl_ImperativeLoopExp)
gen_Janus_imperativeocl_AssertExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=Janus_imperativeocl_AssertExp)
gen_Janus_imperativeocl_AnonymousTupleType_Class = Generalization(general=Class_, specific=Janus_imperativeocl_AnonymousTupleType)
gen_Janus_imperativeocl_AnonymousTupleLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=Janus_imperativeocl_AnonymousTupleLiteralExp)
gen_Janus_imperativeocl_CollectorExp_ImperativeLoopExp = Generalization(general=ImperativeLoopExp, specific=Janus_imperativeocl_CollectorExp)
gen_Janus_imperativeocl_ImperativeExpression_OclExpression = Generalization(general=OclExpression, specific=Janus_imperativeocl_ImperativeExpression)
gen_Janus_imperativeocl_UnpackExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=Janus_imperativeocl_UnpackExp)
gen_Janus_imperativeocl_AnonymousTupleLiteralPart_Element = Generalization(general=Element, specific=Janus_imperativeocl_AnonymousTupleLiteralPart)
gen_Janus_imperativeocl_ListType_CollectionType = Generalization(general=CollectionType, specific=Janus_imperativeocl_ListType)

# Domain Model
domain_model = DomainModel(
    name="Janus",
    types={Operation, Janus_emof_Class, Type, Property_, Janus_emof_Enumeration, DataType, Class_, Janus_emof_DataType, Janus_emof_Element, Object, Tag, Comment, Janus_emof_Tag, Element, Janus_emof_MultiplicityElement, EnumerationLiteral, Janus_emof_NamedElement, Janus_emof_Extent, Janus_emof_Object, Janus_emof_Operation, emof_MultiplicityElement, emof_TypedElement, Parameter_, Janus_emof_EnumerationLiteral, Enumeration_, Janus_emof_Package, NamedElement, Package, Janus_emof_Type, Janus_emof_Parameter, Janus_emof_Property, Janus_emof_TypedElement, Janus_emof_PrimitiveType, Janus_emof_URIExtent, Extent, Janus_emof_Comment, Janus_JTL_Transformation, emof_Class, emof_Package, Model, Pattern, Relation, Janus_JTL_Relation, Transformation, Domain, Variable, Janus_JTL_Domain, Janus_JTL_Model, Janus_JTL_Pattern, Janus_JTL_Predicate, Predicate, TemplateExp, Janus_essentialocl_CallExp, OclExpression, Janus_essentialocl_BooleanLiteralExp, PrimitiveLiteralExp, TryExp, Janus_essentialocl_OclExpression, TypedElement, Janus_essentialocl_UnlimitedNaturalExp, NumericLiteralExp, Janus_essentialocl_IfExp, Janus_essentialocl_Variable, Janus_essentialocl_LetExp, Janus_essentialocl_PropertyCallExp, FeaturePropertyCall, LetExp, ComputeExp, Janus_essentialocl_LoopExp, Janus_essentialocl_VariableExp, Janus_essentialocl_TypeExp, Janus_essentialocl_StringLiteralExp, essentialocl_CallExp, essentialocl_OclExpression, Janus_essentialocl_IteratorExp, LoopExp, Janus_essentialocl_IntegerLiteralExp, Janus_essentialocl_OperationCallExp, Janus_essentialocl_RealLiteralExp, Janus_essentialocl_LiteralExp, Janus_essentialocl_IterateExp, CollectionLiteralExp, Janus_essentialocl_PrimitiveLiteralExp, LiteralExp, Janus_essentialocl_NumericLiteralExp, Janus_essentialocl_CollectionLiteralExp, CollectionLiteralPart, Janus_essentialocl_CollectionLiteralPart, Janus_essentialocl_CollectionItem, Janus_essentialocl_CollectionRange, Janus_essentialocl_NullLiteralExp, Janus_essentialocl_ExpressionInOcl, OpaqueExpression, Janus_essentialocl_TupleLiteralExp, TupleLiteralPart, TupleLiteralExp, Janus_essentialocl_BagType, Janus_essentialocl_OpaqueExpression, Janus_essentialocl_InvalidLiteralExp, Janus_essentialocl_FeaturePropertyCall, CallExp, Janus_essentialocl_TupleLiteralPart, Janus_essentialocl_SetType, Janus_essentialocl_TupleType, emof_DataType, Janus_essentialocl_VoidType, Janus_essentialocl_AnyType, emof_Type, Janus_template_TemplateExp, CollectionType, Janus_essentialocl_CollectionType, Janus_essentialocl_EnumLiteralExp, Janus_essentialocl_InvalidType, Janus_essentialocl_OrderedSetType, Janus_essentialocl_SequenceType, Janus_template_ObjectTemplateExp, PropertyTemplateItem, Janus_template_CollectionTemplateExp, Janus_imperativeocl_AssignExp, ImperativeExpression, Janus_template_PropertyTemplateItem, ObjectTemplateExp, Janus_imperativeocl_ImperativeIterateExp, ImperativeLoopExp, Janus_imperativeocl_BlockExp, Janus_imperativeocl_VariableInitExp, Janus_imperativeocl_SwitchExp, imperativeocl_ImperativeExpression, AltExp, Janus_imperativeocl_WhileExp, Janus_imperativeocl_AltExp, Janus_imperativeocl_ComputeExp, Janus_imperativeocl_UnlinkExp, Janus_imperativeocl_BreakExp, Janus_imperativeocl_TryExp, Janus_imperativeocl_ReturnExp, Janus_imperativeocl_RaiseExp, Janus_imperativeocl_ContinueExp, Janus_imperativeocl_ForExp, Janus_imperativeocl_TupleExp, Janus_imperativeocl_Typedef, Janus_imperativeocl_InstantiationExp, Janus_imperativeocl_DictionaryType, Janus_imperativeocl_DictLiteralExp, Janus_imperativeocl_LogExp, DictLiteralPart, Janus_imperativeocl_DictLiteralPart, Janus_imperativeocl_TemplateParameterType, Janus_imperativeocl_ImperativeLoopExp, essentialocl_LoopExp, Janus_imperativeocl_AssertExp, LogExp, Janus_imperativeocl_AnonymousTupleType, Janus_imperativeocl_AnonymousTupleLiteralExp, AnonymousTupleLiteralPart, Janus_imperativeocl_CollectorExp, Janus_imperativeocl_ImperativeExpression, Janus_imperativeocl_UnpackExp, Janus_imperativeocl_AnonymousTupleLiteralPart, Janus_imperativeocl_ListType, CollectionKind, SeverityKind},
    associations={ownedOperation1, ownedAttribute0, superClass3, tag4, ownedComment6, element7, ownedLiteral9, class11, ownedParameter14, raisedException16, enumeration27, ownedType17, nestedPackage20, package21, operation24, Class29, opposite32, type34, modelParameter37, annotatedElement36, where44, relation38, transformation40, domain42, relation50, when46, variable49, transformation61, pattern53, model55, rootVariable58, whenOwner72, usedPackage64, dependsOn66, whereOwner69, domain81, predicate75, bindsTo77, templateExpression79, pattern84, conditionExpression87, tryBodyOwner90, source88, condition91, thenExpression93, elseExpression96, in99, variable101, initExpression103, LetExp105, bindParameter107, computeOwner110, referredProperty112, referredVariable114, referredType116, body118, iterator120, referredOperation125, argument123, result128, CollectionLiteralExp132, part130, last138, item134, first136, part141, resultVariable148, parameterVariable151, bodyExpression143, context145, TupleLiteralExp154, attribute156, elementType158, referredEnumLiteral160, part168, referredCollectionType170, match172, bindsTo162, where164, part167, target182, value184, objContainer175, value177, referredProperty179, left186, defaultValue189, elsePart195, body192, alternativePart194, condition200, body202, referredVariable198, body208, returnedElement205, target215, condition210, body212, value220, tryBody222, exception225, exceptBody227, item217, instantiatedClass239, exception230, element232, base234, condition236, keyType247, extent241, argument244, condition255, part249, key250, value252, condition264, element257, log260, assertion261, elementType270, target266, variable268, part272, value273},
    generalizations={gen_Janus_emof_Class_Type, gen_Janus_emof_Enumeration_DataType, gen_Janus_emof_DataType_Type, gen_Janus_emof_Element_Object, gen_Janus_emof_Tag_Element, gen_Janus_emof_NamedElement_Element, gen_Janus_emof_Extent_Object, gen_Janus_emof_Operation_emof_MultiplicityElement, gen_Janus_emof_Operation_emof_TypedElement, gen_Janus_emof_EnumerationLiteral_NamedElement, gen_Janus_emof_Package_NamedElement, gen_Janus_emof_Type_NamedElement, gen_Janus_emof_Parameter_emof_MultiplicityElement, gen_Janus_emof_Parameter_emof_TypedElement, gen_Janus_emof_URIExtent_Extent, gen_Janus_emof_Property_emof_MultiplicityElement, gen_Janus_emof_Property_emof_TypedElement, gen_Janus_emof_TypedElement_NamedElement, gen_Janus_emof_PrimitiveType_DataType, gen_Janus_emof_Comment_Element, gen_Janus_JTL_Transformation_emof_Class, gen_Janus_JTL_Transformation_emof_Package, gen_Janus_JTL_Relation_NamedElement, gen_Janus_JTL_Domain_NamedElement, gen_Janus_JTL_Model_NamedElement, gen_Janus_JTL_Pattern_Element, gen_Janus_JTL_Predicate_Element, gen_Janus_essentialocl_CallExp_OclExpression, gen_Janus_essentialocl_BooleanLiteralExp_PrimitiveLiteralExp, gen_Janus_essentialocl_OclExpression_TypedElement, gen_Janus_essentialocl_UnlimitedNaturalExp_NumericLiteralExp, gen_Janus_essentialocl_IfExp_OclExpression, gen_Janus_essentialocl_Variable_TypedElement, gen_Janus_essentialocl_LetExp_OclExpression, gen_Janus_essentialocl_PropertyCallExp_FeaturePropertyCall, gen_Janus_essentialocl_VariableExp_OclExpression, gen_Janus_essentialocl_TypeExp_OclExpression, gen_Janus_essentialocl_IteratorExp_LoopExp, gen_Janus_essentialocl_StringLiteralExp_PrimitiveLiteralExp, gen_Janus_essentialocl_LoopExp_essentialocl_CallExp, gen_Janus_essentialocl_LoopExp_essentialocl_OclExpression, gen_Janus_essentialocl_IntegerLiteralExp_NumericLiteralExp, gen_Janus_essentialocl_OperationCallExp_FeaturePropertyCall, gen_Janus_essentialocl_RealLiteralExp_NumericLiteralExp, gen_Janus_essentialocl_LiteralExp_OclExpression, gen_Janus_essentialocl_IterateExp_LoopExp, gen_Janus_essentialocl_PrimitiveLiteralExp_LiteralExp, gen_Janus_essentialocl_NumericLiteralExp_PrimitiveLiteralExp, gen_Janus_essentialocl_CollectionLiteralExp_LiteralExp, gen_Janus_essentialocl_CollectionLiteralPart_TypedElement, gen_Janus_essentialocl_CollectionItem_CollectionLiteralPart, gen_Janus_essentialocl_CollectionRange_CollectionLiteralPart, gen_Janus_essentialocl_NullLiteralExp_LiteralExp, gen_Janus_essentialocl_ExpressionInOcl_OpaqueExpression, gen_Janus_essentialocl_TupleLiteralExp_LiteralExp, gen_Janus_essentialocl_InvalidLiteralExp_LiteralExp, gen_Janus_essentialocl_FeaturePropertyCall_CallExp, gen_Janus_essentialocl_TupleLiteralPart_TypedElement, gen_Janus_essentialocl_SetType_CollectionType, gen_Janus_essentialocl_TupleType_emof_Class, gen_Janus_essentialocl_TupleType_emof_DataType, gen_Janus_essentialocl_VoidType_Type, gen_Janus_essentialocl_AnyType_emof_Class, gen_Janus_essentialocl_AnyType_emof_Type, gen_Janus_template_TemplateExp_LiteralExp, gen_Janus_essentialocl_BagType_CollectionType, gen_Janus_essentialocl_CollectionType_DataType, gen_Janus_essentialocl_EnumLiteralExp_LiteralExp, gen_Janus_essentialocl_InvalidType_Type, gen_Janus_essentialocl_OrderedSetType_CollectionType, gen_Janus_essentialocl_SequenceType_CollectionType, gen_Janus_template_ObjectTemplateExp_TemplateExp, gen_Janus_template_CollectionTemplateExp_TemplateExp, gen_Janus_imperativeocl_AssignExp_ImperativeExpression, gen_Janus_template_PropertyTemplateItem_Element, gen_Janus_imperativeocl_ImperativeIterateExp_ImperativeLoopExp, gen_Janus_imperativeocl_BlockExp_ImperativeExpression, gen_Janus_imperativeocl_SwitchExp_essentialocl_CallExp, gen_Janus_imperativeocl_SwitchExp_imperativeocl_ImperativeExpression, gen_Janus_imperativeocl_VariableInitExp_ImperativeExpression, gen_Janus_imperativeocl_WhileExp_ImperativeExpression, gen_Janus_imperativeocl_AltExp_ImperativeExpression, gen_Janus_imperativeocl_ComputeExp_ImperativeExpression, gen_Janus_imperativeocl_UnlinkExp_ImperativeExpression, gen_Janus_imperativeocl_BreakExp_ImperativeExpression, gen_Janus_imperativeocl_TryExp_ImperativeExpression, gen_Janus_imperativeocl_ReturnExp_ImperativeExpression, gen_Janus_imperativeocl_InstantiationExp_ImperativeExpression, gen_Janus_imperativeocl_RaiseExp_ImperativeExpression, gen_Janus_imperativeocl_ContinueExp_ImperativeExpression, gen_Janus_imperativeocl_ForExp_ImperativeLoopExp, gen_Janus_imperativeocl_TupleExp_ImperativeExpression, gen_Janus_imperativeocl_Typedef_Class, gen_Janus_imperativeocl_DictionaryType_CollectionType, gen_Janus_imperativeocl_DictLiteralExp_LiteralExp, gen_Janus_imperativeocl_LogExp_ImperativeExpression, gen_Janus_imperativeocl_DictLiteralPart_Element, gen_Janus_imperativeocl_TemplateParameterType_Type, gen_Janus_imperativeocl_ImperativeLoopExp_essentialocl_LoopExp, gen_Janus_imperativeocl_ImperativeLoopExp_imperativeocl_ImperativeExpression, gen_Janus_imperativeocl_AssertExp_ImperativeExpression, gen_Janus_imperativeocl_AnonymousTupleType_Class, gen_Janus_imperativeocl_AnonymousTupleLiteralExp_LiteralExp, gen_Janus_imperativeocl_CollectorExp_ImperativeLoopExp, gen_Janus_imperativeocl_ImperativeExpression_OclExpression, gen_Janus_imperativeocl_UnpackExp_ImperativeExpression, gen_Janus_imperativeocl_AnonymousTupleLiteralPart_Element, gen_Janus_imperativeocl_ListType_CollectionType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)