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
Class_ = Class(name="Class")
JTL_emof_DataType = Class(name="JTL_emof_DataType", is_abstract=True)
JTL_emof_Element = Class(name="JTL_emof_Element", is_abstract=True)
Object = Class(name="Object")
Tag = Class(name="Tag")
Comment = Class(name="Comment")
JTL_emof_Tag = Class(name="JTL_emof_Tag")
Element = Class(name="Element")
JTL_emof_Enumeration = Class(name="JTL_emof_Enumeration")
DataType = Class(name="DataType")
EnumerationLiteral = Class(name="EnumerationLiteral")
JTL_emof_NamedElement = Class(name="JTL_emof_NamedElement", is_abstract=True)
JTL_emof_Class = Class(name="JTL_emof_Class")
Type = Class(name="Type")
Property_ = Class(name="Property")
JTL_emof_Package = Class(name="JTL_emof_Package")
NamedElement = Class(name="NamedElement")
Package = Class(name="Package")
JTL_emof_Type = Class(name="JTL_emof_Type", is_abstract=True)
JTL_emof_Parameter = Class(name="JTL_emof_Parameter")
JTL_emof_EnumerationLiteral = Class(name="JTL_emof_EnumerationLiteral")
Enumeration_ = Class(name="Enumeration")
JTL_emof_Property = Class(name="JTL_emof_Property")
JTL_emof_Extent = Class(name="JTL_emof_Extent")
JTL_emof_Object = Class(name="JTL_emof_Object")
JTL_emof_Operation = Class(name="JTL_emof_Operation")
emof_MultiplicityElement = Class(name="emof_MultiplicityElement")
emof_TypedElement = Class(name="emof_TypedElement")
Parameter_ = Class(name="Parameter")
JTL_emof_MultiplicityElement = Class(name="JTL_emof_MultiplicityElement", is_abstract=True)
JTL_JTL_Relation = Class(name="JTL_JTL_Relation")
Transformation = Class(name="Transformation")
Domain = Class(name="Domain")
Where = Class(name="Where")
When = Class(name="When")
Variable = Class(name="Variable")
JTL_JTL_Domain = Class(name="JTL_JTL_Domain")
Pattern = Class(name="Pattern")
JTL_JTL_Model = Class(name="JTL_JTL_Model")
JTL_emof_TypedElement = Class(name="JTL_emof_TypedElement", is_abstract=True)
JTL_emof_PrimitiveType = Class(name="JTL_emof_PrimitiveType")
JTL_emof_URIExtent = Class(name="JTL_emof_URIExtent")
Extent = Class(name="Extent")
JTL_emof_Comment = Class(name="JTL_emof_Comment")
JTL_JTL_Transformation = Class(name="JTL_JTL_Transformation")
emof_Class = Class(name="emof_Class")
emof_Package = Class(name="emof_Package")
Model = Class(name="Model")
Relation = Class(name="Relation")
JTL_essentialocl_BooleanLiteralExp = Class(name="JTL_essentialocl_BooleanLiteralExp")
PrimitiveLiteralExp = Class(name="PrimitiveLiteralExp")
JTL_essentialocl_CallExp = Class(name="JTL_essentialocl_CallExp", is_abstract=True)
JTL_essentialocl_OclExpression = Class(name="JTL_essentialocl_OclExpression", is_abstract=True)
TypedElement = Class(name="TypedElement")
TryExp = Class(name="TryExp")
JTL_essentialocl_UnlimitedNaturalExp = Class(name="JTL_essentialocl_UnlimitedNaturalExp")
NumericLiteralExp = Class(name="NumericLiteralExp")
JTL_essentialocl_IfExp = Class(name="JTL_essentialocl_IfExp")
JTL_JTL_Pattern = Class(name="JTL_JTL_Pattern")
Predicate = Class(name="Predicate")
TemplateExp = Class(name="TemplateExp")
JTL_JTL_Predicate = Class(name="JTL_JTL_Predicate")
OclExpression = Class(name="OclExpression")
JTL_JTL_When = Class(name="JTL_JTL_When")
JTL_JTL_Where = Class(name="JTL_JTL_Where")
JTL_essentialocl_VariableExp = Class(name="JTL_essentialocl_VariableExp")
JTL_essentialocl_TypeExp = Class(name="JTL_essentialocl_TypeExp")
JTL_essentialocl_LoopExp = Class(name="JTL_essentialocl_LoopExp", is_abstract=True)
essentialocl_CallExp = Class(name="essentialocl_CallExp")
essentialocl_OclExpression = Class(name="essentialocl_OclExpression")
JTL_essentialocl_IteratorExp = Class(name="JTL_essentialocl_IteratorExp")
LoopExp = Class(name="LoopExp")
JTL_essentialocl_StringLiteralExp = Class(name="JTL_essentialocl_StringLiteralExp")
JTL_essentialocl_IntegerLiteralExp = Class(name="JTL_essentialocl_IntegerLiteralExp")
JTL_essentialocl_OperationCallExp = Class(name="JTL_essentialocl_OperationCallExp")
JTL_essentialocl_LetExp = Class(name="JTL_essentialocl_LetExp")
JTL_essentialocl_Variable = Class(name="JTL_essentialocl_Variable")
LetExp = Class(name="LetExp")
ComputeExp = Class(name="ComputeExp")
JTL_essentialocl_PropertyCallExp = Class(name="JTL_essentialocl_PropertyCallExp")
FeaturePropertyCall = Class(name="FeaturePropertyCall")
JTL_essentialocl_CollectionItem = Class(name="JTL_essentialocl_CollectionItem")
JTL_essentialocl_CollectionRange = Class(name="JTL_essentialocl_CollectionRange")
JTL_essentialocl_TupleLiteralExp = Class(name="JTL_essentialocl_TupleLiteralExp")
TupleLiteralPart = Class(name="TupleLiteralPart")
JTL_essentialocl_NullLiteralExp = Class(name="JTL_essentialocl_NullLiteralExp")
JTL_essentialocl_ExpressionInOcl = Class(name="JTL_essentialocl_ExpressionInOcl")
OpaqueExpression = Class(name="OpaqueExpression")
JTL_essentialocl_RealLiteralExp = Class(name="JTL_essentialocl_RealLiteralExp")
JTL_essentialocl_LiteralExp = Class(name="JTL_essentialocl_LiteralExp", is_abstract=True)
JTL_essentialocl_IterateExp = Class(name="JTL_essentialocl_IterateExp")
JTL_essentialocl_PrimitiveLiteralExp = Class(name="JTL_essentialocl_PrimitiveLiteralExp", is_abstract=True)
LiteralExp = Class(name="LiteralExp")
JTL_essentialocl_NumericLiteralExp = Class(name="JTL_essentialocl_NumericLiteralExp", is_abstract=True)
JTL_essentialocl_CollectionLiteralExp = Class(name="JTL_essentialocl_CollectionLiteralExp")
CollectionLiteralPart = Class(name="CollectionLiteralPart")
JTL_essentialocl_CollectionLiteralPart = Class(name="JTL_essentialocl_CollectionLiteralPart", is_abstract=True)
CollectionLiteralExp = Class(name="CollectionLiteralExp")
JTL_essentialocl_InvalidType = Class(name="JTL_essentialocl_InvalidType")
JTL_essentialocl_OrderedSetType = Class(name="JTL_essentialocl_OrderedSetType")
JTL_essentialocl_SequenceType = Class(name="JTL_essentialocl_SequenceType")
JTL_essentialocl_SetType = Class(name="JTL_essentialocl_SetType")
JTL_essentialocl_TupleType = Class(name="JTL_essentialocl_TupleType")
emof_DataType = Class(name="emof_DataType")
JTL_essentialocl_VoidType = Class(name="JTL_essentialocl_VoidType")
JTL_essentialocl_AnyType = Class(name="JTL_essentialocl_AnyType")
emof_Type = Class(name="emof_Type")
JTL_template_TemplateExp = Class(name="JTL_template_TemplateExp", is_abstract=True)
JTL_essentialocl_OpaqueExpression = Class(name="JTL_essentialocl_OpaqueExpression")
JTL_essentialocl_InvalidLiteralExp = Class(name="JTL_essentialocl_InvalidLiteralExp")
JTL_essentialocl_FeaturePropertyCall = Class(name="JTL_essentialocl_FeaturePropertyCall", is_abstract=True)
CallExp = Class(name="CallExp")
JTL_essentialocl_TupleLiteralPart = Class(name="JTL_essentialocl_TupleLiteralPart")
TupleLiteralExp = Class(name="TupleLiteralExp")
JTL_essentialocl_BagType = Class(name="JTL_essentialocl_BagType")
CollectionType = Class(name="CollectionType")
JTL_essentialocl_CollectionType = Class(name="JTL_essentialocl_CollectionType", is_abstract=True)
JTL_essentialocl_EnumLiteralExp = Class(name="JTL_essentialocl_EnumLiteralExp")
JTL_template_PropertyTemplateItem = Class(name="JTL_template_PropertyTemplateItem")
ObjectTemplateExp = Class(name="ObjectTemplateExp")
JTL_imperativeocl_ImperativeIterateExp = Class(name="JTL_imperativeocl_ImperativeIterateExp")
ImperativeLoopExp = Class(name="ImperativeLoopExp")
JTL_imperativeocl_AssignExp = Class(name="JTL_imperativeocl_AssignExp")
ImperativeExpression = Class(name="ImperativeExpression")
JTL_template_ObjectTemplateExp = Class(name="JTL_template_ObjectTemplateExp")
PropertyTemplateItem = Class(name="PropertyTemplateItem")
AssignExp = Class(name="AssignExp")
JTL_template_CollectionTemplateExp = Class(name="JTL_template_CollectionTemplateExp")
JTL_imperativeocl_WhileExp = Class(name="JTL_imperativeocl_WhileExp")
JTL_imperativeocl_ComputeExp = Class(name="JTL_imperativeocl_ComputeExp")
JTL_imperativeocl_AltExp = Class(name="JTL_imperativeocl_AltExp")
JTL_imperativeocl_UnlinkExp = Class(name="JTL_imperativeocl_UnlinkExp")
JTL_imperativeocl_BlockExp = Class(name="JTL_imperativeocl_BlockExp")
JTL_imperativeocl_SwitchExp = Class(name="JTL_imperativeocl_SwitchExp")
imperativeocl_ImperativeExpression = Class(name="imperativeocl_ImperativeExpression")
AltExp = Class(name="AltExp")
JTL_imperativeocl_VariableInitExp = Class(name="JTL_imperativeocl_VariableInitExp")
JTL_imperativeocl_RaiseExp = Class(name="JTL_imperativeocl_RaiseExp")
JTL_imperativeocl_ContinueExp = Class(name="JTL_imperativeocl_ContinueExp")
JTL_imperativeocl_ForExp = Class(name="JTL_imperativeocl_ForExp")
JTL_imperativeocl_TupleExp = Class(name="JTL_imperativeocl_TupleExp")
JTL_imperativeocl_Typedef = Class(name="JTL_imperativeocl_Typedef")
JTL_imperativeocl_InstantiationExp = Class(name="JTL_imperativeocl_InstantiationExp")
JTL_imperativeocl_ReturnExp = Class(name="JTL_imperativeocl_ReturnExp")
JTL_imperativeocl_BreakExp = Class(name="JTL_imperativeocl_BreakExp")
JTL_imperativeocl_TryExp = Class(name="JTL_imperativeocl_TryExp")
JTL_imperativeocl_AssertExp = Class(name="JTL_imperativeocl_AssertExp")
LogExp = Class(name="LogExp")
JTL_imperativeocl_ImperativeLoopExp = Class(name="JTL_imperativeocl_ImperativeLoopExp", is_abstract=True)
essentialocl_LoopExp = Class(name="essentialocl_LoopExp")
JTL_imperativeocl_CollectorExp = Class(name="JTL_imperativeocl_CollectorExp")
JTL_imperativeocl_ImperativeExpression = Class(name="JTL_imperativeocl_ImperativeExpression", is_abstract=True)
JTL_imperativeocl_UnpackExp = Class(name="JTL_imperativeocl_UnpackExp")
JTL_imperativeocl_DictionaryType = Class(name="JTL_imperativeocl_DictionaryType")
JTL_imperativeocl_DictLiteralExp = Class(name="JTL_imperativeocl_DictLiteralExp")
DictLiteralPart = Class(name="DictLiteralPart")
JTL_imperativeocl_DictLiteralPart = Class(name="JTL_imperativeocl_DictLiteralPart")
JTL_imperativeocl_TemplateParameterType = Class(name="JTL_imperativeocl_TemplateParameterType")
JTL_imperativeocl_LogExp = Class(name="JTL_imperativeocl_LogExp")
JTL_imperativeocl_AnonymousTupleType = Class(name="JTL_imperativeocl_AnonymousTupleType")
JTL_imperativeocl_AnonymousTupleLiteralExp = Class(name="JTL_imperativeocl_AnonymousTupleLiteralExp")
AnonymousTupleLiteralPart = Class(name="AnonymousTupleLiteralPart")
JTL_imperativeocl_AnonymousTupleLiteralPart = Class(name="JTL_imperativeocl_AnonymousTupleLiteralPart")
JTL_imperativeocl_ListType = Class(name="JTL_imperativeocl_ListType")

# Operation class attributes and methods

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

# JTL_emof_Enumeration class attributes and methods

# DataType class attributes and methods

# EnumerationLiteral class attributes and methods

# JTL_emof_NamedElement class attributes and methods
JTL_emof_NamedElement_name: Property = Property(name="name", type=StringType)
JTL_emof_NamedElement.attributes={JTL_emof_NamedElement_name}

# JTL_emof_Class class attributes and methods
JTL_emof_Class_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
JTL_emof_Class.attributes={JTL_emof_Class_isAbstract}

# Type class attributes and methods

# Property class attributes and methods

# JTL_emof_Package class attributes and methods
JTL_emof_Package_uri: Property = Property(name="uri", type=StringType)
JTL_emof_Package.attributes={JTL_emof_Package_uri}

# NamedElement class attributes and methods

# Package class attributes and methods

# JTL_emof_Type class attributes and methods

# JTL_emof_Parameter class attributes and methods

# JTL_emof_EnumerationLiteral class attributes and methods

# Enumeration class attributes and methods

# JTL_emof_Property class attributes and methods
JTL_emof_Property_isReadOnly: Property = Property(name="isReadOnly", type=BooleanType)
JTL_emof_Property_isDerived: Property = Property(name="isDerived", type=BooleanType)
JTL_emof_Property_isComposite: Property = Property(name="isComposite", type=BooleanType)
JTL_emof_Property_isId: Property = Property(name="isId", type=BooleanType)
JTL_emof_Property_default: Property = Property(name="default", type=StringType)
JTL_emof_Property.attributes={JTL_emof_Property_isReadOnly, JTL_emof_Property_isDerived, JTL_emof_Property_default, JTL_emof_Property_isId, JTL_emof_Property_isComposite}

# JTL_emof_Extent class attributes and methods

# JTL_emof_Object class attributes and methods

# JTL_emof_Operation class attributes and methods

# emof_MultiplicityElement class attributes and methods

# emof_TypedElement class attributes and methods

# Parameter class attributes and methods

# JTL_emof_MultiplicityElement class attributes and methods
JTL_emof_MultiplicityElement_upper: Property = Property(name="upper", type=StringType)
JTL_emof_MultiplicityElement_isOrdered: Property = Property(name="isOrdered", type=StringType)
JTL_emof_MultiplicityElement_isUnique: Property = Property(name="isUnique", type=StringType)
JTL_emof_MultiplicityElement_lower: Property = Property(name="lower", type=IntegerType)
JTL_emof_MultiplicityElement.attributes={JTL_emof_MultiplicityElement_isOrdered, JTL_emof_MultiplicityElement_upper, JTL_emof_MultiplicityElement_isUnique, JTL_emof_MultiplicityElement_lower}

# JTL_JTL_Relation class attributes and methods
JTL_JTL_Relation_isTopLevel: Property = Property(name="isTopLevel", type=BooleanType)
JTL_JTL_Relation.attributes={JTL_JTL_Relation_isTopLevel}

# Transformation class attributes and methods

# Domain class attributes and methods

# Where class attributes and methods

# When class attributes and methods

# Variable class attributes and methods

# JTL_JTL_Domain class attributes and methods
JTL_JTL_Domain_isCheckable: Property = Property(name="isCheckable", type=BooleanType)
JTL_JTL_Domain_isEnforceable: Property = Property(name="isEnforceable", type=BooleanType)
JTL_JTL_Domain.attributes={JTL_JTL_Domain_isCheckable, JTL_JTL_Domain_isEnforceable}

# Pattern class attributes and methods

# JTL_JTL_Model class attributes and methods
JTL_JTL_Model_usedPackage: Property = Property(name="usedPackage", type=StringType)
JTL_JTL_Model.attributes={JTL_JTL_Model_usedPackage}

# JTL_emof_TypedElement class attributes and methods
JTL_emof_TypedElement_type: Property = Property(name="type", type=StringType)
JTL_emof_TypedElement.attributes={JTL_emof_TypedElement_type}

# JTL_emof_PrimitiveType class attributes and methods

# JTL_emof_URIExtent class attributes and methods

# Extent class attributes and methods

# JTL_emof_Comment class attributes and methods

# JTL_JTL_Transformation class attributes and methods

# emof_Class class attributes and methods

# emof_Package class attributes and methods

# Model class attributes and methods

# Relation class attributes and methods

# JTL_essentialocl_BooleanLiteralExp class attributes and methods
JTL_essentialocl_BooleanLiteralExp_booleanSymbol: Property = Property(name="booleanSymbol", type=BooleanType)
JTL_essentialocl_BooleanLiteralExp.attributes={JTL_essentialocl_BooleanLiteralExp_booleanSymbol}

# PrimitiveLiteralExp class attributes and methods

# JTL_essentialocl_CallExp class attributes and methods

# JTL_essentialocl_OclExpression class attributes and methods

# TypedElement class attributes and methods

# TryExp class attributes and methods

# JTL_essentialocl_UnlimitedNaturalExp class attributes and methods
JTL_essentialocl_UnlimitedNaturalExp_symbol: Property = Property(name="symbol", type=StringType)
JTL_essentialocl_UnlimitedNaturalExp.attributes={JTL_essentialocl_UnlimitedNaturalExp_symbol}

# NumericLiteralExp class attributes and methods

# JTL_essentialocl_IfExp class attributes and methods

# JTL_JTL_Pattern class attributes and methods

# Predicate class attributes and methods

# TemplateExp class attributes and methods

# JTL_JTL_Predicate class attributes and methods

# OclExpression class attributes and methods

# JTL_JTL_When class attributes and methods

# JTL_JTL_Where class attributes and methods

# JTL_essentialocl_VariableExp class attributes and methods

# JTL_essentialocl_TypeExp class attributes and methods

# JTL_essentialocl_LoopExp class attributes and methods

# essentialocl_CallExp class attributes and methods

# essentialocl_OclExpression class attributes and methods

# JTL_essentialocl_IteratorExp class attributes and methods

# LoopExp class attributes and methods

# JTL_essentialocl_StringLiteralExp class attributes and methods
JTL_essentialocl_StringLiteralExp_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
JTL_essentialocl_StringLiteralExp.attributes={JTL_essentialocl_StringLiteralExp_stringSymbol}

# JTL_essentialocl_IntegerLiteralExp class attributes and methods
JTL_essentialocl_IntegerLiteralExp_integerSymbol: Property = Property(name="integerSymbol", type=IntegerType)
JTL_essentialocl_IntegerLiteralExp.attributes={JTL_essentialocl_IntegerLiteralExp_integerSymbol}

# JTL_essentialocl_OperationCallExp class attributes and methods

# JTL_essentialocl_LetExp class attributes and methods

# JTL_essentialocl_Variable class attributes and methods

# LetExp class attributes and methods

# ComputeExp class attributes and methods

# JTL_essentialocl_PropertyCallExp class attributes and methods

# FeaturePropertyCall class attributes and methods

# JTL_essentialocl_CollectionItem class attributes and methods

# JTL_essentialocl_CollectionRange class attributes and methods

# JTL_essentialocl_TupleLiteralExp class attributes and methods

# TupleLiteralPart class attributes and methods

# JTL_essentialocl_NullLiteralExp class attributes and methods

# JTL_essentialocl_ExpressionInOcl class attributes and methods

# OpaqueExpression class attributes and methods

# JTL_essentialocl_RealLiteralExp class attributes and methods
JTL_essentialocl_RealLiteralExp_realSymbol: Property = Property(name="realSymbol", type=FloatType)
JTL_essentialocl_RealLiteralExp.attributes={JTL_essentialocl_RealLiteralExp_realSymbol}

# JTL_essentialocl_LiteralExp class attributes and methods

# JTL_essentialocl_IterateExp class attributes and methods

# JTL_essentialocl_PrimitiveLiteralExp class attributes and methods

# LiteralExp class attributes and methods

# JTL_essentialocl_NumericLiteralExp class attributes and methods

# JTL_essentialocl_CollectionLiteralExp class attributes and methods
JTL_essentialocl_CollectionLiteralExp_kind: Property = Property(name="kind", type=StringType)
JTL_essentialocl_CollectionLiteralExp.attributes={JTL_essentialocl_CollectionLiteralExp_kind}

# CollectionLiteralPart class attributes and methods

# JTL_essentialocl_CollectionLiteralPart class attributes and methods

# CollectionLiteralExp class attributes and methods

# JTL_essentialocl_InvalidType class attributes and methods

# JTL_essentialocl_OrderedSetType class attributes and methods

# JTL_essentialocl_SequenceType class attributes and methods

# JTL_essentialocl_SetType class attributes and methods

# JTL_essentialocl_TupleType class attributes and methods

# emof_DataType class attributes and methods

# JTL_essentialocl_VoidType class attributes and methods

# JTL_essentialocl_AnyType class attributes and methods

# emof_Type class attributes and methods

# JTL_template_TemplateExp class attributes and methods

# JTL_essentialocl_OpaqueExpression class attributes and methods

# JTL_essentialocl_InvalidLiteralExp class attributes and methods

# JTL_essentialocl_FeaturePropertyCall class attributes and methods

# CallExp class attributes and methods

# JTL_essentialocl_TupleLiteralPart class attributes and methods

# TupleLiteralExp class attributes and methods

# JTL_essentialocl_BagType class attributes and methods

# CollectionType class attributes and methods

# JTL_essentialocl_CollectionType class attributes and methods

# JTL_essentialocl_EnumLiteralExp class attributes and methods

# JTL_template_PropertyTemplateItem class attributes and methods

# ObjectTemplateExp class attributes and methods

# JTL_imperativeocl_ImperativeIterateExp class attributes and methods

# ImperativeLoopExp class attributes and methods

# JTL_imperativeocl_AssignExp class attributes and methods
JTL_imperativeocl_AssignExp_isReset: Property = Property(name="isReset", type=BooleanType)
JTL_imperativeocl_AssignExp.attributes={JTL_imperativeocl_AssignExp_isReset}

# ImperativeExpression class attributes and methods

# JTL_template_ObjectTemplateExp class attributes and methods
JTL_template_ObjectTemplateExp_referredClass: Property = Property(name="referredClass", type=StringType)
JTL_template_ObjectTemplateExp.attributes={JTL_template_ObjectTemplateExp_referredClass}

# PropertyTemplateItem class attributes and methods

# AssignExp class attributes and methods

# JTL_template_CollectionTemplateExp class attributes and methods
JTL_template_CollectionTemplateExp_kind: Property = Property(name="kind", type=StringType)
JTL_template_CollectionTemplateExp.attributes={JTL_template_CollectionTemplateExp_kind}

# JTL_imperativeocl_WhileExp class attributes and methods

# JTL_imperativeocl_ComputeExp class attributes and methods

# JTL_imperativeocl_AltExp class attributes and methods

# JTL_imperativeocl_UnlinkExp class attributes and methods

# JTL_imperativeocl_BlockExp class attributes and methods

# JTL_imperativeocl_SwitchExp class attributes and methods

# imperativeocl_ImperativeExpression class attributes and methods

# AltExp class attributes and methods

# JTL_imperativeocl_VariableInitExp class attributes and methods
JTL_imperativeocl_VariableInitExp_withResult: Property = Property(name="withResult", type=BooleanType)
JTL_imperativeocl_VariableInitExp.attributes={JTL_imperativeocl_VariableInitExp_withResult}

# JTL_imperativeocl_RaiseExp class attributes and methods

# JTL_imperativeocl_ContinueExp class attributes and methods

# JTL_imperativeocl_ForExp class attributes and methods

# JTL_imperativeocl_TupleExp class attributes and methods

# JTL_imperativeocl_Typedef class attributes and methods

# JTL_imperativeocl_InstantiationExp class attributes and methods

# JTL_imperativeocl_ReturnExp class attributes and methods

# JTL_imperativeocl_BreakExp class attributes and methods

# JTL_imperativeocl_TryExp class attributes and methods

# JTL_imperativeocl_AssertExp class attributes and methods
JTL_imperativeocl_AssertExp_severity: Property = Property(name="severity", type=StringType)
JTL_imperativeocl_AssertExp.attributes={JTL_imperativeocl_AssertExp_severity}

# LogExp class attributes and methods

# JTL_imperativeocl_ImperativeLoopExp class attributes and methods

# essentialocl_LoopExp class attributes and methods

# JTL_imperativeocl_CollectorExp class attributes and methods

# JTL_imperativeocl_ImperativeExpression class attributes and methods

# JTL_imperativeocl_UnpackExp class attributes and methods

# JTL_imperativeocl_DictionaryType class attributes and methods

# JTL_imperativeocl_DictLiteralExp class attributes and methods

# DictLiteralPart class attributes and methods

# JTL_imperativeocl_DictLiteralPart class attributes and methods

# JTL_imperativeocl_TemplateParameterType class attributes and methods
JTL_imperativeocl_TemplateParameterType_specification: Property = Property(name="specification", type=StringType)
JTL_imperativeocl_TemplateParameterType.attributes={JTL_imperativeocl_TemplateParameterType_specification}

# JTL_imperativeocl_LogExp class attributes and methods
JTL_imperativeocl_LogExp_text: Property = Property(name="text", type=StringType)
JTL_imperativeocl_LogExp_level: Property = Property(name="level", type=IntegerType)
JTL_imperativeocl_LogExp.attributes={JTL_imperativeocl_LogExp_text, JTL_imperativeocl_LogExp_level}

# JTL_imperativeocl_AnonymousTupleType class attributes and methods

# JTL_imperativeocl_AnonymousTupleLiteralExp class attributes and methods

# AnonymousTupleLiteralPart class attributes and methods

# JTL_imperativeocl_AnonymousTupleLiteralPart class attributes and methods

# JTL_imperativeocl_ListType class attributes and methods

# Relationships
ownedOperation1: BinaryAssociation = BinaryAssociation(
    name="ownedOperation1",
    ends={
        Property(name="Operation", type=JTL_emof_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="class_", type=Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superClass2: BinaryAssociation = BinaryAssociation(
    name="superClass2",
    ends={
        Property(name="Class3", type=JTL_emof_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_emof_Class", type=Class_, multiplicity=Multiplicity(0, 9999))
    }
)
tag4: BinaryAssociation = BinaryAssociation(
    name="tag4",
    ends={
        Property(name="Tag", type=JTL_emof_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="element", type=Tag, multiplicity=Multiplicity(0, 9999))
    }
)
ownedComment5: BinaryAssociation = BinaryAssociation(
    name="ownedComment5",
    ends={
        Property(name="Comment", type=JTL_emof_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_emof_Element", type=Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element6: BinaryAssociation = BinaryAssociation(
    name="element6",
    ends={
        Property(name="Element", type=JTL_emof_Tag, multiplicity=Multiplicity(1, 1)),
        Property(name="tag", type=Element, multiplicity=Multiplicity(0, 9999))
    }
)
ownedLiteral7: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral7",
    ends={
        Property(name="EnumerationLiteral", type=JTL_emof_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="enumeration", type=EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAttribute0: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute0",
    ends={
        Property(name="Property", type=JTL_emof_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Class", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedType12: BinaryAssociation = BinaryAssociation(
    name="ownedType12",
    ends={
        Property(name="Type13", type=JTL_emof_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedPackage14: BinaryAssociation = BinaryAssociation(
    name="nestedPackage14",
    ends={
        Property(name="Package", type=JTL_emof_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_emof_Package", type=Package, multiplicity=Multiplicity(0, 9999))
    }
)
package15: BinaryAssociation = BinaryAssociation(
    name="package15",
    ends={
        Property(name="Package16", type=JTL_emof_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedType", type=Package, multiplicity=Multiplicity(1, 1))
    }
)
operation17: BinaryAssociation = BinaryAssociation(
    name="operation17",
    ends={
        Property(name="Operation18", type=JTL_emof_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedParameter", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
enumeration19: BinaryAssociation = BinaryAssociation(
    name="enumeration19",
    ends={
        Property(name="Enumeration", type=JTL_emof_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedLiteral", type=Enumeration_, multiplicity=Multiplicity(0, 1))
    }
)
Class20: BinaryAssociation = BinaryAssociation(
    name="Class20",
    ends={
        Property(name="Class21", type=JTL_emof_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedAttribute", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
opposite22: BinaryAssociation = BinaryAssociation(
    name="opposite22",
    ends={
        Property(name="Property23", type=JTL_emof_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_emof_Property", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
class_8: BinaryAssociation = BinaryAssociation(
    name="class_8",
    ends={
        Property(name="Class9", type=JTL_emof_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedOperation", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
ownedParameter10: BinaryAssociation = BinaryAssociation(
    name="ownedParameter10",
    ends={
        Property(name="Parameter", type=JTL_emof_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
raisedException11: BinaryAssociation = BinaryAssociation(
    name="raisedException11",
    ends={
        Property(name="Type", type=JTL_emof_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_emof_Operation", type=Type, multiplicity=Multiplicity(0, 9999))
    }
)
transformation28: BinaryAssociation = BinaryAssociation(
    name="transformation28",
    ends={
        Property(name="Transformation", type=JTL_JTL_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="relation", type=Transformation, multiplicity=Multiplicity(1, 1))
    }
)
domain29: BinaryAssociation = BinaryAssociation(
    name="domain29",
    ends={
        Property(name="Domain", type=JTL_JTL_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="relation30", type=Domain, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
where31: BinaryAssociation = BinaryAssociation(
    name="where31",
    ends={
        Property(name="Where", type=JTL_JTL_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="whereOwner", type=Where, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
when32: BinaryAssociation = BinaryAssociation(
    name="when32",
    ends={
        Property(name="When", type=JTL_JTL_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="whenOwner", type=When, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable33: BinaryAssociation = BinaryAssociation(
    name="variable33",
    ends={
        Property(name="Variable", type=JTL_JTL_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_JTL_Relation", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relation34: BinaryAssociation = BinaryAssociation(
    name="relation34",
    ends={
        Property(name="Relation35", type=JTL_JTL_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="domain", type=Relation, multiplicity=Multiplicity(1, 1))
    }
)
pattern36: BinaryAssociation = BinaryAssociation(
    name="pattern36",
    ends={
        Property(name="Pattern", type=JTL_JTL_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_JTL_Domain", type=Pattern, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
model37: BinaryAssociation = BinaryAssociation(
    name="model37",
    ends={
        Property(name="Model39", type=JTL_JTL_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_JTL_Domain38", type=Model, multiplicity=Multiplicity(1, 1))
    }
)
rootVariable40: BinaryAssociation = BinaryAssociation(
    name="rootVariable40",
    ends={
        Property(name="Variable42", type=JTL_JTL_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_JTL_Domain41", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
transformation43: BinaryAssociation = BinaryAssociation(
    name="transformation43",
    ends={
        Property(name="Transformation44", type=JTL_JTL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="modelParameter", type=Transformation, multiplicity=Multiplicity(1, 1))
    }
)
dependsOn45: BinaryAssociation = BinaryAssociation(
    name="dependsOn45",
    ends={
        Property(name="Model46", type=JTL_JTL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_JTL_Model", type=Model, multiplicity=Multiplicity(0, 9999))
    }
)
annotatedElement24: BinaryAssociation = BinaryAssociation(
    name="annotatedElement24",
    ends={
        Property(name="NamedElement", type=JTL_emof_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_emof_Comment", type=NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
modelParameter25: BinaryAssociation = BinaryAssociation(
    name="modelParameter25",
    ends={
        Property(name="Model", type=JTL_JTL_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation", type=Model, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relation26: BinaryAssociation = BinaryAssociation(
    name="relation26",
    ends={
        Property(name="Relation", type=JTL_JTL_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation27", type=Relation, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
source62: BinaryAssociation = BinaryAssociation(
    name="source62",
    ends={
        Property(name="OclExpression63", type=JTL_essentialocl_CallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_CallExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tryBodyOwner64: BinaryAssociation = BinaryAssociation(
    name="tryBodyOwner64",
    ends={
        Property(name="TryExp", type=JTL_essentialocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="tryBody", type=TryExp, multiplicity=Multiplicity(0, 1))
    }
)
condition65: BinaryAssociation = BinaryAssociation(
    name="condition65",
    ends={
        Property(name="OclExpression66", type=JTL_essentialocl_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_IfExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression67: BinaryAssociation = BinaryAssociation(
    name="thenExpression67",
    ends={
        Property(name="OclExpression69", type=JTL_essentialocl_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_IfExp68", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression70: BinaryAssociation = BinaryAssociation(
    name="elseExpression70",
    ends={
        Property(name="OclExpression72", type=JTL_essentialocl_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_IfExp71", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
predicate47: BinaryAssociation = BinaryAssociation(
    name="predicate47",
    ends={
        Property(name="Predicate", type=JTL_JTL_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="pattern", type=Predicate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bindsTo48: BinaryAssociation = BinaryAssociation(
    name="bindsTo48",
    ends={
        Property(name="Variable49", type=JTL_JTL_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_JTL_Pattern", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
templateExpression50: BinaryAssociation = BinaryAssociation(
    name="templateExpression50",
    ends={
        Property(name="TemplateExp", type=JTL_JTL_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_JTL_Pattern51", type=TemplateExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
domain52: BinaryAssociation = BinaryAssociation(
    name="domain52",
    ends={
        Property(name="Domain54", type=JTL_JTL_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_JTL_Pattern53", type=Domain, multiplicity=Multiplicity(1, 1))
    }
)
pattern55: BinaryAssociation = BinaryAssociation(
    name="pattern55",
    ends={
        Property(name="Pattern56", type=JTL_JTL_Predicate, multiplicity=Multiplicity(1, 1)),
        Property(name="predicate", type=Pattern, multiplicity=Multiplicity(1, 1))
    }
)
conditionExpression57: BinaryAssociation = BinaryAssociation(
    name="conditionExpression57",
    ends={
        Property(name="OclExpression", type=JTL_JTL_Predicate, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_JTL_Predicate", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
whenOwner58: BinaryAssociation = BinaryAssociation(
    name="whenOwner58",
    ends={
        Property(name="Relation59", type=JTL_JTL_When, multiplicity=Multiplicity(1, 1)),
        Property(name="when", type=Relation, multiplicity=Multiplicity(0, 1))
    }
)
whereOwner60: BinaryAssociation = BinaryAssociation(
    name="whereOwner60",
    ends={
        Property(name="Relation61", type=JTL_JTL_Where, multiplicity=Multiplicity(1, 1)),
        Property(name="where", type=Relation, multiplicity=Multiplicity(0, 1))
    }
)
referredVariable87: BinaryAssociation = BinaryAssociation(
    name="referredVariable87",
    ends={
        Property(name="Variable88", type=JTL_essentialocl_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_VariableExp", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
referredType89: BinaryAssociation = BinaryAssociation(
    name="referredType89",
    ends={
        Property(name="Type90", type=JTL_essentialocl_TypeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_TypeExp", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
body91: BinaryAssociation = BinaryAssociation(
    name="body91",
    ends={
        Property(name="OclExpression92", type=JTL_essentialocl_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_LoopExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterator93: BinaryAssociation = BinaryAssociation(
    name="iterator93",
    ends={
        Property(name="Variable95", type=JTL_essentialocl_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_LoopExp94", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument96: BinaryAssociation = BinaryAssociation(
    name="argument96",
    ends={
        Property(name="OclExpression97", type=JTL_essentialocl_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_OperationCallExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
in_73: BinaryAssociation = BinaryAssociation(
    name="in_73",
    ends={
        Property(name="OclExpression74", type=JTL_essentialocl_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_LetExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable75: BinaryAssociation = BinaryAssociation(
    name="variable75",
    ends={
        Property(name="Variable76", type=JTL_essentialocl_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="LetExp", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initExpression77: BinaryAssociation = BinaryAssociation(
    name="initExpression77",
    ends={
        Property(name="OclExpression78", type=JTL_essentialocl_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_Variable", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
LetExp79: BinaryAssociation = BinaryAssociation(
    name="LetExp79",
    ends={
        Property(name="LetExp80", type=JTL_essentialocl_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="variable", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
bindParameter81: BinaryAssociation = BinaryAssociation(
    name="bindParameter81",
    ends={
        Property(name="Parameter83", type=JTL_essentialocl_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_Variable82", type=Parameter_, multiplicity=Multiplicity(0, 1))
    }
)
computeOwner84: BinaryAssociation = BinaryAssociation(
    name="computeOwner84",
    ends={
        Property(name="ComputeExp", type=JTL_essentialocl_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="returnedElement", type=ComputeExp, multiplicity=Multiplicity(0, 1))
    }
)
referredProperty85: BinaryAssociation = BinaryAssociation(
    name="referredProperty85",
    ends={
        Property(name="Property86", type=JTL_essentialocl_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_PropertyCallExp", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
CollectionLiteralExp104: BinaryAssociation = BinaryAssociation(
    name="CollectionLiteralExp104",
    ends={
        Property(name="part", type=CollectionLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="CollectionLiteralExp105", type=JTL_essentialocl_CollectionLiteralPart, multiplicity=Multiplicity(1, 1))
    }
)
item106: BinaryAssociation = BinaryAssociation(
    name="item106",
    ends={
        Property(name="OclExpression107", type=JTL_essentialocl_CollectionItem, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_CollectionItem", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
first108: BinaryAssociation = BinaryAssociation(
    name="first108",
    ends={
        Property(name="OclExpression109", type=JTL_essentialocl_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_CollectionRange", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
last110: BinaryAssociation = BinaryAssociation(
    name="last110",
    ends={
        Property(name="OclExpression112", type=JTL_essentialocl_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_CollectionRange111", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
part113: BinaryAssociation = BinaryAssociation(
    name="part113",
    ends={
        Property(name="TupleLiteralPart", type=JTL_essentialocl_TupleLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="TupleLiteralExp", type=TupleLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyExpression114: BinaryAssociation = BinaryAssociation(
    name="bodyExpression114",
    ends={
        Property(name="OclExpression115", type=JTL_essentialocl_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_ExpressionInOcl", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context116: BinaryAssociation = BinaryAssociation(
    name="context116",
    ends={
        Property(name="Variable118", type=JTL_essentialocl_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_ExpressionInOcl117", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resultVariable119: BinaryAssociation = BinaryAssociation(
    name="resultVariable119",
    ends={
        Property(name="Variable121", type=JTL_essentialocl_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_ExpressionInOcl120", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
referredOperation98: BinaryAssociation = BinaryAssociation(
    name="referredOperation98",
    ends={
        Property(name="Relation100", type=JTL_essentialocl_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_OperationCallExp99", type=Relation, multiplicity=Multiplicity(0, 1))
    }
)
result101: BinaryAssociation = BinaryAssociation(
    name="result101",
    ends={
        Property(name="Variable102", type=JTL_essentialocl_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_IterateExp", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
part103: BinaryAssociation = BinaryAssociation(
    name="part103",
    ends={
        Property(name="CollectionLiteralPart", type=JTL_essentialocl_CollectionLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="CollectionLiteralExp", type=CollectionLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameterVariable122: BinaryAssociation = BinaryAssociation(
    name="parameterVariable122",
    ends={
        Property(name="Variable124", type=JTL_essentialocl_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_ExpressionInOcl123", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
TupleLiteralExp125: BinaryAssociation = BinaryAssociation(
    name="TupleLiteralExp125",
    ends={
        Property(name="TupleLiteralExp127", type=JTL_essentialocl_TupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="part126", type=TupleLiteralExp, multiplicity=Multiplicity(0, 1))
    }
)
elementType128: BinaryAssociation = BinaryAssociation(
    name="elementType128",
    ends={
        Property(name="Type129", type=JTL_essentialocl_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_CollectionType", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
referredEnumLiteral130: BinaryAssociation = BinaryAssociation(
    name="referredEnumLiteral130",
    ends={
        Property(name="EnumerationLiteral131", type=JTL_essentialocl_EnumLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_essentialocl_EnumLiteralExp", type=EnumerationLiteral, multiplicity=Multiplicity(0, 1))
    }
)
referredCollectionType141: BinaryAssociation = BinaryAssociation(
    name="referredCollectionType141",
    ends={
        Property(name="CollectionType", type=JTL_template_CollectionTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_template_CollectionTemplateExp142", type=CollectionType, multiplicity=Multiplicity(0, 1))
    }
)
match143: BinaryAssociation = BinaryAssociation(
    name="match143",
    ends={
        Property(name="OclExpression145", type=JTL_template_CollectionTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_template_CollectionTemplateExp144", type=OclExpression, multiplicity=Multiplicity(0, 1))
    }
)
objContainer146: BinaryAssociation = BinaryAssociation(
    name="objContainer146",
    ends={
        Property(name="ObjectTemplateExp", type=JTL_template_PropertyTemplateItem, multiplicity=Multiplicity(1, 1)),
        Property(name="part147", type=ObjectTemplateExp, multiplicity=Multiplicity(1, 1))
    }
)
value148: BinaryAssociation = BinaryAssociation(
    name="value148",
    ends={
        Property(name="OclExpression149", type=JTL_template_PropertyTemplateItem, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_template_PropertyTemplateItem", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referredProperty150: BinaryAssociation = BinaryAssociation(
    name="referredProperty150",
    ends={
        Property(name="Property152", type=JTL_template_PropertyTemplateItem, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_template_PropertyTemplateItem151", type=Property_, multiplicity=Multiplicity(1, 1))
    }
)
target153: BinaryAssociation = BinaryAssociation(
    name="target153",
    ends={
        Property(name="Variable154", type=JTL_imperativeocl_ImperativeIterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_ImperativeIterateExp", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value155: BinaryAssociation = BinaryAssociation(
    name="value155",
    ends={
        Property(name="OclExpression156", type=JTL_imperativeocl_AssignExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_AssignExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bindsTo132: BinaryAssociation = BinaryAssociation(
    name="bindsTo132",
    ends={
        Property(name="Variable133", type=JTL_template_TemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_template_TemplateExp", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
where134: BinaryAssociation = BinaryAssociation(
    name="where134",
    ends={
        Property(name="OclExpression136", type=JTL_template_TemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_template_TemplateExp135", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
part137: BinaryAssociation = BinaryAssociation(
    name="part137",
    ends={
        Property(name="PropertyTemplateItem", type=JTL_template_ObjectTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="objContainer", type=PropertyTemplateItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inside138: BinaryAssociation = BinaryAssociation(
    name="inside138",
    ends={
        Property(name="AssignExp", type=JTL_template_ObjectTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_template_ObjectTemplateExp", type=AssignExp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
part139: BinaryAssociation = BinaryAssociation(
    name="part139",
    ends={
        Property(name="OclExpression140", type=JTL_template_CollectionTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_template_CollectionTemplateExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredVariable169: BinaryAssociation = BinaryAssociation(
    name="referredVariable169",
    ends={
        Property(name="Variable170", type=JTL_imperativeocl_VariableInitExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_VariableInitExp", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition171: BinaryAssociation = BinaryAssociation(
    name="condition171",
    ends={
        Property(name="OclExpression172", type=JTL_imperativeocl_WhileExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_WhileExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body173: BinaryAssociation = BinaryAssociation(
    name="body173",
    ends={
        Property(name="OclExpression175", type=JTL_imperativeocl_WhileExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_WhileExp174", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnedElement176: BinaryAssociation = BinaryAssociation(
    name="returnedElement176",
    ends={
        Property(name="Variable177", type=JTL_imperativeocl_ComputeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="computeOwner", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body178: BinaryAssociation = BinaryAssociation(
    name="body178",
    ends={
        Property(name="OclExpression179", type=JTL_imperativeocl_ComputeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_ComputeExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition180: BinaryAssociation = BinaryAssociation(
    name="condition180",
    ends={
        Property(name="OclExpression181", type=JTL_imperativeocl_AltExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_AltExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body182: BinaryAssociation = BinaryAssociation(
    name="body182",
    ends={
        Property(name="OclExpression184", type=JTL_imperativeocl_AltExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_AltExp183", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left157: BinaryAssociation = BinaryAssociation(
    name="left157",
    ends={
        Property(name="OclExpression159", type=JTL_imperativeocl_AssignExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_AssignExp158", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
defaultValue160: BinaryAssociation = BinaryAssociation(
    name="defaultValue160",
    ends={
        Property(name="OclExpression162", type=JTL_imperativeocl_AssignExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_AssignExp161", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body163: BinaryAssociation = BinaryAssociation(
    name="body163",
    ends={
        Property(name="OclExpression164", type=JTL_imperativeocl_BlockExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_BlockExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
alternativePart165: BinaryAssociation = BinaryAssociation(
    name="alternativePart165",
    ends={
        Property(name="AltExp", type=JTL_imperativeocl_SwitchExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_SwitchExp", type=AltExp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elsePart166: BinaryAssociation = BinaryAssociation(
    name="elsePart166",
    ends={
        Property(name="OclExpression168", type=JTL_imperativeocl_SwitchExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_SwitchExp167", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exception199: BinaryAssociation = BinaryAssociation(
    name="exception199",
    ends={
        Property(name="Type200", type=JTL_imperativeocl_RaiseExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_RaiseExp", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
element201: BinaryAssociation = BinaryAssociation(
    name="element201",
    ends={
        Property(name="OclExpression202", type=JTL_imperativeocl_TupleExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_TupleExp", type=OclExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
base203: BinaryAssociation = BinaryAssociation(
    name="base203",
    ends={
        Property(name="Type204", type=JTL_imperativeocl_Typedef, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_Typedef", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
condition205: BinaryAssociation = BinaryAssociation(
    name="condition205",
    ends={
        Property(name="OclExpression207", type=JTL_imperativeocl_Typedef, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_Typedef206", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
instantiatedClass208: BinaryAssociation = BinaryAssociation(
    name="instantiatedClass208",
    ends={
        Property(name="Class209", type=JTL_imperativeocl_InstantiationExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_InstantiationExp", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
extent210: BinaryAssociation = BinaryAssociation(
    name="extent210",
    ends={
        Property(name="Variable212", type=JTL_imperativeocl_InstantiationExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_InstantiationExp211", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
argument213: BinaryAssociation = BinaryAssociation(
    name="argument213",
    ends={
        Property(name="OclExpression215", type=JTL_imperativeocl_InstantiationExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_InstantiationExp214", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target185: BinaryAssociation = BinaryAssociation(
    name="target185",
    ends={
        Property(name="OclExpression186", type=JTL_imperativeocl_UnlinkExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_UnlinkExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
item187: BinaryAssociation = BinaryAssociation(
    name="item187",
    ends={
        Property(name="OclExpression189", type=JTL_imperativeocl_UnlinkExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_UnlinkExp188", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value190: BinaryAssociation = BinaryAssociation(
    name="value190",
    ends={
        Property(name="OclExpression191", type=JTL_imperativeocl_ReturnExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_ReturnExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tryBody192: BinaryAssociation = BinaryAssociation(
    name="tryBody192",
    ends={
        Property(name="OclExpression193", type=JTL_imperativeocl_TryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="tryBodyOwner", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exception194: BinaryAssociation = BinaryAssociation(
    name="exception194",
    ends={
        Property(name="Type195", type=JTL_imperativeocl_TryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_TryExp", type=Type, multiplicity=Multiplicity(0, 9999))
    }
)
exceptBody196: BinaryAssociation = BinaryAssociation(
    name="exceptBody196",
    ends={
        Property(name="OclExpression198", type=JTL_imperativeocl_TryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_TryExp197", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
element226: BinaryAssociation = BinaryAssociation(
    name="element226",
    ends={
        Property(name="Element228", type=JTL_imperativeocl_LogExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_LogExp227", type=Element, multiplicity=Multiplicity(0, 1))
    }
)
log229: BinaryAssociation = BinaryAssociation(
    name="log229",
    ends={
        Property(name="LogExp", type=JTL_imperativeocl_AssertExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_AssertExp", type=LogExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assertion230: BinaryAssociation = BinaryAssociation(
    name="assertion230",
    ends={
        Property(name="OclExpression232", type=JTL_imperativeocl_AssertExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_AssertExp231", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition233: BinaryAssociation = BinaryAssociation(
    name="condition233",
    ends={
        Property(name="OclExpression234", type=JTL_imperativeocl_ImperativeLoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_ImperativeLoopExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target235: BinaryAssociation = BinaryAssociation(
    name="target235",
    ends={
        Property(name="Variable236", type=JTL_imperativeocl_CollectorExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_CollectorExp", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
keyType216: BinaryAssociation = BinaryAssociation(
    name="keyType216",
    ends={
        Property(name="Type217", type=JTL_imperativeocl_DictionaryType, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_DictionaryType", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
part218: BinaryAssociation = BinaryAssociation(
    name="part218",
    ends={
        Property(name="DictLiteralPart", type=JTL_imperativeocl_DictLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_DictLiteralExp", type=DictLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key219: BinaryAssociation = BinaryAssociation(
    name="key219",
    ends={
        Property(name="OclExpression220", type=JTL_imperativeocl_DictLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_DictLiteralPart", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value221: BinaryAssociation = BinaryAssociation(
    name="value221",
    ends={
        Property(name="OclExpression223", type=JTL_imperativeocl_DictLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_DictLiteralPart222", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition224: BinaryAssociation = BinaryAssociation(
    name="condition224",
    ends={
        Property(name="OclExpression225", type=JTL_imperativeocl_LogExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_LogExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable237: BinaryAssociation = BinaryAssociation(
    name="variable237",
    ends={
        Property(name="Variable238", type=JTL_imperativeocl_UnpackExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_UnpackExp", type=Variable, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
elementType239: BinaryAssociation = BinaryAssociation(
    name="elementType239",
    ends={
        Property(name="Type240", type=JTL_imperativeocl_AnonymousTupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_AnonymousTupleType", type=Type, multiplicity=Multiplicity(0, 9999))
    }
)
part241: BinaryAssociation = BinaryAssociation(
    name="part241",
    ends={
        Property(name="AnonymousTupleLiteralPart", type=JTL_imperativeocl_AnonymousTupleLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_AnonymousTupleLiteralExp", type=AnonymousTupleLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value242: BinaryAssociation = BinaryAssociation(
    name="value242",
    ends={
        Property(name="OclExpression243", type=JTL_imperativeocl_AnonymousTupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="JTL_imperativeocl_AnonymousTupleLiteralPart", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_JTL_emof_DataType_Type = Generalization(general=Type, specific=JTL_emof_DataType)
gen_JTL_emof_Element_Object = Generalization(general=Object, specific=JTL_emof_Element)
gen_JTL_emof_Tag_Element = Generalization(general=Element, specific=JTL_emof_Tag)
gen_JTL_emof_Enumeration_DataType = Generalization(general=DataType, specific=JTL_emof_Enumeration)
gen_JTL_emof_NamedElement_Element = Generalization(general=Element, specific=JTL_emof_NamedElement)
gen_JTL_emof_Class_Type = Generalization(general=Type, specific=JTL_emof_Class)
gen_JTL_emof_Package_NamedElement = Generalization(general=NamedElement, specific=JTL_emof_Package)
gen_JTL_emof_Type_NamedElement = Generalization(general=NamedElement, specific=JTL_emof_Type)
gen_JTL_emof_Parameter_emof_MultiplicityElement = Generalization(general=emof_MultiplicityElement, specific=JTL_emof_Parameter)
gen_JTL_emof_Parameter_emof_TypedElement = Generalization(general=emof_TypedElement, specific=JTL_emof_Parameter)
gen_JTL_emof_EnumerationLiteral_NamedElement = Generalization(general=NamedElement, specific=JTL_emof_EnumerationLiteral)
gen_JTL_emof_Property_emof_MultiplicityElement = Generalization(general=emof_MultiplicityElement, specific=JTL_emof_Property)
gen_JTL_emof_Property_emof_TypedElement = Generalization(general=emof_TypedElement, specific=JTL_emof_Property)
gen_JTL_emof_Extent_Object = Generalization(general=Object, specific=JTL_emof_Extent)
gen_JTL_emof_Operation_emof_MultiplicityElement = Generalization(general=emof_MultiplicityElement, specific=JTL_emof_Operation)
gen_JTL_emof_Operation_emof_TypedElement = Generalization(general=emof_TypedElement, specific=JTL_emof_Operation)
gen_JTL_JTL_Relation_NamedElement = Generalization(general=NamedElement, specific=JTL_JTL_Relation)
gen_JTL_JTL_Domain_NamedElement = Generalization(general=NamedElement, specific=JTL_JTL_Domain)
gen_JTL_JTL_Model_NamedElement = Generalization(general=NamedElement, specific=JTL_JTL_Model)
gen_JTL_emof_TypedElement_NamedElement = Generalization(general=NamedElement, specific=JTL_emof_TypedElement)
gen_JTL_emof_PrimitiveType_DataType = Generalization(general=DataType, specific=JTL_emof_PrimitiveType)
gen_JTL_emof_URIExtent_Extent = Generalization(general=Extent, specific=JTL_emof_URIExtent)
gen_JTL_emof_Comment_Element = Generalization(general=Element, specific=JTL_emof_Comment)
gen_JTL_JTL_Transformation_emof_Class = Generalization(general=emof_Class, specific=JTL_JTL_Transformation)
gen_JTL_JTL_Transformation_emof_Package = Generalization(general=emof_Package, specific=JTL_JTL_Transformation)
gen_JTL_essentialocl_BooleanLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=JTL_essentialocl_BooleanLiteralExp)
gen_JTL_essentialocl_CallExp_OclExpression = Generalization(general=OclExpression, specific=JTL_essentialocl_CallExp)
gen_JTL_essentialocl_OclExpression_TypedElement = Generalization(general=TypedElement, specific=JTL_essentialocl_OclExpression)
gen_JTL_essentialocl_UnlimitedNaturalExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=JTL_essentialocl_UnlimitedNaturalExp)
gen_JTL_essentialocl_IfExp_OclExpression = Generalization(general=OclExpression, specific=JTL_essentialocl_IfExp)
gen_JTL_JTL_Pattern_Element = Generalization(general=Element, specific=JTL_JTL_Pattern)
gen_JTL_JTL_Predicate_Element = Generalization(general=Element, specific=JTL_JTL_Predicate)
gen_JTL_JTL_When_Pattern = Generalization(general=Pattern, specific=JTL_JTL_When)
gen_JTL_JTL_Where_Pattern = Generalization(general=Pattern, specific=JTL_JTL_Where)
gen_JTL_essentialocl_VariableExp_OclExpression = Generalization(general=OclExpression, specific=JTL_essentialocl_VariableExp)
gen_JTL_essentialocl_TypeExp_OclExpression = Generalization(general=OclExpression, specific=JTL_essentialocl_TypeExp)
gen_JTL_essentialocl_LoopExp_essentialocl_CallExp = Generalization(general=essentialocl_CallExp, specific=JTL_essentialocl_LoopExp)
gen_JTL_essentialocl_LoopExp_essentialocl_OclExpression = Generalization(general=essentialocl_OclExpression, specific=JTL_essentialocl_LoopExp)
gen_JTL_essentialocl_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=JTL_essentialocl_IteratorExp)
gen_JTL_essentialocl_StringLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=JTL_essentialocl_StringLiteralExp)
gen_JTL_essentialocl_IntegerLiteralExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=JTL_essentialocl_IntegerLiteralExp)
gen_JTL_essentialocl_OperationCallExp_FeaturePropertyCall = Generalization(general=FeaturePropertyCall, specific=JTL_essentialocl_OperationCallExp)
gen_JTL_essentialocl_LetExp_OclExpression = Generalization(general=OclExpression, specific=JTL_essentialocl_LetExp)
gen_JTL_essentialocl_Variable_TypedElement = Generalization(general=TypedElement, specific=JTL_essentialocl_Variable)
gen_JTL_essentialocl_PropertyCallExp_FeaturePropertyCall = Generalization(general=FeaturePropertyCall, specific=JTL_essentialocl_PropertyCallExp)
gen_JTL_essentialocl_CollectionItem_CollectionLiteralPart = Generalization(general=CollectionLiteralPart, specific=JTL_essentialocl_CollectionItem)
gen_JTL_essentialocl_CollectionRange_CollectionLiteralPart = Generalization(general=CollectionLiteralPart, specific=JTL_essentialocl_CollectionRange)
gen_JTL_essentialocl_TupleLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=JTL_essentialocl_TupleLiteralExp)
gen_JTL_essentialocl_NullLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=JTL_essentialocl_NullLiteralExp)
gen_JTL_essentialocl_ExpressionInOcl_OpaqueExpression = Generalization(general=OpaqueExpression, specific=JTL_essentialocl_ExpressionInOcl)
gen_JTL_essentialocl_RealLiteralExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=JTL_essentialocl_RealLiteralExp)
gen_JTL_essentialocl_LiteralExp_OclExpression = Generalization(general=OclExpression, specific=JTL_essentialocl_LiteralExp)
gen_JTL_essentialocl_IterateExp_LoopExp = Generalization(general=LoopExp, specific=JTL_essentialocl_IterateExp)
gen_JTL_essentialocl_PrimitiveLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=JTL_essentialocl_PrimitiveLiteralExp)
gen_JTL_essentialocl_NumericLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=JTL_essentialocl_NumericLiteralExp)
gen_JTL_essentialocl_CollectionLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=JTL_essentialocl_CollectionLiteralExp)
gen_JTL_essentialocl_CollectionLiteralPart_TypedElement = Generalization(general=TypedElement, specific=JTL_essentialocl_CollectionLiteralPart)
gen_JTL_essentialocl_InvalidType_Type = Generalization(general=Type, specific=JTL_essentialocl_InvalidType)
gen_JTL_essentialocl_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=JTL_essentialocl_OrderedSetType)
gen_JTL_essentialocl_SequenceType_CollectionType = Generalization(general=CollectionType, specific=JTL_essentialocl_SequenceType)
gen_JTL_essentialocl_SetType_CollectionType = Generalization(general=CollectionType, specific=JTL_essentialocl_SetType)
gen_JTL_essentialocl_TupleType_emof_Class = Generalization(general=emof_Class, specific=JTL_essentialocl_TupleType)
gen_JTL_essentialocl_TupleType_emof_DataType = Generalization(general=emof_DataType, specific=JTL_essentialocl_TupleType)
gen_JTL_essentialocl_VoidType_Type = Generalization(general=Type, specific=JTL_essentialocl_VoidType)
gen_JTL_essentialocl_AnyType_emof_Class = Generalization(general=emof_Class, specific=JTL_essentialocl_AnyType)
gen_JTL_essentialocl_AnyType_emof_Type = Generalization(general=emof_Type, specific=JTL_essentialocl_AnyType)
gen_JTL_template_TemplateExp_LiteralExp = Generalization(general=LiteralExp, specific=JTL_template_TemplateExp)
gen_JTL_essentialocl_InvalidLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=JTL_essentialocl_InvalidLiteralExp)
gen_JTL_essentialocl_FeaturePropertyCall_CallExp = Generalization(general=CallExp, specific=JTL_essentialocl_FeaturePropertyCall)
gen_JTL_essentialocl_TupleLiteralPart_TypedElement = Generalization(general=TypedElement, specific=JTL_essentialocl_TupleLiteralPart)
gen_JTL_essentialocl_BagType_CollectionType = Generalization(general=CollectionType, specific=JTL_essentialocl_BagType)
gen_JTL_essentialocl_CollectionType_DataType = Generalization(general=DataType, specific=JTL_essentialocl_CollectionType)
gen_JTL_essentialocl_EnumLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=JTL_essentialocl_EnumLiteralExp)
gen_JTL_template_PropertyTemplateItem_Element = Generalization(general=Element, specific=JTL_template_PropertyTemplateItem)
gen_JTL_imperativeocl_ImperativeIterateExp_ImperativeLoopExp = Generalization(general=ImperativeLoopExp, specific=JTL_imperativeocl_ImperativeIterateExp)
gen_JTL_imperativeocl_AssignExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTL_imperativeocl_AssignExp)
gen_JTL_template_ObjectTemplateExp_TemplateExp = Generalization(general=TemplateExp, specific=JTL_template_ObjectTemplateExp)
gen_JTL_template_CollectionTemplateExp_TemplateExp = Generalization(general=TemplateExp, specific=JTL_template_CollectionTemplateExp)
gen_JTL_imperativeocl_VariableInitExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTL_imperativeocl_VariableInitExp)
gen_JTL_imperativeocl_WhileExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTL_imperativeocl_WhileExp)
gen_JTL_imperativeocl_ComputeExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTL_imperativeocl_ComputeExp)
gen_JTL_imperativeocl_AltExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTL_imperativeocl_AltExp)
gen_JTL_imperativeocl_BlockExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTL_imperativeocl_BlockExp)
gen_JTL_imperativeocl_SwitchExp_essentialocl_CallExp = Generalization(general=essentialocl_CallExp, specific=JTL_imperativeocl_SwitchExp)
gen_JTL_imperativeocl_SwitchExp_imperativeocl_ImperativeExpression = Generalization(general=imperativeocl_ImperativeExpression, specific=JTL_imperativeocl_SwitchExp)
gen_JTL_imperativeocl_RaiseExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTL_imperativeocl_RaiseExp)
gen_JTL_imperativeocl_ContinueExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTL_imperativeocl_ContinueExp)
gen_JTL_imperativeocl_ForExp_ImperativeLoopExp = Generalization(general=ImperativeLoopExp, specific=JTL_imperativeocl_ForExp)
gen_JTL_imperativeocl_TupleExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTL_imperativeocl_TupleExp)
gen_JTL_imperativeocl_Typedef_Class = Generalization(general=Class_, specific=JTL_imperativeocl_Typedef)
gen_JTL_imperativeocl_InstantiationExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTL_imperativeocl_InstantiationExp)
gen_JTL_imperativeocl_UnlinkExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTL_imperativeocl_UnlinkExp)
gen_JTL_imperativeocl_ReturnExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTL_imperativeocl_ReturnExp)
gen_JTL_imperativeocl_BreakExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTL_imperativeocl_BreakExp)
gen_JTL_imperativeocl_TryExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTL_imperativeocl_TryExp)
gen_JTL_imperativeocl_AssertExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTL_imperativeocl_AssertExp)
gen_JTL_imperativeocl_ImperativeLoopExp_essentialocl_LoopExp = Generalization(general=essentialocl_LoopExp, specific=JTL_imperativeocl_ImperativeLoopExp)
gen_JTL_imperativeocl_ImperativeLoopExp_imperativeocl_ImperativeExpression = Generalization(general=imperativeocl_ImperativeExpression, specific=JTL_imperativeocl_ImperativeLoopExp)
gen_JTL_imperativeocl_CollectorExp_ImperativeLoopExp = Generalization(general=ImperativeLoopExp, specific=JTL_imperativeocl_CollectorExp)
gen_JTL_imperativeocl_ImperativeExpression_OclExpression = Generalization(general=OclExpression, specific=JTL_imperativeocl_ImperativeExpression)
gen_JTL_imperativeocl_UnpackExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTL_imperativeocl_UnpackExp)
gen_JTL_imperativeocl_DictionaryType_CollectionType = Generalization(general=CollectionType, specific=JTL_imperativeocl_DictionaryType)
gen_JTL_imperativeocl_DictLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=JTL_imperativeocl_DictLiteralExp)
gen_JTL_imperativeocl_DictLiteralPart_Element = Generalization(general=Element, specific=JTL_imperativeocl_DictLiteralPart)
gen_JTL_imperativeocl_TemplateParameterType_Type = Generalization(general=Type, specific=JTL_imperativeocl_TemplateParameterType)
gen_JTL_imperativeocl_LogExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=JTL_imperativeocl_LogExp)
gen_JTL_imperativeocl_AnonymousTupleType_Class = Generalization(general=Class_, specific=JTL_imperativeocl_AnonymousTupleType)
gen_JTL_imperativeocl_AnonymousTupleLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=JTL_imperativeocl_AnonymousTupleLiteralExp)
gen_JTL_imperativeocl_AnonymousTupleLiteralPart_Element = Generalization(general=Element, specific=JTL_imperativeocl_AnonymousTupleLiteralPart)
gen_JTL_imperativeocl_ListType_CollectionType = Generalization(general=CollectionType, specific=JTL_imperativeocl_ListType)

# Domain Model
domain_model = DomainModel(
    name="JTL",
    types={Operation, Class_, JTL_emof_DataType, JTL_emof_Element, Object, Tag, Comment, JTL_emof_Tag, Element, JTL_emof_Enumeration, DataType, EnumerationLiteral, JTL_emof_NamedElement, JTL_emof_Class, Type, Property_, JTL_emof_Package, NamedElement, Package, JTL_emof_Type, JTL_emof_Parameter, JTL_emof_EnumerationLiteral, Enumeration_, JTL_emof_Property, JTL_emof_Extent, JTL_emof_Object, JTL_emof_Operation, emof_MultiplicityElement, emof_TypedElement, Parameter_, JTL_emof_MultiplicityElement, JTL_JTL_Relation, Transformation, Domain, Where, When, Variable, JTL_JTL_Domain, Pattern, JTL_JTL_Model, JTL_emof_TypedElement, JTL_emof_PrimitiveType, JTL_emof_URIExtent, Extent, JTL_emof_Comment, JTL_JTL_Transformation, emof_Class, emof_Package, Model, Relation, JTL_essentialocl_BooleanLiteralExp, PrimitiveLiteralExp, JTL_essentialocl_CallExp, JTL_essentialocl_OclExpression, TypedElement, TryExp, JTL_essentialocl_UnlimitedNaturalExp, NumericLiteralExp, JTL_essentialocl_IfExp, JTL_JTL_Pattern, Predicate, TemplateExp, JTL_JTL_Predicate, OclExpression, JTL_JTL_When, JTL_JTL_Where, JTL_essentialocl_VariableExp, JTL_essentialocl_TypeExp, JTL_essentialocl_LoopExp, essentialocl_CallExp, essentialocl_OclExpression, JTL_essentialocl_IteratorExp, LoopExp, JTL_essentialocl_StringLiteralExp, JTL_essentialocl_IntegerLiteralExp, JTL_essentialocl_OperationCallExp, JTL_essentialocl_LetExp, JTL_essentialocl_Variable, LetExp, ComputeExp, JTL_essentialocl_PropertyCallExp, FeaturePropertyCall, JTL_essentialocl_CollectionItem, JTL_essentialocl_CollectionRange, JTL_essentialocl_TupleLiteralExp, TupleLiteralPart, JTL_essentialocl_NullLiteralExp, JTL_essentialocl_ExpressionInOcl, OpaqueExpression, JTL_essentialocl_RealLiteralExp, JTL_essentialocl_LiteralExp, JTL_essentialocl_IterateExp, JTL_essentialocl_PrimitiveLiteralExp, LiteralExp, JTL_essentialocl_NumericLiteralExp, JTL_essentialocl_CollectionLiteralExp, CollectionLiteralPart, JTL_essentialocl_CollectionLiteralPart, CollectionLiteralExp, JTL_essentialocl_InvalidType, JTL_essentialocl_OrderedSetType, JTL_essentialocl_SequenceType, JTL_essentialocl_SetType, JTL_essentialocl_TupleType, emof_DataType, JTL_essentialocl_VoidType, JTL_essentialocl_AnyType, emof_Type, JTL_template_TemplateExp, JTL_essentialocl_OpaqueExpression, JTL_essentialocl_InvalidLiteralExp, JTL_essentialocl_FeaturePropertyCall, CallExp, JTL_essentialocl_TupleLiteralPart, TupleLiteralExp, JTL_essentialocl_BagType, CollectionType, JTL_essentialocl_CollectionType, JTL_essentialocl_EnumLiteralExp, JTL_template_PropertyTemplateItem, ObjectTemplateExp, JTL_imperativeocl_ImperativeIterateExp, ImperativeLoopExp, JTL_imperativeocl_AssignExp, ImperativeExpression, JTL_template_ObjectTemplateExp, PropertyTemplateItem, AssignExp, JTL_template_CollectionTemplateExp, JTL_imperativeocl_WhileExp, JTL_imperativeocl_ComputeExp, JTL_imperativeocl_AltExp, JTL_imperativeocl_UnlinkExp, JTL_imperativeocl_BlockExp, JTL_imperativeocl_SwitchExp, imperativeocl_ImperativeExpression, AltExp, JTL_imperativeocl_VariableInitExp, JTL_imperativeocl_RaiseExp, JTL_imperativeocl_ContinueExp, JTL_imperativeocl_ForExp, JTL_imperativeocl_TupleExp, JTL_imperativeocl_Typedef, JTL_imperativeocl_InstantiationExp, JTL_imperativeocl_ReturnExp, JTL_imperativeocl_BreakExp, JTL_imperativeocl_TryExp, JTL_imperativeocl_AssertExp, LogExp, JTL_imperativeocl_ImperativeLoopExp, essentialocl_LoopExp, JTL_imperativeocl_CollectorExp, JTL_imperativeocl_ImperativeExpression, JTL_imperativeocl_UnpackExp, JTL_imperativeocl_DictionaryType, JTL_imperativeocl_DictLiteralExp, DictLiteralPart, JTL_imperativeocl_DictLiteralPart, JTL_imperativeocl_TemplateParameterType, JTL_imperativeocl_LogExp, JTL_imperativeocl_AnonymousTupleType, JTL_imperativeocl_AnonymousTupleLiteralExp, AnonymousTupleLiteralPart, JTL_imperativeocl_AnonymousTupleLiteralPart, JTL_imperativeocl_ListType, CollectionKind, SeverityKind},
    associations={ownedOperation1, superClass2, tag4, ownedComment5, element6, ownedLiteral7, ownedAttribute0, ownedType12, nestedPackage14, package15, operation17, enumeration19, Class20, opposite22, class_8, ownedParameter10, raisedException11, transformation28, domain29, where31, when32, variable33, relation34, pattern36, model37, rootVariable40, transformation43, dependsOn45, annotatedElement24, modelParameter25, relation26, source62, tryBodyOwner64, condition65, thenExpression67, elseExpression70, predicate47, bindsTo48, templateExpression50, domain52, pattern55, conditionExpression57, whenOwner58, whereOwner60, referredVariable87, referredType89, body91, iterator93, argument96, in_73, variable75, initExpression77, LetExp79, bindParameter81, computeOwner84, referredProperty85, CollectionLiteralExp104, item106, first108, last110, part113, bodyExpression114, context116, resultVariable119, referredOperation98, result101, part103, parameterVariable122, TupleLiteralExp125, elementType128, referredEnumLiteral130, referredCollectionType141, match143, objContainer146, value148, referredProperty150, target153, value155, bindsTo132, where134, part137, inside138, part139, referredVariable169, condition171, body173, returnedElement176, body178, condition180, body182, left157, defaultValue160, body163, alternativePart165, elsePart166, exception199, element201, base203, condition205, instantiatedClass208, extent210, argument213, target185, item187, value190, tryBody192, exception194, exceptBody196, element226, log229, assertion230, condition233, target235, keyType216, part218, key219, value221, condition224, variable237, elementType239, part241, value242},
    generalizations={gen_JTL_emof_DataType_Type, gen_JTL_emof_Element_Object, gen_JTL_emof_Tag_Element, gen_JTL_emof_Enumeration_DataType, gen_JTL_emof_NamedElement_Element, gen_JTL_emof_Class_Type, gen_JTL_emof_Package_NamedElement, gen_JTL_emof_Type_NamedElement, gen_JTL_emof_Parameter_emof_MultiplicityElement, gen_JTL_emof_Parameter_emof_TypedElement, gen_JTL_emof_EnumerationLiteral_NamedElement, gen_JTL_emof_Property_emof_MultiplicityElement, gen_JTL_emof_Property_emof_TypedElement, gen_JTL_emof_Extent_Object, gen_JTL_emof_Operation_emof_MultiplicityElement, gen_JTL_emof_Operation_emof_TypedElement, gen_JTL_JTL_Relation_NamedElement, gen_JTL_JTL_Domain_NamedElement, gen_JTL_JTL_Model_NamedElement, gen_JTL_emof_TypedElement_NamedElement, gen_JTL_emof_PrimitiveType_DataType, gen_JTL_emof_URIExtent_Extent, gen_JTL_emof_Comment_Element, gen_JTL_JTL_Transformation_emof_Class, gen_JTL_JTL_Transformation_emof_Package, gen_JTL_essentialocl_BooleanLiteralExp_PrimitiveLiteralExp, gen_JTL_essentialocl_CallExp_OclExpression, gen_JTL_essentialocl_OclExpression_TypedElement, gen_JTL_essentialocl_UnlimitedNaturalExp_NumericLiteralExp, gen_JTL_essentialocl_IfExp_OclExpression, gen_JTL_JTL_Pattern_Element, gen_JTL_JTL_Predicate_Element, gen_JTL_JTL_When_Pattern, gen_JTL_JTL_Where_Pattern, gen_JTL_essentialocl_VariableExp_OclExpression, gen_JTL_essentialocl_TypeExp_OclExpression, gen_JTL_essentialocl_LoopExp_essentialocl_CallExp, gen_JTL_essentialocl_LoopExp_essentialocl_OclExpression, gen_JTL_essentialocl_IteratorExp_LoopExp, gen_JTL_essentialocl_StringLiteralExp_PrimitiveLiteralExp, gen_JTL_essentialocl_IntegerLiteralExp_NumericLiteralExp, gen_JTL_essentialocl_OperationCallExp_FeaturePropertyCall, gen_JTL_essentialocl_LetExp_OclExpression, gen_JTL_essentialocl_Variable_TypedElement, gen_JTL_essentialocl_PropertyCallExp_FeaturePropertyCall, gen_JTL_essentialocl_CollectionItem_CollectionLiteralPart, gen_JTL_essentialocl_CollectionRange_CollectionLiteralPart, gen_JTL_essentialocl_TupleLiteralExp_LiteralExp, gen_JTL_essentialocl_NullLiteralExp_LiteralExp, gen_JTL_essentialocl_ExpressionInOcl_OpaqueExpression, gen_JTL_essentialocl_RealLiteralExp_NumericLiteralExp, gen_JTL_essentialocl_LiteralExp_OclExpression, gen_JTL_essentialocl_IterateExp_LoopExp, gen_JTL_essentialocl_PrimitiveLiteralExp_LiteralExp, gen_JTL_essentialocl_NumericLiteralExp_PrimitiveLiteralExp, gen_JTL_essentialocl_CollectionLiteralExp_LiteralExp, gen_JTL_essentialocl_CollectionLiteralPart_TypedElement, gen_JTL_essentialocl_InvalidType_Type, gen_JTL_essentialocl_OrderedSetType_CollectionType, gen_JTL_essentialocl_SequenceType_CollectionType, gen_JTL_essentialocl_SetType_CollectionType, gen_JTL_essentialocl_TupleType_emof_Class, gen_JTL_essentialocl_TupleType_emof_DataType, gen_JTL_essentialocl_VoidType_Type, gen_JTL_essentialocl_AnyType_emof_Class, gen_JTL_essentialocl_AnyType_emof_Type, gen_JTL_template_TemplateExp_LiteralExp, gen_JTL_essentialocl_InvalidLiteralExp_LiteralExp, gen_JTL_essentialocl_FeaturePropertyCall_CallExp, gen_JTL_essentialocl_TupleLiteralPart_TypedElement, gen_JTL_essentialocl_BagType_CollectionType, gen_JTL_essentialocl_CollectionType_DataType, gen_JTL_essentialocl_EnumLiteralExp_LiteralExp, gen_JTL_template_PropertyTemplateItem_Element, gen_JTL_imperativeocl_ImperativeIterateExp_ImperativeLoopExp, gen_JTL_imperativeocl_AssignExp_ImperativeExpression, gen_JTL_template_ObjectTemplateExp_TemplateExp, gen_JTL_template_CollectionTemplateExp_TemplateExp, gen_JTL_imperativeocl_VariableInitExp_ImperativeExpression, gen_JTL_imperativeocl_WhileExp_ImperativeExpression, gen_JTL_imperativeocl_ComputeExp_ImperativeExpression, gen_JTL_imperativeocl_AltExp_ImperativeExpression, gen_JTL_imperativeocl_BlockExp_ImperativeExpression, gen_JTL_imperativeocl_SwitchExp_essentialocl_CallExp, gen_JTL_imperativeocl_SwitchExp_imperativeocl_ImperativeExpression, gen_JTL_imperativeocl_RaiseExp_ImperativeExpression, gen_JTL_imperativeocl_ContinueExp_ImperativeExpression, gen_JTL_imperativeocl_ForExp_ImperativeLoopExp, gen_JTL_imperativeocl_TupleExp_ImperativeExpression, gen_JTL_imperativeocl_Typedef_Class, gen_JTL_imperativeocl_InstantiationExp_ImperativeExpression, gen_JTL_imperativeocl_UnlinkExp_ImperativeExpression, gen_JTL_imperativeocl_ReturnExp_ImperativeExpression, gen_JTL_imperativeocl_BreakExp_ImperativeExpression, gen_JTL_imperativeocl_TryExp_ImperativeExpression, gen_JTL_imperativeocl_AssertExp_ImperativeExpression, gen_JTL_imperativeocl_ImperativeLoopExp_essentialocl_LoopExp, gen_JTL_imperativeocl_ImperativeLoopExp_imperativeocl_ImperativeExpression, gen_JTL_imperativeocl_CollectorExp_ImperativeLoopExp, gen_JTL_imperativeocl_ImperativeExpression_OclExpression, gen_JTL_imperativeocl_UnpackExp_ImperativeExpression, gen_JTL_imperativeocl_DictionaryType_CollectionType, gen_JTL_imperativeocl_DictLiteralExp_LiteralExp, gen_JTL_imperativeocl_DictLiteralPart_Element, gen_JTL_imperativeocl_TemplateParameterType_Type, gen_JTL_imperativeocl_LogExp_ImperativeExpression, gen_JTL_imperativeocl_AnonymousTupleType_Class, gen_JTL_imperativeocl_AnonymousTupleLiteralExp_LiteralExp, gen_JTL_imperativeocl_AnonymousTupleLiteralPart_Element, gen_JTL_imperativeocl_ListType_CollectionType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)