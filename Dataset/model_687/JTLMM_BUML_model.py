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
            EnumerationLiteral(name="Bag"),
			EnumerationLiteral(name="Sequence"),
			EnumerationLiteral(name="OrderedSet"),
			EnumerationLiteral(name="Set")
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
JTLMM_emof_Class = Class(name="JTLMM::emof::Class")
Type = Class(name="Type")
Property_ = Class(name="Property")
Operation = Class(name="Operation")
Class_ = Class(name="Class")
JTLMM_emof_Tag = Class(name="JTLMM::emof::Tag")
Element = Class(name="Element")
JTLMM_emof_Enumeration = Class(name="JTLMM::emof::Enumeration")
DataType = Class(name="DataType")
EnumerationLiteral = Class(name="EnumerationLiteral")
JTLMM_emof_NamedElement = Class(name="JTLMM::emof::NamedElement", is_abstract=True)
JTLMM_emof_DataType = Class(name="JTLMM::emof::DataType", is_abstract=True)
JTLMM_emof_Element = Class(name="JTLMM::emof::Element", is_abstract=True)
Object = Class(name="Object")
Tag = Class(name="Tag")
Comment = Class(name="Comment")
Parameter_ = Class(name="Parameter")
JTLMM_emof_MultiplicityElement = Class(name="JTLMM::emof::MultiplicityElement", is_abstract=True)
JTLMM_emof_Package = Class(name="JTLMM::emof::Package")
NamedElement = Class(name="NamedElement")
JTLMM_emof_Extent = Class(name="JTLMM::emof::Extent")
JTLMM_emof_Object = Class(name="JTLMM::emof::Object")
JTLMM_emof_Operation = Class(name="JTLMM::emof::Operation")
emof_MultiplicityElement = Class(name="emof::MultiplicityElement")
emof_TypedElement = Class(name="emof::TypedElement")
JTLMM_emof_Parameter = Class(name="JTLMM::emof::Parameter")
JTLMM_emof_TypedElement = Class(name="JTLMM::emof::TypedElement", is_abstract=True)
Package = Class(name="Package")
JTLMM_emof_PrimitiveType = Class(name="JTLMM::emof::PrimitiveType")
JTLMM_emof_EnumerationLiteral = Class(name="JTLMM::emof::EnumerationLiteral")
JTLMM_emof_Type = Class(name="JTLMM::emof::Type", is_abstract=True)
Enumeration_ = Class(name="Enumeration")
JTLMM_emof_Property = Class(name="JTLMM::emof::Property")
Relation = Class(name="Relation")
JTLMM_JTL_Relation = Class(name="JTLMM::JTL::Relation")
JTLMM_emof_URIExtent = Class(name="JTLMM::emof::URIExtent")
Extent = Class(name="Extent")
JTLMM_emof_Comment = Class(name="JTLMM::emof::Comment")
JTLMM_JTL_Transformation = Class(name="JTLMM::JTL::Transformation")
emof_Class = Class(name="emof::Class")
emof_Package = Class(name="emof::Package")
Model = Class(name="Model")
Pattern = Class(name="Pattern")
Transformation = Class(name="Transformation")
Domain = Class(name="Domain")
JTLMM_JTL_Domain = Class(name="JTLMM::JTL::Domain")
Variable = Class(name="Variable")
JTLMM_JTL_Model = Class(name="JTLMM::JTL::Model")
Predicate = Class(name="Predicate")
JTLMM_JTL_Pattern = Class(name="JTLMM::JTL::Pattern")
JTLMM_JTL_Predicate = Class(name="JTLMM::JTL::Predicate")
TemplateExp = Class(name="TemplateExp")
JTLMM_essentialocl_BooleanLiteralExp = Class(name="JTLMM::essentialocl::BooleanLiteralExp")
PrimitiveLiteralExp = Class(name="PrimitiveLiteralExp")
OclExpression = Class(name="OclExpression")
JTLMM_essentialocl_OclExpression = Class(name="JTLMM::essentialocl::OclExpression", is_abstract=True)
JTLMM_essentialocl_CallExp = Class(name="JTLMM::essentialocl::CallExp", is_abstract=True)
JTLMM_essentialocl_IfExp = Class(name="JTLMM::essentialocl::IfExp")
TypedElement = Class(name="TypedElement")
TryExp = Class(name="TryExp")
JTLMM_essentialocl_UnlimitedNaturalExp = Class(name="JTLMM::essentialocl::UnlimitedNaturalExp")
NumericLiteralExp = Class(name="NumericLiteralExp")
LetExp = Class(name="LetExp")
JTLMM_essentialocl_LetExp = Class(name="JTLMM::essentialocl::LetExp")
JTLMM_essentialocl_Variable = Class(name="JTLMM::essentialocl::Variable")
JTLMM_essentialocl_LoopExp = Class(name="JTLMM::essentialocl::LoopExp", is_abstract=True)
essentialocl_CallExp = Class(name="essentialocl::CallExp")
essentialocl_OclExpression = Class(name="essentialocl::OclExpression")
ComputeExp = Class(name="ComputeExp")
JTLMM_essentialocl_PropertyCallExp = Class(name="JTLMM::essentialocl::PropertyCallExp")
FeaturePropertyCall = Class(name="FeaturePropertyCall")
JTLMM_essentialocl_VariableExp = Class(name="JTLMM::essentialocl::VariableExp")
JTLMM_essentialocl_TypeExp = Class(name="JTLMM::essentialocl::TypeExp")
JTLMM_essentialocl_RealLiteralExp = Class(name="JTLMM::essentialocl::RealLiteralExp")
JTLMM_essentialocl_LiteralExp = Class(name="JTLMM::essentialocl::LiteralExp", is_abstract=True)
JTLMM_essentialocl_IteratorExp = Class(name="JTLMM::essentialocl::IteratorExp")
LoopExp = Class(name="LoopExp")
JTLMM_essentialocl_StringLiteralExp = Class(name="JTLMM::essentialocl::StringLiteralExp")
JTLMM_essentialocl_IntegerLiteralExp = Class(name="JTLMM::essentialocl::IntegerLiteralExp")
JTLMM_essentialocl_OperationCallExp = Class(name="JTLMM::essentialocl::OperationCallExp")
JTLMM_essentialocl_CollectionItem = Class(name="JTLMM::essentialocl::CollectionItem")
JTLMM_essentialocl_IterateExp = Class(name="JTLMM::essentialocl::IterateExp")
JTLMM_essentialocl_PrimitiveLiteralExp = Class(name="JTLMM::essentialocl::PrimitiveLiteralExp", is_abstract=True)
LiteralExp = Class(name="LiteralExp")
JTLMM_essentialocl_NumericLiteralExp = Class(name="JTLMM::essentialocl::NumericLiteralExp", is_abstract=True)
JTLMM_essentialocl_CollectionLiteralExp = Class(name="JTLMM::essentialocl::CollectionLiteralExp")
CollectionLiteralPart = Class(name="CollectionLiteralPart")
JTLMM_essentialocl_CollectionLiteralPart = Class(name="JTLMM::essentialocl::CollectionLiteralPart", is_abstract=True)
CollectionLiteralExp = Class(name="CollectionLiteralExp")
JTLMM_essentialocl_NullLiteralExp = Class(name="JTLMM::essentialocl::NullLiteralExp")
JTLMM_essentialocl_ExpressionInOcl = Class(name="JTLMM::essentialocl::ExpressionInOcl")
OpaqueExpression = Class(name="OpaqueExpression")
JTLMM_essentialocl_CollectionRange = Class(name="JTLMM::essentialocl::CollectionRange")
JTLMM_essentialocl_TupleLiteralExp = Class(name="JTLMM::essentialocl::TupleLiteralExp")
TupleLiteralPart = Class(name="TupleLiteralPart")
JTLMM_essentialocl_BagType = Class(name="JTLMM::essentialocl::BagType")
CollectionType = Class(name="CollectionType")
JTLMM_essentialocl_CollectionType = Class(name="JTLMM::essentialocl::CollectionType", is_abstract=True)
JTLMM_essentialocl_OpaqueExpression = Class(name="JTLMM::essentialocl::OpaqueExpression")
JTLMM_essentialocl_InvalidLiteralExp = Class(name="JTLMM::essentialocl::InvalidLiteralExp")
JTLMM_essentialocl_FeaturePropertyCall = Class(name="JTLMM::essentialocl::FeaturePropertyCall", is_abstract=True)
CallExp = Class(name="CallExp")
JTLMM_essentialocl_TupleLiteralPart = Class(name="JTLMM::essentialocl::TupleLiteralPart")
TupleLiteralExp = Class(name="TupleLiteralExp")
JTLMM_essentialocl_InvalidType = Class(name="JTLMM::essentialocl::InvalidType")
JTLMM_essentialocl_OrderedSetType = Class(name="JTLMM::essentialocl::OrderedSetType")
JTLMM_essentialocl_EnumLiteralExp = Class(name="JTLMM::essentialocl::EnumLiteralExp")
JTLMM_essentialocl_VoidType = Class(name="JTLMM::essentialocl::VoidType")
JTLMM_essentialocl_AnyType = Class(name="JTLMM::essentialocl::AnyType")
emof_Type = Class(name="emof::Type")
JTLMM_essentialocl_SequenceType = Class(name="JTLMM::essentialocl::SequenceType")
JTLMM_essentialocl_SetType = Class(name="JTLMM::essentialocl::SetType")
JTLMM_essentialocl_TupleType = Class(name="JTLMM::essentialocl::TupleType")
emof_DataType = Class(name="emof::DataType")
JTLMM_template_TemplateExp = Class(name="JTLMM::template::TemplateExp", is_abstract=True)
AssignExp = Class(name="AssignExp")
JTLMM_template_ObjectTemplateExp = Class(name="JTLMM::template::ObjectTemplateExp")
PropertyTemplateItem = Class(name="PropertyTemplateItem")
JTLMM_template_CollectionTemplateExp = Class(name="JTLMM::template::CollectionTemplateExp")
JTLMM_template_PropertyTemplateItem = Class(name="JTLMM::template::PropertyTemplateItem")
ObjectTemplateExp = Class(name="ObjectTemplateExp")
JTLMM_imperativeocl_ImperativeIterateExp = Class(name="JTLMM::imperativeocl::ImperativeIterateExp")
ImperativeLoopExp = Class(name="ImperativeLoopExp")
JTLMM_imperativeocl_AssignExp = Class(name="JTLMM::imperativeocl::AssignExp")
ImperativeExpression = Class(name="ImperativeExpression")
JTLMM_imperativeocl_BlockExp = Class(name="JTLMM::imperativeocl::BlockExp")
JTLMM_imperativeocl_SwitchExp = Class(name="JTLMM::imperativeocl::SwitchExp")
imperativeocl_ImperativeExpression = Class(name="imperativeocl::ImperativeExpression")
AltExp = Class(name="AltExp")
JTLMM_imperativeocl_VariableInitExp = Class(name="JTLMM::imperativeocl::VariableInitExp")
JTLMM_imperativeocl_WhileExp = Class(name="JTLMM::imperativeocl::WhileExp")
JTLMM_imperativeocl_ComputeExp = Class(name="JTLMM::imperativeocl::ComputeExp")
JTLMM_imperativeocl_AltExp = Class(name="JTLMM::imperativeocl::AltExp")
JTLMM_imperativeocl_UnlinkExp = Class(name="JTLMM::imperativeocl::UnlinkExp")
JTLMM_imperativeocl_ReturnExp = Class(name="JTLMM::imperativeocl::ReturnExp")
JTLMM_imperativeocl_BreakExp = Class(name="JTLMM::imperativeocl::BreakExp")
JTLMM_imperativeocl_TryExp = Class(name="JTLMM::imperativeocl::TryExp")
JTLMM_imperativeocl_RaiseExp = Class(name="JTLMM::imperativeocl::RaiseExp")
JTLMM_imperativeocl_ContinueExp = Class(name="JTLMM::imperativeocl::ContinueExp")
JTLMM_imperativeocl_ForExp = Class(name="JTLMM::imperativeocl::ForExp")
JTLMM_imperativeocl_TupleExp = Class(name="JTLMM::imperativeocl::TupleExp")
JTLMM_imperativeocl_Typedef = Class(name="JTLMM::imperativeocl::Typedef")
JTLMM_imperativeocl_InstantiationExp = Class(name="JTLMM::imperativeocl::InstantiationExp")
DictLiteralPart = Class(name="DictLiteralPart")
JTLMM_imperativeocl_DictionaryType = Class(name="JTLMM::imperativeocl::DictionaryType")
JTLMM_imperativeocl_DictLiteralExp = Class(name="JTLMM::imperativeocl::DictLiteralExp")
JTLMM_imperativeocl_DictLiteralPart = Class(name="JTLMM::imperativeocl::DictLiteralPart")
JTLMM_imperativeocl_TemplateParameterType = Class(name="JTLMM::imperativeocl::TemplateParameterType")
JTLMM_imperativeocl_LogExp = Class(name="JTLMM::imperativeocl::LogExp")
LogExp = Class(name="LogExp")
JTLMM_imperativeocl_AssertExp = Class(name="JTLMM::imperativeocl::AssertExp")
JTLMM_imperativeocl_CollectorExp = Class(name="JTLMM::imperativeocl::CollectorExp")
JTLMM_imperativeocl_ImperativeLoopExp = Class(name="JTLMM::imperativeocl::ImperativeLoopExp", is_abstract=True)
essentialocl_LoopExp = Class(name="essentialocl::LoopExp")
JTLMM_imperativeocl_UnpackExp = Class(name="JTLMM::imperativeocl::UnpackExp")
JTLMM_imperativeocl_ImperativeExpression = Class(name="JTLMM::imperativeocl::ImperativeExpression", is_abstract=True)
JTLMM_imperativeocl_AnonymousTupleLiteralExp = Class(name="JTLMM::imperativeocl::AnonymousTupleLiteralExp")
AnonymousTupleLiteralPart = Class(name="AnonymousTupleLiteralPart")
JTLMM_imperativeocl_AnonymousTupleType = Class(name="JTLMM::imperativeocl::AnonymousTupleType")
JTLMM_imperativeocl_AnonymousTupleLiteralPart = Class(name="JTLMM::imperativeocl::AnonymousTupleLiteralPart")
JTLMM_imperativeocl_ListType = Class(name="JTLMM::imperativeocl::ListType")

# JTLMM_emof_Class class attributes and methods
JTLMM_emof_Class_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
JTLMM_emof_Class.attributes={JTLMM_emof_Class_isAbstract}

# Type class attributes and methods

# Property class attributes and methods

# Operation class attributes and methods

# Class class attributes and methods

# JTLMM_emof_Tag class attributes and methods
JTLMM_emof_Tag_value: Property = Property(name="value", type=StringType)
JTLMM_emof_Tag_name: Property = Property(name="name", type=StringType)
JTLMM_emof_Tag.attributes={JTLMM_emof_Tag_name, JTLMM_emof_Tag_value}

# Element class attributes and methods

# JTLMM_emof_Enumeration class attributes and methods

# DataType class attributes and methods

# EnumerationLiteral class attributes and methods

# JTLMM_emof_NamedElement class attributes and methods
JTLMM_emof_NamedElement_name: Property = Property(name="name", type=StringType)
JTLMM_emof_NamedElement.attributes={JTLMM_emof_NamedElement_name}

# JTLMM_emof_DataType class attributes and methods

# JTLMM_emof_Element class attributes and methods

# Object class attributes and methods

# Tag class attributes and methods

# Comment class attributes and methods

# Parameter class attributes and methods

# JTLMM_emof_MultiplicityElement class attributes and methods
JTLMM_emof_MultiplicityElement_isOrdered: Property = Property(name="isOrdered", type=StringType)
JTLMM_emof_MultiplicityElement_isUnique: Property = Property(name="isUnique", type=StringType)
JTLMM_emof_MultiplicityElement_lower: Property = Property(name="lower", type=IntegerType)
JTLMM_emof_MultiplicityElement_upper: Property = Property(name="upper", type=StringType)
JTLMM_emof_MultiplicityElement.attributes={JTLMM_emof_MultiplicityElement_upper, JTLMM_emof_MultiplicityElement_isOrdered, JTLMM_emof_MultiplicityElement_isUnique, JTLMM_emof_MultiplicityElement_lower}

# JTLMM_emof_Package class attributes and methods
JTLMM_emof_Package_uri: Property = Property(name="uri", type=StringType)
JTLMM_emof_Package.attributes={JTLMM_emof_Package_uri}

# NamedElement class attributes and methods

# JTLMM_emof_Extent class attributes and methods

# JTLMM_emof_Object class attributes and methods

# JTLMM_emof_Operation class attributes and methods

# emof_MultiplicityElement class attributes and methods

# emof_TypedElement class attributes and methods

# JTLMM_emof_Parameter class attributes and methods

# JTLMM_emof_TypedElement class attributes and methods
JTLMM_emof_TypedElement_type: Property = Property(name="type", type=StringType)
JTLMM_emof_TypedElement.attributes={JTLMM_emof_TypedElement_type}

# Package class attributes and methods

# JTLMM_emof_PrimitiveType class attributes and methods

# JTLMM_emof_EnumerationLiteral class attributes and methods

# JTLMM_emof_Type class attributes and methods

# Enumeration class attributes and methods

# JTLMM_emof_Property class attributes and methods
JTLMM_emof_Property_isComposite: Property = Property(name="isComposite", type=BooleanType)
JTLMM_emof_Property_isId: Property = Property(name="isId", type=BooleanType)
JTLMM_emof_Property_default: Property = Property(name="default", type=StringType)
JTLMM_emof_Property_isReadOnly: Property = Property(name="isReadOnly", type=BooleanType)
JTLMM_emof_Property_isDerived: Property = Property(name="isDerived", type=BooleanType)
JTLMM_emof_Property.attributes={JTLMM_emof_Property_isComposite, JTLMM_emof_Property_default, JTLMM_emof_Property_isReadOnly, JTLMM_emof_Property_isDerived, JTLMM_emof_Property_isId}

# Relation class attributes and methods

# JTLMM_JTL_Relation class attributes and methods
JTLMM_JTL_Relation_isTopLevel: Property = Property(name="isTopLevel", type=BooleanType)
JTLMM_JTL_Relation.attributes={JTLMM_JTL_Relation_isTopLevel}

# JTLMM_emof_URIExtent class attributes and methods

# Extent class attributes and methods

# JTLMM_emof_Comment class attributes and methods

# JTLMM_JTL_Transformation class attributes and methods

# emof_Class class attributes and methods

# emof_Package class attributes and methods

# Model class attributes and methods

# Pattern class attributes and methods

# Transformation class attributes and methods

# Domain class attributes and methods

# JTLMM_JTL_Domain class attributes and methods
JTLMM_JTL_Domain_isCheckable: Property = Property(name="isCheckable", type=BooleanType)
JTLMM_JTL_Domain_isEnforceable: Property = Property(name="isEnforceable", type=BooleanType)
JTLMM_JTL_Domain.attributes={JTLMM_JTL_Domain_isEnforceable, JTLMM_JTL_Domain_isCheckable}

# Variable class attributes and methods

# JTLMM_JTL_Model class attributes and methods
JTLMM_JTL_Model_usedPackage: Property = Property(name="usedPackage", type=StringType)
JTLMM_JTL_Model.attributes={JTLMM_JTL_Model_usedPackage}

# Predicate class attributes and methods

# JTLMM_JTL_Pattern class attributes and methods

# JTLMM_JTL_Predicate class attributes and methods

# TemplateExp class attributes and methods

# JTLMM_essentialocl_BooleanLiteralExp class attributes and methods
JTLMM_essentialocl_BooleanLiteralExp_booleanSymbol: Property = Property(name="booleanSymbol", type=BooleanType)
JTLMM_essentialocl_BooleanLiteralExp.attributes={JTLMM_essentialocl_BooleanLiteralExp_booleanSymbol}

# PrimitiveLiteralExp class attributes and methods

# OclExpression class attributes and methods

# JTLMM_essentialocl_OclExpression class attributes and methods

# JTLMM_essentialocl_CallExp class attributes and methods

# JTLMM_essentialocl_IfExp class attributes and methods

# TypedElement class attributes and methods

# TryExp class attributes and methods

# JTLMM_essentialocl_UnlimitedNaturalExp class attributes and methods
JTLMM_essentialocl_UnlimitedNaturalExp_symbol: Property = Property(name="symbol", type=StringType)
JTLMM_essentialocl_UnlimitedNaturalExp.attributes={JTLMM_essentialocl_UnlimitedNaturalExp_symbol}

# NumericLiteralExp class attributes and methods

# LetExp class attributes and methods

# JTLMM_essentialocl_LetExp class attributes and methods

# JTLMM_essentialocl_Variable class attributes and methods

# JTLMM_essentialocl_LoopExp class attributes and methods

# essentialocl_CallExp class attributes and methods

# essentialocl_OclExpression class attributes and methods

# ComputeExp class attributes and methods

# JTLMM_essentialocl_PropertyCallExp class attributes and methods

# FeaturePropertyCall class attributes and methods

# JTLMM_essentialocl_VariableExp class attributes and methods

# JTLMM_essentialocl_TypeExp class attributes and methods

# JTLMM_essentialocl_RealLiteralExp class attributes and methods
JTLMM_essentialocl_RealLiteralExp_realSymbol: Property = Property(name="realSymbol", type=FloatType)
JTLMM_essentialocl_RealLiteralExp.attributes={JTLMM_essentialocl_RealLiteralExp_realSymbol}

# JTLMM_essentialocl_LiteralExp class attributes and methods

# JTLMM_essentialocl_IteratorExp class attributes and methods

# LoopExp class attributes and methods

# JTLMM_essentialocl_StringLiteralExp class attributes and methods
JTLMM_essentialocl_StringLiteralExp_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
JTLMM_essentialocl_StringLiteralExp.attributes={JTLMM_essentialocl_StringLiteralExp_stringSymbol}

# JTLMM_essentialocl_IntegerLiteralExp class attributes and methods
JTLMM_essentialocl_IntegerLiteralExp_integerSymbol: Property = Property(name="integerSymbol", type=IntegerType)
JTLMM_essentialocl_IntegerLiteralExp.attributes={JTLMM_essentialocl_IntegerLiteralExp_integerSymbol}

# JTLMM_essentialocl_OperationCallExp class attributes and methods

# JTLMM_essentialocl_CollectionItem class attributes and methods

# JTLMM_essentialocl_IterateExp class attributes and methods

# JTLMM_essentialocl_PrimitiveLiteralExp class attributes and methods

# LiteralExp class attributes and methods

# JTLMM_essentialocl_NumericLiteralExp class attributes and methods

# JTLMM_essentialocl_CollectionLiteralExp class attributes and methods
JTLMM_essentialocl_CollectionLiteralExp_kind: Property = Property(name="kind", type=StringType)
JTLMM_essentialocl_CollectionLiteralExp.attributes={JTLMM_essentialocl_CollectionLiteralExp_kind}

# CollectionLiteralPart class attributes and methods

# JTLMM_essentialocl_CollectionLiteralPart class attributes and methods

# CollectionLiteralExp class attributes and methods

# JTLMM_essentialocl_NullLiteralExp class attributes and methods

# JTLMM_essentialocl_ExpressionInOcl class attributes and methods

# OpaqueExpression class attributes and methods

# JTLMM_essentialocl_CollectionRange class attributes and methods

# JTLMM_essentialocl_TupleLiteralExp class attributes and methods

# TupleLiteralPart class attributes and methods

# JTLMM_essentialocl_BagType class attributes and methods

# CollectionType class attributes and methods

# JTLMM_essentialocl_CollectionType class attributes and methods

# JTLMM_essentialocl_OpaqueExpression class attributes and methods

# JTLMM_essentialocl_InvalidLiteralExp class attributes and methods

# JTLMM_essentialocl_FeaturePropertyCall class attributes and methods

# CallExp class attributes and methods

# JTLMM_essentialocl_TupleLiteralPart class attributes and methods

# TupleLiteralExp class attributes and methods

# JTLMM_essentialocl_InvalidType class attributes and methods

# JTLMM_essentialocl_OrderedSetType class attributes and methods

# JTLMM_essentialocl_EnumLiteralExp class attributes and methods

# JTLMM_essentialocl_VoidType class attributes and methods

# JTLMM_essentialocl_AnyType class attributes and methods

# emof_Type class attributes and methods

# JTLMM_essentialocl_SequenceType class attributes and methods

# JTLMM_essentialocl_SetType class attributes and methods

# JTLMM_essentialocl_TupleType class attributes and methods

# emof_DataType class attributes and methods

# JTLMM_template_TemplateExp class attributes and methods

# AssignExp class attributes and methods

# JTLMM_template_ObjectTemplateExp class attributes and methods
JTLMM_template_ObjectTemplateExp_referredClass: Property = Property(name="referredClass", type=StringType)
JTLMM_template_ObjectTemplateExp.attributes={JTLMM_template_ObjectTemplateExp_referredClass}

# PropertyTemplateItem class attributes and methods

# JTLMM_template_CollectionTemplateExp class attributes and methods
JTLMM_template_CollectionTemplateExp_kind: Property = Property(name="kind", type=StringType)
JTLMM_template_CollectionTemplateExp.attributes={JTLMM_template_CollectionTemplateExp_kind}

# JTLMM_template_PropertyTemplateItem class attributes and methods

# ObjectTemplateExp class attributes and methods

# JTLMM_imperativeocl_ImperativeIterateExp class attributes and methods

# ImperativeLoopExp class attributes and methods

# JTLMM_imperativeocl_AssignExp class attributes and methods
JTLMM_imperativeocl_AssignExp_isReset: Property = Property(name="isReset", type=BooleanType)
JTLMM_imperativeocl_AssignExp.attributes={JTLMM_imperativeocl_AssignExp_isReset}

# ImperativeExpression class attributes and methods

# JTLMM_imperativeocl_BlockExp class attributes and methods

# JTLMM_imperativeocl_SwitchExp class attributes and methods

# imperativeocl_ImperativeExpression class attributes and methods

# AltExp class attributes and methods

# JTLMM_imperativeocl_VariableInitExp class attributes and methods
JTLMM_imperativeocl_VariableInitExp_withResult: Property = Property(name="withResult", type=BooleanType)
JTLMM_imperativeocl_VariableInitExp.attributes={JTLMM_imperativeocl_VariableInitExp_withResult}

# JTLMM_imperativeocl_WhileExp class attributes and methods

# JTLMM_imperativeocl_ComputeExp class attributes and methods

# JTLMM_imperativeocl_AltExp class attributes and methods

# JTLMM_imperativeocl_UnlinkExp class attributes and methods

# JTLMM_imperativeocl_ReturnExp class attributes and methods

# JTLMM_imperativeocl_BreakExp class attributes and methods

# JTLMM_imperativeocl_TryExp class attributes and methods

# JTLMM_imperativeocl_RaiseExp class attributes and methods

# JTLMM_imperativeocl_ContinueExp class attributes and methods

# JTLMM_imperativeocl_ForExp class attributes and methods

# JTLMM_imperativeocl_TupleExp class attributes and methods

# JTLMM_imperativeocl_Typedef class attributes and methods

# JTLMM_imperativeocl_InstantiationExp class attributes and methods

# DictLiteralPart class attributes and methods

# JTLMM_imperativeocl_DictionaryType class attributes and methods

# JTLMM_imperativeocl_DictLiteralExp class attributes and methods

# JTLMM_imperativeocl_DictLiteralPart class attributes and methods

# JTLMM_imperativeocl_TemplateParameterType class attributes and methods
JTLMM_imperativeocl_TemplateParameterType_specification: Property = Property(name="specification", type=StringType)
JTLMM_imperativeocl_TemplateParameterType.attributes={JTLMM_imperativeocl_TemplateParameterType_specification}

# JTLMM_imperativeocl_LogExp class attributes and methods
JTLMM_imperativeocl_LogExp_level: Property = Property(name="level", type=IntegerType)
JTLMM_imperativeocl_LogExp_text: Property = Property(name="text", type=StringType)
JTLMM_imperativeocl_LogExp.attributes={JTLMM_imperativeocl_LogExp_text, JTLMM_imperativeocl_LogExp_level}

# LogExp class attributes and methods

# JTLMM_imperativeocl_AssertExp class attributes and methods
JTLMM_imperativeocl_AssertExp_severity: Property = Property(name="severity", type=StringType)
JTLMM_imperativeocl_AssertExp.attributes={JTLMM_imperativeocl_AssertExp_severity}

# JTLMM_imperativeocl_CollectorExp class attributes and methods

# JTLMM_imperativeocl_ImperativeLoopExp class attributes and methods

# essentialocl_LoopExp class attributes and methods

# JTLMM_imperativeocl_UnpackExp class attributes and methods

# JTLMM_imperativeocl_ImperativeExpression class attributes and methods

# JTLMM_imperativeocl_AnonymousTupleLiteralExp class attributes and methods

# AnonymousTupleLiteralPart class attributes and methods

# JTLMM_imperativeocl_AnonymousTupleType class attributes and methods

# JTLMM_imperativeocl_AnonymousTupleLiteralPart class attributes and methods

# JTLMM_imperativeocl_ListType class attributes and methods

# Relationships
ownedAttribute0: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute0",
    ends={
        Property(name="emof", type=JTLMM_emof_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Property", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation1: BinaryAssociation = BinaryAssociation(
    name="ownedOperation1",
    ends={
        Property(name="emof2", type=JTLMM_emof_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Operation", type=Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass3: BinaryAssociation = BinaryAssociation(
    name="superClass3",
    ends={
        Property(name="Class", type=JTLMM_emof_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_emof_Class", type=Class_, multiplicity=Multiplicity(0, 9999))
    }
)
element7: BinaryAssociation = BinaryAssociation(
    name="element7",
    ends={
        Property(name="emof8", type=JTLMM_emof_Tag, multiplicity=Multiplicity(1, 1)),
        Property(name="Element", type=Element, multiplicity=Multiplicity(0, 9999))
    }
)
ownedLiteral9: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral9",
    ends={
        Property(name="emof10", type=JTLMM_emof_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="EnumerationLiteral", type=EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tag4: BinaryAssociation = BinaryAssociation(
    name="tag4",
    ends={
        Property(name="emof5", type=JTLMM_emof_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="Tag", type=Tag, multiplicity=Multiplicity(0, 9999))
    }
)
ownedComment6: BinaryAssociation = BinaryAssociation(
    name="ownedComment6",
    ends={
        Property(name="Comment", type=JTLMM_emof_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_emof_Element", type=Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedParameter14: BinaryAssociation = BinaryAssociation(
    name="ownedParameter14",
    ends={
        Property(name="emof15", type=JTLMM_emof_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="Parameter", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
raisedException16: BinaryAssociation = BinaryAssociation(
    name="raisedException16",
    ends={
        Property(name="Type", type=JTLMM_emof_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_emof_Operation", type=Type, multiplicity=Multiplicity(0, 9999))
    }
)
class11: BinaryAssociation = BinaryAssociation(
    name="class11",
    ends={
        Property(name="emof13", type=JTLMM_emof_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="Class12", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
package21: BinaryAssociation = BinaryAssociation(
    name="package21",
    ends={
        Property(name="emof23", type=JTLMM_emof_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="Package22", type=Package, multiplicity=Multiplicity(1, 1))
    }
)
ownedType17: BinaryAssociation = BinaryAssociation(
    name="ownedType17",
    ends={
        Property(name="emof19", type=JTLMM_emof_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="Type18", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedPackage20: BinaryAssociation = BinaryAssociation(
    name="nestedPackage20",
    ends={
        Property(name="Package", type=JTLMM_emof_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_emof_Package", type=Package, multiplicity=Multiplicity(0, 9999))
    }
)
operation24: BinaryAssociation = BinaryAssociation(
    name="operation24",
    ends={
        Property(name="emof26", type=JTLMM_emof_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="Operation25", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
enumeration27: BinaryAssociation = BinaryAssociation(
    name="enumeration27",
    ends={
        Property(name="emof28", type=JTLMM_emof_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="Enumeration", type=Enumeration_, multiplicity=Multiplicity(0, 1))
    }
)
Class29: BinaryAssociation = BinaryAssociation(
    name="Class29",
    ends={
        Property(name="emof31", type=JTLMM_emof_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="Class30", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
opposite32: BinaryAssociation = BinaryAssociation(
    name="opposite32",
    ends={
        Property(name="Property33", type=JTLMM_emof_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_emof_Property", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
relation36: BinaryAssociation = BinaryAssociation(
    name="relation36",
    ends={
        Property(name="JTL37", type=JTLMM_JTL_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="Relation", type=Relation, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
annotatedElement34: BinaryAssociation = BinaryAssociation(
    name="annotatedElement34",
    ends={
        Property(name="NamedElement", type=JTLMM_emof_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_emof_Comment", type=NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
modelParameter35: BinaryAssociation = BinaryAssociation(
    name="modelParameter35",
    ends={
        Property(name="JTL", type=JTLMM_JTL_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="Model", type=Model, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
where42: BinaryAssociation = BinaryAssociation(
    name="where42",
    ends={
        Property(name="JTL43", type=JTLMM_JTL_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="Pattern", type=Pattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
transformation38: BinaryAssociation = BinaryAssociation(
    name="transformation38",
    ends={
        Property(name="JTL39", type=JTLMM_JTL_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="Transformation", type=Transformation, multiplicity=Multiplicity(1, 1))
    }
)
domain40: BinaryAssociation = BinaryAssociation(
    name="domain40",
    ends={
        Property(name="JTL41", type=JTLMM_JTL_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="Domain", type=Domain, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
when44: BinaryAssociation = BinaryAssociation(
    name="when44",
    ends={
        Property(name="JTL46", type=JTLMM_JTL_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="Pattern45", type=Pattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable47: BinaryAssociation = BinaryAssociation(
    name="variable47",
    ends={
        Property(name="Variable", type=JTLMM_JTL_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_JTL_Relation", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
model53: BinaryAssociation = BinaryAssociation(
    name="model53",
    ends={
        Property(name="Model55", type=JTLMM_JTL_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_JTL_Domain54", type=Model, multiplicity=Multiplicity(1, 1))
    }
)
relation48: BinaryAssociation = BinaryAssociation(
    name="relation48",
    ends={
        Property(name="JTL50", type=JTLMM_JTL_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="Relation49", type=Relation, multiplicity=Multiplicity(1, 1))
    }
)
pattern51: BinaryAssociation = BinaryAssociation(
    name="pattern51",
    ends={
        Property(name="Pattern52", type=JTLMM_JTL_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_JTL_Domain", type=Pattern, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dependsOn62: BinaryAssociation = BinaryAssociation(
    name="dependsOn62",
    ends={
        Property(name="Model63", type=JTLMM_JTL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_JTL_Model", type=Model, multiplicity=Multiplicity(0, 9999))
    }
)
rootVariable56: BinaryAssociation = BinaryAssociation(
    name="rootVariable56",
    ends={
        Property(name="Variable58", type=JTLMM_JTL_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_JTL_Domain57", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
transformation59: BinaryAssociation = BinaryAssociation(
    name="transformation59",
    ends={
        Property(name="JTL61", type=JTLMM_JTL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="Transformation60", type=Transformation, multiplicity=Multiplicity(1, 1))
    }
)
predicate70: BinaryAssociation = BinaryAssociation(
    name="predicate70",
    ends={
        Property(name="JTL71", type=JTLMM_JTL_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="Predicate", type=Predicate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
whereOwner64: BinaryAssociation = BinaryAssociation(
    name="whereOwner64",
    ends={
        Property(name="JTL66", type=JTLMM_JTL_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="Relation65", type=Relation, multiplicity=Multiplicity(0, 1))
    }
)
whenOwner67: BinaryAssociation = BinaryAssociation(
    name="whenOwner67",
    ends={
        Property(name="JTL69", type=JTLMM_JTL_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="Relation68", type=Relation, multiplicity=Multiplicity(0, 1))
    }
)
domain76: BinaryAssociation = BinaryAssociation(
    name="domain76",
    ends={
        Property(name="Domain78", type=JTLMM_JTL_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_JTL_Pattern77", type=Domain, multiplicity=Multiplicity(1, 1))
    }
)
bindsTo72: BinaryAssociation = BinaryAssociation(
    name="bindsTo72",
    ends={
        Property(name="Variable73", type=JTLMM_JTL_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_JTL_Pattern", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
templateExpression74: BinaryAssociation = BinaryAssociation(
    name="templateExpression74",
    ends={
        Property(name="TemplateExp", type=JTLMM_JTL_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_JTL_Pattern75", type=TemplateExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pattern79: BinaryAssociation = BinaryAssociation(
    name="pattern79",
    ends={
        Property(name="JTL81", type=JTLMM_JTL_Predicate, multiplicity=Multiplicity(1, 1)),
        Property(name="Pattern80", type=Pattern, multiplicity=Multiplicity(1, 1))
    }
)
conditionExpression82: BinaryAssociation = BinaryAssociation(
    name="conditionExpression82",
    ends={
        Property(name="OclExpression", type=JTLMM_JTL_Predicate, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_JTL_Predicate", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source83: BinaryAssociation = BinaryAssociation(
    name="source83",
    ends={
        Property(name="OclExpression84", type=JTLMM_essentialocl_CallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_essentialocl_CallExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tryBodyOwner85: BinaryAssociation = BinaryAssociation(
    name="tryBodyOwner85",
    ends={
        Property(name="imperativeocl", type=JTLMM_essentialocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="TryExp", type=TryExp, multiplicity=Multiplicity(0, 1))
    }
)
elseExpression91: BinaryAssociation = BinaryAssociation(
    name="elseExpression91",
    ends={
        Property(name="OclExpression93", type=JTLMM_essentialocl_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_essentialocl_IfExp92", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition86: BinaryAssociation = BinaryAssociation(
    name="condition86",
    ends={
        Property(name="OclExpression87", type=JTLMM_essentialocl_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_essentialocl_IfExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression88: BinaryAssociation = BinaryAssociation(
    name="thenExpression88",
    ends={
        Property(name="OclExpression90", type=JTLMM_essentialocl_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_essentialocl_IfExp89", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initExpression98: BinaryAssociation = BinaryAssociation(
    name="initExpression98",
    ends={
        Property(name="OclExpression99", type=JTLMM_essentialocl_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_essentialocl_Variable", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
LetExp100: BinaryAssociation = BinaryAssociation(
    name="LetExp100",
    ends={
        Property(name="essentialocl101", type=JTLMM_essentialocl_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="LetExp", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
in94: BinaryAssociation = BinaryAssociation(
    name="in94",
    ends={
        Property(name="OclExpression95", type=JTLMM_essentialocl_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_essentialocl_LetExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable96: BinaryAssociation = BinaryAssociation(
    name="variable96",
    ends={
        Property(name="essentialocl", type=JTLMM_essentialocl_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Variable97", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body113: BinaryAssociation = BinaryAssociation(
    name="body113",
    ends={
        Property(name="OclExpression114", type=JTLMM_essentialocl_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_essentialocl_LoopExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
bindParameter102: BinaryAssociation = BinaryAssociation(
    name="bindParameter102",
    ends={
        Property(name="Parameter104", type=JTLMM_essentialocl_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_essentialocl_Variable103", type=Parameter_, multiplicity=Multiplicity(0, 1))
    }
)
computeOwner105: BinaryAssociation = BinaryAssociation(
    name="computeOwner105",
    ends={
        Property(name="imperativeocl106", type=JTLMM_essentialocl_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="ComputeExp", type=ComputeExp, multiplicity=Multiplicity(0, 1))
    }
)
referredProperty107: BinaryAssociation = BinaryAssociation(
    name="referredProperty107",
    ends={
        Property(name="Property108", type=JTLMM_essentialocl_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_essentialocl_PropertyCallExp", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
referredVariable109: BinaryAssociation = BinaryAssociation(
    name="referredVariable109",
    ends={
        Property(name="Variable110", type=JTLMM_essentialocl_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_essentialocl_VariableExp", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
referredType111: BinaryAssociation = BinaryAssociation(
    name="referredType111",
    ends={
        Property(name="Type112", type=JTLMM_essentialocl_TypeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_essentialocl_TypeExp", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
referredOperation120: BinaryAssociation = BinaryAssociation(
    name="referredOperation120",
    ends={
        Property(name="Relation122", type=JTLMM_essentialocl_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_essentialocl_OperationCallExp121", type=Relation, multiplicity=Multiplicity(0, 1))
    }
)
iterator115: BinaryAssociation = BinaryAssociation(
    name="iterator115",
    ends={
        Property(name="Variable117", type=JTLMM_essentialocl_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_essentialocl_LoopExp116", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument118: BinaryAssociation = BinaryAssociation(
    name="argument118",
    ends={
        Property(name="OclExpression119", type=JTLMM_essentialocl_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_essentialocl_OperationCallExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
CollectionLiteralExp127: BinaryAssociation = BinaryAssociation(
    name="CollectionLiteralExp127",
    ends={
        Property(name="essentialocl128", type=JTLMM_essentialocl_CollectionLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="CollectionLiteralExp", type=CollectionLiteralExp, multiplicity=Multiplicity(1, 1))
    }
)
item129: BinaryAssociation = BinaryAssociation(
    name="item129",
    ends={
        Property(name="OclExpression130", type=JTLMM_essentialocl_CollectionItem, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_essentialocl_CollectionItem", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
result123: BinaryAssociation = BinaryAssociation(
    name="result123",
    ends={
        Property(name="Variable124", type=JTLMM_essentialocl_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_essentialocl_IterateExp", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
part125: BinaryAssociation = BinaryAssociation(
    name="part125",
    ends={
        Property(name="essentialocl126", type=JTLMM_essentialocl_CollectionLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="CollectionLiteralPart", type=CollectionLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyExpression138: BinaryAssociation = BinaryAssociation(
    name="bodyExpression138",
    ends={
        Property(name="OclExpression139", type=JTLMM_essentialocl_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_essentialocl_ExpressionInOcl", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
first131: BinaryAssociation = BinaryAssociation(
    name="first131",
    ends={
        Property(name="OclExpression132", type=JTLMM_essentialocl_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_essentialocl_CollectionRange", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
last133: BinaryAssociation = BinaryAssociation(
    name="last133",
    ends={
        Property(name="OclExpression135", type=JTLMM_essentialocl_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_essentialocl_CollectionRange134", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
part136: BinaryAssociation = BinaryAssociation(
    name="part136",
    ends={
        Property(name="essentialocl137", type=JTLMM_essentialocl_TupleLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="TupleLiteralPart", type=TupleLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
context140: BinaryAssociation = BinaryAssociation(
    name="context140",
    ends={
        Property(name="Variable142", type=JTLMM_essentialocl_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_essentialocl_ExpressionInOcl141", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resultVariable143: BinaryAssociation = BinaryAssociation(
    name="resultVariable143",
    ends={
        Property(name="Variable145", type=JTLMM_essentialocl_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_essentialocl_ExpressionInOcl144", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterVariable146: BinaryAssociation = BinaryAssociation(
    name="parameterVariable146",
    ends={
        Property(name="Variable148", type=JTLMM_essentialocl_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_essentialocl_ExpressionInOcl147", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TupleLiteralExp149: BinaryAssociation = BinaryAssociation(
    name="TupleLiteralExp149",
    ends={
        Property(name="essentialocl150", type=JTLMM_essentialocl_TupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="TupleLiteralExp", type=TupleLiteralExp, multiplicity=Multiplicity(0, 1))
    }
)
elementType151: BinaryAssociation = BinaryAssociation(
    name="elementType151",
    ends={
        Property(name="Type152", type=JTLMM_essentialocl_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_essentialocl_CollectionType", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
referredEnumLiteral153: BinaryAssociation = BinaryAssociation(
    name="referredEnumLiteral153",
    ends={
        Property(name="EnumerationLiteral154", type=JTLMM_essentialocl_EnumLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_essentialocl_EnumLiteralExp", type=EnumerationLiteral, multiplicity=Multiplicity(0, 1))
    }
)
where157: BinaryAssociation = BinaryAssociation(
    name="where157",
    ends={
        Property(name="OclExpression159", type=JTLMM_template_TemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_template_TemplateExp158", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
bindsTo155: BinaryAssociation = BinaryAssociation(
    name="bindsTo155",
    ends={
        Property(name="Variable156", type=JTLMM_template_TemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_template_TemplateExp", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
inside161: BinaryAssociation = BinaryAssociation(
    name="inside161",
    ends={
        Property(name="AssignExp", type=JTLMM_template_ObjectTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_template_ObjectTemplateExp", type=AssignExp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
part160: BinaryAssociation = BinaryAssociation(
    name="part160",
    ends={
        Property(name="template", type=JTLMM_template_ObjectTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="PropertyTemplateItem", type=PropertyTemplateItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredCollectionType164: BinaryAssociation = BinaryAssociation(
    name="referredCollectionType164",
    ends={
        Property(name="CollectionType", type=JTLMM_template_CollectionTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_template_CollectionTemplateExp165", type=CollectionType, multiplicity=Multiplicity(0, 1))
    }
)
part162: BinaryAssociation = BinaryAssociation(
    name="part162",
    ends={
        Property(name="OclExpression163", type=JTLMM_template_CollectionTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_template_CollectionTemplateExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value171: BinaryAssociation = BinaryAssociation(
    name="value171",
    ends={
        Property(name="OclExpression172", type=JTLMM_template_PropertyTemplateItem, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_template_PropertyTemplateItem", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
match166: BinaryAssociation = BinaryAssociation(
    name="match166",
    ends={
        Property(name="OclExpression168", type=JTLMM_template_CollectionTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_template_CollectionTemplateExp167", type=OclExpression, multiplicity=Multiplicity(0, 1))
    }
)
objContainer169: BinaryAssociation = BinaryAssociation(
    name="objContainer169",
    ends={
        Property(name="template170", type=JTLMM_template_PropertyTemplateItem, multiplicity=Multiplicity(1, 1)),
        Property(name="ObjectTemplateExp", type=ObjectTemplateExp, multiplicity=Multiplicity(1, 1))
    }
)
target176: BinaryAssociation = BinaryAssociation(
    name="target176",
    ends={
        Property(name="Variable177", type=JTLMM_imperativeocl_ImperativeIterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_imperativeocl_ImperativeIterateExp", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referredProperty173: BinaryAssociation = BinaryAssociation(
    name="referredProperty173",
    ends={
        Property(name="Property175", type=JTLMM_template_PropertyTemplateItem, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_template_PropertyTemplateItem174", type=Property_, multiplicity=Multiplicity(1, 1))
    }
)
left180: BinaryAssociation = BinaryAssociation(
    name="left180",
    ends={
        Property(name="OclExpression182", type=JTLMM_imperativeocl_AssignExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_imperativeocl_AssignExp181", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value178: BinaryAssociation = BinaryAssociation(
    name="value178",
    ends={
        Property(name="OclExpression179", type=JTLMM_imperativeocl_AssignExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_imperativeocl_AssignExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body186: BinaryAssociation = BinaryAssociation(
    name="body186",
    ends={
        Property(name="OclExpression187", type=JTLMM_imperativeocl_BlockExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_imperativeocl_BlockExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
defaultValue183: BinaryAssociation = BinaryAssociation(
    name="defaultValue183",
    ends={
        Property(name="OclExpression185", type=JTLMM_imperativeocl_AssignExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_imperativeocl_AssignExp184", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elsePart189: BinaryAssociation = BinaryAssociation(
    name="elsePart189",
    ends={
        Property(name="OclExpression191", type=JTLMM_imperativeocl_SwitchExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_imperativeocl_SwitchExp190", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
alternativePart188: BinaryAssociation = BinaryAssociation(
    name="alternativePart188",
    ends={
        Property(name="AltExp", type=JTLMM_imperativeocl_SwitchExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_imperativeocl_SwitchExp", type=AltExp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition194: BinaryAssociation = BinaryAssociation(
    name="condition194",
    ends={
        Property(name="OclExpression195", type=JTLMM_imperativeocl_WhileExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_imperativeocl_WhileExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referredVariable192: BinaryAssociation = BinaryAssociation(
    name="referredVariable192",
    ends={
        Property(name="Variable193", type=JTLMM_imperativeocl_VariableInitExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_imperativeocl_VariableInitExp", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnedElement199: BinaryAssociation = BinaryAssociation(
    name="returnedElement199",
    ends={
        Property(name="essentialocl201", type=JTLMM_imperativeocl_ComputeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Variable200", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body196: BinaryAssociation = BinaryAssociation(
    name="body196",
    ends={
        Property(name="OclExpression198", type=JTLMM_imperativeocl_WhileExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_imperativeocl_WhileExp197", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition204: BinaryAssociation = BinaryAssociation(
    name="condition204",
    ends={
        Property(name="OclExpression205", type=JTLMM_imperativeocl_AltExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_imperativeocl_AltExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body202: BinaryAssociation = BinaryAssociation(
    name="body202",
    ends={
        Property(name="OclExpression203", type=JTLMM_imperativeocl_ComputeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_imperativeocl_ComputeExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target209: BinaryAssociation = BinaryAssociation(
    name="target209",
    ends={
        Property(name="OclExpression210", type=JTLMM_imperativeocl_UnlinkExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_imperativeocl_UnlinkExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body206: BinaryAssociation = BinaryAssociation(
    name="body206",
    ends={
        Property(name="OclExpression208", type=JTLMM_imperativeocl_AltExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_imperativeocl_AltExp207", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value214: BinaryAssociation = BinaryAssociation(
    name="value214",
    ends={
        Property(name="OclExpression215", type=JTLMM_imperativeocl_ReturnExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_imperativeocl_ReturnExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
item211: BinaryAssociation = BinaryAssociation(
    name="item211",
    ends={
        Property(name="OclExpression213", type=JTLMM_imperativeocl_UnlinkExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_imperativeocl_UnlinkExp212", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tryBody216: BinaryAssociation = BinaryAssociation(
    name="tryBody216",
    ends={
        Property(name="essentialocl218", type=JTLMM_imperativeocl_TryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="OclExpression217", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exception219: BinaryAssociation = BinaryAssociation(
    name="exception219",
    ends={
        Property(name="Type220", type=JTLMM_imperativeocl_TryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_imperativeocl_TryExp", type=Type, multiplicity=Multiplicity(0, 9999))
    }
)
exceptBody221: BinaryAssociation = BinaryAssociation(
    name="exceptBody221",
    ends={
        Property(name="OclExpression223", type=JTLMM_imperativeocl_TryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_imperativeocl_TryExp222", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
element226: BinaryAssociation = BinaryAssociation(
    name="element226",
    ends={
        Property(name="OclExpression227", type=JTLMM_imperativeocl_TupleExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_imperativeocl_TupleExp", type=OclExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
exception224: BinaryAssociation = BinaryAssociation(
    name="exception224",
    ends={
        Property(name="Type225", type=JTLMM_imperativeocl_RaiseExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_imperativeocl_RaiseExp", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
condition230: BinaryAssociation = BinaryAssociation(
    name="condition230",
    ends={
        Property(name="OclExpression232", type=JTLMM_imperativeocl_Typedef, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_imperativeocl_Typedef231", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
base228: BinaryAssociation = BinaryAssociation(
    name="base228",
    ends={
        Property(name="Type229", type=JTLMM_imperativeocl_Typedef, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_imperativeocl_Typedef", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
argument238: BinaryAssociation = BinaryAssociation(
    name="argument238",
    ends={
        Property(name="OclExpression240", type=JTLMM_imperativeocl_InstantiationExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_imperativeocl_InstantiationExp239", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instantiatedClass233: BinaryAssociation = BinaryAssociation(
    name="instantiatedClass233",
    ends={
        Property(name="Class234", type=JTLMM_imperativeocl_InstantiationExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_imperativeocl_InstantiationExp", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
extent235: BinaryAssociation = BinaryAssociation(
    name="extent235",
    ends={
        Property(name="Variable237", type=JTLMM_imperativeocl_InstantiationExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_imperativeocl_InstantiationExp236", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
part243: BinaryAssociation = BinaryAssociation(
    name="part243",
    ends={
        Property(name="DictLiteralPart", type=JTLMM_imperativeocl_DictLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_imperativeocl_DictLiteralExp", type=DictLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keyType241: BinaryAssociation = BinaryAssociation(
    name="keyType241",
    ends={
        Property(name="Type242", type=JTLMM_imperativeocl_DictionaryType, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_imperativeocl_DictionaryType", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
value246: BinaryAssociation = BinaryAssociation(
    name="value246",
    ends={
        Property(name="OclExpression248", type=JTLMM_imperativeocl_DictLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_imperativeocl_DictLiteralPart247", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
key244: BinaryAssociation = BinaryAssociation(
    name="key244",
    ends={
        Property(name="OclExpression245", type=JTLMM_imperativeocl_DictLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_imperativeocl_DictLiteralPart", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition249: BinaryAssociation = BinaryAssociation(
    name="condition249",
    ends={
        Property(name="OclExpression250", type=JTLMM_imperativeocl_LogExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_imperativeocl_LogExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
element251: BinaryAssociation = BinaryAssociation(
    name="element251",
    ends={
        Property(name="Element253", type=JTLMM_imperativeocl_LogExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_imperativeocl_LogExp252", type=Element, multiplicity=Multiplicity(0, 1))
    }
)
log254: BinaryAssociation = BinaryAssociation(
    name="log254",
    ends={
        Property(name="LogExp", type=JTLMM_imperativeocl_AssertExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_imperativeocl_AssertExp", type=LogExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assertion255: BinaryAssociation = BinaryAssociation(
    name="assertion255",
    ends={
        Property(name="OclExpression257", type=JTLMM_imperativeocl_AssertExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_imperativeocl_AssertExp256", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition258: BinaryAssociation = BinaryAssociation(
    name="condition258",
    ends={
        Property(name="OclExpression259", type=JTLMM_imperativeocl_ImperativeLoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_imperativeocl_ImperativeLoopExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable262: BinaryAssociation = BinaryAssociation(
    name="variable262",
    ends={
        Property(name="Variable263", type=JTLMM_imperativeocl_UnpackExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_imperativeocl_UnpackExp", type=Variable, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
target260: BinaryAssociation = BinaryAssociation(
    name="target260",
    ends={
        Property(name="Variable261", type=JTLMM_imperativeocl_CollectorExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_imperativeocl_CollectorExp", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
part266: BinaryAssociation = BinaryAssociation(
    name="part266",
    ends={
        Property(name="AnonymousTupleLiteralPart", type=JTLMM_imperativeocl_AnonymousTupleLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_imperativeocl_AnonymousTupleLiteralExp", type=AnonymousTupleLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elementType264: BinaryAssociation = BinaryAssociation(
    name="elementType264",
    ends={
        Property(name="Type265", type=JTLMM_imperativeocl_AnonymousTupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_imperativeocl_AnonymousTupleType", type=Type, multiplicity=Multiplicity(0, 9999))
    }
)
value267: BinaryAssociation = BinaryAssociation(
    name="value267",
    ends={
        Property(name="OclExpression268", type=JTLMM_imperativeocl_AnonymousTupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="JTLMM_imperativeocl_AnonymousTupleLiteralPart", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_JTLMM_emof_Class_Type = Generalization(general=Type, specific=JTLMM_emof_Class)
gen_JTLMM_emof_Tag_Element = Generalization(general=Element, specific=JTLMM_emof_Tag)
gen_JTLMM_emof_Enumeration_DataType = Generalization(general=DataType, specific=JTLMM_emof_Enumeration)
gen_JTLMM_emof_NamedElement_Element = Generalization(general=Element, specific=JTLMM_emof_NamedElement)
gen_JTLMM_emof_DataType_Type = Generalization(general=Type, specific=JTLMM_emof_DataType)
gen_JTLMM_emof_Element_Object = Generalization(general=Object, specific=JTLMM_emof_Element)
gen_JTLMM_emof_Package_NamedElement = Generalization(general=NamedElement, specific=JTLMM_emof_Package)
gen_JTLMM_emof_Extent_Object = Generalization(general=Object, specific=JTLMM_emof_Extent)
gen_JTLMM_emof_Operation_emof_MultiplicityElement = Generalization(general=emof_MultiplicityElement, specific=JTLMM_emof_Operation)
gen_JTLMM_emof_Operation_emof_TypedElement = Generalization(general=emof_TypedElement, specific=JTLMM_emof_Operation)
gen_JTLMM_emof_Parameter_emof_MultiplicityElement = Generalization(general=emof_MultiplicityElement, specific=JTLMM_emof_Parameter)
gen_JTLMM_emof_Parameter_emof_TypedElement = Generalization(general=emof_TypedElement, specific=JTLMM_emof_Parameter)
gen_JTLMM_emof_TypedElement_NamedElement = Generalization(general=NamedElement, specific=JTLMM_emof_TypedElement)
gen_JTLMM_emof_PrimitiveType_DataType = Generalization(general=DataType, specific=JTLMM_emof_PrimitiveType)
gen_JTLMM_emof_EnumerationLiteral_NamedElement = Generalization(general=NamedElement, specific=JTLMM_emof_EnumerationLiteral)
gen_JTLMM_emof_Type_NamedElement = Generalization(general=NamedElement, specific=JTLMM_emof_Type)
gen_JTLMM_emof_Property_emof_MultiplicityElement = Generalization(general=emof_MultiplicityElement, specific=JTLMM_emof_Property)
gen_JTLMM_emof_Property_emof_TypedElement = Generalization(general=emof_TypedElement, specific=JTLMM_emof_Property)
gen_JTLMM_JTL_Relation_NamedElement = Generalization(general=NamedElement, specific=JTLMM_JTL_Relation)
gen_JTLMM_emof_URIExtent_Extent = Generalization(general=Extent, specific=JTLMM_emof_URIExtent)
gen_JTLMM_emof_Comment_Element = Generalization(general=Element, specific=JTLMM_emof_Comment)
gen_JTLMM_JTL_Transformation_emof_Class = Generalization(general=emof_Class, specific=JTLMM_JTL_Transformation)
gen_JTLMM_JTL_Transformation_emof_Package = Generalization(general=emof_Package, specific=JTLMM_JTL_Transformation)
gen_JTLMM_JTL_Domain_NamedElement = Generalization(general=NamedElement, specific=JTLMM_JTL_Domain)
gen_JTLMM_JTL_Model_NamedElement = Generalization(general=NamedElement, specific=JTLMM_JTL_Model)
gen_JTLMM_JTL_Pattern_Element = Generalization(general=Element, specific=JTLMM_JTL_Pattern)
gen_JTLMM_JTL_Predicate_Element = Generalization(general=Element, specific=JTLMM_JTL_Predicate)
gen_JTLMM_essentialocl_BooleanLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=JTLMM_essentialocl_BooleanLiteralExp)
gen_JTLMM_essentialocl_CallExp_OclExpression = Generalization(general=OclExpression, specific=JTLMM_essentialocl_CallExp)
gen_JTLMM_essentialocl_IfExp_OclExpression = Generalization(general=OclExpression, specific=JTLMM_essentialocl_IfExp)
gen_JTLMM_essentialocl_OclExpression_TypedElement = Generalization(general=TypedElement, specific=JTLMM_essentialocl_OclExpression)
gen_JTLMM_essentialocl_UnlimitedNaturalExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=JTLMM_essentialocl_UnlimitedNaturalExp)
gen_JTLMM_essentialocl_LetExp_OclExpression = Generalization(general=OclExpression, specific=JTLMM_essentialocl_LetExp)
gen_JTLMM_essentialocl_Variable_TypedElement = Generalization(general=TypedElement, specific=JTLMM_essentialocl_Variable)
gen_JTLMM_essentialocl_LoopExp_essentialocl_CallExp = Generalization(general=essentialocl_CallExp, specific=JTLMM_essentialocl_LoopExp)
gen_JTLMM_essentialocl_LoopExp_essentialocl_OclExpression = Generalization(general=essentialocl_OclExpression, specific=JTLMM_essentialocl_LoopExp)
gen_JTLMM_essentialocl_PropertyCallExp_FeaturePropertyCall = Generalization(general=FeaturePropertyCall, specific=JTLMM_essentialocl_PropertyCallExp)
gen_JTLMM_essentialocl_VariableExp_OclExpression = Generalization(general=OclExpression, specific=JTLMM_essentialocl_VariableExp)
gen_JTLMM_essentialocl_TypeExp_OclExpression = Generalization(general=OclExpression, specific=JTLMM_essentialocl_TypeExp)
gen_JTLMM_essentialocl_RealLiteralExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=JTLMM_essentialocl_RealLiteralExp)
gen_JTLMM_essentialocl_LiteralExp_OclExpression = Generalization(general=OclExpression, specific=JTLMM_essentialocl_LiteralExp)
gen_JTLMM_essentialocl_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=JTLMM_essentialocl_IteratorExp)
gen_JTLMM_essentialocl_StringLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=JTLMM_essentialocl_StringLiteralExp)
gen_JTLMM_essentialocl_IntegerLiteralExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=JTLMM_essentialocl_IntegerLiteralExp)
gen_JTLMM_essentialocl_OperationCallExp_FeaturePropertyCall = Generalization(general=FeaturePropertyCall, specific=JTLMM_essentialocl_OperationCallExp)
gen_JTLMM_essentialocl_CollectionItem_CollectionLiteralPart = Generalization(general=CollectionLiteralPart, specific=JTLMM_essentialocl_CollectionItem)
gen_JTLMM_essentialocl_IterateExp_LoopExp = Generalization(general=LoopExp, specific=JTLMM_essentialocl_IterateExp)
gen_JTLMM_essentialocl_PrimitiveLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=JTLMM_essentialocl_PrimitiveLiteralExp)
gen_JTLMM_essentialocl_NumericLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=JTLMM_essentialocl_NumericLiteralExp)
gen_JTLMM_essentialocl_CollectionLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=JTLMM_essentialocl_CollectionLiteralExp)
gen_JTLMM_essentialocl_CollectionLiteralPart_TypedElement = Generalization(general=TypedElement, specific=JTLMM_essentialocl_CollectionLiteralPart)
gen_JTLMM_essentialocl_NullLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=JTLMM_essentialocl_NullLiteralExp)
gen_JTLMM_essentialocl_ExpressionInOcl_OpaqueExpression = Generalization(general=OpaqueExpression, specific=JTLMM_essentialocl_ExpressionInOcl)
gen_JTLMM_essentialocl_CollectionRange_CollectionLiteralPart = Generalization(general=CollectionLiteralPart, specific=JTLMM_essentialocl_CollectionRange)
gen_JTLMM_essentialocl_TupleLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=JTLMM_essentialocl_TupleLiteralExp)
gen_JTLMM_essentialocl_BagType_CollectionType = Generalization(general=CollectionType, specific=JTLMM_essentialocl_BagType)
gen_JTLMM_essentialocl_CollectionType_DataType = Generalization(general=DataType, specific=JTLMM_essentialocl_CollectionType)
gen_JTLMM_essentialocl_InvalidLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=JTLMM_essentialocl_InvalidLiteralExp)
gen_JTLMM_essentialocl_FeaturePropertyCall_CallExp = Generalization(general=CallExp, specific=JTLMM_essentialocl_FeaturePropertyCall)
gen_JTLMM_essentialocl_TupleLiteralPart_TypedElement = Generalization(general=TypedElement, specific=JTLMM_essentialocl_TupleLiteralPart)
gen_JTLMM_essentialocl_InvalidType_Type = Generalization(general=Type, specific=JTLMM_essentialocl_InvalidType)
gen_JTLMM_essentialocl_EnumLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=JTLMM_essentialocl_EnumLiteralExp)
gen_JTLMM_essentialocl_VoidType_Type = Generalization(general=Type, specific=JTLMM_essentialocl_VoidType)
gen_JTLMM_essentialocl_AnyType_emof_Class = Generalization(general=emof_Class, specific=JTLMM_essentialocl_AnyType)
gen_JTLMM_essentialocl_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=JTLMM_essentialocl_OrderedSetType)
gen_JTLMM_essentialocl_SequenceType_CollectionType = Generalization(general=CollectionType, specific=JTLMM_essentialocl_SequenceType)
gen_JTLMM_essentialocl_SetType_CollectionType = Generalization(general=CollectionType, specific=JTLMM_essentialocl_SetType)
gen_JTLMM_essentialocl_TupleType_emof_Class = Generalization(general=emof_Class, specific=JTLMM_essentialocl_TupleType)
gen_JTLMM_essentialocl_TupleType_emof_DataType = Generalization(general=emof_DataType, specific=JTLMM_essentialocl_TupleType)
gen_JTLMM_essentialocl_AnyType_emof_Type = Generalization(general=emof_Type, specific=JTLMM_essentialocl_AnyType)
gen_JTLMM_template_TemplateExp_LiteralExp = Generalization(general=LiteralExp, specific=JTLMM_template_TemplateExp)
gen_JTLMM_template_ObjectTemplateExp_TemplateExp = Generalization(general=TemplateExp, specific=JTLMM_template_ObjectTemplateExp)
gen_JTLMM_template_CollectionTemplateExp_TemplateExp = Generalization(general=TemplateExp, specific=JTLMM_template_CollectionTemplateExp)
gen_JTLMM_template_PropertyTemplateItem_Element = Generalization(general=Element, specific=JTLMM_template_PropertyTemplateItem)
gen_JTLMM_imperativeocl_ImperativeIterateExp_ImperativeLoopExp = Generalization(general=ImperativeLoopExp, specific=JTLMM_imperativeocl_ImperativeIterateExp)
gen_JTLMM_imperativeocl_AssignExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTLMM_imperativeocl_AssignExp)
gen_JTLMM_imperativeocl_BlockExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTLMM_imperativeocl_BlockExp)
gen_JTLMM_imperativeocl_SwitchExp_essentialocl_CallExp = Generalization(general=essentialocl_CallExp, specific=JTLMM_imperativeocl_SwitchExp)
gen_JTLMM_imperativeocl_SwitchExp_imperativeocl_ImperativeExpression = Generalization(general=imperativeocl_ImperativeExpression, specific=JTLMM_imperativeocl_SwitchExp)
gen_JTLMM_imperativeocl_WhileExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTLMM_imperativeocl_WhileExp)
gen_JTLMM_imperativeocl_VariableInitExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTLMM_imperativeocl_VariableInitExp)
gen_JTLMM_imperativeocl_ComputeExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTLMM_imperativeocl_ComputeExp)
gen_JTLMM_imperativeocl_AltExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTLMM_imperativeocl_AltExp)
gen_JTLMM_imperativeocl_UnlinkExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTLMM_imperativeocl_UnlinkExp)
gen_JTLMM_imperativeocl_ReturnExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTLMM_imperativeocl_ReturnExp)
gen_JTLMM_imperativeocl_BreakExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTLMM_imperativeocl_BreakExp)
gen_JTLMM_imperativeocl_TryExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTLMM_imperativeocl_TryExp)
gen_JTLMM_imperativeocl_RaiseExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTLMM_imperativeocl_RaiseExp)
gen_JTLMM_imperativeocl_ContinueExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTLMM_imperativeocl_ContinueExp)
gen_JTLMM_imperativeocl_ForExp_ImperativeLoopExp = Generalization(general=ImperativeLoopExp, specific=JTLMM_imperativeocl_ForExp)
gen_JTLMM_imperativeocl_TupleExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTLMM_imperativeocl_TupleExp)
gen_JTLMM_imperativeocl_Typedef_Class = Generalization(general=Class_, specific=JTLMM_imperativeocl_Typedef)
gen_JTLMM_imperativeocl_InstantiationExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTLMM_imperativeocl_InstantiationExp)
gen_JTLMM_imperativeocl_DictLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=JTLMM_imperativeocl_DictLiteralExp)
gen_JTLMM_imperativeocl_DictionaryType_CollectionType = Generalization(general=CollectionType, specific=JTLMM_imperativeocl_DictionaryType)
gen_JTLMM_imperativeocl_DictLiteralPart_Element = Generalization(general=Element, specific=JTLMM_imperativeocl_DictLiteralPart)
gen_JTLMM_imperativeocl_TemplateParameterType_Type = Generalization(general=Type, specific=JTLMM_imperativeocl_TemplateParameterType)
gen_JTLMM_imperativeocl_LogExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTLMM_imperativeocl_LogExp)
gen_JTLMM_imperativeocl_AssertExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTLMM_imperativeocl_AssertExp)
gen_JTLMM_imperativeocl_ImperativeLoopExp_essentialocl_LoopExp = Generalization(general=essentialocl_LoopExp, specific=JTLMM_imperativeocl_ImperativeLoopExp)
gen_JTLMM_imperativeocl_ImperativeLoopExp_imperativeocl_ImperativeExpression = Generalization(general=imperativeocl_ImperativeExpression, specific=JTLMM_imperativeocl_ImperativeLoopExp)
gen_JTLMM_imperativeocl_UnpackExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTLMM_imperativeocl_UnpackExp)
gen_JTLMM_imperativeocl_CollectorExp_ImperativeLoopExp = Generalization(general=ImperativeLoopExp, specific=JTLMM_imperativeocl_CollectorExp)
gen_JTLMM_imperativeocl_ImperativeExpression_OclExpression = Generalization(general=OclExpression, specific=JTLMM_imperativeocl_ImperativeExpression)
gen_JTLMM_imperativeocl_AnonymousTupleLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=JTLMM_imperativeocl_AnonymousTupleLiteralExp)
gen_JTLMM_imperativeocl_AnonymousTupleType_Class = Generalization(general=Class_, specific=JTLMM_imperativeocl_AnonymousTupleType)
gen_JTLMM_imperativeocl_AnonymousTupleLiteralPart_Element = Generalization(general=Element, specific=JTLMM_imperativeocl_AnonymousTupleLiteralPart)
gen_JTLMM_imperativeocl_ListType_CollectionType = Generalization(general=CollectionType, specific=JTLMM_imperativeocl_ListType)

# Domain Model
domain_model = DomainModel(
    name="JTLMM",
    types={JTLMM_emof_Class, Type, Property_, Operation, Class_, JTLMM_emof_Tag, Element, JTLMM_emof_Enumeration, DataType, EnumerationLiteral, JTLMM_emof_NamedElement, JTLMM_emof_DataType, JTLMM_emof_Element, Object, Tag, Comment, Parameter_, JTLMM_emof_MultiplicityElement, JTLMM_emof_Package, NamedElement, JTLMM_emof_Extent, JTLMM_emof_Object, JTLMM_emof_Operation, emof_MultiplicityElement, emof_TypedElement, JTLMM_emof_Parameter, JTLMM_emof_TypedElement, Package, JTLMM_emof_PrimitiveType, JTLMM_emof_EnumerationLiteral, JTLMM_emof_Type, Enumeration_, JTLMM_emof_Property, Relation, JTLMM_JTL_Relation, JTLMM_emof_URIExtent, Extent, JTLMM_emof_Comment, JTLMM_JTL_Transformation, emof_Class, emof_Package, Model, Pattern, Transformation, Domain, JTLMM_JTL_Domain, Variable, JTLMM_JTL_Model, Predicate, JTLMM_JTL_Pattern, JTLMM_JTL_Predicate, TemplateExp, JTLMM_essentialocl_BooleanLiteralExp, PrimitiveLiteralExp, OclExpression, JTLMM_essentialocl_OclExpression, JTLMM_essentialocl_CallExp, JTLMM_essentialocl_IfExp, TypedElement, TryExp, JTLMM_essentialocl_UnlimitedNaturalExp, NumericLiteralExp, LetExp, JTLMM_essentialocl_LetExp, JTLMM_essentialocl_Variable, JTLMM_essentialocl_LoopExp, essentialocl_CallExp, essentialocl_OclExpression, ComputeExp, JTLMM_essentialocl_PropertyCallExp, FeaturePropertyCall, JTLMM_essentialocl_VariableExp, JTLMM_essentialocl_TypeExp, JTLMM_essentialocl_RealLiteralExp, JTLMM_essentialocl_LiteralExp, JTLMM_essentialocl_IteratorExp, LoopExp, JTLMM_essentialocl_StringLiteralExp, JTLMM_essentialocl_IntegerLiteralExp, JTLMM_essentialocl_OperationCallExp, JTLMM_essentialocl_CollectionItem, JTLMM_essentialocl_IterateExp, JTLMM_essentialocl_PrimitiveLiteralExp, LiteralExp, JTLMM_essentialocl_NumericLiteralExp, JTLMM_essentialocl_CollectionLiteralExp, CollectionLiteralPart, JTLMM_essentialocl_CollectionLiteralPart, CollectionLiteralExp, JTLMM_essentialocl_NullLiteralExp, JTLMM_essentialocl_ExpressionInOcl, OpaqueExpression, JTLMM_essentialocl_CollectionRange, JTLMM_essentialocl_TupleLiteralExp, TupleLiteralPart, JTLMM_essentialocl_BagType, CollectionType, JTLMM_essentialocl_CollectionType, JTLMM_essentialocl_OpaqueExpression, JTLMM_essentialocl_InvalidLiteralExp, JTLMM_essentialocl_FeaturePropertyCall, CallExp, JTLMM_essentialocl_TupleLiteralPart, TupleLiteralExp, JTLMM_essentialocl_InvalidType, JTLMM_essentialocl_OrderedSetType, JTLMM_essentialocl_EnumLiteralExp, JTLMM_essentialocl_VoidType, JTLMM_essentialocl_AnyType, emof_Type, JTLMM_essentialocl_SequenceType, JTLMM_essentialocl_SetType, JTLMM_essentialocl_TupleType, emof_DataType, JTLMM_template_TemplateExp, AssignExp, JTLMM_template_ObjectTemplateExp, PropertyTemplateItem, JTLMM_template_CollectionTemplateExp, JTLMM_template_PropertyTemplateItem, ObjectTemplateExp, JTLMM_imperativeocl_ImperativeIterateExp, ImperativeLoopExp, JTLMM_imperativeocl_AssignExp, ImperativeExpression, JTLMM_imperativeocl_BlockExp, JTLMM_imperativeocl_SwitchExp, imperativeocl_ImperativeExpression, AltExp, JTLMM_imperativeocl_VariableInitExp, JTLMM_imperativeocl_WhileExp, JTLMM_imperativeocl_ComputeExp, JTLMM_imperativeocl_AltExp, JTLMM_imperativeocl_UnlinkExp, JTLMM_imperativeocl_ReturnExp, JTLMM_imperativeocl_BreakExp, JTLMM_imperativeocl_TryExp, JTLMM_imperativeocl_RaiseExp, JTLMM_imperativeocl_ContinueExp, JTLMM_imperativeocl_ForExp, JTLMM_imperativeocl_TupleExp, JTLMM_imperativeocl_Typedef, JTLMM_imperativeocl_InstantiationExp, DictLiteralPart, JTLMM_imperativeocl_DictionaryType, JTLMM_imperativeocl_DictLiteralExp, JTLMM_imperativeocl_DictLiteralPart, JTLMM_imperativeocl_TemplateParameterType, JTLMM_imperativeocl_LogExp, LogExp, JTLMM_imperativeocl_AssertExp, JTLMM_imperativeocl_CollectorExp, JTLMM_imperativeocl_ImperativeLoopExp, essentialocl_LoopExp, JTLMM_imperativeocl_UnpackExp, JTLMM_imperativeocl_ImperativeExpression, JTLMM_imperativeocl_AnonymousTupleLiteralExp, AnonymousTupleLiteralPart, JTLMM_imperativeocl_AnonymousTupleType, JTLMM_imperativeocl_AnonymousTupleLiteralPart, JTLMM_imperativeocl_ListType, CollectionKind, SeverityKind},
    associations={ownedAttribute0, ownedOperation1, superClass3, element7, ownedLiteral9, tag4, ownedComment6, ownedParameter14, raisedException16, class11, package21, ownedType17, nestedPackage20, operation24, enumeration27, Class29, opposite32, relation36, annotatedElement34, modelParameter35, where42, transformation38, domain40, when44, variable47, model53, relation48, pattern51, dependsOn62, rootVariable56, transformation59, predicate70, whereOwner64, whenOwner67, domain76, bindsTo72, templateExpression74, pattern79, conditionExpression82, source83, tryBodyOwner85, elseExpression91, condition86, thenExpression88, initExpression98, LetExp100, in94, variable96, body113, bindParameter102, computeOwner105, referredProperty107, referredVariable109, referredType111, referredOperation120, iterator115, argument118, CollectionLiteralExp127, item129, result123, part125, bodyExpression138, first131, last133, part136, context140, resultVariable143, parameterVariable146, TupleLiteralExp149, elementType151, referredEnumLiteral153, where157, bindsTo155, inside161, part160, referredCollectionType164, part162, value171, match166, objContainer169, target176, referredProperty173, left180, value178, body186, defaultValue183, elsePart189, alternativePart188, condition194, referredVariable192, returnedElement199, body196, condition204, body202, target209, body206, value214, item211, tryBody216, exception219, exceptBody221, element226, exception224, condition230, base228, argument238, instantiatedClass233, extent235, part243, keyType241, value246, key244, condition249, element251, log254, assertion255, condition258, variable262, target260, part266, elementType264, value267},
    generalizations={gen_JTLMM_emof_Class_Type, gen_JTLMM_emof_Tag_Element, gen_JTLMM_emof_Enumeration_DataType, gen_JTLMM_emof_NamedElement_Element, gen_JTLMM_emof_DataType_Type, gen_JTLMM_emof_Element_Object, gen_JTLMM_emof_Package_NamedElement, gen_JTLMM_emof_Extent_Object, gen_JTLMM_emof_Operation_emof_MultiplicityElement, gen_JTLMM_emof_Operation_emof_TypedElement, gen_JTLMM_emof_Parameter_emof_MultiplicityElement, gen_JTLMM_emof_Parameter_emof_TypedElement, gen_JTLMM_emof_TypedElement_NamedElement, gen_JTLMM_emof_PrimitiveType_DataType, gen_JTLMM_emof_EnumerationLiteral_NamedElement, gen_JTLMM_emof_Type_NamedElement, gen_JTLMM_emof_Property_emof_MultiplicityElement, gen_JTLMM_emof_Property_emof_TypedElement, gen_JTLMM_JTL_Relation_NamedElement, gen_JTLMM_emof_URIExtent_Extent, gen_JTLMM_emof_Comment_Element, gen_JTLMM_JTL_Transformation_emof_Class, gen_JTLMM_JTL_Transformation_emof_Package, gen_JTLMM_JTL_Domain_NamedElement, gen_JTLMM_JTL_Model_NamedElement, gen_JTLMM_JTL_Pattern_Element, gen_JTLMM_JTL_Predicate_Element, gen_JTLMM_essentialocl_BooleanLiteralExp_PrimitiveLiteralExp, gen_JTLMM_essentialocl_CallExp_OclExpression, gen_JTLMM_essentialocl_IfExp_OclExpression, gen_JTLMM_essentialocl_OclExpression_TypedElement, gen_JTLMM_essentialocl_UnlimitedNaturalExp_NumericLiteralExp, gen_JTLMM_essentialocl_LetExp_OclExpression, gen_JTLMM_essentialocl_Variable_TypedElement, gen_JTLMM_essentialocl_LoopExp_essentialocl_CallExp, gen_JTLMM_essentialocl_LoopExp_essentialocl_OclExpression, gen_JTLMM_essentialocl_PropertyCallExp_FeaturePropertyCall, gen_JTLMM_essentialocl_VariableExp_OclExpression, gen_JTLMM_essentialocl_TypeExp_OclExpression, gen_JTLMM_essentialocl_RealLiteralExp_NumericLiteralExp, gen_JTLMM_essentialocl_LiteralExp_OclExpression, gen_JTLMM_essentialocl_IteratorExp_LoopExp, gen_JTLMM_essentialocl_StringLiteralExp_PrimitiveLiteralExp, gen_JTLMM_essentialocl_IntegerLiteralExp_NumericLiteralExp, gen_JTLMM_essentialocl_OperationCallExp_FeaturePropertyCall, gen_JTLMM_essentialocl_CollectionItem_CollectionLiteralPart, gen_JTLMM_essentialocl_IterateExp_LoopExp, gen_JTLMM_essentialocl_PrimitiveLiteralExp_LiteralExp, gen_JTLMM_essentialocl_NumericLiteralExp_PrimitiveLiteralExp, gen_JTLMM_essentialocl_CollectionLiteralExp_LiteralExp, gen_JTLMM_essentialocl_CollectionLiteralPart_TypedElement, gen_JTLMM_essentialocl_NullLiteralExp_LiteralExp, gen_JTLMM_essentialocl_ExpressionInOcl_OpaqueExpression, gen_JTLMM_essentialocl_CollectionRange_CollectionLiteralPart, gen_JTLMM_essentialocl_TupleLiteralExp_LiteralExp, gen_JTLMM_essentialocl_BagType_CollectionType, gen_JTLMM_essentialocl_CollectionType_DataType, gen_JTLMM_essentialocl_InvalidLiteralExp_LiteralExp, gen_JTLMM_essentialocl_FeaturePropertyCall_CallExp, gen_JTLMM_essentialocl_TupleLiteralPart_TypedElement, gen_JTLMM_essentialocl_InvalidType_Type, gen_JTLMM_essentialocl_EnumLiteralExp_LiteralExp, gen_JTLMM_essentialocl_VoidType_Type, gen_JTLMM_essentialocl_AnyType_emof_Class, gen_JTLMM_essentialocl_OrderedSetType_CollectionType, gen_JTLMM_essentialocl_SequenceType_CollectionType, gen_JTLMM_essentialocl_SetType_CollectionType, gen_JTLMM_essentialocl_TupleType_emof_Class, gen_JTLMM_essentialocl_TupleType_emof_DataType, gen_JTLMM_essentialocl_AnyType_emof_Type, gen_JTLMM_template_TemplateExp_LiteralExp, gen_JTLMM_template_ObjectTemplateExp_TemplateExp, gen_JTLMM_template_CollectionTemplateExp_TemplateExp, gen_JTLMM_template_PropertyTemplateItem_Element, gen_JTLMM_imperativeocl_ImperativeIterateExp_ImperativeLoopExp, gen_JTLMM_imperativeocl_AssignExp_ImperativeExpression, gen_JTLMM_imperativeocl_BlockExp_ImperativeExpression, gen_JTLMM_imperativeocl_SwitchExp_essentialocl_CallExp, gen_JTLMM_imperativeocl_SwitchExp_imperativeocl_ImperativeExpression, gen_JTLMM_imperativeocl_WhileExp_ImperativeExpression, gen_JTLMM_imperativeocl_VariableInitExp_ImperativeExpression, gen_JTLMM_imperativeocl_ComputeExp_ImperativeExpression, gen_JTLMM_imperativeocl_AltExp_ImperativeExpression, gen_JTLMM_imperativeocl_UnlinkExp_ImperativeExpression, gen_JTLMM_imperativeocl_ReturnExp_ImperativeExpression, gen_JTLMM_imperativeocl_BreakExp_ImperativeExpression, gen_JTLMM_imperativeocl_TryExp_ImperativeExpression, gen_JTLMM_imperativeocl_RaiseExp_ImperativeExpression, gen_JTLMM_imperativeocl_ContinueExp_ImperativeExpression, gen_JTLMM_imperativeocl_ForExp_ImperativeLoopExp, gen_JTLMM_imperativeocl_TupleExp_ImperativeExpression, gen_JTLMM_imperativeocl_Typedef_Class, gen_JTLMM_imperativeocl_InstantiationExp_ImperativeExpression, gen_JTLMM_imperativeocl_DictLiteralExp_LiteralExp, gen_JTLMM_imperativeocl_DictionaryType_CollectionType, gen_JTLMM_imperativeocl_DictLiteralPart_Element, gen_JTLMM_imperativeocl_TemplateParameterType_Type, gen_JTLMM_imperativeocl_LogExp_ImperativeExpression, gen_JTLMM_imperativeocl_AssertExp_ImperativeExpression, gen_JTLMM_imperativeocl_ImperativeLoopExp_essentialocl_LoopExp, gen_JTLMM_imperativeocl_ImperativeLoopExp_imperativeocl_ImperativeExpression, gen_JTLMM_imperativeocl_UnpackExp_ImperativeExpression, gen_JTLMM_imperativeocl_CollectorExp_ImperativeLoopExp, gen_JTLMM_imperativeocl_ImperativeExpression_OclExpression, gen_JTLMM_imperativeocl_AnonymousTupleLiteralExp_LiteralExp, gen_JTLMM_imperativeocl_AnonymousTupleType_Class, gen_JTLMM_imperativeocl_AnonymousTupleLiteralPart_Element, gen_JTLMM_imperativeocl_ListType_CollectionType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)