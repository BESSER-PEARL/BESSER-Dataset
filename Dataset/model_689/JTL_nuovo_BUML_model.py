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
Class_ = Class(name="Class")
Janus_emof_DataType = Class(name="Janus_emof_DataType", is_abstract=True)
Janus_emof_Element = Class(name="Janus_emof_Element", is_abstract=True)
Object = Class(name="Object")
Tag = Class(name="Tag")
Comment = Class(name="Comment")
Janus_emof_Tag = Class(name="Janus_emof_Tag")
Element = Class(name="Element")
Janus_emof_Class = Class(name="Janus_emof_Class")
Type = Class(name="Type")
Property_ = Class(name="Property")
Operation = Class(name="Operation")
Janus_emof_Parameter = Class(name="Janus_emof_Parameter")
Janus_emof_EnumerationLiteral = Class(name="Janus_emof_EnumerationLiteral")
Enumeration_ = Class(name="Enumeration")
Janus_emof_Property = Class(name="Janus_emof_Property")
Janus_emof_Enumeration = Class(name="Janus_emof_Enumeration")
DataType = Class(name="DataType")
EnumerationLiteral = Class(name="EnumerationLiteral")
Janus_emof_NamedElement = Class(name="Janus_emof_NamedElement", is_abstract=True)
Janus_emof_Extent = Class(name="Janus_emof_Extent")
Janus_emof_Object = Class(name="Janus_emof_Object")
Janus_emof_Operation = Class(name="Janus_emof_Operation")
emof_MultiplicityElement = Class(name="emof_MultiplicityElement")
emof_TypedElement = Class(name="emof_TypedElement")
Parameter_ = Class(name="Parameter")
Janus_emof_MultiplicityElement = Class(name="Janus_emof_MultiplicityElement", is_abstract=True)
Janus_emof_Package = Class(name="Janus_emof_Package")
NamedElement = Class(name="NamedElement")
Package = Class(name="Package")
Janus_emof_Type = Class(name="Janus_emof_Type", is_abstract=True)
Variable = Class(name="Variable")
Janus_JTL_Domain = Class(name="Janus_JTL_Domain")
Janus_JTL_Model = Class(name="Janus_JTL_Model")
Janus_emof_TypedElement = Class(name="Janus_emof_TypedElement", is_abstract=True)
Janus_emof_PrimitiveType = Class(name="Janus_emof_PrimitiveType")
Janus_emof_URIExtent = Class(name="Janus_emof_URIExtent")
Extent = Class(name="Extent")
Janus_emof_Comment = Class(name="Janus_emof_Comment")
Janus_JTL_Transformation = Class(name="Janus_JTL_Transformation")
emof_Class = Class(name="emof_Class")
emof_Package = Class(name="emof_Package")
Model = Class(name="Model")
Relation = Class(name="Relation")
Janus_JTL_Relation = Class(name="Janus_JTL_Relation")
Transformation = Class(name="Transformation")
Domain = Class(name="Domain")
Pattern = Class(name="Pattern")
Janus_essentialocl_OclExpression = Class(name="Janus_essentialocl_OclExpression", is_abstract=True)
TypedElement = Class(name="TypedElement")
TryExp = Class(name="TryExp")
Janus_essentialocl_UnlimitedNaturalExp = Class(name="Janus_essentialocl_UnlimitedNaturalExp")
NumericLiteralExp = Class(name="NumericLiteralExp")
Janus_essentialocl_IfExp = Class(name="Janus_essentialocl_IfExp")
Janus_JTL_Pattern = Class(name="Janus_JTL_Pattern")
Predicate = Class(name="Predicate")
TemplateExp = Class(name="TemplateExp")
Janus_JTL_Predicate = Class(name="Janus_JTL_Predicate")
OclExpression = Class(name="OclExpression")
Janus_essentialocl_BooleanLiteralExp = Class(name="Janus_essentialocl_BooleanLiteralExp")
PrimitiveLiteralExp = Class(name="PrimitiveLiteralExp")
Janus_essentialocl_CallExp = Class(name="Janus_essentialocl_CallExp", is_abstract=True)
essentialocl_CallExp = Class(name="essentialocl_CallExp")
essentialocl_OclExpression = Class(name="essentialocl_OclExpression")
Janus_essentialocl_IteratorExp = Class(name="Janus_essentialocl_IteratorExp")
LoopExp = Class(name="LoopExp")
Janus_essentialocl_StringLiteralExp = Class(name="Janus_essentialocl_StringLiteralExp")
Janus_essentialocl_IntegerLiteralExp = Class(name="Janus_essentialocl_IntegerLiteralExp")
Janus_essentialocl_OperationCallExp = Class(name="Janus_essentialocl_OperationCallExp")
Janus_essentialocl_RealLiteralExp = Class(name="Janus_essentialocl_RealLiteralExp")
Janus_essentialocl_LetExp = Class(name="Janus_essentialocl_LetExp")
Janus_essentialocl_Variable = Class(name="Janus_essentialocl_Variable")
LetExp = Class(name="LetExp")
ComputeExp = Class(name="ComputeExp")
Janus_essentialocl_PropertyCallExp = Class(name="Janus_essentialocl_PropertyCallExp")
FeaturePropertyCall = Class(name="FeaturePropertyCall")
Janus_essentialocl_VariableExp = Class(name="Janus_essentialocl_VariableExp")
Janus_essentialocl_TypeExp = Class(name="Janus_essentialocl_TypeExp")
Janus_essentialocl_LoopExp = Class(name="Janus_essentialocl_LoopExp", is_abstract=True)
TupleLiteralPart = Class(name="TupleLiteralPart")
Janus_essentialocl_NullLiteralExp = Class(name="Janus_essentialocl_NullLiteralExp")
Janus_essentialocl_ExpressionInOcl = Class(name="Janus_essentialocl_ExpressionInOcl")
OpaqueExpression = Class(name="OpaqueExpression")
Janus_essentialocl_OpaqueExpression = Class(name="Janus_essentialocl_OpaqueExpression")
Janus_essentialocl_InvalidLiteralExp = Class(name="Janus_essentialocl_InvalidLiteralExp")
Janus_essentialocl_FeaturePropertyCall = Class(name="Janus_essentialocl_FeaturePropertyCall", is_abstract=True)
CallExp = Class(name="CallExp")
Janus_essentialocl_TupleLiteralPart = Class(name="Janus_essentialocl_TupleLiteralPart")
TupleLiteralExp = Class(name="TupleLiteralExp")
Janus_essentialocl_LiteralExp = Class(name="Janus_essentialocl_LiteralExp", is_abstract=True)
Janus_essentialocl_IterateExp = Class(name="Janus_essentialocl_IterateExp")
Janus_essentialocl_PrimitiveLiteralExp = Class(name="Janus_essentialocl_PrimitiveLiteralExp", is_abstract=True)
LiteralExp = Class(name="LiteralExp")
Janus_essentialocl_NumericLiteralExp = Class(name="Janus_essentialocl_NumericLiteralExp", is_abstract=True)
Janus_essentialocl_CollectionLiteralExp = Class(name="Janus_essentialocl_CollectionLiteralExp")
CollectionLiteralPart = Class(name="CollectionLiteralPart")
Janus_essentialocl_CollectionLiteralPart = Class(name="Janus_essentialocl_CollectionLiteralPart", is_abstract=True)
CollectionLiteralExp = Class(name="CollectionLiteralExp")
Janus_essentialocl_CollectionItem = Class(name="Janus_essentialocl_CollectionItem")
Janus_essentialocl_CollectionRange = Class(name="Janus_essentialocl_CollectionRange")
Janus_essentialocl_TupleLiteralExp = Class(name="Janus_essentialocl_TupleLiteralExp")
Janus_template_CollectionTemplateExp = Class(name="Janus_template_CollectionTemplateExp")
Janus_template_PropertyTemplateItem = Class(name="Janus_template_PropertyTemplateItem")
ObjectTemplateExp = Class(name="ObjectTemplateExp")
Janus_essentialocl_BagType = Class(name="Janus_essentialocl_BagType")
CollectionType = Class(name="CollectionType")
Janus_essentialocl_CollectionType = Class(name="Janus_essentialocl_CollectionType", is_abstract=True)
Janus_essentialocl_EnumLiteralExp = Class(name="Janus_essentialocl_EnumLiteralExp")
Janus_essentialocl_InvalidType = Class(name="Janus_essentialocl_InvalidType")
Janus_essentialocl_OrderedSetType = Class(name="Janus_essentialocl_OrderedSetType")
Janus_essentialocl_SequenceType = Class(name="Janus_essentialocl_SequenceType")
Janus_essentialocl_SetType = Class(name="Janus_essentialocl_SetType")
Janus_essentialocl_TupleType = Class(name="Janus_essentialocl_TupleType")
emof_DataType = Class(name="emof_DataType")
Janus_essentialocl_VoidType = Class(name="Janus_essentialocl_VoidType")
Janus_essentialocl_AnyType = Class(name="Janus_essentialocl_AnyType")
emof_Type = Class(name="emof_Type")
Janus_template_TemplateExp = Class(name="Janus_template_TemplateExp", is_abstract=True)
Janus_template_ObjectTemplateExp = Class(name="Janus_template_ObjectTemplateExp")
PropertyTemplateItem = Class(name="PropertyTemplateItem")
Janus_imperativeocl_WhileExp = Class(name="Janus_imperativeocl_WhileExp")
Janus_imperativeocl_ComputeExp = Class(name="Janus_imperativeocl_ComputeExp")
Janus_imperativeocl_ImperativeIterateExp = Class(name="Janus_imperativeocl_ImperativeIterateExp")
ImperativeLoopExp = Class(name="ImperativeLoopExp")
Janus_imperativeocl_AssignExp = Class(name="Janus_imperativeocl_AssignExp")
ImperativeExpression = Class(name="ImperativeExpression")
Janus_imperativeocl_BlockExp = Class(name="Janus_imperativeocl_BlockExp")
Janus_imperativeocl_SwitchExp = Class(name="Janus_imperativeocl_SwitchExp")
imperativeocl_ImperativeExpression = Class(name="imperativeocl_ImperativeExpression")
AltExp = Class(name="AltExp")
Janus_imperativeocl_VariableInitExp = Class(name="Janus_imperativeocl_VariableInitExp")
Janus_imperativeocl_RaiseExp = Class(name="Janus_imperativeocl_RaiseExp")
Janus_imperativeocl_ContinueExp = Class(name="Janus_imperativeocl_ContinueExp")
Janus_imperativeocl_ForExp = Class(name="Janus_imperativeocl_ForExp")
Janus_imperativeocl_TupleExp = Class(name="Janus_imperativeocl_TupleExp")
Janus_imperativeocl_Typedef = Class(name="Janus_imperativeocl_Typedef")
Janus_imperativeocl_AltExp = Class(name="Janus_imperativeocl_AltExp")
Janus_imperativeocl_UnlinkExp = Class(name="Janus_imperativeocl_UnlinkExp")
Janus_imperativeocl_ReturnExp = Class(name="Janus_imperativeocl_ReturnExp")
Janus_imperativeocl_BreakExp = Class(name="Janus_imperativeocl_BreakExp")
Janus_imperativeocl_TryExp = Class(name="Janus_imperativeocl_TryExp")
Janus_imperativeocl_LogExp = Class(name="Janus_imperativeocl_LogExp")
Janus_imperativeocl_AssertExp = Class(name="Janus_imperativeocl_AssertExp")
LogExp = Class(name="LogExp")
Janus_imperativeocl_InstantiationExp = Class(name="Janus_imperativeocl_InstantiationExp")
Janus_imperativeocl_DictionaryType = Class(name="Janus_imperativeocl_DictionaryType")
Janus_imperativeocl_DictLiteralExp = Class(name="Janus_imperativeocl_DictLiteralExp")
DictLiteralPart = Class(name="DictLiteralPart")
Janus_imperativeocl_DictLiteralPart = Class(name="Janus_imperativeocl_DictLiteralPart")
Janus_imperativeocl_TemplateParameterType = Class(name="Janus_imperativeocl_TemplateParameterType")
Janus_imperativeocl_ListType = Class(name="Janus_imperativeocl_ListType")
Janus_imperativeocl_ImperativeLoopExp = Class(name="Janus_imperativeocl_ImperativeLoopExp", is_abstract=True)
essentialocl_LoopExp = Class(name="essentialocl_LoopExp")
Janus_imperativeocl_CollectorExp = Class(name="Janus_imperativeocl_CollectorExp")
Janus_imperativeocl_ImperativeExpression = Class(name="Janus_imperativeocl_ImperativeExpression", is_abstract=True)
Janus_imperativeocl_UnpackExp = Class(name="Janus_imperativeocl_UnpackExp")
Janus_imperativeocl_AnonymousTupleType = Class(name="Janus_imperativeocl_AnonymousTupleType")
Janus_imperativeocl_AnonymousTupleLiteralExp = Class(name="Janus_imperativeocl_AnonymousTupleLiteralExp")
AnonymousTupleLiteralPart = Class(name="AnonymousTupleLiteralPart")
Janus_imperativeocl_AnonymousTupleLiteralPart = Class(name="Janus_imperativeocl_AnonymousTupleLiteralPart")

# Class class attributes and methods

# Janus_emof_DataType class attributes and methods

# Janus_emof_Element class attributes and methods

# Object class attributes and methods

# Tag class attributes and methods

# Comment class attributes and methods

# Janus_emof_Tag class attributes and methods
Janus_emof_Tag_value: Property = Property(name="value", type=StringType)
Janus_emof_Tag_name: Property = Property(name="name", type=StringType)
Janus_emof_Tag.attributes={Janus_emof_Tag_value, Janus_emof_Tag_name}

# Element class attributes and methods

# Janus_emof_Class class attributes and methods
Janus_emof_Class_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
Janus_emof_Class.attributes={Janus_emof_Class_isAbstract}

# Type class attributes and methods

# Property class attributes and methods

# Operation class attributes and methods

# Janus_emof_Parameter class attributes and methods

# Janus_emof_EnumerationLiteral class attributes and methods

# Enumeration class attributes and methods

# Janus_emof_Property class attributes and methods
Janus_emof_Property_isReadOnly: Property = Property(name="isReadOnly", type=BooleanType)
Janus_emof_Property_isDerived: Property = Property(name="isDerived", type=BooleanType)
Janus_emof_Property_isComposite: Property = Property(name="isComposite", type=BooleanType)
Janus_emof_Property_isId: Property = Property(name="isId", type=BooleanType)
Janus_emof_Property_default: Property = Property(name="default", type=StringType)
Janus_emof_Property.attributes={Janus_emof_Property_isDerived, Janus_emof_Property_isReadOnly, Janus_emof_Property_default, Janus_emof_Property_isComposite, Janus_emof_Property_isId}

# Janus_emof_Enumeration class attributes and methods

# DataType class attributes and methods

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

# Janus_emof_MultiplicityElement class attributes and methods
Janus_emof_MultiplicityElement_isOrdered: Property = Property(name="isOrdered", type=StringType)
Janus_emof_MultiplicityElement_isUnique: Property = Property(name="isUnique", type=StringType)
Janus_emof_MultiplicityElement_lower: Property = Property(name="lower", type=IntegerType)
Janus_emof_MultiplicityElement_upper: Property = Property(name="upper", type=StringType)
Janus_emof_MultiplicityElement.attributes={Janus_emof_MultiplicityElement_lower, Janus_emof_MultiplicityElement_isUnique, Janus_emof_MultiplicityElement_isOrdered, Janus_emof_MultiplicityElement_upper}

# Janus_emof_Package class attributes and methods
Janus_emof_Package_uri: Property = Property(name="uri", type=StringType)
Janus_emof_Package.attributes={Janus_emof_Package_uri}

# NamedElement class attributes and methods

# Package class attributes and methods

# Janus_emof_Type class attributes and methods

# Variable class attributes and methods

# Janus_JTL_Domain class attributes and methods
Janus_JTL_Domain_isCheckable: Property = Property(name="isCheckable", type=BooleanType)
Janus_JTL_Domain_isEnforceable: Property = Property(name="isEnforceable", type=BooleanType)
Janus_JTL_Domain.attributes={Janus_JTL_Domain_isEnforceable, Janus_JTL_Domain_isCheckable}

# Janus_JTL_Model class attributes and methods

# Janus_emof_TypedElement class attributes and methods

# Janus_emof_PrimitiveType class attributes and methods

# Janus_emof_URIExtent class attributes and methods

# Extent class attributes and methods

# Janus_emof_Comment class attributes and methods

# Janus_JTL_Transformation class attributes and methods

# emof_Class class attributes and methods

# emof_Package class attributes and methods

# Model class attributes and methods

# Relation class attributes and methods

# Janus_JTL_Relation class attributes and methods
Janus_JTL_Relation_isTopLevel: Property = Property(name="isTopLevel", type=BooleanType)
Janus_JTL_Relation.attributes={Janus_JTL_Relation_isTopLevel}

# Transformation class attributes and methods

# Domain class attributes and methods

# Pattern class attributes and methods

# Janus_essentialocl_OclExpression class attributes and methods

# TypedElement class attributes and methods

# TryExp class attributes and methods

# Janus_essentialocl_UnlimitedNaturalExp class attributes and methods
Janus_essentialocl_UnlimitedNaturalExp_symbol: Property = Property(name="symbol", type=StringType)
Janus_essentialocl_UnlimitedNaturalExp.attributes={Janus_essentialocl_UnlimitedNaturalExp_symbol}

# NumericLiteralExp class attributes and methods

# Janus_essentialocl_IfExp class attributes and methods

# Janus_JTL_Pattern class attributes and methods

# Predicate class attributes and methods

# TemplateExp class attributes and methods

# Janus_JTL_Predicate class attributes and methods

# OclExpression class attributes and methods

# Janus_essentialocl_BooleanLiteralExp class attributes and methods
Janus_essentialocl_BooleanLiteralExp_booleanSymbol: Property = Property(name="booleanSymbol", type=BooleanType)
Janus_essentialocl_BooleanLiteralExp.attributes={Janus_essentialocl_BooleanLiteralExp_booleanSymbol}

# PrimitiveLiteralExp class attributes and methods

# Janus_essentialocl_CallExp class attributes and methods

# essentialocl_CallExp class attributes and methods

# essentialocl_OclExpression class attributes and methods

# Janus_essentialocl_IteratorExp class attributes and methods

# LoopExp class attributes and methods

# Janus_essentialocl_StringLiteralExp class attributes and methods
Janus_essentialocl_StringLiteralExp_stringSymbol: Property = Property(name="stringSymbol", type=StringType)
Janus_essentialocl_StringLiteralExp.attributes={Janus_essentialocl_StringLiteralExp_stringSymbol}

# Janus_essentialocl_IntegerLiteralExp class attributes and methods
Janus_essentialocl_IntegerLiteralExp_integerSymbol: Property = Property(name="integerSymbol", type=IntegerType)
Janus_essentialocl_IntegerLiteralExp.attributes={Janus_essentialocl_IntegerLiteralExp_integerSymbol}

# Janus_essentialocl_OperationCallExp class attributes and methods

# Janus_essentialocl_RealLiteralExp class attributes and methods
Janus_essentialocl_RealLiteralExp_realSymbol: Property = Property(name="realSymbol", type=FloatType)
Janus_essentialocl_RealLiteralExp.attributes={Janus_essentialocl_RealLiteralExp_realSymbol}

# Janus_essentialocl_LetExp class attributes and methods

# Janus_essentialocl_Variable class attributes and methods
Janus_essentialocl_Variable_varType: Property = Property(name="varType", type=StringType)
Janus_essentialocl_Variable.attributes={Janus_essentialocl_Variable_varType}

# LetExp class attributes and methods

# ComputeExp class attributes and methods

# Janus_essentialocl_PropertyCallExp class attributes and methods

# FeaturePropertyCall class attributes and methods

# Janus_essentialocl_VariableExp class attributes and methods

# Janus_essentialocl_TypeExp class attributes and methods

# Janus_essentialocl_LoopExp class attributes and methods

# TupleLiteralPart class attributes and methods

# Janus_essentialocl_NullLiteralExp class attributes and methods

# Janus_essentialocl_ExpressionInOcl class attributes and methods

# OpaqueExpression class attributes and methods

# Janus_essentialocl_OpaqueExpression class attributes and methods

# Janus_essentialocl_InvalidLiteralExp class attributes and methods

# Janus_essentialocl_FeaturePropertyCall class attributes and methods

# CallExp class attributes and methods

# Janus_essentialocl_TupleLiteralPart class attributes and methods

# TupleLiteralExp class attributes and methods

# Janus_essentialocl_LiteralExp class attributes and methods

# Janus_essentialocl_IterateExp class attributes and methods

# Janus_essentialocl_PrimitiveLiteralExp class attributes and methods

# LiteralExp class attributes and methods

# Janus_essentialocl_NumericLiteralExp class attributes and methods

# Janus_essentialocl_CollectionLiteralExp class attributes and methods
Janus_essentialocl_CollectionLiteralExp_kind: Property = Property(name="kind", type=StringType)
Janus_essentialocl_CollectionLiteralExp.attributes={Janus_essentialocl_CollectionLiteralExp_kind}

# CollectionLiteralPart class attributes and methods

# Janus_essentialocl_CollectionLiteralPart class attributes and methods

# CollectionLiteralExp class attributes and methods

# Janus_essentialocl_CollectionItem class attributes and methods

# Janus_essentialocl_CollectionRange class attributes and methods

# Janus_essentialocl_TupleLiteralExp class attributes and methods

# Janus_template_CollectionTemplateExp class attributes and methods
Janus_template_CollectionTemplateExp_kind: Property = Property(name="kind", type=StringType)
Janus_template_CollectionTemplateExp.attributes={Janus_template_CollectionTemplateExp_kind}

# Janus_template_PropertyTemplateItem class attributes and methods

# ObjectTemplateExp class attributes and methods

# Janus_essentialocl_BagType class attributes and methods

# CollectionType class attributes and methods

# Janus_essentialocl_CollectionType class attributes and methods

# Janus_essentialocl_EnumLiteralExp class attributes and methods

# Janus_essentialocl_InvalidType class attributes and methods

# Janus_essentialocl_OrderedSetType class attributes and methods

# Janus_essentialocl_SequenceType class attributes and methods

# Janus_essentialocl_SetType class attributes and methods

# Janus_essentialocl_TupleType class attributes and methods

# emof_DataType class attributes and methods

# Janus_essentialocl_VoidType class attributes and methods

# Janus_essentialocl_AnyType class attributes and methods

# emof_Type class attributes and methods

# Janus_template_TemplateExp class attributes and methods

# Janus_template_ObjectTemplateExp class attributes and methods
Janus_template_ObjectTemplateExp_referredClass: Property = Property(name="referredClass", type=StringType)
Janus_template_ObjectTemplateExp.attributes={Janus_template_ObjectTemplateExp_referredClass}

# PropertyTemplateItem class attributes and methods

# Janus_imperativeocl_WhileExp class attributes and methods

# Janus_imperativeocl_ComputeExp class attributes and methods

# Janus_imperativeocl_ImperativeIterateExp class attributes and methods

# ImperativeLoopExp class attributes and methods

# Janus_imperativeocl_AssignExp class attributes and methods
Janus_imperativeocl_AssignExp_isReset: Property = Property(name="isReset", type=BooleanType)
Janus_imperativeocl_AssignExp.attributes={Janus_imperativeocl_AssignExp_isReset}

# ImperativeExpression class attributes and methods

# Janus_imperativeocl_BlockExp class attributes and methods

# Janus_imperativeocl_SwitchExp class attributes and methods

# imperativeocl_ImperativeExpression class attributes and methods

# AltExp class attributes and methods

# Janus_imperativeocl_VariableInitExp class attributes and methods
Janus_imperativeocl_VariableInitExp_withResult: Property = Property(name="withResult", type=BooleanType)
Janus_imperativeocl_VariableInitExp.attributes={Janus_imperativeocl_VariableInitExp_withResult}

# Janus_imperativeocl_RaiseExp class attributes and methods

# Janus_imperativeocl_ContinueExp class attributes and methods

# Janus_imperativeocl_ForExp class attributes and methods

# Janus_imperativeocl_TupleExp class attributes and methods

# Janus_imperativeocl_Typedef class attributes and methods

# Janus_imperativeocl_AltExp class attributes and methods

# Janus_imperativeocl_UnlinkExp class attributes and methods

# Janus_imperativeocl_ReturnExp class attributes and methods

# Janus_imperativeocl_BreakExp class attributes and methods

# Janus_imperativeocl_TryExp class attributes and methods

# Janus_imperativeocl_LogExp class attributes and methods
Janus_imperativeocl_LogExp_text: Property = Property(name="text", type=StringType)
Janus_imperativeocl_LogExp_level: Property = Property(name="level", type=IntegerType)
Janus_imperativeocl_LogExp.attributes={Janus_imperativeocl_LogExp_level, Janus_imperativeocl_LogExp_text}

# Janus_imperativeocl_AssertExp class attributes and methods
Janus_imperativeocl_AssertExp_severity: Property = Property(name="severity", type=StringType)
Janus_imperativeocl_AssertExp.attributes={Janus_imperativeocl_AssertExp_severity}

# LogExp class attributes and methods

# Janus_imperativeocl_InstantiationExp class attributes and methods

# Janus_imperativeocl_DictionaryType class attributes and methods

# Janus_imperativeocl_DictLiteralExp class attributes and methods

# DictLiteralPart class attributes and methods

# Janus_imperativeocl_DictLiteralPart class attributes and methods

# Janus_imperativeocl_TemplateParameterType class attributes and methods
Janus_imperativeocl_TemplateParameterType_specification: Property = Property(name="specification", type=StringType)
Janus_imperativeocl_TemplateParameterType.attributes={Janus_imperativeocl_TemplateParameterType_specification}

# Janus_imperativeocl_ListType class attributes and methods

# Janus_imperativeocl_ImperativeLoopExp class attributes and methods

# essentialocl_LoopExp class attributes and methods

# Janus_imperativeocl_CollectorExp class attributes and methods

# Janus_imperativeocl_ImperativeExpression class attributes and methods

# Janus_imperativeocl_UnpackExp class attributes and methods

# Janus_imperativeocl_AnonymousTupleType class attributes and methods

# Janus_imperativeocl_AnonymousTupleLiteralExp class attributes and methods

# AnonymousTupleLiteralPart class attributes and methods

# Janus_imperativeocl_AnonymousTupleLiteralPart class attributes and methods

# Relationships
superClass2: BinaryAssociation = BinaryAssociation(
    name="superClass2",
    ends={
        Property(name="Class3", type=Janus_emof_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_emof_Class", type=Class_, multiplicity=Multiplicity(0, 9999))
    }
)
tag4: BinaryAssociation = BinaryAssociation(
    name="tag4",
    ends={
        Property(name="Tag", type=Janus_emof_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="element", type=Tag, multiplicity=Multiplicity(0, 9999))
    }
)
ownedComment5: BinaryAssociation = BinaryAssociation(
    name="ownedComment5",
    ends={
        Property(name="Comment", type=Janus_emof_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_emof_Element", type=Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
element6: BinaryAssociation = BinaryAssociation(
    name="element6",
    ends={
        Property(name="Element", type=Janus_emof_Tag, multiplicity=Multiplicity(1, 1)),
        Property(name="tag", type=Element, multiplicity=Multiplicity(0, 9999))
    }
)
ownedAttribute0: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute0",
    ends={
        Property(name="Property", type=Janus_emof_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Class", type=Property_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedOperation1: BinaryAssociation = BinaryAssociation(
    name="ownedOperation1",
    ends={
        Property(name="Operation", type=Janus_emof_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="class_", type=Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package15: BinaryAssociation = BinaryAssociation(
    name="package15",
    ends={
        Property(name="Package16", type=Janus_emof_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedType", type=Package, multiplicity=Multiplicity(1, 1))
    }
)
operation17: BinaryAssociation = BinaryAssociation(
    name="operation17",
    ends={
        Property(name="Operation18", type=Janus_emof_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedParameter", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
enumeration19: BinaryAssociation = BinaryAssociation(
    name="enumeration19",
    ends={
        Property(name="Enumeration", type=Janus_emof_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedLiteral", type=Enumeration_, multiplicity=Multiplicity(0, 1))
    }
)
Class20: BinaryAssociation = BinaryAssociation(
    name="Class20",
    ends={
        Property(name="Class21", type=Janus_emof_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedAttribute", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
opposite22: BinaryAssociation = BinaryAssociation(
    name="opposite22",
    ends={
        Property(name="Property23", type=Janus_emof_Property, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_emof_Property", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
ownedLiteral7: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral7",
    ends={
        Property(name="EnumerationLiteral", type=Janus_emof_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="enumeration", type=EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
class_8: BinaryAssociation = BinaryAssociation(
    name="class_8",
    ends={
        Property(name="Class9", type=Janus_emof_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedOperation", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
ownedParameter10: BinaryAssociation = BinaryAssociation(
    name="ownedParameter10",
    ends={
        Property(name="Parameter", type=Janus_emof_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operation", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
raisedException11: BinaryAssociation = BinaryAssociation(
    name="raisedException11",
    ends={
        Property(name="Type", type=Janus_emof_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_emof_Operation", type=Type, multiplicity=Multiplicity(0, 9999))
    }
)
ownedType12: BinaryAssociation = BinaryAssociation(
    name="ownedType12",
    ends={
        Property(name="Type13", type=Janus_emof_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="package", type=Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nestedPackage14: BinaryAssociation = BinaryAssociation(
    name="nestedPackage14",
    ends={
        Property(name="Package", type=Janus_emof_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_emof_Package", type=Package, multiplicity=Multiplicity(0, 9999))
    }
)
when34: BinaryAssociation = BinaryAssociation(
    name="when34",
    ends={
        Property(name="Pattern35", type=Janus_JTL_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="whenOwner", type=Pattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable36: BinaryAssociation = BinaryAssociation(
    name="variable36",
    ends={
        Property(name="Variable", type=Janus_JTL_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_JTL_Relation", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relation37: BinaryAssociation = BinaryAssociation(
    name="relation37",
    ends={
        Property(name="Relation38", type=Janus_JTL_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="domain", type=Relation, multiplicity=Multiplicity(1, 1))
    }
)
pattern39: BinaryAssociation = BinaryAssociation(
    name="pattern39",
    ends={
        Property(name="Pattern40", type=Janus_JTL_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_JTL_Domain", type=Pattern, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
model41: BinaryAssociation = BinaryAssociation(
    name="model41",
    ends={
        Property(name="Model43", type=Janus_JTL_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_JTL_Domain42", type=Model, multiplicity=Multiplicity(1, 1))
    }
)
rootVariable44: BinaryAssociation = BinaryAssociation(
    name="rootVariable44",
    ends={
        Property(name="Variable46", type=Janus_JTL_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_JTL_Domain45", type=Variable, multiplicity=Multiplicity(1, 1))
    }
)
transformation47: BinaryAssociation = BinaryAssociation(
    name="transformation47",
    ends={
        Property(name="Transformation48", type=Janus_JTL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="modelParameter", type=Transformation, multiplicity=Multiplicity(1, 1))
    }
)
type24: BinaryAssociation = BinaryAssociation(
    name="type24",
    ends={
        Property(name="Type25", type=Janus_emof_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_emof_TypedElement", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
annotatedElement26: BinaryAssociation = BinaryAssociation(
    name="annotatedElement26",
    ends={
        Property(name="NamedElement", type=Janus_emof_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_emof_Comment", type=NamedElement, multiplicity=Multiplicity(0, 9999))
    }
)
modelParameter27: BinaryAssociation = BinaryAssociation(
    name="modelParameter27",
    ends={
        Property(name="Model", type=Janus_JTL_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation", type=Model, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relation28: BinaryAssociation = BinaryAssociation(
    name="relation28",
    ends={
        Property(name="Relation", type=Janus_JTL_Transformation, multiplicity=Multiplicity(1, 1)),
        Property(name="transformation29", type=Relation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transformation30: BinaryAssociation = BinaryAssociation(
    name="transformation30",
    ends={
        Property(name="Transformation", type=Janus_JTL_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="relation", type=Transformation, multiplicity=Multiplicity(1, 1))
    }
)
domain31: BinaryAssociation = BinaryAssociation(
    name="domain31",
    ends={
        Property(name="Domain", type=Janus_JTL_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="relation32", type=Domain, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
where33: BinaryAssociation = BinaryAssociation(
    name="where33",
    ends={
        Property(name="Pattern", type=Janus_JTL_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="whereOwner", type=Pattern, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source69: BinaryAssociation = BinaryAssociation(
    name="source69",
    ends={
        Property(name="OclExpression70", type=Janus_essentialocl_CallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_CallExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tryBodyOwner71: BinaryAssociation = BinaryAssociation(
    name="tryBodyOwner71",
    ends={
        Property(name="TryExp", type=Janus_essentialocl_OclExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="tryBody", type=TryExp, multiplicity=Multiplicity(0, 1))
    }
)
condition72: BinaryAssociation = BinaryAssociation(
    name="condition72",
    ends={
        Property(name="OclExpression73", type=Janus_essentialocl_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_IfExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
thenExpression74: BinaryAssociation = BinaryAssociation(
    name="thenExpression74",
    ends={
        Property(name="OclExpression76", type=Janus_essentialocl_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_IfExp75", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseExpression77: BinaryAssociation = BinaryAssociation(
    name="elseExpression77",
    ends={
        Property(name="OclExpression79", type=Janus_essentialocl_IfExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_IfExp78", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
usedPackage49: BinaryAssociation = BinaryAssociation(
    name="usedPackage49",
    ends={
        Property(name="Package50", type=Janus_JTL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_JTL_Model", type=Package, multiplicity=Multiplicity(0, 9999))
    }
)
dependsOn51: BinaryAssociation = BinaryAssociation(
    name="dependsOn51",
    ends={
        Property(name="Model53", type=Janus_JTL_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_JTL_Model52", type=Model, multiplicity=Multiplicity(0, 9999))
    }
)
whereOwner54: BinaryAssociation = BinaryAssociation(
    name="whereOwner54",
    ends={
        Property(name="Relation55", type=Janus_JTL_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="where", type=Relation, multiplicity=Multiplicity(0, 1))
    }
)
whenOwner56: BinaryAssociation = BinaryAssociation(
    name="whenOwner56",
    ends={
        Property(name="Relation57", type=Janus_JTL_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="when", type=Relation, multiplicity=Multiplicity(0, 1))
    }
)
predicate58: BinaryAssociation = BinaryAssociation(
    name="predicate58",
    ends={
        Property(name="Predicate", type=Janus_JTL_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="pattern", type=Predicate, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bindsTo59: BinaryAssociation = BinaryAssociation(
    name="bindsTo59",
    ends={
        Property(name="Variable60", type=Janus_JTL_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_JTL_Pattern", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
templateExpression61: BinaryAssociation = BinaryAssociation(
    name="templateExpression61",
    ends={
        Property(name="TemplateExp", type=Janus_JTL_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_JTL_Pattern62", type=TemplateExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
domain63: BinaryAssociation = BinaryAssociation(
    name="domain63",
    ends={
        Property(name="Domain65", type=Janus_JTL_Pattern, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_JTL_Pattern64", type=Domain, multiplicity=Multiplicity(1, 1))
    }
)
pattern66: BinaryAssociation = BinaryAssociation(
    name="pattern66",
    ends={
        Property(name="Pattern67", type=Janus_JTL_Predicate, multiplicity=Multiplicity(1, 1)),
        Property(name="predicate", type=Pattern, multiplicity=Multiplicity(1, 1))
    }
)
conditionExpression68: BinaryAssociation = BinaryAssociation(
    name="conditionExpression68",
    ends={
        Property(name="OclExpression", type=Janus_JTL_Predicate, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_JTL_Predicate", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body98: BinaryAssociation = BinaryAssociation(
    name="body98",
    ends={
        Property(name="OclExpression99", type=Janus_essentialocl_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_LoopExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
iterator100: BinaryAssociation = BinaryAssociation(
    name="iterator100",
    ends={
        Property(name="Variable102", type=Janus_essentialocl_LoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_LoopExp101", type=Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument103: BinaryAssociation = BinaryAssociation(
    name="argument103",
    ends={
        Property(name="OclExpression104", type=Janus_essentialocl_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_OperationCallExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredOperation105: BinaryAssociation = BinaryAssociation(
    name="referredOperation105",
    ends={
        Property(name="Operation107", type=Janus_essentialocl_OperationCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_OperationCallExp106", type=Operation, multiplicity=Multiplicity(0, 1))
    }
)
in_80: BinaryAssociation = BinaryAssociation(
    name="in_80",
    ends={
        Property(name="OclExpression81", type=Janus_essentialocl_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_LetExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variable82: BinaryAssociation = BinaryAssociation(
    name="variable82",
    ends={
        Property(name="Variable83", type=Janus_essentialocl_LetExp, multiplicity=Multiplicity(1, 1)),
        Property(name="LetExp", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
initExpression84: BinaryAssociation = BinaryAssociation(
    name="initExpression84",
    ends={
        Property(name="OclExpression85", type=Janus_essentialocl_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_Variable", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
LetExp86: BinaryAssociation = BinaryAssociation(
    name="LetExp86",
    ends={
        Property(name="LetExp87", type=Janus_essentialocl_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="variable", type=LetExp, multiplicity=Multiplicity(0, 1))
    }
)
bindParameter88: BinaryAssociation = BinaryAssociation(
    name="bindParameter88",
    ends={
        Property(name="Parameter90", type=Janus_essentialocl_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_Variable89", type=Parameter_, multiplicity=Multiplicity(0, 1))
    }
)
computeOwner91: BinaryAssociation = BinaryAssociation(
    name="computeOwner91",
    ends={
        Property(name="ComputeExp", type=Janus_essentialocl_Variable, multiplicity=Multiplicity(1, 1)),
        Property(name="returnedElement", type=ComputeExp, multiplicity=Multiplicity(0, 1))
    }
)
referredProperty92: BinaryAssociation = BinaryAssociation(
    name="referredProperty92",
    ends={
        Property(name="Property93", type=Janus_essentialocl_PropertyCallExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_PropertyCallExp", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
referredVariable94: BinaryAssociation = BinaryAssociation(
    name="referredVariable94",
    ends={
        Property(name="Variable95", type=Janus_essentialocl_VariableExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_VariableExp", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
referredType96: BinaryAssociation = BinaryAssociation(
    name="referredType96",
    ends={
        Property(name="Type97", type=Janus_essentialocl_TypeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_TypeExp", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
part120: BinaryAssociation = BinaryAssociation(
    name="part120",
    ends={
        Property(name="TupleLiteralPart", type=Janus_essentialocl_TupleLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="TupleLiteralExp", type=TupleLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
bodyExpression121: BinaryAssociation = BinaryAssociation(
    name="bodyExpression121",
    ends={
        Property(name="OclExpression122", type=Janus_essentialocl_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_ExpressionInOcl", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
context123: BinaryAssociation = BinaryAssociation(
    name="context123",
    ends={
        Property(name="Variable125", type=Janus_essentialocl_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_ExpressionInOcl124", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resultVariable126: BinaryAssociation = BinaryAssociation(
    name="resultVariable126",
    ends={
        Property(name="Variable128", type=Janus_essentialocl_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_ExpressionInOcl127", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameterVariable129: BinaryAssociation = BinaryAssociation(
    name="parameterVariable129",
    ends={
        Property(name="Variable131", type=Janus_essentialocl_ExpressionInOcl, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_ExpressionInOcl130", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
result108: BinaryAssociation = BinaryAssociation(
    name="result108",
    ends={
        Property(name="Variable109", type=Janus_essentialocl_IterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_IterateExp", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
part110: BinaryAssociation = BinaryAssociation(
    name="part110",
    ends={
        Property(name="CollectionLiteralPart", type=Janus_essentialocl_CollectionLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="CollectionLiteralExp", type=CollectionLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
CollectionLiteralExp111: BinaryAssociation = BinaryAssociation(
    name="CollectionLiteralExp111",
    ends={
        Property(name="CollectionLiteralExp112", type=Janus_essentialocl_CollectionLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="part", type=CollectionLiteralExp, multiplicity=Multiplicity(1, 1))
    }
)
item113: BinaryAssociation = BinaryAssociation(
    name="item113",
    ends={
        Property(name="OclExpression114", type=Janus_essentialocl_CollectionItem, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_CollectionItem", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
first115: BinaryAssociation = BinaryAssociation(
    name="first115",
    ends={
        Property(name="OclExpression116", type=Janus_essentialocl_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_CollectionRange", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
last117: BinaryAssociation = BinaryAssociation(
    name="last117",
    ends={
        Property(name="OclExpression119", type=Janus_essentialocl_CollectionRange, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_CollectionRange118", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
part147: BinaryAssociation = BinaryAssociation(
    name="part147",
    ends={
        Property(name="OclExpression148", type=Janus_template_CollectionTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_template_CollectionTemplateExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredCollectionType149: BinaryAssociation = BinaryAssociation(
    name="referredCollectionType149",
    ends={
        Property(name="CollectionType", type=Janus_template_CollectionTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_template_CollectionTemplateExp150", type=CollectionType, multiplicity=Multiplicity(0, 1))
    }
)
match151: BinaryAssociation = BinaryAssociation(
    name="match151",
    ends={
        Property(name="OclExpression153", type=Janus_template_CollectionTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_template_CollectionTemplateExp152", type=OclExpression, multiplicity=Multiplicity(0, 1))
    }
)
objContainer154: BinaryAssociation = BinaryAssociation(
    name="objContainer154",
    ends={
        Property(name="ObjectTemplateExp", type=Janus_template_PropertyTemplateItem, multiplicity=Multiplicity(1, 1)),
        Property(name="part155", type=ObjectTemplateExp, multiplicity=Multiplicity(1, 1))
    }
)
value156: BinaryAssociation = BinaryAssociation(
    name="value156",
    ends={
        Property(name="OclExpression157", type=Janus_template_PropertyTemplateItem, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_template_PropertyTemplateItem", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
TupleLiteralExp132: BinaryAssociation = BinaryAssociation(
    name="TupleLiteralExp132",
    ends={
        Property(name="TupleLiteralExp134", type=Janus_essentialocl_TupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="part133", type=TupleLiteralExp, multiplicity=Multiplicity(0, 1))
    }
)
attribute135: BinaryAssociation = BinaryAssociation(
    name="attribute135",
    ends={
        Property(name="Property136", type=Janus_essentialocl_TupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_TupleLiteralPart", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
elementType137: BinaryAssociation = BinaryAssociation(
    name="elementType137",
    ends={
        Property(name="Type138", type=Janus_essentialocl_CollectionType, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_CollectionType", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
referredEnumLiteral139: BinaryAssociation = BinaryAssociation(
    name="referredEnumLiteral139",
    ends={
        Property(name="EnumerationLiteral140", type=Janus_essentialocl_EnumLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_essentialocl_EnumLiteralExp", type=EnumerationLiteral, multiplicity=Multiplicity(0, 1))
    }
)
bindsTo141: BinaryAssociation = BinaryAssociation(
    name="bindsTo141",
    ends={
        Property(name="Variable142", type=Janus_template_TemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_template_TemplateExp", type=Variable, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
where143: BinaryAssociation = BinaryAssociation(
    name="where143",
    ends={
        Property(name="OclExpression145", type=Janus_template_TemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_template_TemplateExp144", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
part146: BinaryAssociation = BinaryAssociation(
    name="part146",
    ends={
        Property(name="PropertyTemplateItem", type=Janus_template_ObjectTemplateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="objContainer", type=PropertyTemplateItem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referredVariable177: BinaryAssociation = BinaryAssociation(
    name="referredVariable177",
    ends={
        Property(name="Variable178", type=Janus_imperativeocl_VariableInitExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_VariableInitExp", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition179: BinaryAssociation = BinaryAssociation(
    name="condition179",
    ends={
        Property(name="OclExpression180", type=Janus_imperativeocl_WhileExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_WhileExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body181: BinaryAssociation = BinaryAssociation(
    name="body181",
    ends={
        Property(name="OclExpression183", type=Janus_imperativeocl_WhileExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_WhileExp182", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnedElement184: BinaryAssociation = BinaryAssociation(
    name="returnedElement184",
    ends={
        Property(name="Variable185", type=Janus_imperativeocl_ComputeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="computeOwner", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body186: BinaryAssociation = BinaryAssociation(
    name="body186",
    ends={
        Property(name="OclExpression187", type=Janus_imperativeocl_ComputeExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_ComputeExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
referredProperty158: BinaryAssociation = BinaryAssociation(
    name="referredProperty158",
    ends={
        Property(name="Property160", type=Janus_template_PropertyTemplateItem, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_template_PropertyTemplateItem159", type=Property_, multiplicity=Multiplicity(1, 1))
    }
)
target161: BinaryAssociation = BinaryAssociation(
    name="target161",
    ends={
        Property(name="Variable162", type=Janus_imperativeocl_ImperativeIterateExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_ImperativeIterateExp", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value163: BinaryAssociation = BinaryAssociation(
    name="value163",
    ends={
        Property(name="OclExpression164", type=Janus_imperativeocl_AssignExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_AssignExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left165: BinaryAssociation = BinaryAssociation(
    name="left165",
    ends={
        Property(name="OclExpression167", type=Janus_imperativeocl_AssignExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_AssignExp166", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
defaultValue168: BinaryAssociation = BinaryAssociation(
    name="defaultValue168",
    ends={
        Property(name="OclExpression170", type=Janus_imperativeocl_AssignExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_AssignExp169", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body171: BinaryAssociation = BinaryAssociation(
    name="body171",
    ends={
        Property(name="OclExpression172", type=Janus_imperativeocl_BlockExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_BlockExp", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
alternativePart173: BinaryAssociation = BinaryAssociation(
    name="alternativePart173",
    ends={
        Property(name="AltExp", type=Janus_imperativeocl_SwitchExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_SwitchExp", type=AltExp, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elsePart174: BinaryAssociation = BinaryAssociation(
    name="elsePart174",
    ends={
        Property(name="OclExpression176", type=Janus_imperativeocl_SwitchExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_SwitchExp175", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exceptBody204: BinaryAssociation = BinaryAssociation(
    name="exceptBody204",
    ends={
        Property(name="OclExpression206", type=Janus_imperativeocl_TryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_TryExp205", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
exception207: BinaryAssociation = BinaryAssociation(
    name="exception207",
    ends={
        Property(name="Type208", type=Janus_imperativeocl_RaiseExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_RaiseExp", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
element209: BinaryAssociation = BinaryAssociation(
    name="element209",
    ends={
        Property(name="OclExpression210", type=Janus_imperativeocl_TupleExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_TupleExp", type=OclExpression, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
base211: BinaryAssociation = BinaryAssociation(
    name="base211",
    ends={
        Property(name="Type212", type=Janus_imperativeocl_Typedef, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_Typedef", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
condition213: BinaryAssociation = BinaryAssociation(
    name="condition213",
    ends={
        Property(name="OclExpression215", type=Janus_imperativeocl_Typedef, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_Typedef214", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition188: BinaryAssociation = BinaryAssociation(
    name="condition188",
    ends={
        Property(name="OclExpression189", type=Janus_imperativeocl_AltExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_AltExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body190: BinaryAssociation = BinaryAssociation(
    name="body190",
    ends={
        Property(name="OclExpression192", type=Janus_imperativeocl_AltExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_AltExp191", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target193: BinaryAssociation = BinaryAssociation(
    name="target193",
    ends={
        Property(name="OclExpression194", type=Janus_imperativeocl_UnlinkExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_UnlinkExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
item195: BinaryAssociation = BinaryAssociation(
    name="item195",
    ends={
        Property(name="OclExpression197", type=Janus_imperativeocl_UnlinkExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_UnlinkExp196", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value198: BinaryAssociation = BinaryAssociation(
    name="value198",
    ends={
        Property(name="OclExpression199", type=Janus_imperativeocl_ReturnExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_ReturnExp", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tryBody200: BinaryAssociation = BinaryAssociation(
    name="tryBody200",
    ends={
        Property(name="OclExpression201", type=Janus_imperativeocl_TryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="tryBodyOwner", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
exception202: BinaryAssociation = BinaryAssociation(
    name="exception202",
    ends={
        Property(name="Type203", type=Janus_imperativeocl_TryExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_TryExp", type=Type, multiplicity=Multiplicity(0, 9999))
    }
)
condition232: BinaryAssociation = BinaryAssociation(
    name="condition232",
    ends={
        Property(name="OclExpression233", type=Janus_imperativeocl_LogExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_LogExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
element234: BinaryAssociation = BinaryAssociation(
    name="element234",
    ends={
        Property(name="Element236", type=Janus_imperativeocl_LogExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_LogExp235", type=Element, multiplicity=Multiplicity(0, 1))
    }
)
log237: BinaryAssociation = BinaryAssociation(
    name="log237",
    ends={
        Property(name="LogExp", type=Janus_imperativeocl_AssertExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_AssertExp", type=LogExp, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assertion238: BinaryAssociation = BinaryAssociation(
    name="assertion238",
    ends={
        Property(name="OclExpression240", type=Janus_imperativeocl_AssertExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_AssertExp239", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
instantiatedClass216: BinaryAssociation = BinaryAssociation(
    name="instantiatedClass216",
    ends={
        Property(name="Class217", type=Janus_imperativeocl_InstantiationExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_InstantiationExp", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
extent218: BinaryAssociation = BinaryAssociation(
    name="extent218",
    ends={
        Property(name="Variable220", type=Janus_imperativeocl_InstantiationExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_InstantiationExp219", type=Variable, multiplicity=Multiplicity(0, 1))
    }
)
argument221: BinaryAssociation = BinaryAssociation(
    name="argument221",
    ends={
        Property(name="OclExpression223", type=Janus_imperativeocl_InstantiationExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_InstantiationExp222", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keyType224: BinaryAssociation = BinaryAssociation(
    name="keyType224",
    ends={
        Property(name="Type225", type=Janus_imperativeocl_DictionaryType, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_DictionaryType", type=Type, multiplicity=Multiplicity(0, 1))
    }
)
part226: BinaryAssociation = BinaryAssociation(
    name="part226",
    ends={
        Property(name="DictLiteralPart", type=Janus_imperativeocl_DictLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_DictLiteralExp", type=DictLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key227: BinaryAssociation = BinaryAssociation(
    name="key227",
    ends={
        Property(name="OclExpression228", type=Janus_imperativeocl_DictLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_DictLiteralPart", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
value229: BinaryAssociation = BinaryAssociation(
    name="value229",
    ends={
        Property(name="OclExpression231", type=Janus_imperativeocl_DictLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_DictLiteralPart230", type=OclExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition241: BinaryAssociation = BinaryAssociation(
    name="condition241",
    ends={
        Property(name="OclExpression242", type=Janus_imperativeocl_ImperativeLoopExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_ImperativeLoopExp", type=OclExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
target243: BinaryAssociation = BinaryAssociation(
    name="target243",
    ends={
        Property(name="Variable244", type=Janus_imperativeocl_CollectorExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_CollectorExp", type=Variable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable245: BinaryAssociation = BinaryAssociation(
    name="variable245",
    ends={
        Property(name="Variable246", type=Janus_imperativeocl_UnpackExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_UnpackExp", type=Variable, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
elementType247: BinaryAssociation = BinaryAssociation(
    name="elementType247",
    ends={
        Property(name="Type248", type=Janus_imperativeocl_AnonymousTupleType, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_AnonymousTupleType", type=Type, multiplicity=Multiplicity(0, 9999))
    }
)
part249: BinaryAssociation = BinaryAssociation(
    name="part249",
    ends={
        Property(name="AnonymousTupleLiteralPart", type=Janus_imperativeocl_AnonymousTupleLiteralExp, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_AnonymousTupleLiteralExp", type=AnonymousTupleLiteralPart, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value250: BinaryAssociation = BinaryAssociation(
    name="value250",
    ends={
        Property(name="OclExpression251", type=Janus_imperativeocl_AnonymousTupleLiteralPart, multiplicity=Multiplicity(1, 1)),
        Property(name="Janus_imperativeocl_AnonymousTupleLiteralPart", type=OclExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_Janus_emof_DataType_Type = Generalization(general=Type, specific=Janus_emof_DataType)
gen_Janus_emof_Element_Object = Generalization(general=Object, specific=Janus_emof_Element)
gen_Janus_emof_Tag_Element = Generalization(general=Element, specific=Janus_emof_Tag)
gen_Janus_emof_Class_Type = Generalization(general=Type, specific=Janus_emof_Class)
gen_Janus_emof_Parameter_emof_MultiplicityElement = Generalization(general=emof_MultiplicityElement, specific=Janus_emof_Parameter)
gen_Janus_emof_Parameter_emof_TypedElement = Generalization(general=emof_TypedElement, specific=Janus_emof_Parameter)
gen_Janus_emof_EnumerationLiteral_NamedElement = Generalization(general=NamedElement, specific=Janus_emof_EnumerationLiteral)
gen_Janus_emof_Property_emof_MultiplicityElement = Generalization(general=emof_MultiplicityElement, specific=Janus_emof_Property)
gen_Janus_emof_Property_emof_TypedElement = Generalization(general=emof_TypedElement, specific=Janus_emof_Property)
gen_Janus_emof_Enumeration_DataType = Generalization(general=DataType, specific=Janus_emof_Enumeration)
gen_Janus_emof_NamedElement_Element = Generalization(general=Element, specific=Janus_emof_NamedElement)
gen_Janus_emof_Extent_Object = Generalization(general=Object, specific=Janus_emof_Extent)
gen_Janus_emof_Operation_emof_MultiplicityElement = Generalization(general=emof_MultiplicityElement, specific=Janus_emof_Operation)
gen_Janus_emof_Operation_emof_TypedElement = Generalization(general=emof_TypedElement, specific=Janus_emof_Operation)
gen_Janus_emof_Package_NamedElement = Generalization(general=NamedElement, specific=Janus_emof_Package)
gen_Janus_emof_Type_NamedElement = Generalization(general=NamedElement, specific=Janus_emof_Type)
gen_Janus_JTL_Domain_NamedElement = Generalization(general=NamedElement, specific=Janus_JTL_Domain)
gen_Janus_JTL_Model_NamedElement = Generalization(general=NamedElement, specific=Janus_JTL_Model)
gen_Janus_emof_TypedElement_NamedElement = Generalization(general=NamedElement, specific=Janus_emof_TypedElement)
gen_Janus_emof_PrimitiveType_DataType = Generalization(general=DataType, specific=Janus_emof_PrimitiveType)
gen_Janus_emof_URIExtent_Extent = Generalization(general=Extent, specific=Janus_emof_URIExtent)
gen_Janus_emof_Comment_Element = Generalization(general=Element, specific=Janus_emof_Comment)
gen_Janus_JTL_Transformation_emof_Class = Generalization(general=emof_Class, specific=Janus_JTL_Transformation)
gen_Janus_JTL_Transformation_emof_Package = Generalization(general=emof_Package, specific=Janus_JTL_Transformation)
gen_Janus_JTL_Relation_NamedElement = Generalization(general=NamedElement, specific=Janus_JTL_Relation)
gen_Janus_essentialocl_OclExpression_TypedElement = Generalization(general=TypedElement, specific=Janus_essentialocl_OclExpression)
gen_Janus_essentialocl_UnlimitedNaturalExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=Janus_essentialocl_UnlimitedNaturalExp)
gen_Janus_essentialocl_IfExp_OclExpression = Generalization(general=OclExpression, specific=Janus_essentialocl_IfExp)
gen_Janus_JTL_Pattern_Element = Generalization(general=Element, specific=Janus_JTL_Pattern)
gen_Janus_JTL_Predicate_Element = Generalization(general=Element, specific=Janus_JTL_Predicate)
gen_Janus_essentialocl_BooleanLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=Janus_essentialocl_BooleanLiteralExp)
gen_Janus_essentialocl_CallExp_OclExpression = Generalization(general=OclExpression, specific=Janus_essentialocl_CallExp)
gen_Janus_essentialocl_LoopExp_essentialocl_CallExp = Generalization(general=essentialocl_CallExp, specific=Janus_essentialocl_LoopExp)
gen_Janus_essentialocl_LoopExp_essentialocl_OclExpression = Generalization(general=essentialocl_OclExpression, specific=Janus_essentialocl_LoopExp)
gen_Janus_essentialocl_IteratorExp_LoopExp = Generalization(general=LoopExp, specific=Janus_essentialocl_IteratorExp)
gen_Janus_essentialocl_StringLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=Janus_essentialocl_StringLiteralExp)
gen_Janus_essentialocl_IntegerLiteralExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=Janus_essentialocl_IntegerLiteralExp)
gen_Janus_essentialocl_OperationCallExp_FeaturePropertyCall = Generalization(general=FeaturePropertyCall, specific=Janus_essentialocl_OperationCallExp)
gen_Janus_essentialocl_RealLiteralExp_NumericLiteralExp = Generalization(general=NumericLiteralExp, specific=Janus_essentialocl_RealLiteralExp)
gen_Janus_essentialocl_LetExp_OclExpression = Generalization(general=OclExpression, specific=Janus_essentialocl_LetExp)
gen_Janus_essentialocl_Variable_TypedElement = Generalization(general=TypedElement, specific=Janus_essentialocl_Variable)
gen_Janus_essentialocl_PropertyCallExp_FeaturePropertyCall = Generalization(general=FeaturePropertyCall, specific=Janus_essentialocl_PropertyCallExp)
gen_Janus_essentialocl_VariableExp_OclExpression = Generalization(general=OclExpression, specific=Janus_essentialocl_VariableExp)
gen_Janus_essentialocl_TypeExp_OclExpression = Generalization(general=OclExpression, specific=Janus_essentialocl_TypeExp)
gen_Janus_essentialocl_NullLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=Janus_essentialocl_NullLiteralExp)
gen_Janus_essentialocl_ExpressionInOcl_OpaqueExpression = Generalization(general=OpaqueExpression, specific=Janus_essentialocl_ExpressionInOcl)
gen_Janus_essentialocl_InvalidLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=Janus_essentialocl_InvalidLiteralExp)
gen_Janus_essentialocl_FeaturePropertyCall_CallExp = Generalization(general=CallExp, specific=Janus_essentialocl_FeaturePropertyCall)
gen_Janus_essentialocl_TupleLiteralPart_TypedElement = Generalization(general=TypedElement, specific=Janus_essentialocl_TupleLiteralPart)
gen_Janus_essentialocl_LiteralExp_OclExpression = Generalization(general=OclExpression, specific=Janus_essentialocl_LiteralExp)
gen_Janus_essentialocl_IterateExp_LoopExp = Generalization(general=LoopExp, specific=Janus_essentialocl_IterateExp)
gen_Janus_essentialocl_PrimitiveLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=Janus_essentialocl_PrimitiveLiteralExp)
gen_Janus_essentialocl_NumericLiteralExp_PrimitiveLiteralExp = Generalization(general=PrimitiveLiteralExp, specific=Janus_essentialocl_NumericLiteralExp)
gen_Janus_essentialocl_CollectionLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=Janus_essentialocl_CollectionLiteralExp)
gen_Janus_essentialocl_CollectionLiteralPart_TypedElement = Generalization(general=TypedElement, specific=Janus_essentialocl_CollectionLiteralPart)
gen_Janus_essentialocl_CollectionItem_CollectionLiteralPart = Generalization(general=CollectionLiteralPart, specific=Janus_essentialocl_CollectionItem)
gen_Janus_essentialocl_CollectionRange_CollectionLiteralPart = Generalization(general=CollectionLiteralPart, specific=Janus_essentialocl_CollectionRange)
gen_Janus_essentialocl_TupleLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=Janus_essentialocl_TupleLiteralExp)
gen_Janus_template_CollectionTemplateExp_TemplateExp = Generalization(general=TemplateExp, specific=Janus_template_CollectionTemplateExp)
gen_Janus_template_PropertyTemplateItem_Element = Generalization(general=Element, specific=Janus_template_PropertyTemplateItem)
gen_Janus_essentialocl_BagType_CollectionType = Generalization(general=CollectionType, specific=Janus_essentialocl_BagType)
gen_Janus_essentialocl_CollectionType_DataType = Generalization(general=DataType, specific=Janus_essentialocl_CollectionType)
gen_Janus_essentialocl_EnumLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=Janus_essentialocl_EnumLiteralExp)
gen_Janus_essentialocl_InvalidType_Type = Generalization(general=Type, specific=Janus_essentialocl_InvalidType)
gen_Janus_essentialocl_OrderedSetType_CollectionType = Generalization(general=CollectionType, specific=Janus_essentialocl_OrderedSetType)
gen_Janus_essentialocl_SequenceType_CollectionType = Generalization(general=CollectionType, specific=Janus_essentialocl_SequenceType)
gen_Janus_essentialocl_SetType_CollectionType = Generalization(general=CollectionType, specific=Janus_essentialocl_SetType)
gen_Janus_essentialocl_TupleType_emof_Class = Generalization(general=emof_Class, specific=Janus_essentialocl_TupleType)
gen_Janus_essentialocl_TupleType_emof_DataType = Generalization(general=emof_DataType, specific=Janus_essentialocl_TupleType)
gen_Janus_essentialocl_VoidType_Type = Generalization(general=Type, specific=Janus_essentialocl_VoidType)
gen_Janus_essentialocl_AnyType_emof_Class = Generalization(general=emof_Class, specific=Janus_essentialocl_AnyType)
gen_Janus_essentialocl_AnyType_emof_Type = Generalization(general=emof_Type, specific=Janus_essentialocl_AnyType)
gen_Janus_template_TemplateExp_LiteralExp = Generalization(general=LiteralExp, specific=Janus_template_TemplateExp)
gen_Janus_template_ObjectTemplateExp_TemplateExp = Generalization(general=TemplateExp, specific=Janus_template_ObjectTemplateExp)
gen_Janus_imperativeocl_WhileExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=Janus_imperativeocl_WhileExp)
gen_Janus_imperativeocl_ComputeExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=Janus_imperativeocl_ComputeExp)
gen_Janus_imperativeocl_ImperativeIterateExp_ImperativeLoopExp = Generalization(general=ImperativeLoopExp, specific=Janus_imperativeocl_ImperativeIterateExp)
gen_Janus_imperativeocl_AssignExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=Janus_imperativeocl_AssignExp)
gen_Janus_imperativeocl_BlockExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=Janus_imperativeocl_BlockExp)
gen_Janus_imperativeocl_SwitchExp_essentialocl_CallExp = Generalization(general=essentialocl_CallExp, specific=Janus_imperativeocl_SwitchExp)
gen_Janus_imperativeocl_SwitchExp_imperativeocl_ImperativeExpression = Generalization(general=imperativeocl_ImperativeExpression, specific=Janus_imperativeocl_SwitchExp)
gen_Janus_imperativeocl_VariableInitExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=Janus_imperativeocl_VariableInitExp)
gen_Janus_imperativeocl_RaiseExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=Janus_imperativeocl_RaiseExp)
gen_Janus_imperativeocl_ContinueExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=Janus_imperativeocl_ContinueExp)
gen_Janus_imperativeocl_ForExp_ImperativeLoopExp = Generalization(general=ImperativeLoopExp, specific=Janus_imperativeocl_ForExp)
gen_Janus_imperativeocl_TupleExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=Janus_imperativeocl_TupleExp)
gen_Janus_imperativeocl_Typedef_Class = Generalization(general=Class_, specific=Janus_imperativeocl_Typedef)
gen_Janus_imperativeocl_AltExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=Janus_imperativeocl_AltExp)
gen_Janus_imperativeocl_UnlinkExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=Janus_imperativeocl_UnlinkExp)
gen_Janus_imperativeocl_ReturnExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=Janus_imperativeocl_ReturnExp)
gen_Janus_imperativeocl_BreakExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=Janus_imperativeocl_BreakExp)
gen_Janus_imperativeocl_TryExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=Janus_imperativeocl_TryExp)
gen_Janus_imperativeocl_LogExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=Janus_imperativeocl_LogExp)
gen_Janus_imperativeocl_AssertExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=Janus_imperativeocl_AssertExp)
gen_Janus_imperativeocl_InstantiationExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=Janus_imperativeocl_InstantiationExp)
gen_Janus_imperativeocl_DictionaryType_CollectionType = Generalization(general=CollectionType, specific=Janus_imperativeocl_DictionaryType)
gen_Janus_imperativeocl_DictLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=Janus_imperativeocl_DictLiteralExp)
gen_Janus_imperativeocl_DictLiteralPart_Element = Generalization(general=Element, specific=Janus_imperativeocl_DictLiteralPart)
gen_Janus_imperativeocl_TemplateParameterType_Type = Generalization(general=Type, specific=Janus_imperativeocl_TemplateParameterType)
gen_Janus_imperativeocl_ListType_CollectionType = Generalization(general=CollectionType, specific=Janus_imperativeocl_ListType)
gen_Janus_imperativeocl_ImperativeLoopExp_essentialocl_LoopExp = Generalization(general=essentialocl_LoopExp, specific=Janus_imperativeocl_ImperativeLoopExp)
gen_Janus_imperativeocl_ImperativeLoopExp_imperativeocl_ImperativeExpression = Generalization(general=imperativeocl_ImperativeExpression, specific=Janus_imperativeocl_ImperativeLoopExp)
gen_Janus_imperativeocl_CollectorExp_ImperativeLoopExp = Generalization(general=ImperativeLoopExp, specific=Janus_imperativeocl_CollectorExp)
gen_Janus_imperativeocl_ImperativeExpression_OclExpression = Generalization(general=OclExpression, specific=Janus_imperativeocl_ImperativeExpression)
gen_Janus_imperativeocl_UnpackExp_ImperativeExpression = Generalization(general=ImperativeExpression, specific=Janus_imperativeocl_UnpackExp)
gen_Janus_imperativeocl_AnonymousTupleType_Class = Generalization(general=Class_, specific=Janus_imperativeocl_AnonymousTupleType)
gen_Janus_imperativeocl_AnonymousTupleLiteralExp_LiteralExp = Generalization(general=LiteralExp, specific=Janus_imperativeocl_AnonymousTupleLiteralExp)
gen_Janus_imperativeocl_AnonymousTupleLiteralPart_Element = Generalization(general=Element, specific=Janus_imperativeocl_AnonymousTupleLiteralPart)

# Domain Model
domain_model = DomainModel(
    name="Janus",
    types={Class_, Janus_emof_DataType, Janus_emof_Element, Object, Tag, Comment, Janus_emof_Tag, Element, Janus_emof_Class, Type, Property_, Operation, Janus_emof_Parameter, Janus_emof_EnumerationLiteral, Enumeration_, Janus_emof_Property, Janus_emof_Enumeration, DataType, EnumerationLiteral, Janus_emof_NamedElement, Janus_emof_Extent, Janus_emof_Object, Janus_emof_Operation, emof_MultiplicityElement, emof_TypedElement, Parameter_, Janus_emof_MultiplicityElement, Janus_emof_Package, NamedElement, Package, Janus_emof_Type, Variable, Janus_JTL_Domain, Janus_JTL_Model, Janus_emof_TypedElement, Janus_emof_PrimitiveType, Janus_emof_URIExtent, Extent, Janus_emof_Comment, Janus_JTL_Transformation, emof_Class, emof_Package, Model, Relation, Janus_JTL_Relation, Transformation, Domain, Pattern, Janus_essentialocl_OclExpression, TypedElement, TryExp, Janus_essentialocl_UnlimitedNaturalExp, NumericLiteralExp, Janus_essentialocl_IfExp, Janus_JTL_Pattern, Predicate, TemplateExp, Janus_JTL_Predicate, OclExpression, Janus_essentialocl_BooleanLiteralExp, PrimitiveLiteralExp, Janus_essentialocl_CallExp, essentialocl_CallExp, essentialocl_OclExpression, Janus_essentialocl_IteratorExp, LoopExp, Janus_essentialocl_StringLiteralExp, Janus_essentialocl_IntegerLiteralExp, Janus_essentialocl_OperationCallExp, Janus_essentialocl_RealLiteralExp, Janus_essentialocl_LetExp, Janus_essentialocl_Variable, LetExp, ComputeExp, Janus_essentialocl_PropertyCallExp, FeaturePropertyCall, Janus_essentialocl_VariableExp, Janus_essentialocl_TypeExp, Janus_essentialocl_LoopExp, TupleLiteralPart, Janus_essentialocl_NullLiteralExp, Janus_essentialocl_ExpressionInOcl, OpaqueExpression, Janus_essentialocl_OpaqueExpression, Janus_essentialocl_InvalidLiteralExp, Janus_essentialocl_FeaturePropertyCall, CallExp, Janus_essentialocl_TupleLiteralPart, TupleLiteralExp, Janus_essentialocl_LiteralExp, Janus_essentialocl_IterateExp, Janus_essentialocl_PrimitiveLiteralExp, LiteralExp, Janus_essentialocl_NumericLiteralExp, Janus_essentialocl_CollectionLiteralExp, CollectionLiteralPart, Janus_essentialocl_CollectionLiteralPart, CollectionLiteralExp, Janus_essentialocl_CollectionItem, Janus_essentialocl_CollectionRange, Janus_essentialocl_TupleLiteralExp, Janus_template_CollectionTemplateExp, Janus_template_PropertyTemplateItem, ObjectTemplateExp, Janus_essentialocl_BagType, CollectionType, Janus_essentialocl_CollectionType, Janus_essentialocl_EnumLiteralExp, Janus_essentialocl_InvalidType, Janus_essentialocl_OrderedSetType, Janus_essentialocl_SequenceType, Janus_essentialocl_SetType, Janus_essentialocl_TupleType, emof_DataType, Janus_essentialocl_VoidType, Janus_essentialocl_AnyType, emof_Type, Janus_template_TemplateExp, Janus_template_ObjectTemplateExp, PropertyTemplateItem, Janus_imperativeocl_WhileExp, Janus_imperativeocl_ComputeExp, Janus_imperativeocl_ImperativeIterateExp, ImperativeLoopExp, Janus_imperativeocl_AssignExp, ImperativeExpression, Janus_imperativeocl_BlockExp, Janus_imperativeocl_SwitchExp, imperativeocl_ImperativeExpression, AltExp, Janus_imperativeocl_VariableInitExp, Janus_imperativeocl_RaiseExp, Janus_imperativeocl_ContinueExp, Janus_imperativeocl_ForExp, Janus_imperativeocl_TupleExp, Janus_imperativeocl_Typedef, Janus_imperativeocl_AltExp, Janus_imperativeocl_UnlinkExp, Janus_imperativeocl_ReturnExp, Janus_imperativeocl_BreakExp, Janus_imperativeocl_TryExp, Janus_imperativeocl_LogExp, Janus_imperativeocl_AssertExp, LogExp, Janus_imperativeocl_InstantiationExp, Janus_imperativeocl_DictionaryType, Janus_imperativeocl_DictLiteralExp, DictLiteralPart, Janus_imperativeocl_DictLiteralPart, Janus_imperativeocl_TemplateParameterType, Janus_imperativeocl_ListType, Janus_imperativeocl_ImperativeLoopExp, essentialocl_LoopExp, Janus_imperativeocl_CollectorExp, Janus_imperativeocl_ImperativeExpression, Janus_imperativeocl_UnpackExp, Janus_imperativeocl_AnonymousTupleType, Janus_imperativeocl_AnonymousTupleLiteralExp, AnonymousTupleLiteralPart, Janus_imperativeocl_AnonymousTupleLiteralPart, CollectionKind, SeverityKind},
    associations={superClass2, tag4, ownedComment5, element6, ownedAttribute0, ownedOperation1, package15, operation17, enumeration19, Class20, opposite22, ownedLiteral7, class_8, ownedParameter10, raisedException11, ownedType12, nestedPackage14, when34, variable36, relation37, pattern39, model41, rootVariable44, transformation47, type24, annotatedElement26, modelParameter27, relation28, transformation30, domain31, where33, source69, tryBodyOwner71, condition72, thenExpression74, elseExpression77, usedPackage49, dependsOn51, whereOwner54, whenOwner56, predicate58, bindsTo59, templateExpression61, domain63, pattern66, conditionExpression68, body98, iterator100, argument103, referredOperation105, in_80, variable82, initExpression84, LetExp86, bindParameter88, computeOwner91, referredProperty92, referredVariable94, referredType96, part120, bodyExpression121, context123, resultVariable126, parameterVariable129, result108, part110, CollectionLiteralExp111, item113, first115, last117, part147, referredCollectionType149, match151, objContainer154, value156, TupleLiteralExp132, attribute135, elementType137, referredEnumLiteral139, bindsTo141, where143, part146, referredVariable177, condition179, body181, returnedElement184, body186, referredProperty158, target161, value163, left165, defaultValue168, body171, alternativePart173, elsePart174, exceptBody204, exception207, element209, base211, condition213, condition188, body190, target193, item195, value198, tryBody200, exception202, condition232, element234, log237, assertion238, instantiatedClass216, extent218, argument221, keyType224, part226, key227, value229, condition241, target243, variable245, elementType247, part249, value250},
    generalizations={gen_Janus_emof_DataType_Type, gen_Janus_emof_Element_Object, gen_Janus_emof_Tag_Element, gen_Janus_emof_Class_Type, gen_Janus_emof_Parameter_emof_MultiplicityElement, gen_Janus_emof_Parameter_emof_TypedElement, gen_Janus_emof_EnumerationLiteral_NamedElement, gen_Janus_emof_Property_emof_MultiplicityElement, gen_Janus_emof_Property_emof_TypedElement, gen_Janus_emof_Enumeration_DataType, gen_Janus_emof_NamedElement_Element, gen_Janus_emof_Extent_Object, gen_Janus_emof_Operation_emof_MultiplicityElement, gen_Janus_emof_Operation_emof_TypedElement, gen_Janus_emof_Package_NamedElement, gen_Janus_emof_Type_NamedElement, gen_Janus_JTL_Domain_NamedElement, gen_Janus_JTL_Model_NamedElement, gen_Janus_emof_TypedElement_NamedElement, gen_Janus_emof_PrimitiveType_DataType, gen_Janus_emof_URIExtent_Extent, gen_Janus_emof_Comment_Element, gen_Janus_JTL_Transformation_emof_Class, gen_Janus_JTL_Transformation_emof_Package, gen_Janus_JTL_Relation_NamedElement, gen_Janus_essentialocl_OclExpression_TypedElement, gen_Janus_essentialocl_UnlimitedNaturalExp_NumericLiteralExp, gen_Janus_essentialocl_IfExp_OclExpression, gen_Janus_JTL_Pattern_Element, gen_Janus_JTL_Predicate_Element, gen_Janus_essentialocl_BooleanLiteralExp_PrimitiveLiteralExp, gen_Janus_essentialocl_CallExp_OclExpression, gen_Janus_essentialocl_LoopExp_essentialocl_CallExp, gen_Janus_essentialocl_LoopExp_essentialocl_OclExpression, gen_Janus_essentialocl_IteratorExp_LoopExp, gen_Janus_essentialocl_StringLiteralExp_PrimitiveLiteralExp, gen_Janus_essentialocl_IntegerLiteralExp_NumericLiteralExp, gen_Janus_essentialocl_OperationCallExp_FeaturePropertyCall, gen_Janus_essentialocl_RealLiteralExp_NumericLiteralExp, gen_Janus_essentialocl_LetExp_OclExpression, gen_Janus_essentialocl_Variable_TypedElement, gen_Janus_essentialocl_PropertyCallExp_FeaturePropertyCall, gen_Janus_essentialocl_VariableExp_OclExpression, gen_Janus_essentialocl_TypeExp_OclExpression, gen_Janus_essentialocl_NullLiteralExp_LiteralExp, gen_Janus_essentialocl_ExpressionInOcl_OpaqueExpression, gen_Janus_essentialocl_InvalidLiteralExp_LiteralExp, gen_Janus_essentialocl_FeaturePropertyCall_CallExp, gen_Janus_essentialocl_TupleLiteralPart_TypedElement, gen_Janus_essentialocl_LiteralExp_OclExpression, gen_Janus_essentialocl_IterateExp_LoopExp, gen_Janus_essentialocl_PrimitiveLiteralExp_LiteralExp, gen_Janus_essentialocl_NumericLiteralExp_PrimitiveLiteralExp, gen_Janus_essentialocl_CollectionLiteralExp_LiteralExp, gen_Janus_essentialocl_CollectionLiteralPart_TypedElement, gen_Janus_essentialocl_CollectionItem_CollectionLiteralPart, gen_Janus_essentialocl_CollectionRange_CollectionLiteralPart, gen_Janus_essentialocl_TupleLiteralExp_LiteralExp, gen_Janus_template_CollectionTemplateExp_TemplateExp, gen_Janus_template_PropertyTemplateItem_Element, gen_Janus_essentialocl_BagType_CollectionType, gen_Janus_essentialocl_CollectionType_DataType, gen_Janus_essentialocl_EnumLiteralExp_LiteralExp, gen_Janus_essentialocl_InvalidType_Type, gen_Janus_essentialocl_OrderedSetType_CollectionType, gen_Janus_essentialocl_SequenceType_CollectionType, gen_Janus_essentialocl_SetType_CollectionType, gen_Janus_essentialocl_TupleType_emof_Class, gen_Janus_essentialocl_TupleType_emof_DataType, gen_Janus_essentialocl_VoidType_Type, gen_Janus_essentialocl_AnyType_emof_Class, gen_Janus_essentialocl_AnyType_emof_Type, gen_Janus_template_TemplateExp_LiteralExp, gen_Janus_template_ObjectTemplateExp_TemplateExp, gen_Janus_imperativeocl_WhileExp_ImperativeExpression, gen_Janus_imperativeocl_ComputeExp_ImperativeExpression, gen_Janus_imperativeocl_ImperativeIterateExp_ImperativeLoopExp, gen_Janus_imperativeocl_AssignExp_ImperativeExpression, gen_Janus_imperativeocl_BlockExp_ImperativeExpression, gen_Janus_imperativeocl_SwitchExp_essentialocl_CallExp, gen_Janus_imperativeocl_SwitchExp_imperativeocl_ImperativeExpression, gen_Janus_imperativeocl_VariableInitExp_ImperativeExpression, gen_Janus_imperativeocl_RaiseExp_ImperativeExpression, gen_Janus_imperativeocl_ContinueExp_ImperativeExpression, gen_Janus_imperativeocl_ForExp_ImperativeLoopExp, gen_Janus_imperativeocl_TupleExp_ImperativeExpression, gen_Janus_imperativeocl_Typedef_Class, gen_Janus_imperativeocl_AltExp_ImperativeExpression, gen_Janus_imperativeocl_UnlinkExp_ImperativeExpression, gen_Janus_imperativeocl_ReturnExp_ImperativeExpression, gen_Janus_imperativeocl_BreakExp_ImperativeExpression, gen_Janus_imperativeocl_TryExp_ImperativeExpression, gen_Janus_imperativeocl_LogExp_ImperativeExpression, gen_Janus_imperativeocl_AssertExp_ImperativeExpression, gen_Janus_imperativeocl_InstantiationExp_ImperativeExpression, gen_Janus_imperativeocl_DictionaryType_CollectionType, gen_Janus_imperativeocl_DictLiteralExp_LiteralExp, gen_Janus_imperativeocl_DictLiteralPart_Element, gen_Janus_imperativeocl_TemplateParameterType_Type, gen_Janus_imperativeocl_ListType_CollectionType, gen_Janus_imperativeocl_ImperativeLoopExp_essentialocl_LoopExp, gen_Janus_imperativeocl_ImperativeLoopExp_imperativeocl_ImperativeExpression, gen_Janus_imperativeocl_CollectorExp_ImperativeLoopExp, gen_Janus_imperativeocl_ImperativeExpression_OclExpression, gen_Janus_imperativeocl_UnpackExp_ImperativeExpression, gen_Janus_imperativeocl_AnonymousTupleType_Class, gen_Janus_imperativeocl_AnonymousTupleLiteralExp_LiteralExp, gen_Janus_imperativeocl_AnonymousTupleLiteralPart_Element},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)